from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List
from uuid import uuid4


def infer_source_surface_type(artifact_path: Path) -> str:
    artifact_ref = str(artifact_path)
    if "comparison" in artifact_path.name:
        return "comparison_result"
    if artifact_path.name in {"current_phase.json", "preflight_last_decision.json"}:
        return "phase_surface"
    if artifact_path.name == "index.json" and "engine_state_latest" in artifact_ref:
        return "engine_state_index"
    if "/references/" in artifact_ref:
        return "reference_artifact"
    return "artifact_surface"


def build_execution_trace_record(
    artifact_path: Path,
    current_hint: Dict[str, Any] | None,
    previous_hint: Dict[str, Any] | None,
    reentry_prebias: Dict[str, Any] | None,
    classification: Dict[str, Any] | None,
    question_shift: str = "",
    execution_context: str = "",
) -> Dict[str, Any]:
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    run_id = f"exec_trace_{datetime.now().astimezone().strftime('%Y%m%dT%H%M%S')}_{uuid4().hex[:8]}"

    ordered_transition_path = _build_ordered_transition_path(
        current_hint=current_hint,
        reentry_prebias=reentry_prebias,
        classification=classification,
    )
    family_sequence = [step["family_id"] for step in ordered_transition_path if step.get("family_id")]
    projection_sequence = [step["projection_id"] for step in ordered_transition_path if step.get("projection_id")]
    route_sequence = [step["route_id"] for step in ordered_transition_path if step.get("route_id")]

    residue_notes = _collect_residue_notes(previous_hint, reentry_prebias)
    return {
        "schema_version": "execution_trace_v0",
        "run_id": run_id,
        "timestamp": timestamp,
        "execution_context": execution_context or "prototype_execution_spine_stub",
        "source_artifact": str(artifact_path),
        "source_surface_type": infer_source_surface_type(artifact_path),
        "current_hint": current_hint,
        "previous_hint": previous_hint,
        "reentry_prebias": reentry_prebias,
        "final_family": str((classification or {}).get("selected_family_id") or "") or None,
        "final_projection": str((classification or {}).get("selected_projection_id") or "") or None,
        "final_route": str((classification or {}).get("selected_route_id") or "") or None,
        "classifier_rule_selected": str((classification or {}).get("selected_rule_id") or "") or None,
        "classifier_signal_kind": str((classification or {}).get("inferred_signal_kind") or "") or None,
        "question_shift": question_shift or None,
        "ordered_transition_path": ordered_transition_path,
        "family_sequence": family_sequence,
        "projection_sequence": projection_sequence,
        "route_sequence": route_sequence,
        "reentry_rule_ids": list((reentry_prebias or {}).get("matched_rule_ids") or []),
        "residue_related_notes": residue_notes,
    }


def append_execution_trace(trace_log_path: Path, record: Dict[str, Any]) -> Dict[str, Any]:
    trace_log_path.parent.mkdir(parents=True, exist_ok=True)
    with trace_log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return {
        "trace_log_path": str(trace_log_path),
        "recorded": True,
        "run_id": record.get("run_id"),
    }


def load_trace_records(trace_log_path: Path) -> List[Dict[str, Any]]:
    if not trace_log_path.exists():
        return []
    records: List[Dict[str, Any]] = []
    for line in trace_log_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        records.append(json.loads(line))
    return records


def _build_ordered_transition_path(
    current_hint: Dict[str, Any] | None,
    reentry_prebias: Dict[str, Any] | None,
    classification: Dict[str, Any] | None,
) -> List[Dict[str, Any]]:
    path: List[Dict[str, Any]] = []
    for family_id, projection_id, route_id in zip(
        list((current_hint or {}).get("candidate_family_ids") or []),
        list((current_hint or {}).get("candidate_projection_ids") or []),
        list((current_hint or {}).get("candidate_route_ids") or []),
    ):
        path.append(
            {
                "stage": "current_hint",
                "family_id": family_id,
                "projection_id": projection_id,
                "route_id": route_id,
            }
        )

    reentry_family_ids = list((reentry_prebias or {}).get("reentry_family_ids") or [])
    reentry_projection_ids = list((reentry_prebias or {}).get("reentry_projection_ids") or [])
    reentry_route_ids = list((reentry_prebias or {}).get("reentry_route_ids") or [])
    max_len = max(len(reentry_family_ids), len(reentry_projection_ids), len(reentry_route_ids), 0)
    for index in range(max_len):
        path.append(
            {
                "stage": "reentry_prebias",
                "family_id": reentry_family_ids[index] if index < len(reentry_family_ids) else None,
                "projection_id": reentry_projection_ids[index] if index < len(reentry_projection_ids) else None,
                "route_id": reentry_route_ids[index] if index < len(reentry_route_ids) else None,
            }
        )

    final_family = str((classification or {}).get("selected_family_id") or "") or None
    final_projection = str((classification or {}).get("selected_projection_id") or "") or None
    final_route = str((classification or {}).get("selected_route_id") or "") or None
    if final_family or final_projection or final_route:
        path.append(
            {
                "stage": "final_selection",
                "family_id": final_family,
                "projection_id": final_projection,
                "route_id": final_route,
            }
        )
    return path


def _collect_residue_notes(
    previous_hint: Dict[str, Any] | None,
    reentry_prebias: Dict[str, Any] | None,
) -> List[str]:
    notes: List[str] = []
    previous_residue_bias = str((previous_hint or {}).get("residue_reentry_bias") or "")
    if previous_residue_bias:
        notes.append(f"previous_residue_bias={previous_residue_bias}")
    for rule_id in list((reentry_prebias or {}).get("matched_rule_ids") or []):
        notes.append(f"matched_reentry_rule={rule_id}")
    for reason in list((reentry_prebias or {}).get("reentry_reason") or []):
        notes.append(str(reason))
    return notes
