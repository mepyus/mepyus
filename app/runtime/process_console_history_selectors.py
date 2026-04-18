from __future__ import annotations

from typing import Any, Dict, List, Optional


CANONICAL_FIELDS = [
    "packet_texture",
    "grounding_status",
    "emergence_status",
    "carryover_risk",
    "maturation_state",
    "traceability_status",
    "comparison_memory_reason",
    "gate_blocker_summary",
]


def _same_value(field: str, current: Any, previous: Any) -> bool:
    if field in {"comparison_memory_reason", "gate_blocker_summary"}:
        return set(current or []) == set(previous or [])
    return current == previous


def _derive_changed_fields(previous: Optional[Dict[str, Any]], current: Dict[str, Any]) -> List[str]:
    if previous is None:
        return list(CANONICAL_FIELDS)
    changed: List[str] = []
    for field in CANONICAL_FIELDS:
        if not _same_value(field, current.get(field), previous.get(field)):
            changed.append(field)
    return changed


def _derive_change_labels(changed_fields: List[str]) -> List[str]:
    if not changed_fields:
        return ["provenance_only"]
    labels = ["canonical_change"]
    if "traceability_status" in changed_fields:
        labels.append("traceability_change")
    if "grounding_status" in changed_fields:
        labels.append("grounding_change")
    if "emergence_status" in changed_fields:
        labels.append("emergence_change")
    if "gate_blocker_summary" in changed_fields:
        labels.append("blocker_change")
    return labels


def _trigger_badge(value: Optional[str]) -> str:
    if value == "backfill":
        return "backfill"
    if value == "runtime_evidence":
        return "runtime"
    if value == "recompute":
        return "recompute"
    if value == "manual_correction":
        return "manual"
    return "unknown"


def build_history_timeline(
    history_rows: List[Dict[str, Any]],
    *,
    recent_limit: int = 10,
) -> Dict[str, Any]:
    if not history_rows:
        return {
            "state": "history_unavailable",
            "items": [],
            "total_count": 0,
            "overflow_count": 0,
            "latest_lineage_link": None,
            "history_summary": {
                "recent_update_count": 0,
                "latest_update_trigger_type": None,
                "latest_update_reason": None,
                "last_updated_at": None,
                "latest_change_kind": None,
            },
        }

    ascending = list(history_rows)
    timeline: List[Dict[str, Any]] = []
    previous: Optional[Dict[str, Any]] = None
    for row in ascending:
        changed_fields = _derive_changed_fields(previous, row)
        change_labels = _derive_change_labels(changed_fields)
        timeline.append(
            {
                "updated_at": row.get("updated_at"),
                "update_trigger_type": row.get("update_trigger_type"),
                "trigger_badge": _trigger_badge(row.get("update_trigger_type")),
                "update_reason": row.get("update_reason"),
                "changed_fields": changed_fields,
                "change_labels": change_labels,
                "provenance_only_update": not changed_fields,
                "evidence_refs": row.get("evidence_refs", []),
                "state_notes": row.get("state_notes"),
                "schema_version": row.get("schema_version"),
                "canonical_snapshot": {
                    field: row.get(field)
                    for field in CANONICAL_FIELDS
                },
                "experimental_namespace_present": bool(row.get("experimental_namespace")),
            }
        )
        previous = row

    descending = list(reversed(timeline))
    recent_items = descending[:recent_limit]
    latest = recent_items[0]
    return {
        "state": "loaded",
        "all_items": descending,
        "items": recent_items,
        "total_count": len(descending),
        "overflow_count": max(0, len(descending) - len(recent_items)),
        "latest_lineage_link": {
            "summary": f"current latest formed from recent {min(len(descending), recent_limit)} updates",
            "latest_update_trigger_type": latest["update_trigger_type"],
            "latest_update_reason": latest["update_reason"],
            "latest_updated_at": latest["updated_at"],
            "previous_state_available": len(descending) > 1,
        },
        "history_summary": {
            "recent_update_count": len(descending),
            "latest_update_trigger_type": latest["update_trigger_type"],
            "latest_update_reason": latest["update_reason"],
            "last_updated_at": latest["updated_at"],
            "latest_change_kind": latest["change_labels"][0] if latest["change_labels"] else None,
            "provenance_only_update": latest["provenance_only_update"],
        },
    }
