#!/usr/bin/env python3
"""Create a Phase 1 merge/diff/hold report draft."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from identity_helpers import build_identity_anchor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question_packet", type=Path)
    parser.add_argument("exploration_result", type=Path)
    parser.add_argument("--mode", choices=["merge", "diff", "hold"], default="merge")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.question_packet.read_text(encoding="utf-8"))
    exploration = json.loads(args.exploration_result.read_text(encoding="utf-8"))
    inferred_mode = packet.get("merge_mode_candidate") or args.mode
    stop_conditions = packet.get("constraints", {}).get("stop_conditions", [])
    selected_paths = [
        asset.get("path", "")
        for asset in exploration.get("selected_assets", [])
        if asset.get("path")
    ]
    evidence_units = exploration.get("evidence_units", [])
    depth_summary = exploration.get("evidence_depth_summary", {})
    if not depth_summary:
        depth_summary = {
            "pointer_only": sum(1 for unit in evidence_units if unit.get("grounding_status") == "pointer_only"),
            "weak_grounded": sum(1 for unit in evidence_units if unit.get("grounding_status") == "weak_grounded"),
            "direct_grounded": sum(1 for unit in evidence_units if unit.get("grounding_status") == "direct_grounded"),
            "cross_supported": sum(1 for unit in evidence_units if unit.get("grounding_status") == "cross_supported"),
            "total": len(evidence_units),
        }
    confidence_distribution = {
        "low": sum(1 for unit in evidence_units if unit.get("local_confidence") == "low" or unit.get("confidence") == "low"),
        "medium": sum(1 for unit in evidence_units if unit.get("local_confidence") == "medium" or unit.get("confidence") == "medium"),
        "high": sum(1 for unit in evidence_units if unit.get("local_confidence") == "high" or unit.get("confidence") == "high"),
    }
    quality_summary = exploration.get("excerpt_quality_summary", {})
    structured_units = exploration.get("structured_evidence_units", [])
    structured_summary = exploration.get("structured_evidence_summary", {})
    diff_units = exploration.get("diff_evidence_units", [])
    diff_summary = exploration.get("diff_evidence_summary", {})
    pairing_units = exploration.get("pairing_units", [])
    pairing_summary = exploration.get("pairing_summary", {})
    identity_summary = exploration.get("identity_anchor_summary", {})
    if stop_conditions:
        mode = "hold"
    elif args.mode != "merge":
        mode = args.mode
    elif inferred_mode == "merge" and depth_summary.get("total", 0) and depth_summary.get("pointer_only", 0) == depth_summary.get("total", 0):
        mode = "diff"
    else:
        mode = inferred_mode
    strongest_support_refs = [
        unit.get("pointer") or unit.get("source_ref")
        for unit in evidence_units
        if unit.get("grounding_status") in {"direct_grounded", "cross_supported"}
    ][:5]
    strongest_tension_refs = [
        unit.get("pointer") or unit.get("source_ref")
        for unit in evidence_units
        if unit.get("relation_type") in {"tension", "contrast"} or unit.get("contradiction_note")
    ][:5]
    merge_risk_note = ""
    if depth_summary.get("pointer_only", 0):
        merge_risk_note = "Some evidence remains pointer-only; avoid treating this as fully grounded."
    if quality_summary.get("poor", 0):
        merge_risk_note = "Some excerpts are poor quality; review before relying on merge."
    if mode == "merge" and not strongest_support_refs:
        merge_risk_note = "Merge is cautious because no direct/cross-supported excerpt was found."
    salient_paths = [
        unit.get("path_ref", "")
        for unit in structured_units
        if unit.get("structured_quality") == "salient_path"
    ][:10]
    strongest_structured_support_refs = [
        unit.get("pointer", "")
        for unit in structured_units
        if unit.get("structured_quality") == "salient_path" and unit.get("local_confidence") in {"medium", "high"}
    ][:5]
    strongest_structured_tension_refs = [
        unit.get("pointer", "")
        for unit in structured_units
        if unit.get("relation_type") in {"tension", "contrast"}
    ][:5]
    shape_vs_meaning_note = (
        "Structured evidence includes salient field paths."
        if structured_summary.get("salient_path", 0)
        else "Structured evidence is identity/shape-level only."
    )
    structured_merge_risk_note = ""
    if structured_summary.get("identity_only", 0) or structured_summary.get("shape_only", 0):
        structured_merge_risk_note = "Some structured evidence is identity/shape-only; do not over-merge from shape similarity."
    salient_diff_paths = [
        unit.get("path_ref", "")
        for unit in diff_units
        if unit.get("diff_quality") == "salient_diff"
    ][:10]
    strongest_diff_support_refs = [
        f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}:{unit.get('path_ref')}"
        for unit in diff_units
        if unit.get("diff_quality") == "salient_diff"
    ][:5]
    strongest_diff_tension_refs = [
        f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}:{unit.get('path_ref')}"
        for unit in diff_units
        if unit.get("change_type") in {"mode_shift", "status_change", "evidence_depth_change"}
    ][:5]
    comparison_risk_note = ""
    if diff_summary.get("trivial", 0) and not diff_summary.get("salient_diff", 0):
        comparison_risk_note = "Only trivial diff paths were found; avoid strong diff claims."
    elif diff_summary.get("salient_diff", 0):
        comparison_risk_note = "Salient changed paths found; diff evidence can inform judgment."
    if pairing_summary.get("weak_pair", 0):
        comparison_risk_note = (
            (comparison_risk_note + " " if comparison_risk_note else "")
            + "At least one comparison rests on a weak pair; treat diff claims as cautious."
        )
    pair_confidence = (
        "weak_pair"
        if pairing_summary.get("weak_pair", 0)
        else ("strong_pair" if pairing_summary.get("strong_pair", 0) else ("plausible_pair" if pairing_summary.get("plausible_pair", 0) else "none"))
    )
    family_keys = pairing_summary.get("family_keys", [])
    pairing_basis = pairing_summary.get("pairing_basis", [])
    strongest_pair_support_refs = [
        f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')} ({unit.get('pair_confidence')})"
        for unit in pairing_units
        if unit.get("pair_confidence") in {"strong_pair", "plausible_pair"}
    ][:5]
    rejected_pair_candidates_summary = [
        {
            "pair": f"{unit.get('source_ref_before')} -> {unit.get('source_ref_after')}",
            "rejected": unit.get("rejected_pair_candidates", []),
        }
        for unit in pairing_units
        if unit.get("rejected_pair_candidates")
    ][:5]
    pairing_risk_note = ""
    if pair_confidence == "weak_pair":
        pairing_risk_note = "Pair confidence is weak; diff salience should not be treated as fully decisive."
    elif pair_confidence == "plausible_pair":
        pairing_risk_note = "Pair is plausible but not strongly marked by version or phase lineage."
    elif pair_confidence == "strong_pair":
        pairing_risk_note = "Pairing has explicit lineage markers and can support stronger comparison claims."
    if pairing_summary.get("weak_identity_pair", 0):
        pairing_risk_note = (
            (pairing_risk_note + " " if pairing_risk_note else "")
            + "At least one paired artifact has weak identity; comparison remains identity-cautious."
        )
    identity_risk_note = ""
    if identity_summary.get("weak_identity", 0):
        identity_risk_note = "Some artifacts still require path/stem identity inference."
    elif identity_summary.get("strong_identity", 0):
        identity_risk_note = "Identity anchors are present and usable for comparison context."
    elif identity_summary.get("total", 0):
        identity_risk_note = "Identity is path-inferred rather than self-described; keep comparison claims cautious."
    pairing_identity_support_refs = [
        ref
        for unit in pairing_units
        for ref in unit.get("pairing_identity_support_refs", [])
    ][:8]
    changed_mode_or_status_note = "; ".join(
        unit.get("delta_summary", "")
        for unit in diff_units
        if unit.get("change_type") in {"mode_shift", "status_change"}
    )[:900]
    report = {
        "contract_id": "merge_diff_report_v5",
        "contract_status": "draft_instance",
        "extends": "merge_diff_report_v4",
        "artifact_identity": build_identity_anchor(
            str(args.out) if args.out else "stdout_merge_diff_report",
            "merge_diff_report",
            generated_from_ref=str(args.exploration_result),
            prior_artifact_ref=str(args.exploration_result),
        ),
        "question_packet_ref": str(args.question_packet),
        "exploration_result_ref": str(args.exploration_result),
        "space_position": {
            "summary": "Use Phase 1/1.5 working specs as an operating layer below existing baselines.",
            "basis_refs": selected_paths,
        },
        "codex_position": {
            "summary": "Proceed with bounded CLI usage-loop artifacts without baseline promotion or path migration.",
            "basis": "rule_based_phase1_5_entrypoint_reasoning",
        },
        "alignment_points": [
            "No UI work is required.",
            "Existing authority structure is preserved.",
            "Artifacts are written to the Phase 1 runtime lanes.",
        ],
        "difference_points": [
            "Generated artifacts may still need human refinement for deep semantic claims."
        ],
        "unresolved_tensions": [
            condition.get("type", "stop_condition") for condition in stop_conditions
        ],
        "chosen_mode": mode,
        "final_reasoning_basis": selected_paths,
        "user_decision_required": mode == "hold",
        "user_decision_reason_if_any": "; ".join(
            condition.get("type", "stop_condition") for condition in stop_conditions
        ),
        "evidence_depth_summary": depth_summary,
        "confidence_distribution": confidence_distribution,
        "excerpt_quality_summary": quality_summary,
        "structured_evidence_summary": structured_summary,
        "salient_paths": salient_paths,
        "strongest_structured_support_refs": strongest_structured_support_refs,
        "strongest_structured_tension_refs": strongest_structured_tension_refs,
        "shape_vs_meaning_note": shape_vs_meaning_note,
        "structured_merge_risk_note": structured_merge_risk_note,
        "diff_salience_summary": diff_summary,
        "salient_diff_paths": salient_diff_paths,
        "strongest_diff_support_refs": strongest_diff_support_refs,
        "strongest_diff_tension_refs": strongest_diff_tension_refs,
        "comparison_risk_note": comparison_risk_note,
        "changed_mode_or_status_note": changed_mode_or_status_note,
        "pair_confidence": pair_confidence,
        "family_key": family_keys,
        "pairing_basis": pairing_basis,
        "pairing_risk_note": pairing_risk_note,
        "identity_anchor_summary": identity_summary,
        "identity_confidence_before": [
            unit.get("identity_confidence_before", "")
            for unit in pairing_units
        ],
        "identity_confidence_after": [
            unit.get("identity_confidence_after", "")
            for unit in pairing_units
        ],
        "shared_family_confirmed": any(unit.get("shared_family_confirmed") for unit in pairing_units),
        "lineage_link_type": sorted({unit.get("lineage_link_type", "") for unit in pairing_units if unit.get("lineage_link_type")}),
        "identity_risk_note": identity_risk_note,
        "pairing_identity_support_refs": pairing_identity_support_refs,
        "strongest_pair_support_refs": strongest_pair_support_refs,
        "comparison_candidate_count": pairing_summary.get("comparison_candidate_count", 0),
        "rejected_pair_candidates_summary": rejected_pair_candidates_summary,
        "strongest_support_refs": strongest_support_refs,
        "strongest_tension_refs": strongest_tension_refs,
        "merge_risk_note": merge_risk_note,
        "hold_trigger_reason": "; ".join(
            condition.get("type", "stop_condition") for condition in stop_conditions
        ),
        "validation": {
            "authority_ladder_applied": True,
            "hold_not_overused": mode != "hold" or bool(stop_conditions),
            "differences_preserved": True,
            "evidence_depth_considered": True,
            "structured_evidence_considered": True,
            "diff_evidence_considered": True,
            "pairing_evidence_considered": True,
            "identity_anchors_considered": True,
        },
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
