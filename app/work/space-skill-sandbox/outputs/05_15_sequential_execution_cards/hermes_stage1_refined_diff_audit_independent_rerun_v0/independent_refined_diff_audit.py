#!/usr/bin/env python3
"""Hermes Stage 1 refined diff-audit independent rerun.

Stdlib only. No subprocess/git/network. Reads only declared prior patch/report inputs.
Writes only report/receipt in this output directory.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards"
OUT = BASE / "hermes_stage1_refined_diff_audit_independent_rerun_v0"
REPORT = OUT / "independent_refined_diff_audit_report.md"
RECEIPT = OUT / "independent_refined_diff_audit_receipt.json"

HIST_PATCH_DIR = BASE / "hermes_stage1_historical_code_diff_sample_audit_v0/patches"
SEEDED_FIXTURE_DIR = BASE / "hermes_stage1_seeded_true_positive_pressure_v0/fixtures"
REFERENCE_REPORTS = [
    BASE / "hermes_stage1_secret_rule_refinement_audit_v0/secret_rule_refinement_report.md",
    BASE / "hermes_stage1_refined_rule_historical_replay_v0/refined_rule_historical_replay_report.md",
    BASE / "hermes_stage1_seeded_true_positive_pressure_v0/seeded_true_positive_pressure_report.md",
]

VERDICT = "[HERMES_STAGE1_REFINED_DIFF_AUDIT_INDEPENDENT_RERUN_EXECUTED_WITH_WATCH]"
RECEIPT_VERDICT = "[HERMES_STAGE1_REFINED_DIFF_AUDIT_INDEPENDENT_RERUN_RECEIPT]"
COMMAND = "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit.py"

CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".json", ".toml", ".yaml", ".yml", ".env"}
SCRIPT_EXTS = {".sh", ".bash", ".zsh"}
SECRET_NAMES = ("api_key", "token", "password", "secret", "credential", "service_token", "api_token")
PLACEHOLDER_PATTERNS = [
    re.compile(r"^\s*$"),
    re.compile(r"^\$\{[^}]+\}$"),
    re.compile(r"^<[^>]+>$"),
    re.compile(r"^(example|placeholder|changeme|change-me|set-in-env|redacted)$", re.I),
]
SECRET_LINE = re.compile(r"(?P<name>api_key|api_token|service_token|token|password|secret|credential)\s*=\s*(?P<quote>['\"])(?P<value>.*?)(?P=quote)", re.I)
ENV_READ = re.compile(r"os\.environ|getenv|read_from_env", re.I)
SECRET_WORD = re.compile(r"api_key|api_token|service_token|token|password|secret|credential|sk_live", re.I)

NON_SECRET_PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("debug_print_python", re.compile(r"^\s*print\s*\(")),
    ("debug_print_js", re.compile(r"^\s*console\.log\s*\(")),
    ("bare_except", re.compile(r"^\s*except\s*:\s*(#.*)?$")),
    ("dynamic_eval", re.compile(r"^\s*eval\s*\(")),
    ("dynamic_exec", re.compile(r"^\s*exec\s*\(")),
    ("dynamic_subprocess_shell_true", re.compile(r"subprocess\.run\s*\(.*shell\s*=\s*True", re.I)),
    ("dynamic_os_system", re.compile(r"os\.system\s*\(", re.I)),
    ("shell_curl_pipe_bash", re.compile(r"curl\b.*\|\s*bash", re.I)),
    ("shell_rm_rf", re.compile(r"rm\s+-rf", re.I)),
    ("shell_chmod_777", re.compile(r"chmod\s+777", re.I)),
    ("unresolved_todo", re.compile(r"\bTODO\b")),
    ("unresolved_fixme", re.compile(r"\bFIXME\b")),
]

MAX_EXAMPLES = 8


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def redact(s: str) -> str:
    s = SECRET_LINE.sub(lambda m: f"{m.group('name')} = [REDACTED]", s)
    s = re.sub(r"sk_live[_A-Za-z0-9-]*", "[REDACTED]", s)
    return s[:220]


def context_for(path: str) -> str:
    p = path.replace("\\", "/")
    suffix = Path(p).suffix.lower()
    name = Path(p).name.lower()
    if p.startswith("docs/") or suffix == ".md":
        return "docs"
    if p.startswith("tests/") or "/tests/" in f"/{p}" or "fixture" in p.lower() or "fixtures" in p.lower():
        return "tests_or_fixtures"
    if p.startswith("config/") or suffix in CONFIG_EXTS or "env" in name:
        return "config_or_env_like"
    if p.startswith("scripts/") or p.startswith("deploy") or "/deploy" in p or suffix in SCRIPT_EXTS:
        return "scripts_or_deploy"
    if p.startswith("app/") and suffix in CODE_EXTS:
        return "app_source"
    if suffix in CODE_EXTS:
        return "source_code"
    return "other"


def is_placeholder(value: str) -> bool:
    v = value.strip()
    return any(rx.search(v) for rx in PLACEHOLDER_PATTERNS)


def classify_secret(line: str, ctx: str) -> Tuple[str, str] | None:
    if not SECRET_WORD.search(line):
        return None
    if ctx in {"docs", "tests_or_fixtures"}:
        return "review_note", "docs_tests_fixtures_secret_example"
    m = SECRET_LINE.search(line)
    if m:
        value = m.group("value")
        if is_placeholder(value) or ENV_READ.search(line):
            return "review_note", "placeholder_or_env_secret_value"
        if ctx in {"app_source", "source_code", "config_or_env_like", "scripts_or_deploy"}:
            return "hard_finding", "literal_secret_assignment"
        return "review_note", "literal_secret_outside_hard_context"
    # unquoted, env, normalization, parser tokens, and bare secret words are review notes.
    return "review_note", "semantic_or_env_or_secret_word_without_literal_assignment"


def classify_non_secret(rule: str, line: str, ctx: str) -> Tuple[str, str] | None:
    # Avoid string-only noise for print/eval/exec/TODO-like data labels by requiring rule pattern matches already anchored where relevant.
    if ctx in {"docs", "tests_or_fixtures"}:
        return "review_note", "docs_tests_fixtures_non_secret_pattern"
    if rule in {"debug_print_python", "debug_print_js", "bare_except", "dynamic_eval", "dynamic_exec", "dynamic_subprocess_shell_true", "dynamic_os_system"}:
        if ctx in {"app_source", "source_code"}:
            return "hard_finding", "app_source_non_secret_rule"
        if ctx == "scripts_or_deploy" and rule.startswith("dynamic_"):
            return "hard_finding", "script_dynamic_execution"
        return "review_note", "non_secret_pattern_outside_hard_context"
    if rule in {"shell_curl_pipe_bash", "shell_rm_rf", "shell_chmod_777"}:
        if ctx == "scripts_or_deploy":
            return "hard_finding", "script_shell_or_destructive_command"
        return "review_note", "shell_pattern_outside_script_deploy"
    if rule in {"unresolved_todo", "unresolved_fixme"}:
        return "review_note", "unresolved_marker"
    return None


def empty_result(name: str, group: str) -> Dict[str, object]:
    return {
        "group": group,
        "patch": name,
        "files_touched_count": 0,
        "sample_files_touched": [],
        "added_lines_seen": 0,
        "deleted_lines_seen": 0,
        "contexts": {},
        "hard_findings": 0,
        "review_notes": 0,
        "rule_hits": {},
        "hard_examples": [],
        "review_examples": [],
    }


def add_hit(result: Dict[str, object], severity: str, rule: str, reason: str, file_path: str, line_no: int, ctx: str, line: str) -> None:
    result["rule_hits"].setdefault(rule, {"hard_finding": 0, "review_note": 0})  # type: ignore[index]
    result["rule_hits"][rule][severity] += 1  # type: ignore[index]
    result["hard_findings" if severity == "hard_finding" else "review_notes"] += 1  # type: ignore[operator]
    bucket = result["hard_examples" if severity == "hard_finding" else "review_examples"]
    if len(bucket) < MAX_EXAMPLES:  # type: ignore[arg-type]
        bucket.append({  # type: ignore[union-attr]
            "severity": severity,
            "rule": rule,
            "reason": reason,
            "file": file_path,
            "line_no": line_no,
            "context": ctx,
            "excerpt": redact(line.strip()),
        })


def parse_patch(p: Path, group: str) -> Dict[str, object]:
    result = empty_result(p.name, group)
    current_file = "UNKNOWN"
    files = set()
    with p.open("r", encoding="utf-8", errors="replace") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.rstrip("\n")
            if raw.startswith("diff --git "):
                parts = raw.split()
                if len(parts) >= 4:
                    current_file = parts[3][2:] if parts[3].startswith("b/") else parts[3]
                    files.add(current_file)
                    ctx = context_for(current_file)
                    result["contexts"][ctx] = result["contexts"].get(ctx, 0) + 1  # type: ignore[index]
                continue
            if raw.startswith("+++ b/"):
                current_file = raw[6:]
                files.add(current_file)
                continue
            if raw.startswith("-") and not raw.startswith("---"):
                result["deleted_lines_seen"] += 1  # type: ignore[operator]
                continue
            if not raw.startswith("+") or raw.startswith("+++"):
                continue
            result["added_lines_seen"] += 1  # type: ignore[operator]
            added = raw[1:]
            ctx = context_for(current_file)
            secret = classify_secret(added, ctx)
            if secret:
                sev, reason = secret
                add_hit(result, sev, "secret_boundary", reason, current_file, line_no, ctx, added)
            for rule, rx in NON_SECRET_PATTERNS:
                if rx.search(added):
                    c = classify_non_secret(rule, added, ctx)
                    if c:
                        sev, reason = c
                        add_hit(result, sev, rule, reason, current_file, line_no, ctx, added)
    result["files_touched_count"] = len(files)
    result["sample_files_touched"] = sorted(files)[:15]
    return result


def merge_rule_hits(results: List[Dict[str, object]]) -> Dict[str, Dict[str, int]]:
    merged: Dict[str, Dict[str, int]] = {}
    for r in results:
        for rule, counts in r["rule_hits"].items():  # type: ignore[union-attr]
            merged.setdefault(rule, {"hard_finding": 0, "review_note": 0})
            merged[rule]["hard_finding"] += int(counts.get("hard_finding", 0))
            merged[rule]["review_note"] += int(counts.get("review_note", 0))
    return merged


def example_lines(items: List[Dict[str, object]]) -> List[str]:
    if not items:
        return ["- none"]
    return [f"- {x['severity']} | {x['rule']} | {x['reason']} | {x['file']}:{x['line_no']} | context={x['context']} | `{x['excerpt']}`" for x in items]


def render_group(title: str, results: List[Dict[str, object]]) -> List[str]:
    lines = [f"## {title}", ""]
    for r in results:
        lines += [
            f"### {r['patch']}",
            f"- files_touched_count: {r['files_touched_count']}",
            f"- added_lines_seen: {r['added_lines_seen']}",
            f"- deleted_lines_seen: {r['deleted_lines_seen']}",
            f"- hard_findings: {r['hard_findings']}",
            f"- review_notes: {r['review_notes']}",
            f"- contexts: `{json.dumps(r['contexts'], ensure_ascii=False, sort_keys=True)}`",
            "- hard finding examples:",
        ]
        lines += example_lines(r["hard_examples"])  # type: ignore[arg-type]
        lines.append("- review note examples:")
        lines += example_lines(r["review_examples"])  # type: ignore[arg-type]
        lines.append("")
    return lines


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # Verify/reference reports are explicit read-only inputs; read only for evidence anchoring.
    reference_report_bytes = {rel(p): len(p.read_text(encoding="utf-8", errors="replace")) for p in REFERENCE_REPORTS if p.exists()}
    historical_files = sorted(HIST_PATCH_DIR.glob("*.patch"))
    seeded_files = sorted(SEEDED_FIXTURE_DIR.glob("*.patch"))
    historical_results = [parse_patch(p, "historical") for p in historical_files]
    seeded_results = [parse_patch(p, "seeded") for p in seeded_files]
    all_results = historical_results + seeded_results
    historical_hard = sum(int(r["hard_findings"]) for r in historical_results)
    historical_notes = sum(int(r["review_notes"]) for r in historical_results)
    seeded_hard = sum(int(r["hard_findings"]) for r in seeded_results)
    seeded_notes = sum(int(r["review_notes"]) for r in seeded_results)
    aggregate_rule_hits = merge_rule_hits(all_results)

    differences = []
    if historical_hard != 1:
        differences.append(f"historical_hard_findings differs from Codex replay target 1: observed {historical_hard}")
    else:
        differences.append("historical_hard_findings matched Codex replay target: 1")
    if seeded_hard != 19 or seeded_notes != 23:
        differences.append(f"seeded aggregate differs from Codex replay target 19/23: observed {seeded_hard}/{seeded_notes}")
    else:
        differences.append("seeded aggregate matched Codex replay target: hard=19, review=23")
    if historical_notes != 30:
        differences.append(f"historical_review_notes differs from prior replay 30: observed {historical_notes}; likely independent rule implementation/counting boundary variation")

    report_lines: List[str] = [
        "# Hermes Stage 1 Refined Diff Audit Independent Rerun Report v0", "",
        "## Verdict", "", VERDICT, "",
        "## Command Run", "", f"`{COMMAND}`", "",
        "## Files Read", "",
        f"- {rel(HIST_PATCH_DIR)}/",
        f"- {rel(SEEDED_FIXTURE_DIR)}/",
    ]
    report_lines += [f"- {rel(p)}" for p in REFERENCE_REPORTS]
    report_lines += [f"- {rel(p)}" for p in historical_files + seeded_files]
    report_lines += ["", "## Files Created", "", f"- {rel(Path(__file__).resolve())}", f"- {rel(REPORT)}", f"- {rel(RECEIPT)}", ""]
    report_lines += render_group("Historical Patch Results", historical_results)
    report_lines += render_group("Seeded Fixture Results", seeded_results)
    report_lines += [
        "## Aggregate Counts", "",
        f"- historical_hard_findings: {historical_hard}",
        f"- historical_review_notes: {historical_notes}",
        f"- seeded_hard_findings: {seeded_hard}",
        f"- seeded_review_notes: {seeded_notes}",
        f"- aggregate_hard_findings: {historical_hard + seeded_hard}",
        f"- aggregate_review_notes: {historical_notes + seeded_notes}",
        "", "## Rule Hits", "",
    ]
    report_lines += [f"- {rule}: hard_finding={counts['hard_finding']}, review_note={counts['review_note']}" for rule, counts in sorted(aggregate_rule_hits.items())] or ["- none"]
    report_lines += ["", "## Differences From Codex Replay", ""] + [f"- {d}" for d in differences]
    report_lines += [
        "", "## False-Positive Notes", "",
        "- Semantic token normalization and token iteration are review notes, not hard findings.",
        "- Docs/tests/fixtures examples stay review notes even when they contain secret-looking or dynamic-execution strings.",
        "- String/path-context detection cannot prove whether a literal value is a real live credential; secret-like excerpts are redacted.",
        "", "## False-Negative Notes", "",
        "- This rerun does not perform entropy scanning, data-flow analysis, runtime reachability, dependency analysis, or git history secret scanning.",
        "- Literal secret detection can miss concatenated, encoded, or indirectly loaded values.",
        "- Anchored print/eval/exec detection intentionally avoids string-only noise and may miss obfuscated calls.",
        "", "## VectorFL Recovery Suggestion", "",
        "receipt:", "  Hermes independently reran refined diff audit with command/output evidence", "",
        "residue:", "  count differences, false-positive notes, false-negative notes", "",
        "candidate:", "  refined diff-audit rule set becomes stronger if behavior matches Codex replay", "",
        "component:", "  HOLD until broader real sample and user/Codex explicit approval", "",
        "STOP:", "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation", "",
        "## WATCH", "", "independent rerun may strengthen candidate status but still does not authorize component/workflow/skill/baseline", "",
        "## HOLD", "",
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
        "", "## Hard Stop Confirmation", "",
        "No mutation, promotion, persistence, git, network, browser, MCP, package install, cron, memory, skill, config, or VectorFL authority action was performed.", "",
    ]
    REPORT.write_text("\n".join(report_lines), encoding="utf-8")

    receipt = {
        "verdict": RECEIPT_VERDICT,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "command": COMMAND,
        "input_files": [rel(p) for p in REFERENCE_REPORTS + historical_files + seeded_files],
        "reference_report_bytes": reference_report_bytes,
        "output_files": [rel(Path(__file__).resolve()), rel(REPORT), rel(RECEIPT)],
        "exit_code": 0,
        "historical_hard_findings": historical_hard,
        "historical_review_notes": historical_notes,
        "seeded_hard_findings": seeded_hard,
        "seeded_review_notes": seeded_notes,
        "aggregate_rule_hits": aggregate_rule_hits,
        "historical_results": historical_results,
        "seeded_results": seeded_results,
        "differences_from_codex_replay": differences,
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
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
