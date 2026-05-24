#!/usr/bin/env python3
"""One-shot bounded Hermes external runner pilot.

Reads only the explicit VectorFL input files named by the pilot prompt and writes
one markdown report inside the declared sandbox output directory.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
OUTPUT_DIR = Path(__file__).resolve().parent
REPORT_PATH = OUTPUT_DIR / "vessel_runner_pilot_report.md"

INPUTS = [
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md",
        "current vessel working standard candidate",
    ),
    (
        "app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md",
        "prior Hermes space recognition and asset-use test return",
    ),
    (
        "app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md",
        "Hermes carrier sizing and boundary closeout",
    ),
]

VESSEL_TERMS = ["IIC", "SOF", "MOL", "RML"]
BOUNDARY_TERMS = [
    "SOF current authority wins",
    "RML evidence",
    "MOL read-only",
    "STOP",
    "no automation",
    "no baseline promotion",
    "no Hermes memory edit",
    "no Hermes skill creation",
    "1-5 explicit",
    "bounded carrier",
]


def read_inputs():
    records = []
    corpus_parts = []
    for rel_path, role in INPUTS:
        path = ROOT / rel_path
        exists = path.exists()
        text = ""
        size = 0
        if exists:
            data = path.read_bytes()
            size = len(data)
            text = data.decode("utf-8", errors="replace")
            corpus_parts.append((rel_path, text))
        records.append(
            {
                "rel_path": rel_path,
                "role": role,
                "exists": exists,
                "bytes": size,
                "text": text,
            }
        )
    return records, corpus_parts


def find_term(term, corpus_parts):
    term_l = term.lower()
    sources = []
    for rel_path, text in corpus_parts:
        if term_l in text.lower():
            sources.append(rel_path)
    return sources


def bool_text(value):
    return "yes" if value else "no"


def table_cell_sources(sources):
    if not sources:
        return "-"
    return "<br>".join(sources)


def build_report(records, corpus_parts):
    vessel_hits = [(term, find_term(term, corpus_parts)) for term in VESSEL_TERMS]
    boundary_hits = [(term, find_term(term, corpus_parts)) for term in BOUNDARY_TERMS]
    missing = [term for term, sources in vessel_hits + boundary_hits if not sources]

    lines = []
    lines.append("# Hermes External Runner Pilot Report v0")
    lines.append("")
    lines.append("## 1. Verdict")
    lines.append("")
    lines.append("[HERMES_EXTERNAL_RUNNER_PILOT_REPORT_WITH_WATCH]")
    lines.append("")
    lines.append("## 2. Inputs")
    lines.append("")
    lines.append("| File | Exists | Bytes | Role |")
    lines.append("|---|---:|---:|---|")
    for record in records:
        lines.append(
            f"| {record['rel_path']} | {bool_text(record['exists'])} | {record['bytes']} | {record['role']} |"
        )
    lines.append("")
    lines.append("## 3. Detected Vessel Terms")
    lines.append("")
    lines.append("| Term | Found | Evidence source |")
    lines.append("|---|---:|---|")
    for term, sources in vessel_hits:
        lines.append(f"| {term} | {bool_text(bool(sources))} | {table_cell_sources(sources)} |")
    lines.append("")
    lines.append("## 4. Detected Boundary Terms")
    lines.append("")
    lines.append("| Term | Found | Evidence source |")
    lines.append("|---|---:|---|")
    for term, sources in boundary_hits:
        lines.append(f"| {term} | {bool_text(bool(sources))} | {table_cell_sources(sources)} |")
    lines.append("")
    lines.append("## 5. Missing / Weak Terms")
    lines.append("")
    if missing:
        for term in missing:
            lines.append(f"- {term}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 6. External Runner Fit")
    lines.append("")
    lines.append("What Hermes can implement safely:")
    lines.append("- Tiny one-shot scripts inside a declared sandbox output directory.")
    lines.append("- Plain string checks over explicitly listed non-sensitive files.")
    lines.append("- A small structured report and execution receipt for Codex/User recovery.")
    lines.append("- Read-only evidence extraction that preserves SOF-over-RML and MOL-read-only boundaries.")
    lines.append("")
    lines.append("What Hermes must not implement:")
    lines.append("- Promotion, baseline, workflow, registry, schema, ontology, or VectorFL authority changes.")
    lines.append("- Broad repo search, sibling inspection, secret/session/log reading, or network/package installation.")
    lines.append("- Recurring automation, cron jobs, Hermes memory/config edits, or Hermes skill creation.")
    lines.append("- Any script that modifies input files or treats RML evidence as authority.")
    lines.append("")
    lines.append("Recommended next runner task:")
    lines.append("- Keep the next task one-shot, sandbox-only, and limited to 1-5 explicit files with a declared report/receipt output, then let Codex/VectorFL evaluate the result.")
    lines.append("")
    lines.append("## 7. WATCH")
    lines.append("")
    lines.append("- A local runner can accidentally become automation if reused as a recurring workflow.")
    lines.append("- String detection can confirm term presence but not full semantic compliance or authority.")
    lines.append("- Candidate evidence and report fluency must not be promoted into standard interface claims.")
    lines.append("")
    lines.append("## 8. HOLD")
    lines.append("")
    lines.append("- no AGENTS.md update")
    lines.append("- no SKILL.md creation")
    lines.append("- no Hermes skill creation")
    lines.append("- no Hermes memory edit")
    lines.append("- no Hermes config edit")
    lines.append("- no recurring automation or cron job")
    lines.append("- no baseline promotion")
    lines.append("- no workflow/schema/registry/ontology creation")
    lines.append("- no current-position or output_manifest update")
    lines.append("- no broad repo search or sibling folder inspection")
    lines.append("- no input file modification")
    lines.append("")
    return "\n".join(lines)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    records, corpus_parts = read_inputs()
    report = build_report(records, corpus_parts)
    REPORT_PATH.write_text(report, encoding="utf-8")
    missing_files = [record["rel_path"] for record in records if not record["exists"]]
    print("report_written:", REPORT_PATH)
    print("inputs_existing:", sum(1 for record in records if record["exists"]))
    print("inputs_missing:", len(missing_files))


if __name__ == "__main__":
    main()
