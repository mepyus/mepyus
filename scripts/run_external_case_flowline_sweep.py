#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_ROOT = REPO_ROOT / "inputs" / "external_cases"
OUTPUT_DIR = REPO_ROOT / "app" / "work" / "archive_review" / "external_case_support" / "external_case_flowline_sweep" / "generated"

TIMECODE_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b|\b\d+분\s*\d+초\b")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+|\n+")

AXIS_TERMS: Dict[str, Sequence[str]] = {
    "context_structuring": (
        "컨텍스트", "context", "문서", "markdown", "spec", "지침", "설계", "프론트메터", "frontmatter",
        "구조화", "정리", "instruction", "prompt", "맥락", "document",
    ),
    "agent_delegation": (
        "에이전트", "agent", "sub agent", "sub-agent", "delegation", "delegate", "세션", "병렬",
        "parallel", "codex", "claude code", "클로드 코드", "위임", "호출", "skill",
    ),
    "operating_automation": (
        "자동화", "automation", "운영", "workflow", "파이프라인", "pipeline", "process", "승인",
        "hook", "mcp", "tool", "도구", "system", "배치", "routing", "queue", "approval",
    ),
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


def _normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = TIMECODE_RE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def _sentences(text: str) -> List[str]:
    normalized = _normalize(text)
    rows = [part.strip() for part in SENTENCE_SPLIT_RE.split(normalized) if part.strip()]
    return rows or [normalized]


def _score_axis(text: str, terms: Sequence[str]) -> int:
    lowered = text.lower()
    score = 0
    for term in terms:
        if term.lower() in lowered:
            score += 1
    return score


def _classify_file(path: Path) -> Dict[str, object]:
    raw_text = path.read_text(encoding="utf-8")
    sentences = _sentences(raw_text)
    axis_scores = {axis: _score_axis(raw_text, terms) for axis, terms in AXIS_TERMS.items()}

    matched_segments: List[Dict[str, object]] = []
    for sentence in sentences:
        segment_scores = {axis: _score_axis(sentence, terms) for axis, terms in AXIS_TERMS.items()}
        hit_axes = [axis for axis, score in segment_scores.items() if score > 0]
        if len(hit_axes) >= 2:
            matched_segments.append(
                {
                    "text": sentence[:280],
                    "hit_axes": hit_axes,
                    "scores": segment_scores,
                }
            )
    matched_segments = matched_segments[:6]

    active_axes = [axis for axis, score in axis_scores.items() if score > 0]
    if len(active_axes) == 3:
        support_level = "strong_flowline_contact"
    elif len(active_axes) == 2:
        support_level = "partial_flowline_contact"
    elif len(active_axes) == 1:
        support_level = "single_axis_contact"
    else:
        support_level = "weak_or_none"

    why_selected = _why_selected(axis_scores, support_level)
    return {
        "input_path": _relative(path),
        "support_level": support_level,
        "axis_scores": axis_scores,
        "active_axes": active_axes,
        "why_selected": why_selected,
        "matched_segments": matched_segments,
        "user_language_summary": _user_summary(path.name, support_level, active_axes),
        "user_language_caution": _user_caution(support_level, matched_segments),
    }


def _why_selected(axis_scores: Dict[str, int], support_level: str) -> str:
    if support_level == "strong_flowline_contact":
        return (
            "the file contains signals for context structuring, agent delegation, and operating automation "
            "in the same material family"
        )
    if support_level == "partial_flowline_contact":
        top_axes = [axis for axis, score in axis_scores.items() if score > 0]
        return f"the file strongly touches {', '.join(top_axes)} but does not yet show the full operating chain"
    if support_level == "single_axis_contact":
        top_axis = max(axis_scores.items(), key=lambda item: item[1])[0]
        return f"the file is dominated by one axis only: {top_axis}"
    return "the file does not clearly express the target flowline with the current bounded read"


def _user_summary(filename: str, support_level: str, active_axes: Sequence[str]) -> str:
    if support_level == "strong_flowline_contact":
        return f"{filename}는 문서/맥락 구조화, 에이전트 위임, 운영 자동화가 함께 나타나는 편이라 공통 흐름선에 직접 닿는다."
    if support_level == "partial_flowline_contact":
        return f"{filename}는 {', '.join(active_axes)} 쪽은 보이지만 아직 전체 흐름선이 한 번에 강하게 잡히진 않는다."
    if support_level == "single_axis_contact":
        return f"{filename}는 흐름 전체보다 한 축만 강하게 말하는 자료에 가깝다."
    return f"{filename}는 현재 bounded sweep 기준으로는 이 흐름선 접점이 약하다."


def _user_caution(support_level: str, matched_segments: Sequence[Dict[str, object]]) -> str:
    if support_level == "strong_flowline_contact" and matched_segments:
        return "공통 흐름선에 닿는다고 해서 곧바로 같은 line으로 잠그면 과하다. 실제로는 운영 사례, 홍보, 설명 톤이 섞여 있을 수 있다."
    if support_level == "partial_flowline_contact":
        return "일부 축만 잡혔다고 전체 operating chain으로 읽으면 과장될 수 있다."
    return "weak contact 자료를 억지로 같은 흐름에 묶지 말아야 한다."


def main(argv: List[str]) -> int:
    files = sorted(
        [
            path
            for path in INPUT_ROOT.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".txt", ".md"}
            and path.name not in {"README.md", "folder_status.md"}
        ]
    )
    rows = [_classify_file(path) for path in files]
    counts = Counter(row["support_level"] for row in rows)
    strong = [row for row in rows if row["support_level"] == "strong_flowline_contact"]
    partial = [row for row in rows if row["support_level"] == "partial_flowline_contact"]

    payload = {
        "sweep_name": "external_case_flowline_sweep_v0",
        "generated_at": _now_iso(),
        "target_flowline": "context structuring -> agent delegation / parallel execution -> operating automation",
        "file_count": len(rows),
        "support_level_counts": dict(counts),
        "strong_examples": strong[:12],
        "partial_examples": partial[:12],
        "rows": rows,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"external_case_flowline_sweep_{_stamp()}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "output_path": _relative(output_path),
                "file_count": len(rows),
                "support_level_counts": dict(counts),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
