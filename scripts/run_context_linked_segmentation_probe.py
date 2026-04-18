#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.context_linked_segmentation import ContextLinkedSegmenter, Segment


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a small context-linked segmentation probe.")
    parser.add_argument(
        "--output-root",
        default="/tmp/context_linked_segmentation_probe",
        help="Temporary sandbox output directory.",
    )
    return parser.parse_args()


def _fixture_segments() -> list[Segment]:
    return [
        Segment(
            segment_id="seg_001",
            source_id="probe_doc",
            text="이 시스템의 핵심은 읽기 관측을 누적하는 것이고,",
            order_index=0,
            start_anchor={"paragraph": 1, "offset": 0},
            end_anchor={"paragraph": 1, "offset": 27},
            provenance={"fixture": "probe"},
            speaker_id="speaker_a",
        ),
        Segment(
            segment_id="seg_002",
            source_id="probe_doc",
            text="그 결과 line은 미리 정의된 개념이 아니라 뒤에서 떠오른다.",
            order_index=1,
            start_anchor={"paragraph": 1, "offset": 28},
            end_anchor={"paragraph": 1, "offset": 63},
            provenance={"fixture": "probe"},
            speaker_id="speaker_a",
        ),
        Segment(
            segment_id="seg_003",
            source_id="probe_doc",
            text="왜 segmentation을 다시 묶어야 하는가?",
            order_index=2,
            start_anchor={"paragraph": 2, "offset": 0},
            end_anchor={"paragraph": 2, "offset": 24},
            provenance={"fixture": "probe"},
            speaker_id="speaker_b",
        ),
        Segment(
            segment_id="seg_004",
            source_id="probe_doc",
            text="혼자 두면 의미가 약한 조각이 앞뒤 문맥과 함께 살아나기 때문이다.",
            order_index=3,
            start_anchor={"paragraph": 2, "offset": 25},
            end_anchor={"paragraph": 2, "offset": 66},
            provenance={"fixture": "probe"},
            speaker_id="speaker_b",
        ),
        Segment(
            segment_id="seg_005",
            source_id="probe_doc",
            text="하지만 너무 멀리 있는 조각을 억지로 묶으면 overread가 생긴다.",
            order_index=4,
            start_anchor={"paragraph": 3, "offset": 0},
            end_anchor={"paragraph": 3, "offset": 39},
            provenance={"fixture": "probe"},
            speaker_id="speaker_c",
        ),
    ]


def main() -> int:
    args = _parse_args()
    output_root = Path(args.output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    segmenter = ContextLinkedSegmenter()
    linked = segmenter.link(_fixture_segments())
    payload = {
        "output_root": str(output_root),
        "linked_segment_count": len(linked),
        "linked_segments": [asdict(item) for item in linked],
    }
    (output_root / "linked_segments.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
