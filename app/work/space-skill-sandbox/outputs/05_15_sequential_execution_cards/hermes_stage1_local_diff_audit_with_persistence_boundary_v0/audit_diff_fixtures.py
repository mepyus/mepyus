#!/usr/bin/env python3
"""Stage 1 local deterministic diff fixture audit.

Constraints: Python standard library only; read fixture_diff_A.patch and
fixture_diff_B.patch only; do not inspect repo, call git, use subprocess,
network, or mutate input files.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FIXTURE_FILES = ["fixture_diff_A.patch", "fixture_diff_B.patch"]
REPORT_FILE = "audit_report.md"
RECEIPT_FILE = "audit_receipt.json"
COMMAND = "python3 audit_diff_fixtures.py"

RULE_ORDER = [
    "debug print",
    "hardcoded secret-looking string",
    "bare except",
    "unresolved TODO / FIXME",
    "suspicious shell command: curl pipe bash",
    "suspicious shell command: rm -rf",
    "large deletion marker",
]


def is_added_line(line: str) -> bool:
    return line.startswith("+") and not line.startswith("+++")


def is_removed_line(line: str) -> bool:
    return line.startswith("-") and not line.startswith("---")


def added_payload(line: str) -> str:
    return line[1:]


def detect_fixture(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings = []
    removed_count = 0

    for idx, line in enumerate(lines, start=1):
        if is_removed_line(line):
            removed_count += 1
        if not is_added_line(line):
            continue
        payload = added_payload(line)
        stripped = payload.strip()
        lower = payload.lower()

        if "print(" in payload:
            findings.append({
                "rule": "debug print",
                "line": idx,
                "evidence": payload,
                "severity": "medium",
                "note": "Added print() statement in code diff.",
            })

        secret_terms = ["sk_live", "api_key", "token =", "password =", "secret ="]
        if any(term in lower for term in secret_terms):
            findings.append({
                "rule": "hardcoded secret-looking string",
                "line": idx,
                "evidence": payload,
                "severity": "high",
                "note": "Added line contains secret-looking token/API-key marker.",
            })

        if stripped == "except:":
            findings.append({
                "rule": "bare except",
                "line": idx,
                "evidence": payload,
                "severity": "medium",
                "note": "Added bare except may hide failures.",
            })

        if "TODO" in payload or "FIXME" in payload:
            findings.append({
                "rule": "unresolved TODO / FIXME",
                "line": idx,
                "evidence": payload,
                "severity": "low",
                "note": "Added unresolved TODO/FIXME marker.",
            })

        if "curl" in payload and "|" in payload and "bash" in payload:
            findings.append({
                "rule": "suspicious shell command: curl pipe bash",
                "line": idx,
                "evidence": payload,
                "severity": "high",
                "note": "Added curl pipe bash command.",
            })

        if "rm -rf" in payload:
            findings.append({
                "rule": "suspicious shell command: rm -rf",
                "line": idx,
                "evidence": payload,
                "severity": "high",
                "note": "Added rm -rf command.",
            })

    if removed_count >= 5:
        findings.append({
            "rule": "large deletion marker",
            "line": None,
            "evidence": f"{removed_count} removed lines",
            "severity": "medium",
            "note": "Fixture removes 5 or more lines.",
        })

    return {
        "file": path.name,
        "removed_line_count": removed_count,
        "finding_count": len(findings),
        "findings": findings,
    }


def count_rule_hits(results: list[dict]) -> dict:
    counts = {rule: 0 for rule in RULE_ORDER}
    for result in results:
        for finding in result["findings"]:
            counts[finding["rule"]] = counts.get(finding["rule"], 0) + 1
    return counts


def md_escape(value: object) -> str:
    return str(value).replace("|", "\\|")


def write_report(results: list[dict], rule_hits: dict) -> None:
    files_read = [str(BASE_DIR / name) for name in FIXTURE_FILES]
    files_created = [
        str(BASE_DIR / "fixture_diff_A.patch"),
        str(BASE_DIR / "fixture_diff_B.patch"),
        str(BASE_DIR / "audit_diff_fixtures.py"),
        str(BASE_DIR / REPORT_FILE),
        str(BASE_DIR / RECEIPT_FILE),
    ]

    lines = []
    lines.append("# Hermes Stage 1 Local Diff Audit Report v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_STAGE1_LOCAL_DIFF_AUDIT_EXECUTED_WITH_WATCH]")
    lines.append("")
    lines.append("## 2. Command")
    lines.append("")
    lines.append(f"- command: `{COMMAND}`")
    lines.append("- execution mode: one-shot local Python standard-library script")
    lines.append("- exit status: 0 if this report and receipt were written")
    lines.append("")
    lines.append("## 3. Files Read")
    lines.append("")
    for item in files_read:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 4. Files Created")
    lines.append("")
    for item in files_created:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 5. Findings Per Fixture")
    lines.append("")
    for result in results:
        lines.append(f"### {result['file']}")
        lines.append("")
        lines.append(f"- removed line count: {result['removed_line_count']}")
        lines.append(f"- finding count: {result['finding_count']}")
        if result["findings"]:
            lines.append("")
            lines.append("| Rule | Line | Severity | Evidence | Note |")
            lines.append("|---|---:|---|---|---|")
            for finding in result["findings"]:
                line_value = "n/a" if finding["line"] is None else finding["line"]
                lines.append(
                    f"| {md_escape(finding['rule'])} | {line_value} | {md_escape(finding['severity'])} | `{md_escape(finding['evidence'])}` | {md_escape(finding['note'])} |"
                )
        else:
            lines.append("- no rule hits")
        lines.append("")
    lines.append("## 6. Rule Hits")
    lines.append("")
    lines.append("| Rule | Hits |")
    lines.append("|---|---:|")
    for rule in RULE_ORDER:
        lines.append(f"| {rule} | {rule_hits.get(rule, 0)} |")
    lines.append("")
    lines.append("## 7. False-Positive Notes")
    lines.append("")
    lines.append("- This audit uses simple string detection over added diff lines only.")
    lines.append("- A hit is a review signal, not proof of exploitability, policy violation, or production impact.")
    lines.append("- `api_key`, `sk_live`, `curl ... | bash`, and `rm -rf` are intentionally synthetic fixture signals.")
    lines.append("- Large deletion marker is count-based and does not prove harmful deletion.")
    lines.append("")
    lines.append("## 8. Limits")
    lines.append("")
    lines.append("- No AST parsing, shell parsing, taint analysis, or repository context was used.")
    lines.append("- The script did not call git, subprocess, network, browser, MCP, package installers, or external apps.")
    lines.append("- The script read only the two fixture patch files and wrote only the declared report and receipt.")
    lines.append("- Script success is execution evidence, not semantic compliance or VectorFL authority.")
    lines.append("")
    lines.append("## 9. VectorFL Recovery Suggestion")
    lines.append("")
    lines.append("receipt:")
    lines.append("  audit ran, with command/output evidence")
    lines.append("")
    lines.append("residue:")
    lines.append("  repeated risk pattern if found")
    lines.append("")
    lines.append("candidate:")
    lines.append("  reusable diff-audit rules if useful")
    lines.append("")
    lines.append("component:")
    lines.append("  not yet; only after repeated validation")
    lines.append("")
    lines.append("STOP:")
    lines.append("  any attempt to patch files, commit changes, create skill, write memory, schedule cron, change config, call MCP, use network, or promote audit rules to baseline/workflow/schema/registry/ontology")
    lines.append("")
    lines.append("## 10. WATCH")
    lines.append("")
    lines.append("- local diff audit may become candidate rules, but not component/workflow/skill/baseline yet")
    lines.append("- local execution permission must not be confused with VectorFL authority update permission")
    lines.append("- script success != semantic compliance")
    lines.append("- receipt != authority")
    lines.append("- component candidate != workflow")
    lines.append("- candidate rules remain proposal-only until repeated validation and separate approval")
    lines.append("")
    lines.append("## 11. HOLD")
    lines.append("")
    hold_items = [
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
    for item in hold_items:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## 12. Hard Stop Confirmation")
    lines.append("")
    for item in hold_items:
        lines.append(item)

    (BASE_DIR / REPORT_FILE).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_receipt(results: list[dict], rule_hits: dict) -> None:
    receipt = {
        "verdict": "[HERMES_STAGE1_LOCAL_DIFF_AUDIT_RECEIPT]",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "command": COMMAND,
        "input_files": [str(BASE_DIR / name) for name in FIXTURE_FILES],
        "output_files": [
            str(BASE_DIR / "fixture_diff_A.patch"),
            str(BASE_DIR / "fixture_diff_B.patch"),
            str(BASE_DIR / "audit_diff_fixtures.py"),
            str(BASE_DIR / REPORT_FILE),
            str(BASE_DIR / RECEIPT_FILE),
        ],
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
        "rule_hits": rule_hits,
        "notes": [
            "Stage 1 local deterministic execution only.",
            "Fixture patch files are synthetic and were not applied.",
            "Receipt is evidence only, not VectorFL authority.",
            "Reusable diff-audit rules are candidate only, not component/workflow/skill/baseline.",
        ],
    }
    (BASE_DIR / RECEIPT_FILE).write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    results = [detect_fixture(BASE_DIR / name) for name in FIXTURE_FILES]
    rule_hits = count_rule_hits(results)
    write_report(results, rule_hits)
    write_receipt(results, rule_hits)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
