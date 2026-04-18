from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import re


TIMESTAMP_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
KOREAN_TIME_RE = re.compile(r"\b\d+분\s*\d+초\b")
TRANSCRIPT_MARKER_RE = re.compile(r"(?:챕터\s*\d+[:.]?\s*|(?:^|\s)\d+:\d{2,}초?)", re.IGNORECASE)
SPEAKER_RE = re.compile(r"^\s*[A-Za-z가-힣][A-Za-z가-힣 ._-]{0,30}:\s+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+")

SHORT_INTERJECTION_SET = {
    "네",
    "네.",
    "음",
    "음.",
    "아",
    "아.",
    "어",
    "어.",
    "그죠?",
    "그쵸?",
    "그렇죠?",
    "맞아요",
    "맞아요.",
    "오",
    "오.",
}


@dataclass(frozen=True)
class PreprocessResult:
    original_line_count: int
    normalized_sentence_count: int
    regrouped_chunk_count: int
    dropped_interjection_count: int
    normalized_text: str
    regrouped_chunks: List[str]
    checkpoints: Dict[str, object]


def preprocess_transcript_text(raw_text: str) -> PreprocessResult:
    lines = [line.strip() for line in raw_text.replace("\r\n", "\n").replace("\r", "\n").splitlines()]
    lines = [line for line in lines if line]

    normalized_sentences: List[str] = []
    dropped_interjection_count = 0

    for line in lines:
        cleaned = _normalize_line(line)
        if not cleaned:
            continue
        sentence_like = [part.strip() for part in SENTENCE_SPLIT_RE.split(cleaned) if part.strip()]
        for part in sentence_like or [cleaned]:
            if _is_droppable_interjection(part):
                dropped_interjection_count += 1
                continue
            normalized_sentences.append(part)

    regrouped_chunks = _aggregate_sentences(normalized_sentences)
    normalized_text = "\n\n".join(regrouped_chunks)

    return PreprocessResult(
        original_line_count=len(lines),
        normalized_sentence_count=len(normalized_sentences),
        regrouped_chunk_count=len(regrouped_chunks),
        dropped_interjection_count=dropped_interjection_count,
        normalized_text=normalized_text,
        regrouped_chunks=regrouped_chunks,
        checkpoints={
            "preprocess_objective": "move from subtitle-like shards toward bounded meaning chunks",
            "verification_points": [
                "timestamp markers should stop dominating chunk starts",
                "short response tails should be absorbed or dropped when they carry no local claim",
                "chunk count should be materially lower than raw dust shard count",
                "result should still remain traceable to source text family",
            ],
        },
    )


def preprocess_transcript_file(input_path: Path) -> PreprocessResult:
    return preprocess_transcript_text(input_path.read_text(encoding="utf-8"))


def _normalize_line(line: str) -> str:
    cleaned = TRANSCRIPT_MARKER_RE.sub(" ", line)
    cleaned = TIMESTAMP_RE.sub(" ", cleaned)
    cleaned = KOREAN_TIME_RE.sub(" ", cleaned)
    cleaned = SPEAKER_RE.sub("", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _is_droppable_interjection(text: str) -> bool:
    stripped = text.strip()
    if stripped in SHORT_INTERJECTION_SET:
        return True
    if len(stripped) <= 4 and stripped.endswith("?") and stripped in SHORT_INTERJECTION_SET:
        return True
    return False


def _aggregate_sentences(sentences: List[str]) -> List[str]:
    chunks: List[str] = []
    current: List[str] = []
    char_budget = 0

    for sentence in sentences:
        sentence_len = len(sentence)
        # Keep chunks bounded and readable rather than letting one long transcript swallow everything.
        if current and (char_budget + sentence_len > 420 or len(current) >= 5):
            chunks.append(" ".join(current).strip())
            current = []
            char_budget = 0
        current.append(sentence)
        char_budget += sentence_len + 1

    if current:
        chunks.append(" ".join(current).strip())
    return chunks
