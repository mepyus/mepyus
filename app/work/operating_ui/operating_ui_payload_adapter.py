from __future__ import annotations

from typing import Any, Dict, List, Optional


def adapt_process_console_payload_to_operating_ui_model(
    payload: Dict[str, Any],
    initial_asset_id: Optional[str] = None,
    internal_search_panel: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    payload = payload if isinstance(payload, dict) else {}

    summary = _as_dict(payload.get("summary"))
    header = _as_dict(payload.get("header"))
    state_panel = _as_dict(payload.get("state_panel"))
    latest_state_preview = _as_dict(payload.get("latest_state_preview"))
    attention_queue = _as_dict(payload.get("attention_queue"))
    history_drilldown = _as_dict(payload.get("history_drilldown"))
    compare_entry = _as_dict(payload.get("compare_entry"))
    guards = _as_dict(payload.get("guards"))

    board_items = [_adapt_asset_card(item) for item in _as_list(payload.get("asset_rail"))]
    board_items = [item for item in board_items if item.get("id")]

    selected_asset_id = _resolve_selected_asset_id(
        initial_asset_id=initial_asset_id,
        summary_selected_id=summary.get("selected_asset_id"),
        board_items=board_items,
    )
    state_unavailable = bool(summary.get("state_unavailable")) or header.get("state") == "state_unavailable"

    selected_asset = None if state_unavailable or not selected_asset_id else _adapt_selected_asset(
        selected_asset_id=selected_asset_id,
        header=header,
        state_panel=state_panel,
    )
    detail_modal = None if selected_asset is None else dict(selected_asset)

    derived_strip = _adapt_derived_strip(
        header=header,
        latest_state_preview=latest_state_preview,
        diff_summary=_as_dict(state_panel.get("diff_summary")),
        selected_attention=_as_dict_or_none(attention_queue.get("selected_asset_attention")),
        selected_memory=_as_dict_or_none(attention_queue.get("selected_asset_memory")),
        state_unavailable=state_unavailable,
    )
    activity_panel = _adapt_activity_panel(history_drilldown)
    compare_candidates = _adapt_compare_candidates(_as_list(compare_entry.get("related_assets")))

    page_title = (
        (selected_asset or {}).get("title")
        or header.get("asset_name")
        or guards.get("state_unavailable_label")
        or "no_canonical_state_yet"
    )

    feedback_disabled = state_unavailable or selected_asset is None
    feedback_composer = {
        "draft": {"text": "", "category": None},
        "disabled": feedback_disabled,
        "submitLabel": "submit feedback",
        "scopeLabel": "selected asset operating state" if not feedback_disabled else None,
    }

    return {
        "pageTitle": page_title,
        "selectedAssetId": selected_asset_id,
        "boardItems": board_items,
        "selectedAsset": selected_asset,
        "derivedStrip": derived_strip,
        "detailModal": detail_modal,
        "activityPanel": activity_panel,
        "feedbackComposer": feedback_composer,
        "compareCandidates": compare_candidates,
        "internalSearchPanel": internal_search_panel,
        "guards": {
            "stateUnavailable": state_unavailable,
            "stateUnavailableLabel": guards.get("state_unavailable_label", "no_canonical_state_yet"),
            "experimentalHiddenByDefault": guards.get("experimental_hidden_by_default", True),
        },
    }


def _adapt_asset_card(item: Dict[str, Any]) -> Dict[str, Any]:
    item = _as_dict(item)
    return {
        "id": item.get("asset_id"),
        "title": item.get("asset_name") or item.get("asset_id"),
        "sourceType": item.get("source_type"),
        "packetTextureLabel": item.get("packet_texture_label") or item.get("packet_texture"),
        "maturationLabel": item.get("maturation_state_label") or item.get("maturation_state"),
        "traceabilityLabel": item.get("traceability_status_label") or item.get("traceability_status"),
        "emergenceLabel": item.get("emergence_status_label") or item.get("emergence_status"),
        "updatedAt": item.get("updated_at"),
    }


def _adapt_selected_asset(
    *,
    selected_asset_id: str,
    header: Dict[str, Any],
    state_panel: Dict[str, Any],
) -> Dict[str, Any]:
    history_summary = _as_dict(state_panel.get("history_summary"))
    compare_reasons = [str(value) for value in _as_list(state_panel.get("compare_reasons")) if value is not None]
    gate_blockers = [str(value) for value in _as_list(state_panel.get("gate_blockers")) if value is not None]

    evidence_refs = []
    for ref in _as_list(state_panel.get("evidence_refs")):
        ref_dict = _as_dict(ref)
        kind = ref_dict.get("ref_kind") or ref_dict.get("kind")
        ref_id = ref_dict.get("ref_id") or ref_dict.get("id")
        label = f"{kind}: {ref_id}" if kind or ref_id else ""
        evidence_refs.append(
            {
                "kind": kind,
                "id": ref_id,
                "label": label,
            }
        )

    return {
        "id": selected_asset_id,
        "title": header.get("asset_name") or selected_asset_id,
        "subtitle": header.get("source_type"),
        "createdAt": None,
        "updatedAt": header.get("updated_at"),
        "canonicalStateRows": [
            {
                "key": field.get("key"),
                "label": field.get("label") or field.get("value"),
            }
            for field in _as_list(state_panel.get("canonical_fields"))
            if isinstance(field, dict)
        ],
        "stateNotes": state_panel.get("state_notes"),
        "scopeLabel": "selected asset operating state",
        "dependencyList": list(compare_reasons),
        "evidenceRefs": evidence_refs,
        "compareReasons": compare_reasons,
        "gateBlockers": gate_blockers,
        "historySummary": {
            "latestTrigger": history_summary.get("latest_update_trigger_type"),
            "latestReason": history_summary.get("latest_update_reason"),
            "recentUpdateCount": history_summary.get("recent_update_count"),
        },
    }


def _adapt_derived_strip(
    *,
    header: Dict[str, Any],
    latest_state_preview: Dict[str, Any],
    diff_summary: Dict[str, Any],
    selected_attention: Optional[Dict[str, Any]],
    selected_memory: Optional[Dict[str, Any]],
    state_unavailable: bool,
) -> Dict[str, Any]:
    badges = [
        {
            "key": badge.get("key"),
            "label": badge.get("label") or badge.get("value"),
        }
        for badge in _as_list(header.get("badges"))
        if isinstance(badge, dict)
    ]

    latest_preview = None
    if latest_state_preview.get("state") != "state_unavailable":
        latest_preview = {
            "packetTexture": latest_state_preview.get("packet_texture_label") or latest_state_preview.get("packet_texture"),
            "maturation": latest_state_preview.get("maturation_state_label") or latest_state_preview.get("maturation_state"),
            "traceability": latest_state_preview.get("traceability_status_label") or latest_state_preview.get("traceability_status"),
            "updatedAt": latest_state_preview.get("updated_at"),
        }

    diff_state = diff_summary.get("state") or ("state_unavailable" if state_unavailable else "loaded")
    diff_summary_model = {
        "state": diff_state,
        "diffClass": diff_summary.get("diff_class"),
        "changedFieldCount": int(diff_summary.get("changed_field_count") or 0),
        "provenanceOnly": bool(diff_summary.get("provenance_only")),
    }

    attention_summary = None
    if selected_attention:
        attention_summary = {
            "state": "loaded",
            "priority": selected_attention.get("priority_level"),
            "reason": selected_attention.get("attention_reason"),
            "queueStatus": selected_attention.get("queue_status"),
        }

    if selected_memory:
        memory_summary = {
            "summary": selected_memory.get("attention_pattern_summary") or "insufficient_attention_history",
            "totalEvents": selected_memory.get("total_attention_events", 0),
            "provenanceDensity": selected_memory.get("provenance_only_repeat_density"),
            "dominantShiftTypes": _as_list(selected_memory.get("dominant_shift_types")),
        }
    else:
        memory_summary = {
            "summary": "insufficient_attention_history",
            "totalEvents": 0,
            "provenanceDensity": None,
            "dominantShiftTypes": [],
        }

    return {
        "badgeItems": badges,
        "latestPreview": latest_preview,
        "diffSummary": diff_summary_model,
        "attentionSummary": attention_summary,
        "memorySummary": memory_summary,
    }


def _adapt_activity_panel(history_drilldown: Dict[str, Any]) -> Dict[str, Any]:
    items = []
    for item in _as_list(history_drilldown.get("items")):
        row = _as_dict(item)
        items.append(
            {
                "updatedAt": row.get("updated_at"),
                "triggerType": row.get("update_trigger_type"),
                "reason": row.get("update_reason"),
                "changedFields": _as_list(row.get("changed_fields")),
                "compareIndex": row.get("compare_index"),
            }
        )

    latest_lineage = _as_dict(history_drilldown.get("latest_lineage_link"))
    return {
        "items": items,
        "latestLineageSummary": latest_lineage.get("summary"),
        "latestTrigger": latest_lineage.get("latest_update_trigger_type"),
        "latestReason": latest_lineage.get("latest_update_reason"),
        "latestUpdatedAt": latest_lineage.get("latest_updated_at"),
    }


def _adapt_compare_candidates(items: List[Any]) -> List[Dict[str, Any]]:
    candidates = []
    for item in items:
        row = _as_dict(item)
        candidates.append(
            {
                "assetId": row.get("asset_id"),
                "reason": row.get("reason") or row.get("label"),
            }
        )
    return candidates


def _resolve_selected_asset_id(
    *,
    initial_asset_id: Optional[str],
    summary_selected_id: Optional[str],
    board_items: List[Dict[str, Any]],
) -> Optional[str]:
    valid_ids = {item.get("id") for item in board_items if item.get("id")}
    if initial_asset_id and initial_asset_id in valid_ids:
        return initial_asset_id
    if summary_selected_id and summary_selected_id in valid_ids:
        return summary_selected_id
    if board_items:
        return board_items[0].get("id")
    return None


def _as_dict(value: Any) -> Dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _as_dict_or_none(value: Any) -> Optional[Dict[str, Any]]:
    return value if isinstance(value, dict) else None


def _as_list(value: Any) -> List[Any]:
    return value if isinstance(value, list) else []
