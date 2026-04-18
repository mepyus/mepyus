#!/usr/bin/env python3
from __future__ import annotations

import json
import re
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

OUTPUT_DIR = REPO_ROOT / "app" / "work" / "archive_review" / "probe_support" / "future_segment_probe" / "generated"

FUTURE_PATTERN = re.compile(
    r"미래|future|AGI|초지능|자동화|장기적 미래|미래의 AI|10년 후|20년 뒤|앞으로|미래 전망",
    re.IGNORECASE,
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        rel = path.resolve()
    return str(rel).replace("\\", "/")


def _matches_future(text: str, anchors: List[object]) -> bool:
    if FUTURE_PATTERN.search(text):
        return True
    for anchor in anchors:
        value = getattr(anchor, "value", "")
        if value and FUTURE_PATTERN.search(str(value)):
            return True
    return False


def _excerpt(text: str, limit: int = 160) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def _top(counter: Counter[str], limit: int = 8) -> List[Dict[str, object]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _default_inputs() -> List[Path]:
    root = REPO_ROOT / "inputs" / "external_cases"
    matched: List[Path] = []
    for path in sorted(root.glob("*")):
        if path.suffix.lower() not in {".txt", ".md"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if FUTURE_PATTERN.search(text):
            matched.append(path)
    return matched


def main(argv: List[str]) -> int:
    input_paths = [Path(arg).resolve() for arg in argv[1:]] if len(argv) > 1 else _default_inputs()
    if not input_paths:
        print("[]")
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    created_at = _now_iso()
    overall_scene: Counter[str] = Counter()
    overall_flow: Counter[str] = Counter()
    overall_anchor: Counter[str] = Counter()
    results: List[Dict[str, object]] = []

    for input_path in input_paths:
        raw_text = input_path.read_text(encoding="utf-8").strip()
        dust_inputs = build_dust_inputs_from_source(
            source_id=f"src_{uuid4().hex[:12]}",
            source_type="text",
            source_ref=f"{_relative(input_path)}#ai_future_segment_probe_v1",
            raw_payload=raw_text,
            created_at=created_at,
        )
        labeled = label_dust_inputs(dust_inputs)
        matched_units = [unit for unit in labeled if _matches_future(unit.text, list(unit.anchors))]
        if not matched_units:
            continue

        scene_counter: Counter[str] = Counter()
        flow_counter: Counter[str] = Counter()
        anchor_counter: Counter[str] = Counter()
        samples: List[Dict[str, object]] = []

        for unit in matched_units:
            scene_counter[unit.scene] += 1
            flow_counter[unit.flow] += 1
            overall_scene[unit.scene] += 1
            overall_flow[unit.flow] += 1
            for anchor in unit.anchors:
                anchor_counter[str(anchor.value)] += 1
                overall_anchor[str(anchor.value)] += 1
            if len(samples) < 6:
                samples.append(
                    {
                        "dust_id": unit.dust_id,
                        "scene": unit.scene,
                        "flow": unit.flow,
                        "short_label": unit.short_label,
                        "excerpt": _excerpt(unit.text),
                    }
                )

        results.append(
            {
                "input_path": _relative(input_path),
                "matched_segment_count": len(matched_units),
                "scene_counts": dict(scene_counter),
                "flow_counts": dict(flow_counter),
                "top_anchor_values": _top(anchor_counter),
                "sample_segments": samples,
            }
        )

    payload = {
        "probe_name": "ai_future_segment_probe_v1",
        "created_at": created_at,
        "matched_source_count": len(results),
        "overall_scene_counts": dict(overall_scene),
        "overall_flow_counts": dict(overall_flow),
        "overall_top_anchor_values": _top(overall_anchor, limit=12),
        "sources": sorted(results, key=lambda row: int(row["matched_segment_count"]), reverse=True),
    }

    output_path = OUTPUT_DIR / f"ai_future_segment_probe_{_stamp()}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output_path": _relative(output_path), "matched_source_count": len(results)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
