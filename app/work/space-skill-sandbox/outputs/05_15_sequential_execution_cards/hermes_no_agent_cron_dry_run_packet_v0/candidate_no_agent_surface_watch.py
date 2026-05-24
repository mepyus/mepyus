#!/usr/bin/env python3
"""Candidate no-agent surface watch script for a future Hermes cron.

Dry-run constraints:
- Python standard library only.
- Reads only explicit input files listed below.
- Writes only no_agent_cron_dry_run_report.md in this declared output dir.
- Does not use network, subprocess, Hermes CLI, cron commands, or input mutation.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUTPUT_DIR = Path(__file__).resolve().parent
REPORT_PATH = OUTPUT_DIR / "no_agent_cron_dry_run_report.md"

INPUTS = [
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md",
        "vessel working standard candidate and SOF/IIC/MOL/RML rules",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_design_packet.md",
        "pre-cron design packet and future cron design constraints",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md",
        "pre-cron design review receipt and boundary confirmation",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md",
        "one-shot automation session report and automation boundary findings",
    ),
    (
        "app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md",
        "Hermes carrier sizing and boundary closeout",
    ),
]

TERMS = [
    "IIC",
    "SOF",
    "MOL",
    "RML",
    "STOP",
    "SOF current authority wins",
    "RML evidence",
    "MOL read-only",
    "no automation",
    "no recurring automation",
    "no cron job",
    "no Hermes memory edit",
    "no Hermes skill creation",
    "bounded carrier",
    "one-shot",
    "1-5 explicit",
    "Real cron",
    "HOLD",
]


def read_inputs():
    records = []
    corpus = []
    for rel_path, role in INPUTS:
        path = ROOT / rel_path
        exists = path.exists()
        size = 0
        text = ""
        if exists:
            raw = path.read_bytes()
            size = len(raw)
            text = raw.decode("utf-8", errors="replace")
            corpus.append((rel_path, text))
        records.append({"rel_path": rel_path, "role": role, "exists": exists, "bytes": size})
    return records, corpus


def find_sources(term, corpus):
    needle = term.lower()
    return [rel_path for rel_path, text in corpus if needle in text.lower()]


def yn(value):
    return "yes" if value else "no"


def src_cell(sources):
    return "<br>".join(sources) if sources else "-"


def build_report(records, detections):
    missing_terms = [term for term, sources in detections if not sources]
    lines = []
    lines.append("# Hermes No-Agent Cron Dry-Run Report v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_NO_AGENT_CRON_DRY_RUN_PACKET_RETURNED_WITH_WATCH]")
    lines.append("")
    lines.append("## 2. Dry-Run Type")
    lines.append("")
    lines.append("manual local dry-run")
    lines.append("no real cron")
    lines.append("no recurring automation")
    lines.append("no Hermes cron command")
    lines.append("")
    lines.append("## 3. Inputs")
    lines.append("")
    lines.append("| File | Exists | Bytes | Role |")
    lines.append("|---|---:|---:|---|")
    for record in records:
        lines.append(
            f"| {record['rel_path']} | {yn(record['exists'])} | {record['bytes']} | {record['role']} |"
        )
    lines.append("")
    lines.append("## 4. Detection Results")
    lines.append("")
    lines.append("| Term | Found | Evidence source |")
    lines.append("|---|---:|---|")
    for term, sources in detections:
        lines.append(f"| {term} | {yn(bool(sources))} | {src_cell(sources)} |")
    lines.append("")
    lines.append("## 5. Missing / Weak Terms")
    lines.append("")
    if missing_terms:
        for term in missing_terms:
            lines.append(f"- {term}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 6. No-Agent Cron Candidate Fit")
    lines.append("")
    lines.append("What this script can safely do:")
    lines.append("- Run as a deterministic, manual local dry-run over five explicit non-sensitive inputs.")
    lines.append("- Detect expected vessel and automation-boundary terms using plain text checks.")
    lines.append("- Write one declared markdown report in the sandbox output directory for Codex/User review.")
    lines.append("- Support a future no-agent cron design review without creating or registering real cron.")
    lines.append("")
    lines.append("What it must not do:")
    lines.append("- Create, update, run, remove, or inspect Hermes cron jobs or ~/.hermes/cron/jobs.json.")
    lines.append("- Use network, subprocess, Hermes CLI, external packages, broad repo search, sibling inspection, or secret/session/log reads.")
    lines.append("- Modify inputs, Hermes memory/skills/config, AGENTS.md, SKILL.md, VectorFL baseline, workflow, schema, registry, ontology, current-position, output_manifest, or authority surfaces.")
    lines.append("- Treat term detection, repeated reports, or RML evidence as authority or promotion readiness.")
    lines.append("")
    lines.append("Ready for real cron?")
    lines.append("- No. This is a dry-run packet only. Real cron remains HOLD until Codex/User approve the final no-agent script, self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.")
    lines.append("")
    lines.append("## 7. WATCH")
    lines.append("")
    lines.append("- No-agent mode lowers LLM drift but does not by itself authorize real cron or recurrence.")
    lines.append("- String checks detect surface terms, not full semantic or authority compliance.")
    lines.append("- Manual-trigger-first can still drift into recurring automation if approval boundaries are skipped.")
    lines.append("")
    lines.append("## 8. HOLD")
    lines.append("")
    lines.append("- no real Hermes cron job created")
    lines.append("- no ~/.hermes/cron/jobs.json edit")
    lines.append("- no hermes cron command run")
    lines.append("- no gateway install")
    lines.append("- no recurring automation")
    lines.append("- no Hermes skill creation")
    lines.append("- no Hermes memory edit")
    lines.append("- no Hermes config edit")
    lines.append("- no AGENTS.md update")
    lines.append("- no SKILL.md creation")
    lines.append("- no baseline promotion")
    lines.append("- no workflow/schema/registry/ontology creation")
    lines.append("- no current-position update")
    lines.append("- no output_manifest update")
    lines.append("- no local core / derived / surface authority change")
    lines.append("- no broad repo search")
    lines.append("- Real cron remains HOLD until Codex/User approve the final no-agent script, self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.")
    lines.append("")
    return "\n".join(lines)


def main():
    records, corpus = read_inputs()
    detections = [(term, find_sources(term, corpus)) for term in TERMS]
    REPORT_PATH.write_text(build_report(records, detections), encoding="utf-8")
    missing_files = [record["rel_path"] for record in records if not record["exists"]]
    print(f"report_written: {REPORT_PATH}")
    print(f"inputs_existing: {sum(1 for record in records if record['exists'])}")
    print(f"inputs_missing: {len(missing_files)}")
    if missing_files:
        print("missing_files:")
        for rel_path in missing_files:
            print(f"- {rel_path}")


if __name__ == "__main__":
    main()
