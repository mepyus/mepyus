from __future__ import annotations

from typing import Any, Callable, Dict, Optional


def build_derived_state_strip_view(
    *,
    selectedAsset: Optional[Dict[str, Any]],
    latestPreview: Optional[Dict[str, Any]],
    diffSummary: Optional[Dict[str, Any]],
    attentionSummary: Optional[Dict[str, Any]],
    memorySummary: Optional[Dict[str, Any]],
    compareHref: Optional[str] = None,
    onOpenDiff: Optional[Callable[[], None]] = None,
    onOpenAttention: Optional[Callable[[], None]] = None,
    onOpenMemory: Optional[Callable[[], None]] = None,
) -> Dict[str, Any]:
    if not selectedAsset:
        return {
            "state": "no_selected_asset",
            "title": None,
            "badges": [],
            "latestLine": None,
            "diffLine": "select an asset to inspect state",
            "attentionLine": "no active attention",
            "memoryLine": "insufficient attention history",
            "canOpenDiff": False,
            "canOpenAttention": False,
            "canOpenMemory": False,
            "compareHref": None,
        }

    badges = [
        row.get("label")
        for row in selectedAsset.get("canonicalStateRows", [])
        if isinstance(row, dict) and row.get("label")
    ][:4]

    latest_line = None
    if latestPreview:
        latest_line = " / ".join(
            value
            for value in [
                latestPreview.get("packetTexture"),
                latestPreview.get("maturation"),
                latestPreview.get("traceability"),
            ]
            if value
        )

    diff = diffSummary or {}
    diff_state = diff.get("state") or "state_unavailable"
    if diff_state == "no_previous_state":
        diff_line = "compare to previous unavailable"
        can_open_diff = False
    elif diff_state == "state_unavailable":
        diff_line = "no canonical state yet"
        can_open_diff = False
    else:
        diff_class = diff.get("diffClass") or "loaded"
        changed_count = diff.get("changedFieldCount", 0)
        provenance_only = bool(diff.get("provenanceOnly"))
        diff_line = f"{diff_class} / changed={changed_count}"
        if provenance_only:
            diff_line += " / provenance only"
        can_open_diff = bool(compareHref or onOpenDiff)

    if attentionSummary:
        attention_line = " / ".join(
            value
            for value in [
                attentionSummary.get("priority"),
                attentionSummary.get("reason"),
                attentionSummary.get("queueStatus"),
            ]
            if value
        ) or "attention loaded"
        can_open_attention = bool(onOpenAttention)
    else:
        attention_line = "no active attention"
        can_open_attention = False

    memory = memorySummary or {}
    memory_label = memory.get("summary") or "insufficient attention history"
    if memory_label == "insufficient_attention_history":
        memory_line = "insufficient attention history"
        can_open_memory = False
    else:
        density = memory.get("provenanceDensity")
        dominant = ", ".join(memory.get("dominantShiftTypes", [])[:2])
        extras = []
        if density is not None:
            extras.append(f"density={density}")
        if dominant:
            extras.append(f"shift={dominant}")
        memory_line = " / ".join([memory_label] + extras)
        can_open_memory = bool(onOpenMemory)

    return {
        "state": "loaded",
        "title": selectedAsset.get("title"),
        "badges": badges,
        "latestLine": latest_line,
        "diffLine": diff_line,
        "attentionLine": attention_line,
        "memoryLine": memory_line,
        "canOpenDiff": can_open_diff,
        "canOpenAttention": can_open_attention,
        "canOpenMemory": can_open_memory,
        "compareHref": compareHref if can_open_diff else None,
    }


def render_derived_state_strip_text(view: Dict[str, Any]) -> str:
    if view.get("state") == "no_selected_asset":
        return "DerivedStateStrip[state=no_selected_asset] | select an asset to inspect state"

    parts = [
        f"DerivedStateStrip[{view.get('title')}]",
        view.get("latestLine") or "latest unavailable",
        f"diff={view.get('diffLine')}",
        f"attention={view.get('attentionLine')}",
        f"memory={view.get('memoryLine')}",
    ]
    if view.get("badges"):
        parts.append(f"badges={', '.join(view.get('badges', []))}")
    return " | ".join(part for part in parts if part)
