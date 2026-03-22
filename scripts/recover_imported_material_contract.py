#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.imported_material_contract import recover_imported_material_contract


def main(argv: list[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    source_refs = argv[2:] if len(argv) > 2 else None
    payload = recover_imported_material_contract(runtime_root, source_refs=source_refs)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
