from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence
import re


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+")
BULLET_RE = re.compile(r"^\s*[-*•]\s+")


@dataclass(frozen=True)
class DustInput:
    dust_id: str
    origin_id: str
    source_type: str
    source_ref: Optional[str]
    text: str
    source_path: Optional[str]
    source_span: Dict[str, Optional[int]]
    siblings: Sequence[str]
    created_at: str


def build_dust_inputs_for_material(material: Dict[str, object]) -> List[DustInput]:
    source_type = _normalized_source_type(str(material.get("source_type", "unknown")))
    source_ref = str(material.get("source_ref", "")) or None
    raw_payload = str(material.get("raw_payload", ""))
    created_at = str(material.get("created_at", ""))

    units = split_into_dust_units(source_type, raw_payload)
    if not units:
        return []

    preview_ids = [
        "dst_%s_%03d" % (material["material_id"], index)
        for index, _ in enumerate(units, start=1)
    ]
    rows: List[DustInput] = []
    for index, unit in enumerate(units, start=1):
        dust_id = preview_ids[index - 1]
        rows.append(
            DustInput(
                dust_id=dust_id,
                origin_id=str(material["material_id"]),
                source_type=source_type,
                source_ref=source_ref,
                text=unit,
                source_path=source_ref,
                source_span={"start": None, "end": None},
                siblings=tuple(ref for ref in preview_ids if ref != dust_id),
                created_at=created_at,
            )
        )
    return rows


def build_dust_inputs_from_source(
    *,
    source_id: str,
    source_type: str,
    source_ref: Optional[str],
    raw_payload: str,
    created_at: str,
) -> List[DustInput]:
    synthetic_material = {
        "material_id": source_id,
        "source_type": source_type,
        "source_ref": source_ref or "",
        "raw_payload": raw_payload,
        "created_at": created_at,
    }
    return build_dust_inputs_for_material(synthetic_material)


def split_into_dust_units(source_type: str, text: str) -> List[str]:
    normalized = _normalize_text(text)
    if not normalized:
        return []
    if source_type == "code":
        units = _split_code_units(normalized)
    elif source_type == "log":
        units = _split_log_units(normalized)
    elif source_type == "bullet":
        units = _split_bullet_units(normalized)
    else:
        units = _split_text_units(normalized)
    return [unit for unit in units if unit]


def _split_text_units(text: str) -> List[str]:
    sentences = [part.strip() for part in SENTENCE_SPLIT_RE.split(text) if part.strip()]
    return sentences or [text]


def _split_code_units(text: str) -> List[str]:
    chunks = [chunk.strip() for chunk in re.split(r"\n(?=def |class )", text) if chunk.strip()]
    return chunks or [text]


def _split_log_units(text: str) -> List[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines or [text]


def _split_bullet_units(text: str) -> List[str]:
    bullets = [BULLET_RE.sub("", line).strip() for line in text.splitlines() if BULLET_RE.match(line)]
    return bullets or _split_text_units(text)


def _normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def _normalized_source_type(source_type: str) -> str:
    lowered = source_type.strip().lower()
    if lowered in {
        "memo",
        "paper",
        "review",
        "text",
        "note",
        "worklog",
        "journal",
        "essay",
        "doc",
        "report",
        "document",
        "spec",
    }:
        return "text"
    if lowered in {"code"}:
        return "code"
    if lowered in {"log"}:
        return "log"
    if lowered in {"bullet", "checklist"}:
        return "bullet"
    return lowered or "unknown"
