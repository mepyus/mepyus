#!/usr/bin/env python3
from __future__ import annotations

import argparse
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

OUTPUT_DIR = REPO_ROOT / "app" / "work" / "archive_review" / "probe_support" / "concept_segment_probe" / "generated"

SCENE_GLOSS = {
    "review": "설명/해석 층",
    "impl": "구현/실행 층",
    "evidence": "근거/검증 층",
    "spec": "규칙/형식 힌트 층",
}

FLOW_GLOSS = {
    "compare": "비교/해석 흐름",
    "run": "작동/실행 흐름",
    "break": "끊김/전환 흐름",
    "fix": "수정/보정 흐름",
}

GENERIC_DISCOURSE_TERMS = {
    "그래서", "우리가", "우리는", "있습니다", "겁니다", "그러니까", "사실", "사실은",
    "어떻게", "이렇게", "그리고", "하지만", "이제", "지금", "여기서", "그런데",
    "정말", "아주", "이미", "모든", "결국", "되는", "되죠", "거죠", "보면",
}

SPEAKER_OR_SOURCE_RESIDUE_TERMS = {
    "dario", "andrej", "alex", "karpathy", "karp", "amodei",
    "이경일", "김성현", "최승준", "솔트룩스", "팔란티어", "palantir",
    "claude", "anthropic",
}

USER_LAYER_HINTS = {
    "전망/방향": {"미래", "future", "agi", "초지능", "시대", "방향", "전망"},
    "구현/실행": {"구현", "실행", "deployment", "deploy", "run", "workflow", "자동화", "리트리버", "검색"},
    "근거/검증": {"검증", "verification", "evidence", "평가", "benchmark", "신뢰", "reliability"},
    "구조/연결": {"온톨로지", "ontology", "그래프", "graph", "연결", "노드", "엣지", "구조"},
    "통제/운영": {"control", "통제", "운영", "operator", "deployment", "보안", "security"},
    "문제/병목": {"문제", "한계", "constraint", "병목", "위험", "갭", "gap"},
    "사회/산업 변화": {"산업", "사회", "국가", "기업", "노동", "시장", "안보"},
}


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


def _excerpt(text: str, limit: int = 160) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def _top(counter: Counter[str], limit: int = 8) -> List[Dict[str, object]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _scene_gloss(scene_counts: Dict[str, int]) -> List[Dict[str, object]]:
    return [
        {"value": key, "display_label": SCENE_GLOSS.get(key, key), "count": value}
        for key, value in sorted(scene_counts.items(), key=lambda item: item[1], reverse=True)
    ]


def _flow_gloss(flow_counts: Dict[str, int]) -> List[Dict[str, object]]:
    return [
        {"value": key, "display_label": FLOW_GLOSS.get(key, key), "count": value}
        for key, value in sorted(flow_counts.items(), key=lambda item: item[1], reverse=True)
    ]


def _anchor_bucket(value: str) -> str:
    lowered = value.lower()
    if lowered in {term.lower() for term in GENERIC_DISCOURSE_TERMS} or value in GENERIC_DISCOURSE_TERMS:
        return "discourse_residue_anchor"
    if lowered in {term.lower() for term in SPEAKER_OR_SOURCE_RESIDUE_TERMS} or value in SPEAKER_OR_SOURCE_RESIDUE_TERMS:
        return "speaker_or_source_residue_anchor"
    for hint_terms in USER_LAYER_HINTS.values():
        if lowered in {term.lower() for term in hint_terms} or value in hint_terms:
            return "user_layer_hint_anchor"
    return "core_topic_anchor"


def _anchor_bucket_counts(counter: Counter[str]) -> Dict[str, int]:
    bucket_counter: Counter[str] = Counter()
    for value, count in counter.items():
        bucket_counter[_anchor_bucket(value)] += count
    return dict(bucket_counter)


def _user_layer_hints(counter: Counter[str], limit: int = 5) -> List[Dict[str, object]]:
    layer_counts: Counter[str] = Counter()
    for value, count in counter.items():
        lowered = value.lower()
        for layer, hint_terms in USER_LAYER_HINTS.items():
            if lowered in {term.lower() for term in hint_terms} or value in hint_terms:
                layer_counts[layer] += count
    return [{"layer": layer, "count": count} for layer, count in layer_counts.most_common(limit)]


def _overall_opening_summary(scene_counts: Dict[str, int], flow_counts: Dict[str, int], layer_hints: List[Dict[str, object]]) -> str:
    top_scene = max(scene_counts.items(), key=lambda item: item[1])[0] if scene_counts else None
    top_flow = max(flow_counts.items(), key=lambda item: item[1])[0] if flow_counts else None
    top_layers = ", ".join(row["layer"] for row in layer_hints[:3]) if layer_hints else "명확한 사용자 층위 힌트 없음"
    return f"{SCENE_GLOSS.get(top_scene, top_scene or 'unknown')} 중심, {FLOW_GLOSS.get(top_flow, top_flow or 'unknown')} 우세, 주요 사용자 층위 힌트: {top_layers}"


def _default_inputs(pattern: re.Pattern[str]) -> List[Path]:
    root = REPO_ROOT / "inputs" / "external_cases"
    matched: List[Path] = []
    for path in sorted(root.glob("*")):
        if path.suffix.lower() not in {".txt", ".md"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if pattern.search(text):
            matched.append(path)
    return matched


def _matches(text: str, anchors: List[object], pattern: re.Pattern[str]) -> bool:
    if pattern.search(text):
        return True
    for anchor in anchors:
        value = getattr(anchor, "value", "")
        if value and pattern.search(str(value)):
            return True
    return False


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--pattern", required=True)
    parser.add_argument("inputs", nargs="*")
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    pattern = re.compile(args.pattern, re.IGNORECASE)
    input_paths = [Path(arg).resolve() for arg in args.inputs] if args.inputs else _default_inputs(pattern)
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
            source_ref=f"{_relative(input_path)}#{args.label}",
            raw_payload=raw_text,
            created_at=created_at,
        )
        labeled = label_dust_inputs(dust_inputs)
        matched_units = [unit for unit in labeled if _matches(unit.text, list(unit.anchors), pattern)]
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
                "scene_display_counts": _scene_gloss(dict(scene_counter)),
                "flow_counts": dict(flow_counter),
                "flow_display_counts": _flow_gloss(dict(flow_counter)),
                "top_anchor_values": _top(anchor_counter),
                "anchor_bucket_counts": _anchor_bucket_counts(anchor_counter),
                "user_layer_hints": _user_layer_hints(anchor_counter),
                "opening_summary": _overall_opening_summary(dict(scene_counter), dict(flow_counter), _user_layer_hints(anchor_counter)),
                "sample_segments": samples,
            }
        )

    payload = {
        "probe_name": args.label,
        "created_at": created_at,
        "pattern": args.pattern,
        "matched_source_count": len(results),
        "overall_scene_counts": dict(overall_scene),
        "overall_scene_display_counts": _scene_gloss(dict(overall_scene)),
        "overall_flow_counts": dict(overall_flow),
        "overall_flow_display_counts": _flow_gloss(dict(overall_flow)),
        "overall_top_anchor_values": _top(overall_anchor, limit=12),
        "overall_anchor_bucket_counts": _anchor_bucket_counts(overall_anchor),
        "overall_user_layer_hints": _user_layer_hints(overall_anchor),
        "overall_opening_summary": _overall_opening_summary(dict(overall_scene), dict(overall_flow), _user_layer_hints(overall_anchor)),
        "sources": sorted(results, key=lambda row: int(row["matched_segment_count"]), reverse=True),
    }

    output_path = OUTPUT_DIR / f"{args.label}_{_stamp()}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output_path": _relative(output_path), "matched_source_count": len(results)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
