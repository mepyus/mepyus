from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

from app.fragment.schema import FragmentRecord, PageRef, SourceRange


def enrich_fragment_with_source_location(runtime_root: Path, fragment: FragmentRecord) -> FragmentRecord:
    source_text = _read_source_text(runtime_root, fragment.source_path)
    if not source_text:
        return fragment

    start, end = _find_span(source_text, fragment.raw_text)
    paragraph_index = _find_paragraph_index(source_text, start) if start is not None else fragment.paragraph_index

    return FragmentRecord(
        fragment_id=fragment.fragment_id,
        source_id=fragment.source_id,
        source_type=fragment.source_type,
        source_path=fragment.source_path,
        raw_text=fragment.raw_text,
        unit_scale=fragment.unit_scale,
        created_at=fragment.created_at,
        source_range=SourceRange(
            start=start if start is not None else fragment.source_range.start,
            end=end if end is not None else fragment.source_range.end,
        ),
        page_ref=fragment.page_ref if fragment.page_ref != PageRef() else PageRef(page_index=0, page_label="p1"),
        paragraph_index=paragraph_index,
        anchor=fragment.anchor,
        anchors=fragment.anchors,
        D=fragment.D,
        I=fragment.I,
        S=fragment.S,
        scene=fragment.scene,
        flow=fragment.flow,
        time=fragment.time,
        confidence=fragment.confidence,
        provenance_log=fragment.provenance_log,
        metadata=fragment.metadata,
    )


def _read_source_text(runtime_root: Path, source_path: str) -> str:
    if not source_path:
        return ""

    direct_path = Path(source_path)
    candidates = []
    if direct_path.is_absolute():
        candidates.append(direct_path)
    else:
        candidates.append(runtime_root / "source_documents" / source_path)
        candidates.append(runtime_root / source_path)

    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.read_text(encoding="utf-8")
    return ""


def _find_span(source_text: str, fragment_text: str) -> Tuple[Optional[int], Optional[int]]:
    needle = " ".join(fragment_text.split())
    if not needle:
        return None, None

    exact = source_text.find(fragment_text)
    if exact >= 0:
        return exact, exact + len(fragment_text)

    normalized_source = " ".join(source_text.split())
    normalized_index = normalized_source.find(needle)
    if normalized_index < 0:
        return None, None

    # Fallback when whitespace normalization changes direct offsets.
    raw_index = source_text.find(fragment_text.strip())
    if raw_index >= 0:
        return raw_index, raw_index + len(fragment_text.strip())
    return None, None


def _find_paragraph_index(source_text: str, start: Optional[int]) -> Optional[int]:
    if start is None:
        return None
    paragraphs = source_text.split("\n\n")
    cursor = 0
    for index, paragraph in enumerate(paragraphs):
        para_start = cursor
        para_end = cursor + len(paragraph)
        if para_start <= start <= para_end:
            return index
        cursor = para_end + 2
    return None
