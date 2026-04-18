from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Tuple


def detect_flow_candidates(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    stage_sequences: Dict[Tuple[str, ...], List[str]] = defaultdict(list)
    family_handoffs: Dict[Tuple[str, ...], List[str]] = defaultdict(list)
    route_edges: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    reentry_hooks: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    residue_tendencies: Dict[Tuple[str, str], List[str]] = defaultdict(list)

    for record in records:
        run_id = str(record.get("run_id") or "")
        family_sequence = tuple(record.get("family_sequence") or [])
        route_sequence = tuple(record.get("route_sequence") or [])
        reentry_rule_ids = list(record.get("reentry_rule_ids") or [])
        previous_hint = dict(record.get("previous_hint") or {})
        previous_residue_bias = str(previous_hint.get("residue_reentry_bias") or "")
        final_family = str(record.get("final_family") or "")

        stage_seq = tuple(step.get("stage") or "" for step in record.get("ordered_transition_path") or [])
        if stage_seq:
            stage_sequences[stage_seq].append(run_id)
        if family_sequence:
            family_handoffs[family_sequence].append(run_id)
        for left, right in zip(route_sequence, route_sequence[1:]):
            route_edges[(left, right)].append(run_id)
        for rule_id in reentry_rule_ids:
            reentry_hooks[(rule_id, final_family)].append(run_id)
        if previous_residue_bias and final_family:
            residue_tendencies[(previous_residue_bias, final_family)].append(run_id)

    candidates: List[Dict[str, Any]] = []
    candidates.extend(_make_candidates("stage_sequence", stage_sequences))
    candidates.extend(_make_candidates("family_handoff", family_handoffs))
    candidates.extend(_make_candidates("route_edge", route_edges))
    candidates.extend(_make_candidates("reentry_hook", reentry_hooks))
    candidates.extend(_make_candidates("residue_to_next_family", residue_tendencies))
    candidates.sort(key=lambda item: (item["support_count"], item["pattern_type"]), reverse=True)

    return {
        "schema_version": "flow_candidate_detection_v0",
        "record_count": len(records),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }


def _make_candidates(
    pattern_type: str,
    grouped_runs: Dict[Tuple[str, ...] | Tuple[str, str], List[str]],
) -> List[Dict[str, Any]]:
    candidates: List[Dict[str, Any]] = []
    for index, (sequence, supporting_runs) in enumerate(grouped_runs.items(), start=1):
        unique_runs = _dedupe_keep_order(supporting_runs)
        if len(unique_runs) < 2:
            continue
        candidates.append(
            {
                "candidate_pattern_id": f"{pattern_type}_{index:03d}",
                "pattern_type": pattern_type,
                "observed_sequence": list(sequence),
                "supporting_runs": unique_runs,
                "support_count": len(unique_runs),
                "strength_level": _strength_level(len(unique_runs)),
                "ambiguity_warning": _ambiguity_warning(pattern_type, sequence, unique_runs),
            }
        )
    return candidates


def _strength_level(support_count: int) -> str:
    if support_count >= 4:
        return "strong"
    if support_count >= 3:
        return "medium"
    return "weak"


def _ambiguity_warning(
    pattern_type: str,
    sequence: Tuple[str, ...] | Tuple[str, str],
    supporting_runs: List[str],
) -> str | None:
    if pattern_type in {"stage_sequence", "family_handoff"} and len(sequence) <= 1:
        return "single-step repetition is too weak to treat as future flow evidence"
    if pattern_type == "route_edge" and len(sequence) == 2 and sequence[0] == sequence[1]:
        return "same route repeated across runs may mix different family contexts; do not treat route repetition alone as promotable flow"
    if len(supporting_runs) == 2:
        return "only two supporting runs; treat as weak candidate rather than promotable flow"
    return None


def _dedupe_keep_order(values: List[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered
