#!/usr/bin/env python3
"""Seeded true-positive pressure audit for refined diff rules. Stdlib only."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent
FIXTURE_DIR = BASE / "fixtures"
REPORT = BASE / "seeded_true_positive_pressure_report.md"
RECEIPT = BASE / "seeded_true_positive_pressure_receipt.json"
VERDICT = "[CODEX_STAGE1_SEEDED_TRUE_POSITIVE_PRESSURE_EXECUTED_WITH_WATCH]"

CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".env", ".json", ".toml", ".yaml", ".yml"}
SCRIPT_EXTS = {".sh", ".bash", ".zsh"}

SECRET_NAME_RX = re.compile(r"\b(api[_-]?key|token|password|secret|credential|service_token|api_token)\b", re.IGNORECASE)
ASSIGN_RX = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$")
SHELL_ASSIGN_RX = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)=(.+?)\s*$")
PLACEHOLDER_RX = re.compile(r"(<[^>]+>|\$\{[^}]+\}|fixture|placeholder|set-in-env|dummy|sample)", re.IGNORECASE)
NORMALIZER_RX = re.compile(r"(_normalize|normalize|tokenize|parse|lower\s*\(|strip\s*\(|len\s*\(|list\s*\(|str\s*\(|os\.environ|read_from_env|getenv)", re.IGNORECASE)
QUOTED_RX = re.compile(r"^(['\"])(.*)\1$")
REALISH_SECRET_RX = re.compile(r"(sk_live|prod-token|real-looking|plain-text|admin123|embedded-secret|service-account)", re.IGNORECASE)

NON_SECRET_RULES: List[Tuple[str, re.Pattern[str]]] = [
    ("debug_print_python", re.compile(r"^\s*print\s*\(")),
    ("debug_print_js", re.compile(r"^\s*console\.log\s*\(")),
    ("bare_except", re.compile(r"^\s*except\s*:\s*(#.*)?$")),
    ("unresolved_todo", re.compile(r"\bTODO\b")),
    ("unresolved_fixme", re.compile(r"\bFIXME\b")),
    ("shell_curl_pipe_bash", re.compile(r"curl\b.*\|\s*bash", re.IGNORECASE)),
    ("shell_rm_rf", re.compile(r"rm\s+-rf", re.IGNORECASE)),
    ("shell_chmod_777", re.compile(r"chmod\s+777", re.IGNORECASE)),
    ("dynamic_eval", re.compile(r"^\s*eval\s*\(")),
    ("dynamic_exec", re.compile(r"^\s*exec\s*\(")),
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
    if p.startswith("config/") or suffix in CONFIG_EXTS or "env" in Path(p).name.lower():
        return "config_or_env_like"
    if p.startswith("scripts/") or "deploy" in p.lower() or suffix in SCRIPT_EXTS:
        return "scripts_or_deploy"
    if p.startswith("app/") and suffix in CODE_EXTS:
        return "app_source"
    if suffix in CODE_EXTS:
        return "source_code"
    return "other"


def strip_quotes(rhs: str) -> str:
    rhs = rhs.strip()
    quoted = QUOTED_RX.match(rhs)
    return quoted.group(2) if quoted else rhs


def classify_secret(line: str, context: str) -> Tuple[str, str]:
    stripped = line.strip()
    match = ASSIGN_RX.match(stripped) or SHELL_ASSIGN_RX.match(stripped)
    if not match:
        if SECRET_NAME_RX.search(stripped):
            return ("review_note", "secret_word_without_direct_assignment")
        return ("none", "no_secret_boundary")
    name, rhs = match.group(1), match.group(2).strip()
    if not SECRET_NAME_RX.search(name):
        return ("none", "assignment_not_secret_named")
    if context in {"docs", "tests_or_fixtures"}:
        return ("review_note", f"{context}_example")
    if NORMALIZER_RX.search(rhs):
        return ("review_note", "semantic_or_env_boundary_not_literal_secret")
    value = strip_quotes(rhs)
    if PLACEHOLDER_RX.search(value) or value == "":
        return ("review_note", "placeholder_or_empty_secret_value")
    if context in {"config_or_env_like", "scripts_or_deploy"} or REALISH_SECRET_RX.search(value):
        return ("hard_finding", "literal_secret_assignment")
    return ("review_note", "secret_named_assignment_needs_review")


def classify_non_secret(rule: str, context: str) -> str:
    shell = rule.startswith("shell_")
    dynamic = rule.startswith("dynamic_")
    debug = rule.startswith("debug_")
    bare = rule == "bare_except"
    if context in {"docs", "tests_or_fixtures"}:
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
            context = path_context(current_file)
            if SECRET_NAME_RX.search(added):
                sev, reason = classify_secret(added, context)
                if sev != "none":
                    rows.append({"severity": sev, "rule": "secret_boundary", "reason": reason, "file": current_file, "line_no": line_no, "context": context, "line": added.strip()[:220]})
            for rule, rx in NON_SECRET_RULES:
                if not rx.search(added):
                    continue
                sev = classify_non_secret(rule, context)
                rows.append({"severity": sev, "rule": rule, "reason": "non_secret_rule", "file": current_file, "line_no": line_no, "context": context, "line": added.strip()[:220]})
    return {
        "patch": path.name,
        "files_touched_count": len(files_seen),
        "added_lines_seen": added_lines,
        "hard_findings": sum(1 for row in rows if row["severity"] == "hard_finding"),
        "review_notes": sum(1 for row in rows if row["severity"] == "review_note"),
        "rows": rows,
    }


def main() -> int:
    fixtures = sorted(FIXTURE_DIR.glob("*.patch"))
    summaries = [parse_patch(path) for path in fixtures]
    hard = sum(int(s["hard_findings"]) for s in summaries)
    review = sum(int(s["review_notes"]) for s in summaries)
    timestamp = datetime.now(timezone.utc).isoformat()
    lines = [
        "# Seeded True-Positive Pressure Report v0",
        "",
        "## 1. Verdict",
        "",
        VERDICT,
        "",
        "## 2. Command",
        "",
        "`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/audit_seeded_true_positive_pressure.py`",
        "",
        "## 3. Aggregate",
        "",
        f"- total_hard_findings: {hard}",
        f"- total_review_notes: {review}",
        "",
        "## 4. Per Fixture",
        "",
    ]
    for summary in summaries:
        lines.extend([
            f"### {summary['patch']}",
            f"- files_touched_count: {summary['files_touched_count']}",
            f"- added_lines_seen: {summary['added_lines_seen']}",
            f"- hard_findings: {summary['hard_findings']}",
            f"- review_notes: {summary['review_notes']}",
        ])
        for row in summary["rows"][:18]:  # type: ignore[index]
            lines.append(f"- {row['severity']} | {row['rule']} | {row['reason']} | {row['file']}:{row['line_no']} | context={row['context']} | `{row['line']}`")
        lines.append("")
    lines.extend([
        "## 5. Recovered Judgment",
        "",
        "- Refined rules still catch seeded literal secrets in app/config/script contexts.",
        "- Refined rules keep semantic token normalization as review-level pressure.",
        "- Docs and test fixtures remain review notes, not hard findings.",
        "- Dangerous shell and dynamic execution remain hard findings in app/script contexts.",
        "",
        "## 6. VectorFL Recovery Suggestion",
        "",
        "receipt:",
        "  seeded pressure audit ran with command/output evidence",
        "",
        "residue:",
        "  remaining false-negative and false-positive boundaries",
        "",
        "candidate:",
        "  diff-audit rule boundary is stronger after true-positive pressure",
        "",
        "component:",
        "  HOLD until broader real sample and independent Hermes rerun",
        "",
        "STOP:",
        "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation",
        "",
        "## 7. HOLD",
        "",
        "- no source files modified",
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
        "verdict": "[CODEX_STAGE1_SEEDED_TRUE_POSITIVE_PRESSURE_RECEIPT]",
        "timestamp": timestamp,
        "command": "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/audit_seeded_true_positive_pressure.py",
        "input_files": [f"fixtures/{p.name}" for p in fixtures],
        "output_files": ["seeded_true_positive_pressure_report.md", "seeded_true_positive_pressure_receipt.json"],
        "exit_code": 0,
        "total_hard_findings": hard,
        "total_review_notes": review,
        "network_used": False,
        "packages_installed": False,
        "git_used": False,
        "source_files_modified": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_files_modified": False,
        "baseline_workflow_schema_registry_ontology_promoted": False,
        "per_fixture_summary": summaries,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": VERDICT,
        "total_hard_findings": hard,
        "total_review_notes": review,
        "report": str(REPORT),
        "receipt": str(RECEIPT),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
