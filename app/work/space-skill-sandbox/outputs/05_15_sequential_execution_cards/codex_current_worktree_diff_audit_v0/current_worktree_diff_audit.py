#!/usr/bin/env python3
"""Read-only current worktree/staged diff audit using tightened Stage 1 rules."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent
REPORT = BASE / "current_worktree_diff_audit_report.md"
RECEIPT = BASE / "current_worktree_diff_audit_receipt.json"
VERDICT = "[CODEX_CURRENT_WORKTREE_DIFF_AUDIT_EXECUTED_WITH_WATCH]"

PATHS = [
    "app/ui",
    "app/core",
    "app/runtime",
    "scripts",
    "config",
    "package.json",
    "vite.config.js",
    "vite.config.ts",
    "vite.config.mjs",
]

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


def run_git(args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=BASE.parents[5], text=True, capture_output=True, check=False)


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
            if re.search(r"\b(tokenize|tokenizer|tokens?|PATH_TOKEN_RE|overlap_tokens|sentence_tokens|canonicalizable_token)", stripped):
                return ("none", "ordinary_token_processing_noise")
            return ("review_note", "explicit_secret_or_credential_name")
        return ("none", "no_secret_boundary")
    name, rhs = match.group(1), match.group(2).strip()
    if not SECRET_NAME_RX.search(name):
        return ("none", "assignment_not_secret_named")
    if context in {"docs", "tests_or_fixtures"}:
        return ("review_note", "docs_tests_explicit_secret_assignment_example")
    if NORMALIZER_RX.search(rhs):
        return ("review_note", "semantic_token_assignment")
    value = strip_quotes(rhs)
    if PLACEHOLDER_RX.search(value) or value == "":
        return ("review_note", "placeholder_or_env_secret_value")
    if context in {"config_or_env_like", "scripts_or_deploy"} or REALISH_SECRET_RX.search(value):
        return ("hard_finding", "literal_secret_assignment")
    return ("review_note", "secret_named_assignment_needs_review")


def classify_non_secret(rule: str, context: str) -> Tuple[str, str]:
    shell = rule.startswith("shell_")
    dynamic = rule.startswith("dynamic_")
    debug = rule.startswith("debug_")
    bare = rule == "bare_except"
    if context in {"docs", "tests_or_fixtures"}:
        return ("review_note", "docs_tests_fixtures_non_secret_pattern")
    if context == "scripts_or_deploy" and (shell or dynamic):
        return ("hard_finding", "script_shell_or_dynamic_command")
    if context in {"app_source", "source_code"} and (debug or bare or dynamic):
        return ("hard_finding", "app_source_non_secret_rule")
    return ("review_note", "non_secret_pattern_outside_hard_context")


def parse_diff(label: str, text: str) -> Dict[str, object]:
    current_file = "UNKNOWN"
    files_seen = set()
    added_lines = 0
    deleted_lines = 0
    rows: List[Dict[str, object]] = []
    contexts: Dict[str, int] = {}
    for line_no, raw in enumerate(text.splitlines(), start=1):
        if raw.startswith("diff --git "):
            parts = raw.split()
            if len(parts) >= 4:
                current_file = parts[3][2:] if parts[3].startswith("b/") else parts[3]
                files_seen.add(current_file)
                ctx = path_context(current_file)
                contexts[ctx] = contexts.get(ctx, 0) + 1
            continue
        if raw.startswith("+++ b/"):
            current_file = raw[6:]
            files_seen.add(current_file)
            continue
        if raw.startswith("-") and not raw.startswith("---"):
            deleted_lines += 1
            continue
        if not raw.startswith("+") or raw.startswith("+++"):
            continue
        added_lines += 1
        added = raw[1:]
        ctx = path_context(current_file)
        if SECRET_NAME_RX.search(added):
            sev, reason = classify_secret(added, ctx)
            if sev != "none":
                rows.append({"severity": sev, "rule": "secret_boundary", "reason": reason, "file": current_file, "line_no": line_no, "context": ctx, "line": added.strip()[:220]})
        for rule, rx in NON_SECRET_RULES:
            if not rx.search(added):
                continue
            sev, reason = classify_non_secret(rule, ctx)
            rows.append({"severity": sev, "rule": rule, "reason": reason, "file": current_file, "line_no": line_no, "context": ctx, "line": added.strip()[:220]})
    return {
        "label": label,
        "files_touched_count": len(files_seen),
        "sample_files_touched": sorted(files_seen)[:30],
        "added_lines_seen": added_lines,
        "deleted_lines_seen": deleted_lines,
        "contexts": contexts,
        "hard_findings": sum(1 for row in rows if row["severity"] == "hard_finding"),
        "review_notes": sum(1 for row in rows if row["severity"] == "review_note"),
        "rows": rows,
    }


def row_lines(rows: List[Dict[str, object]], severity: str, limit: int = 16) -> List[str]:
    selected = [row for row in rows if row["severity"] == severity][:limit]
    if not selected:
        return ["- none"]
    return [
        f"- {row['severity']} | {row['rule']} | {row['reason']} | {row['file']}:{row['line_no']} | context={row['context']} | `{row['line']}`"
        for row in selected
    ]


def main() -> int:
    timestamp = datetime.now(timezone.utc).isoformat()
    staged_proc = run_git(["diff", "--cached", "--no-ext-diff", "--", *PATHS])
    unstaged_proc = run_git(["diff", "--no-ext-diff", "--", *PATHS])
    staged_names = run_git(["diff", "--cached", "--name-only", "--", *PATHS])
    unstaged_names = run_git(["diff", "--name-only", "--", *PATHS])
    status = run_git(["status", "--short"])
    results = [
        parse_diff("staged", staged_proc.stdout),
        parse_diff("unstaged", unstaged_proc.stdout),
    ]
    hard_total = sum(int(r["hard_findings"]) for r in results)
    review_total = sum(int(r["review_notes"]) for r in results)
    untracked_count = sum(1 for line in status.stdout.splitlines() if line.startswith("?? "))

    lines = [
        "# Current Worktree Diff Audit Report v0",
        "",
        "## 1. Verdict",
        "",
        VERDICT,
        "",
        "## 2. Commands Run",
        "",
        "- `git diff --cached --no-ext-diff -- <bounded paths>`",
        "- `git diff --no-ext-diff -- <bounded paths>`",
        "- `git diff --cached --name-only -- <bounded paths>`",
        "- `git diff --name-only -- <bounded paths>`",
        "- `git status --short`",
        "",
        "## 3. Scope",
        "",
        "- Read-only git commands only.",
        "- Staged and unstaged tracked diffs under bounded code/script/config paths were audited.",
        "- Untracked files were counted from status but not diff-audited because `git diff` does not include untracked content.",
        f"- untracked_status_entries_count: {untracked_count}",
        "",
        "## 4. Files Seen",
        "",
        "staged files:",
    ]
    lines.extend(f"- {name}" for name in staged_names.stdout.splitlines() if name.strip())
    lines.append("")
    lines.append("unstaged files:")
    lines.extend(f"- {name}" for name in unstaged_names.stdout.splitlines() if name.strip())
    lines.extend([
        "",
        "## 5. Aggregate Counts",
        "",
        f"- total_hard_findings: {hard_total}",
        f"- total_review_notes: {review_total}",
        "",
        "## 6. Per Diff Results",
        "",
    ])
    for result in results:
        rows = result["rows"]  # type: ignore[index]
        lines.extend([
            f"### {result['label']}",
            f"- files_touched_count: {result['files_touched_count']}",
            f"- added_lines_seen: {result['added_lines_seen']}",
            f"- deleted_lines_seen: {result['deleted_lines_seen']}",
            f"- hard_findings: {result['hard_findings']}",
            f"- review_notes: {result['review_notes']}",
            f"- contexts: `{json.dumps(result['contexts'], ensure_ascii=False, sort_keys=True)}`",
            "- hard finding examples:",
        ])
        lines.extend(row_lines(rows, "hard_finding"))  # type: ignore[arg-type]
        lines.append("- review note examples:")
        lines.extend(row_lines(rows, "review_note"))  # type: ignore[arg-type]
        lines.append("")
    lines.extend([
        "## 7. Recovered Judgment",
        "",
        "- This is a current tracked diff audit, not an audit of all untracked files.",
        "- Hard findings are candidate review signals, not proof of exploitability.",
        "- Review notes are threshold signals, not authority or component readiness.",
        "",
        "## 8. VectorFL Recovery Suggestion",
        "",
        "receipt:",
        "  current staged/unstaged tracked diff audit ran with command/output evidence",
        "",
        "residue:",
        "  current surface findings, untracked surface limitation, and threshold behavior",
        "",
        "candidate:",
        "  refined diff-audit rule set gets broader real-surface pressure evidence",
        "",
        "component:",
        "  HOLD",
        "",
        "STOP:",
        "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation",
        "",
        "## 9. HOLD",
        "",
        "- no source files modified",
        "- no patches applied",
        "- no git add / commit / reset / checkout",
        "- no package install",
        "- no network / browser / MCP",
        "- no Hermes memory / skill / cron / config edit",
        "- no VectorFL authority update",
        "- no baseline / workflow / schema / registry / ontology promotion",
        "",
    ])
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    receipt = {
        "verdict": "[CODEX_CURRENT_WORKTREE_DIFF_AUDIT_RECEIPT]",
        "timestamp": timestamp,
        "commands": [
            "git diff --cached --no-ext-diff -- <bounded paths>",
            "git diff --no-ext-diff -- <bounded paths>",
            "git diff --cached --name-only -- <bounded paths>",
            "git diff --name-only -- <bounded paths>",
            "git status --short",
        ],
        "bounded_paths": PATHS,
        "staged_files": [name for name in staged_names.stdout.splitlines() if name.strip()],
        "unstaged_files": [name for name in unstaged_names.stdout.splitlines() if name.strip()],
        "untracked_status_entries_count": untracked_count,
        "exit_codes": {
            "staged_diff": staged_proc.returncode,
            "unstaged_diff": unstaged_proc.returncode,
            "staged_names": staged_names.returncode,
            "unstaged_names": unstaged_names.returncode,
            "status": status.returncode,
        },
        "total_hard_findings": hard_total,
        "total_review_notes": review_total,
        "results": results,
        "network_used": False,
        "packages_installed": False,
        "git_mutation_used": False,
        "source_files_modified": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_files_modified": False,
        "baseline_workflow_schema_registry_ontology_promoted": False,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "verdict": VERDICT,
        "total_hard_findings": hard_total,
        "total_review_notes": review_total,
        "staged_files": len(receipt["staged_files"]),
        "unstaged_files": len(receipt["unstaged_files"]),
        "untracked_status_entries_count": untracked_count,
        "report": str(REPORT),
        "receipt": str(RECEIPT),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
