from __future__ import annotations

from datetime import datetime
from typing import Mapping


DEFAULT_EXTERNAL_LABELS = {
    "docrole": "memo",
    "runmode": "ingest_only",
    "priority": "normal",
}


def _allowed_values(alias_map: Mapping[str, Mapping[str, str]], section: str) -> set[str]:
    return set(alias_map.get(section, {}).values())


def _normalize_single(
    section: str,
    raw_value: str | None,
    alias_map: Mapping[str, Mapping[str, str]],
    default: str,
) -> str:
    if not raw_value:
        return default
    value = raw_value.strip()
    normalized = alias_map.get(section, {}).get(value)
    if normalized is None:
        normalized = alias_map.get(section, {}).get(value.lower())
    if normalized is None:
        lowered = value.lower()
        normalized = lowered if lowered in _allowed_values(alias_map, section) else default
    return normalized


def normalize_external_labels(
    raw_markers: Mapping[str, str],
    alias_map: Mapping[str, Mapping[str, str]],
    defaults: Mapping[str, str] | None = None,
) -> dict[str, str]:
    merged_defaults = {**DEFAULT_EXTERNAL_LABELS, **(defaults or {})}
    return {
        "docrole": _normalize_single("docrole", raw_markers.get("DOCROLE"), alias_map, merged_defaults["docrole"]),
        "runmode": _normalize_single("runmode", raw_markers.get("RUNMODE"), alias_map, merged_defaults["runmode"]),
        "priority": _normalize_single("priority", raw_markers.get("PRIORITY"), alias_map, merged_defaults["priority"]),
    }


def build_core_intake_labels(
    external_labels: Mapping[str, str],
    *,
    source_session: str,
    input_class: str = "structured_internal_doc",
) -> dict[str, object]:
    runmode = external_labels["runmode"]
    if runmode in {"ingest_then_execute", "execute_only"}:
        processing_profile = "execution_coupled"
        execution_linkable = True
    elif runmode == "reference_only":
        processing_profile = "reference_only"
        execution_linkable = False
    else:
        processing_profile = "minimal_preprocess"
        execution_linkable = False
    return {
        "input_class": input_class,
        "processing_profile": processing_profile,
        "material_grade": "grade_a",
        "role": external_labels["docrole"],
        "execution_linkable": execution_linkable,
        "source_session": source_session,
    }


def build_label_packet(
    *,
    doc_id: str,
    doc_ref: str,
    external_labels: Mapping[str, str],
    core_labels: Mapping[str, object],
) -> dict[str, object]:
    return {
        "label_packet": {
            "doc_id": doc_id,
            "doc_ref": doc_ref,
            "external_labels": dict(external_labels),
            "core_labels": dict(core_labels),
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "packet_kind": "structured_doc_intake_label_packet",
        }
    }
