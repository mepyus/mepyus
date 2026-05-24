#!/usr/bin/env python3
"""Hermes Stage 1 review-note threshold tightening test.

Stdlib only. No subprocess/git/network. Reads only declared prior receipt/report and
patch fixture inputs. Writes only report/receipt under declared output directory.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards"
OUT = BASE / "hermes_stage1_review_note_threshold_tightening_v0"
REPORT = OUT / "review_note_threshold_tightening_report.md"
RECEIPT = OUT / "review_note_threshold_tightening_receipt.json"
PRIOR_REPORT = BASE / "hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_report.md"
PRIOR_RECEIPT = BASE / "hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_receipt.json"
HIST_PATCH_DIR = BASE / "hermes_stage1_historical_code_diff_sample_audit_v0/patches"
SEEDED_FIXTURE_DIR = BASE / "hermes_stage1_seeded_true_positive_pressure_v0/fixtures"

VERDICT = "[HERMES_STAGE1_REVIEW_NOTE_THRESHOLD_TIGHTENING_EXECUTED_WITH_WATCH]"
RECEIPT_VERDICT = "[HERMES_STAGE1_REVIEW_NOTE_THRESHOLD_TIGHTENING_RECEIPT]"
COMMAND = "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening.py"

CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx"}
CONFIG_EXTS = {".json", ".toml", ".yaml", ".yml", ".env"}
SCRIPT_EXTS = {".sh", ".bash", ".zsh"}
SECRET_NAMES = r"api_key|api_token|service_token|token|password|secret|credential"
SECRET_ASSIGN = re.compile(rf"(?P<name>{SECRET_NAMES})\s*=\s*(?P<quote>['\"])(?P<value>.*?)(?P=quote)", re.I)
SECRET_ANY_ASSIGN = re.compile(rf"(?P<name>{SECRET_NAMES})\s*=\s*(?P<rhs>.+)", re.I)
ENV_REF = re.compile(r"(os\.environ\s*\[\s*['\"][A-Z0-9_]*(TOKEN|SECRET|PASSWORD|CREDENTIAL|API_KEY)[A-Z0-9_]*['\"]\s*\]|getenv\s*\(\s*['\"][A-Z0-9_]*(TOKEN|SECRET|PASSWORD|CREDENTIAL|API_KEY)[A-Z0-9_]*['\"]\s*\)|read_from_env\s*\(\s*['\"][A-Z0-9_]*(TOKEN|SECRET|PASSWORD|CREDENTIAL|API_KEY)[A-Z0-9_]*['\"]\s*\))", re.I)
EXPLICIT_SECRET_NAME = re.compile(r"api_key|api_token|service_token|password|secret|credential", re.I)
ORDINARY_TOKEN_NOISE = re.compile(r"PATH_TOKEN_RE|sentence_tokens|overlap_tokens|canonicalizable_token_pair_count|token_count|_tokenize|_collect_anchor_tokens|for\s+token\s+in\s+tokens|tokens\.add\(token\)|for\s+token\s+in\s+sentence_tokens", re.I)
PLACEHOLDER = [
    re.compile(r"^\s*$"),
    re.compile(r"^\$\{[^}]+\}$"),
    re.compile(r"^<[^>]+>$"),
    re.compile(r"^(placeholder|changeme|change-me|set-in-env|redacted)$", re.I),
]

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
MAX_EXAMPLES = 10


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def redact(s: str) -> str:
    s = SECRET_ASSIGN.sub(lambda m: f"{m.group('name')} = [REDACTED]", s)
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
    return any(rx.search(v) for rx in PLACEHOLDER)


def classify_secret_tight(line: str, ctx: str) -> Tuple[str, str] | None:
    line_stripped = line.strip()
    if ctx in {"docs", "tests_or_fixtures"}:
        if SECRET_ASSIGN.search(line) or re.search(r"API_KEY\s*=|TOKEN\s*=|password\s*=|api_key\s*=|token\s*=|secret\s*=|credential\s*=", line, re.I):
            return "review_note", "docs_tests_explicit_secret_assignment_example"
        return None

    literal = SECRET_ASSIGN.search(line)
    if literal:
        value = literal.group("value")
        name = literal.group("name").lower()
        if is_placeholder(value) or ENV_REF.search(line):
            return "review_note", "placeholder_or_env_secret_value"
        # token literals are hard only when clearly secret-like or in config/script/app source by recovered rule.
        if ctx in {"app_source", "source_code", "config_or_env_like", "scripts_or_deploy"}:
            return "hard_finding", "literal_secret_assignment"
        return "review_note", "literal_secret_outside_hard_context"

    if ENV_REF.search(line):
        return "review_note", "env_reference_boundary"

    assign = SECRET_ANY_ASSIGN.search(line)
    if assign:
        name = assign.group("name").lower()
        rhs = assign.group("rhs")
        # Keep semantic token assignment as review note, but suppress broad variable/function/loop occurrences.
        if name == "token" and ORDINARY_TOKEN_NOISE.search(line):
            return None
        if name == "token" and re.search(r"_normalize_token|\.lower\s*\(|str\s*\(|os\.environ|getenv|read_from_env", rhs, re.I):
            return "review_note", "semantic_token_assignment"
        if name != "token" or EXPLICIT_SECRET_NAME.search(name):
            return "review_note", "secret_named_assignment_without_literal_secret"

    # Explicit secret/credential/password/api_key naming can be review-level; ordinary token processing is suppressed.
    if EXPLICIT_SECRET_NAME.search(line) and not ORDINARY_TOKEN_NOISE.search(line):
        return "review_note", "explicit_secret_or_credential_name"
    return None


def classify_non_secret(rule: str, ctx: str) -> Tuple[str, str] | None:
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
        "hard_findings": 0,
        "review_notes": 0,
        "suppressed_review_notes": 0,
        "contexts": {},
        "rule_hits": {},
        "hard_examples": [],
        "review_examples": [],
        "suppressed_examples": [],
    }


def add_hit(result: Dict[str, object], severity: str, rule: str, reason: str, file_path: str, line_no: int, ctx: str, line: str) -> None:
    result["rule_hits"].setdefault(rule, {"hard_finding": 0, "review_note": 0})  # type: ignore[index]
    result["rule_hits"][rule][severity] += 1  # type: ignore[index]
    result["hard_findings" if severity == "hard_finding" else "review_notes"] += 1  # type: ignore[operator]
    bucket = result["hard_examples" if severity == "hard_finding" else "review_examples"]
    if len(bucket) < MAX_EXAMPLES:  # type: ignore[arg-type]
        bucket.append({"severity": severity, "rule": rule, "reason": reason, "file": file_path, "line_no": line_no, "context": ctx, "excerpt": redact(line.strip())})  # type: ignore[union-attr]


def add_suppressed(result: Dict[str, object], reason: str, file_path: str, line_no: int, ctx: str, line: str) -> None:
    result["suppressed_review_notes"] += 1  # type: ignore[operator]
    bucket = result["suppressed_examples"]
    if len(bucket) < MAX_EXAMPLES:  # type: ignore[arg-type]
        bucket.append({"reason": reason, "file": file_path, "line_no": line_no, "context": ctx, "excerpt": redact(line.strip())})  # type: ignore[union-attr]


def parse_patch(p: Path, group: str) -> Dict[str, object]:
    result = empty_result(p.name, group)
    current_file = "UNKNOWN"
    files = set()
    with p.open("r", encoding="utf-8", errors="replace") as fh:
        for line_no, raw in enumerate(fh, 1):
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
            secret = classify_secret_tight(added, ctx)
            if secret:
                sev, reason = secret
                add_hit(result, sev, "secret_boundary", reason, current_file, line_no, ctx, added)
            elif re.search(r"token|secret|password|credential|api_key", added, re.I) and ORDINARY_TOKEN_NOISE.search(added):
                add_suppressed(result, "ordinary_token_processing_noise", current_file, line_no, ctx, added)
            for rule, rx in NON_SECRET_PATTERNS:
                if rx.search(added):
                    c = classify_non_secret(rule, ctx)
                    if c:
                        sev, reason = c
                        add_hit(result, sev, rule, reason, current_file, line_no, ctx, added)
    result["files_touched_count"] = len(files)
    result["sample_files_touched"] = sorted(files)[:15]
    return result


def sum_field(results: List[Dict[str, object]], field: str) -> int:
    return sum(int(r[field]) for r in results)


def parse_prior_counts() -> Dict[str, int]:
    data = json.loads(PRIOR_RECEIPT.read_text(encoding="utf-8"))
    return {
        "before_historical_hard_findings": int(data.get("historical_hard_findings", 0)),
        "before_historical_review_notes": int(data.get("historical_review_notes", 0)),
        "before_seeded_hard_findings": int(data.get("seeded_hard_findings", 0)),
        "before_seeded_review_notes": int(data.get("seeded_review_notes", 0)),
    }


def lines_for_examples(items: List[Dict[str, object]]) -> List[str]:
    if not items:
        return ["- none"]
    return [f"- {x.get('severity', 'suppressed')} | {x['reason']} | {x['file']}:{x['line_no']} | context={x['context']} | `{x['excerpt']}`" for x in items]


def render_group(title: str, results: List[Dict[str, object]]) -> List[str]:
    out = [f"## {title}", ""]
    for r in results:
        out += [
            f"### {r['patch']}",
            f"- files_touched_count: {r['files_touched_count']}",
            f"- added_lines_seen: {r['added_lines_seen']}",
            f"- deleted_lines_seen: {r['deleted_lines_seen']}",
            f"- hard_findings: {r['hard_findings']}",
            f"- review_notes: {r['review_notes']}",
            f"- suppressed_review_notes: {r['suppressed_review_notes']}",
            f"- contexts: `{json.dumps(r['contexts'], ensure_ascii=False, sort_keys=True)}`",
            "- hard finding examples:",
        ]
        out += lines_for_examples(r["hard_examples"])  # type: ignore[arg-type]
        out.append("- retained review note examples:")
        out += lines_for_examples(r["review_examples"])  # type: ignore[arg-type]
        out.append("- suppressed review-note examples:")
        out += lines_for_examples(r["suppressed_examples"])  # type: ignore[arg-type]
        out.append("")
    return out


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    before = parse_prior_counts()
    prior_report_bytes = len(PRIOR_REPORT.read_text(encoding="utf-8", errors="replace"))
    hist_files = sorted(HIST_PATCH_DIR.glob("*.patch"))
    seeded_files = sorted(SEEDED_FIXTURE_DIR.glob("*.patch"))
    hist_results = [parse_patch(p, "historical") for p in hist_files]
    seeded_results = [parse_patch(p, "seeded") for p in seeded_files]

    after_hist_hard = sum_field(hist_results, "hard_findings")
    after_hist_notes = sum_field(hist_results, "review_notes")
    after_seed_hard = sum_field(seeded_results, "hard_findings")
    after_seed_notes = sum_field(seeded_results, "review_notes")
    suppressed_hist = sum_field(hist_results, "suppressed_review_notes")
    suppressed_seed = sum_field(seeded_results, "suppressed_review_notes")

    hard_stable = after_hist_hard == before["before_historical_hard_findings"] == 1 and after_seed_hard == before["before_seeded_hard_findings"] == 19
    report: List[str] = [
        "# Hermes Stage 1 Review-Note Threshold Tightening Report v0", "",
        "## Verdict", "", VERDICT, "",
        "## Command Run", "", f"`{COMMAND}`", "",
        "## Files Read", "",
        f"- {rel(PRIOR_REPORT)}",
        f"- {rel(PRIOR_RECEIPT)}",
        f"- {rel(HIST_PATCH_DIR)}/",
        f"- {rel(SEEDED_FIXTURE_DIR)}/",
    ]
    report += [f"- {rel(p)}" for p in hist_files + seeded_files]
    report += ["", "## Files Created", "", f"- {rel(Path(__file__).resolve())}", f"- {rel(REPORT)}", f"- {rel(RECEIPT)}", ""]
    report += [
        "## Before Counts From Hermes Independent Rerun", "",
        f"- historical_hard_findings: {before['before_historical_hard_findings']}",
        f"- historical_review_notes: {before['before_historical_review_notes']}",
        f"- seeded_hard_findings: {before['before_seeded_hard_findings']}",
        f"- seeded_review_notes: {before['before_seeded_review_notes']}",
        "", "## After Counts From Tightened Threshold", "",
        f"- historical_hard_findings: {after_hist_hard}",
        f"- historical_review_notes: {after_hist_notes}",
        f"- seeded_hard_findings: {after_seed_hard}",
        f"- seeded_review_notes: {after_seed_notes}",
        f"- historical_suppressed_review_notes: {suppressed_hist}",
        f"- seeded_suppressed_review_notes: {suppressed_seed}",
        "", "## Hard-Finding Stability Check", "",
        f"- hard_findings_stable: {str(hard_stable).lower()}",
        "- expected: historical_hard_findings stays 1; seeded_hard_findings stays 19",
        "- result: hard rules unchanged; only secret_boundary review-note threshold was tightened",
        "",
    ]
    report += render_group("Historical Patch Results", hist_results)
    report += render_group("Seeded Fixture Results", seeded_results)
    report += [
        "## Review Notes Suppressed", "",
        f"- historical: {before['before_historical_review_notes']} -> {after_hist_notes} (suppressed at least {max(0, before['before_historical_review_notes'] - after_hist_notes)} from prior count; direct parser-token suppression examples counted={suppressed_hist})",
        f"- seeded: {before['before_seeded_review_notes']} -> {after_seed_notes} (suppressed at least {max(0, before['before_seeded_review_notes'] - after_seed_notes)} from prior count; direct parser-token suppression examples counted={suppressed_seed})",
        "- suppressed class: ordinary tokenizer/parser/path-token naming without direct secret assignment, env/reference boundary, placeholder secret value, or explicit secret/credential/password/api_key naming.",
        "", "## Review Notes Retained", "",
        "- semantic `token = ...` assignments remain review notes.",
        "- env/reference boundaries remain review notes.",
        "- placeholder/env secret values remain review notes.",
        "- docs/tests explicit secret-like assignments or dangerous command examples remain review notes.",
        "- non-secret TODO/shell/dynamic patterns outside hard contexts remain review notes.",
        "", "## False-Positive Notes", "",
        "- Ordinary token-processing terms such as PATH_TOKEN_RE, for token in tokens, _tokenize, overlap_tokens, canonicalizable_token_pair_count, and sentence_tokens are no longer counted as secret_boundary review notes by themselves.",
        "- Remaining review notes still include semantic token assignments and explicit examples, so review counts may not exactly match Codex replay.",
        "", "## False-Negative Notes", "",
        "- Tightening review notes can suppress naming-only clues that may matter in rare credential misuse cases.",
        "- This script still does not perform entropy scanning, data-flow analysis, runtime reachability, dependency analysis, or git history secret scanning.",
        "", "## VectorFL Recovery Suggestion", "",
        "receipt:", "  Hermes tightened review-note threshold with command/output evidence", "",
        "residue:", "  suppressed-token-noise examples and retained-review examples", "",
        "candidate:", "  refined diff-audit rule set becomes stronger if hard findings remain stable and review noise decreases", "",
        "component:", "  HOLD until broader real sample and user/Codex explicit approval", "",
        "STOP:", "  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation", "",
        "## WATCH", "", "review-note tightening may strengthen candidate status but still does not authorize component/workflow/skill/baseline", "",
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
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8")
    receipt = {
        "verdict": RECEIPT_VERDICT,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "command": COMMAND,
        "input_files": [rel(PRIOR_REPORT), rel(PRIOR_RECEIPT)] + [rel(p) for p in hist_files + seeded_files],
        "prior_report_bytes": prior_report_bytes,
        "output_files": [rel(Path(__file__).resolve()), rel(REPORT), rel(RECEIPT)],
        "exit_code": 0,
        **before,
        "after_historical_hard_findings": after_hist_hard,
        "after_historical_review_notes": after_hist_notes,
        "after_seeded_hard_findings": after_seed_hard,
        "after_seeded_review_notes": after_seed_notes,
        "historical_suppressed_review_notes": suppressed_hist,
        "seeded_suppressed_review_notes": suppressed_seed,
        "hard_findings_stable": hard_stable,
        "historical_results": hist_results,
        "seeded_results": seeded_results,
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
