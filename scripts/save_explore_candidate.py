from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.active_asset_first_pass_alignment import ensure_active_asset_first_pass_fragments
from app.runtime.runtime_preflight import build_runtime_preflight
from app.runtime.saved_connections import create_saved_connection_from_candidate, load_saved_connections
from app.runtime.user_page_shell import _build_explore_candidates, _build_explore_reading_context, _build_source


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    asset_id = sys.argv[2] if len(sys.argv) > 2 else None
    candidate_id = sys.argv[3] if len(sys.argv) > 3 else None

    build_runtime_preflight(
        runtime_root,
        requested_mode="space_reading",
        requested_artifact_ref=asset_id,
        page_key="explore",
    )
    source = _build_source(runtime_root, asset_id=asset_id)
    candidates = _build_explore_candidates(
        source["selected_asset"],
        raw_asset=source.get("raw_selected_asset") or {},
    )
    if not candidates:
        print(json.dumps({"saved": False, "reason": "no_candidates"}, ensure_ascii=False, indent=2))
        return 0

    target = None
    if candidate_id:
        for candidate in candidates:
            if candidate.get("id") == candidate_id:
                target = candidate
                break
    if target is None:
        target = candidates[0]

    reading_context = _build_explore_reading_context(
        asset_id=source["selected_asset_id"],
        raw_asset=source.get("raw_selected_asset") or {},
        candidate=target,
    )
    ensure_active_asset_first_pass_fragments(
        runtime_root,
        raw_asset=source.get("raw_selected_asset") or {},
    )
    record, created = create_saved_connection_from_candidate(
        runtime_root,
        candidate=target,
        reading_context=reading_context,
    )
    print(
        json.dumps(
            {
                "saved": created,
                "selected_candidate_id": target.get("id"),
                "record": record,
                "saved_connection_count": len(load_saved_connections(runtime_root)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
