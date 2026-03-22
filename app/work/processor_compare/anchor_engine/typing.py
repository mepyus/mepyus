from __future__ import annotations

from typing import Dict

from .dictionaries import alias_lookup, anchor_type_lookup


OBJECT_SUFFIXES = ("engine", "system", "panel", "camera", "viewer", "sdk")
PROCESS_SUFFIXES = ("추출", "정규화", "승격", "전이", "추적", "detection", "pipeline", "normalization", "promotion")
STRUCTURAL_SUFFIXES = ("layer", "field", "boundary", "region", "space", "atlas")


def assign_anchor_type(item: Dict[str, object]) -> Dict[str, object]:
    key = str(item.get("canonical_key", ""))
    label = str(item.get("display_label", ""))
    normalized = str(item.get("normalized_text", ""))

    explicit = anchor_type_lookup().get(key)
    if explicit:
        item["anchor_type"] = explicit
        return item

    alias = alias_lookup().get(normalized)
    if alias and alias.get("anchor_type"):
        item["anchor_type"] = str(alias["anchor_type"])
        return item

    lowered = label.lower()
    if lowered.endswith(OBJECT_SUFFIXES):
        item["anchor_type"] = "object"
    elif lowered.endswith(PROCESS_SUFFIXES):
        item["anchor_type"] = "process"
    elif lowered.endswith(STRUCTURAL_SUFFIXES):
        item["anchor_type"] = "structural"
    else:
        item["anchor_type"] = "semantic"
    return item

