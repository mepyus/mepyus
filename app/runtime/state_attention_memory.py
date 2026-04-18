from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from app.core.runtime.file_store import JsonDirectoryStore
from app.runtime.attention_resolution_loop import apply_attention_resolution_loop
from app.runtime.process_console_history_loader import load_engine_state_history
from app.runtime.process_console_state_loader import load_engine_state_index
from app.runtime.runtime_evidence_priority_router import route_runtime_evidence_priority
from app.runtime.state_change_diff_selectors import build_state_change_diff
from app.runtime.state_change_interpretation_badge import build_diff_interpretation_badges


ATTENTION_MEMORY_EVENT_WINDOW = 20


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _load_latest_state(runtime_root: Path, asset_id: str) -> Optional[Dict[str, Any]]:
    path = runtime_root / "views" / "engine_state_latest" / f"{asset_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _queue_like_item(asset_id: str, asset_name: str, diff: Dict[str, Any], routed: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "asset_id": asset_id,
        "asset_name": asset_name,
        "latest_updated_at": diff.get("current_updated_at"),
        "priority_level": routed.get("priority_level"),
        "attention_reason": routed.get("attention_reason"),
        "diff_class": diff.get("diff_class"),
        "interpretation_badges": diff.get("interpretation_badges", []),
        "changed_fields": diff.get("changed_fields", []),
        "update_trigger_type": diff.get("current_trigger"),
        "update_reason": diff.get("current_reason"),
        "evidence_refs_count": len(diff.get("evidence_refs", [])),
        "queue_status": "new" if routed.get("queue_candidate") else "suppressed",
        "enqueued_at": routed.get("routed_at") or diff.get("current_updated_at"),
        "provenance_only": bool(diff.get("provenance_only")),
    }


def _background_summary(asset_id: str, asset_name: str, diff: Dict[str, Any], routed: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "asset_id": asset_id,
        "asset_name": asset_name,
        "latest_updated_at": diff.get("current_updated_at"),
        "priority_level": routed.get("priority_level", "background"),
        "attention_reason": routed.get("attention_reason"),
        "diff_class": "provenance_only",
        "changed_fields": [],
        "update_trigger_type": diff.get("current_trigger"),
        "update_reason": diff.get("current_reason"),
        "queue_status": "suppressed",
        "provenance_only": True,
        "summary": f"background provenance-only update on {asset_name}",
    }


def _iter_attention_events(asset_id: str, asset_name: str, history_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    events: List[Dict[str, Any]] = []
    previous_row: Optional[Dict[str, Any]] = None
    previous_asset_view: Optional[Dict[str, Any]] = None
    for row in history_rows[-ATTENTION_MEMORY_EVENT_WINDOW:]:
        diff = build_state_change_diff(row, previous_row)
        diff["interpretation_badges"] = build_diff_interpretation_badges(diff)
        routed = route_runtime_evidence_priority(asset_id=asset_id, diff=diff)
        queue_item = _queue_like_item(asset_id, asset_name, diff, routed)
        background = None
        if not routed.get("queue_candidate") and diff.get("current_trigger") == "runtime_evidence":
            background = _background_summary(asset_id, asset_name, diff, routed)

        lifecycle = apply_attention_resolution_loop(
            previous_asset_view=previous_asset_view,
            current_item=queue_item if routed.get("queue_candidate") else None,
            background_summary=background,
        )

        latest_item = lifecycle.get("latest_item")
        background_item = lifecycle.get("background_summary")
        resolved_items = list(lifecycle.get("resolved_items") or [])

        if latest_item:
            events.append(
                {
                    "kind": "active",
                    "updated_at": latest_item.get("latest_updated_at"),
                    "queue_status": latest_item.get("queue_status"),
                    "attention_reason": latest_item.get("attention_reason"),
                    "priority_level": latest_item.get("priority_level"),
                    "changed_fields": latest_item.get("changed_fields", []),
                    "interpretation_badges": latest_item.get("interpretation_badges", []),
                }
            )
        if background_item:
            events.append(
                {
                    "kind": "background",
                    "updated_at": background_item.get("latest_updated_at"),
                    "queue_status": background_item.get("queue_status"),
                    "attention_reason": background_item.get("attention_reason"),
                    "priority_level": background_item.get("priority_level"),
                    "changed_fields": background_item.get("changed_fields", []),
                    "interpretation_badges": ["provenance_only"],
                }
            )
        if resolved_items:
            latest_resolved = resolved_items[-1]
            if latest_resolved.get("resolved_at") == row.get("updated_at"):
                events.append(
                    {
                        "kind": "resolved",
                        "updated_at": latest_resolved.get("resolved_at"),
                        "queue_status": latest_resolved.get("queue_status"),
                        "attention_reason": latest_resolved.get("attention_reason"),
                        "priority_level": latest_resolved.get("priority_level"),
                        "changed_fields": latest_resolved.get("changed_fields", []),
                        "interpretation_badges": latest_resolved.get("interpretation_badges", []),
                    }
                )

        previous_asset_view = {
            "latest_item": latest_item,
            "background_summary": background_item,
            "resolved_items": resolved_items,
        }
        previous_row = row
    return events


def _pattern_summary(
    *,
    total: int,
    provenance_density: float,
    dominant_reason: Optional[str],
    dominant_shift: Optional[str],
    suppressed_count: int,
) -> str:
    if total >= 2 and provenance_density >= 0.5 and suppressed_count >= 1:
        return "mostly provenance_only background updates"
    if total < 3:
        return "insufficient_attention_history"
    if provenance_density >= 0.7:
        return "mostly provenance_only background updates"
    if dominant_shift == "grounding_shift":
        return "repeated grounding-related attention"
    if dominant_shift == "blocker_shift":
        return "repeated blocker attention pattern"
    if dominant_shift == "traceability_shift":
        return "repeated traceability-related attention"
    if dominant_shift == "packet_texture_shift":
        return "repeated packet-texture attention"
    if dominant_reason:
        return f"dominant attention reason: {dominant_reason}"
    return "mixed low-volume attention pattern"


def _build_asset_memory(runtime_root: Path, asset_id: str, asset_name: str) -> Dict[str, Any]:
    history_rows = load_engine_state_history(runtime_root, asset_id)
    events = _iter_attention_events(asset_id, asset_name, history_rows)
    if not events:
        return {
            "asset_id": asset_id,
            "memory_window_start": None,
            "memory_window_end": None,
            "total_attention_events": 0,
            "active_attention_count": 0,
            "resolved_attention_count": 0,
            "suppressed_attention_count": 0,
            "reopened_attention_count": 0,
            "recurring_attention_signatures": [],
            "dominant_attention_reasons": [],
            "dominant_shift_types": [],
            "provenance_only_cluster_count": 0,
            "provenance_only_repeat_density": 0.0,
            "blocker_attention_count": 0,
            "grounding_attention_count": 0,
            "traceability_attention_count": 0,
            "packet_texture_attention_count": 0,
            "maturation_attention_count": 0,
            "attention_pattern_summary": "insufficient_attention_history",
            "last_attention_at": None,
            "last_reopened_at": None,
            "last_resolved_at": None,
            "updated_at": _now_iso(),
        }

    reason_counter = Counter(str(event.get("attention_reason") or "") for event in events if event.get("attention_reason"))
    shift_counter = Counter(
        badge
        for event in events
        for badge in (event.get("interpretation_badges") or [])
        if badge
        not in {
            "runtime_update",
            "backfill_origin",
            "recompute",
            "manual_correction",
            "canonical_change",
        }
    )

    recurring = [reason for reason, count in reason_counter.items() if count >= 2]
    provenance_count = sum(1 for event in events if event.get("attention_reason") == "provenance_only_runtime_update")
    total = len(events)
    provenance_density = provenance_count / total if total else 0.0

    cluster_count = 0
    previous_provenance = False
    for event in events:
        current_provenance = event.get("attention_reason") == "provenance_only_runtime_update"
        if current_provenance and not previous_provenance:
            cluster_count += 1
        previous_provenance = current_provenance

    dominant_reason = reason_counter.most_common(1)[0][0] if reason_counter else None
    dominant_shift = shift_counter.most_common(1)[0][0] if shift_counter else None

    return {
        "asset_id": asset_id,
        "memory_window_start": events[0].get("updated_at"),
        "memory_window_end": events[-1].get("updated_at"),
        "total_attention_events": total,
        "active_attention_count": sum(1 for event in events if event.get("queue_status") in {"new", "seen", "deferred", "reopened"}),
        "resolved_attention_count": sum(1 for event in events if event.get("queue_status") == "resolved"),
        "suppressed_attention_count": sum(1 for event in events if event.get("queue_status") == "suppressed"),
        "reopened_attention_count": sum(1 for event in events if event.get("queue_status") == "reopened"),
        "recurring_attention_signatures": recurring[:5],
        "dominant_attention_reasons": [reason for reason, _count in reason_counter.most_common(3)],
        "dominant_shift_types": [shift for shift, _count in shift_counter.most_common(3)],
        "provenance_only_cluster_count": cluster_count,
        "provenance_only_repeat_density": round(provenance_density, 4),
        "blocker_attention_count": sum(1 for event in events if "blocker_shift" in (event.get("interpretation_badges") or [])),
        "grounding_attention_count": sum(1 for event in events if "grounding_shift" in (event.get("interpretation_badges") or [])),
        "traceability_attention_count": sum(1 for event in events if "traceability_shift" in (event.get("interpretation_badges") or [])),
        "packet_texture_attention_count": sum(1 for event in events if "packet_texture_shift" in (event.get("interpretation_badges") or [])),
        "maturation_attention_count": sum(1 for event in events if "maturation_shift" in (event.get("interpretation_badges") or [])),
        "attention_pattern_summary": _pattern_summary(
            total=total,
            provenance_density=provenance_density,
            dominant_reason=dominant_reason,
            dominant_shift=dominant_shift,
            suppressed_count=sum(1 for event in events if event.get("queue_status") == "suppressed"),
        ),
        "last_attention_at": events[-1].get("updated_at"),
        "last_reopened_at": next((event.get("updated_at") for event in reversed(events) if event.get("queue_status") == "reopened"), None),
        "last_resolved_at": next((event.get("updated_at") for event in reversed(events) if event.get("queue_status") == "resolved"), None),
        "updated_at": _now_iso(),
    }


def write_state_attention_memory_surface(runtime_root: Path) -> Dict[str, Any]:
    runtime_root = runtime_root.resolve()
    latest_index = load_engine_state_index(runtime_root)
    store = JsonDirectoryStore(runtime_root / "views" / "state_attention_memory")
    items: List[Dict[str, Any]] = []
    for item in latest_index.get("items", []):
        asset_id = str(item.get("asset_id") or "")
        if not asset_id:
            continue
        latest = _load_latest_state(runtime_root, asset_id)
        asset_name = str((latest or {}).get("asset_name") or asset_id)
        memory = _build_asset_memory(runtime_root, asset_id, asset_name)
        items.append(memory)
        store.put(asset_id, memory)
    index_payload = {
        "state": "loaded",
        "generated_at": _now_iso(),
        "items": sorted(items, key=lambda row: (str(row.get("updated_at") or ""), str(row.get("asset_id") or "")), reverse=True),
    }
    store.put("index", index_payload)
    return index_payload


def load_state_attention_memory_index(runtime_root: Path) -> Dict[str, Any]:
    path = runtime_root / "views" / "state_attention_memory" / "index.json"
    if not path.exists():
        return {"state": "memory_unavailable", "items": []}
    return json.loads(path.read_text(encoding="utf-8"))


def load_asset_attention_memory(runtime_root: Path, asset_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not asset_id:
        return None
    path = runtime_root / "views" / "state_attention_memory" / f"{asset_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
