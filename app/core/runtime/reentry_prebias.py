from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_hint_by_artifact(hints_manifest_path: Path, artifact_path: Path) -> Dict[str, Any] | None:
    payload = load_json(hints_manifest_path)
    artifact_ref = str(artifact_path)
    for hint in payload.get("hints", []):
        if str(hint.get("artifact_path") or "") == artifact_ref:
            return dict(hint)
    return None


def build_reentry_prebias(
    previous_hint: Dict[str, Any] | None,
    new_hint: Dict[str, Any] | None,
    residue_rules_path: Path,
    question_shift: str,
) -> Dict[str, Any]:
    previous_residue_bias = str((previous_hint or {}).get("residue_reentry_bias") or "")
    rules_payload = load_json(residue_rules_path)
    matched_rules: List[Dict[str, Any]] = []
    for rule in rules_payload.get("rules", []):
        if str(rule.get("source_residue_bias") or "") != previous_residue_bias:
            continue
        if str(rule.get("question_shift") or "") != question_shift:
            continue
        matched_rules.append(dict(rule))

    preferred_family_ids: List[str] = []
    preferred_projection_ids: List[str] = []
    preferred_route_ids: List[str] = []
    strengths: List[str] = []
    reasons: List[str] = []

    for rule in matched_rules:
        preferred_family_ids.extend(rule.get("preferred_family_ids") or [])
        preferred_projection_ids.extend(rule.get("preferred_projection_ids") or [])
        preferred_route_ids.extend(rule.get("preferred_route_ids") or [])
        if rule.get("strength"):
            strengths.append(str(rule["strength"]))
        reasons.append(
            f"matched residue rule {rule.get('rule_id')} from {previous_residue_bias} with question_shift={question_shift}"
        )

    existing_new_family_ids = list((new_hint or {}).get("candidate_family_ids") or [])
    existing_new_projection_ids = list((new_hint or {}).get("candidate_projection_ids") or [])
    existing_new_route_ids = list((new_hint or {}).get("candidate_route_ids") or [])

    return {
        "previous_residue_bias": previous_residue_bias,
        "question_shift": question_shift,
        "matched_rule_ids": [rule.get("rule_id") for rule in matched_rules],
        "source_hint_family_ids": existing_new_family_ids,
        "source_hint_projection_ids": existing_new_projection_ids,
        "source_hint_route_ids": existing_new_route_ids,
        "residue_rule_family_ids": _dedupe_keep_order(preferred_family_ids),
        "residue_rule_projection_ids": _dedupe_keep_order(preferred_projection_ids),
        "residue_rule_route_ids": _dedupe_keep_order(preferred_route_ids),
        "reentry_family_ids": _dedupe_keep_order(preferred_family_ids + existing_new_family_ids),
        "reentry_projection_ids": _dedupe_keep_order(preferred_projection_ids + existing_new_projection_ids),
        "reentry_route_ids": _dedupe_keep_order(preferred_route_ids + existing_new_route_ids),
        "reentry_strength": strengths[0] if strengths else None,
        "reentry_reason": reasons,
        "new_hint_present": new_hint is not None,
    }


def _dedupe_keep_order(values: List[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered
