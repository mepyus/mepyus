#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    local_space_dir = runtime_root / "core" / "local_spaces"
    updated = []
    for path in sorted(local_space_dir.glob("*.json")):
        payload = sync_local_space_anchor_metadata(runtime_root, path.stem)
        if payload:
            updated.append(payload)
    print(json.dumps({"runtime_root": str(runtime_root), "updated_count": len(updated), "updates": updated}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
