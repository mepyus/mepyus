from __future__ import annotations

import re
from typing import List

from .schema import ObserverFeatureSet


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+")
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+-]{2,}|[가-힣]{2,}")

COMPARISON_MARKERS = ("반면", "반대로", "다르다", "같지만", "하나는", "다른 하나", "비슷", "대조", "비교")
REFLECTION_MARKERS = ("것 같다", "아닐까", "어쩌면", "느껴진다", "돌아보면", "실감한다", "문제처럼", "가깝다")
EVIDENCE_MARKERS = ("그 장면", "보여 준다", "보여준다", "그 때문이다", "그 이유도", "실제", "통계", "데이터", "장면")
EXAMPLE_MARKERS = ("예를 들어", "예컨대", "가령", "사례", "장면")
PROBLEM_MARKERS = ("문제", "부족", "불안", "흔들", "막힐", "충돌", "어긋", "실패", "낯설")
DEFINITION_MARKERS = ("란 ", "라기보다", "의미", "가깝다", "정의", "말한다")
GENERALIZATION_MARKERS = ("결국", "그래서", "그러니", "이런 데서", "이 말은", "일처럼", "지표", "일반")
MIXED_SIGNAL_MARKERS = ("하지만", "동시에", "같기도", "반복됐고", "상반", "섞여", "한쪽", "다른 쪽")


def extract_features(text: str) -> ObserverFeatureSet:
    normalized = " ".join(text.split())
    lowered = normalized.lower()
    sentences = [part.strip() for part in SENTENCE_SPLIT_RE.split(normalized) if part.strip()]
    anchor_terms = _extract_anchor_terms(normalized)
    return ObserverFeatureSet(
        text=normalized,
        lowered=lowered,
        sentence_count=max(1, len(sentences)),
        has_quote=("\"" in normalized or "“" in normalized or "”" in normalized),
        has_question=("?" in normalized or "까" in normalized),
        has_comparison_marker=_contains_any(normalized, COMPARISON_MARKERS),
        has_reflection_marker=_contains_any(normalized, REFLECTION_MARKERS),
        has_evidence_marker=_contains_any(normalized, EVIDENCE_MARKERS),
        has_example_marker=_contains_any(normalized, EXAMPLE_MARKERS),
        has_problem_marker=_contains_any(normalized, PROBLEM_MARKERS),
        has_definition_marker=_contains_any(normalized, DEFINITION_MARKERS),
        has_generalization_marker=_contains_any(normalized, GENERALIZATION_MARKERS),
        has_mixed_signal=_contains_any(normalized, MIXED_SIGNAL_MARKERS),
        token_count=len(TOKEN_RE.findall(normalized)),
        anchor_terms=anchor_terms,
    )


def _contains_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(pattern in text for pattern in patterns)


def _extract_anchor_terms(text: str) -> List[str]:
    seen = set()
    out: List[str] = []
    for token in TOKEN_RE.findall(text):
        lowered = token.lower()
        if lowered in seen:
            continue
        if len(lowered) < 3:
            continue
        seen.add(lowered)
        out.append(lowered)
        if len(out) >= 6:
            break
    return out
