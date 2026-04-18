from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


ROW_KEY_LEXICON = {
    "packet_texture": [
        "인베딩 공간",
        "거리",
        "가까워지도록",
        "멀리 떨어지도록",
        "매트릭 러닝",
    ],
    "grounding_status": [
        "레이블",
        "분류",
        "클래스 토큰",
        "파지티브",
        "네거티브",
        "기준에 따라서",
    ],
    "emergence_status": [
        "응용",
        "클러스터링",
        "리트리벌",
        "랭킹",
    ],
    "carryover_risk": [
        "데이터 수집",
        "레이블링",
        "힘든 일",
        "편하죠",
    ],
    "maturation_state": [
        "어떻게 배우느냐",
        "의미 있는 거리",
        "훈련을 해요",
        "몇 가지 방법",
        "설명을 드릴 거고",
        "인베딩 공간을 배워서",
    ],
    "traceability_status": [
        "앵커",
        "주제",
        "가장 가까운 거",
        "추천",
    ],
}

OBJECT_CONTEXT_LEXICON = [
    "시작하도록 하겠습니다",
    "처음",
    "알아두시면",
    "비전 랭귀지 모델",
    "매트릭 러닝",
]


def extract_segment_source_context(
    *,
    asset_id: str,
    state_row_key: str,
    source_pointer: str,
) -> Dict[str, str]:
    source_path = Path(source_pointer)
    if not source_path.exists():
        raise FileNotFoundError(f"source file not found: {source_pointer}")

    paragraphs = _load_timestamp_paragraphs(source_path)
    if not paragraphs:
        raise ValueError(f"no readable paragraphs in source file: {source_pointer}")

    matched = _match_paragraph(state_row_key=state_row_key, paragraphs=paragraphs)
    surrounding = _surrounding_context(paragraphs, matched["index"])
    return {
        "asset_id": asset_id,
        "state_row_key": state_row_key,
        "source_pointer": source_pointer,
        "paragraph_ref": matched["paragraph_ref"],
        "paragraph_text": matched["paragraph_text"],
        "surrounding_context": surrounding,
        "row_to_paragraph_mapping": f"{state_row_key} -> {matched['paragraph_ref']}",
        "match_score": str(matched["match_score"]),
        "match_confidence": matched["match_confidence"],
    }


def extract_source_opening_context(*, source_pointer: str) -> Dict[str, str]:
    source_path = Path(source_pointer)
    if not source_path.exists():
        raise FileNotFoundError(f"source file not found: {source_pointer}")

    paragraphs = _load_timestamp_paragraphs(source_path)
    if not paragraphs:
        raise ValueError(f"no readable paragraphs in source file: {source_pointer}")

    first = paragraphs[0]
    surrounding = _surrounding_context(paragraphs, 0)
    return {
        "source_pointer": source_pointer,
        "paragraph_ref": first["paragraph_ref"],
        "paragraph_text": first["paragraph_text"],
        "surrounding_context": surrounding,
    }


def extract_object_source_context(*, source_pointer: str) -> Dict[str, str]:
    source_path = Path(source_pointer)
    if not source_path.exists():
        raise FileNotFoundError(f"source file not found: {source_pointer}")

    paragraphs = _load_timestamp_paragraphs(source_path)
    if not paragraphs:
        raise ValueError(f"no readable paragraphs in source file: {source_pointer}")

    matched = _match_object_paragraph(paragraphs)
    surrounding = _surrounding_context(paragraphs, matched["index"])
    return {
        "source_pointer": source_pointer,
        "paragraph_ref": matched["paragraph_ref"],
        "paragraph_text": matched["paragraph_text"],
        "surrounding_context": surrounding,
    }


def _load_timestamp_paragraphs(path: Path) -> List[Dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    paragraphs: List[Dict[str, str]] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if _looks_like_timestamp(line) and index + 1 < len(lines):
            text_line = lines[index + 1].strip()
            if text_line:
                paragraphs.append(
                    {
                        "index": str(len(paragraphs)),
                        "timestamp": line,
                        "paragraph_ref": f"lines {index + 1}-{index + 2} @ {line}",
                        "paragraph_text": text_line,
                    }
                )
            index += 2
            continue
        paragraphs.append(
            {
                "index": str(len(paragraphs)),
                "timestamp": "",
                "paragraph_ref": f"line {index + 1}",
                "paragraph_text": line,
            }
        )
        index += 1
    return paragraphs


def _match_paragraph(*, state_row_key: str, paragraphs: List[Dict[str, str]]) -> Dict[str, Any]:
    lexicon = ROW_KEY_LEXICON.get(state_row_key, [])
    scored: List[tuple[int, int, Dict[str, str]]] = []
    for idx, paragraph in enumerate(paragraphs):
        text = paragraph["paragraph_text"]
        score = 0
        for token in lexicon:
            if token in text:
                score += 1
        if state_row_key == "packet_texture":
            if "인베딩 공간" in text and "거리" in text:
                score += 2
            if "가까워지도록" in text or "멀리 떨어지도록" in text:
                score += 1
        scored.append((score, -idx, paragraph))
    best_score, _neg_idx, best = max(scored, key=lambda item: (item[0], item[1]))
    if best_score <= 0:
        best = paragraphs[0]
    if best_score >= 3:
        confidence = "high"
    elif best_score >= 2:
        confidence = "medium"
    else:
        confidence = "low"
    return {
        "index": int(best["index"]),
        "paragraph_ref": best["paragraph_ref"],
        "paragraph_text": best["paragraph_text"],
        "match_score": best_score,
        "match_confidence": confidence,
    }


def _match_object_paragraph(paragraphs: List[Dict[str, str]]) -> Dict[str, Any]:
    scored: List[tuple[int, int, Dict[str, str]]] = []
    for idx, paragraph in enumerate(paragraphs[:12]):
        text = paragraph["paragraph_text"]
        score = 0
        for token in OBJECT_CONTEXT_LEXICON:
            if token in text:
                score += 1
        if "비전 랭귀지 모델" in text and "처음" in text:
            score += 2
        if "매트릭 러닝" in text:
            score += 1
        scored.append((score, -idx, paragraph))
    best_score, _neg_idx, best = max(scored, key=lambda item: (item[0], item[1]))
    if best_score <= 0:
        best = paragraphs[0]
    return {
        "index": int(best["index"]),
        "paragraph_ref": best["paragraph_ref"],
        "paragraph_text": best["paragraph_text"],
    }


def _surrounding_context(paragraphs: List[Dict[str, str]], index: int) -> str:
    parts: List[str] = []
    start = max(0, index - 1)
    end = min(len(paragraphs), index + 2)
    for idx in range(start, end):
        prefix = "current" if idx == index else ("prev" if idx < index else "next")
        paragraph = paragraphs[idx]
        parts.append(f"{prefix} [{paragraph['paragraph_ref']}] {paragraph['paragraph_text']}")
    return "\n".join(parts)


def _looks_like_timestamp(text: str) -> bool:
    if ":" not in text:
        return False
    left, right = text.split(":", 1)
    return left.isdigit() and right.isdigit()
