from __future__ import annotations

from typing import Any, Dict, List, Optional


DISPLAY_LABELS = {
    "moderately_open": "moderately open",
    "structured_open_low_emergence": "structured-open / low-emergence",
    "overcompressed_closure_heavy": "overcompressed / closure-heavy",
    "overcompressed_breathing": "overcompressed / breathing",
    "direct_grounded": "direct grounded",
    "partially_grounded": "partially grounded",
    "fallback_grounded": "fallback grounded",
    "empty_ref_risk": "empty-ref risk",
    "question_opening_present": "question opening present",
    "minimal_emergence": "minimal emergence",
    "low_emergence": "low emergence",
    "no_emergence": "no emergence",
    "prepared_scaffold_carryover": "prepared scaffold carryover",
    "hold": "hold",
    "residue": "residue",
    "weak": "weak",
    "fallback": "fallback",
    "blocked": "blocked",
    "breathing": "breathing",
    "traceable": "traceable",
    "partially_traceable": "partially traceable",
    "not_traceable": "not traceable",
}

MATURATION_ORDER = {
    "blocked": 0,
    "fallback": 1,
    "weak": 2,
    "hold": 3,
    "residue": 4,
    "breathing": 5,
}

EMERGENCE_ORDER = {
    "no_emergence": 0,
    "low_emergence": 1,
    "minimal_emergence": 2,
    "question_opening_present": 3,
}

GROUNDING_ORDER = {
    "empty_ref_risk": 0,
    "fallback_grounded": 1,
    "partially_grounded": 2,
    "direct_grounded": 3,
}

CARRYOVER_ORDER = {
    "prepared_scaffold_carryover": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

PACKET_TEXTURE_ORDER = {
    "overcompressed_closure_heavy": 0,
    "overcompressed_breathing": 1,
    "structured_open_low_emergence": 2,
    "moderately_open": 3,
}


def display_label(value: Optional[str]) -> str:
    if not value:
        return "not_available_yet"
    return DISPLAY_LABELS.get(value, value.replace("_", " "))


def apply_state_filters(rows: List[Dict[str, Any]], filters: Dict[str, str]) -> List[Dict[str, Any]]:
    filtered = list(rows)
    for key in [
        "packet_texture",
        "grounding_status",
        "emergence_status",
        "carryover_risk",
        "maturation_state",
    ]:
        value = filters.get(key)
        if value:
            filtered = [row for row in filtered if row.get(key) == value]
    if filters.get("traceable_only") in {"1", "true", "yes"}:
        filtered = [row for row in filtered if row.get("traceability_status") == "traceable"]
    return filtered


def sort_state_rows(rows: List[Dict[str, Any]], sort_by: str) -> List[Dict[str, Any]]:
    if sort_by == "packet_texture":
        return sorted(rows, key=lambda row: (PACKET_TEXTURE_ORDER.get(row.get("packet_texture", ""), 99), row.get("asset_name", "")))
    if sort_by == "maturation_state":
        return sorted(rows, key=lambda row: (MATURATION_ORDER.get(row.get("maturation_state", ""), 99), row.get("asset_name", "")))
    if sort_by == "carryover_risk":
        return sorted(rows, key=lambda row: (CARRYOVER_ORDER.get(row.get("carryover_risk", ""), 99), row.get("asset_name", "")))
    if sort_by == "emergence_status":
        return sorted(rows, key=lambda row: (EMERGENCE_ORDER.get(row.get("emergence_status", ""), 99), row.get("asset_name", "")))
    return sorted(rows, key=lambda row: (row.get("updated_at", ""), row.get("asset_name", "")), reverse=True)


def build_compare_candidates(selected: Optional[Dict[str, Any]], rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not selected:
        return []
    candidates = []
    selected_reasons = set(selected.get("comparison_memory_reason", []))
    selected_blockers = set(selected.get("gate_blocker_summary", []))
    selected_texture = selected.get("packet_texture")
    selected_carryover = selected.get("carryover_risk")
    for row in rows:
        if row.get("asset_id") == selected.get("asset_id"):
            continue
        score = 0
        reasons = []
        if row.get("packet_texture") == selected_texture:
            score += 3
            reasons.append("same_packet_texture")
        if row.get("carryover_risk") == selected_carryover:
            score += 2
            reasons.append("same_carryover_risk")
        overlap_reasons = sorted(selected_reasons & set(row.get("comparison_memory_reason", [])))
        if overlap_reasons:
            score += len(overlap_reasons) * 2
            reasons.extend(overlap_reasons)
        overlap_blockers = sorted(selected_blockers & set(row.get("gate_blocker_summary", [])))
        if overlap_blockers:
            score += len(overlap_blockers)
            reasons.extend(overlap_blockers)
        compressed_pair = {selected_texture, row.get("packet_texture")}
        if compressed_pair <= {"overcompressed_closure_heavy", "overcompressed_breathing"}:
            score += 1
            reasons.append("same_compressed_family")
        if compressed_pair == {"overcompressed_breathing", "moderately_open"}:
            score += 1
            reasons.append("breathing_contrast")
        if score <= 0:
            continue
        candidates.append(
            {
                "asset_id": row.get("asset_id"),
                "asset_name": row.get("asset_name"),
                "score": score,
                "reasons": sorted(set(reasons)),
                "packet_texture": row.get("packet_texture"),
                "maturation_state": row.get("maturation_state"),
            }
        )
    candidates.sort(key=lambda row: (-row["score"], row["asset_name"]))
    return candidates[:4]
