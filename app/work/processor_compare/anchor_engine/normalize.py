from __future__ import annotations

import re
from typing import Dict, Tuple

from .dictionaries import acronym_whitelist, alias_lookup, ending_suffixes, particle_suffixes


PUNCT_RE = re.compile(r"^[\s'\"“”‘’\(\)\[\]\{\}<>,.:;!?/\-–—]+|[\s'\"“”‘’\(\)\[\]\{\}<>,.:;!?/\-–—]+$")
SPACE_RE = re.compile(r"\s+")
DELIM_RE = re.compile(r"[-/]+")
VERB_NOMINALIZE = {
    "추적한다": "추적",
    "연결된다": "연결",
    "승격한다": "승격",
    "정규화한다": "정규화",
}


def normalize_candidate_text(text: str) -> Tuple[str, str, str, str, bool]:
    surface = surface_clean(text)
    reduced = reduce_korean_surface(surface)
    lowered = SPACE_RE.sub(" ", reduced).strip().lower()
    lowered = DELIM_RE.sub(" ", lowered)
    lowered = SPACE_RE.sub(" ", lowered).strip()
    alias = alias_lookup().get(lowered)
    if alias:
        return surface, reduced, lowered, str(alias["canonical_key"]), True
    return surface, reduced, lowered, heuristic_canonicalize(reduced), False


def canonical_display_label(surface_text: str, reduced_text: str, normalized_text: str, canonical_key: str) -> str:
    alias = alias_lookup().get(normalized_text)
    if alias:
        return str(alias["display_label"])
    if surface_text in acronym_whitelist():
        return surface_text
    return reduced_text.strip() or canonical_key.replace("_", " ")


def surface_clean(text: str) -> str:
    cleaned = PUNCT_RE.sub("", text.strip())
    cleaned = SPACE_RE.sub(" ", cleaned)
    return cleaned.strip()


def reduce_korean_surface(text: str) -> str:
    value = text.strip()
    if value in VERB_NOMINALIZE:
        return VERB_NOMINALIZE[value]
    for suffix in ending_suffixes():
        if value.endswith(suffix) and len(value) > len(suffix) + 1:
            value = value[: -len(suffix)]
            break
    parts = value.split()
    reduced_parts = []
    for part in parts:
        if part in particle_suffixes():
            continue
        reduced = part
        for suffix in particle_suffixes():
            if reduced.endswith(suffix) and len(reduced) > len(suffix) + 1:
                reduced = reduced[: -len(suffix)]
                break
        if reduced and reduced not in particle_suffixes():
            reduced_parts.append(reduced)
    value = " ".join(part for part in reduced_parts if part)
    for suffix in particle_suffixes():
        if value.endswith(suffix) and len(value) > len(suffix) + 1:
            value = value[: -len(suffix)]
            break
    return value.strip()


def heuristic_canonicalize(text: str) -> str:
    value = DELIM_RE.sub(" ", text.strip().lower())
    value = SPACE_RE.sub(" ", value).strip()
    return value.replace(" ", "_")


def normalize_record(candidate: Dict[str, object]) -> Dict[str, object]:
    surface_text, reduced_text, normalized_text, canonical_key, alias_matched = normalize_candidate_text(str(candidate["candidate_text"]))
    record = dict(candidate)
    record["surface_text"] = surface_text
    record["reduced_text"] = reduced_text
    record["normalized_text"] = normalized_text
    record["canonical_key"] = canonical_key
    record["alias_matched"] = alias_matched
    record["display_label"] = canonical_display_label(surface_text, reduced_text, normalized_text, canonical_key)
    return record
