from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json


PAPER_MANIFEST_PATHS = {
    "codex_handoff": "runtime/manifests/vectorfl_paper_codex_handoff_latest_v0.json",
    "codex_return": "runtime/manifests/vectorfl_paper_codex_return_latest_v0.json",
    "gemini_review": "runtime/manifests/vectorfl_paper_gemini_review_latest_v0.json",
    "supervisor_decision": "runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json",
    "current_slot": "runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json",
    "gate_validation": "runtime/manifests/vectorfl_paper_actual_export_gate_validation_latest_v0.json",
    "dry_run": "runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json",
    "comparison": "runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json",
}


def _read_json(repo_root: Path, rel_path: str) -> Dict[str, Any]:
    path = repo_root / rel_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_vectorfl_paper_operable_state(runtime_root: Path) -> Dict[str, Any]:
    repo_root = runtime_root.resolve().parent
    handoff = _read_json(repo_root, PAPER_MANIFEST_PATHS["codex_handoff"])
    codex_return = _read_json(repo_root, PAPER_MANIFEST_PATHS["codex_return"])
    gemini_review = _read_json(repo_root, PAPER_MANIFEST_PATHS["gemini_review"])
    decision = _read_json(repo_root, PAPER_MANIFEST_PATHS["supervisor_decision"])
    current_slot = _read_json(repo_root, PAPER_MANIFEST_PATHS["current_slot"])
    gate_validation = _read_json(repo_root, PAPER_MANIFEST_PATHS["gate_validation"])
    dry_run = _read_json(repo_root, PAPER_MANIFEST_PATHS["dry_run"])
    comparison = _read_json(repo_root, PAPER_MANIFEST_PATHS["comparison"])
    supervisor_answers = comparison.get("supervisor_answers") or {}

    return {
        "schema_version": "vectorfl_paper_operable_state_v0",
        "surface_role": "server_backed_state_boundary",
        "migration_posture": "static_snapshot_to_server_backed_operable_surface",
        "layer_classification": {
            "current_route": "/vectorfl-paper",
            "current_route_role": "engine_status_console_not_final_integrated_operating_page",
            "top_layer_target": "paperclip_like_integrated_operating_layer",
            "reason": "proper and operable_surface are substrate surfaces; the final operating page must sit above them as work/organ/governance control plane",
        },
        "source_surface": "vectorfl_paper_proper",
        "target_surface": "vectorfl_operable_surface",
        "guard": {
            "gate_close": "forbidden",
            "slot_replacement": "forbidden",
            "candidate_promotion": "forbidden",
            "fake_controls": "forbidden",
            "static_generator_role": "snapshot_export_only_after_action_boundary",
        },
        "paths": PAPER_MANIFEST_PATHS,
        "current_ssot": {
            "path": PAPER_MANIFEST_PATHS["current_slot"],
            "state": current_slot.get("current_state") or "unknown",
            "anchor": current_slot.get("current_validation_anchor_ref")
            or current_slot.get("current_placeholder_ref")
            or "unknown",
            "honesty": current_slot.get("validation_anchor_status") or "unknown",
            "note": current_slot.get("validation_anchor_note") or "",
        },
        "dry_run_preview": {
            "path": PAPER_MANIFEST_PATHS["dry_run"],
            "source_record": dry_run.get("source_record_artifact") or "unknown",
            "validation_status": dry_run.get("validation_status") or "unknown",
            "honesty_class": dry_run.get("honesty_class") or "unknown",
            "gate_effect": dry_run.get("gate_effect") or "unknown",
            "delta_vs_current_anchor": dry_run.get("delta_vs_current_anchor") or {},
        },
        "comparison_summary": {
            "path": PAPER_MANIFEST_PATHS["comparison"],
            "candidate_for_reopen_validation_repeatable": supervisor_answers.get(
                "is_candidate_for_reopen_validation_repeatable_across_references"
            ),
            "shape_preserving_references": supervisor_answers.get(
                "references_that_preserve_shape_while_improving_honesty_boundary"
            )
            or [],
            "any_candidate_close_to_gate_close": supervisor_answers.get(
                "is_any_candidate_close_to_actual_export_only_gate_close"
            ),
            "validator_stable_for_merge_testing": supervisor_answers.get(
                "is_validator_stable_enough_for_post_stabilization_merge_testing"
            ),
        },
        "worker_handoff": {
            "path": PAPER_MANIFEST_PATHS["codex_handoff"],
            "status": handoff.get("status") or "unknown",
            "task": handoff.get("task") or "",
            "requested_action": handoff.get("requested_action") or "",
            "codex_top_files": handoff.get("codex_top_files") or handoff.get("relevant_files") or [],
        },
        "codex_return": {
            "path": PAPER_MANIFEST_PATHS["codex_return"],
            "status": codex_return.get("status") or "unknown",
            "summary": codex_return.get("summary") or "",
            "changed_files_count": len(codex_return.get("changed_files") or []),
            "blockers_count": len(codex_return.get("blockers") or []),
            "next_recommendation": codex_return.get("next_recommendation") or "",
            "needs_supervisor_decision": bool(codex_return.get("needs_supervisor_decision")),
        },
        "gemini_review": {
            "path": PAPER_MANIFEST_PATHS["gemini_review"],
            "review_status": gemini_review.get("review_status") or "unknown",
            "agreement_assessment": gemini_review.get("agreement_assessment") or "unknown",
            "detected_risks_count": len(gemini_review.get("detected_risks") or []),
            "missing_points_count": len(gemini_review.get("missing_points") or []),
            "recommendation": gemini_review.get("recommendation") or "",
            "suggested_supervisor_action": gemini_review.get("suggested_supervisor_action") or "",
            "gemini_review_top_files": gemini_review.get("gemini_review_top_files") or [],
        },
        "supervisor_decision": {
            "path": PAPER_MANIFEST_PATHS["supervisor_decision"],
            "decision": decision.get("decision") or "unknown",
            "rationale": decision.get("rationale") or "",
            "decision_tension": decision.get("decision_tension") or "",
            "pending_validations": decision.get("pending_validations") or [],
            "continue_gate": decision.get("continue_gate") or "",
        },
        "gate_validation": {
            "path": PAPER_MANIFEST_PATHS["gate_validation"],
            "validation_status": gate_validation.get("validation_status") or "unknown",
            "honesty_class": gate_validation.get("honesty_class") or "unknown",
            "gate_effect": gate_validation.get("gate_effect") or "unknown",
            "recommendation": gate_validation.get("recommendation") or "",
        },
        "next_ui_step": {
            "recommended_shell": "jsx_or_server_rendered_shell",
            "first_consumer": "GET /api/vectorfl-paper/state",
            "do_not_implement_yet": [
                "slot replacement",
                "candidate promotion",
                "gate close",
                "fake execution buttons",
            ],
        },
    }
