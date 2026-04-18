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

from app.core.runtime.external_input_gate import assess_external_input_gate
from app.core.runtime.external_transcript_preprocess import preprocess_transcript_file


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
        print("usage: run_transcript_aware_regroup.py <input_path>", file=sys.stderr)
        return 1

    input_path = Path(argv[1])
    if not input_path.is_absolute():
        input_path = (REPO_ROOT / input_path).resolve()

    before = assess_external_input_gate(input_path)
    preprocess = preprocess_transcript_file(input_path)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = input_path.stem
    stamp = _stamp()
    preprocessed_path = OUTPUT_DIR / f"{stem}_transcript_regroup_{stamp}.txt"
    preprocessed_path.write_text(preprocess.normalized_text, encoding="utf-8")
    after = assess_external_input_gate(preprocessed_path)

    payload = {
        "runner": "transcript_aware_regroup_v0",
        "input_path": _relative(input_path),
        "preprocessed_path": _relative(preprocessed_path),
        "before_gate": before,
        "after_gate": after,
        "preprocess_summary": {
            "original_line_count": preprocess.original_line_count,
            "normalized_sentence_count": preprocess.normalized_sentence_count,
            "regrouped_chunk_count": preprocess.regrouped_chunk_count,
            "dropped_interjection_count": preprocess.dropped_interjection_count,
            "sample_chunks": preprocess.regrouped_chunks[:5],
        },
        "checkpoints": preprocess.checkpoints,
    }

    report_path = OUTPUT_DIR / f"{stem}_transcript_regroup_{stamp}.json"
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "preprocessed_path": _relative(preprocessed_path),
                "report_path": _relative(report_path),
                "before_decision": before["decision"],
                "after_decision": after["decision"],
                "regrouped_chunk_count": preprocess.regrouped_chunk_count,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
