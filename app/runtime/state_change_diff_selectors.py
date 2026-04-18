from __future__ import annotations

from typing import Any, Dict, List, Optional

from app.runtime.process_console_history_selectors import CANONICAL_FIELDS


SCALAR_FIELDS = [
    "packet_texture",
    "grounding_status",
    "emergence_status",
    "carryover_risk",
    "maturation_state",
    "traceability_status",
]
ARRAY_FIELDS = [
    "comparison_memory_reason",
    "gate_blocker_summary",
]


def _derive_diff_class(changed_fields: List[str]) -> str:
    if not changed_fields:
        return "provenance_only"
    non_blocker = [field for field in changed_fields if field != "gate_blocker_summary"]
    if len(changed_fields) > 1 and len(non_blocker) > 1:
        return "mixed_change"
    priority = [
        "packet_texture",
        "grounding_status",
        "emergence_status",
        "carryover_risk",
        "maturation_state",
        "traceability_status",
        "gate_blocker_summary",
        "comparison_memory_reason",
    ]
    first = next((field for field in priority if field in changed_fields), changed_fields[0])
    mapping = {
        "packet_texture": "packet_texture_change",
        "grounding_status": "grounding_change",
        "emergence_status": "emergence_change",
        "carryover_risk": "carryover_change",
        "maturation_state": "maturation_change",
        "traceability_status": "traceability_change",
        "gate_blocker_summary": "blocker_change",
        "comparison_memory_reason": "comparison_memory_change",
    }
    return mapping[first]


def build_state_change_diff(
    current: Optional[Dict[str, Any]],
    previous: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    if current is None:
        return {
            "state": "state_unavailable",
            "diff_class": None,
            "changed_fields": [],
            "field_rows": [],
        }
    if previous is None:
        return {
            "state": "no_previous_state",
            "diff_class": None,
            "changed_fields": [],
            "field_rows": [],
            "current_updated_at": current.get("updated_at"),
            "current_trigger": current.get("update_trigger_type"),
            "current_reason": current.get("update_reason"),
        }

    changed_fields: List[str] = []
    field_rows: List[Dict[str, Any]] = []
    added_items_by_field: Dict[str, List[str]] = {}
    removed_items_by_field: Dict[str, List[str]] = {}
    unchanged_fields_count = 0

    for field in SCALAR_FIELDS:
        old_value = previous.get(field)
        new_value = current.get(field)
        changed = old_value != new_value
        if changed:
            changed_fields.append(field)
        else:
            unchanged_fields_count += 1
        field_rows.append(
            {
                "field_name": field,
                "old_value": old_value,
                "new_value": new_value,
                "changed": changed,
                "display_note": "state movement" if changed else "unchanged",
            }
        )

    for field in ARRAY_FIELDS:
        old_set = set(previous.get(field, []) or [])
        new_set = set(current.get(field, []) or [])
        added = sorted(new_set - old_set)
        removed = sorted(old_set - new_set)
        changed = bool(added or removed)
        if changed:
            changed_fields.append(field)
            added_items_by_field[field] = added
            removed_items_by_field[field] = removed
        else:
            unchanged_fields_count += 1
        field_rows.append(
            {
                "field_name": field,
                "old_value": sorted(old_set),
                "new_value": sorted(new_set),
                "changed": changed,
                "display_note": "set-like diff" if changed else "unchanged",
                "added_items": added,
                "removed_items": removed,
            }
        )

    diff_class = _derive_diff_class(changed_fields)
    return {
        "state": "loaded",
        "diff_class": diff_class,
        "provenance_only": not changed_fields,
        "changed_fields": changed_fields,
        "field_rows": field_rows,
        "added_items_by_field": added_items_by_field,
        "removed_items_by_field": removed_items_by_field,
        "unchanged_fields_count": unchanged_fields_count,
        "current_updated_at": current.get("updated_at"),
        "current_trigger": current.get("update_trigger_type"),
        "current_reason": current.get("update_reason"),
        "previous_updated_at": previous.get("updated_at"),
        "previous_trigger": previous.get("update_trigger_type"),
        "evidence_refs": current.get("evidence_refs", []),
    }
