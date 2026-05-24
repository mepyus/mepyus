#!/usr/bin/env python3
"""Codex-side audit of extracted historical patch fixtures.

Reads only patches/*.patch under this sandbox directory and writes one report
and one receipt. This is evidence for recovery classification, not a component
or authority surface.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PATCH_DIR = BASE_DIR / "patches"
REPORT = BASE_DIR / "historical_patch_audit_codex_report.md"
RECEIPT = BASE_DIR / "historical_patch_audit_codex_receipt.json"


def is_added(line: str) -> bool:
    return line.startswith("+") and not line.startswith("+++")


def target_path(lines: list[str]) -> str:
    for line in lines:
        if line.startswith("+++ b/"):
            return line[6:]
    return "unknown"


def context(path: str) -> str:
    if path.startswith("docs/") or path.endswith(".md"):
        return "docs"
    if path.startswith("tests/") or "/test" in path or "fixture" in path:
        return "test"
    if path.startswith("generated/") or "/generated/" in path:
        return "generated"
    if path.startswith("config/") or path.endswith(".env"):
        return "config"
    if path.startswith("scripts/") or path.endswith(".sh"):
        return "script"
    return "code"


def classify(rule: str, ctx: str, payload: str) -> tuple[str, str]:
    low = payload.lower()
    if ctx == "docs":
        return "review_note", "documentation/markdown context; not executable by itself."
    if ctx in {"test", "generated"}:
        return "review_note", f"{ctx} context; review but do not treat as hard finding alone."
    if rule == "unresolved TODO / FIXME":
        if any(word in low for word in ["production", "launch", "security", "secret", "credential"]):
            return "hard_finding", "TODO/FIXME tied to production/security wording."
        return "review_note", "TODO/FIXME requires review but is not a hard finding alone."
    if ctx == "config":
        return "hard_finding", "risk pattern in config context."
    return "hard_finding", "risk pattern in executable or operational context."


def detect(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    tgt = target_path(lines)
    ctx = context(tgt)
    findings = []
    for idx, line in enumerate(lines, 1):
        if not is_added(line):
            continue
        payload = line[1:]
        stripped = payload.strip()
        low = payload.lower()
        rules = []
        if "print(" in payload:
            rules.append("debug print")
        if any(term in low for term in ["sk_live", "api_key", "token =", "password =", "secret =", "credential"]):
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
            severity, note = classify(rule, ctx, payload)
            findings.append({
                "rule": rule,
                "severity": severity,
                "line": idx,
                "context": ctx,
                "evidence": payload,
                "note": note,
            })
    return {
        "patch": path.name,
        "target_path": tgt,
        "context": ctx,
        "hard_findings": sum(1 for f in findings if f["severity"] == "hard_finding"),
        "review_notes": sum(1 for f in findings if f["severity"] == "review_note"),
        "findings": findings,
    }


def esc(value: object) -> str:
    return str(value).replace("|", "\\|")


def main() -> int:
    patches = sorted(PATCH_DIR.glob("*.patch"))
    results = [detect(path) for path in patches]
    total_hard = sum(r["hard_findings"] for r in results)
    total_notes = sum(r["review_notes"] for r in results)

    lines = [
        "# Codex Historical Patch Audit Report v0",
        "",
        "## 1. Verdict",
        "",
        "[CODEX_HISTORICAL_PATCH_AUDIT_RETURNED_WITH_WATCH]",
        "",
        "## 2. Scope",
        "",
        f"- patch_count: {len(patches)}",
        f"- total_hard_findings: {total_hard}",
        f"- total_review_notes: {total_notes}",
        "- input_scope: patches/*.patch under hermes_historical_audit only",
        "- no source files modified",
        "",
        "## 3. Results",
        "",
        "| Patch | Target path | Context | Hard findings | Review notes |",
        "|---|---|---|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| {esc(result['patch'])} | `{esc(result['target_path'])}` | {esc(result['context'])} | {result['hard_findings']} | {result['review_notes']} |"
        )
    lines.extend(["", "## 4. Findings", ""])
    for result in results:
        lines.append(f"### {result['patch']}")
        if not result["findings"]:
            lines.append("- no findings")
            lines.append("")
            continue
        lines.extend(["", "| Rule | Severity | Line | Evidence | Note |", "|---|---|---:|---|---|"])
        for item in result["findings"]:
            lines.append(
                f"| {esc(item['rule'])} | {esc(item['severity'])} | {item['line']} | `{esc(item['evidence'])}` | {esc(item['note'])} |"
            )
        lines.append("")
    lines.extend([
        "## 5. Interpretation",
        "",
        "- This run actually read the extracted historical patch files.",
        "- Zero hard findings means these sampled historical patches did not match current hard rules.",
        "- It does not prove the repository has no risks.",
        "- It does not prove component readiness.",
        "- Most sampled patches appear documentation/work-output oriented, so this is a weak real-history sample for code-risk auditing.",
        "",
        "## 6. Recovery Suggestion",
        "",
        "receipt:",
        "  historical patch audit ran over extracted patch files",
        "",
        "residue:",
        "  current historical sample is documentation-heavy and weak for code-risk validation",
        "",
        "candidate:",
        "  audit rules remain candidate; input discovery and fixture selection need stronger control",
        "",
        "component:",
        "  HOLD",
        "",
        "## 7. HOLD",
        "",
        "- no source files modified",
        "- no patches applied",
        "- no git add / git commit",
        "- no Hermes memory/skill/config edit",
        "- no cron",
        "- no VectorFL authority update",
        "- no current-position/output_manifest update",
    ])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    receipt = {
        "verdict": "[CODEX_HISTORICAL_PATCH_AUDIT_RECEIPT]",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_files": [str(p) for p in patches],
        "output_files": [str(REPORT), str(RECEIPT)],
        "patch_count": len(patches),
        "total_hard_findings": total_hard,
        "total_review_notes": total_notes,
        "source_files_modified": False,
        "patches_applied": False,
        "git_mutation_used": False,
        "network_used": False,
        "results": results,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
