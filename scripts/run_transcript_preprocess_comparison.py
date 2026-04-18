#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.external_input_comparison import build_transcript_preprocess_comparison


OUTPUT_DIR = REPO_ROOT / "app" / "work" / "external_input_preprocess" / "generated"


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("usage: run_transcript_preprocess_comparison.py <input_path>", file=sys.stderr)
        return 1

    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = (REPO_ROOT / input_path).resolve()

    payload = build_transcript_preprocess_comparison(input_path)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_DIR / f"{input_path.stem}_transcript_preprocess_comparison.json"
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "report_path": str(report_path.relative_to(REPO_ROOT)).replace("\\", "/"),
                "before_decision": payload["before_gate"]["decision"],
                "after_decision": payload["after_gate"]["decision"],
                "readiness_status": payload["comparison"]["readiness_read"]["status"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
