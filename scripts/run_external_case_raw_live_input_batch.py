#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input import ingest_live_input


def _usage() -> int:
    print(
        "usage: run_external_case_raw_live_input_batch.py <runtime_root> <input_a> <input_b> [<input_c> ...]",
        file=sys.stderr,
    )
    return 1


def _relative_ref(path: Path) -> str:
    try:
        rel = path.relative_to(REPO_ROOT)
    except ValueError:
        rel = path
    return str(rel).replace("\\", "/")


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _top_anchor_values(material_rows: List[Dict[str, object]], limit: int = 8) -> List[Dict[str, object]]:
    counter: Counter[str] = Counter()
    for row in material_rows:
        metadata = dict(row.get("metadata", {}))
        for anchor in metadata.get("anchors", []):
            value = str(anchor.get("value", "")).strip()
            if value:
                counter[value] += 1
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _summarize_materials(material_rows: List[Dict[str, object]]) -> Dict[str, object]:
    scene_counter: Counter[str] = Counter()
    flow_counter: Counter[str] = Counter()
    d_values: List[float] = []
    i_values: List[float] = []
    s_values: List[float] = []
    labels: List[str] = []

    for row in material_rows:
        metadata = dict(row.get("metadata", {}))
        scene_counter[str(metadata.get("scene", "unknown"))] += 1
        flow_counter[str(metadata.get("flow", "unknown"))] += 1
        d_values.append(_safe_float(metadata.get("D"), 0.0))
        i_values.append(_safe_float(metadata.get("I"), 0.0))
        s_values.append(_safe_float(metadata.get("S"), 0.0))
        label = str(metadata.get("short_label", "")).strip()
        if label:
            labels.append(label)

    count = max(1, len(material_rows))
    return {
        "scene_counts": dict(scene_counter),
        "flow_counts": dict(flow_counter),
        "avg_D": round(sum(d_values) / count, 3),
        "avg_I": round(sum(i_values) / count, 3),
        "avg_S": round(sum(s_values) / count, 3),
        "top_anchor_values": _top_anchor_values(material_rows),
        "sample_short_labels": labels[:8],
    }


def main(argv: List[str]) -> int:
    if len(argv) < 4:
        return _usage()

    runtime_root = Path(argv[1]).resolve()
    input_paths = [Path(arg).resolve() for arg in argv[2:]]

    service = FormationService(runtime_root)
    batch_rows: List[Dict[str, object]] = []

    for input_path in input_paths:
        raw_payload = input_path.read_text(encoding="utf-8").strip()
        if not raw_payload:
            batch_rows.append(
                {
                    "input_path": _relative_ref(input_path),
                    "status": "empty",
                }
            )
            continue

        source_ref = f"{_relative_ref(input_path)}#raw_live_input_v1"
        stem = input_path.stem
        ingest_result = ingest_live_input(
            runtime_root,
            {
                "raw_payload": raw_payload,
                "source_type": "text",
                "source_ref": source_ref,
                "session_id": "external-case-raw-live-input-batch-20260328",
                "actor_id": "codex_raw_input_probe",
                "family_id": f"raw_live_input_{stem}",
            },
        )

        material_rows = []
        for material_id in ingest_result.get("material_ids", []):
            record = service.materials.get(str(material_id)) or {}
            if record:
                material_rows.append(record)

        batch_rows.append(
            {
                "input_path": _relative_ref(input_path),
                "source_ref": source_ref,
                "status": "ok",
                "ingest_result": ingest_result,
                "material_summary": _summarize_materials(material_rows),
            }
        )

    payload = {
        "runtime_root": str(runtime_root),
        "batch_name": "external_case_raw_live_input_batch_20260328",
        "inputs": batch_rows,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
