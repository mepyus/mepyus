#!/usr/bin/env python3
"""Fast bounded historical code-diff audit: stdlib only, no subprocess/git/network."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent
PATCH_DIR = BASE / "patches"
REPORT = BASE / "historical_code_diff_audit_report.md"
RECEIPT = BASE / "historical_code_diff_audit_receipt.json"
VERDICT = "[HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_EXECUTED_WITH_WATCH]"
RECEIPT_VERDICT = "[HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_RECEIPT]"

SELECTED_COMMITS = [
    {"sha": "a542716f3", "subject": "Align whole-space orientation and Package 033 candidate-evidence closeout", "selection_reason": "Touches app/core runtime Python, app/runtime Python, app/ui TSX/package surfaces, plus generated JSON."},
    {"sha": "4601f7c18", "subject": "Add integrated engine operating spine workbench updates", "selection_reason": "Touches app/runtime Python, integrated engine TSX/package surfaces, runtime session JSON/log surfaces."},
    {"sha": "4e0389a4d", "subject": "Initial commit: Initialize vectorfl_replica repository", "selection_reason": "Large initial code/config/script surface commit; selected despite size to pressure path-context handling."},
    {"sha": "a998543da", "subject": "m", "selection_reason": "Large historical code/script/config seed commit with app/runtime, scripts, tests, JSON and UI surfaces."},
]
SELECTION_COMMANDS = [
    "git log --oneline -- app/core app/ui scripts config package.json vite.config.js vite.config.ts vite.config.mjs '*.json' '*.toml' '*.yaml' '*.yml' ':(exclude)app/work/*.md' ':(exclude)app/work/**' ':(exclude)**/*.md'",
    "git diff-tree --no-commit-id --name-only -r <sha>",
    "git show --stat --oneline --no-renames a998543da",
    "git show --no-ext-diff --no-renames --format=medium <sha> -- <selected_code_paths> > patches/<short_sha>.patch",
]
SELECTION_LIMITS = [
    "Read-only git only for selection/extraction; no git mutation commands used.",
    "Only 4 qualifying non-doc-only historical commits were found under the bounded pathspec; packet allowed continuing with fewer than 5.",
    "Initial/seed commits are large and include generated/binary/report surfaces; audit keeps path-context notes rather than semantic claims.",
    "First audit attempt timed out because the script kept too many finding objects from very large seed patches; the script was rewritten inside the declared output directory to stream counts/examples only, then rerun.",
]

PATTERNS: List[Tuple[str, re.Pattern[str]]] = [
    ("debug_print_python", re.compile(r"\bprint\s*\(")),
    ("debug_print_js", re.compile(r"\bconsole\.log\s*\(")),
    ("secret_sk_live", re.compile(r"sk_live", re.IGNORECASE)),
    ("secret_api_key", re.compile(r"api_key", re.IGNORECASE)),
    ("secret_token_assignment", re.compile(r"\btoken\s*=" , re.IGNORECASE)),
    ("secret_password_assignment", re.compile(r"\bpassword\s*=" , re.IGNORECASE)),
    ("secret_assignment", re.compile(r"\bsecret\s*=" , re.IGNORECASE)),
    ("secret_credential", re.compile(r"credential", re.IGNORECASE)),
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
SECRETISH = re.compile(r"(sk_live[_A-Za-z0-9-]*|api_key\s*=\s*['\"][^'\"]+['\"]|token\s*=\s*['\"][^'\"]+['\"]|password\s*=\s*['\"][^'\"]+['\"]|secret\s*=\s*['\"][^'\"]+['\"])", re.IGNORECASE)
CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".json", ".toml", ".yaml", ".yml"}
SCRIPT_EXTS = {".sh", ".bash", ".zsh"}
MAX_EXAMPLES_PER_KIND = 8


def redact(text: str) -> str:
    return SECRETISH.sub("[REDACTED]", text)[:220]


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
    if p.startswith("scripts/") or "deploy" in p.lower() or suffix in SCRIPT_EXTS:
        return "scripts_or_deploy"
    if p.startswith("app/") and suffix in CODE_EXTS:
        return "app_source"
    if suffix in CODE_EXTS:
        return "source_code"
    return "other"


def severity_for(rule: str, context: str) -> str:
    secret = rule.startswith("secret_")
    shell = rule.startswith("shell_")
    dynamic = rule.startswith("dynamic_")
    debug = rule.startswith("debug_")
    bare = rule == "bare_except"
    if context in {"docs", "tests_or_fixtures", "generated"}:
        return "review_note"
    if context == "config_or_env_like" and secret:
        return "hard_finding"
    if context == "scripts_or_deploy" and (shell or dynamic or secret):
        return "hard_finding"
    if context in {"app_source", "source_code"} and (debug or secret or bare or dynamic):
        return "hard_finding"
    return "review_note"


def empty_patch_summary(name: str) -> Dict[str, object]:
    return {
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


def add_example(bucket: List[Dict[str, object]], finding: Dict[str, object]) -> None:
    if len(bucket) < MAX_EXAMPLES_PER_KIND:
        bucket.append(finding)


def parse_patch(path: Path) -> Dict[str, object]:
    r = empty_patch_summary(path.name)
    files_seen = set()
    current_file = "UNKNOWN"
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        for idx, raw in enumerate(fh, start=1):
            raw = raw.rstrip("\n")
            if raw.startswith("diff --git "):
                parts = raw.split()
                if len(parts) >= 4:
                    current_file = parts[3][2:] if parts[3].startswith("b/") else parts[3]
                    if current_file not in files_seen:
                        files_seen.add(current_file)
                        r["sample_files_touched"] = sorted(files_seen)[:15]
                    ctx = path_context(current_file)
                    r["contexts"][ctx] = r["contexts"].get(ctx, 0) + 1  # type: ignore[index]
                continue
            if raw.startswith("+++ b/"):
                current_file = raw[6:]
                if current_file not in files_seen:
                    files_seen.add(current_file)
                    r["sample_files_touched"] = sorted(files_seen)[:15]
                continue
            if raw.startswith("-") and not raw.startswith("---"):
                r["deleted_lines_seen"] += 1  # type: ignore[operator]
                continue
            if not raw.startswith("+") or raw.startswith("+++"):
                continue
            r["added_lines_seen"] += 1  # type: ignore[operator]
            added = raw[1:]
            ctx = path_context(current_file)
            for rule, rx in PATTERNS:
                if not rx.search(added):
                    continue
                sev = severity_for(rule, ctx)
                r["rule_hits"].setdefault(rule, {"hard_finding": 0, "review_note": 0})  # type: ignore[index]
                r["rule_hits"][rule][sev] += 1  # type: ignore[index]
                finding = {"severity": sev, "rule": rule, "file": current_file, "line_no": idx, "context": ctx, "excerpt": redact(added.strip())}
                if sev == "hard_finding":
                    r["hard_findings"] += 1  # type: ignore[operator]
                    add_example(r["hard_examples"], finding)  # type: ignore[arg-type]
                else:
                    r["review_notes"] += 1  # type: ignore[operator]
                    add_example(r["review_examples"], finding)  # type: ignore[arg-type]
    r["files_touched_count"] = len(files_seen)
    return r


def merge_rule_hits(results: List[Dict[str, object]]) -> Dict[str, Dict[str, int]]:
    merged: Dict[str, Dict[str, int]] = {}
    for r in results:
        for rule, counts in r["rule_hits"].items():  # type: ignore[union-attr]
            merged.setdefault(rule, {"hard_finding": 0, "review_note": 0})
            merged[rule]["hard_finding"] += counts.get("hard_finding", 0)
            merged[rule]["review_note"] += counts.get("review_note", 0)
    return merged


def example_lines(items: List[Dict[str, object]]) -> List[str]:
    if not items:
        return ["- none"]
    return [f"- {x['severity']} | {x['rule']} | {x['file']}:{x['line_no']} | context={x['context']} | `{x['excerpt']}`" for x in items]


def main() -> int:
    patch_files = sorted(PATCH_DIR.glob("*.patch"))
    results = [parse_patch(p) for p in patch_files]
    total_hard = sum(int(r["hard_findings"]) for r in results)
    total_notes = sum(int(r["review_notes"]) for r in results)
    rule_hits = merge_rule_hits(results)
    timestamp = datetime.now(timezone.utc).isoformat()

    lines: List[str] = [
        "# Hermes Stage 1 Historical Code Diff Sample Audit Report v0", "", "## 1. Verdict", "", VERDICT, "",
        "## 2. Patch Selection", "", "selected commits:",
    ]
    for c in SELECTED_COMMITS:
        lines.append(f"- {c['sha']}: {c['subject']} — {c['selection_reason']}")
    lines += ["", "selection command summary:"] + [f"- `{c}`" for c in SELECTION_COMMANDS] + ["", "selection limits:"] + [f"- {x}" for x in SELECTION_LIMITS]
    lines += ["", "## 3. Command", "", "`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/audit_historical_code_diffs.py`", "", "## 4. Files Read", "", "- HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_PACKET_V0.md"]
    lines += [f"- {p.relative_to(BASE)}" for p in patch_files]
    lines += ["", "## 5. Files Created", "", "- patches/a542716f3.patch", "- patches/4601f7c18.patch", "- patches/4e0389a4d.patch", "- patches/a998543da.patch", "- audit_historical_code_diffs.py", "- historical_code_diff_audit_report.md", "- historical_code_diff_audit_receipt.json", "", "## 6. Findings Per Patch", ""]
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
        lines += ["- review note examples:"]
        lines += example_lines(r["review_examples"])  # type: ignore[arg-type]
        lines.append("")
    lines += ["## 7. Context Summary", "", f"- selected_patch_count: {len(patch_files)}", f"- total_hard_findings: {total_hard}", f"- total_review_notes: {total_notes}", "- documentation/generated/test contexts were downgraded to review_note unless stronger executable/path pressure appeared.", "- app source, script/deploy, and config/env-like contexts retain hard-finding pressure for relevant rules.", "", "## 8. Rule Hits", ""]
    lines += [f"- {rule}: hard_finding={counts['hard_finding']}, review_note={counts['review_note']}" for rule, counts in sorted(rule_hits.items())] or ["- none"]
    lines += [
        "", "## 9. False Positive / False Negative Notes", "",
        "- False-positive watch: initial/seed commits include generated assets, cache-like package files, docs, reports, and large JSON surfaces; these can inflate review-note counts without representing source risk.",
        "- False-positive watch: token/credential words in comments, tests, docs, schema fields, generated metadata, or lock/package metadata are not automatically credentials; secret-like excerpts are redacted.",
        "- False-negative watch: string/path-context audit does not trace data flow, imports, runtime reachability, build behavior, or whether a command actually executes.",
        "- Sample-selection note: this repository history exposed fewer than 5 bounded non-doc-only code/config commits under the selected pathspec; continuing with 4 commits is explicitly allowed by the packet.",
        "- Execution note: an initial audit command timed out before report/receipt creation; final report/receipt come from the optimized streaming rerun. Treat this as receipt evidence, not a component-quality guarantee.",
        "", "## 10. Limits", "", "- This is a string/path-context audit only.", "- It does not prove semantic compliance, exploitability, production impact, workflow readiness, or VectorFL promotion readiness.", "- It does not inspect repo state beyond extracted patch files.", "- It does not modify input patch files.",
        "", "## 11. VectorFL Recovery Suggestion", "", "receipt:", "  historical code-diff audit ran with command/output evidence", "", "residue:", "  false-positive, false-negative, path-context, and sample-selection notes", "", "candidate:", "  refined code/script/config diff-audit rules if useful", "", "component:", "  still HOLD until repeated validation on real diffs with stable false-positive behavior", "", "STOP:", "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation",
        "", "## 12. WATCH", "", "historical code-diff results may refine candidate rules, but still do not authorize component/workflow/skill/baseline",
        "", "## 13. HOLD", "", "- no source files modified", "- no patches applied", "- no git add", "- no git commit", "- no git reset", "- no git checkout", "- no package install", "- no network", "- no browser", "- no MCP call", "- no cron", "- no Hermes memory edit", "- no Hermes skill edit", "- no Hermes config edit", "- no AGENTS.md update", "- no SKILL.md creation", "- no VectorFL authority update", "- no current-position update", "- no output_manifest update", "- no baseline/workflow/schema/registry/ontology promotion",
        "", "## 14. Hard Stop Confirmation", "", "No mutation/promotion/persistence action was performed. Any request to convert this audit directly into a component, workflow, skill, baseline, current-position update, output_manifest update, cron, memory, config, or VectorFL authority file update remains STOP/HOLD pending separate Codex/User approval.", ""
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    receipt = {
        "verdict": RECEIPT_VERDICT,
        "timestamp": timestamp,
        "selection_commands": SELECTION_COMMANDS,
        "selected_commits": SELECTED_COMMITS,
        "selection_limits": SELECTION_LIMITS,
        "input_patch_files": [str(p.relative_to(BASE)) for p in patch_files],
        "output_files": ["patches/a542716f3.patch", "patches/4601f7c18.patch", "patches/4e0389a4d.patch", "patches/a998543da.patch", "audit_historical_code_diffs.py", "historical_code_diff_audit_report.md", "historical_code_diff_audit_receipt.json"],
        "audit_command": "python3 audit_historical_code_diffs.py",
        "actual_audit_command_from_repo_root": "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/audit_historical_code_diffs.py",
        "exit_code": 0,
        "prior_audit_attempt_timed_out": True,
        "network_used": False,
        "packages_installed": False,
        "subprocess_used_by_audit_script": False,
        "git_used_for_patch_selection_only": True,
        "git_mutation_used": False,
        "source_files_modified": False,
        "patches_applied": False,
        "input_files_modified": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_files_modified": False,
        "current_position_updated": False,
        "output_manifest_updated": False,
        "baseline_workflow_schema_registry_ontology_promoted": False,
        "patch_count": len(patch_files),
        "total_hard_findings": total_hard,
        "total_review_notes": total_notes,
        "rule_hits": rule_hits,
        "per_patch_summary": results,
        "non_actions": ["no source files modified", "no patches applied", "no git add/commit/reset/checkout", "no package install", "no network/browser/MCP", "no Hermes memory/skill/cron/config edit", "no VectorFL authority update", "no current-position/output_manifest update", "no baseline/workflow/schema/registry/ontology promotion"],
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
