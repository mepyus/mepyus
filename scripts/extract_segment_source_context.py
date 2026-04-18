from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.operating_ui_live import build_operating_ui_live_composition_data
from app.runtime.runtime_preflight import build_runtime_preflight
from app.runtime.segment_to_source_context_extractor import extract_segment_source_context


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    asset_id = sys.argv[2] if len(sys.argv) > 2 else None
    state_row_key = sys.argv[3] if len(sys.argv) > 3 else "packet_texture"

    live = build_operating_ui_live_composition_data(runtime_root, asset_id=asset_id)
    resolved_asset_id = str(live.get("selected_asset_id") or asset_id or "")
    build_runtime_preflight(
        runtime_root,
        requested_mode="space_reading",
        requested_artifact_ref=resolved_asset_id or asset_id,
        page_key="operating",
    )
    raw_asset = ((live.get("adapted_model") or {}).get("selectedAsset") or {}) if live.get("state") == "loaded" else {}
    source_file = None
    for ref in raw_asset.get("evidenceRefs") or []:
        if isinstance(ref, dict) and ref.get("kind") == "source_file":
            source_file = str(ref.get("id") or "").strip()
            break
    if not source_file:
        raise SystemExit("no source_file evidenceRef found")

    payload = extract_segment_source_context(
        asset_id=resolved_asset_id,
        state_row_key=state_row_key,
        source_pointer=source_file,
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
