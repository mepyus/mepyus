from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_selected_asset_detail_summary_view(
    *,
    selectedAsset: Optional[Dict[str, Any]],
    latestPreview: Optional[Dict[str, Any]],
    diffSummary: Optional[Dict[str, Any]],
    attentionSummary: Optional[Dict[str, Any]],
    memorySummary: Optional[Dict[str, Any]],
    compareCandidates: Optional[List[Dict[str, Any]]] = None,
    guards: Optional[Dict[str, Any]] = None,
    statusBadge: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    guard_state = guards or {}
    if not selectedAsset:
        state = "state_unavailable" if guard_state.get("stateUnavailable") else "no_selected_asset"
        return {
            "state": state,
            "title": None,
            "subtitle": None,
            "statusBadge": None,
            "meta": [],
            "canonicalSummary": [],
            "latestSummary": None,
            "diffSummary": _neutral_diff_summary(diffSummary, state=state),
            "attentionSummary": _neutral_attention_summary(attentionSummary),
            "memorySummary": _neutral_memory_summary(memorySummary),
            "compareSummary": [],
            "helperText": "selected asset has no canonical state yet" if state == "state_unavailable" else "select an asset to open detail",
        }

    canonical_rows = [
        row for row in (selectedAsset.get("canonicalStateRows") or [])
        if isinstance(row, dict) and row.get("label")
    ]
    canonical_summary = [
        {"key": row.get("key"), "label": row.get("label")}
        for row in canonical_rows[:6]
    ]

    latest_summary = None
    if latestPreview:
        latest_summary = " / ".join(
            value for value in [
                latestPreview.get("packetTexture"),
                latestPreview.get("maturation"),
                latestPreview.get("traceability"),
            ] if value
        ) or None

    compare_items = []
    for item in (compareCandidates or [])[:3]:
        if isinstance(item, dict):
            label = item.get("reason") or item.get("label")
            asset_id = item.get("assetId") or item.get("asset_id")
            if label or asset_id:
                compare_items.append({"assetId": asset_id, "label": label or asset_id})

    return {
        "state": "loaded",
        "title": selectedAsset.get("title"),
        "subtitle": selectedAsset.get("subtitle"),
        "statusBadge": statusBadge if isinstance(statusBadge, dict) and statusBadge.get("label") else None,
        "meta": [
            value for value in [
                selectedAsset.get("updatedAt"),
                selectedAsset.get("scopeLabel"),
            ] if value
        ],
        "canonicalSummary": canonical_summary,
        "latestSummary": latest_summary,
        "diffSummary": _build_diff_summary(diffSummary),
        "attentionSummary": _build_attention_summary(attentionSummary),
        "memorySummary": _build_memory_summary(memorySummary),
        "compareSummary": compare_items,
        "helperText": selectedAsset.get("stateNotes"),
    }


def render_selected_asset_detail_summary_text(view: Dict[str, Any]) -> str:
    state = view.get("state")
    if state != "loaded":
        return f"SelectedAssetDetailSummary[state={state}] | {view.get('helperText') or 'unavailable'}"

    parts = [
        f"SelectedAssetDetailSummary[{view.get('title')}]",
    ]
    status_badge = view.get("statusBadge") or {}
    if status_badge.get("label"):
        parts.append(f"badge={status_badge['label']}")
    if view.get("subtitle"):
        parts.append(str(view.get("subtitle")))
    if view.get("latestSummary"):
        parts.append(f"latest={view.get('latestSummary')}")
    if view.get("diffSummary", {}).get("label"):
        parts.append(f"diff={view['diffSummary']['label']}")
    if view.get("attentionSummary", {}).get("label"):
        parts.append(f"attention={view['attentionSummary']['label']}")
    if view.get("memorySummary", {}).get("label"):
        parts.append(f"memory={view['memorySummary']['label']}")
    if view.get("compareSummary"):
        parts.append(
            "compare=" + ", ".join(item.get("label") or "" for item in view.get("compareSummary", []))
        )
    return " | ".join(part for part in parts if part)


def _build_diff_summary(diff: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    diff = diff or {}
    state = diff.get("state") or "state_unavailable"
    if state == "no_previous_state":
        return {"state": state, "label": "compare to previous unavailable"}
    if state == "state_unavailable":
        return {"state": state, "label": "no canonical state yet"}
    label = diff.get("diffClass") or "loaded"
    changed = diff.get("changedFieldCount")
    if changed is not None:
        label = f"{label} / changed={changed}"
    if diff.get("provenanceOnly"):
        label += " / provenance only"
    return {"state": state, "label": label}


def _neutral_diff_summary(diff: Optional[Dict[str, Any]], *, state: str) -> Dict[str, Any]:
    if state == "state_unavailable":
        return {"state": "state_unavailable", "label": "selected asset has no canonical state yet"}
    return _build_diff_summary(diff)


def _build_attention_summary(attention: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not attention:
        return {"state": "no_active_attention", "label": "no active attention"}
    label = " / ".join(
        value for value in [
            attention.get("priority"),
            attention.get("reason"),
            attention.get("queueStatus"),
        ] if value
    ) or "attention loaded"
    return {"state": attention.get("state") or "loaded", "label": label}


def _neutral_attention_summary(attention: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return _build_attention_summary(attention)


def _build_memory_summary(memory: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not memory:
        return {"state": "insufficient_attention_history", "label": "insufficient attention history"}
    summary = memory.get("summary") or "insufficient attention history"
    if summary == "insufficient_attention_history":
        return {"state": "insufficient_attention_history", "label": "insufficient attention history"}
    extras = []
    if memory.get("provenanceDensity") is not None:
        extras.append(f"density={memory.get('provenanceDensity')}")
    if memory.get("dominantShiftTypes"):
        extras.append("shift=" + ", ".join(memory.get("dominantShiftTypes", [])[:2]))
    label = " / ".join([summary] + extras) if extras else summary
    return {"state": "loaded", "label": label}


def _neutral_memory_summary(memory: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    return _build_memory_summary(memory)
