#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.runtime_preflight import (
    append_pipeline_observation,
    append_preflight_breadcrumb,
    append_phase_decision_log,
    build_runtime_preflight,
    write_current_phase_snapshot,
    write_preflight_snapshot,
)
from app.core.runtime.line_thickening import record_preflight_line_thickening


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the runtime preflight gate before reading begins.")
    parser.add_argument("runtime_root", nargs="?", default="runtime")
    parser.add_argument("--mode", dest="mode", default=None)
    parser.add_argument("--page", dest="page", default=None)
    parser.add_argument("--ref", dest="ref", default=None)
    parser.add_argument("--purpose", dest="purpose", default=None)
    parser.add_argument(
        "--record-observation",
        action="store_true",
        help="Append a pipeline observation registry row for the default candidate path.",
    )
    parser.add_argument(
        "--record-line-thickening",
        action="store_true",
        help="Append bounded line-thickening observations from the actual preflight reread path.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    runtime_root = Path(args.runtime_root)
    decision = build_runtime_preflight(
        runtime_root,
        requested_mode=args.mode,
        requested_artifact_ref=args.ref,
        page_key=args.page,
        purpose=args.purpose,
    )
    snapshot_path = write_preflight_snapshot(runtime_root, decision)
    crumb = append_preflight_breadcrumb(runtime_root, decision)
    phase_record = dict(decision.get("phase_transition") or {})
    if phase_record:
        phase_record["related_breadcrumb_refs"] = [crumb.get("crumb_id") or ""]
    phase_path = write_current_phase_snapshot(runtime_root, phase_record)
    phase_log = append_phase_decision_log(runtime_root, phase_record)
    observation = None
    if args.record_observation:
        boundary_note = None
        if (decision.get("selected_mode") or "") == "reflection" and str(decision.get("requested_artifact_ref") or "").startswith("inputs/external_cases/"):
            boundary_note = "different_mode_leads_to_different_entry_surface"
        observation = append_pipeline_observation(
            runtime_root,
            decision=decision,
            candidate_name="raw_to_first_pass_to_report",
            repeated_on=[
                "saltlux_ai",
                "ontology_youtube",
                "choi_ai_classroom_vlm",
                "enterprise",
            ],
            not_promoted_reason="observation only; raw -> first-pass -> report remains a candidate rather than a locked pipeline",
            boundary_note=boundary_note,
        )
    line_thickening = []
    if args.record_line_thickening:
        line_thickening = record_preflight_line_thickening(
            runtime_root,
            decision=decision,
            phase_record=phase_record,
            enabled=True,
        )
    print(
        json.dumps(
            {
                "decision": decision,
                "snapshot_path": str(snapshot_path),
                "phase_path": str(phase_path),
                "phase_log": phase_log,
                "breadcrumb": crumb,
                "pipeline_observation": observation,
                "line_thickening": line_thickening,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
