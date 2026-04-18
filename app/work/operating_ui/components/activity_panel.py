from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional


def build_activity_panel_view(
    items: List[Dict[str, Any]],
    *,
    historySummary: Optional[Dict[str, Any]] = None,
    latestLineage: Optional[Dict[str, Any]] = None,
    emptyLabel: str = "no recent activity",
    onOpenHistoryItem: Optional[Callable[[int], None]] = None,
    onOpenDiff: Optional[Callable[[int], None]] = None,
) -> Dict[str, Any]:
    rows = [item for item in (items if isinstance(items, list) else []) if isinstance(item, dict)]
    history_summary = historySummary if isinstance(historySummary, dict) else {}
    latest_lineage = latestLineage if isinstance(latestLineage, dict) else {}

    latest_lineage_view = _build_latest_lineage_view(latest_lineage)
    diff_hint = _build_diff_hint(history_summary)

    if not rows:
        state = "history_unavailable" if history_summary.get("state") == "history_unavailable" else "empty"
        return {
            "state": state,
            "items": [],
            "emptyLabel": "history unavailable" if state == "history_unavailable" else emptyLabel,
            "latestLineage": latest_lineage_view,
            "diffHint": diff_hint,
            "hasHistoryCta": False,
            "hasDiffCta": False,
        }

    adapted_items = []
    for index, row in enumerate(rows):
        compare_index = row.get("compareIndex")
        adapted_items.append(
            {
                "state": "loaded",
                "id": row.get("id") or f"activity-{index}",
                "label": row.get("label") or row.get("reason") or row.get("triggerType") or "activity",
                "activityType": row.get("activityType") or row.get("triggerType") or "runtime",
                "summary": row.get("summary") or row.get("reason") or "recent activity",
                "timestamp": row.get("updatedAt") or row.get("timestamp"),
                "lineageMarker": row.get("lineageMarker") or None,
                "diffMarker": row.get("diffMarker") or ("compare available" if compare_index is not None else None),
                "canOpenHistoryItem": bool(compare_index is not None and onOpenHistoryItem is not None),
                "canOpenDiff": bool(compare_index is not None and onOpenDiff is not None),
                "compareIndex": compare_index,
            }
        )

    return {
        "state": "loaded",
        "items": adapted_items,
        "emptyLabel": None,
        "latestLineage": latest_lineage_view,
        "diffHint": diff_hint,
        "hasHistoryCta": any(item["canOpenHistoryItem"] for item in adapted_items),
        "hasDiffCta": any(item["canOpenDiff"] for item in adapted_items),
    }


def render_activity_panel_text(view: Dict[str, Any]) -> str:
    state = view.get("state")
    if state in {"empty", "history_unavailable"}:
        base = f"ActivityPanel[state={state}] | {view.get('emptyLabel')}"
        if view.get("latestLineage", {}).get("summary"):
            base += f" | lineage={view['latestLineage']['summary']}"
        if view.get("diffHint", {}).get("summary"):
            base += f" | diff={view['diffHint']['summary']}"
        return base

    header_parts = ["ActivityPanel[state=loaded]"]
    lineage = view.get("latestLineage", {})
    if lineage.get("summary"):
        header_parts.append(f"lineage={lineage['summary']}")
    diff_hint = view.get("diffHint", {})
    if diff_hint.get("summary"):
        header_parts.append(f"diff={diff_hint['summary']}")

    lines = [" | ".join(header_parts)]
    for item in view.get("items", []):
        parts = [
            item.get("label") or "activity",
            item.get("activityType") or "",
            item.get("summary") or "",
        ]
        if item.get("timestamp"):
            parts.append(str(item.get("timestamp")))
        if item.get("diffMarker"):
            parts.append(f"diff={item.get('diffMarker')}")
        lines.append("- " + " | ".join(part for part in parts if part))
    return "\n".join(lines)


def _build_latest_lineage_view(latest_lineage: Dict[str, Any]) -> Dict[str, Any]:
    if not latest_lineage:
        return {"state": "absent", "summary": None}
    return {
        "state": "loaded",
        "summary": latest_lineage.get("summary"),
        "latestTrigger": latest_lineage.get("latestTrigger") or latest_lineage.get("latest_update_trigger_type"),
        "latestReason": latest_lineage.get("latestReason") or latest_lineage.get("latest_update_reason"),
        "latestUpdatedAt": latest_lineage.get("latestUpdatedAt") or latest_lineage.get("latest_updated_at"),
    }


def _build_diff_hint(history_summary: Dict[str, Any]) -> Dict[str, Any]:
    if not history_summary:
        return {"state": "absent", "summary": None, "canOpenDiff": False}

    latest_change_kind = history_summary.get("latestChangeKind") or history_summary.get("latest_change_kind")
    latest_reason = history_summary.get("latestReason") or history_summary.get("latest_update_reason")
    if not latest_change_kind and not latest_reason:
        return {"state": "absent", "summary": None, "canOpenDiff": False}

    summary = latest_change_kind or latest_reason
    return {
        "state": "loaded",
        "summary": summary,
        "canOpenDiff": latest_change_kind not in {None, "no_previous_state", "state_unavailable"},
    }
