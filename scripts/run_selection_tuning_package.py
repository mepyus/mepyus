#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_lower_support_reread_trial import run_trial


OUTPUT_ROOT = REPO_ROOT / "runtime" / "reread_trials" / "phase1_19_selection_tuning"


FAMILY_RUNS: list[dict[str, str]] = [
    {
        "family": "route_selection",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_route_selection_policy_v0_camera_guard_20260422_183238.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_route_selection_policy_v0_camera_guard_20260422_183238.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_route_selection_policy_v0_camera_guard_20260422_183238.json",
    },
    {
        "family": "raw_intake_gap",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_raw_intake_gap_analysis_before_middle_layer_fix_v1_camera_guard_20260422_183238.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_raw_intake_gap_analysis_before_middle_layer_fix_v1_camera_guard_20260422_183238.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_raw_intake_gap_analysis_before_middle_layer_fix_v1_camera_guard_20260422_183238.json",
    },
    {
        "family": "preprocess_builder",
        "role": "app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison_content_role_tags.json",
        "seed": "app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison_line_seed_bundles.json",
        "camera": "app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison_camera_support_bundles.json",
    },
    {
        "family": "preprocess_jung",
        "role": "app/work/external_input_preprocess/generated/codex_ambassader_jung_transcript_preprocess_comparison_content_role_tags.json",
        "seed": "app/work/external_input_preprocess/generated/codex_ambassader_jung_transcript_preprocess_comparison_line_seed_bundles.json",
        "camera": "app/work/external_input_preprocess/generated/codex_ambassader_jung_transcript_preprocess_comparison_camera_support_bundles.json",
    },
    {
        "family": "compact_title_only",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_middle_layer_thickening_program_instruction_v1_camera_guard_20260422_183238.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_middle_layer_thickening_program_instruction_v1_camera_guard_20260422_183238.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_middle_layer_thickening_program_instruction_v1_camera_guard_20260422_183238.json",
    },
    {
        "family": "input_layer_wrapper",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_input_layer_wrapper_core_link_note_v1_flow_guard_20260422_185702.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_input_layer_wrapper_core_link_note_v1_flow_guard_20260422_185702.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_input_layer_wrapper_core_link_note_v1_flow_guard_20260422_185702.json",
    },
    {
        "family": "general_line_vs_flow",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_general_line_vs_flow_candidate_v0_flow_guard_20260422_185702.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_general_line_vs_flow_candidate_v0_flow_guard_20260422_185702.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_general_line_vs_flow_candidate_v0_flow_guard_20260422_185702.json",
    },
    {
        "family": "operating_cell",
        "role": "app/work/observer_ingest_min/generated/content_role_tags_vectorfl_paper_operating_cell_schema_v0_flow_guard_20260422_185725.json",
        "seed": "app/work/observer_ingest_min/generated/line_seed_bundles_vectorfl_paper_operating_cell_schema_v0_flow_guard_20260422_185725.json",
        "camera": "app/work/observer_ingest_min/generated/camera_support_bundles_vectorfl_paper_operating_cell_schema_v0_flow_guard_20260422_185725.json",
    },
]


def _classify_family(default_payload: dict[str, Any], flow_payload: dict[str, Any], family: str) -> str:
    default_flow = default_payload["flow_judgment"]["result"]
    flow_pref_flow = flow_payload["flow_judgment"]["result"]
    if flow_pref_flow == "independent value" and default_flow != "independent value":
        return "selection-dependent independent"
    if flow_pref_flow == "independent value" and default_flow == "independent value":
        return "family-local only"
    if family.startswith("preprocess_") or family == "compact_title_only":
        return "default-stable"
    if default_payload["comparison_note_ab"]["camera_added_value"] == flow_payload["comparison_note_ab"]["camera_added_value"]:
        return "default-stable"
    return "not worth tuning"


def _gating_result(default_payload: dict[str, Any], flow_payload: dict[str, Any], family: str, carry: str) -> dict[str, Any]:
    default_flow = default_payload["flow_judgment"]
    flow_pref_flow = flow_payload["flow_judgment"]
    default_focus = default_payload["variant_c_role_seed_flow"]["reread_focus"]
    flow_focus = flow_payload["variant_c_role_seed_flow"]["reread_focus"]
    flow_strength = flow_pref_flow.get("flow_strength", "insufficient")
    focus_narrowed = default_focus != flow_focus
    meaningful_thin = (
        flow_strength == "thin"
        and flow_pref_flow.get("result") == "independent value"
        and carry in {"reroute_helpful", "stable_handle_helpful"}
    )
    has_strong_flow = flow_strength == "has_signal"
    carry_ok = carry in {"reroute_helpful", "stable_handle_helpful"}
    change_boundary_default = default_payload["comparison_note_ab"]["camera_added_value"]
    flow_beats_default = "flow" in flow_payload["comparison_note_ab"]["camera_added_value"] and (
        "flow" not in change_boundary_default or focus_narrowed
    )

    allowed = (
        flow_pref_flow.get("result") == "independent value"
        and carry_ok
        and focus_narrowed
        and (has_strong_flow or meaningful_thin)
        and flow_beats_default
        and family not in {"compact_title_only", "preprocess_builder", "preprocess_jung", "raw_intake_gap"}
    )

    if allowed:
        return {
            "mode": "flow-aware",
            "reason": "Flow-aware gating passed: independent flow survived, carry-forward helped, and reread focus narrowed.",
            "selected": flow_payload,
            "candidate_class": "allow-list candidate",
        }

    if family in {"compact_title_only", "preprocess_builder", "preprocess_jung", "raw_intake_gap"}:
        return {
            "mode": "default",
            "reason": "Flow-aware gating blocked: family is default-stable and flow-aware adds little or increases bias risk.",
            "selected": default_payload,
            "candidate_class": "block-list candidate" if family in {"compact_title_only", "preprocess_builder", "preprocess_jung"} else "default-sufficient",
        }

    if default_flow.get("result") == "independent value":
        return {
            "mode": "default",
            "reason": "Flow exists already, but tuning is not needed because default selection is sufficient.",
            "selected": default_payload,
            "candidate_class": "default-sufficient",
        }

    return {
        "mode": "default",
        "reason": "Flow-aware gating blocked: local flow evidence is not strong enough to justify switching selection mode.",
        "selected": default_payload,
        "candidate_class": "conditional-only",
    }


def _freeze_class(default_payload: dict[str, Any], flow_payload: dict[str, Any], gating: dict[str, Any], family: str) -> str:
    if gating["candidate_class"] == "allow-list candidate":
        return "allow-list candidate"
    if family in {"compact_title_only", "preprocess_builder", "preprocess_jung"}:
        return "block-list candidate"
    if gating["candidate_class"] == "default-sufficient":
        return "default-sufficient"
    return "conditional-only"


def _carry_forward_observation(default_payload: dict[str, Any], flow_payload: dict[str, Any]) -> str:
    default_refs = default_payload["variant_c_role_seed_flow"].get("carry_forward_refs", [])
    flow_refs = flow_payload["variant_c_role_seed_flow"].get("carry_forward_refs", [])
    flow_result = flow_payload["flow_judgment"]["result"]
    if flow_result == "independent value" and default_refs != flow_refs:
        return "reroute_helpful"
    if flow_result == "independent value" and default_refs == flow_refs:
        return "stable_handle_helpful"
    return "mostly_formal"


def _run_family(row: dict[str, str]) -> dict[str, Any]:
    family = row["family"]
    default_output = OUTPUT_ROOT / f"{family}_default.json"
    flow_output = OUTPUT_ROOT / f"{family}_flow_pref.json"
    default_payload = run_trial(
        label=f"{family}_default",
        role_path=(REPO_ROOT / row["role"]).resolve(),
        seed_path=(REPO_ROOT / row["seed"]).resolve(),
        camera_path=(REPO_ROOT / row["camera"]).resolve(),
        output_path=default_output,
    )
    flow_payload = run_trial(
        label=f"{family}_flow_pref",
        role_path=(REPO_ROOT / row["role"]).resolve(),
        seed_path=(REPO_ROOT / row["seed"]).resolve(),
        camera_path=(REPO_ROOT / row["camera"]).resolve(),
        output_path=flow_output,
        prefer_flow=True,
    )
    verdict = _classify_family(default_payload, flow_payload, family)
    carry = _carry_forward_observation(default_payload, flow_payload)
    gating = _gating_result(default_payload, flow_payload, family, carry)
    provisional = _freeze_class(default_payload, flow_payload, gating, family)
    combined = {
        "family": family,
        "default_output_path": str(default_output.relative_to(REPO_ROOT)).replace("\\", "/"),
        "flow_preferred_output_path": str(flow_output.relative_to(REPO_ROOT)).replace("\\", "/"),
        "default": default_payload,
        "flow_preferred": flow_payload,
        "family_verdict": verdict,
        "carry_forward_observation": carry,
        "gated_flow_aware": {
            "mode": gating["mode"],
            "reason": gating["reason"],
            "candidate_class": provisional,
            "selected_focus": gating["selected"]["variant_c_role_seed_flow"]["reread_focus"],
            "selected_flow_judgment": gating["selected"]["flow_judgment"],
        },
    }
    combined_path = OUTPUT_ROOT / f"{family}_selection_compare.json"
    combined_path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "family": family,
        "verdict": verdict,
        "carry_forward_observation": carry,
        "gated_mode": gating["mode"],
        "candidate_class": provisional,
        "combined_output_path": str(combined_path.relative_to(REPO_ROOT)).replace("\\", "/"),
    }


def main() -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    rows = [_run_family(row) for row in FAMILY_RUNS]
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
