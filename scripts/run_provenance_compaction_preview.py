from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.provenance_hygiene import build_compaction_preview, load_provenance_links, write_compaction_preview


PROVENANCE_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_link_index_v1.json"
PREVIEW_JSON_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_compaction" / "provenance_compaction_preview_latest.json"
PREVIEW_MD_PATH = REPO_ROOT / "runtime" / "views" / "provenance_compacted_latest.md"


def main() -> None:
    links = load_provenance_links(PROVENANCE_PATH)
    preview = build_compaction_preview(links)
    write_compaction_preview(preview, PREVIEW_JSON_PATH, PREVIEW_MD_PATH, PROVENANCE_PATH)
    summary = {
        "preview_manifest": str(PREVIEW_JSON_PATH.relative_to(REPO_ROOT)),
        "preview_surface": str(PREVIEW_MD_PATH.relative_to(REPO_ROOT)),
        "total_rows": preview["scan_summary"]["total_rows"],
        "safe_group_count": preview["candidate_summary"]["safe_group_count"],
        "manual_review_group_count": preview["candidate_summary"]["manual_review_group_count"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
