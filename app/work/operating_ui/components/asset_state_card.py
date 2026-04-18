from __future__ import annotations

from typing import Any, Callable, Dict, Optional


def build_asset_state_card_view(
    item: Dict[str, Any],
    *,
    selected: bool = False,
    show_compare_reason: bool = False,
    show_attention_hint: bool = False,
    href: Optional[str] = None,
    onClick: Optional[Callable[[str], None]] = None,
    onOpenDetail: Optional[Callable[[str], None]] = None,
) -> Dict[str, Any]:
    row = item if isinstance(item, dict) else {}
    asset_id = row.get("id")
    title = row.get("title") or asset_id or "unknown_asset"
    packet = row.get("packetTextureLabel") or "packet unknown"
    maturation = row.get("maturationLabel") or "maturation unknown"
    traceability = row.get("traceabilityLabel") or "traceability unavailable"
    emergence = row.get("emergenceLabel") or "emergence unavailable"
    grounding = row.get("groundingLabel")

    meta_lines = [
        packet,
        maturation,
        traceability,
        emergence,
    ]
    if grounding:
        meta_lines.insert(3, grounding)

    badges = []
    if selected:
        badges.append("selected")
    if show_compare_reason and row.get("compareReason"):
        badges.append(f"compare: {row.get('compareReason')}")
    if show_attention_hint and row.get("attentionHint"):
        badges.append(f"attention: {row.get('attentionHint')}")

    helper = []
    if not grounding:
        helper.append("grounding not surfaced in board card v1")
    if row.get("updatedAt"):
        helper.append(f"updated {row.get('updatedAt')}")

    return {
        "state": "loaded" if asset_id else "empty",
        "assetId": asset_id,
        "title": title,
        "selected": selected,
        "primarySummary": f"{packet} / {maturation}",
        "secondarySummary": " / ".join(
            value for value in [traceability, grounding, emergence] if value
        ),
        "badges": badges,
        "helperText": " | ".join(helper) if helper else None,
        "href": href if asset_id else None,
        "canClick": bool(asset_id and onClick is not None),
        "canOpenDetail": bool(asset_id and onOpenDetail is not None),
    }


def render_asset_state_card_text(view: Dict[str, Any]) -> str:
    if view.get("state") != "loaded":
        return "AssetStateCard[state=empty]"

    parts = [
        f"AssetStateCard[{view.get('assetId')}]",
        view.get("primarySummary") or "",
        view.get("secondarySummary") or "",
    ]
    if view.get("badges"):
        parts.append(f"badges={', '.join(view.get('badges', []))}")
    if view.get("helperText"):
        parts.append(f"helper={view.get('helperText')}")
    return " | ".join(part for part in parts if part)
