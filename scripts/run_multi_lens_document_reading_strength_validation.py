#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.runtime.context_linked_segmentation import ContextLinkedSegmenter
from app.core.runtime.multi_lens_document_reading import MultiLensDocumentReader
from scripts.run_context_linked_segmentation_validation import _fixtures


def main() -> int:
    output_root = Path("/tmp/multi_lens_document_reading_strength_validation")
    output_root.mkdir(parents=True, exist_ok=True)

    registry_path = ROOT / "runtime/manifests/line_registry.json"
    segmenter = ContextLinkedSegmenter()
    reader = MultiLensDocumentReader(str(registry_path))

    fixture_results = []
    overall_distribution = Counter()
    stable_lens_distribution = Counter()
    secondary_lens = [
        {
            "line_id": line.line_id,
            "line_name": line.line_name,
            "status": line.status,
            "thickness_level": line.thickness_level,
            "operating_state": line.operating_state,
        }
        for line in reader.secondary_line_definitions
    ]

    for fixture in _fixtures():
        linked_segments = segmenter.link(fixture.segments)
        result = reader.read(linked_segments)
        surfaced = reader.surface_readout(result)
        strength_by_lens: dict[str, list[str]] = defaultdict(list)
        for reading in result.readings:
            strength_by_lens[reading.line_id].append(reading.reading_strength)
            overall_distribution.update([reading.reading_strength])
            stable_lens_distribution.update([reading.reading_strength])

        fixture_results.append(
            {
                "fixture_name": fixture.fixture_name,
                "linked_segment_count": len(linked_segments),
                "lens_ids_used": result.lens_ids_used,
                "is_stable_lens_only": result.is_stable_lens_only,
                "line_states": surfaced.line_states,
                "strength_by_lens": dict(strength_by_lens),
                "readings": [asdict(item) for item in result.readings],
                "surfaced_readout": [asdict(item) for item in surfaced.readings],
            }
        )

    payload = {
        "registry_path": str(registry_path),
        "primary_lens_ids": [line.line_id for line in reader.primary_line_definitions],
        "secondary_lens_metadata": secondary_lens,
        "overall_strength_distribution": dict(overall_distribution),
        "stable_lens_strength_distribution": dict(stable_lens_distribution),
        "fixture_results": fixture_results,
    }
    (output_root / "validation_result.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
