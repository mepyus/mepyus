from __future__ import annotations

from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.work.operating_ui.operating_ui_payload_adapter import (
    adapt_process_console_payload_to_operating_ui_model,
)
from app.work.operating_ui.components.asset_state_card import (
    build_asset_state_card_view,
    render_asset_state_card_text,
)
from app.work.operating_ui.components.derived_state_strip import (
    build_derived_state_strip_view,
    render_derived_state_strip_text,
)


FIXTURE_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "fixtures"


def main() -> int:
    cases = ["a", "b", "c", "d"]
    output = {"results": []}

    for case in cases:
        raw = json.loads((FIXTURE_ROOT / f"process_console_payload_case_{case}.json").read_text(encoding="utf-8"))
        model = adapt_process_console_payload_to_operating_ui_model(raw)

        first_card = model["boardItems"][0] if model.get("boardItems") else {}
        card_view = build_asset_state_card_view(first_card, selected=True)
        strip_view = build_derived_state_strip_view(
            selectedAsset=model.get("selectedAsset"),
            latestPreview=(model.get("derivedStrip") or {}).get("latestPreview"),
            diffSummary=(model.get("derivedStrip") or {}).get("diffSummary"),
            attentionSummary=(model.get("derivedStrip") or {}).get("attentionSummary"),
            memorySummary=(model.get("derivedStrip") or {}).get("memorySummary"),
            compareHref="/compare" if (model.get("derivedStrip") or {}).get("diffSummary", {}).get("state") == "loaded" else None,
        )

        output["results"].append(
            {
                "case": case.upper(),
                "card": card_view,
                "card_text": render_asset_state_card_text(card_view),
                "strip": strip_view,
                "strip_text": render_derived_state_strip_text(strip_view),
            }
        )

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
