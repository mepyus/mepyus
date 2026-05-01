#!/usr/bin/env python3
"""Create a Phase 1 exploration result draft from a question packet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from excerpt_helpers import extract_excerpt
from structured_helpers import extract_structured_evidence, summarize_structured_units
from diff_helpers import diff_json_pair, summarize_diff_units
from pairing_helpers import pair_json_assets_with_metadata, summarize_pairing_units
from identity_helpers import build_identity_anchor, read_identity_anchor, summarize_identity_anchors


def authority_for_path(path: str) -> str:
    if path == "CURRENT.md" or path.startswith("source_assets/baselines/"):
        return "locked_baseline"
    if path == "vectorfl_status.md":
        return "current_working_baseline"
    if path.startswith("docs/policies/") or path.startswith("docs/contracts/") or path.startswith("docs/specs/"):
        return "policy_or_contract"
    if path.startswith("docs/guides/") or path.startswith("docs/indexes/"):
        return "guide_or_index"
    if path.startswith("docs/reports/") or path.startswith("docs/notes/"):
        return "report_or_observation"
    if path.startswith("runtime/"):
        return "runtime_artifact"
    return "weak_candidate"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question_packet", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.question_packet.read_text(encoding="utf-8"))
    targets = packet.get("search_targets", [])
    searched_paths = [target.get("path", "") for target in targets if target.get("path")]
    selected_assets = [
        {
            "path": path,
            "authority_level": authority_for_path(path),
            "reason": target.get("reason", "Selected from question packet search_targets."),
        }
        for target in targets
        for path in [target.get("path", "")]
        if path
    ]
    evidence_units = []
    structured_evidence_units = []
    for asset in selected_assets:
        excerpt = extract_excerpt(asset["path"], asset["reason"])
        relation_type = (
            "direct_support"
            if asset["authority_level"] in {"locked_baseline", "current_working_baseline", "policy_or_contract"}
            else "contextual_support"
        )
        evidence_units.append(
            {
            "source_ref": asset["path"],
            "excerpt_or_pointer": excerpt["excerpt_window"] or asset["path"],
            "pointer": excerpt["pointer"],
            "excerpt_window": excerpt["excerpt_window"],
            "excerpt_mode": excerpt["excerpt_mode"],
            "why_it_matters": asset["reason"],
            "relation_type": relation_type,
            "confidence": excerpt["local_confidence"],
            "local_confidence": excerpt["local_confidence"],
            "excerpt_quality": excerpt.get("excerpt_quality", "usable"),
            "excerpt_retry_count": excerpt.get("excerpt_retry_count", 0),
            "fallback_reason": excerpt.get("fallback_reason", ""),
            "tuning_note": excerpt.get("tuning_note", ""),
            "cross_support_refs": [],
            "contradiction_note": "",
            "grounding_status": excerpt["grounding_status"],
            }
        )
        structured_evidence_units.extend(
            extract_structured_evidence(asset["path"], asset["reason"], relation_type)
        )
    by_relation = {}
    for unit in evidence_units:
        key = unit["relation_type"]
        by_relation.setdefault(key, []).append(unit)
    if len(evidence_units) > 1:
        for unit in evidence_units:
            siblings = [
                other["source_ref"]
                for other in by_relation.get(unit["relation_type"], [])
                if other["source_ref"] != unit["source_ref"]
            ][:3]
            if siblings and unit["grounding_status"] == "direct_grounded" and unit.get("excerpt_quality") in {"usable", "strong"}:
                unit["cross_support_refs"] = siblings
                unit["grounding_status"] = "cross_supported"
                if unit.get("excerpt_quality") == "strong":
                    unit["confidence"] = "high"
                    unit["local_confidence"] = "high"
                else:
                    unit["confidence"] = "medium"
    depth_summary = {
        "pointer_only": sum(1 for unit in evidence_units if unit["grounding_status"] == "pointer_only"),
        "weak_grounded": sum(1 for unit in evidence_units if unit["grounding_status"] == "weak_grounded"),
        "direct_grounded": sum(1 for unit in evidence_units if unit["grounding_status"] == "direct_grounded"),
        "cross_supported": sum(1 for unit in evidence_units if unit["grounding_status"] == "cross_supported"),
        "total": len(evidence_units),
    }
    quality_summary = {
        "poor": sum(1 for unit in evidence_units if unit.get("excerpt_quality") == "poor"),
        "usable": sum(1 for unit in evidence_units if unit.get("excerpt_quality") == "usable"),
        "strong": sum(1 for unit in evidence_units if unit.get("excerpt_quality") == "strong"),
        "title_or_metadata_issues": sum(
            1
            for unit in evidence_units
            if unit.get("tuning_note") in {"title_only", "metadata_only"}
        ),
        "retried": sum(1 for unit in evidence_units if unit.get("excerpt_retry_count", 0) > 0),
        "total": len(evidence_units),
    }
    structured_summary = summarize_structured_units(structured_evidence_units)
    identity_anchors = [
        read_identity_anchor(path)
        for path in searched_paths
        if path.endswith(".json") and Path(path).exists()
    ]
    identity_summary = summarize_identity_anchors(identity_anchors)
    pairing_units = pair_json_assets_with_metadata(searched_paths)
    pairing_summary = summarize_pairing_units(pairing_units)
    diff_evidence_units = []
    for pair in pairing_units:
        pair_reason = (
            f"Compare {pair['source_ref_before']} to {pair['source_ref_after']} after pairing by "
            f"{pair['pairing_basis']} with {pair['pair_confidence']} confidence."
        )
        for diff_unit in diff_json_pair(pair["source_ref_before"], pair["source_ref_after"], pair_reason):
            diff_unit["family_key"] = pair.get("family_key", "")
            diff_unit["pair_confidence"] = pair.get("pair_confidence", "weak_pair")
            diff_unit["pairing_basis"] = pair.get("pairing_basis", "")
            diff_unit["pairing_unit_ref"] = f"{pair.get('source_ref_before')} -> {pair.get('source_ref_after')}"
            diff_unit["pairing_risk_note"] = pair.get("ambiguity_note", "")
            diff_unit["identity_confidence_before"] = pair.get("identity_confidence_before", "weak_identity")
            diff_unit["identity_confidence_after"] = pair.get("identity_confidence_after", "weak_identity")
            diff_unit["lineage_link_type"] = pair.get("lineage_link_type", "")
            diff_unit["shared_family_confirmed"] = pair.get("shared_family_confirmed", False)
            diff_evidence_units.append(diff_unit)
    diff_summary = summarize_diff_units(diff_evidence_units)
    stop_conditions = packet.get("constraints", {}).get("stop_conditions", [])
    result = {
        "contract_id": "space_exploration_result_v5",
        "contract_status": "draft_instance",
        "extends": "space_exploration_result_v4",
        "artifact_identity": build_identity_anchor(
            str(args.out) if args.out else "stdout_exploration_result",
            "exploration_result",
            generated_from_ref=str(args.question_packet),
            prior_artifact_ref=str(args.question_packet),
        ),
        "question_packet_ref": str(args.question_packet),
        "searched_paths": searched_paths,
        "selected_assets": selected_assets,
        "selected_asset_reasons": [asset["reason"] for asset in selected_assets],
        "discarded_assets": [
            {
                "path": "runtime/cli_sessions/*",
                "reason": "Too detailed for bounded usage-loop run unless a specific session is referenced.",
            },
            {
                "path": "runtime/views/* UI surface files",
                "reason": "Phase 1.5 non-goal: no UI or surface work.",
            },
        ],
        "evidence_units": evidence_units,
        "structured_evidence_units": structured_evidence_units,
        "identity_anchors": identity_anchors,
        "pairing_units": pairing_units,
        "diff_evidence_units": diff_evidence_units,
        "evidence_depth_summary": depth_summary,
        "excerpt_quality_summary": quality_summary,
        "structured_evidence_summary": structured_summary,
        "identity_anchor_summary": identity_summary,
        "pairing_summary": pairing_summary,
        "diff_evidence_summary": diff_summary,
        "supporting_links": searched_paths,
        "tension_or_conflict_assets": [
            {
                "reason": condition.get("type", "stop_condition"),
                "matched_terms": condition.get("matched_terms", []),
            }
            for condition in stop_conditions
        ],
        "missing_gaps": [
            "Some evidence may still require human reading for semantic claims."
        ]
        + (
            ["Pointer-only fallback occurred for at least one evidence unit."]
            if depth_summary["pointer_only"]
            else []
        ),
        "confidence": "high"
        if depth_summary["cross_supported"] or depth_summary["direct_grounded"]
        else ("medium" if selected_assets else "low"),
        "next_probe_candidates": [],
        "exploration_validation": {
            "is_evidence_bundle": bool(evidence_units),
            "selected_and_discarded_separated": True,
            "gaps_recorded": True,
            "grounded_fields_present": all(
                "grounding_status" in unit and "excerpt_mode" in unit for unit in evidence_units
            ),
            "pointer_fallback_preserved": True,
            "excerpt_quality_present": all("excerpt_quality" in unit for unit in evidence_units),
            "structured_fields_present": bool(structured_evidence_units) or not any(path.endswith(".json") for path in searched_paths),
            "diff_fields_present": bool(diff_evidence_units) or len([path for path in searched_paths if path.endswith(".json")]) < 2,
            "pairing_fields_present": bool(pairing_units) or len([path for path in searched_paths if path.endswith(".json")]) < 2,
            "identity_fields_present": True,
        },
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
