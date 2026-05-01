"""Bounded artifact identity anchor helpers for Phase 1.11/1.12."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, Optional

LEGACY_IDENTITY_MAP = Path("docs/indexes/legacy_artifact_family_identity_map_v0.json")


def _load_legacy_identity_map() -> Dict[str, Any]:
    try:
        data = json.loads(LEGACY_IDENTITY_MAP.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}
    artifacts = data.get("artifacts", {})
    return artifacts if isinstance(artifacts, dict) else {}


def _role_from_path(path: str) -> str:
    path = _workspace_path(path)
    lower = Path(path).name.lower()
    if "question_packet" in lower:
        return "question_packet"
    if "exploration_result" in lower:
        return "exploration_result"
    if "merge_diff_report" in lower:
        return "merge_diff_report"
    if "reingress_record" in lower:
        return "reingress_record"
    if Path(path).as_posix().startswith("runtime/contracts/"):
        return "runtime_contract"
    if path.endswith(".json"):
        return "generated_artifact"
    return "comparison_candidate"


def _run_stem(path: str) -> str:
    path = _workspace_path(path)
    stem = Path(path).stem
    for suffix in ("_question_packet", "_exploration_result", "_merge_diff_report", "_reingress_record"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)]
    return stem


def _phase_label(stem: str) -> str:
    match = re.search(r"phase1_\d+", stem)
    return match.group(0) if match else ""


def _family_key(path: str, role: str) -> str:
    path = _workspace_path(path)
    p = Path(path)
    stem = _run_stem(path).lower()
    stem = re.sub(r"phase1_\d+", "phase1_x", stem)
    stem = re.sub(r"_v\d+\b", "_vx", stem)
    if role in {"question_packet", "exploration_result", "merge_diff_report", "reingress_record"}:
        return f"{p.parent.as_posix().lower()}::{stem}::{role}"
    contract_stem = re.sub(r"_v\d+\b", "_vx", p.stem.lower())
    return f"{p.parent.as_posix().lower()}::{contract_stem}"


def _workspace_path(path: str) -> str:
    p = Path(path)
    if p.is_absolute():
        try:
            return p.resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            return p.as_posix()
    return p.as_posix()


def _artifact_slot(role: str) -> str:
    slots = {
        "question_packet": "run artifact slot",
        "exploration_result": "run artifact slot",
        "merge_diff_report": "report family slot",
        "reingress_record": "run artifact slot",
        "runtime_contract": "contract family slot",
        "generated_artifact": "same logical slot across runs",
    }
    return slots.get(role, "comparison candidate slot")


def build_identity_anchor(
    path: str,
    artifact_role: Optional[str] = None,
    generated_from_ref: str = "",
    prior_artifact_ref: str = "",
    anchor_source: str = "emitted",
) -> Dict[str, Any]:
    path = _workspace_path(path)
    role = artifact_role or _role_from_path(path)
    run_stem = _run_stem(path)
    phase_label = _phase_label(run_stem)
    basis = ["path_plus_role"]
    if generated_from_ref:
        basis.append("generated_from_chain")
    if prior_artifact_ref:
        basis.append("explicit_prior_ref")
    if anchor_source == "inferred_from_path":
        confidence = "plausible_identity" if role else "weak_identity"
    elif phase_label and role:
        confidence = "strong_identity"
    elif role:
        confidence = "plausible_identity"
    else:
        confidence = "weak_identity"
    return {
        "artifact_id": Path(path).stem,
        "artifact_role": role,
        "family_key": _family_key(path, role),
        "lineage_hint": f"{phase_label or 'unknown_phase'}:{run_stem}:{role}",
        "run_stem": run_stem,
        "phase_label": phase_label,
        "artifact_slot": _artifact_slot(role),
        "generated_from_ref": generated_from_ref,
        "prior_artifact_ref": prior_artifact_ref,
        "comparison_ready": role in {"exploration_result", "merge_diff_report", "reingress_record", "runtime_contract", "generated_artifact"},
        "identity_confidence": confidence,
        "identity_basis": basis,
        "identity_anchor_source": anchor_source,
    }


def read_identity_anchor(path: str) -> Dict[str, Any]:
    workspace_path = _workspace_path(path)
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        legacy_anchor = _load_legacy_identity_map().get(workspace_path)
        if isinstance(legacy_anchor, dict):
            anchor = dict(legacy_anchor)
            anchor.setdefault("identity_anchor_source", "legacy_backfill_map")
            return anchor
        return build_identity_anchor(path, "comparison_candidate")
    anchor = data.get("artifact_identity")
    if isinstance(anchor, dict):
        anchor.setdefault("identity_anchor_source", "embedded_marker")
        return anchor
    legacy_anchor = _load_legacy_identity_map().get(workspace_path)
    if isinstance(legacy_anchor, dict):
        anchor = dict(legacy_anchor)
        anchor.setdefault("identity_anchor_source", "legacy_backfill_map")
        return anchor
    return build_identity_anchor(path, anchor_source="inferred_from_path")


def summarize_identity_anchors(anchors: list[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "strong_identity": sum(1 for anchor in anchors if anchor.get("identity_confidence") == "strong_identity"),
        "plausible_identity": sum(1 for anchor in anchors if anchor.get("identity_confidence") == "plausible_identity"),
        "weak_identity": sum(1 for anchor in anchors if anchor.get("identity_confidence") == "weak_identity"),
        "family_keys": sorted({anchor.get("family_key", "") for anchor in anchors if anchor.get("family_key")})[:8],
        "identity_basis": sorted({basis for anchor in anchors for basis in anchor.get("identity_basis", [])}),
        "total": len(anchors),
    }
