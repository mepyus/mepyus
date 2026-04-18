from __future__ import annotations

from typing import Any, Dict, List


PRIORITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "background": 4,
}


def route_runtime_evidence_priority(
    *,
    asset_id: str,
    diff: Dict[str, Any],
) -> Dict[str, Any]:
    changed_fields = list(diff.get("changed_fields", []))
    added_blockers = list((diff.get("added_items_by_field") or {}).get("gate_blocker_summary", []))
    removed_blockers = list((diff.get("removed_items_by_field") or {}).get("gate_blocker_summary", []))
    provenance_only = bool(diff.get("provenance_only"))
    trigger = diff.get("current_trigger")
    diff_class = diff.get("diff_class")

    priority_level = "background"
    attention_reason = "background_provenance_only_runtime_update"
    queue_candidate = False
    suppress_reason = "provenance_only_flood_prevention"

    if diff.get("state") == "no_previous_state":
        priority_level = "medium"
        attention_reason = "no_previous_state_anchor"
        queue_candidate = True
        suppress_reason = None
    elif trigger == "manual_correction":
        priority_level = "critical"
        attention_reason = "manual_correction_requires_attention"
        queue_candidate = True
        suppress_reason = None
    elif "traceability_status" in changed_fields:
        priority_level = "critical"
        attention_reason = "traceability_shift"
        queue_candidate = True
        suppress_reason = None
    elif "grounding_status" in changed_fields:
        priority_level = "critical"
        attention_reason = "grounding_shift"
        queue_candidate = True
        suppress_reason = None
    elif "packet_texture" in changed_fields:
        priority_level = "critical"
        attention_reason = "packet_texture_shift"
        queue_candidate = True
        suppress_reason = None
    elif added_blockers:
        priority_level = "critical"
        attention_reason = "blocker_added"
        queue_candidate = True
        suppress_reason = None
    elif diff_class == "mixed_change":
        priority_level = "high"
        attention_reason = "mixed_shift"
        queue_candidate = True
        suppress_reason = None
    elif "emergence_status" in changed_fields:
        priority_level = "high"
        attention_reason = "emergence_shift"
        queue_candidate = True
        suppress_reason = None
    elif "carryover_risk" in changed_fields:
        priority_level = "high"
        attention_reason = "carryover_shift"
        queue_candidate = True
        suppress_reason = None
    elif "maturation_state" in changed_fields:
        priority_level = "high"
        attention_reason = "maturation_shift"
        queue_candidate = True
        suppress_reason = None
    elif removed_blockers:
        priority_level = "high"
        attention_reason = "blocker_removed"
        queue_candidate = True
        suppress_reason = None
    elif "comparison_memory_reason" in changed_fields:
        priority_level = "medium"
        attention_reason = "comparison_memory_shift"
        queue_candidate = True
        suppress_reason = None
    elif changed_fields:
        priority_level = "medium"
        attention_reason = "canonical_change"
        queue_candidate = True
        suppress_reason = None
    elif provenance_only and trigger == "runtime_evidence":
        priority_level = "background"
        attention_reason = "provenance_only_runtime_update"
        queue_candidate = False
        suppress_reason = "provenance_only_flood_prevention"
    elif provenance_only:
        priority_level = "low"
        attention_reason = "provenance_only_non_runtime_update"
        queue_candidate = False
        suppress_reason = "low_priority_provenance_only"

    return {
        "asset_id": asset_id,
        "priority_level": priority_level,
        "attention_reason": attention_reason,
        "queue_candidate": queue_candidate,
        "suppress_reason": suppress_reason,
        "provenance_only": provenance_only,
        "changed_fields": changed_fields,
        "added_blockers": added_blockers,
        "removed_blockers": removed_blockers,
        "changed_scalar_count": len([field for field in changed_fields if field not in {"comparison_memory_reason", "gate_blocker_summary"}]),
        "routed_at": diff.get("current_updated_at"),
    }
