#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from uuid import uuid4

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs


def _usage() -> int:
    print(
        "usage: run_external_case_raw_intake_probe.py <input_a> <input_b> [<input_c> ...]",
        file=sys.stderr,
    )
    return 1


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _relative_ref(path: Path) -> str:
    try:
        rel = path.relative_to(REPO_ROOT)
    except ValueError:
        rel = path
    return str(rel).replace("\\", "/")


def _top_values(counter: Counter[str], limit: int = 10) -> List[Dict[str, object]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        return _usage()

    created_at = _now_iso()
    payload: Dict[str, object] = {
        "probe_name": "external_case_raw_intake_probe_20260328",
        "created_at": created_at,
        "inputs": [],
    }

    for raw_path in argv[1:]:
        input_path = Path(raw_path).resolve()
        raw_text = input_path.read_text(encoding="utf-8").strip()
        source_ref = f"{_relative_ref(input_path)}#raw_intake_probe_v1"
        source_id = f"src_{uuid4().hex[:12]}"

        dust_inputs = build_dust_inputs_from_source(
            source_id=source_id,
            source_type="text",
            source_ref=source_ref,
            raw_payload=raw_text,
            created_at=created_at,
        )
        labeled = label_dust_inputs(dust_inputs)

        scene_counter: Counter[str] = Counter()
        flow_counter: Counter[str] = Counter()
        anchor_counter: Counter[str] = Counter()
        labels: List[str] = []
        d_values: List[float] = []
        i_values: List[float] = []
        s_values: List[float] = []

        for unit in labeled:
            scene_counter[unit.scene] += 1
            flow_counter[unit.flow] += 1
            labels.append(unit.short_label)
            d_values.append(unit.D)
            i_values.append(unit.I)
            s_values.append(unit.S)
            for anchor in unit.anchors:
                anchor_counter[f"{anchor.type}:{anchor.value}"] += 1

        count = max(1, len(labeled))
        payload["inputs"].append(
            {
                "input_path": _relative_ref(input_path),
                "source_ref": source_ref,
                "dust_count": len(labeled),
                "scene_counts": dict(scene_counter),
                "flow_counts": dict(flow_counter),
                "avg_D": round(sum(d_values) / count, 3),
                "avg_I": round(sum(i_values) / count, 3),
                "avg_S": round(sum(s_values) / count, 3),
                "sample_short_labels": labels[:10],
                "top_anchor_values": _top_values(anchor_counter),
            }
        )

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
