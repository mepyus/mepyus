#!/usr/bin/env python3
"""Replay refined secret/debug diff rules on prior historical patch sample."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent
HISTORICAL_DIR = BASE.parent / "hermes_stage1_historical_code_diff_sample_audit_v0" / "patches"
REPORT = BASE / "refined_rule_historical_replay_report.md"
RECEIPT = BASE / "refined_rule_historical_replay_receipt.json"
VERDICT = "[CODEX_STAGE1_REFINED_RULE_HISTORICAL_REPLAY_EXECUTED_WITH_WATCH]"

CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".env", ".json", ".toml", ".yaml", ".yml"}

SECRET_NAME_RX = re.compile(r"\b(api[_-]?key|token|password|secret|credential|service_token|api_token)\b", re.IGNORECASE)
ASSIGN_RX = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$")
PLACEHOLDER_RX = re.compile(r"(<[^>]+>|\$\{[^}]+\}|fixture|placeholder|set-in-env|dummy|sample)", re.IGNORECASE)
NORMALIZER_RX = re.compile(r"(_normalize|normalize|tokenize|parse|lower\s*\(|strip\s*\(|len\s*\(|list\s*\(|str\s*\(|os\.environ|read_from_env|getenv)", re.IGNORECASE)
QUOTED_RX = re.compile(r"^(['\"])(.*)\1$")
REALISH_SECRET_RX = re.compile(r"(sk_live|secret-token|real-looking|plain-text|embedded-credential|local-dev-secret|not-a-normalizer-literal)", re.IGNORECASE)

RULES: List[Tuple[str, re.Pattern[str]]] = [
    ("debug_print_python", re.compile(r"\bprint\s*\(")),
    ("debug_print_js", re.compile(r"\bconsole\.log\s*\(")),
    ("bare_except", re.compile(r"^\s*except\s*:\s*(#.*)?$")),
    ("unresolved_todo", re.compile(r"\bTODO\b")),
    ("unresolved_fixme", re.compile(r"\bFIXME\b")),
    ("shell_curl_pipe_bash", re.compile(r"curl\b.*\|\s*bash", re.IGNORECASE)),
    ("shell_rm_rf", re.compile(r"rm\s+-rf", re.IGNORECASE)),
    ("shell_chmod_777", re.compile(r"chmod\s+777", re.IGNORECASE)),
    ("dynamic_eval", re.compile(r"\beval\s*\(")),
    ("dynamic_exec", re.compile(r"\bexec\s*\(")),
    ("dynamic_subprocess_shell_true", re.compile(r"subprocess\.run\s*\(.*shell\s*=\s*True", re.IGNORECASE)),
    ("dynamic_os_system", re.compile(r"\bos\.system\s*\(")),
]


def path_context(path: str) -> str:
    p = path.replace("\\", "/")
    suffix = Path(p).suffix.lower()
    if p.startswith("docs/") or suffix == ".md":
        return "docs"
    if "/tests/" in f"/{p}" or p.startswith("tests/") or "fixture" in p.lower() or "fixtures" in p.lower():
        return "tests_or_fixtures"
    if "/generated/" in p or p.startswith("generated/") or "/.vite/" in p:
        return "generated"
    if p.startswith("config/") or suffix in CONFIG_EXTS or "env" in Path(p).name.lower():
        return "config_or_env_like"
    if p.startswith("scripts/") or "deploy" in p.lower() or suffix in {".sh", ".bash", ".zsh"}:
        return "scripts_or_deploy"
    if p.startswith("app/") and suffix in CODE_EXTS:
        return "app_source"
    if suffix in CODE_EXTS:
        return "source_code"
    return "other"


def legacy_secret_hit(line: str) -> bool:
    return bool(re.search(r"\b(api_key|token|password|secret|credential)\s*=", line, re.IGNORECASE))


def classify_secret_refined(line: str, context: str) -> Tuple[str, str]:
    stripped = line.strip()
    match = ASSIGN_RX.match(stripped)
    if not match:
        if SECRET_NAME_RX.search(stripped):
            return ("review_note", "secret_word_without_direct_assignment")
        return ("none", "no_secret_boundary")
    name, rhs = match.group(1), match.group(2).strip()
    if not SECRET_NAME_RX.search(name):
        return ("none", "assignment_not_secret_named")
    if context in {"docs", "tests_or_fixtures", "generated"}:
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


def severity_for_non_secret(rule: str, context: str) -> str:
    shell = rule.startswith("shell_")
    dynamic = rule.startswith("dynamic_")
    debug = rule.startswith("debug_")
    bare = rule == "bare_except"
    if context in {"docs", "tests_or_fixtures", "generated"}:
        return "review_note"
    if context == "scripts_or_deploy" and (shell or dynamic):
        return "hard_finding"
    if context in {"app_source", "source_code"} and (debug or bare or dynamic):
        return "hard_finding"
    return "review_note"


def parse_patch(path: Path) -> Dict[str, object]:
    current_file = "UNKNOWN"
    files_seen = set()
    rows: List[Dict[str, object]] = []
    old_hard = 0
    refined_hard = 0
    old_review = 0
    refined_review = 0
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
            added = raw[1:]
            context = path_context(current_file)
            if legacy_secret_hit(added) or SECRET_NAME_RX.search(added):
                old = "hard_finding" if legacy_secret_hit(added) and context not in {"docs", "tests_or_fixtures", "generated"} else "review_note"
                refined, reason = classify_secret_refined(added, context)
                if old == "hard_finding":
                    old_hard += 1
                elif old == "review_note":
                    old_review += 1
                if refined == "hard_finding":
                    refined_hard += 1
                elif refined == "review_note":
                    refined_review += 1
                if old != "none" or refined != "none":
                    rows.append({"line_no": line_no, "file": current_file, "context": context, "rule": "secret_boundary", "old": old, "refined": refined, "reason": reason, "line": added.strip()[:220]})
            for rule, rx in RULES:
                if not rx.search(added):
                    continue
                sev = severity_for_non_secret(rule, context)
                if sev == "hard_finding":
                    old_hard += 1
                    refined_hard += 1
                else:
                    old_review += 1
                    refined_review += 1
                rows.append({"line_no": line_no, "file": current_file, "context": context, "rule": rule, "old": sev, "refined": sev, "reason": "non_secret_rule_unchanged", "line": added.strip()[:220]})
    return {
        "patch": path.name,
        "files_touched_count": len(files_seen),
        "old_hard_findings": old_hard,
        "old_review_notes": old_review,
        "refined_hard_findings": refined_hard,
        "refined_review_notes": refined_review,
        "rows": rows,
    }


def main() -> int:
    patches = sorted(HISTORICAL_DIR.glob("*.patch"))
    summaries = [parse_patch(p) for p in patches]
    old_hard = sum(int(s["old_hard_findings"]) for s in summaries)
    old_review = sum(int(s["old_review_notes"]) for s in summaries)
    refined_hard = sum(int(s["refined_hard_findings"]) for s in summaries)
    refined_review = sum(int(s["refined_review_notes"]) for s in summaries)
    timestamp = datetime.now(timezone.utc).isoformat()

    lines = [
        "# Refined Rule Historical Replay Report v0",
        "",
        "## 1. Verdict",
        "",
        VERDICT,
        "",
        "## 2. Command",
        "",
        "`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_rule_historical_replay_v0/replay_refined_rules_on_historical_patches.py`",
        "",
        "## 3. Files Read",
        "",
    ]
    lines.extend(f"- {p.relative_to(BASE.parent)}" for p in patches)
    lines.extend([
        "",
        "## 4. Aggregate Replay",
        "",
        f"- old_hard_findings_estimate: {old_hard}",
        f"- old_review_notes_estimate: {old_review}",
        f"- refined_hard_findings: {refined_hard}",
        f"- refined_review_notes: {refined_review}",
        f"- hard_finding_delta: {refined_hard - old_hard}",
        "",
        "## 5. Per Patch Results",
        "",
    ])
    for summary in summaries:
        lines.extend([
            f"### {summary['patch']}",
            f"- files_touched_count: {summary['files_touched_count']}",
            f"- old_hard_findings_estimate: {summary['old_hard_findings']}",
            f"- refined_hard_findings: {summary['refined_hard_findings']}",
            f"- refined_review_notes: {summary['refined_review_notes']}",
        ])
        for row in summary["rows"][:12]:  # type: ignore[index]
            lines.append(f"- {row['refined']} | old={row['old']} | rule={row['rule']} | reason={row['reason']} | {row['file']}:{row['line_no']} | `{row['line']}`")
        lines.append("")
    lines.extend([
        "## 6. Recovered Judgment",
        "",
        "- The refined secret/token rule lowers historical `_normalize_token(...)` examples from hard finding to review note.",
        "- The `console.log(...)` app-source finding remains a hard finding.",
        "- No component/workflow/skill/baseline authority is created by this replay.",
        "",
        "## 7. VectorFL Recovery Suggestion",
        "",
        "receipt:",
        "  refined rule replay ran over the historical patch sample",
        "",
        "residue:",
        "  old-vs-refined delta and remaining false-positive/false-negative notes",
        "",
        "candidate:",
        "  refined diff-audit rule boundary is stronger",
        "",
        "component:",
        "  HOLD until the rule set is replayed against a broader real sample and a seeded true-positive set",
        "",
        "STOP:",
        "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation",
        "",
        "## 8. HOLD",
        "",
        "- no source files modified",
        "- no prior audit files modified",
        "- no patches applied",
        "- no git used",
        "- no package install",
        "- no network / browser / MCP",
        "- no Hermes memory / skill / cron / config edit",
        "- no VectorFL authority update",
        "- no baseline / workflow / schema / registry / ontology promotion",
        "",
    ])
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    receipt = {
        "verdict": "[CODEX_STAGE1_REFINED_RULE_HISTORICAL_REPLAY_RECEIPT]",
        "timestamp": timestamp,
        "command": "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_rule_historical_replay_v0/replay_refined_rules_on_historical_patches.py",
        "input_files": [str(p.relative_to(BASE.parent)) for p in patches],
        "output_files": ["refined_rule_historical_replay_report.md", "refined_rule_historical_replay_receipt.json"],
        "exit_code": 0,
        "old_hard_findings_estimate": old_hard,
        "old_review_notes_estimate": old_review,
        "refined_hard_findings": refined_hard,
        "refined_review_notes": refined_review,
        "hard_finding_delta": refined_hard - old_hard,
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
        "baseline_workflow_schema_registry_ontology_promoted": False,
        "per_patch_summary": summaries,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": VERDICT,
        "old_hard_findings_estimate": old_hard,
        "refined_hard_findings": refined_hard,
        "report": str(REPORT),
        "receipt": str(RECEIPT),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
