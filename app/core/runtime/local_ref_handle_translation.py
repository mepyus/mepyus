from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Sequence
import json
import re


ALIAS_DICTIONARY_PATH = (
    Path(__file__).resolve().parents[2]
    / "work"
    / "processor_compare"
    / "anchor_engine"
    / "dictionaries"
    / "alias_dictionary.json"
)


def build_local_ref_translated_handles(metadata: Dict[str, object]) -> List[Dict[str, object]]:
    handles = dict(metadata.get("transformable_handles", {}) or {})
    source_local_ref = str(handles.get("source_local_ref", "")).strip()
    if not source_local_ref:
        return []

    rows: List[Dict[str, object]] = []
    seen = set()
    for original, basis in _iter_translation_candidates(metadata):
        match = _match_alias(original)
        if not match:
            continue
        translated_handle = str(match.get("canonical_key", "")).strip()
        if not translated_handle:
            continue
        dedupe = (source_local_ref, translated_handle)
        if dedupe in seen:
            continue
        seen.add(dedupe)
        rows.append(
            {
                "original_handle": original,
                "translated_handle": translated_handle,
                "display_label": str(match.get("display_label", "")).strip() or original,
                "translation_basis": basis,
                "translation_scope": "local_ref",
                "translation_source_local_ref": source_local_ref,
                "translation_confidence": _translation_confidence(basis),
            }
        )
    return rows[:12]


def _iter_translation_candidates(metadata: Dict[str, object]) -> Sequence[tuple[str, str]]:
    rows: List[tuple[str, str]] = []
    bundle = dict(metadata.get("anchor_bundle", {}) or {})
    for item in list(bundle.get("representative_anchors", []) or []):
        label = str(item.get("display_label", "")).strip()
        key = str(item.get("canonical_key", "")).strip()
        if label:
            rows.append((label, "representative_anchor"))
        if key:
            rows.append((key.replace("_", " "), "representative_anchor_key"))
    for item in list(bundle.get("supporting_anchors", []) or []):
        label = str(item).strip()
        if label:
            rows.append((label, "supporting_anchor"))
    short_label = str((metadata.get("transformable_handles", {}) or {}).get("short_label", "")).strip()
    if short_label:
        rows.append((short_label, "short_label"))
    return rows


def _translation_confidence(basis: str) -> float:
    if basis == "representative_anchor_key":
        return 0.86
    if basis == "representative_anchor":
        return 0.8
    if basis == "supporting_anchor":
        return 0.72
    return 0.6


def _match_alias(value: str) -> Dict[str, object] | None:
    normalized = _normalize(value)
    if not normalized:
        return None
    for row in _alias_rows():
        aliases = [str(alias) for alias in row.get("aliases", [])]
        alias_norms = {_normalize(alias) for alias in aliases}
        alias_norms.add(_normalize(str(row.get("display_label", ""))))
        alias_norms.add(_normalize(str(row.get("canonical_key", "")).replace("_", " ")))
        if normalized in alias_norms:
            return row
    return None


@lru_cache(maxsize=1)
def _alias_rows() -> List[Dict[str, object]]:
    try:
        return list(json.loads(ALIAS_DICTIONARY_PATH.read_text(encoding="utf-8")))
    except Exception:
        return []


def _normalize(value: str) -> str:
    lowered = value.strip().lower()
    lowered = lowered.replace("_", " ").replace("-", " ").replace("/", " ")
    lowered = re.sub(r"\s+", " ", lowered)
    return lowered.strip()
