from __future__ import annotations

from collections import Counter
from typing import Any


ROLE_KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    ("principle", ("principle", "philosophy", "core", "thesis", "why")),
    ("directive", ("directive", "instruction", "must", "should", "do not", "rule")),
    ("validation", ("validation", "verify", "check", "acceptance", "test")),
    ("hold", ("hold", "caution", "risk", "warning", "restriction", "avoid")),
    ("contrast", ("contrast", "difference", "vs", "however", "but", "instead")),
    ("adoption", ("adoption", "apply", "use", "bring", "borrow", "adopt")),
    ("handoff", ("handoff", "next", "routing", "route", "team", "lane")),
    ("context", ("context", "background", "source", "purpose", "scope")),
]

ORDER_HINTS: list[tuple[str, tuple[str, ...]]] = [
    ("input_to_processing_to_result", ("input", "process", "result")),
    ("explanation_to_directive_to_validation", ("explanation", "directive", "validation")),
    ("requirement_to_design_to_execution", ("requirement", "design", "execution")),
    ("criteria_to_exception_to_hold", ("criteria", "exception", "hold")),
]


def _normalize(text: str) -> str:
    return " ".join((text or "").strip().lower().split())


def _infer_role(text: str, unit_type: str) -> str:
    lowered = _normalize(text)
    for role, keywords in ROLE_KEYWORDS:
        if any(keyword in lowered for keyword in keywords):
            return role
    if "heading" in unit_type:
        return "context"
    if "list" in unit_type:
        return "directive"
    return "context"


def _infer_ordering_basis(unit_texts: list[str]) -> str:
    corpus = " ".join(_normalize(text) for text in unit_texts)
    for label, keywords in ORDER_HINTS:
        if all(keyword in corpus for keyword in keywords):
            return label
    numbered = sum(1 for text in unit_texts if text.strip().startswith(("1.", "2.", "3.", "4.", "5.")))
    if numbered >= 2:
        return "ordered_enumeration"
    return "progressive_document_order"


def _infer_relation(prev_role: str, next_role: str) -> str:
    if prev_role == "context" and next_role in {"directive", "principle"}:
        return "grounds"
    if prev_role in {"principle", "directive"} and next_role == "validation":
        return "validated_by"
    if next_role == "hold":
        return "qualified_by"
    if next_role == "contrast":
        return "contrasted_by"
    if next_role == "handoff":
        return "routes_to"
    return "follows"


def _human_gloss(text: str) -> str:
    cleaned = " ".join(text.replace("\n", " ").split())
    if len(cleaned) <= 140:
        return cleaned
    return cleaned[:137].rstrip() + "..."


def build_gmd_native_read(
    *,
    doc_ref: str,
    source_manifest: dict[str, Any],
    split_units: list[dict[str, Any]],
    processing_trace: dict[str, Any],
) -> dict[str, Any]:
    unit_texts = [str(unit.get("text_excerpt") or unit.get("start_ref") or "") for unit in split_units]
    ordering_basis = _infer_ordering_basis(unit_texts)
    unit_type_counts = Counter(str(unit.get("unit_type") or "unknown") for unit in split_units)
    dominant_unit_type = unit_type_counts.most_common(1)[0][0] if unit_type_counts else "unknown"

    unit_roles: list[dict[str, Any]] = []
    relation_candidates: list[dict[str, Any]] = []
    provisional_line_blocks: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []

    for idx, unit in enumerate(split_units):
        unit_id = str(unit.get("unit_id") or f"unit_{idx + 1:03d}")
        text = str(unit.get("text_excerpt") or unit.get("start_ref") or "")
        unit_type = str(unit.get("unit_type") or "unknown")
        role_type = _infer_role(text, unit_type)
        unit_roles.append(
            {
                "unit_id": unit_id,
                "role_type": role_type,
                "function_in_source": _human_gloss(text),
                "upstream": split_units[idx - 1].get("unit_id") if idx > 0 else None,
                "downstream": split_units[idx + 1].get("unit_id") if idx + 1 < len(split_units) else None,
            }
        )

        if idx + 1 < len(split_units):
            next_unit = split_units[idx + 1]
            next_text = str(next_unit.get("text_excerpt") or next_unit.get("start_ref") or "")
            next_role = _infer_role(next_text, str(next_unit.get("unit_type") or "unknown"))
            relation_candidates.append(
                {
                    "from_unit_id": unit_id,
                    "to_unit_id": str(next_unit.get("unit_id") or f"unit_{idx + 2:03d}"),
                    "relation_type": _infer_relation(role_type, next_role),
                }
            )

        preserves = []
        if unit.get("start_ref"):
            preserves.append(f"start_ref={unit['start_ref']}")
        if unit.get("end_ref"):
            preserves.append(f"end_ref={unit['end_ref']}")
        if unit.get("source_segment_ids"):
            preserves.append(f"source_segments={len(unit.get('source_segment_ids') or [])}")

        provisional_line_blocks.append(
            {
                "unit_id": unit_id,
                "provisional_line": _human_gloss(text),
                "human_gloss": _human_gloss(text),
                "what_it_preserves": preserves,
                "what_it_omits": [
                    "full paragraph-level nuance omitted",
                    "cross-unit relation must be read with adjacent units",
                ],
                "family_position": idx,
            }
        )

        if role_type == "context" and len(text) > 280:
            unresolved.append(
                {
                    "unit_id": unit_id,
                    "ambiguity": "long_context_block",
                    "forced_mapping": "context role assigned conservatively",
                    "pending_interpretation": "may contain multiple roles that need later reread",
                }
            )

    semantic_commentary = {
        "source_summary": f"{source_manifest.get('label') or doc_ref} is being preserved as a structured source before VectorFL-specific line completion.",
        "structure_summary": f"The document currently reads as {ordering_basis} with {len(split_units)} units, dominated by {dominant_unit_type}.",
        "why_this_structure_matters": "This native read keeps segmentation basis, role hints, and relation clues available before line translation and internal recall.",
        "processing_context": processing_trace.get("notes") or "load -> detect -> split -> summary",
    }

    translation_ready_material = {
        "source_block": {
            "source_type": source_manifest.get("input_kind") or "unknown",
            "source_name": source_manifest.get("label") or doc_ref,
            "source_unit": dominant_unit_type,
            "source_context": source_manifest.get("detected_profile") or "unknown",
            "why_this_unit_matters": "It preserves native document structure before VectorFL mapping.",
        },
        "role_block": unit_roles[:8],
        "provisional_line_block": provisional_line_blocks[:8],
        "family_block": {
            "related_lines": [row["unit_id"] for row in provisional_line_blocks[:8]],
            "supporting_records": [doc_ref],
            "conflicting_records": [],
            "expandable_records": [str(source_manifest.get("source_path") or doc_ref)],
            "family_position": "native_document_sequence",
        },
        "use_block": {
            "usable_for_search": True,
            "usable_for_adoption": True,
            "usable_for_page_design": True,
            "usable_for_handoff": True,
            "next_team_or_lane": "translation_first",
        },
        "uncertainty_block": unresolved[:8],
    }

    return {
        "doc_ref": doc_ref,
        "gmd_native_read": {
            "segmentation_basis": {
                "split_mode_used": source_manifest.get("split_mode_used") or processing_trace.get("split_mode_used"),
                "dominant_unit_type": dominant_unit_type,
                "unit_type_distribution": dict(unit_type_counts),
            },
            "ordering_basis": ordering_basis,
            "grouping_logic": "adjacent_units_in_native_document_order",
            "unit_role_hints": unit_roles,
            "relation_clues": relation_candidates,
            "unresolved_structure": unresolved,
        },
        "semantic_commentary": semantic_commentary,
        "translation_ready_material": translation_ready_material,
        "uncertainty_loss_log": {
            "ambiguity_count": len(unresolved),
            "forced_mapping_count": len(unresolved),
            "dropped_nuance": ["cross-paragraph rhetorical nuance is not fully preserved in single-unit glosses"],
            "pending_interpretation": [row["unit_id"] for row in unresolved],
        },
    }
