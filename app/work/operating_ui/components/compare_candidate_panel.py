from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_compare_candidate_panel_view(
    *,
    selectedAsset: Optional[Dict[str, Any]],
    compareCandidates: Optional[List[Dict[str, Any]]],
    liveAvailability: str,
    guards: Optional[Dict[str, Any]] = None,
    emptyLabel: str = "no compare candidates",
) -> Dict[str, Any]:
    guard_state = guards or {}

    if liveAvailability == "live_unavailable":
        return {
            "state": "live_unavailable",
            "title": "Compare Candidates",
            "count": 0,
            "items": [],
            "helperText": "compare candidates unavailable",
        }

    if not selectedAsset:
        state = "state_unavailable" if guard_state.get("stateUnavailable") else "no_selected_asset"
        helper = (
            "compare candidates unavailable"
            if state == "state_unavailable"
            else "select an asset to inspect compare candidates"
        )
        return {
            "state": state,
            "title": "Compare Candidates",
            "count": 0,
            "items": [],
            "helperText": helper,
        }

    rows = []
    for item in compareCandidates or []:
        if not isinstance(item, dict):
            continue
        asset_id = item.get("assetId") or item.get("asset_id")
        reason = item.get("reason") or item.get("label")
        if asset_id or reason:
            rows.append(
                {
                    "assetId": asset_id,
                    "title": item.get("title") or asset_id,
                    "reason": reason,
                }
            )

    if not rows:
        return {
            "state": "empty",
            "title": "Compare Candidates",
            "count": 0,
            "items": [],
            "helperText": emptyLabel,
        }

    return {
        "state": "loaded",
        "title": "Compare Candidates",
        "count": len(rows),
        "items": rows,
        "helperText": None,
    }


def render_compare_candidate_panel_text(view: Dict[str, Any]) -> str:
    state = view.get("state")
    if state != "loaded":
        return f"CompareCandidatePanel[state={state}] | {view.get('helperText') or 'unavailable'}"

    lines = [f"CompareCandidatePanel[count={view.get('count', 0)}]"]
    for item in view.get("items", []):
        parts = [
            item.get("title") or item.get("assetId") or "candidate",
            item.get("reason") or "compare candidate",
        ]
        lines.append("- " + " | ".join(part for part in parts if part))
    return "\n".join(lines)
