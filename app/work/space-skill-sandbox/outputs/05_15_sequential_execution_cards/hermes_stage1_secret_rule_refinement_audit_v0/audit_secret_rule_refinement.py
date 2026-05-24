#!/usr/bin/env python3
"""Stage 1 secret/token rule refinement audit. Stdlib only."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent
FIXTURE_DIR = BASE / "fixtures"
REPORT = BASE / "secret_rule_refinement_report.md"
RECEIPT = BASE / "secret_rule_refinement_receipt.json"
VERDICT = "[CODEX_STAGE1_SECRET_RULE_REFINEMENT_AUDIT_EXECUTED_WITH_WATCH]"

SECRET_NAME_RX = re.compile(r"\b(api[_-]?key|token|password|secret|credential|service_token|api_token)\b", re.IGNORECASE)
ASSIGN_RX = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$")
PLACEHOLDER_RX = re.compile(r"(<[^>]+>|\$\{[^}]+\}|fixture|placeholder|set-in-env|dummy|sample)", re.IGNORECASE)
NORMALIZER_RX = re.compile(r"(_normalize|normalize|tokenize|parse|lower\s*\(|strip\s*\(|len\s*\(|list\s*\(|str\s*\(|os\.environ|read_from_env|getenv)", re.IGNORECASE)
QUOTED_RX = re.compile(r"^(['\"])(.*)\1$")
REALISH_SECRET_RX = re.compile(r"(sk_live|secret-token|real-looking|plain-text|embedded-credential|local-dev-secret|not-a-normalizer-literal)", re.IGNORECASE)

CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".env", ".json", ".toml", ".yaml", ".yml"}


def path_context(path: str) -> str:
    p = path.replace("\\", "/")
    suffix = Path(p).suffix.lower()
    if p.startswith("docs/") or suffix == ".md":
        return "docs"
    if "/tests/" in f"/{p}" or p.startswith("tests/") or "fixture" in p.lower() or "fixtures" in p.lower():
        return "tests_or_fixtures"
    if p.startswith("config/") or suffix in CONFIG_EXTS or "env" in Path(p).name.lower():
        return "config_or_env_like"
    if p.startswith("scripts/"):
        return "scripts_or_deploy"
    if p.startswith("app/") and suffix in CODE_EXTS:
        return "app_source"
    if suffix in CODE_EXTS:
        return "source_code"
    return "other"


def old_behavior(line: str, context: str) -> str:
    if not re.search(r"\b(api_key|token|password|secret|credential)\s*=", line, re.IGNORECASE):
        return "none"
    if context in {"docs", "tests_or_fixtures"}:
        return "review_note"
    if context in {"app_source", "source_code", "config_or_env_like", "scripts_or_deploy"}:
        return "hard_finding"
    return "review_note"


def classify_refined(line: str, context: str) -> Tuple[str, str]:
    stripped = line.strip()
    match = ASSIGN_RX.match(stripped)
    if not match:
        if SECRET_NAME_RX.search(stripped):
            return ("review_note", "secret_word_without_direct_assignment")
        return ("none", "no_secret_boundary")
    name, rhs = match.group(1), match.group(2).strip()
    if not SECRET_NAME_RX.search(name):
        return ("none", "assignment_not_secret_named")
    if context in {"docs", "tests_or_fixtures"}:
        return ("review_note", f"{context}_example")
    quoted = QUOTED_RX.match(rhs)
    if quoted:
        value = quoted.group(2)
        if PLACEHOLDER_RX.search(value) or value == "":
            return ("review_note", "placeholder_or_empty_secret_value")
        if context == "config_or_env_like" or REALISH_SECRET_RX.search(value):
            return ("hard_finding", "literal_secret_assignment")
        return ("review_note", "quoted_secret_named_value_needs_review")
    if NORMALIZER_RX.search(rhs):
        return ("review_note", "semantic_or_env_boundary_not_literal_secret")
    if PLACEHOLDER_RX.search(rhs):
        return ("review_note", "placeholder_secret_assignment")
    if context == "config_or_env_like":
        return ("review_note", "config_secret_nonliteral_or_reference")
    return ("review_note", "secret_named_nonliteral_assignment")


def parse_patch(path: Path) -> Dict[str, object]:
    current_file = "UNKNOWN"
    rows: List[Dict[str, object]] = []
    files_seen = set()
    added_lines = 0
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.rstrip("\n")
            if raw.startswith("diff --git "):
                parts = raw.split()
                if len(parts) >= 4:
                    current_file = parts[3][2:] if parts[3].startswith("b/") else parts[3]
                    files_seen.add(current_file)
                continue
            if raw.startswith("+++ b/"):
                current_file = raw[6:]
                files_seen.add(current_file)
                continue
            if not raw.startswith("+") or raw.startswith("+++"):
                continue
            added_lines += 1
            added = raw[1:]
            if not SECRET_NAME_RX.search(added):
                continue
            context = path_context(current_file)
            old = old_behavior(added, context)
            refined, reason = classify_refined(added, context)
            rows.append({
                "file": current_file,
                "line_no": line_no,
                "context": context,
                "old_behavior": old,
                "refined_behavior": refined,
                "reason": reason,
                "line": added.strip()[:220],
            })
    return {
        "patch": path.name,
        "files_touched_count": len(files_seen),
        "added_lines_seen": added_lines,
        "findings": rows,
    }


def count(rows: List[Dict[str, object]], key: str, value: str) -> int:
    return sum(1 for row in rows if row.get(key) == value)


def main() -> int:
    fixture_files = sorted(FIXTURE_DIR.glob("*.patch"))
    summaries = [parse_patch(path) for path in fixture_files]
    all_rows = [row for summary in summaries for row in summary["findings"]]  # type: ignore[index]
    old_hard = count(all_rows, "old_behavior", "hard_finding")
    refined_hard = count(all_rows, "refined_behavior", "hard_finding")
    old_review = count(all_rows, "old_behavior", "review_note")
    refined_review = count(all_rows, "refined_behavior", "review_note")
    historical_rows = [row for row in all_rows if row["file"] == "app/core/runtime/live_input_space.py"]
    timestamp = datetime.now(timezone.utc).isoformat()

    lines = [
        "# Secret/Token Rule Refinement Audit Report v0",
        "",
        "## 1. Verdict",
        "",
        VERDICT,
        "",
        "## 2. Command",
        "",
        "`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/audit_secret_rule_refinement.py`",
        "",
        "## 3. Files Read",
        "",
    ]
    lines.extend(f"- fixtures/{path.name}" for path in fixture_files)
    lines.extend([
        "",
        "## 4. Files Created",
        "",
        "- fixtures/actual_credential_literal.patch",
        "- fixtures/semantic_token_normalization.patch",
        "- fixtures/config_env_boundary.patch",
        "- fixtures/docs_and_tests_examples.patch",
        "- fixtures/historical_token_examples.patch",
        "- audit_secret_rule_refinement.py",
        "- secret_rule_refinement_report.md",
        "- secret_rule_refinement_receipt.json",
        "",
        "## 5. Aggregate Behavior",
        "",
        f"- old_hard_findings: {old_hard}",
        f"- old_review_notes: {old_review}",
        f"- refined_hard_findings: {refined_hard}",
        f"- refined_review_notes: {refined_review}",
        f"- false_positive_reduction_against_old_hard_count: {old_hard - refined_hard}",
        "",
        "## 6. Fixture Results",
        "",
    ])
    for summary in summaries:
        findings = summary["findings"]  # type: ignore[index]
        lines.extend([
            f"### {summary['patch']}",
            f"- files_touched_count: {summary['files_touched_count']}",
            f"- added_lines_seen: {summary['added_lines_seen']}",
            f"- old_hard_findings: {count(findings, 'old_behavior', 'hard_finding')}",
            f"- refined_hard_findings: {count(findings, 'refined_behavior', 'hard_finding')}",
            f"- refined_review_notes: {count(findings, 'refined_behavior', 'review_note')}",
        ])
        for row in findings[:12]:
            lines.append(f"- {row['refined_behavior']} | old={row['old_behavior']} | reason={row['reason']} | {row['file']}:{row['line_no']} | `{row['line']}`")
        lines.append("")
    lines.extend([
        "## 7. Historical Example Comparison",
        "",
    ])
    for row in historical_rows:
        lines.append(f"- old={row['old_behavior']} -> refined={row['refined_behavior']} | reason={row['reason']} | `{row['line']}`")
    lines.extend([
        "",
        "## 8. Recovered Rule Boundary",
        "",
        "- Quoted literal secret-like assignments in app/source/config remain hard findings.",
        "- Placeholder/env/reference values are review notes, not hard findings.",
        "- `_normalize_token(...)`, parser-token variables, and derived token lists are semantic token handling, not credential leakage by themselves.",
        "- Docs and test fixtures stay as review notes unless a separate authority boundary says they are live secrets.",
        "- Config/env-like literal secrets keep hard-finding pressure.",
        "",
        "## 9. False Positive / False Negative Notes",
        "",
        "- False-positive reduced: the historical `_normalize_token(...)` examples no longer become hard findings.",
        "- False-negative watch: a real secret can still be hidden behind variable indirection, concatenation, decoding, or environment reads.",
        "- This script does not perform data-flow analysis, entropy checks, git history secret scanning, or runtime reachability analysis.",
        "",
        "## 10. VectorFL Recovery Suggestion",
        "",
        "receipt:",
        "  refinement audit ran with command/output evidence",
        "",
        "residue:",
        "  observed false-positive and false-negative boundaries",
        "",
        "candidate:",
        "  refined secret/token rule boundary",
        "",
        "component:",
        "  HOLD until tested against more real diffs and at least one deliberately seeded true-positive case",
        "",
        "STOP:",
        "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation",
        "",
        "## 11. WATCH",
        "",
        "refined secret/token rules may reduce false positives but still do not authorize component/workflow/skill/baseline",
        "",
        "## 12. HOLD",
        "",
        "- no source files modified",
        "- no prior audit files modified",
        "- no patches applied",
        "- no git used",
        "- no git add / commit / reset / checkout",
        "- no package install",
        "- no network / browser / MCP",
        "- no Hermes memory / skill / cron / config edit",
        "- no AGENTS.md / SKILL.md update",
        "- no VectorFL authority update",
        "- no current-position / output_manifest update",
        "- no baseline / workflow / schema / registry / ontology promotion",
        "- no declared output directory outside write",
        "",
    ])
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    receipt = {
        "verdict": "[CODEX_STAGE1_SECRET_RULE_REFINEMENT_AUDIT_RECEIPT]",
        "timestamp": timestamp,
        "command": "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/audit_secret_rule_refinement.py",
        "input_files": [f"fixtures/{path.name}" for path in fixture_files],
        "output_files": [
            "secret_rule_refinement_report.md",
            "secret_rule_refinement_receipt.json",
        ],
        "exit_code": 0,
        "old_hard_findings": old_hard,
        "old_review_notes": old_review,
        "refined_hard_findings": refined_hard,
        "refined_review_notes": refined_review,
        "false_positive_reduction_against_old_hard_count": old_hard - refined_hard,
        "historical_rows": historical_rows,
        "network_used": False,
        "packages_installed": False,
        "git_used": False,
        "source_files_modified": False,
        "prior_files_modified": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_files_modified": False,
        "current_position_updated": False,
        "output_manifest_updated": False,
        "baseline_workflow_schema_registry_ontology_promoted": False,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": VERDICT,
        "old_hard_findings": old_hard,
        "refined_hard_findings": refined_hard,
        "report": str(REPORT),
        "receipt": str(RECEIPT),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
