#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.external_input_gate import assess_external_input_gate


def _usage() -> int:
    print("usage: run_external_input_gate.py <input_a> [<input_b> ...]", file=sys.stderr)
    return 1


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        return _usage()

    rows = []
    for raw_path in argv[1:]:
        input_path = Path(raw_path)
        if not input_path.is_absolute():
            input_path = (REPO_ROOT / input_path).resolve()
        rows.append(assess_external_input_gate(input_path))

    print(
        json.dumps(
            {
                "gate_name": "external_input_gate_v0",
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
