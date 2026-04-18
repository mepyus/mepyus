#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence
from uuid import uuid4

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs

OUTPUT_DIR = REPO_ROOT / "app" / "work" / "dialogue_loop_test" / "generated"

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

OBJECT_KEYWORDS: Dict[str, Sequence[str]] = {
    "AI의 미래": ("ai의 미래", "미래", "future", "발전상", "capability", "overhang", "모델 world"),
    "일의 미래": ("일의 미래", "노동", "직무", "감독관", "회장님", "일하게", "생산성"),
    "생산성/코딩": ("생산성", "코딩", "coding", "claude code", "codex", "프롬프트", "connector"),
    "에이전트 애플리케이션": ("에이전트", "agent", "openclaw", "omo.bot", "assistant", "앱", "cua"),
    "모델 work": ("모델", "model", "pre-train", "rlvr", "reward", "evaluation", "search problem"),
    "구현/자동화": ("자동화", "automation", "하네스", "harness", "workflow", "loop", "meta"),
    "전략/방향성": ("전략", "strategy", "비즈니스", "business", "ax", "moat", "bundle", "unbundle"),
}

LAYER_HINT_TERMS: Dict[str, Sequence[str]] = {
    "설명/해석 층": ("의미", "해석", "관점", "인사이트", "설명", "정리"),
    "구현/실행 층": ("실행", "구현", "자동화", "workflow", "deploy", "run", "harness"),
    "구조/연결 층": ("구조", "연결", "레이어", "relationship", "bundle", "unbundle", "framework"),
    "전략/방향 층": ("미래", "방향", "전략", "사업", "비즈니스", "moat", "적응"),
    "검증/근거 층": ("검증", "evidence", "evaluation", "metric", "reward", "보상"),
    "질문 유도 층": ("왜", "어떻게", "무엇", "궁금", "질문", "?"),
}

RELATION_HINT_TERMS: Dict[str, Sequence[str]] = {
    "reinforcement_hint": ("그래서", "결국", "즉", "또", "더", "그러면서"),
    "contrast_hint": ("하지만", "반면", "근데", "그러나", "아니지만"),
    "transition_hint": ("이제", "넘어가", "그러면", "다음", "정리하면"),
    "execution_shift_hint": ("실행", "돌리", "운영", "workflow", "자동화", "deploy", "에이전트"),
    "specification_hint": ("objective", "evaluation", "metric", "spec", "스펙", "목표", "기준"),
    "question_generation_hint": ("왜", "어떻게", "무엇", "궁금", "?"),
}

QUESTION_INTENT_TERMS = (
    "미래", "future", "일", "노동", "생산성", "에이전트", "앱", "openclaw", "사업", "비즈니스",
    "전략", "방향", "검증", "보안", "ax", "automation", "모델", "work",
)

DISCOURSE_CONNECTIVE_RESIDUE = {
    "그래서", "그러니까", "그리고", "하지만", "근데", "그러면", "이제", "사실", "어쨌든",
}
SPEAKER_RESIDUE = {
    "노정석", "최승준", "정석님", "승준님", "Jensen", "Sam", "Benedict", "Andrej",
}
CONVERSATIONAL_FILLER_RESIDUE = {
    "뭐", "약간", "되게", "이런", "저희가", "그냥", "진짜", "사실은", "거죠",
}
GENERIC_ABSTRACTION_RESIDUE = {
    "방향", "변화", "문제", "구조", "부분", "세상", "이야기", "관점", "의미",
}
QUASI_TOPIC_RESIDUE = {
    "모델", "사업", "회사", "세상", "구조", "전략",
}

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_.+-]{1,}|[가-힣]{2,}")
TIMESTAMP_RE = re.compile(r"^\d{1,2}:\d{2}$")


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


def _excerpt(text: str, limit: int = 180) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def _contains_term(text: str, terms: Sequence[str]) -> int:
    lowered = text.lower()
    hits = 0
    for term in terms:
        if term.lower() in lowered:
            hits += 1
    return hits


def _is_assist_heading(lines: Sequence[str], index: int) -> bool:
    line = lines[index].strip()
    if not line or TIMESTAMP_RE.match(line):
        return False
    if index + 1 >= len(lines) or not TIMESTAMP_RE.match(lines[index + 1].strip()):
        return False
    # Keep this narrow: short title-like lines before timestamps become headings.
    if len(line) > 48:
        return False
    if any(token in line for token in (".", "?", "!", "다.", "요.", "죠.", "니다.")):
        return False
    return True


def _split_blocks(text: str, segment_assist: str = "none") -> List[Dict[str, str]]:
    blocks: List[Dict[str, str]] = []
    heading = "untitled"
    paragraph_lines: List[str] = []
    lines = text.splitlines()
    for index, raw_line in enumerate(lines):
        line = raw_line.rstrip()
        if line.startswith("## "):
            if paragraph_lines:
                paragraph = "\n".join(paragraph_lines).strip()
                if paragraph:
                    blocks.append({"heading": heading, "text": paragraph})
                paragraph_lines = []
            heading = line[3:].strip() or heading
            continue
        if segment_assist == "index_support" and _is_assist_heading(lines, index):
            if paragraph_lines:
                paragraph = "\n".join(paragraph_lines).strip()
                if paragraph:
                    blocks.append({"heading": heading, "text": paragraph})
                paragraph_lines = []
            heading = line.strip() or heading
            continue
        if segment_assist == "index_support" and TIMESTAMP_RE.match(line.strip()):
            if paragraph_lines:
                paragraph = "\n".join(paragraph_lines).strip()
                if paragraph:
                    blocks.append({"heading": heading, "text": paragraph})
                paragraph_lines = []
            continue
        if not line.strip():
            if paragraph_lines:
                paragraph = "\n".join(paragraph_lines).strip()
                if paragraph:
                    blocks.append({"heading": heading, "text": paragraph})
                paragraph_lines = []
            continue
        paragraph_lines.append(line)
    if paragraph_lines:
        paragraph = "\n".join(paragraph_lines).strip()
        if paragraph:
            blocks.append({"heading": heading, "text": paragraph})
    return blocks


def _windowed(blocks: Sequence[Dict[str, str]], size: int, stride: int) -> List[Dict[str, object]]:
    windows: List[Dict[str, object]] = []
    if not blocks:
        return windows
    index = 0
    while index < len(blocks):
        chunk = list(blocks[index:index + size])
        if not chunk:
            break
        windows.append(
            {
                "start_index": index,
                "end_index": index + len(chunk) - 1,
                "headings": [row["heading"] for row in chunk],
                "blocks": chunk,
                "text": "\n\n".join(f"## {row['heading']}\n{row['text']}" for row in chunk),
            }
        )
        if index + size >= len(blocks):
            break
        index += stride
    return windows


def _top(counter: Counter[str], limit: int = 8, key_name: str = "value") -> List[Dict[str, object]]:
    return [{key_name: value, "count": count} for value, count in counter.most_common(limit)]


def _anchor_bucket(value: str) -> str:
    lowered = value.lower()
    if value in DISCOURSE_CONNECTIVE_RESIDUE or lowered in {row.lower() for row in DISCOURSE_CONNECTIVE_RESIDUE}:
        return "discourse_residue_anchor"
    if value in SPEAKER_RESIDUE or lowered in {row.lower() for row in SPEAKER_RESIDUE}:
        return "speaker_or_source_residue_anchor"
    for terms in OBJECT_KEYWORDS.values():
        if any(term.lower() == lowered for term in terms):
            return "user_layer_hint_anchor"
    return "core_topic_anchor"


def _bucket_counts(counter: Counter[str]) -> Dict[str, int]:
    buckets: Counter[str] = Counter()
    for value, count in counter.items():
        buckets[_anchor_bucket(value)] += count
    return dict(buckets)


def _layer_hints(text: str, scene_counter: Counter[str], flow_counter: Counter[str]) -> List[Dict[str, object]]:
    layer_counter: Counter[str] = Counter()
    for layer, terms in LAYER_HINT_TERMS.items():
        hits = _contains_term(text, terms)
        if hits:
            layer_counter[layer] += hits
    if scene_counter.get("review"):
        layer_counter["설명/해석 층"] += scene_counter["review"]
    if scene_counter.get("impl") or flow_counter.get("run"):
        layer_counter["구현/실행 층"] += scene_counter.get("impl", 0) + flow_counter.get("run", 0)
    if scene_counter.get("evidence"):
        layer_counter["검증/근거 층"] += scene_counter["evidence"]
    if scene_counter.get("spec"):
        layer_counter["구조/연결 층"] += scene_counter["spec"]
    return [{"layer": layer, "count": count} for layer, count in layer_counter.most_common()]


def _relation_hints(text: str) -> List[str]:
    hints: List[str] = []
    for hint, terms in RELATION_HINT_TERMS.items():
        if _contains_term(text, terms):
            hints.append(hint)
    return hints


def _question_intent_score(text: str) -> int:
    return _contains_term(text, QUESTION_INTENT_TERMS)


def _object_candidates(text: str) -> List[Dict[str, object]]:
    counter: Counter[str] = Counter()
    for name, terms in OBJECT_KEYWORDS.items():
        hits = _contains_term(text, terms)
        if hits:
            counter[name] += hits
    return [{"object": name, "count": count} for name, count in counter.most_common()]


def _residue_breakdown(text: str, anchor_counter: Counter[str]) -> Dict[str, int]:
    lowered_text = text.lower()
    return {
        "discourse_connective_residue": sum(1 for term in DISCOURSE_CONNECTIVE_RESIDUE if term.lower() in lowered_text),
        "speaker_or_source_residue": sum(1 for term in SPEAKER_RESIDUE if term.lower() in lowered_text),
        "conversational_filler_residue": sum(1 for term in CONVERSATIONAL_FILLER_RESIDUE if term.lower() in lowered_text),
        "generic_abstraction_residue": sum(1 for term in GENERIC_ABSTRACTION_RESIDUE if term.lower() in lowered_text),
        "quasi_topic_residue": sum(1 for term in QUASI_TOPIC_RESIDUE if term.lower() in lowered_text and anchor_counter[term] > 0),
    }


def _open_summary(object_candidates: List[Dict[str, object]], layer_hints: List[Dict[str, object]], relation_hints: List[str]) -> str:
    object_part = ", ".join(row["object"] for row in object_candidates[:3]) if object_candidates else "명확한 객체 후보 없음"
    layer_part = ", ".join(row["layer"] for row in layer_hints[:3]) if layer_hints else "명확한 층위 힌트 약함"
    relation_part = ", ".join(relation_hints[:3]) if relation_hints else "관계 운동 힌트 약함"
    return f"주요 객체 후보: {object_part} / 주요 층위: {layer_part} / 관계 힌트: {relation_part}"


def _probe_window(window: Dict[str, object], label: str, created_at: str) -> Dict[str, object]:
    text = str(window["text"])
    dust_inputs = build_dust_inputs_from_source(
        source_id=f"src_{uuid4().hex[:12]}",
        source_type="text",
        source_ref=f"{label}#{window['start_index']}_{window['end_index']}",
        raw_payload=text,
        created_at=created_at,
    )
    labeled = label_dust_inputs(dust_inputs)

    scene_counter: Counter[str] = Counter()
    flow_counter: Counter[str] = Counter()
    anchor_counter: Counter[str] = Counter()
    sample_segments: List[Dict[str, object]] = []

    for unit in labeled:
        scene_counter[unit.scene] += 1
        flow_counter[unit.flow] += 1
        for anchor in unit.anchors:
            anchor_counter[str(anchor.value)] += 1
        if len(sample_segments) < 4:
            sample_segments.append(
                {
                    "dust_id": unit.dust_id,
                    "scene": unit.scene,
                    "flow": unit.flow,
                    "short_label": unit.short_label,
                    "excerpt": _excerpt(unit.text),
                }
            )

    object_candidates = _object_candidates(text)
    layer_hints = _layer_hints(text, scene_counter, flow_counter)
    relation_hints = _relation_hints(text)
    question_score = _question_intent_score(text)
    residue_breakdown = _residue_breakdown(text, anchor_counter)
    residue_total = sum(residue_breakdown.values())

    return {
        "window_id": f"{window['start_index']}_{window['end_index']}",
        "start_index": window["start_index"],
        "end_index": window["end_index"],
        "headings": list(window["headings"]),
        "scene_counts": dict(scene_counter),
        "scene_display_counts": [{"value": key, "display_label": SCENE_GLOSS.get(key, key), "count": value} for key, value in scene_counter.most_common()],
        "flow_counts": dict(flow_counter),
        "flow_display_counts": [{"value": key, "display_label": FLOW_GLOSS.get(key, key), "count": value} for key, value in flow_counter.most_common()],
        "object_candidates": object_candidates,
        "layer_hints": layer_hints,
        "relation_hints": relation_hints,
        "question_intent_score": question_score,
        "top_anchor_values": _top(anchor_counter, limit=10),
        "anchor_bucket_counts": _bucket_counts(anchor_counter),
        "residue_breakdown": residue_breakdown,
        "residue_total": residue_total,
        "opening_summary": _open_summary(object_candidates, layer_hints, relation_hints),
        "sample_blocks": [{"heading": row["heading"], "excerpt": _excerpt(row["text"])} for row in list(window["blocks"])[:3]],
        "sample_segments": sample_segments,
    }


def _parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--window-size", required=True, type=int)
    parser.add_argument("--stride", required=True, type=int)
    parser.add_argument("--segment-assist", choices=["none", "index_support"], default="none")
    return parser.parse_args(argv[1:])


def main(argv: List[str]) -> int:
    args = _parse_args(argv)
    input_path = Path(args.input).resolve()
    text = input_path.read_text(encoding="utf-8")
    blocks = _split_blocks(text, segment_assist=args.segment_assist)
    windows = _windowed(blocks, args.window_size, args.stride)
    created_at = _now_iso()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    overall_scene: Counter[str] = Counter()
    overall_flow: Counter[str] = Counter()
    overall_anchor: Counter[str] = Counter()
    overall_objects: Counter[str] = Counter()
    overall_layers: Counter[str] = Counter()
    overall_relations: Counter[str] = Counter()
    overall_residue: Counter[str] = Counter()
    rows: List[Dict[str, object]] = []

    for window in windows:
        row = _probe_window(window, args.label, created_at)
        rows.append(row)
        for key, count in row["scene_counts"].items():
            overall_scene[key] += count
        for key, count in row["flow_counts"].items():
            overall_flow[key] += count
        for item in row["top_anchor_values"]:
            overall_anchor[str(item["value"])] += int(item["count"])
        for item in row["object_candidates"]:
            overall_objects[str(item["object"])] += int(item["count"])
        for item in row["layer_hints"]:
            overall_layers[str(item["layer"])] += int(item["count"])
        for hint in row["relation_hints"]:
            overall_relations[hint] += 1
        for name, count in row["residue_breakdown"].items():
            overall_residue[name] += count

    top_question_windows = sorted(rows, key=lambda row: (int(row["question_intent_score"]), sum(item["count"] for item in row["object_candidates"])), reverse=True)[:5]
    top_residue_windows = sorted(rows, key=lambda row: int(row["residue_total"]), reverse=True)[:5]

    payload = {
        "probe_name": args.label,
        "input_path": _relative(input_path),
        "created_at": created_at,
        "window_size": args.window_size,
        "stride": args.stride,
        "segment_assist": args.segment_assist,
        "block_count": len(blocks),
        "window_count": len(windows),
        "overall_scene_counts": dict(overall_scene),
        "overall_scene_display_counts": [{"value": key, "display_label": SCENE_GLOSS.get(key, key), "count": value} for key, value in overall_scene.most_common()],
        "overall_flow_counts": dict(overall_flow),
        "overall_flow_display_counts": [{"value": key, "display_label": FLOW_GLOSS.get(key, key), "count": value} for key, value in overall_flow.most_common()],
        "overall_object_candidates": _top(overall_objects, limit=10, key_name="object"),
        "overall_layer_hints": _top(overall_layers, limit=10, key_name="layer"),
        "overall_relation_hints": _top(overall_relations, limit=10, key_name="hint"),
        "overall_anchor_bucket_counts": _bucket_counts(overall_anchor),
        "overall_top_anchor_values": _top(overall_anchor, limit=12),
        "overall_residue_breakdown": dict(overall_residue),
        "top_question_intent_windows": top_question_windows,
        "top_residue_windows": top_residue_windows,
        "windows": rows,
    }

    output_path = OUTPUT_DIR / f"{args.label}_w{args.window_size}_s{args.stride}_{_stamp()}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output_path": _relative(output_path), "window_count": len(windows)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
