from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.internal_search_minimum import build_internal_search_panel_payload
from app.work.operating_ui.components.internal_search_panel import (
    build_internal_search_panel_view,
    render_internal_search_panel_text,
)
from app.work.operating_ui.operating_ui_payload_adapter import (
    adapt_process_console_payload_to_operating_ui_model,
)


FIXTURE_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "fixtures"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "operating_ui" / "generated"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render capability-aware internal search operating panel.")
    parser.add_argument("runtime_root", help="Runtime root path")
    parser.add_argument("--query", action="append", dest="queries", help="Query to search")
    parser.add_argument("--fixture-case", default="a", help="Operating UI fixture case to use")
    parser.add_argument("--selected-candidate-id", default=None)
    parser.add_argument("--stdout-only", action="store_true")
    args = parser.parse_args()

    runtime_root = (REPO_ROOT / args.runtime_root).resolve() if not Path(args.runtime_root).is_absolute() else Path(args.runtime_root)
    queries = [query for query in (args.queries or ["input observer", "sandbox trip", "validation"]) if query]

    base_payload = _load_fixture_payload(args.fixture_case)
    rendered_cases: List[Dict[str, Any]] = []
    for query in queries:
        panel_payload = build_internal_search_panel_payload(
            runtime_root,
            query=query,
            selected_candidate_id=args.selected_candidate_id,
        )
        model = adapt_process_console_payload_to_operating_ui_model(
            base_payload,
            internal_search_panel=panel_payload,
        )
        panel_view = build_internal_search_panel_view(
            query=query,
            results=panel_payload.get("results"),
            selectedResult=panel_payload.get("selectedResult"),
            summary=panel_payload.get("summary"),
        )
        rendered_cases.append(
            {
                "query": query,
                "panel_payload": panel_payload,
                "panel_view": panel_view,
                "panel_text": render_internal_search_panel_text(panel_view),
                "operating_ui_model_excerpt": {
                    "pageTitle": model.get("pageTitle"),
                    "selectedAssetId": model.get("selectedAssetId"),
                    "internalSearchPanel": model.get("internalSearchPanel"),
                },
            }
        )

    output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "runtime_root": str(runtime_root),
        "fixture_case": args.fixture_case,
        "cases": rendered_cases,
    }

    if args.stdout_only:
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_path = OUTPUT_ROOT / f"internal_search_panel_demo_{timestamp}.json"
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"written": str(output_path), "case_count": len(rendered_cases)}, ensure_ascii=False, indent=2))
    return 0


def _load_fixture_payload(case: str) -> Dict[str, Any]:
    path = FIXTURE_ROOT / f"process_console_payload_case_{case.lower()}.json"
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
