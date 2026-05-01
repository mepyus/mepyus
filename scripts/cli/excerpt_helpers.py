"""Bounded excerpt helpers for Phase 1.6/1.7 evidence grounding."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Tuple

MAX_EXCERPT_LINES = 12
MAX_EXCERPT_CHARS = 1600
MIN_USEFUL_CHARS = 80
METADATA_PREFIXES = ("- phase:", "- authority:", "- compatibility:", "- baseline_promotion:", "- created_for:")


def _clip(lines: List[str]) -> List[str]:
    text = "\n".join(lines[:MAX_EXCERPT_LINES])
    if len(text) <= MAX_EXCERPT_CHARS:
        return lines[:MAX_EXCERPT_LINES]
    clipped = text[:MAX_EXCERPT_CHARS].splitlines()
    return clipped or lines[:1]


def _is_heading_only(lines: List[str]) -> bool:
    non_empty = [line.strip() for line in lines if line.strip()]
    return len(non_empty) == 1 and non_empty[0].startswith("#")


def _is_metadata_only(lines: List[str]) -> bool:
    non_empty = [line.strip().lower() for line in lines if line.strip()]
    if not non_empty:
        return False
    metadata_count = sum(1 for line in non_empty if line.startswith(METADATA_PREFIXES))
    return metadata_count == len(non_empty)


def _quality(lines: List[str], reason: str) -> Tuple[str, str]:
    excerpt = "\n".join(lines).strip()
    if not excerpt:
        return "poor", "empty"
    if _is_heading_only(lines):
        return "poor", "title_only"
    if _is_metadata_only(lines):
        return "poor", "metadata_only"
    reason_terms = _terms_from(reason, "")
    term_hits = sum(1 for term in reason_terms if term in excerpt.lower())
    if len(excerpt) < MIN_USEFUL_CHARS and term_hits == 0:
        return "poor", "too_short_to_support"
    if term_hits >= 2 or any(marker in excerpt.lower() for marker in ("must", "do not", "should", "required", "allowed", "forbidden", "금지", "필수", "한다", "해야")):
        return "strong", ""
    return "usable", ""


def _terms_from(reason: str, path: str) -> List[str]:
    raw = reason.replace("/", " ").replace("_", " ").replace("-", " ").split()
    path_terms = Path(path).stem.replace("_", " ").replace("-", " ").split()
    terms = []
    for term in raw + path_terms:
        clean = "".join(ch for ch in term.lower() if ch.isalnum())
        if len(clean) >= 5 and clean not in terms:
            terms.append(clean)
    return terms[:10]


def _find_match(lines: List[str], terms: Iterable[str]) -> int:
    lowered = [line.lower() for line in lines]
    for term in terms:
        for idx, line in enumerate(lowered):
            if term in line:
                return idx
    for idx, line in enumerate(lines):
        if line.strip():
            return idx
    return 0


def _heading_plus_block(lines: List[str], idx: int) -> tuple[List[str], int, int]:
    heading = idx
    for pos in range(idx, -1, -1):
        if lines[pos].lstrip().startswith("#"):
            heading = pos
            break
    end = min(len(lines), heading + MAX_EXCERPT_LINES)
    block = []
    seen_content_after_heading = False
    for pos in range(heading, end):
        line = lines[pos]
        if pos > heading and line.lstrip().startswith("#") and seen_content_after_heading:
            break
        if line.strip():
            seen_content_after_heading = True
        block.append(line)
    return _clip(block), heading, heading + len(block) - 1


def _heading_plus_substantive_block(lines: List[str], idx: int) -> tuple[List[str], int, int]:
    block, start, end = _heading_plus_block(lines, idx)
    if not _is_heading_only(block) and not _is_metadata_only(block):
        return block, start, end
    heading = start
    pos = heading + 1
    while pos < len(lines) and not lines[pos].strip():
        pos += 1
    # Skip short status metadata blocks when a real section follows.
    while pos < len(lines):
        if lines[pos].lstrip().startswith("#"):
            next_block, next_start, next_end = _heading_plus_block(lines, pos)
            if not _is_heading_only(next_block) and not _is_metadata_only(next_block):
                return next_block, next_start, next_end
        para, para_start, para_end = _paragraph_block(lines, pos)
        if not _is_heading_only(para) and not _is_metadata_only(para) and "\n".join(para).strip():
            return _clip([lines[heading], ""] + para), heading, min(len(lines) - 1, heading + len(_clip([lines[heading], ""] + para)) - 1)
        pos = para_end + 1
    return block, start, end


def _paragraph_block(lines: List[str], idx: int) -> tuple[List[str], int, int]:
    start = idx
    while start > 0 and lines[start - 1].strip():
        start -= 1
    end = idx
    while end + 1 < len(lines) and lines[end + 1].strip():
        end += 1
    block = _clip(lines[start : end + 1])
    return block, start, start + len(block) - 1


def _bullet_cluster(lines: List[str], idx: int) -> tuple[List[str], int, int]:
    def is_bullet(line: str) -> bool:
        stripped = line.lstrip()
        return stripped.startswith("- ") or stripped.startswith("* ") or stripped[:3].endswith(". ")

    if not is_bullet(lines[idx]):
        return _paragraph_block(lines, idx)
    start = idx
    while start > 0 and is_bullet(lines[start - 1]):
        start -= 1
    end = idx
    while end + 1 < len(lines) and is_bullet(lines[end + 1]):
        end += 1
    # Single bullets are often too thin; include a following sibling paragraph if bounded.
    if start == end and end + 1 < len(lines):
        probe = end + 1
        while probe < len(lines) and not lines[probe].strip():
            probe += 1
        if probe < len(lines) and not lines[probe].lstrip().startswith("#"):
            end = min(len(lines) - 1, probe + 2)
    block = _clip(lines[start : end + 1])
    return block, start, start + len(block) - 1


def _line_window(lines: List[str], idx: int) -> tuple[List[str], int, int]:
    start = max(0, idx - 3)
    end = min(len(lines), idx + 4)
    block = _clip(lines[start:end])
    return block, start, start + len(block) - 1


def _result(path: str, pointer: str, block: List[str], mode: str, start: int, end: int, reason: str, retry_count: int = 0, fallback_reason: str = "") -> dict:
    excerpt = "\n".join(block).strip()
    quality, quality_reason = _quality(block, reason)
    if mode == "pointer_only":
        quality = "poor"
        quality_reason = fallback_reason or quality_reason or "pointer_only"
    if quality == "poor" and mode != "pointer_only":
        status = "weak_grounded"
        confidence = "low"
    elif quality == "usable":
        status = "direct_grounded"
        confidence = "medium"
    elif quality == "strong":
        status = "direct_grounded"
        confidence = "high"
    else:
        status = "pointer_only"
        confidence = "low"
    return {
        "pointer": f"{path}:L{start + 1}-L{end + 1}" if mode != "pointer_only" else pointer,
        "excerpt_window": excerpt,
        "excerpt_mode": mode,
        "grounding_status": status,
        "local_confidence": confidence,
        "excerpt_quality": quality,
        "excerpt_retry_count": retry_count,
        "fallback_reason": fallback_reason if mode == "pointer_only" else "",
        "tuning_note": quality_reason,
    }


def extract_excerpt(path: str, reason: str = "") -> dict:
    source = Path(path)
    if not source.exists() or not source.is_file():
        return {
            "pointer": path,
            "excerpt_window": "",
            "excerpt_mode": "pointer_only",
            "grounding_status": "pointer_only",
            "local_confidence": "low",
            "excerpt_quality": "poor",
            "excerpt_retry_count": 0,
            "fallback_reason": "missing_or_not_file",
            "tuning_note": "pointer_only",
        }
    try:
        text = source.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {
            "pointer": path,
            "excerpt_window": "",
            "excerpt_mode": "pointer_only",
            "grounding_status": "pointer_only",
            "local_confidence": "low",
            "excerpt_quality": "poor",
            "excerpt_retry_count": 0,
            "fallback_reason": "unicode_decode_error",
            "tuning_note": "pointer_only",
        }
    if not text.strip():
        return {
            "pointer": path,
            "excerpt_window": "",
            "excerpt_mode": "pointer_only",
            "grounding_status": "pointer_only",
            "local_confidence": "low",
            "excerpt_quality": "poor",
            "excerpt_retry_count": 0,
            "fallback_reason": "empty_file",
            "tuning_note": "pointer_only",
        }
    lines = text.splitlines()
    idx = _find_match(lines, _terms_from(reason, path))
    suffix = source.suffix.lower()
    if suffix == ".json":
        block, start, end = _line_window(lines, idx)
        mode = "line_window"
    elif idx < len(lines) and lines[idx].lstrip().startswith(("- ", "* ")):
        block, start, end = _bullet_cluster(lines, idx)
        mode = "bullet_cluster"
    elif any(line.lstrip().startswith("#") for line in lines[: max(idx + 1, 1)]):
        block, start, end = _heading_plus_substantive_block(lines, idx)
        mode = "heading_plus_block"
    else:
        block, start, end = _paragraph_block(lines, idx)
        mode = "paragraph_block"
    quality, quality_reason = _quality(block, reason)
    retry_count = 0
    if quality == "poor" and quality_reason in {"title_only", "metadata_only", "too_short_to_support"}:
        retry_count += 1
        retry_block, retry_start, retry_end = _line_window(lines, idx)
        retry_quality, _ = _quality(retry_block, reason)
        if retry_quality != "poor":
            block, start, end, mode, quality = retry_block, retry_start, retry_end, "line_window", retry_quality
    if quality == "poor" and not "\n".join(block).strip():
        return _result(path, path, [], "pointer_only", 0, 0, reason, retry_count, "empty_after_extraction")
    return _result(path, path, block, mode, start, end, reason, retry_count)
