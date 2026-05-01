"""Bounded artifact family pairing helpers for Phase 1.10."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from structured_helpers import asset_kind_for_path
from identity_helpers import read_identity_anchor

MAX_PAIR_UNITS = 4


def _normalize_stem(path: str) -> str:
    p = Path(path)
    stem = p.stem.lower()
    stem = re.sub(r"phase1_\d+", "phase1_x", stem)
    stem = re.sub(r"_v\d+\b", "_vx", stem)
    stem = re.sub(r"\d{8}t\d{6}z", "timestamp", stem)
    stem = re.sub(r"\d{4}-\d{2}-\d{2}", "date", stem)
    return f"{p.parent.as_posix().lower()}::{stem}"


def _order_key(path: str) -> Tuple[int, int, int, str]:
    stem = Path(path).stem.lower()
    phase_match = re.search(r"phase1_(\d+)", stem)
    run_match = re.search(r"run_(\d+)", stem)
    version_match = re.search(r"_v(\d+)\b", stem)
    phase = int(phase_match.group(1)) if phase_match else -1
    run = int(run_match.group(1)) if run_match else -1
    version = int(version_match.group(1)) if version_match else -1
    return (phase, run, version, path)


def _basis(before_path: str, after_path: str, family_key: str) -> Tuple[str, str, str]:
    before_stem = Path(before_path).stem.lower()
    after_stem = Path(after_path).stem.lower()
    before_dir = Path(before_path).parent.as_posix()
    after_dir = Path(after_path).parent.as_posix()
    if re.search(r"phase1_\d+_run_\d+", before_stem) and re.search(r"phase1_\d+_run_\d+", after_stem):
        return ("shared_run_stem", "strong_pair", "phase/run markers provide before/after ordering inside the same normalized family.")
    if re.search(r"_v\d+\b", before_stem) and re.search(r"_v\d+\b", after_stem):
        return ("shared_contract_family", "strong_pair", "version markers provide before/after ordering inside the same contract family.")
    if before_dir == after_dir and family_key:
        return ("shared_stem", "plausible_pair", "same directory and normalized stem suggest a family relation.")
    return ("selected_order_fallback", "weak_pair", "no strong family marker was found; selected order is retained only as fallback.")


def _why_this_pair(before_path: str, after_path: str, basis: str, confidence: str) -> str:
    return (
        f"Selected {before_path} -> {after_path} by {basis}. "
        f"Pair confidence is {confidence}; timestamp or discovery order is not treated as the sole basis."
    )


def _identity_link(before_identity: Dict[str, Any], after_identity: Dict[str, Any]) -> Tuple[bool, str]:
    same_role = before_identity.get("artifact_role") == after_identity.get("artifact_role")
    same_slot = before_identity.get("artifact_slot") == after_identity.get("artifact_slot")
    same_family = before_identity.get("family_key") == after_identity.get("family_key")
    if after_identity.get("prior_artifact_ref") and after_identity.get("prior_artifact_ref") == before_identity.get("artifact_id"):
        return True, "explicit_prior_ref"
    if same_family and same_role and same_slot:
        return True, "embedded_same_family_role_slot"
    if same_role and same_slot:
        return True, "same_role_same_slot"
    return False, "identity_unconfirmed"


def _identity_adjusted_confidence(pair_confidence: str, before_identity: Dict[str, Any], after_identity: Dict[str, Any]) -> str:
    shared, _ = _identity_link(before_identity, after_identity)
    before_conf = before_identity.get("identity_confidence")
    after_conf = after_identity.get("identity_confidence")
    if shared and before_conf == "strong_identity" and after_conf == "strong_identity":
        return pair_confidence
    if pair_confidence == "strong_pair" and (before_conf == "weak_identity" or after_conf == "weak_identity"):
        return "plausible_pair"
    return pair_confidence


def pair_json_assets_with_metadata(paths: List[str]) -> List[Dict[str, Any]]:
    json_paths = []
    seen = set()
    for path in paths:
        if path.endswith(".json") and Path(path).exists() and path not in seen:
            json_paths.append(path)
            seen.add(path)
    groups: Dict[str, List[str]] = {}
    for path in json_paths:
        groups.setdefault(_normalize_stem(path), []).append(path)

    units: List[Dict[str, Any]] = []
    for family_key, family_paths in sorted(groups.items()):
        if len(family_paths) < 2:
            continue
        ordered = sorted(family_paths, key=_order_key)
        before_path, after_path = ordered[-2], ordered[-1]
        if before_path == after_path:
            continue
        basis, confidence, note = _basis(before_path, after_path, family_key)
        before_identity = read_identity_anchor(before_path)
        after_identity = read_identity_anchor(after_path)
        confidence = _identity_adjusted_confidence(confidence, before_identity, after_identity)
        shared_identity, lineage_link_type = _identity_link(before_identity, after_identity)
        rejected = [path for path in ordered if path not in {before_path, after_path}][:4]
        units.append(
            {
                "source_ref_before": before_path,
                "source_ref_after": after_path,
                "asset_kind": asset_kind_for_path(after_path),
                "family_key": family_key,
                "lineage_hint": f"{_order_key(before_path)} -> {_order_key(after_path)}",
                "pairing_basis": basis,
                "pair_confidence": confidence,
                "ordering_basis": "phase_or_version_marker" if confidence == "strong_pair" else "family_then_path_order",
                "why_this_pair": _why_this_pair(before_path, after_path, basis, confidence),
                "rejected_pair_candidates": rejected,
                "ambiguity_note": "" if confidence == "strong_pair" else note,
                "identity_confidence_before": before_identity.get("identity_confidence", "weak_identity"),
                "identity_confidence_after": after_identity.get("identity_confidence", "weak_identity"),
                "shared_family_confirmed": shared_identity,
                "lineage_link_type": lineage_link_type,
                "identity_risk_note": "" if shared_identity else "Artifact identity anchors did not independently confirm the family link.",
                "pairing_identity_support_refs": [
                    before_identity.get("artifact_id", before_path),
                    after_identity.get("artifact_id", after_path),
                ],
            }
        )

    if not units and len(json_paths) >= 2:
        before_path, after_path = sorted(json_paths)[:2]
        before_identity = read_identity_anchor(before_path)
        after_identity = read_identity_anchor(after_path)
        shared_identity, lineage_link_type = _identity_link(before_identity, after_identity)
        units.append(
            {
                "source_ref_before": before_path,
                "source_ref_after": after_path,
                "asset_kind": asset_kind_for_path(after_path),
                "family_key": "fallback:selected_json_order",
                "lineage_hint": "no normalized family with at least two members",
                "pairing_basis": "selected_order_fallback",
                "pair_confidence": "weak_pair",
                "ordering_basis": "path_order_fallback",
                "why_this_pair": _why_this_pair(before_path, after_path, "selected_order_fallback", "weak_pair"),
                "rejected_pair_candidates": sorted(json_paths)[2:6],
                "ambiguity_note": "Comparison pair is weak because no same-family lineage was confirmed.",
                "identity_confidence_before": before_identity.get("identity_confidence", "weak_identity"),
                "identity_confidence_after": after_identity.get("identity_confidence", "weak_identity"),
                "shared_family_confirmed": shared_identity,
                "lineage_link_type": lineage_link_type,
                "identity_risk_note": "Weak fallback pair; identity anchors did not provide a same-family comparison.",
                "pairing_identity_support_refs": [
                    before_identity.get("artifact_id", before_path),
                    after_identity.get("artifact_id", after_path),
                ],
            }
        )
    return units[:MAX_PAIR_UNITS]


def summarize_pairing_units(units: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "strong_pair": sum(1 for unit in units if unit.get("pair_confidence") == "strong_pair"),
        "plausible_pair": sum(1 for unit in units if unit.get("pair_confidence") == "plausible_pair"),
        "weak_pair": sum(1 for unit in units if unit.get("pair_confidence") == "weak_pair"),
        "comparison_candidate_count": len(units),
        "family_keys": sorted({unit.get("family_key", "") for unit in units if unit.get("family_key")})[:8],
        "pairing_basis": sorted({unit.get("pairing_basis", "") for unit in units if unit.get("pairing_basis")}),
        "rejected_pair_candidate_count": sum(len(unit.get("rejected_pair_candidates", [])) for unit in units),
        "strong_identity_pair": sum(
            1
            for unit in units
            if unit.get("identity_confidence_before") == "strong_identity"
            and unit.get("identity_confidence_after") == "strong_identity"
        ),
        "weak_identity_pair": sum(
            1
            for unit in units
            if unit.get("identity_confidence_before") == "weak_identity"
            or unit.get("identity_confidence_after") == "weak_identity"
        ),
        "shared_family_confirmed": sum(1 for unit in units if unit.get("shared_family_confirmed")),
    }
