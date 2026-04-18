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
from app.work.operating_ui.components.activity_panel import (
    build_activity_panel_view,
    render_activity_panel_text,
)


FIXTURE_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "fixtures"


def main() -> int:
    case_a_raw = _load_json(FIXTURE_ROOT / "process_console_payload_case_a.json")
    case_b_raw = _load_json(FIXTURE_ROOT / "process_console_payload_case_b.json")
    case_d_raw = _load_json(FIXTURE_ROOT / "process_console_payload_case_d.json")

    case_a_model = adapt_process_console_payload_to_operating_ui_model(case_a_raw)
    case_b_model = adapt_process_console_payload_to_operating_ui_model(case_b_raw)
    case_d_model = adapt_process_console_payload_to_operating_ui_model(case_d_raw)

    results = {
        "normal_activity": _demo_panel(
            case_a_model["activityPanel"]["items"],
            history_summary={"latestChangeKind": "canonical_change", "latestReason": "first_live_run_turboquant_youtube_v1"},
            latest_lineage=case_a_model["activityPanel"],
        ),
        "empty_activity_with_lineage": _demo_panel(
            case_b_model["activityPanel"]["items"],
            history_summary={"latestChangeKind": "no_previous_state", "latestReason": "lecture_transcript_cohort_batch_test_v1"},
            latest_lineage=case_b_model["activityPanel"],
        ),
        "history_unavailable": _demo_panel(
            case_d_model["activityPanel"]["items"],
            history_summary={"state": "history_unavailable"},
            latest_lineage=None,
        ),
        "latest_lineage_absent": _demo_panel(
            case_a_model["activityPanel"]["items"],
            history_summary={"latestChangeKind": "canonical_change"},
            latest_lineage=None,
        ),
    }

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


def _demo_panel(items, *, history_summary=None, latest_lineage=None):
    view = build_activity_panel_view(
        items,
        historySummary=history_summary,
        latestLineage=latest_lineage,
    )
    return {
        "view": view,
        "text": render_activity_panel_text(view),
    }


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
