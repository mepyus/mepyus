from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.atomic_io import atomic_write_json
from app.core.registry.provenance_hygiene import apply_bounded_compaction, build_compaction_preview, load_provenance_links


PROVENANCE_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_link_index_v1.json"
OUTPUT_ROOT = REPO_ROOT / "runtime" / "manifests" / "provenance_compaction"


def main() -> None:
    links = load_provenance_links(PROVENANCE_PATH)
    preview = build_compaction_preview(links)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    snapshot_path = OUTPUT_ROOT / "provenance_link_index_snapshot_before_apply_v1.json"
    atomic_write_json(snapshot_path, {"index_name": "provenance_link_index_snapshot_before_apply_v1", "links": links})
    result = apply_bounded_compaction(preview, PROVENANCE_PATH, OUTPUT_ROOT)
    summary = {
        "snapshot_path": str(snapshot_path.relative_to(REPO_ROOT)),
        "apply_summary_path": str((OUTPUT_ROOT / 'provenance_compaction_apply_latest.json').relative_to(REPO_ROOT)),
        "compacted_index_path": str((OUTPUT_ROOT / 'provenance_link_index_compacted_v1.json').relative_to(REPO_ROOT)),
        "raw_row_count": result["raw_row_count"],
        "compacted_row_count": result["compacted_row_count"],
        "compacted_group_count": len(result["compacted_groups"]),
        "raw_preserved": True,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
