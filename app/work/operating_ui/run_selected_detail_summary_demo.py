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
from app.work.operating_ui.components.selected_asset_detail_summary import (
    build_selected_asset_detail_summary_view,
    render_selected_asset_detail_summary_text,
)


FIXTURE_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "fixtures"


def main() -> int:
    cases = {
        "normal_selected": _build_from_fixture("a"),
        "no_previous_state": _build_from_fixture("b"),
        "insufficient_attention_history": _build_from_fixture("c"),
        "state_unavailable": _build_from_fixture("d"),
        "no_selected_asset": _build_no_selected_case(),
    }
    print(json.dumps(cases, ensure_ascii=False, indent=2))
    return 0


def _build_from_fixture(case: str):
    raw = json.loads((FIXTURE_ROOT / f"process_console_payload_case_{case}.json").read_text(encoding="utf-8"))
    model = adapt_process_console_payload_to_operating_ui_model(raw)
    view = build_selected_asset_detail_summary_view(
        selectedAsset=model.get("selectedAsset"),
        latestPreview=(model.get("derivedStrip") or {}).get("latestPreview"),
        diffSummary=(model.get("derivedStrip") or {}).get("diffSummary"),
        attentionSummary=(model.get("derivedStrip") or {}).get("attentionSummary"),
        memorySummary=(model.get("derivedStrip") or {}).get("memorySummary"),
        compareCandidates=model.get("compareCandidates"),
        guards=model.get("guards"),
    )
    return {"view": view, "text": render_selected_asset_detail_summary_text(view)}


def _build_no_selected_case():
    raw = json.loads((FIXTURE_ROOT / "process_console_payload_case_a.json").read_text(encoding="utf-8"))
    model = adapt_process_console_payload_to_operating_ui_model(raw)
    view = build_selected_asset_detail_summary_view(
        selectedAsset=None,
        latestPreview=(model.get("derivedStrip") or {}).get("latestPreview"),
        diffSummary=(model.get("derivedStrip") or {}).get("diffSummary"),
        attentionSummary=(model.get("derivedStrip") or {}).get("attentionSummary"),
        memorySummary=(model.get("derivedStrip") or {}).get("memorySummary"),
        compareCandidates=model.get("compareCandidates"),
        guards={"stateUnavailable": False},
    )
    return {"view": view, "text": render_selected_asset_detail_summary_text(view)}


if __name__ == "__main__":
    raise SystemExit(main())
