from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.explore_candidate_extractor import extract_explore_candidates
from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
from app.runtime.runtime_preflight import build_runtime_preflight
from app.runtime.user_page_shell import _normalize_asset


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    asset_id = sys.argv[2] if len(sys.argv) > 2 else None

    build_runtime_preflight(
        runtime_root,
        requested_mode="space_reading",
        requested_artifact_ref=asset_id,
        page_key="explore",
    )
    live = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    raw_asset = ((live.get("adapted_model") or {}).get("selectedAsset") or {}) if live.get("state") == "loaded" else {}
    fallback_id = str(live.get("selected_asset_id") or asset_id or "sample-input")
    normalized = _normalize_asset(raw_asset, fallback_id=fallback_id)
    candidates = extract_explore_candidates(
        raw_asset=raw_asset,
        fallback_object=str(normalized.get("title") or fallback_id),
        readable_original_refs=list(normalized.get("original_refs") or []),
    )
    print(json.dumps(candidates, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
