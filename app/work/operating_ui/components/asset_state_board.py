from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional

from app.work.operating_ui.components.asset_state_card import (
    build_asset_state_card_view,
    render_asset_state_card_text,
)


def build_asset_state_board_view(
    items: List[Dict[str, Any]],
    *,
    selectedAssetId: Optional[str] = None,
    emptyLabel: str = "no assets available",
    sortLabel: Optional[str] = None,
    filterSummary: Optional[str] = None,
    baseHref: Optional[str] = None,
    onSelectAsset: Optional[Callable[[str], None]] = None,
) -> Dict[str, Any]:
    rows = [item for item in (items if isinstance(items, list) else []) if isinstance(item, dict)]
    if not rows:
        return {
            "state": "empty",
            "items": [],
            "emptyLabel": emptyLabel,
            "sortLabel": sortLabel,
            "filterSummary": filterSummary,
            "selectedAssetId": None,
            "selectionState": "empty_board",
        }

    valid_ids = {row.get("id") for row in rows if row.get("id")}
    selected_id = selectedAssetId if selectedAssetId in valid_ids else None
    selection_state = (
        "selected"
        if selected_id
        else ("invalid_selected_asset" if selectedAssetId and selectedAssetId not in valid_ids else "none_selected")
    )

    cards = []
    for row in rows:
        asset_id = row.get("id")
        card = build_asset_state_card_view(
            row,
            selected=bool(selected_id and asset_id == selected_id),
            href=(f"{baseHref}?asset_id={asset_id}" if baseHref and asset_id else None),
            onClick=onSelectAsset,
        )
        cards.append(card)

    return {
        "state": "loaded",
        "items": cards,
        "emptyLabel": None,
        "sortLabel": sortLabel,
        "filterSummary": filterSummary,
        "selectedAssetId": selected_id,
        "selectionState": selection_state,
        "hasSelectableCallback": onSelectAsset is not None,
    }


def render_asset_state_board_text(view: Dict[str, Any]) -> str:
    if view.get("state") == "empty":
        return f"AssetStateBoard[state=empty] | {view.get('emptyLabel') or 'no assets available'}"

    header_bits = [
        f"AssetStateBoard[state={view.get('state')}]",
        f"selection={view.get('selectionState')}",
    ]
    if view.get("sortLabel"):
        header_bits.append(f"sort={view.get('sortLabel')}")
    if view.get("filterSummary"):
        header_bits.append(f"filter={view.get('filterSummary')}")

    lines = [" | ".join(header_bits)]
    for card in view.get("items", []):
        lines.append(f"- {render_asset_state_card_text(card)}")
    return "\n".join(lines)
