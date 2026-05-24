#!/usr/bin/env python3
"""Stage 1 real-ish diff fixture audit expansion.

Stdlib only. Reads declared fixture patch files in this directory, writes a
markdown report and JSON receipt. Does not inspect the repo, call git, use
subprocess/network, or mutate inputs.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FIXTURES = [
    "fixture_actual_risk.patch",
    "fixture_clean_refactor.patch",
    "fixture_config_risk.patch",
    "fixture_docs_example.patch",
    "fixture_generated_file.patch",
    "fixture_test_fixture.patch",
]
REPORT_FILE = "realish_fixture_expansion_report.md"
RECEIPT_FILE = "realish_fixture_expansion_receipt.json"
COMMAND = (
    "python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/"
    "hermes_stage1_local_diff_audit_realish_fixture_expansion_v0/audit_realish_fixtures.py"
)


def is_added(line: str) -> bool:
    return line.startswith("+") and not line.startswith("+++")


def is_removed(line: str) -> bool:
    return line.startswith("-") and not line.startswith("---")


def path_from_diff(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("+++ b/"):
            return line[6:]
    return "unknown"


def context_for(path: str) -> str:
    if path.startswith("docs/"):
        return "docs"
    if path.startswith("tests/") or "/test" in path or "fixture" in path:
        return "test"
    if path.startswith("generated/") or "/generated/" in path:
        return "generated"
    if path.startswith("config/") or path.endswith(".env"):
        return "config"
    return "code"


def classify(rule: str, context: str, payload: str) -> tuple[str, str]:
    if context == "docs":
        return "review_note", "documentation-context example; not executable code."
    if context == "test":
        if rule in {"hardcoded secret-looking string", "debug print"}:
            return "review_note", "test fixture context; review only unless copied to production."
    if context == "generated":
        return "review_note", "generated context; fix upstream or generator before manual patching."
    if rule == "unresolved TODO / FIXME":
        if context in {"code", "config"} and any(marker in payload.lower() for marker in ["production", "launch", "verification"]):
            return "hard_finding", "TODO/FIXME is tied to production/launch risk."
        return "review_note", "TODO/FIXME requires review but is not a hard finding alone."
    if context == "config" and rule == "hardcoded secret-looking string":
        return "hard_finding", "secret-looking value in config context."
    return "hard_finding", "risk pattern in executable or operational context."


def detect(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    target_path = path_from_diff(lines)
    context = context_for(target_path)
    removed = sum(1 for line in lines if is_removed(line))
    findings = []
    for idx, line in enumerate(lines, start=1):
        if not is_added(line):
            continue
        payload = line[1:]
        stripped = payload.strip()
        lower = payload.lower()
        rules = []
        if "print(" in payload:
            rules.append("debug print")
        if any(term in lower for term in ["sk_live", "api_key", "token =", "password =", "secret =", "stripe_secret"]):
            rules.append("hardcoded secret-looking string")
        if stripped == "except:":
            rules.append("bare except")
        if "TODO" in payload or "FIXME" in payload:
            rules.append("unresolved TODO / FIXME")
        if "curl" in payload and "|" in payload and "bash" in payload:
            rules.append("suspicious shell command: curl pipe bash")
        if "rm -rf" in payload:
            rules.append("suspicious shell command: rm -rf")
        for rule in rules:
            severity, note = classify(rule, context, payload)
            findings.append({
                "rule": rule,
                "line": idx,
                "severity": severity,
                "context": context,
                "evidence": payload,
                "note": note,
            })
    if removed >= 5:
        severity, note = ("review_note", "large deletion marker is count-based and requires context.")
        findings.append({
            "rule": "large deletion marker",
            "line": None,
            "severity": severity,
            "context": context,
            "evidence": f"{removed} removed lines",
            "note": note,
        })
    hard = sum(1 for item in findings if item["severity"] == "hard_finding")
    notes = sum(1 for item in findings if item["severity"] == "review_note")
    return {
        "fixture": path.name,
        "target_path": target_path,
        "context": context,
        "removed_line_count": removed,
        "hard_findings": hard,
        "review_notes": notes,
        "findings": findings,
    }


def aggregate(results: list[dict]) -> dict:
    rules: dict[str, int] = {}
    contexts: dict[str, dict[str, int]] = {}
    for result in results:
        contexts.setdefault(result["context"], {"hard_findings": 0, "review_notes": 0})
        contexts[result["context"]]["hard_findings"] += result["hard_findings"]
        contexts[result["context"]]["review_notes"] += result["review_notes"]
        for finding in result["findings"]:
            rules[finding["rule"]] = rules.get(finding["rule"], 0) + 1
    return {"rule_hits": rules, "context_summary": contexts}


def esc(value: object) -> str:
    return str(value).replace("|", "\\|")


def write_report(results: list[dict], summary: dict) -> None:
    out = []
    out.extend([
        "# Hermes Stage 1 Local Diff Audit Real-ish Fixture Expansion Report v0",
        "",
        "## 1. Verdict",
        "",
        "[HERMES_STAGE1_LOCAL_DIFF_AUDIT_REALISH_FIXTURE_EXPANSION_EXECUTED_WITH_WATCH]",
        "",
        "## 2. Command",
        "",
        f"- command: `{COMMAND}`",
        "- execution mode: one-shot local Python standard-library script",
        "- exit status: 0 if this report and receipt were written",
        "",
        "## 3. Files Read",
        "",
    ])
    for name in FIXTURES:
        out.append(f"- {BASE_DIR / name}")
    out.extend(["", "## 4. Files Created", ""])
    for name in [*FIXTURES, "audit_realish_fixtures.py", REPORT_FILE, RECEIPT_FILE]:
        out.append(f"- {BASE_DIR / name}")
    out.extend(["", "## 5. Findings Per Fixture", ""])
    for result in results:
        out.extend([
            f"### {result['fixture']}",
            "",
            f"- target path: `{result['target_path']}`",
            f"- context: `{result['context']}`",
            f"- hard findings: {result['hard_findings']}",
            f"- review notes: {result['review_notes']}",
        ])
        if result["findings"]:
            out.extend([
                "",
                "| Rule | Severity | Context | Line | Evidence | Note |",
                "|---|---|---|---:|---|---|",
            ])
            for item in result["findings"]:
                line = "n/a" if item["line"] is None else item["line"]
                out.append(
                    f"| {esc(item['rule'])} | {esc(item['severity'])} | {esc(item['context'])} | {line} | `{esc(item['evidence'])}` | {esc(item['note'])} |"
                )
        else:
            out.append("- no findings")
        out.append("")
    out.extend([
        "## 6. Context Summary",
        "",
        "| Context | Hard findings | Review notes |",
        "|---|---:|---:|",
    ])
    for context, counts in sorted(summary["context_summary"].items()):
        out.append(f"| {context} | {counts['hard_findings']} | {counts['review_notes']} |")
    out.extend(["", "## 7. Rule Hits", "", "| Rule | Hits |", "|---|---:|"])
    for rule, count in sorted(summary["rule_hits"].items()):
        out.append(f"| {rule} | {count} |")
    out.extend([
        "",
        "## 8. False-Positive / Borderline Notes",
        "",
        "- Docs and test fixtures can contain dangerous-looking strings as examples; these are review notes unless copied into production code/config.",
        "- Generated files should usually be fixed upstream or through the generator, not patched manually.",
        "- Config files with token/password/secret-looking values are hard findings even without external side effects.",
        "- TODO/FIXME is review-only unless paired with production/launch/security risk or high-risk code/shell context.",
        "",
        "## 9. Limits",
        "",
        "- This is string and path-context detection only.",
        "- No AST parsing, shell parsing, taint analysis, or repository context was used.",
        "- The script did not call git, subprocess, network, browser, MCP, package installers, or external apps.",
        "- Script success is receipt evidence, not semantic compliance or VectorFL authority.",
        "",
        "## 10. VectorFL Recovery Suggestion",
        "",
        "receipt:",
        "  real-ish fixture expansion audit ran, with command/output evidence",
        "",
        "residue:",
        "  false-positive, context, generated-file, and config-risk behavior notes",
        "",
        "candidate:",
        "  refined diff-audit rules with path-context distinction",
        "",
        "component:",
        "  still not yet; needs repeated validation on real diffs and review of false-positive behavior",
        "",
        "STOP:",
        "  any attempt to patch files, commit changes, create skill, write memory, schedule cron, change config, call MCP, use network, or promote audit rules to baseline/workflow/schema/registry/ontology",
        "",
        "## 11. WATCH",
        "",
        "- rule quality improved but remains candidate only",
        "- path-context heuristics can hide real issues if abused",
        "- generated/test/docs contexts are not automatic safe zones",
        "- config context is higher persistence risk",
        "- receipt != authority",
        "- candidate rules != component/workflow/skill/baseline",
        "",
        "## 12. HOLD",
        "",
    ])
    hold = [
        "no source files modified",
        "no patches applied",
        "no git add",
        "no git commit",
        "no repo-wide search",
        "no package install",
        "no network",
        "no browser",
        "no MCP call",
        "no cron",
        "no Hermes memory edit",
        "no Hermes skill edit",
        "no Hermes config edit",
        "no AGENTS.md update",
        "no SKILL.md creation",
        "no VectorFL authority update",
        "no current-position update",
        "no output_manifest update",
        "no baseline/workflow/schema/registry/ontology promotion",
    ]
    out.extend(f"- {item}" for item in hold)
    out.extend(["", "## 13. Hard Stop Confirmation", ""])
    out.extend(hold)
    (BASE_DIR / REPORT_FILE).write_text("\n".join(out) + "\n", encoding="utf-8")


def write_receipt(results: list[dict], summary: dict) -> None:
    receipt = {
        "verdict": "[HERMES_STAGE1_LOCAL_DIFF_AUDIT_REALISH_FIXTURE_EXPANSION_RECEIPT]",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "command": COMMAND,
        "input_files": [str(BASE_DIR / name) for name in FIXTURES],
        "output_files": [str(BASE_DIR / name) for name in [*FIXTURES, "audit_realish_fixtures.py", REPORT_FILE, RECEIPT_FILE]],
        "exit_code": 0,
        "network_used": False,
        "packages_installed": False,
        "subprocess_used": False,
        "git_used": False,
        "input_files_modified": False,
        "memory_modified": False,
        "skill_modified": False,
        "cron_modified": False,
        "config_modified": False,
        "vectorfl_authority_files_modified": False,
        "source_files_modified": False,
        "patches_applied": False,
        "repo_wide_search_used": False,
        "browser_used": False,
        "mcp_used": False,
        "current_position_updated": False,
        "output_manifest_updated": False,
        "baseline_workflow_schema_registry_ontology_promoted": False,
        "results": results,
        "summary": summary,
        "notes": [
            "Stage 1 local deterministic execution only.",
            "Fixture patch files are synthetic and were not applied.",
            "Receipt is evidence only, not VectorFL authority.",
            "Refined diff-audit rules are candidate only, not component/workflow/skill/baseline.",
        ],
    }
    (BASE_DIR / RECEIPT_FILE).write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    results = [detect(BASE_DIR / name) for name in FIXTURES]
    summary = aggregate(results)
    write_report(results, summary)
    write_receipt(results, summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
