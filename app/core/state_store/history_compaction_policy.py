from __future__ import annotations

from typing import Any, Dict, List


RECENT_FULL_WINDOW = 3


def _is_turning_point(item: Dict[str, Any], *, index: int, total_count: int) -> bool:
    if index == total_count - 1:
        return True
    if item.get("trigger_badge") == "manual":
        return True
    changed = set(item.get("changed_fields", []))
    if "packet_texture" in changed:
        return True
    if "grounding_status" in changed or "traceability_status" in changed:
        return True
    if "gate_blocker_summary" in changed:
        return True
    return False


def compact_history_items(
    items_descending: List[Dict[str, Any]],
    *,
    recent_window: int = RECENT_FULL_WINDOW,
) -> Dict[str, Any]:
    if len(items_descending) <= recent_window:
        return {
            "recent_items": items_descending,
            "older_nodes": [],
            "recent_window": recent_window,
        }

    recent_items = items_descending[:recent_window]
    older = items_descending[recent_window:]
    older_nodes: List[Dict[str, Any]] = []
    buffer: List[Dict[str, Any]] = []

    def flush_buffer() -> None:
        nonlocal buffer
        if not buffer:
            return
        first = buffer[-1]
        last = buffer[0]
        trigger_types = sorted({item.get("update_trigger_type") for item in buffer if item.get("update_trigger_type")})
        canonical_change_count = sum(1 for item in buffer if not item.get("provenance_only_update"))
        provenance_only_count = sum(1 for item in buffer if item.get("provenance_only_update"))
        notable_shift_types = sorted({badge for item in buffer for badge in item.get("interpretation_badges", []) if badge not in {"provenance_only", "runtime_update", "backfill_origin"}})
        older_nodes.append(
            {
                "node_type": "summary",
                "summary_type": "compacted_history_summary",
                "covered_range_start": first.get("updated_at"),
                "covered_range_end": last.get("updated_at"),
                "covered_record_count": len(buffer),
                "trigger_types_included": trigger_types,
                "canonical_change_count": canonical_change_count,
                "provenance_only_count": provenance_only_count,
                "notable_shift_types": notable_shift_types,
                "representative_reasons": sorted({item.get("update_reason") for item in buffer if item.get("update_reason")})[:3],
                "representative_evidence_refs_count": sum(len(item.get("evidence_refs", [])) for item in buffer),
                "items": list(buffer),
            }
        )
        buffer = []

    total_count = len(items_descending)
    for local_index, item in enumerate(older, start=recent_window):
        if _is_turning_point(item, index=local_index, total_count=total_count):
            flush_buffer()
            older_nodes.append(
                {
                    "node_type": "anchor",
                    "item": item,
                }
            )
            continue
        if item.get("provenance_only_update"):
            buffer.append(item)
            continue
        flush_buffer()
        older_nodes.append(
            {
                "node_type": "anchor",
                "item": item,
            }
        )

    flush_buffer()
    return {
        "recent_items": recent_items,
        "older_nodes": older_nodes,
        "recent_window": recent_window,
    }
