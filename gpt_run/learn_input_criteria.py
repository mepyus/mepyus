#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
learn_input_criteria.py

목적:
- 대화 txt에서 입력기 기준 후보를 추출한다.
- 아직 ML 학습기가 아니라 '기준 추출기(seed builder)'다.

입력:
- raw chat txt
- 사용자 시작 마커: []
- assistant 시작 마커: [[A]]

출력:
- candidates.jsonl
- summary.json
- criteria_seed.md
- accepted_seed.jsonl
- review_queue.jsonl

분류 정책:
- hard_criteria      -> accepted_seed.jsonl
- soft_criteria      -> review_queue.jsonl
- material_candidate -> review_queue.jsonl
- uncertain          -> review_queue.jsonl
- archive_only       -> 원본 보존만, seed/review에서는 제외

실행 예시:
python3 learn_input_criteria.py --input ./a.txt --output-dir ./criteria_out_v4
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from typing import List, Optional, Tuple


USER_MARKER_RE = re.compile(r"^\s*\[\](.*)$")
ASSISTANT_MARKER_RE = re.compile(r"^\s*\[\[A\]\](.*)$")


NOISE_PATTERNS = [
    r"^[ㅋㅎ]{2,}$",
    r"^[\-_=~\.]{2,}$",
    r"^[ㅠㅜ]{2,}$",
    r"^[ㄷㄷㅇㅇ]+$",
    r"^[ㅋㅎㅠㅜㅡ\s!?.~]+$",
    r"^[(){}\[\]\s]+$",
]

STRONG_CRITERIA_KEYWORDS = [
    "입력기", "기준", "추출", "채택", "분리", "구조", "정책", "규칙",
    "엔진", "fragment", "fragment-first", "projection", "anchor",
    "archive", "ingest", "정규화", "후보", "보존", "판정", "판단",
    "의미 경계", "대화 경계", "raw", "jsonl", "manifest",
]

MEDIUM_CRITERIA_KEYWORDS = [
    "맞다", "좋다", "위험", "부담", "어렵다", "안 된다", "나눠", "추가",
    "단계", "흐름", "역할", "레이어", "측정", "observer", "ticket",
    "결정", "기록", "보류", "candidate", "archive only", "capture",
]

MATERIAL_HINT_KEYWORDS = [
    "예시", "샘플", "문장", "메모", "raw fragment", "scene", "dust",
    "point", "cluster", "space", "local attach", "shared_axes",
]

DECISION_PATTERNS = [
    r"해야 한다",
    r"하는 게 맞다",
    r"분리해야",
    r"금지",
    r"보존",
    r"직접 넣지 말고",
    r"먼저 .* 다음",
    r"오직 .* 만",
]

SHORT_IGNORE_PATTERNS = [
    r"^응+$",
    r"^오케이+$",
    r"^좋아+$",
    r"^맞아요+$",
    r"^그렇지+$",
]


@dataclass
class Segment:
    segment_id: str
    speaker: str
    text: str


@dataclass
class Candidate:
    segment_id: str
    speaker: str
    text: str
    score: float
    label: str
    reasons: List[str]


def detect_marker(line: str) -> Optional[Tuple[str, str]]:
    m = USER_MARKER_RE.match(line)
    if m:
        return "user", m.group(1).lstrip()

    m = ASSISTANT_MARKER_RE.match(line)
    if m:
        return "assistant", m.group(1).lstrip()

    return None


def parse_segments(raw_text: str) -> List[Segment]:
    """
    아주 단순한 세그먼트 파서.
    - [] / [[A]]가 있으면 speaker 전환
    - 빈 줄 두 개 이상이면 세그먼트 경계
    - 마커 없으면 현재 speaker 유지, 없으면 user 시작
    """
    lines = raw_text.splitlines()
    segments: List[Segment] = []

    current_speaker: Optional[str] = None
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_speaker, current_lines, segments
        text = "\n".join(current_lines).strip()
        if text:
            segments.append(
                Segment(
                    segment_id=f"seg_{len(segments) + 1:04d}",
                    speaker=current_speaker or "user",
                    text=text,
                )
            )
        current_lines = []

    blank_streak = 0

    for line in lines:
        detected = detect_marker(line)
        if detected:
            flush()
            speaker, remainder = detected
            current_speaker = speaker
            current_lines = [remainder] if remainder else []
            blank_streak = 0
            continue

        if not line.strip():
            blank_streak += 1
            if blank_streak >= 2:
                flush()
            else:
                current_lines.append("")
            continue

        blank_streak = 0

        if current_speaker is None:
            current_speaker = "user"

        current_lines.append(line.rstrip())

    flush()
    return segments


def is_noise_like(text: str) -> bool:
    t = text.strip()
    if not t:
        return True

    for pattern in NOISE_PATTERNS:
        if re.fullmatch(pattern, t):
            return True

    for pattern in SHORT_IGNORE_PATTERNS:
        if re.fullmatch(pattern, t):
            return True

    if len(t) <= 3 and re.fullmatch(r"[가-힣a-zA-Z0-9!?~.]+", t):
        return True

    return False


def count_keyword_hits(text: str, keywords: List[str]) -> int:
    lower_text = text.lower()
    hits = 0
    for kw in keywords:
        if kw.lower() in lower_text:
            hits += 1
    return hits


def count_pattern_hits(text: str, patterns: List[str]) -> int:
    hits = 0
    for pattern in patterns:
        if re.search(pattern, text):
            hits += 1
    return hits


def score_segment(seg: Segment) -> Candidate:
    text = seg.text.strip()
    reasons: List[str] = []

    if is_noise_like(text):
        return Candidate(
            segment_id=seg.segment_id,
            speaker=seg.speaker,
            text=text,
            score=0.0,
            label="archive_only",
            reasons=["noise_like"],
        )

    score = 0.0

    strong_hits = count_keyword_hits(text, STRONG_CRITERIA_KEYWORDS)
    medium_hits = count_keyword_hits(text, MEDIUM_CRITERIA_KEYWORDS)
    material_hits = count_keyword_hits(text, MATERIAL_HINT_KEYWORDS)
    decision_hits = count_pattern_hits(text, DECISION_PATTERNS)

    if strong_hits:
        score += strong_hits * 2.0
        reasons.append(f"strong_keyword_hits={strong_hits}")

    if medium_hits:
        score += medium_hits * 1.0
        reasons.append(f"medium_keyword_hits={medium_hits}")

    if material_hits:
        score += material_hits * 0.8
        reasons.append(f"material_hint_hits={material_hits}")

    if decision_hits:
        score += decision_hits * 2.2
        reasons.append(f"decision_pattern_hits={decision_hits}")

    length = len(text)
    if length >= 40:
        score += 1.0
        reasons.append("length>=40")
    if length >= 90:
        score += 1.0
        reasons.append("length>=90")
    if length <= 20:
        score -= 1.6
        reasons.append("too_short")

    if seg.speaker == "assistant":
        score += 0.25
        reasons.append("assistant_structural_bias_light")

    user_policy_flag = any(
        x in text for x in ["문제", "기준", "입력기", "분리", "추출"]
    )

    if seg.speaker == "user" and user_policy_flag:
        score += 0.8
        reasons.append("user_policy_signal")

    hard_gate = False

    if seg.speaker == "assistant":
        if decision_hits >= 1 and strong_hits >= 2:
            hard_gate = True
            reasons.append("hard_gate=assistant_decision_plus_strong")
    elif seg.speaker == "user":
        if decision_hits >= 1 or (strong_hits >= 3 and user_policy_flag):
            hard_gate = True
            reasons.append("hard_gate=user_policy_or_decision")

    if score >= 7.5 and hard_gate:
        label = "hard_criteria"
    elif score >= 4.5:
        label = "soft_criteria"
    elif score >= 3.0 and material_hits > 0:
        label = "material_candidate"
    elif score >= 2.5:
        label = "uncertain"
    else:
        label = "archive_only"

    return Candidate(
        segment_id=seg.segment_id,
        speaker=seg.speaker,
        text=text,
        score=round(score, 2),
        label=label,
        reasons=reasons,
    )


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def build_export_record(item: Candidate, queue_type: str) -> dict:
    return {
        "segment_id": item.segment_id,
        "speaker": item.speaker,
        "text": item.text,
        "score": item.score,
        "label": item.label,
        "queue_type": queue_type,
        "reasons": item.reasons,
        "source_type": "chat_txt",
    }


def write_jsonl(path: str, records: List[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_outputs(candidates: List[Candidate], output_dir: str) -> None:
    ensure_dir(output_dir)

    candidates_path = os.path.join(output_dir, "candidates.jsonl")
    summary_path = os.path.join(output_dir, "summary.json")
    seed_md_path = os.path.join(output_dir, "criteria_seed.md")
    accepted_seed_path = os.path.join(output_dir, "accepted_seed.jsonl")
    review_queue_path = os.path.join(output_dir, "review_queue.jsonl")

    with open(candidates_path, "w", encoding="utf-8") as f:
        for item in candidates:
            f.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")

    accepted_seed_records = [
        build_export_record(x, "accepted_seed")
        for x in candidates
        if x.label == "hard_criteria"
    ]

    review_queue_records = [
        build_export_record(x, "review_queue")
        for x in candidates
        if x.label in ("soft_criteria", "material_candidate", "uncertain")
    ]

    write_jsonl(accepted_seed_path, accepted_seed_records)
    write_jsonl(review_queue_path, review_queue_records)

    summary = {
        "total_segments": len(candidates),
        "hard_criteria": sum(1 for x in candidates if x.label == "hard_criteria"),
        "soft_criteria": sum(1 for x in candidates if x.label == "soft_criteria"),
        "material_candidate": sum(1 for x in candidates if x.label == "material_candidate"),
        "uncertain": sum(1 for x in candidates if x.label == "uncertain"),
        "archive_only": sum(1 for x in candidates if x.label == "archive_only"),
        "accepted_seed_count": len(accepted_seed_records),
        "review_queue_count": len(review_queue_records),
    }

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    top_items = sorted(
        [
            x for x in candidates
            if x.label in ("hard_criteria", "soft_criteria", "material_candidate", "uncertain")
        ],
        key=lambda x: x.score,
        reverse=True,
    )

    with open(seed_md_path, "w", encoding="utf-8") as f:
        f.write("# criteria seed\n\n")

        f.write("## accepted_seed\n\n")
        for item in [x for x in top_items if x.label == "hard_criteria"]:
            f.write(f"### {item.segment_id} | {item.label} | score={item.score}\n")
            f.write(f"- speaker: {item.speaker}\n")
            f.write(f"- reasons: {', '.join(item.reasons)}\n")
            f.write(f"- text:\n\n{item.text}\n\n")

        f.write("## review_queue\n\n")
        for item in [x for x in top_items if x.label in ("soft_criteria", "material_candidate", "uncertain")]:
            f.write(f"### {item.segment_id} | {item.label} | score={item.score}\n")
            f.write(f"- speaker: {item.speaker}\n")
            f.write(f"- reasons: {', '.join(item.reasons)}\n")
            f.write(f"- text:\n\n{item.text}\n\n")

    print(f"[OK] total_segments={len(candidates)}")
    print(f"[OK] hard_criteria={summary['hard_criteria']}")
    print(f"[OK] soft_criteria={summary['soft_criteria']}")
    print(f"[OK] material_candidate={summary['material_candidate']}")
    print(f"[OK] uncertain={summary['uncertain']}")
    print(f"[OK] archive_only={summary['archive_only']}")
    print(f"[OK] accepted_seed_count={summary['accepted_seed_count']}")
    print(f"[OK] review_queue_count={summary['review_queue_count']}")
    print(f"[OK] output_dir={output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="입력 txt 경로")
    parser.add_argument("--output-dir", required=True, help="출력 디렉토리")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        raw_text = f.read()

    segments = parse_segments(raw_text)
    candidates = [score_segment(seg) for seg in segments]
    write_outputs(candidates, args.output_dir)


if __name__ == "__main__":
    main()