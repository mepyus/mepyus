from __future__ import annotations

from typing import Any, Dict, List


def _limit_badges(badges: List[str], limit: int = 3) -> List[str]:
    ordered: List[str] = []
    seen = set()
    for badge in badges:
        if not badge or badge in seen:
            continue
        seen.add(badge)
        ordered.append(badge)
    return ordered[:limit]


def build_diff_interpretation_badges(diff: Dict[str, Any]) -> List[str]:
    state = diff.get("state")
    if state == "no_previous_state":
        return ["no_previous_state"]
    if state != "loaded":
        return []

    badges: List[str] = []
    if diff.get("provenance_only"):
        badges.append("provenance_only")
    else:
        badges.append("canonical_change")

    mapping = {
        "packet_texture": "packet_texture_shift",
        "grounding_status": "grounding_shift",
        "emergence_status": "emergence_shift",
        "carryover_risk": "carryover_shift",
        "maturation_state": "maturation_shift",
        "traceability_status": "traceability_shift",
        "gate_blocker_summary": "blocker_shift",
        "comparison_memory_reason": "comparison_memory_shift",
    }
    for field in diff.get("changed_fields", []):
        badge = mapping.get(field)
        if badge:
            badges.append(badge)

    if len(diff.get("changed_fields", [])) > 1:
        badges.insert(1, "mixed_shift")

    trigger = diff.get("current_trigger")
    trigger_badge = {
        "runtime_evidence": "runtime_update",
        "backfill": "backfill_origin",
        "recompute": "recompute",
        "manual_correction": "manual_correction",
    }.get(trigger)
    if trigger_badge:
        badges.append(trigger_badge)
    return _limit_badges(badges)


def build_history_item_badges(item: Dict[str, Any]) -> List[str]:
    badges: List[str] = []
    if item.get("provenance_only_update"):
        badges.append("provenance_only")
    else:
        badges.append("canonical_change")

    for label in item.get("change_labels", []):
        if label == "provenance_only":
            continue
        if label == "canonical_change":
            continue
        badges.append(label)

    trigger_badge = {
        "runtime": "runtime_update",
        "backfill": "backfill_origin",
        "recompute": "recompute",
        "manual": "manual_correction",
    }.get(item.get("trigger_badge"))
    if trigger_badge:
        badges.append(trigger_badge)
    return _limit_badges(badges)


def build_lineage_summary_badges(history_summary: Dict[str, Any]) -> List[str]:
    badges: List[str] = []
    if history_summary.get("provenance_only_update"):
        badges.append("provenance_only")
    elif history_summary.get("latest_change_kind"):
        badges.append(history_summary["latest_change_kind"])

    trigger_badge = {
        "runtime_evidence": "runtime_update",
        "backfill": "backfill_origin",
        "recompute": "recompute",
        "manual_correction": "manual_correction",
    }.get(history_summary.get("latest_update_trigger_type"))
    if trigger_badge:
        badges.append(trigger_badge)
    return _limit_badges(badges)
