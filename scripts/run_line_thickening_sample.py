#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.line_thickening import RereadObservation, record_reread_observation


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a small line thickening sample.")
    parser.add_argument("--runtime-root", default="runtime/line_thickening_demo")
    return parser.parse_args()


def _sample_observations() -> list[RereadObservation]:
    return [
        RereadObservation(
            run_id="line_thickening_sample_run_v1",
            asset_or_surface="runtime/current_phase.json",
            view_type="pre_read_eye",
            line_name="pre_read_eye",
            evidence="preflight decides mode before content read begins",
            grounding_type="direct",
            support_points=["mode-first gate precedes read"],
            weakness_points=["still needs a second surface to confirm repeatability"],
            contradiction_points=[],
            caution_points=["still needs a second surface to confirm repeatability"],
            next_probe_surface="runtime/breadcrumbs.jsonl",
            thickness_before="thin",
            thickness_after="medium",
            observed_at="2026-04-02T09:00:00Z",
            source_kind="preflight_decision",
            source_path_or_ref="runtime/current_phase.json",
            source_run_id_or_event_id="line_thickening_sample_run_v1",
            source_pointer="runtime/current_phase.json#current_phase",
            evidence_mode="summary_echo",
            validation_path_id="sample_run_v1",
            evidence_origin_kind="summary_echo",
            independence_class="self_referential_derived",
        ),
        RereadObservation(
            run_id="line_thickening_sample_run_v1",
            asset_or_surface="runtime/breadcrumbs.jsonl",
            view_type="pre_read_eye",
            line_name="pre_read_eye",
            evidence="breadcrumb records judgment movement and keeps why visible",
            grounding_type="direct",
            support_points=["decision movement is append-only", "why is preserved in trace"],
            weakness_points=["needs cross-surface reread to become operating"],
            contradiction_points=[],
            caution_points=["needs cross-surface reread to become operating"],
            next_probe_surface="runtime/manifests/phase_decision_log.jsonl",
            thickness_before="medium",
            thickness_after="thick",
            observed_at="2026-04-02T09:01:00Z",
            source_kind="raw_surface",
            source_path_or_ref="runtime/breadcrumbs.jsonl",
            source_run_id_or_event_id="line_thickening_sample_run_v1",
            source_pointer="runtime/breadcrumbs.jsonl#latest",
            evidence_mode="primary_structured",
            validation_path_id="sample_run_v1",
            evidence_origin_kind="primary_structured",
            independence_class="primary",
        ),
        RereadObservation(
            run_id="line_thickening_sample_run_v1",
            asset_or_surface="runtime/manifests/phase_decision_log.jsonl",
            view_type="pre_read_eye",
            line_name="pre_read_eye",
            evidence="phase decision log shows the read-before-read gate as append-only evidence",
            grounding_type="direct",
            support_points=["phase decisions remain append-only", "reread can reopen the gate path"],
            weakness_points=["still only a sample and not yet a production registry"],
            contradiction_points=[],
            caution_points=["still only a sample and not yet a production registry"],
            next_probe_surface="runtime/manifests/line_registry.json",
            thickness_before="thick",
            thickness_after="thick",
            observed_at="2026-04-02T09:02:00Z",
            source_kind="trace_log",
            source_path_or_ref="runtime/manifests/phase_decision_log.jsonl",
            source_run_id_or_event_id="line_thickening_sample_run_v1",
            source_pointer="runtime/manifests/phase_decision_log.jsonl#latest",
            evidence_mode="derived_trace",
            validation_path_id="sample_run_v1",
            evidence_origin_kind="derived_trace",
            independence_class="derived",
        ),
        RereadObservation(
            run_id="line_thickening_sample_run_v1",
            asset_or_surface="inputs/external_cases/enterprise.txt",
            view_type="raw_return_preservation",
            line_name="raw_return_preservation",
            evidence="raw / first-pass / report separation keeps return to source possible",
            grounding_type="direct",
            support_points=["raw anchor is retained", "report surface does not overwrite source"],
            weakness_points=["needs more than one family to stabilize"],
            contradiction_points=[],
            caution_points=["summary-only reread would erase the return path", "needs more than one family to stabilize"],
            next_probe_surface="docs/reports/pipeline_candidate_scope_summary_and_enterprise_reflection_anchor_assessment_v1.md",
            thickness_before="thin",
            thickness_after="medium",
            observed_at="2026-04-02T09:02:00Z",
            source_kind="raw_surface",
            source_path_or_ref="inputs/external_cases/enterprise.txt",
            source_run_id_or_event_id="line_thickening_sample_run_v1",
            source_pointer="inputs/external_cases/enterprise.txt#source_anchor",
            evidence_mode="primary_raw",
            validation_path_id="sample_run_v1",
            evidence_origin_kind="primary_raw",
            independence_class="primary",
        ),
        # exact duplicate to demonstrate suppression
        RereadObservation(
            run_id="line_thickening_sample_run_v1",
            asset_or_surface="inputs/external_cases/enterprise.txt",
            view_type="raw_return_preservation",
            line_name="raw_return_preservation",
            evidence="raw / first-pass / report separation keeps return to source possible",
            grounding_type="direct",
            support_points=["raw anchor is retained", "report surface does not overwrite source"],
            weakness_points=["needs more than one family to stabilize"],
            contradiction_points=[],
            caution_points=["summary-only reread would erase the return path", "needs more than one family to stabilize"],
            next_probe_surface="docs/reports/pipeline_candidate_scope_summary_and_enterprise_reflection_anchor_assessment_v1.md",
            thickness_before="thin",
            thickness_after="medium",
            observed_at="2026-04-02T09:02:00Z",
            source_kind="raw_surface",
            source_path_or_ref="inputs/external_cases/enterprise.txt",
            source_run_id_or_event_id="line_thickening_sample_run_v1",
            source_pointer="inputs/external_cases/enterprise.txt#source_anchor",
            evidence_mode="primary_raw",
            validation_path_id="sample_run_v1",
            evidence_origin_kind="primary_raw",
            independence_class="primary",
        ),
    ]


def main() -> int:
    args = _parse_args()
    runtime_root = Path(args.runtime_root)
    results = [record_reread_observation(runtime_root, obs) for obs in _sample_observations()]
    print(json.dumps({"runtime_root": str(runtime_root), "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
