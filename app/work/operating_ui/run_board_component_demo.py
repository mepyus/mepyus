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
from app.work.operating_ui.components.asset_state_board import (
    build_asset_state_board_view,
    render_asset_state_board_text,
)


FIXTURE_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "fixtures"


def main() -> int:
    case_a = adapt_process_console_payload_to_operating_ui_model(
        _load_json(FIXTURE_ROOT / "process_console_payload_case_a.json")
    )
    case_d = adapt_process_console_payload_to_operating_ui_model(
        _load_json(FIXTURE_ROOT / "process_console_payload_case_d.json")
    )

    results = {
        "normal_selected": _demo_board(case_a["boardItems"], selected_asset_id=case_a["selectedAssetId"]),
        "invalid_selected": _demo_board(case_a["boardItems"], selected_asset_id="missing_asset"),
        "none_selected": _demo_board(case_a["boardItems"], selected_asset_id=None),
        "empty_board": _demo_board(case_d["boardItems"], selected_asset_id=None),
    }
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


def _demo_board(items, *, selected_asset_id):
    view = build_asset_state_board_view(
        items,
        selectedAssetId=selected_asset_id,
        sortLabel="updated_at",
        filterSummary="packet_texture=all",
        baseHref="/operating-ui-live",
    )
    return {
        "view": view,
        "text": render_asset_state_board_text(view),
    }


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
