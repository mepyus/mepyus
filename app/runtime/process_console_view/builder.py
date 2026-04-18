from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
from app.runtime.process_console_history_loader import (
    load_engine_state_history,
    load_engine_state_update_event,
)
from app.runtime.process_console_history_selectors import build_history_timeline
from app.runtime.process_console_history_compacted_loader import build_compacted_history_surface
from app.runtime.state_change_diff_loader import select_adjacent_history_pair
from app.runtime.state_change_diff_selectors import build_state_change_diff
from app.runtime.state_change_interpretation_badge import (
    build_diff_interpretation_badges,
    build_history_item_badges,
    build_lineage_summary_badges,
)
from app.runtime.state_change_attention_queue import (
    load_state_change_attention_queue_index,
    select_asset_attention_entry,
)
from app.runtime.state_attention_memory import load_asset_attention_memory
from app.runtime.process_console_state_loader import (
    load_engine_state_index,
    load_engine_state_items,
    load_engine_state_latest,
)
from app.runtime.process_console_state_selectors import (
    apply_state_filters,
    build_compare_candidates,
    display_label,
    sort_state_rows,
)


def build_process_console_view_data(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    filters: Optional[Dict[str, str]] = None,
    sort_by: str = "updated_at",
    compare_index: int = 0,
    debug: bool = False,
) -> Dict[str, object]:
    index = load_engine_state_index(runtime_root)
    items = load_engine_state_items(runtime_root)
    filtered = apply_state_filters(items, filters or {})
    sorted_items = sort_state_rows(filtered, sort_by)
    selected_id = asset_id or (sorted_items[0]["asset_id"] if sorted_items else None)
    selected = load_engine_state_latest(runtime_root, selected_id) if selected_id else None
    history_rows = load_engine_state_history(runtime_root, selected_id)
    history_timeline = build_history_timeline(history_rows, recent_limit=3)
    latest_update_event = load_engine_state_update_event(runtime_root, selected_id)
    diff_pair = select_adjacent_history_pair(history_rows, compare_index=compare_index)
    state_change_diff = build_state_change_diff(diff_pair["current"], diff_pair["previous"])
    state_change_diff["interpretation_badges"] = build_diff_interpretation_badges(state_change_diff)
    history_summary = dict(history_timeline["history_summary"])
    history_summary["interpretation_badges"] = build_lineage_summary_badges(history_summary)
    history_timeline["history_summary"] = history_summary
    history_items = _attach_history_badges(_attach_history_compare_links(history_timeline["items"], selected_id))
    compacted_history = build_compacted_history_surface(
        _attach_history_badges(history_timeline.get("all_items", []))
    )
    attention_queue_index = load_state_change_attention_queue_index(runtime_root)
    selected_attention = select_asset_attention_entry(attention_queue_index, selected_id)
    selected_attention_memory = load_asset_attention_memory(runtime_root, selected_id)

    return {
        "summary": {
            "asset_count": len(sorted_items),
            "selected_asset_id": selected_id,
            "state_source": "runtime/views/engine_state_latest",
            "sort_by": sort_by,
            "filters": filters or {},
            "state_unavailable": selected is None,
            "compare_index": compare_index,
        },
        "header": _build_header(selected),
        "asset_rail": [_to_asset_card(row) for row in sorted_items],
        "state_panel": _build_state_panel(selected, history_timeline, state_change_diff, selected_id),
        "compare_entry": _build_compare_entry(selected, sorted_items),
        "latest_state_preview": _build_latest_preview(selected),
        "attention_queue": {
            "state": attention_queue_index.get("state", "loaded"),
            "selected_asset_attention": selected_attention,
            "selected_asset_memory": selected_attention_memory,
            "top_items": attention_queue_index.get("items", [])[:5],
            "background_summaries": attention_queue_index.get("background_summaries", [])[:5],
            "counts": attention_queue_index.get("counts", {}),
        },
        "history_summary": history_summary,
        "history_drilldown": {
            "state": history_timeline["state"],
            "items": history_items,
            "total_count": history_timeline["total_count"],
            "overflow_count": history_timeline["overflow_count"],
            "latest_lineage_link": history_timeline["latest_lineage_link"],
            "event_summary": latest_update_event or {},
            "older_compacted": compacted_history,
        },
        "state_change_diff": _build_state_change_diff_payload(state_change_diff, selected_id, compare_index),
        "guards": {
            "experimental_hidden_by_default": True,
            "state_unavailable_label": "no_canonical_state_yet",
            "debug_experimental_visible": debug,
        },
        "debug": {
            "selected_experimental_namespace": (selected or {}).get("experimental_namespace", {}) if debug else {},
        },
    }


def _build_header(selected: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not selected:
        return {
            "state": "state_unavailable",
            "badges": [],
        }
    badges = []
    for key in [
        "packet_texture",
        "grounding_status",
        "emergence_status",
        "carryover_risk",
        "maturation_state",
        "traceability_status",
    ]:
        badges.append({"key": key, "value": selected.get(key), "label": display_label(selected.get(key))})
    return {
        "state": "loaded",
        "asset_name": selected.get("asset_name"),
        "source_type": selected.get("source_type"),
        "updated_at": selected.get("updated_at"),
        "badges": badges,
    }


def _to_asset_card(row: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "asset_id": row.get("asset_id"),
        "asset_name": row.get("asset_name"),
        "packet_texture": row.get("packet_texture"),
        "packet_texture_label": display_label(row.get("packet_texture")),
        "maturation_state": row.get("maturation_state"),
        "maturation_state_label": display_label(row.get("maturation_state")),
        "traceability_status": row.get("traceability_status"),
        "traceability_status_label": display_label(row.get("traceability_status")),
        "emergence_status": row.get("emergence_status"),
        "emergence_status_label": display_label(row.get("emergence_status")),
        "updated_at": row.get("updated_at"),
    }


def _build_state_panel(
    selected: Optional[Dict[str, Any]],
    history_timeline: Dict[str, Any],
    state_change_diff: Dict[str, Any],
    selected_id: Optional[str],
) -> Dict[str, Any]:
    if not selected:
        return {
            "state": "state_unavailable",
            "canonical_fields": [],
            "evidence_refs": [],
            "compare_reasons": [],
            "gate_blockers": [],
            "history_summary": history_timeline["history_summary"],
            "diff_summary": _build_diff_summary_strip(state_change_diff, selected_id),
        }
    canonical_fields = []
    for key in [
        "packet_texture",
        "grounding_status",
        "emergence_status",
        "carryover_risk",
        "maturation_state",
        "traceability_status",
    ]:
        canonical_fields.append({"key": key, "value": selected.get(key), "label": display_label(selected.get(key))})
    return {
        "state": "loaded",
        "canonical_fields": canonical_fields,
        "state_notes": selected.get("state_notes"),
        "evidence_refs": selected.get("evidence_refs", []),
        "compare_reasons": selected.get("comparison_memory_reason", []),
        "gate_blockers": selected.get("gate_blocker_summary", []),
        "history_summary": history_timeline["history_summary"],
        "diff_summary": _build_diff_summary_strip(state_change_diff, selected_id),
    }


def _build_compare_entry(selected: Optional[Dict[str, Any]], rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not selected:
        return {"state": "state_unavailable", "related_assets": []}
    return {"state": "loaded", "related_assets": build_compare_candidates(selected, rows)}


def _build_latest_preview(selected: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not selected:
        return {"state": "state_unavailable"}
    return {
        "state": "loaded",
        "packet_texture": selected.get("packet_texture"),
        "packet_texture_label": display_label(selected.get("packet_texture")),
        "maturation_state": selected.get("maturation_state"),
        "maturation_state_label": display_label(selected.get("maturation_state")),
        "traceability_status": selected.get("traceability_status"),
        "traceability_status_label": display_label(selected.get("traceability_status")),
        "updated_at": selected.get("updated_at"),
    }


def _attach_history_compare_links(items: List[Dict[str, Any]], selected_id: Optional[str]) -> List[Dict[str, Any]]:
    linked: List[Dict[str, Any]] = []
    for index, item in enumerate(items):
        row = dict(item)
        row["compare_index"] = index
        row["can_compare_to_previous"] = index + 1 < len(items)
        row["compare_to_previous_href"] = (
            f"/process-console?asset_id={selected_id}&compare_index={index}"
            if selected_id and index + 1 < len(items)
            else None
        )
        linked.append(row)
    return linked


def _attach_history_badges(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for item in items:
        row = dict(item)
        row["interpretation_badges"] = build_history_item_badges(row)
        rows.append(row)
    return rows


def _build_diff_summary_strip(state_change_diff: Dict[str, Any], selected_id: Optional[str]) -> Dict[str, Any]:
    if state_change_diff["state"] == "state_unavailable":
        return {"state": "state_unavailable"}
    if state_change_diff["state"] == "no_previous_state":
        return {
            "state": "no_previous_state",
            "compare_to_previous_href": None,
        }
    return {
        "state": "loaded",
        "diff_class": state_change_diff["diff_class"],
        "changed_field_count": len(state_change_diff["changed_fields"]),
        "provenance_only": state_change_diff["provenance_only"],
        "interpretation_badges": state_change_diff.get("interpretation_badges", []),
        "compare_to_previous_href": (
            f"/process-console?asset_id={selected_id}&compare_index=0"
            if selected_id
            else None
        ),
    }


def _build_state_change_diff_payload(
    state_change_diff: Dict[str, Any],
    selected_id: Optional[str],
    compare_index: int,
) -> Dict[str, Any]:
    payload = dict(state_change_diff)
    payload["compare_index"] = compare_index
    payload["selected_asset_id"] = selected_id
    payload["compare_navigation"] = {
        "current_compare_href": (
            f"/process-console?asset_id={selected_id}&compare_index={compare_index}"
            if selected_id and state_change_diff["state"] == "loaded"
            else None
        ),
        "next_compare_href": (
            f"/process-console?asset_id={selected_id}&compare_index={compare_index + 1}"
            if selected_id and state_change_diff["state"] == "loaded"
            else None
        ),
    }
    return payload
