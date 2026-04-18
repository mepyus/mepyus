from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.provenance_hygiene import build_compaction_preview, load_provenance_links


PROVENANCE_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_link_index_v1.json"


def main() -> None:
    links = load_provenance_links(PROVENANCE_PATH)
    preview = build_compaction_preview(links)
    summary = {
        "source_path": str(PROVENANCE_PATH.relative_to(REPO_ROOT)),
        "total_rows": preview["scan_summary"]["total_rows"],
        "safe_group_count": preview["candidate_summary"]["safe_group_count"],
        "manual_review_group_count": preview["candidate_summary"]["manual_review_group_count"],
        "safe_candidate_rows": preview["candidate_summary"]["safe_candidate_rows"],
        "manual_review_candidate_rows": preview["candidate_summary"]["manual_review_candidate_rows"],
        "top_classifications": preview["candidate_summary"]["classification_counts"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
