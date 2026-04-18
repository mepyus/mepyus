from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from app.core.runtime.file_store import JsonDirectoryStore
from app.runtime.attention_resolution_loop import apply_attention_resolution_loop
from app.runtime.process_console_history_loader import load_engine_state_history
from app.runtime.process_console_history_selectors import build_history_timeline
from app.runtime.process_console_state_loader import load_engine_state_index
from app.runtime.runtime_evidence_priority_router import PRIORITY_ORDER, route_runtime_evidence_priority
from app.runtime.state_change_diff_loader import select_adjacent_history_pair
from app.runtime.state_change_diff_selectors import build_state_change_diff
from app.runtime.state_change_interpretation_badge import build_diff_interpretation_badges


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _load_latest_state(runtime_root: Path, asset_id: str) -> Optional[Dict[str, Any]]:
    path = runtime_root / "views" / "engine_state_latest" / f"{asset_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _recent_provenance_only_runtime_count(history_rows: List[Dict[str, Any]]) -> int:
    timeline = build_history_timeline(history_rows, recent_limit=max(1, len(history_rows)))
    count = 0
    for item in timeline.get("all_items", []):
        if not item.get("provenance_only_update"):
            break
        if item.get("update_trigger_type") != "runtime_evidence":
            break
        count += 1
    return count


def _build_queue_item(
    *,
    asset_id: str,
    asset_name: str,
    diff: Dict[str, Any],
    routed: Dict[str, Any],
) -> Dict[str, Any]:
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
        "process_console_href": f"/process-console?asset_id={asset_id}",
        "compare_to_previous_href": f"/process-console?asset_id={asset_id}&compare_index=0",
    }


def _build_background_summary(
    *,
    asset_id: str,
    asset_name: str,
    latest_updated_at: Optional[str],
    provenance_only_count: int,
    routed: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "node_type": "background_summary",
        "asset_id": asset_id,
        "asset_name": asset_name,
        "priority_level": routed.get("priority_level", "background"),
        "attention_reason": routed.get("attention_reason"),
        "queue_status": "suppressed",
        "provenance_only_count": provenance_only_count,
        "latest_updated_at": latest_updated_at,
        "summary": f"{provenance_only_count} background provenance-only updates on {asset_name}",
        "process_console_href": f"/process-console?asset_id={asset_id}",
    }


def _sort_queue_items(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        items,
        key=lambda row: (
            PRIORITY_ORDER.get(str(row.get("priority_level")), 99),
            str(row.get("latest_updated_at") or ""),
            str(row.get("asset_id") or ""),
        ),
        reverse=False,
    )


def write_state_change_attention_queue_surface(runtime_root: Path) -> Dict[str, Any]:
    runtime_root = runtime_root.resolve()
    store = JsonDirectoryStore(runtime_root / "views" / "state_change_attention_queue")
    index = load_engine_state_index(runtime_root)
    active_items: List[Dict[str, Any]] = []
    background_summaries: List[Dict[str, Any]] = []
    resolved_items: List[Dict[str, Any]] = []
    asset_views: List[Dict[str, Any]] = []

    for item in index.get("items", []):
        asset_id = str(item.get("asset_id") or "")
        if not asset_id:
            continue
        previous_asset_view = store.get(asset_id)
        latest = _load_latest_state(runtime_root, asset_id)
        if not latest:
            continue
        history_rows = load_engine_state_history(runtime_root, asset_id)
        diff_pair = select_adjacent_history_pair(history_rows, compare_index=0)
        diff = build_state_change_diff(diff_pair.get("current"), diff_pair.get("previous"))
        diff["interpretation_badges"] = build_diff_interpretation_badges(diff)
        routed = route_runtime_evidence_priority(asset_id=asset_id, diff=diff)
        queue_item = _build_queue_item(
            asset_id=asset_id,
            asset_name=str(latest.get("asset_name") or asset_id),
            diff=diff,
            routed=routed,
        )
        provenance_only_count = _recent_provenance_only_runtime_count(history_rows)

        current_background_summary = None
        if not routed.get("queue_candidate") and provenance_only_count > 0:
            current_background_summary = _build_background_summary(
                asset_id=asset_id,
                asset_name=str(latest.get("asset_name") or asset_id),
                latest_updated_at=queue_item.get("latest_updated_at"),
                provenance_only_count=provenance_only_count,
                routed=routed,
            )

        lifecycle = apply_attention_resolution_loop(
            previous_asset_view=previous_asset_view,
            current_item=queue_item if routed.get("queue_candidate") else None,
            background_summary=current_background_summary,
        )

        if lifecycle["latest_item"]:
            active_items.append(lifecycle["latest_item"])
        if lifecycle["background_summary"]:
            background_summaries.append(lifecycle["background_summary"])
        resolved_items.extend(lifecycle["resolved_items"])

        asset_view = {
            "asset_id": asset_id,
            "asset_name": latest.get("asset_name"),
            "latest_item": lifecycle["latest_item"],
            "background_summary": lifecycle["background_summary"],
            "resolved_items": lifecycle["resolved_items"],
            "generated_at": _now_iso(),
        }
        asset_views.append(asset_view)
        store.put(asset_id, asset_view)

    active_items = _sort_queue_items(active_items)
    background_summaries = sorted(
        background_summaries,
        key=lambda row: (
            str(row.get("latest_updated_at") or ""),
            str(row.get("asset_id") or ""),
        ),
        reverse=True,
    )
    payload = {
        "state": "loaded",
        "generated_at": _now_iso(),
        "items": active_items,
        "background_summaries": background_summaries,
        "resolved_items": sorted(
            resolved_items,
            key=lambda row: (
                str(row.get("resolved_at") or row.get("latest_updated_at") or ""),
                str(row.get("asset_id") or ""),
            ),
            reverse=True,
        )[:20],
        "counts": {
            "active": len(active_items),
            "background_summaries": len(background_summaries),
            "resolved": len(resolved_items),
        },
    }
    store.put("index", payload)
    from app.runtime.state_attention_memory import write_state_attention_memory_surface

    write_state_attention_memory_surface(runtime_root)
    return payload


def load_state_change_attention_queue_index(runtime_root: Path) -> Dict[str, Any]:
    path = runtime_root / "views" / "state_change_attention_queue" / "index.json"
    if not path.exists():
        return {
            "state": "queue_unavailable",
            "items": [],
            "background_summaries": [],
            "resolved_items": [],
            "counts": {"active": 0, "background_summaries": 0, "resolved": 0},
        }
    return json.loads(path.read_text(encoding="utf-8"))


def select_asset_attention_entry(queue_index: Dict[str, Any], asset_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not asset_id:
        return None
    for item in queue_index.get("items", []):
        if item.get("asset_id") == asset_id:
            return {"kind": "active_item", **item}
    for item in queue_index.get("background_summaries", []):
        if item.get("asset_id") == asset_id:
            return {"kind": "background_summary", **item}
    for item in queue_index.get("resolved_items", []):
        if item.get("asset_id") == asset_id:
            return {"kind": "resolved_item", **item}
    return None
