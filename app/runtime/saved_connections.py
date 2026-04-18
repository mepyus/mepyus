from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from app.core.runtime.file_store import JsonlEventStore
from app.runtime.rule_eligibility import project_candidate_rule_binding


def create_saved_connection_from_candidate(
    runtime_root: Path,
    *,
    candidate: Dict[str, Any],
    reading_context: Dict[str, Any],
) -> Tuple[Dict[str, Any], bool]:
    normalized = _normalize_candidate(runtime_root=runtime_root, candidate=candidate, reading_context=reading_context)
    rows = load_saved_connections(runtime_root)
    dedupe_key = (
        normalized.get("source_asset") or "",
        normalized.get("source_candidate_id") or "",
        normalized.get("value_source_pointer") or "",
    )
    for row in rows:
        existing_key = (
            str(row.get("source_asset") or ""),
            str(row.get("source_candidate_id") or ""),
            str(row.get("value_source_pointer") or ""),
        )
        if existing_key == dedupe_key:
            if _should_upgrade_saved_row(existing=row, incoming=normalized):
                upgraded = dict(normalized)
                upgraded["id"] = str(row.get("id") or normalized.get("id") or "").strip()
                upgraded["created_at"] = str(row.get("created_at") or normalized.get("created_at") or "").strip()
                upgraded["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                upgraded["reread_count"] = int(row.get("reread_count") or 0)
                upgraded["expanded_from_connection_id"] = row.get("expanded_from_connection_id")
                _saved_connection_store(runtime_root).append(upgraded)
                return upgraded, True
            return row, False
    _saved_connection_store(runtime_root).append(normalized)
    return normalized, True


def load_saved_connections(runtime_root: Path) -> List[Dict[str, Any]]:
    rows = _saved_connection_store(runtime_root).read_all()
    latest_by_id: Dict[str, Dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        connection_id = str(row.get("id") or "").strip()
        if not connection_id:
            continue
        normalized_row = _normalize_saved_row(row)
        existing = latest_by_id.get(connection_id)
        if existing is None:
            latest_by_id[connection_id] = normalized_row
            continue
        existing_updated = str(existing.get("updated_at") or existing.get("created_at") or "")
        incoming_updated = str(normalized_row.get("updated_at") or normalized_row.get("created_at") or "")
        if incoming_updated >= existing_updated:
            latest_by_id[connection_id] = normalized_row
    normalized = list(latest_by_id.values())
    normalized.sort(key=lambda item: item.get("updated_at") or item.get("created_at") or "", reverse=True)
    return normalized


def _normalize_candidate(*, runtime_root: Path, candidate: Dict[str, Any], reading_context: Dict[str, Any]) -> Dict[str, Any]:
    source_asset = str(candidate.get("source_asset") or candidate.get("object") or "saved-connection").strip()
    source_candidate_id = str(candidate.get("id") or "candidate").strip()
    value_source_pointer = str(reading_context.get("value_source_pointer") or candidate.get("source_pointer") or source_candidate_id).strip()
    connection_id = "conn_" + "_".join(
        filter(
            None,
            [
                _slug(source_asset),
                _slug(source_candidate_id),
                _slug(value_source_pointer)[:32],
            ],
        )
    )
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rule_binding = project_candidate_rule_binding(
        candidate,
        reading_context=reading_context,
        runtime_root=runtime_root,
    )
    object_label = str(candidate.get("object") or source_asset).strip()
    value_label = str(candidate.get("layer") or candidate.get("title") or source_candidate_id).strip()
    relation_summary = str(candidate.get("meaning") or "").strip() or f"{object_label}에서 {value_label}를 다시 읽는 연결"
    relation_note = _relation_note(candidate, reading_context)
    sticker_text = str(candidate.get("sticker_slot") or "").strip()
    return {
        "schema": "saved_connection_v1",
        "id": connection_id,
        "status": "saved",
        "created_at": timestamp,
        "updated_at": timestamp,
        "source_asset": source_asset,
        "object_key": str(rule_binding.get("object_key") or "").strip(),
        "object_label": object_label,
        "object_paragraph_ref": str(reading_context.get("object_paragraph_ref") or "").strip(),
        "object_paragraph_text": str(reading_context.get("object_paragraph_text") or "").strip(),
        "object_source_pointer": str(reading_context.get("object_source_pointer") or reading_context.get("source_pointer") or candidate.get("source_pointer") or "").strip(),
        "value_key": str(rule_binding.get("value_key") or "").strip(),
        "value_label": value_label,
        "value_type": _value_type(str(rule_binding.get("value_key") or "")),
        "value_paragraph_ref": str(reading_context.get("value_paragraph_ref") or "").strip(),
        "value_paragraph_text": str(reading_context.get("value_paragraph_text") or candidate.get("original_preview") or "").strip(),
        "value_source_pointer": value_source_pointer,
        "scene": str(rule_binding.get("scene") or "").strip(),
        "flow": str(rule_binding.get("flow") or "").strip(),
        "primary_rule_key": str(rule_binding.get("primary_rule_key") or "").strip(),
        "support_rule_keys": list(rule_binding.get("support_rule_keys") or []),
        "rule_projection": {
            "object_status": str(rule_binding.get("object_status") or "").strip(),
            "object_label": str(rule_binding.get("object_label") or "").strip(),
            "value_status": str(rule_binding.get("value_status") or "").strip(),
            "value_label": str(rule_binding.get("value_label") or "").strip(),
            "primary_rule_key": str(rule_binding.get("primary_rule_key") or "").strip(),
            "support_only": list(rule_binding.get("support_only") or []),
            "provenance_only": list(rule_binding.get("provenance_only") or []),
            "watchlist_only": list(rule_binding.get("watchlist_only") or []),
            "binding_source": str(rule_binding.get("binding_source") or "").strip(),
            "object_fragment_id": str(rule_binding.get("object_fragment_id") or "").strip(),
            "value_fragment_id": str(rule_binding.get("value_fragment_id") or "").strip(),
        },
        "relation_summary": relation_summary,
        "relation_note": relation_note,
        "source_candidate_id": source_candidate_id,
        "sticker": {
            "attached": True,
            "label": "keep",
            "note": sticker_text or "남겨 둘 연결이면 여기서 다시 읽는다.",
        },
        "reread_count": 0,
        "expanded_from_connection_id": None,
    }


def _normalize_saved_row(row: Dict[str, Any]) -> Dict[str, Any]:
    if row.get("schema") == "saved_connection_v1":
        return {
            "schema": "saved_connection_v1",
            "id": str(row.get("id") or "").strip(),
            "status": str(row.get("status") or "saved").strip(),
            "created_at": str(row.get("created_at") or "").strip(),
            "updated_at": str(row.get("updated_at") or row.get("created_at") or "").strip(),
            "source_asset": str(row.get("source_asset") or "").strip(),
            "object_key": str(row.get("object_key") or "").strip(),
            "object_label": str(row.get("object_label") or "").strip(),
            "object_paragraph_ref": str(row.get("object_paragraph_ref") or "").strip(),
            "object_paragraph_text": str(row.get("object_paragraph_text") or "").strip(),
            "object_source_pointer": str(row.get("object_source_pointer") or "").strip(),
            "value_key": str(row.get("value_key") or "").strip(),
            "value_label": str(row.get("value_label") or "").strip(),
            "value_type": str(row.get("value_type") or "").strip(),
            "value_paragraph_ref": str(row.get("value_paragraph_ref") or "").strip(),
            "value_paragraph_text": str(row.get("value_paragraph_text") or "").strip(),
            "value_source_pointer": str(row.get("value_source_pointer") or "").strip(),
            "scene": str(row.get("scene") or "").strip(),
            "flow": str(row.get("flow") or "").strip(),
            "primary_rule_key": str(row.get("primary_rule_key") or "").strip(),
            "support_rule_keys": [str(item).strip() for item in (row.get("support_rule_keys") or []) if str(item).strip()],
            "rule_projection": {
                **dict(row.get("rule_projection") or {}),
            },
            "relation_summary": str(row.get("relation_summary") or "").strip(),
            "relation_note": str(row.get("relation_note") or "").strip(),
            "source_candidate_id": str(row.get("source_candidate_id") or "").strip(),
            "sticker": dict(row.get("sticker") or {}),
            "reread_count": int(row.get("reread_count") or 0),
            "expanded_from_connection_id": row.get("expanded_from_connection_id"),
        }
    created_at = str(row.get("created_at") or "").strip()
    title = str(row.get("title") or row.get("id") or "").strip()
    original_preview = str(row.get("original_preview") or "").strip()
    source_pointer = str(row.get("source_pointer") or "").strip()
    source_asset = str(row.get("source_asset") or "").strip()
    source_candidate_id = str(row.get("source_candidate_id") or "").strip()
    return {
        "schema": "saved_connection_v1",
        "id": str(row.get("id") or "").strip(),
        "status": "saved",
        "created_at": created_at,
        "updated_at": created_at,
        "source_asset": source_asset,
        "object_key": f"object.asset.{_slug(str(row.get('object') or source_asset or 'unknown'))}",
        "object_label": str(row.get("object") or source_asset).strip(),
        "object_paragraph_ref": "",
        "object_paragraph_text": "",
        "object_source_pointer": source_pointer,
        "value_key": "",
        "value_label": str(row.get("layer") or title).strip(),
        "value_type": "semantic",
        "value_paragraph_ref": "",
        "value_paragraph_text": original_preview,
        "value_source_pointer": source_pointer,
        "scene": "",
        "flow": "",
        "primary_rule_key": "",
        "support_rule_keys": [],
        "rule_projection": {
            "object_status": "support_only",
            "value_status": "watchlist_only",
            "primary_rule_key": "",
            "support_only": [],
            "provenance_only": [],
            "watchlist_only": [],
        },
        "relation_summary": str(row.get("meaning") or "").strip(),
        "relation_note": "",
        "source_candidate_id": source_candidate_id,
        "sticker": {
            "attached": True,
            "label": "keep",
            "note": str(row.get("sticker_slot") or "").strip(),
        },
        "reread_count": 0,
        "expanded_from_connection_id": None,
    }


def _relation_note(candidate: Dict[str, Any], reading_context: Dict[str, Any]) -> str:
    parts: List[str] = []
    reading_basis = str(candidate.get("candidate_kind") or "").strip()
    if reading_basis:
        parts.append(f"basis={reading_basis}")
    if reading_context.get("value_paragraph_ref"):
        parts.append(f"value={reading_context.get('value_paragraph_ref')}")
    if reading_context.get("object_paragraph_ref"):
        parts.append(f"object={reading_context.get('object_paragraph_ref')}")
    return " / ".join(parts)


def _should_upgrade_saved_row(*, existing: Dict[str, Any], incoming: Dict[str, Any]) -> bool:
    existing_binding = str((existing.get("rule_projection") or {}).get("binding_source") or "").strip()
    incoming_binding = str((incoming.get("rule_projection") or {}).get("binding_source") or "").strip()
    if existing_binding != "first_pass_canonical" and incoming_binding == "first_pass_canonical":
        return True
    existing_primary = str(existing.get("primary_rule_key") or "").strip()
    incoming_primary = str(incoming.get("primary_rule_key") or "").strip()
    if existing_primary.startswith("semantic.row.") and incoming_primary and not incoming_primary.startswith("semantic.row."):
        return True
    existing_object = str(existing.get("object_key") or "").strip()
    incoming_object = str(incoming.get("object_key") or "").strip()
    if existing_object.startswith("object.asset.") and incoming_object and not incoming_object.startswith("object.asset."):
        return True
    return False


def _value_type(value_key: str) -> str:
    if value_key.startswith("object."):
        return "object"
    if value_key.startswith("semantic."):
        return "semantic"
    if value_key.startswith("structural."):
        return "structural"
    if value_key.startswith("source."):
        return "source"
    if value_key.startswith("observer."):
        return "observer"
    return "semantic"


def _saved_connection_store(runtime_root: Path) -> JsonlEventStore:
    return JsonlEventStore(runtime_root / "manifests" / "user_pages" / "saved_connections.jsonl")


def _slug(value: str) -> str:
    lowered = (value or "").strip().lower()
    cleaned = []
    for char in lowered:
        if char.isalnum():
            cleaned.append(char)
        else:
            cleaned.append("_")
    collapsed = "".join(cleaned).strip("_")
    while "__" in collapsed:
        collapsed = collapsed.replace("__", "_")
    return collapsed or "item"
