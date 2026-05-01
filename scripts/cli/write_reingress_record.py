#!/usr/bin/env python3
"""Create a Phase 1 reingress record draft."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from identity_helpers import build_identity_anchor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("--mode", choices=["merge", "diff", "hold"], default="merge")
    parser.add_argument("--question-packet", type=Path)
    parser.add_argument("--exploration-result", type=Path)
    parser.add_argument("--merge-diff-report", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    packet = (
        json.loads(args.question_packet.read_text(encoding="utf-8"))
        if args.question_packet and args.question_packet.exists()
        else {}
    )
    exploration = (
        json.loads(args.exploration_result.read_text(encoding="utf-8"))
        if args.exploration_result and args.exploration_result.exists()
        else {}
    )
    merge_report = (
        json.loads(args.merge_diff_report.read_text(encoding="utf-8"))
        if args.merge_diff_report and args.merge_diff_report.exists()
        else {}
    )
    chosen_mode = merge_report.get("chosen_mode", args.mode)
    evidence_units = exploration.get("evidence_units", [])
    depth_summary = merge_report.get("evidence_depth_summary") or exploration.get("evidence_depth_summary", {})
    quality_summary = merge_report.get("excerpt_quality_summary") or exploration.get("excerpt_quality_summary", {})
    structured_summary = merge_report.get("structured_evidence_summary") or exploration.get("structured_evidence_summary", {})
    structured_units = exploration.get("structured_evidence_units", [])
    diff_units = exploration.get("diff_evidence_units", [])
    diff_summary = merge_report.get("diff_salience_summary") or exploration.get("diff_evidence_summary", {})
    pairing_units = exploration.get("pairing_units", [])
    pairing_summary = exploration.get("pairing_summary", {})
    identity_summary = merge_report.get("identity_anchor_summary") or exploration.get("identity_anchor_summary", {})
    useful_excerpt_modes = sorted(
        {
            unit.get("excerpt_mode")
            for unit in evidence_units
            if unit.get("excerpt_mode") and unit.get("excerpt_mode") != "pointer_only"
        }
    )
    weak_grounding_areas = [
        unit.get("source_ref", "")
        for unit in evidence_units
        if unit.get("grounding_status") == "pointer_only"
        or unit.get("local_confidence") == "low"
        or unit.get("excerpt_quality") == "poor"
    ]
    reuse_candidate_assets = [
        unit.get("source_ref", "")
        for unit in evidence_units
        if unit.get("grounding_status") in {"direct_grounded", "cross_supported"}
    ][:5]
    unresolved_grounding_note = (
        "Pointer-only evidence remains; next run should inspect these sources manually or improve extraction."
        if weak_grounding_areas
        else "Grounded excerpts were available for selected evidence units."
    )
    record = {
        "contract_id": "space_reingress_record_v5",
        "contract_status": "draft_instance",
        "extends": "space_reingress_record_v4",
        "artifact_identity": build_identity_anchor(
            str(args.out) if args.out else "stdout_reingress_record",
            "reingress_record",
            generated_from_ref=str(args.merge_diff_report) if args.merge_diff_report else "",
            prior_artifact_ref=str(args.merge_diff_report) if args.merge_diff_report else "",
        ),
        "record_id": args.out.stem if args.out else "",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "original_user_request": args.request,
        "interpreted_goal": packet.get("interpreted_goal", ""),
        "searched_assets_summary": exploration.get("searched_paths", []),
        "space_position_summary": merge_report.get("space_position", {}).get("summary", ""),
        "codex_position_summary": merge_report.get("codex_position", {}).get("summary", ""),
        "chosen_mode": chosen_mode,
        "final_return_summary": (
            "Phase 1.5 usage-loop artifacts generated. "
            f"Chosen mode: {chosen_mode}."
        ),
        "unresolved_notes": merge_report.get("unresolved_tensions", []),
        "new_line_or_axis_candidate": "phase1_5_usage_loop_binding",
        "future_probe_note": "Use repeated real questions to decide what deserves automation or promotion later.",
        "evidence_depth_summary": depth_summary,
        "excerpt_quality_summary": quality_summary,
        "useful_excerpt_modes": useful_excerpt_modes,
        "weak_grounding_areas": weak_grounding_areas,
        "next_probe_hint": "Prefer reuse_candidate_assets first; inspect weak_grounding_areas when the claim depends on them.",
        "reuse_candidate_assets": reuse_candidate_assets,
        "unresolved_grounding_note": unresolved_grounding_note,
        "merge_risk_summary": merge_report.get("merge_risk_note", ""),
        "future_validation_hint": "Compare future runs by pointer_only ratio and strongest_support_refs.",
        "structured_evidence_summary": structured_summary,
        "useful_structured_modes": sorted({unit.get("asset_kind", "") for unit in structured_units if unit.get("asset_kind")}),
        "salient_paths_summary": merge_report.get("salient_paths", []),
        "weak_structured_areas": [
            unit.get("source_ref", "")
            for unit in structured_units
            if unit.get("structured_quality") in {"identity_only", "shape_only", "structured_fallback"}
        ][:8],
        "shape_only_warning": merge_report.get("structured_merge_risk_note", ""),
        "next_structured_probe_hint": "Prefer salient_paths_summary; inspect weak_structured_areas when structured claims depend on them.",
        "reusable_structured_assets": sorted(
            {
                unit.get("source_ref", "")
                for unit in structured_units
                if unit.get("structured_quality") == "salient_path"
            }
        )[:8],
        "generated_asset_reading_note": merge_report.get("shape_vs_meaning_note", ""),
        "diff_salience_summary": diff_summary,
        "useful_diff_modes": sorted({unit.get("change_type", "") for unit in diff_units if unit.get("diff_quality") == "salient_diff"}),
        "salient_diff_paths_summary": merge_report.get("salient_diff_paths", []),
        "weak_diff_areas": [
            f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}:{unit.get('path_ref')}"
            for unit in diff_units
            if unit.get("diff_quality") in {"trivial_diff", "comparison_fallback"}
        ][:8],
        "trivial_diff_warning": (
            "Trivial diff paths found; review before treating comparison as operationally meaningful."
            if diff_summary.get("trivial", 0)
            else ""
        ),
        "next_diff_probe_hint": "Prefer salient_diff_paths_summary and compare generated records from the same artifact family.",
        "reusable_comparison_pairs": sorted(
            {
                f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}"
                for unit in diff_units
                if unit.get("diff_quality") == "salient_diff"
            }
        )[:5],
        "generated_diff_note": merge_report.get("comparison_risk_note", ""),
        "useful_pairing_modes": pairing_summary.get("pairing_basis", []),
        "family_key_summary": pairing_summary.get("family_keys", []),
        "weak_pair_areas": [
            f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}"
            for unit in pairing_units
            if unit.get("pair_confidence") == "weak_pair"
        ][:8],
        "rejected_pair_summary": [
            {
                "pair": f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}",
                "rejected": unit.get("rejected_pair_candidates", []),
            }
            for unit in pairing_units
            if unit.get("rejected_pair_candidates")
        ][:5],
        "next_pairing_probe_hint": "Prefer same family_key and explicit phase/version lineage before reading diff salience.",
        "reusable_family_groups": pairing_summary.get("family_keys", []),
        "pairing_risk_summary": merge_report.get("pairing_risk_note", ""),
        "identity_anchor_summary": identity_summary,
        "useful_identity_modes": identity_summary.get("identity_basis", []),
        "weak_identity_areas": [
            f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}"
            for unit in pairing_units
            if unit.get("identity_confidence_before") == "weak_identity"
            or unit.get("identity_confidence_after") == "weak_identity"
        ][:8],
        "generated_from_chain_summary": [
            ref
            for ref in [
                str(args.question_packet) if args.question_packet else "",
                str(args.exploration_result) if args.exploration_result else "",
                str(args.merge_diff_report) if args.merge_diff_report else "",
            ]
            if ref
        ],
        "next_identity_probe_hint": "Prefer artifacts with embedded artifact_identity before relying on path/stem inference.",
        "reusable_identity_groups": identity_summary.get("family_keys", []),
        "identity_risk_summary": merge_report.get("identity_risk_note", ""),
        "artifact_refs": {
            "question_packet_ref": str(args.question_packet) if args.question_packet else "",
            "exploration_result_ref": str(args.exploration_result) if args.exploration_result else "",
            "merge_diff_report_ref": str(args.merge_diff_report) if args.merge_diff_report else "",
        },
        "validation": {
            "reusable_for_next_question": True,
            "reasoning_trace_present": True,
            "unresolved_preserved": True,
            "learning_fields_present": True,
            "structured_learning_fields_present": True,
            "diff_learning_fields_present": True,
            "pairing_learning_fields_present": True,
            "identity_learning_fields_present": True,
        },
    }
    text = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
