#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.post_preprocess_first_pass import preprocess_and_probe_first_pass


OUTPUT_DIR = REPO_ROOT / "app" / "work" / "external_input_preprocess" / "generated"


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        rel = path.resolve()
    return str(rel).replace("\\", "/")


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("usage: run_post_preprocess_first_pass_probe.py <input_path>", file=sys.stderr)
        return 1

    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = (REPO_ROOT / input_path).resolve()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sidecar_path = OUTPUT_DIR / f"{input_path.stem}_post_preprocess_first_pass_{_stamp()}.txt"
    result = preprocess_and_probe_first_pass(input_path, output_path=sidecar_path)
    report_path = OUTPUT_DIR / f"{input_path.stem}_post_preprocess_first_pass_probe.json"
    report_path.write_text(
        json.dumps(
            {
                "probe_name": "post_preprocess_first_pass_probe_v0",
                "generated_at": result.generated_at,
                "input_path": _relative(Path(result.input_path)),
                "preprocessed_path": _relative(Path(result.preprocessed_path)),
                "first_pass_read": result.first_pass_read,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "report_path": _relative(report_path),
                "preprocessed_path": _relative(sidecar_path),
                "dust_count": result.first_pass_read["dust_count"],
                "human_read_summary": result.first_pass_read["human_read_summary"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
