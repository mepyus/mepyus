from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def classify_entry_state(
    classifier_path: Path,
    signal_taxonomy_path: Path,
    current_hint: Dict[str, Any] | None,
    reentry_prebias: Dict[str, Any] | None = None,
    requested_outcome: str = "",
) -> Dict[str, Any]:
    classifier_payload = load_json(classifier_path)
    taxonomy_payload = load_json(signal_taxonomy_path)
    signal_lookup = {
        str(signal.get("signal_kind") or ""): dict(signal)
        for signal in taxonomy_payload.get("signals", [])
    }

    target_family_ids = _collect_ordered_ids(
        reentry_prebias,
        current_hint,
        reentry_key="reentry_family_ids",
        hint_key="candidate_family_ids",
    )
    target_projection_ids = _collect_ordered_ids(
        reentry_prebias,
        current_hint,
        reentry_key="reentry_projection_ids",
        hint_key="candidate_projection_ids",
    )
    target_route_ids = _collect_ordered_ids(
        reentry_prebias,
        current_hint,
        reentry_key="reentry_route_ids",
        hint_key="candidate_route_ids",
    )

    scored_rules: List[Dict[str, Any]] = []
    for rule in classifier_payload.get("classifier_rules", []):
        rule_requested_outcome = str(rule.get("requested_outcome") or "")
        if requested_outcome:
            if rule_requested_outcome and rule_requested_outcome != requested_outcome:
                continue
        elif rule_requested_outcome:
            if not _projection_requires_requested_outcome(
                target_projection_ids,
                target_route_ids,
                rule_requested_outcome,
            ):
                continue

        score = _score_rule(rule, target_family_ids, target_projection_ids, target_route_ids)
        if score <= 0:
            continue

        signal_kind = str(rule.get("signal_kind") or "")
        signal_entry = signal_lookup.get(signal_kind, {})
        scored_rules.append(
            {
                "rule": dict(rule),
                "score": score,
                "signal_entry": signal_entry,
            }
        )

    scored_rules.sort(
        key=lambda item: (
            item["score"],
            1 if item["rule"].get("requested_outcome") else 0,
        ),
        reverse=True,
    )
    selected = scored_rules[0] if scored_rules else None

    return {
        "classification_mode": "rule_reverse_match",
        "target_family_ids": target_family_ids,
        "target_projection_ids": target_projection_ids,
        "target_route_ids": target_route_ids,
        "requested_outcome": requested_outcome or "",
        "matched_rule_count": len(scored_rules),
        "matched_rule_ids": [item["rule"].get("rule_id") for item in scored_rules],
        "inferred_signal_kind": str((selected or {}).get("rule", {}).get("signal_kind") or "") or None,
        "inferred_family_rooted_alias": str(
            (selected or {}).get("signal_entry", {}).get("family_rooted_alias") or ""
        )
        or None,
        "selected_rule_id": str((selected or {}).get("rule", {}).get("rule_id") or "") or None,
        "selected_family_id": str((selected or {}).get("rule", {}).get("preferred_family_id") or "") or None,
        "selected_projection_id": str((selected or {}).get("rule", {}).get("preferred_projection_id") or "") or None,
        "selected_route_id": str((selected or {}).get("rule", {}).get("initial_route_id") or "") or None,
        "selected_requested_outcome": str((selected or {}).get("rule", {}).get("requested_outcome") or "") or None,
        "selected_confidence": str((selected or {}).get("rule", {}).get("confidence") or "") or None,
        "classification_reason": list((selected or {}).get("rule", {}).get("classification_reason") or []),
        "selection_trace": _build_selection_trace(selected, target_family_ids, target_projection_ids, target_route_ids),
    }


def _collect_ordered_ids(
    reentry_prebias: Dict[str, Any] | None,
    current_hint: Dict[str, Any] | None,
    reentry_key: str,
    hint_key: str,
) -> List[str]:
    ordered: List[str] = []
    for value in list((reentry_prebias or {}).get(reentry_key) or []):
        if value and value not in ordered:
            ordered.append(str(value))
    for value in list((current_hint or {}).get(hint_key) or []):
        if value and value not in ordered:
            ordered.append(str(value))
    return ordered


def _score_rule(
    rule: Dict[str, Any],
    target_family_ids: List[str],
    target_projection_ids: List[str],
    target_route_ids: List[str],
) -> int:
    family_id = str(rule.get("preferred_family_id") or "")
    projection_id = str(rule.get("preferred_projection_id") or "")
    route_id = str(rule.get("initial_route_id") or "")
    score = 0
    if family_id and family_id in target_family_ids:
        score += 3
    if projection_id and projection_id in target_projection_ids:
        score += 4
    if route_id and route_id in target_route_ids:
        score += 5
    if family_id and projection_id and family_id in target_family_ids and projection_id in target_projection_ids:
        score += 3
    if family_id and route_id and family_id in target_family_ids and route_id in target_route_ids:
        score += 2
    return score


def _projection_requires_requested_outcome(
    target_projection_ids: List[str],
    target_route_ids: List[str],
    requested_outcome: str,
) -> bool:
    if requested_outcome == "operator_explanation":
        return "proj_transition_operator_readout" in target_projection_ids or "route_readonly_board" in target_route_ids
    return False


def _build_selection_trace(
    selected: Dict[str, Any] | None,
    target_family_ids: List[str],
    target_projection_ids: List[str],
    target_route_ids: List[str],
) -> List[str]:
    if not selected:
        return ["no classifier rule matched the current target family/projection/route set"]
    rule = selected["rule"]
    trace = [
        f"target families={target_family_ids}",
        f"target projections={target_projection_ids}",
        f"target routes={target_route_ids}",
        f"selected {rule.get('rule_id')} by reverse-matching classifier preferences against current entry state",
    ]
    if rule.get("requested_outcome"):
        trace.append(
            f"requested outcome override matched from current state: {rule.get('requested_outcome')}"
        )
    return trace
