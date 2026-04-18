from __future__ import annotations

import argparse
import html
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "runtime" / "views" / "vectorfl_paper_proper"
HANDOFF_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_codex_handoff_latest_v0.json"
RETURN_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_codex_return_latest_v0.json"
DECISION_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_supervisor_decision_latest_v0.json"
GEMINI_REVIEW_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_gemini_review_latest_v0.json"
ACTUAL_EXPORT_VALIDATION_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_actual_export_gate_validation_latest_v0.json"
ACTUAL_EXPORT_VALIDATION_DRY_RUN_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_actual_export_gate_validation_dry_run_v0.json"
REFERENCE_COMPARISON_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_reference_candidate_validation_comparison_v0.json"
ACTUAL_EXPORT_SLOT_REF = "runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json"
EXTERNAL_RECORD_ANCHOR_REF = "runtime/contracts/vectorfl_paper_weekend_live_export_shaped_host_record_v2.json"
CODEX_TOP_FILES = [
    "runtime/contracts/vectorfl_paper_proper_selection_state_v0.json",
    EXTERNAL_RECORD_ANCHOR_REF,
    "runtime/contracts/vectorfl_paper_weekend_live_external_resource_output_v1.json",
    "runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json",
]
GEMINI_REVIEW_TOP_FILES = [
    "runtime/manifests/vectorfl_paper_codex_return_latest_v0.json",
    "runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json",
    ACTUAL_EXPORT_SLOT_REF,
    EXTERNAL_RECORD_ANCHOR_REF,
]
LABELS = {
    "current_ssot": "current_ssot",
    "preview_only": "preview_only",
    "summary_only": "summary_only",
    "hold_current": "hold_current",
    "bounded_reopen": "bounded_reopen",
}


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json_if_exists(path: Path) -> Dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _chip(text: str) -> str:
    return f'<span class="chip">{html.escape(text)}</span>'


def _label(key: str) -> str:
    return LABELS[key]


def _section(title: str, body: str, kicker: str = "") -> str:
    kicker_html = f'<div class="kicker">{html.escape(kicker)}</div>' if kicker else ""
    return f"""
    <section class="panel">
      {kicker_html}
      <h2>{html.escape(title)}</h2>
      {body}
    </section>
    """


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _build_codex_handoff(
    *,
    active_task: Dict[str, Any],
    selection_state: Dict[str, Any],
    supervisor_board: Dict[str, Any],
    status_board: Dict[str, Any],
    runtime_write_back: Dict[str, Any],
    actual_export_slot: Dict[str, Any],
    external_record_anchor: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "schema_version": "vectorfl_paper_codex_handoff_latest_v0",
        "worker_target": "codex",
        "task": active_task["title"],
        "goal": active_task["user_goal"],
        "selected_context_summary": {
            "working_context": selection_state["selected_case"]["case_id"],
            "task_focus": "Keep the loop thin and supervisor-readable while improving the issue/run/result/governance translation quality.",
            "current_task_sentence": f"{selection_state['selected_line']['line_id']} is the active proof pressure and {supervisor_board['single_remaining_gate']['name']} is the remaining gate.",
            "selected_line": selection_state["selected_line"]["line_id"],
            "selected_bundle": selection_state["selected_bundle"]["bundle_id"],
            "compare_target": selection_state["compare_target"]["target_id"],
            "external_record_anchor": {
                "slot": ACTUAL_EXPORT_SLOT_REF,
                "record": EXTERNAL_RECORD_ANCHOR_REF,
                "record_id": external_record_anchor["record_id"],
                "current_state": actual_export_slot["current_state"],
                "honesty_note": external_record_anchor["honesty_note"],
            },
            "current_status_summary": f"judgment={supervisor_board['current_direction']['judgment']} / runtime_write_back={runtime_write_back['write_back_state']} / human_gate_required={str(active_task['current_governance']['human_gate_required']).lower()}",
        },
        "relevant_files": CODEX_TOP_FILES,
        "codex_top_files": CODEX_TOP_FILES,
        "external_record_anchor": {
            "slot": ACTUAL_EXPORT_SLOT_REF,
            "record": EXTERNAL_RECORD_ANCHOR_REF,
            "record_id": external_record_anchor["record_id"],
            "source_kind": external_record_anchor["source_kind"],
            "current_state": actual_export_slot["current_state"],
            "validation_scope": "Use this as the single export-shaped validation anchor; do not treat it as proof that actual_export_only is fully closed.",
            "honesty_note": external_record_anchor["honesty_note"],
        },
        "constraints": [
            "paper remains read_only",
            "do not pretend Codex is fully attached to the runtime",
            "keep the overlay thin",
            "do not broaden search scope",
            "do not hide unresolved tensions",
            "do not expand into many new pages or documents",
        ],
        "requested_action": "compare issue/run/result/governance mapping and reject broader ontology import",
        "expected_output": {
            "return_slot": "external_candidates_latest",
            "deliverables": [
                "summary",
                "changed_files_or_no_change_note",
                "trace_notes",
                "recommendation",
            ],
        },
        "forbidden_scope": [
            "fake execution control",
            "gemini handoff emission",
            "result intake persistence",
            "supervisor decision persistence",
            "broad UI expansion",
        ],
        "status": "emitted",
        "emitted_at": _now_iso(),
        "source_surface": "vectorfl_paper_proper",
        "status_board_ref": status_board["board_id"],
    }


def _write_codex_handoff(payload: Dict[str, Any]) -> Path:
    HANDOFF_PATH.parent.mkdir(parents=True, exist_ok=True)
    HANDOFF_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return HANDOFF_PATH


def _build_codex_return(*, handoff_payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "schema_version": "vectorfl_paper_codex_return_latest_v0",
        "source_handoff_artifact": str(HANDOFF_PATH.relative_to(REPO_ROOT)),
        "worker": "codex",
        "status": "mock_return_recorded",
        "summary": "Codex is not connected yet, but the latest return slot is now reserved as a concrete runtime artifact that points back to the emitted handoff and keeps the next review readable inside Paper.",
        "changed_files": [
            "scripts/run_vectorfl_paper_proper_mock.py",
            "runtime/views/vectorfl_paper_proper/index.html",
        ],
        "blockers": [
            "real Codex worker connection is not attached yet",
            "result intake is surface-visible but not yet persisted from an actual worker run",
        ],
        "next_recommendation": "Ask the supervisor to review the latest emitted handoff and decide whether the first real Codex return should preserve the same return slot shape.",
        "needs_supervisor_decision": True,
        "returned_at": _now_iso(),
    }


def _write_codex_return(payload: Dict[str, Any]) -> Path:
    RETURN_PATH.parent.mkdir(parents=True, exist_ok=True)
    RETURN_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return RETURN_PATH


def _build_supervisor_decision(
    *,
    codex_return_payload: Dict[str, Any],
    gemini_review_payload: Dict[str, Any] | None,
    actual_export_slot: Dict[str, Any],
    external_record_anchor: Dict[str, Any],
) -> Dict[str, Any]:
    required_surfaces = actual_export_slot["expected_shape"]["required_surfaces"]
    present_surfaces = [surface for surface in required_surfaces if surface in external_record_anchor]
    validation_reduced = [
        f"One export-shaped host record anchor is now fixed: {EXTERNAL_RECORD_ANCHOR_REF}.",
        f"The anchor exposes {len(present_surfaces)}/{len(required_surfaces)} required surfaces: {', '.join(present_surfaces)}.",
    ]
    pending_validations = [
        "Replace the local export-shaped fixture with a truly actual external export while preserving the same thin seam.",
        "Exercise one real reopen decision path instead of relying on a hypothetical reopen case.",
        "Directly verify that the actual_export_only gate is closed from observed material rather than inference.",
    ]
    codex_position_summary = (
        "Codex says the thin overlay is still correct and can now inspect one fixed export-shaped record anchor, but the realism gate remains open until that anchor is actual rather than local fixture data."
    )

    if gemini_review_payload:
        gemini_action = str(gemini_review_payload.get("suggested_supervisor_action", "unknown"))
        gemini_position_summary = (
            f"Gemini mostly agrees with the Codex reading and suggests {gemini_action}; the supervisor still treats actual_export_only as the binding gate until direct validation lands."
        )
        decision = "hold_pending_validations"
        rationale = (
            "Codex supports the current thin mapping, and Gemini's review does not identify a new mapping objection. "
            "The honest supervisor state is still hold because actual_export_only remains evidenced as an open validation gate."
        )
        followup_action = (
            "Hold broad forward motion. Run one actual external export validation and one supervisor-readable hold/go/reopen check, then revisit continue."
        )
        decision_tension = f"codex_gate_open_vs_gemini_{gemini_action}"
    else:
        gemini_position_summary = "No Gemini cross-check is available yet, so the supervisor can only preserve a soft provisional continue-read."
        decision = "continue_provisional"
        rationale = (
            "Codex provides a viable thin-path reading, but without Gemini review the supervisor decision remains provisional and should not be treated as a hardened go signal."
        )
        followup_action = (
            "Keep the path thin and wait for a Gemini review before promoting this decision beyond provisional continue."
        )
        decision_tension = "codex_continue_ready_vs_review_missing"

    return {
        "schema_version": "vectorfl_paper_supervisor_decision_latest_v0",
        "source_return_artifact": str(RETURN_PATH.relative_to(REPO_ROOT)),
        "source_review_artifact": str(GEMINI_REVIEW_PATH.relative_to(REPO_ROOT)) if gemini_review_payload else None,
        "decision": decision,
        "rationale": rationale,
        "followup_action": followup_action,
        "target_worker": None,
        "lock_later_note": "Soft lock only. Promote to continue only after the pending validations are evidenced through the same latest return and review path.",
        "external_record_anchor": {
            "slot": ACTUAL_EXPORT_SLOT_REF,
            "record": EXTERNAL_RECORD_ANCHOR_REF,
            "record_id": external_record_anchor["record_id"],
            "current_state": actual_export_slot["current_state"],
            "honesty_note": external_record_anchor["honesty_note"],
        },
        "codex_position_summary": codex_position_summary,
        "gemini_position_summary": gemini_position_summary,
        "decision_tension": decision_tension,
        "validation_reduced": validation_reduced,
        "pending_validations": pending_validations,
        "continue_gate": "Continue becomes honest only after the fixed export-shaped fixture is replaced by a truly actual external record and one supervisor-readable hold/go/reopen decision is directly verified.",
        "decided_at": _now_iso(),
    }


def _write_supervisor_decision(payload: Dict[str, Any]) -> Path:
    DECISION_PATH.parent.mkdir(parents=True, exist_ok=True)
    DECISION_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return DECISION_PATH


def render_proper_page(repo_root: Path, *, emit_latest: bool = False) -> str:
    contracts = repo_root / "runtime" / "contracts"
    manifests = repo_root / "runtime" / "manifests"

    active_task = _load_json(contracts / "vectorfl_paper_weekend_pilot_active_task_v0.json")
    status_board = _load_json(contracts / "vectorfl_paper_weekend_pilot_status_board_v0.json")
    cell_registry = _load_json(contracts / "vectorfl_paper_weekend_pilot_cell_registry_v0.json")
    supervisor_board = _load_json(contracts / "vectorfl_paper_supervisor_current_board_v0.json")
    proper_tree = _load_json(contracts / "vectorfl_paper_proper_page_tree_v0.json")
    board_sections = _load_json(contracts / "vectorfl_paper_operating_board_sections_v0.json")
    worker_sections = _load_json(contracts / "vectorfl_paper_cell_worker_panel_sections_v0.json")
    case_sections = _load_json(contracts / "vectorfl_paper_case_detail_sections_v0.json")
    trace_sections = _load_json(contracts / "vectorfl_paper_trace_governance_sections_v0.json")
    selection_state = _load_json(contracts / "vectorfl_paper_proper_selection_state_v0.json")
    selection_presets = _load_json(contracts / "vectorfl_paper_proper_selection_presets_v0.json")
    live_packet = _load_json(contracts / "vectorfl_paper_weekend_live_translated_work_packet_v3.json")
    live_trace = _load_json(contracts / "vectorfl_paper_weekend_live_append_only_trace_row_v0.json")
    reinjection_stub = _load_json(contracts / "vectorfl_paper_weekend_live_result_reinjection_stub_v0.json")
    synthesis_output = _load_json(contracts / "vectorfl_paper_weekend_live_synthesis_output_v1.json")
    runtime_write_back = _load_json(manifests / "vectorfl_paper_weekend_live_runtime_write_back_v0.json")
    reopen_case = _load_json(manifests / "vectorfl_paper_weekend_live_reopen_case_v0.json")
    pilot_current = _load_json(manifests / "vectorfl_paper_pilot_current_v0.json")
    actual_export_slot = _load_json(manifests / "vectorfl_paper_actual_export_host_record_slot_v0.json")
    external_record_anchor = _load_json(repo_root / EXTERNAL_RECORD_ANCHOR_REF)
    actual_export_validation = _load_json_if_exists(ACTUAL_EXPORT_VALIDATION_PATH)
    actual_export_validation_dry_run = _load_json_if_exists(ACTUAL_EXPORT_VALIDATION_DRY_RUN_PATH)
    reference_comparison = _load_json_if_exists(REFERENCE_COMPARISON_PATH)
    reference_pack = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_internal_material_reference_pack_v0.md")
    codex_handoff = _build_codex_handoff(
        active_task=active_task,
        selection_state=selection_state,
        supervisor_board=supervisor_board,
        status_board=status_board,
        runtime_write_back=runtime_write_back,
        actual_export_slot=actual_export_slot,
        external_record_anchor=external_record_anchor,
    )
    handoff_path = _write_codex_handoff(codex_handoff) if emit_latest else HANDOFF_PATH
    existing_return = _load_json_if_exists(RETURN_PATH)
    if existing_return is None:
        codex_return = _build_codex_return(handoff_payload=codex_handoff)
        return_path = _write_codex_return(codex_return) if emit_latest else RETURN_PATH
    else:
        codex_return = existing_return
        return_path = RETURN_PATH
    gemini_review = _load_json_if_exists(GEMINI_REVIEW_PATH)
    supervisor_decision = _build_supervisor_decision(
        codex_return_payload=codex_return,
        gemini_review_payload=gemini_review,
        actual_export_slot=actual_export_slot,
        external_record_anchor=external_record_anchor,
    )
    decision_path = _write_supervisor_decision(supervisor_decision) if emit_latest else DECISION_PATH
    comparison_answers = (reference_comparison or {}).get("supervisor_answers", {})
    comparison_candidates = (reference_comparison or {}).get("candidate_results", [])
    comparison_guard = (reference_comparison or {}).get("merge_guard", {})
    comparison_shape_preserved_count = sum(1 for item in comparison_candidates if item.get("shape_preserved"))
    comparison_honesty_improved_count = sum(1 for item in comparison_candidates if item.get("honesty_boundary_improved"))
    comparison_summary_block = (
        f"""
    <div class="label">comparison summary only</div>
    <div class="chip-row">
      {_chip('reopen_validation_repeatable=' + str(comparison_answers.get('is_candidate_for_reopen_validation_repeatable_across_references', 'unknown')).lower())}
      {_chip(_label('summary_only') + '=true')}
      {_chip('shape_preserved_refs=' + str(comparison_shape_preserved_count) + '/' + str(len(comparison_candidates)))}
      {_chip('honesty_boundary_improved_refs=' + str(comparison_honesty_improved_count) + '/' + str(len(comparison_candidates)))}
      {_chip('gate_close_candidate=' + str(comparison_answers.get('is_any_candidate_close_to_actual_export_only_gate_close', 'unknown')).lower())}
    </div>
    <div class="meta">summary_source={html.escape(str(REFERENCE_COMPARISON_PATH.relative_to(repo_root)))} / no archive rows merged</div>
    <div class="label">hold / reopen guard</div>
    <div class="chip-row">
      {_chip(_label('hold_current') + '=true')}
      {_chip(_label('bounded_reopen') + '=allowed')}
      {_chip('current_slot_replacement=' + str(comparison_guard.get('current_slot_replacement', 'forbidden')))}
      {_chip('gate_close=false')}
      {_chip('candidate_promotion=false')}
      {_chip('allowed_next=bounded_reopen_validation')}
    </div>
    <div class="body-copy">Current SSOT stays on the actual_export slot. Dry-run remains preview-only; comparison is supervisor summary only; continue waits for a true host/export candidate with raw provenance.</div>
    """
        if reference_comparison
        else """
    <div class="label">comparison summary only</div>
    <div class="chip-row"><span class="chip">comparison_status=not_available</span></div>
    <div class="meta">No reference comparison manifest is available; keep current SSOT and dry-run preview separated.</div>
    """
    )

    active_cases_body = f"""
    <div class="list-row">
      <div class="entity-title">{html.escape(active_task['title'])}</div>
      <div class="entity-sub">{html.escape(active_task['user_goal'])}</div>
      <div class="chip-row">
        {_chip('stage=first_loop_proof')}
        {_chip('route=internal_first_external_ready')}
        {_chip('current_case=weekend_pilot_first_loop')}
        {_chip('posture=' + supervisor_decision['decision'])}
      </div>
      <div class="meta">hold_reason=actual_export_only is still open / next_gate={html.escape(supervisor_decision['continue_gate'])}</div>
    </div>
    """
    decision_queue_body = f"""
    <div class="list-row">
      <div class="entity-title">actual_export_only</div>
      <div class="entity-sub">{html.escape(supervisor_board['single_remaining_gate']['description'])}</div>
      <div class="chip-row">
        {_chip('decision=' + supervisor_decision['decision'])}
        {_chip('urgency=next_real_input')}
        {_chip('pending_validations=' + str(len(supervisor_decision['pending_validations'])))}
        {_chip('approval_mode=human_gate_after_real_validation')}
      </div>
      <div class="meta">reason={html.escape(supervisor_decision['rationale'])}</div>
      <div class="meta">continue_gate={html.escape(supervisor_decision['continue_gate'])}</div>
    </div>
    """
    current_proof_body = f"""
    <div class="body-copy">{html.escape(supervisor_board['headline'])}</div>
    <div class="label">why this exists now</div>
    <div class="body-copy">{html.escape(active_task['task_seed']['why_now'])}</div>
    <div class="chip-row">
      {_chip('current_stage=proper_surface_definition')}
      {_chip('single_remaining_gate=' + supervisor_board['single_remaining_gate']['name'])}
    </div>
    """
    active_cells_body = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(cell['label'])}</div>
          <div class="entity-sub">{html.escape(cell['purpose'])}</div>
          <div class="chip-row">
            {_chip('owner=' + cell['managing_cli'])}
            {_chip('state=' + ('waiting_for_real_export' if cell['cell_id'] == 'external_resource_cell' else 'ready'))}
          </div>
          <div class="meta">handoff={html.escape(', '.join(item['cell_id'] for item in cell['handoff_targets']))}</div>
        </div>
        """
        for cell in cell_registry["cells"]
    )
    latest_returns_body = f"""
    <div class="list-row">
      <div class="entity-title">runtime write-back</div>
      <div class="entity-sub">{html.escape(runtime_write_back['operator_readout']['what_changed'])}</div>
    </div>
    <div class="list-row">
      <div class="entity-title">reopen case</div>
      <div class="entity-sub">{html.escape(reopen_case['supervisor_language_summary'])}</div>
    </div>
    <div class="list-row">
      <div class="entity-title">reinjection hint</div>
      <div class="entity-sub">{html.escape(reinjection_stub['advisory_return_hint'])}</div>
    </div>
    """
    remaining_gates_body = f"""
    <div class="chip-row">
      {_chip('realism_gate=actual_export_pending')}
      {_chip('reading_protection_gate=keep_overlay_thin')}
      {_chip('external_comparison_gate=do_not_broaden_search')}
      {_chip('promotion_gate=proper_naming_waits_for_real_export')}
    </div>
    <div class="meta">{html.escape(actual_export_slot['operator_note'])}</div>
    """
    selection_block = f"""
    <div class="label">selected case</div>
    <div class="chip-row">{_chip(selection_state['selected_case']['case_id'])}</div>
    <div class="label">selected line</div>
    <div class="body-copy">{html.escape(selection_state['selected_line']['line_id'])}</div>
    <div class="meta">{html.escape(selection_state['selected_line']['why_now'])}</div>
    <div class="label">selected bundle</div>
    <div class="body-copy">{html.escape(selection_state['selected_bundle']['bundle_id'])}</div>
    <div class="label">compare target</div>
    <div class="body-copy">{html.escape(selection_state['compare_target']['label'])}</div>
    <div class="label">worker target / return slot</div>
    <div class="chip-row">{_chip(selection_state['current_worker_target']['cell_id'])}{_chip(selection_state['current_worker_target']['cli'])}{_chip(selection_state['current_return_slot']['slot_id'])}</div>
    """
    selection_variants_body = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(preset['label'])}</div>
          <div class="entity-sub">line={html.escape(preset['selected_line'])} / worker={html.escape(preset['worker_target'])} / cli={html.escape(preset['cli'])}</div>
          <div class="chip-row">
            {_chip('return=' + preset['target_return_slot'])}
            {_chip('action=' + preset['requested_action'])}
          </div>
          <div class="meta">gate={html.escape(preset['governance_emphasis'])} / next={html.escape(preset['next_move'])}</div>
        </div>
        """
        for preset in selection_presets["presets"]
    )
    codex_presets = [preset for preset in selection_presets["presets"] if preset.get("cli") == "codex-cli"]
    gemini_presets = [preset for preset in selection_presets["presets"] if preset.get("cli") == "gemini-cli"]
    current_context_body = f"""
    <div class="body-copy">Read-only supervisor surface. The task here is not to widen the system but to keep one thin loop legible enough that the next worker can act without re-decoding the page.</div>
    <div class="label">current goal</div>
    <div class="entity-title">{html.escape(active_task['title'])}</div>
    <div class="entity-sub">{html.escape(active_task['user_goal'])}</div>
    <div class="label">worker-ready focus</div>
    <div class="body-copy">{html.escape(selection_state['selected_line']['line_id'])} is the active proof pressure, {html.escape(selection_state['compare_target']['label'])} is the only allowed comparison seam, and {html.escape(supervisor_board['single_remaining_gate']['name'])} is the remaining gate.</div>
    <div class="chip-row">
      {_chip('selected_case=' + selection_state['selected_case']['case_id'])}
      {_chip('selected_line=' + selection_state['selected_line']['line_id'])}
      {_chip('selected_bundle=' + selection_state['selected_bundle']['bundle_id'])}
      {_chip('compare_target=' + selection_state['compare_target']['target_id'])}
    </div>
    <div class="label">state summary</div>
    <div class="chip-row">
      {_chip('judgment=' + supervisor_board['current_direction']['judgment'])}
      {_chip('remaining_gate=' + supervisor_board['single_remaining_gate']['name'])}
      {_chip('human_gate_required=' + str(active_task['current_governance']['human_gate_required']).lower())}
      {_chip('runtime_write_back=' + runtime_write_back['write_back_state'])}
    </div>
    <div class="label">external validation anchor</div>
    <div class="chip-row">
      {_chip('slot=' + actual_export_slot['slot_id'])}
      {_chip('state=' + actual_export_slot['current_state'])}
      {_chip('record=' + external_record_anchor['record_id'])}
      {_chip('source_kind=' + external_record_anchor['source_kind'])}
    </div>
    <div class="meta">{html.escape(external_record_anchor['honesty_note'])}</div>
    <div class="label">actual_export gate validator</div>
    {(
        f'''
    <div class="chip-row">
      {_chip('validation_status=' + str(actual_export_validation.get('validation_status', 'unknown')))}
      {_chip('honesty_class=' + str(actual_export_validation.get('honesty_class', 'unknown')))}
      {_chip('gate_effect=' + str(actual_export_validation.get('gate_effect', 'unknown')))}
    </div>
    <div class="meta">validated_at={html.escape(str(actual_export_validation.get('validated_at', '')))}</div>
    <div class="body-copy">{html.escape(str(actual_export_validation.get('recommendation', '')))}</div>
    '''
        if actual_export_validation
        else f'''
    <div class="chip-row">
      {_chip('validation_status=not_run')}
      {_chip('gate_effect=unknown')}
    </div>
    <div class="meta">Run scripts/run_vectorfl_paper_actual_export_gate_validator.py to record the latest actual_export_only gate judgment.</div>
    '''
    )}
    <div class="label">actual_export dry-run preview</div>
    {(
        f'''
    <div class="chip-row">
      {_chip('source=' + str(actual_export_validation_dry_run.get('source_record_artifact', 'unknown')))}
      {_chip('validation_status=' + str(actual_export_validation_dry_run.get('validation_status', 'unknown')))}
      {_chip('honesty_class=' + str(actual_export_validation_dry_run.get('honesty_class', 'unknown')))}
      {_chip('gate_effect=' + str(actual_export_validation_dry_run.get('gate_effect', 'unknown')))}
    </div>
    <div class="meta">validated_at={html.escape(str(actual_export_validation_dry_run.get('validated_at', '')))}</div>
    <div class="meta">delta_vs_current_anchor={html.escape(json.dumps(actual_export_validation_dry_run.get('delta_vs_current_anchor', {}), ensure_ascii=False))}</div>
    '''
        if actual_export_validation_dry_run
        else f'''
    <div class="chip-row">
      {_chip('dry_run_status=not_run')}
    </div>
    <div class="meta">Dry-run preview is separate from the current latest validator result.</div>
    '''
    )}
    <div class="label">current SSOT vs dry-run distinction</div>
    <div class="chip-row">
      {_chip(_label('current_ssot') + '=' + actual_export_slot['slot_id'])}
      {_chip('current_state=' + actual_export_slot['current_state'])}
      {_chip('dry_run=' + _label('preview_only'))}
      {_chip('slot_replacement=false')}
      {_chip('gate_close=false')}
    </div>
    <div class="meta">Dry-run can narrow supervisor reading, but it does not replace the current slot and does not promote any candidate.</div>
    {comparison_summary_block}
    <div class="label">working files</div>
    <div class="chip-row">
      {_chip('active_task_v0')}
      {_chip('selection_state_v0')}
      {_chip('external_resource_output_v1')}
      {_chip('synthesis_output_v1')}
      {_chip('runtime_write_back_v0')}
    </div>
    """
    worker_handoff_body = f"""
    <div class="body-copy">This slot does not launch a worker yet. It keeps the handoff package visible so the current context can later be emitted to Codex or Gemini without re-summarizing the page by hand.</div>
    <div class="label">worker target placeholder</div>
    <div class="chip-row">
      {_chip('current_target=' + selection_state['current_worker_target']['cli'])}
      {_chip('cell=' + selection_state['current_worker_target']['cell_id'])}
      {_chip('status=placeholder_only')}
      {_chip('launch_mode=not_connected')}
    </div>
    <div class="label">handoff brief area</div>
    <div class="body-copy">{html.escape(selection_state['current_worker_target']['action'])}</div>
    <div class="label">relevant files</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in codex_handoff['relevant_files'])}
    </div>
    <div class="label">codex_top_files</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in codex_handoff['codex_top_files'])}
    </div>
    <div class="label">external_record_anchor</div>
    <div class="chip-row">
      {_chip(codex_handoff['external_record_anchor']['record'])}
      {_chip('state=' + codex_handoff['external_record_anchor']['current_state'])}
      {_chip('scope=single_anchor_only')}
    </div>
    <div class="meta">{html.escape(codex_handoff['external_record_anchor']['validation_scope'])}</div>
    <div class="label">gemini_review_top_files</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in GEMINI_REVIEW_TOP_FILES)}
    </div>
    <div class="label">relevant constraints</div>
    <div class="chip-row">
      {_chip('read_only_truth_visible')}
      {_chip('keep_overlay_thin')}
      {_chip('do_not_broaden_search')}
      {_chip('do_not_hide_unresolved_tensions')}
    </div>
    <div class="label">expected output / forbidden scope</div>
    <div class="chip-row">
      {_chip('expected=' + selection_state['current_return_slot']['slot_id'])}
      {_chip('expected=summary+trace+recommendation')}
      {_chip('forbidden=fake_execution')}
      {_chip('forbidden=page_proliferation')}
    </div>
    <div class="label">role split</div>
    <div class="list-row">
      <div class="entity-title">Codex placeholder</div>
      <div class="entity-sub">deep reading / file inspection / patch or implementation / line tracing</div>
      <div class="meta">{html.escape(', '.join(preset['requested_action'] for preset in codex_presets) or 'no codex preset yet')}</div>
    </div>
    <div class="list-row">
      <div class="entity-title">Gemini placeholder</div>
      <div class="entity-sub">cross-check / review / bias-omission check / lightweight alternative reading</div>
      <div class="meta">{html.escape(', '.join(preset['requested_action'] for preset in gemini_presets) or 'no gemini preset yet')}</div>
    </div>
    <div class="label">last emitted handoff</div>
    <div class="chip-row">
      {_chip('worker=' + codex_handoff['worker_target'])}
      {_chip('status=' + codex_handoff['status'])}
      {_chip('return=' + codex_handoff['expected_output']['return_slot'])}
    </div>
    <div class="meta">path={html.escape(str(handoff_path.relative_to(repo_root)))} / emitted_at={html.escape(codex_handoff['emitted_at'])}</div>
    """
    result_intake_body = f"""
    <div class="body-copy">This slot is reserved for worker returns so results land back inside Paper instead of being scattered across chat or temporary notes.</div>
    <div class="label">status placeholder</div>
    <div class="chip-row">
      {_chip('intake_status=waiting_for_worker_connection')}
      {_chip('return_slot=' + selection_state['current_return_slot']['slot_id'])}
      {_chip('source_trace=' + live_trace['trace_id'])}
      {_chip('reopen_status=' + reopen_case['status'])}
    </div>
    <div class="label">summary</div>
    <div class="body-copy">{html.escape(runtime_write_back['operator_readout']['what_changed'])}</div>
    <div class="label">changed files / trace / notes</div>
    <div class="chip-row">
      {_chip('packet=' + live_packet['packet_id'])}
      {_chip('trace=' + live_trace['trace_id'])}
      {_chip('reopen=' + reopen_case['reopen_case_id'])}
      {_chip('report=vectorfl_paper_weekend_live_supervisor_report_v1.md')}
    </div>
    <div class="label">blockers</div>
    <div class="chip-row">
      {_chip('actual_export_only')}
      {_chip('real_worker_result_not_yet_ingested')}
      {_chip('supervisor_bridge_slot_only')}
    </div>
    <div class="label">recommendation</div>
    <div class="body-copy">{html.escape(synthesis_output['recommendation']['reason'])}</div>
    <div class="label">latest codex return</div>
    <div class="chip-row">
      {_chip('worker=' + codex_return['worker'])}
      {_chip('status=' + codex_return['status'])}
      {_chip('needs_supervisor_decision=' + str(codex_return['needs_supervisor_decision']).lower())}
    </div>
    <div class="meta">source_handoff_artifact={html.escape(codex_return['source_handoff_artifact'])}</div>
    <div class="meta">return_path={html.escape(str(return_path.relative_to(repo_root)))} / returned_at={html.escape(codex_return['returned_at'])}</div>
    <div class="body-copy">{html.escape(codex_return['summary'])}</div>
    <div class="label">changed files preview</div>
    <div class="chip-row">
      {_chip('count=' + str(len(codex_return['changed_files'])))}
      {''.join(_chip(item) for item in codex_return['changed_files'][:2])}
    </div>
    <div class="label">blockers present</div>
    <div class="chip-row">
      {_chip('has_blockers=' + str(bool(codex_return['blockers'])).lower())}
      {''.join(_chip(item) for item in codex_return['blockers'][:2])}
    </div>
    <div class="label">next recommendation</div>
    <div class="body-copy">{html.escape(codex_return['next_recommendation'])}</div>
    <div class="label">latest gemini cross-check</div>
    {(
        f'''
    <div class="chip-row">
      {_chip('worker=' + str(gemini_review.get('worker', 'gemini')))}
      {_chip('review_status=' + str(gemini_review.get('review_status', 'unknown')))}
      {_chip('agreement=' + str(gemini_review.get('agreement_assessment', 'unknown')))}
    </div>
    <div class="meta">source_return_artifact={html.escape(str(gemini_review.get('source_return_artifact', '')))}</div>
    <div class="meta">review_path={html.escape(str(GEMINI_REVIEW_PATH.relative_to(repo_root)))} / reviewed_at={html.escape(str(gemini_review.get('reviewed_at', '')))}</div>
    <div class="body-copy">{html.escape(str(gemini_review.get('recommendation', '')))}</div>
    <div class="chip-row">
      {_chip('suggested_supervisor_action=' + str(gemini_review.get('suggested_supervisor_action', 'unknown')))}
      {_chip('has_detected_risks=' + str(bool(gemini_review.get('detected_risks'))).lower())}
      {_chip('has_missing_points=' + str(bool(gemini_review.get('missing_points'))).lower())}
    </div>
    <div class="label">gemini_review_top_files</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in gemini_review.get('gemini_review_top_files', GEMINI_REVIEW_TOP_FILES))}
    </div>
    '''
        if gemini_review
        else f'''
    <div class="chip-row">
      {_chip('worker=gemini')}
      {_chip('review_status=not_run')}
    </div>
    <div class="meta">No Gemini cross-check artifact has been recorded yet.</div>
    '''
    )}
    """
    supervisor_decision_slot_body = f"""
    <div class="body-copy">Supervisor judgment remains human-owned. This slot is ready to record the next decision after future worker results return, without pretending the runtime already decides on its own.</div>
    <div class="label">decision options</div>
    <div class="chip-row">
      {_chip('continue')}
      {_chip('hold')}
      {_chip('reopen')}
      {_chip('cross-check')}
      {_chip('redirect')}
      {_chip('lock-later')}
    </div>
    <div class="label">current supervisor read</div>
    <div class="chip-row">
      {_chip('recommendation=' + supervisor_decision['decision'])}
      {_chip('remaining_gate=' + supervisor_board['single_remaining_gate']['name'])}
      {_chip('pending_validations=' + str(len(supervisor_decision['pending_validations'])))}
    </div>
    <div class="label">decision note</div>
    <div class="body-copy">{html.escape(supervisor_board['supervisor_takeaway'])}</div>
    <div class="label">lock-later note</div>
    <div class="meta">Hard lock waits until a real worker handoff and result intake complete one return loop through this same surface.</div>
    <div class="label">latest supervisor decision</div>
    <div class="chip-row">
      {_chip('decision=' + supervisor_decision['decision'])}
      {_chip('target_worker=' + str(supervisor_decision['target_worker']))}
    </div>
    <div class="meta">source_return_artifact={html.escape(supervisor_decision['source_return_artifact'])}</div>
    <div class="meta">source_review_artifact={html.escape(str(supervisor_decision.get('source_review_artifact')))}</div>
    <div class="meta">decision_path={html.escape(str(decision_path.relative_to(repo_root)))} / decided_at={html.escape(supervisor_decision['decided_at'])}</div>
    <div class="body-copy">{html.escape(supervisor_decision['rationale'])}</div>
    <div class="label">codex position</div>
    <div class="body-copy">{html.escape(supervisor_decision['codex_position_summary'])}</div>
    <div class="label">gemini position</div>
    <div class="body-copy">{html.escape(supervisor_decision['gemini_position_summary'])}</div>
    <div class="label">decision tension</div>
    <div class="chip-row">
      {_chip(supervisor_decision['decision_tension'])}
    </div>
    <div class="label">validation reduced</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in supervisor_decision['validation_reduced'])}
    </div>
    <div class="label">validator result</div>
    {(
        f'''
    <div class="chip-row">
      {_chip('validation_status=' + str(actual_export_validation.get('validation_status', 'unknown')))}
      {_chip('honesty_class=' + str(actual_export_validation.get('honesty_class', 'unknown')))}
      {_chip('gate_effect=' + str(actual_export_validation.get('gate_effect', 'unknown')))}
    </div>
    <div class="body-copy">{html.escape(str(actual_export_validation.get('recommendation', '')))}</div>
    '''
        if actual_export_validation
        else f'''
    <div class="chip-row">
      {_chip('validation_status=not_run')}
    </div>
    '''
    )}
    <div class="label">validator dry-run posture</div>
    {(
        f'''
    <div class="chip-row">
      {_chip('dry_run=' + _label('preview_only'))}
      {_chip('source=see_current_context')}
      {_chip('slot_replacement=false')}
      {_chip('gate_close=false')}
    </div>
    <div class="meta">Detailed dry-run preview is shown once in Current Context; Supervisor Decision keeps it subordinate to current SSOT.</div>
    '''
        if actual_export_validation_dry_run
        else f'''
    <div class="chip-row">
      {_chip('dry_run=' + _label('preview_only'))}
      {_chip('dry_run_status=not_run')}
    </div>
    '''
    )}
    <div class="label">pending validations</div>
    <div class="chip-row">
      {''.join(_chip(item) for item in supervisor_decision['pending_validations'])}
    </div>
    <div class="label">continue gate</div>
    <div class="body-copy">{html.escape(supervisor_decision['continue_gate'])}</div>
    <div class="label">followup action</div>
    <div class="body-copy">{html.escape(supervisor_decision['followup_action'])}</div>
    <div class="label">lock later</div>
    <div class="body-copy">{html.escape(supervisor_decision['lock_later_note'])}</div>
    """
    future_connection_body = f"""
    <div class="list-row">
      <div class="entity-title">where handoff will be emitted</div>
      <div class="entity-sub">current worker handoff slot in this page</div>
      <div class="meta">source anchors: selection state, cell registry, current proof, compare target, constraints</div>
    </div>
    <div class="list-row">
      <div class="entity-title">where result will be ingested</div>
      <div class="entity-sub">result intake slot in this page</div>
      <div class="meta">expected payload: summary / changed files / trace / blockers / recommendation / status</div>
    </div>
    <div class="list-row">
      <div class="entity-title">where supervisor action will be recorded</div>
      <div class="entity-sub">supervisor decision slot in this page</div>
      <div class="meta">actions reserved: continue / hold / reopen / cross-check / redirect / lock-later</div>
    </div>
    """
    alive_line_body = """
    <div class="chip-row">
      <span class="chip">input/context observed</span>
      <span class="chip">handoff prepared</span>
      <span class="chip">external worker result placeholder</span>
      <span class="chip">supervisor decision prepared</span>
      <span class="chip">return path reserved</span>
    </div>
    <div class="meta">The line is bridge-ready, not execution-complete. It should stay honest until a real Codex/Gemini attachment uses the handoff and intake slots.</div>
    """

    selected_cell = cell_registry["cells"][0]
    selected_cell_body = f"""
    <div class="body-copy">{html.escape(selected_cell['purpose'])}</div>
    <div class="label">lens</div>
    <div class="chip-row">{''.join(_chip(item) for item in selected_cell['lens'])}</div>
    <div class="label">managed internal functions</div>
    <div class="chip-row">{''.join(_chip(item) for item in selected_cell['managed_internal_functions'])}</div>
    <div class="label">outputs</div>
    <div class="chip-row">{''.join(_chip(item) for item in selected_cell['outputs'])}</div>
    <div class="label">handoff targets</div>
    <div class="chip-row">{''.join(_chip(item['cell_id']) for item in selected_cell['handoff_targets'])}</div>
    """
    cell_registry_body = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(cell['label'])}</div>
          <div class="entity-sub">{html.escape(', '.join(cell['lens']))}</div>
          <div class="chip-row">
            {_chip('owner=' + cell['managing_cli'])}
            {_chip('return=' + cell['return_slot'])}
          </div>
        </div>
        """
        for cell in cell_registry["cells"]
    )
    cli_ownership_body = f"""
    <div class="chip-row">
      {_chip('primary=' + selected_cell['managing_cli'])}
      {_chip('secondary=codex-cli')}
    </div>
    <div class="body-copy">The selected cell is owned by {html.escape(selected_cell['managing_cli'])} because its main work is internal reread pressure extraction and line seed formation.</div>
    """
    contract_body = f"""
    <div class="meta">contract={html.escape(selected_cell['md_contract'])}</div>
    <div class="label">allowed actions</div>
    <div class="chip-row">{''.join(_chip(item) for item in selected_cell['governance']['allowed_actions'])}</div>
    <div class="label">disallowed actions</div>
    <div class="chip-row">{''.join(_chip(item) for item in selected_cell['governance']['disallowed_actions'])}</div>
    <div class="label">return slot</div>
    <div class="chip-row">{_chip(selected_cell['return_slot'])}</div>
    """
    adapter_body = """
    <div class="chip-row">
      <span class="chip">provider=local_cli</span>
      <span class="chip">model=gemini-cli</span>
      <span class="chip">timeout=bounded</span>
      <span class="chip">budget=low</span>
      <span class="chip">enabled=true</span>
    </div>
    <div class="meta">The first proper mock keeps adapter settings explicit so cli ownership is readable as an operating condition rather than a hidden implementation detail.</div>
    """
    payload_body = f"""
    <div class="label">selected case</div>
    <div class="chip-row">{_chip(selection_state['selected_case']['case_id'])}</div>
    <div class="label">primary line</div>
    <div class="chip-row">{_chip(selection_state['selected_line']['line_id'])}</div>
    <div class="label">support lines</div>
    <div class="chip-row">{''.join(_chip(item) for item in live_packet['line_translation']['support_line_ids'])}</div>
    <div class="label">compare target</div>
    <div class="body-copy">{html.escape(selection_state['compare_target']['label'])}</div>
    <div class="label">requested action</div>
    <div class="chip-row">{_chip(selection_state['current_worker_target']['action'])}</div>
    """
    launch_body = """
    <div class="chip-row">
      <span class="chip">dry-run</span>
      <span class="chip">launch</span>
      <span class="chip">export</span>
      <span class="chip">reopen</span>
      <span class="chip">hold</span>
    </div>
    <div class="meta">Launch controls stay governance-aware: no free run is considered complete until trace append and return slot visibility are preserved.</div>
    """
    return_body = f"""
    <div class="label">target return slot</div>
    <div class="chip-row">{_chip(selection_state['current_return_slot']['slot_id'])}</div>
    <div class="label">trace append</div>
    <div class="body-copy">{html.escape(live_trace['summary'])}</div>
    <div class="label">reopen trigger</div>
    <div class="body-copy">{html.escape(reopen_case['reopen_questions'][0])}</div>
    """
    case_header_body = f"""
    <div class="body-copy">{html.escape(active_task['title'])}</div>
    <div class="chip-row">
      {_chip('current_stage=first_loop_proof')}
      {_chip('judgment=' + supervisor_board['current_direction']['judgment'])}
      {_chip('case_scope=' + active_task['scenario_scope'])}
    </div>
    <div class="meta">{html.escape(active_task['user_goal'])}</div>
    """
    source_read_body = f"""
    <div class="label">reread materials</div>
    <div class="chip-row">{''.join(_chip(item) for item in _load_json(contracts / "vectorfl_paper_weekend_live_internal_read_output_v1.json")['reread_materials'])}</div>
    <div class="label">scenario pressure</div>
    <div class="body-copy">{html.escape(active_task['task_seed']['headline'])}</div>
    <div class="label">current compare target</div>
    <div class="body-copy">{html.escape(selection_state['compare_target']['label'])}</div>
    """
    line_seeds_body = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(item['line_name'])}</div>
          <div class="entity-sub">{html.escape(item['core_claim'])}</div>
          <div class="meta">enables={html.escape(', '.join(item['what_it_enables']))} / selected={str(item['line_name'] == selection_state['selected_line']['line_id']).lower()}</div>
        </div>
        """
        for item in _load_json(contracts / "vectorfl_paper_weekend_live_internal_read_output_v1.json")["line_seeds"]
    )
    bundles_body = f"""
    <div class="list-row">
      <div class="entity-title">live bundle selection</div>
      <div class="entity-sub">The current case is grounded in the selected live bundle that preserves maturation posture, supervision language, operating flow, reading-organ surface, and thin Paperclip overlay grammar.</div>
    </div>
    <div class="list-row">
      <div class="entity-title">selected bundle</div>
      <div class="entity-sub">It keeps the first proper case tied to scenario-bearing material instead of flattening into generic work items.</div>
      <div class="meta">selected_bundle={html.escape(selection_state['selected_bundle']['bundle_id'])} / why={html.escape(selection_state['selected_bundle']['why_attached'])}</div>
    </div>
    """
    human_translation_body = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(item['line_name'])}</div>
          <div class="entity-sub">{html.escape(item['human_translation'])}</div>
          <div class="meta">next_use={html.escape(item['next_use'])}</div>
        </div>
        """
        for item in synthesis_output["confirmed_lines"]
    )
    missing_body = f"""
    <div class="chip-row">{''.join(_chip(item) for item in synthesis_output['unresolved_tensions'])}</div>
    <div class="meta">The main remaining realism gap is still the actual exported host record rerun.</div>
    """
    next_action_body = f"""
    <div class="body-copy">{html.escape(synthesis_output['next_loop_proposal']['why'])}</div>
    <div class="chip-row">
      {_chip('next_cell=' + synthesis_output['next_loop_proposal']['next_cell'])}
      {_chip('route_after=' + reopen_case['reopen_target']['handoff_after'])}
    </div>
    """
    run_trace_body = f"""
    <div class="label">current packet</div>
    <div class="chip-row">{_chip(live_packet['packet_id'])}</div>
    <div class="label">trace summary</div>
    <div class="body-copy">{html.escape(live_trace['summary'])}</div>
    <div class="meta">residue={html.escape(live_trace['residue_note'])}</div>
    """
    governance_body = f"""
    <div class="chip-row">
      {_chip('route=' + _load_json(contracts / 'vectorfl_paper_weekend_live_governance_gate_note_v0.json')['route_gate'])}
      {_chip('hold=' + _load_json(contracts / 'vectorfl_paper_weekend_live_governance_gate_note_v0.json')['hold_trace'])}
      {_chip('promotion=' + _load_json(contracts / 'vectorfl_paper_weekend_live_governance_gate_note_v0.json')['promotion_gate'])}
    </div>
    <div class="body-copy">{html.escape(_load_json(contracts / 'vectorfl_paper_weekend_live_governance_gate_note_v0.json')['caution_note'])}</div>
    <div class="meta">selection_basis={html.escape(selection_state['selected_line']['line_id'])} / compare_target={html.escape(selection_state['compare_target']['target_id'])}</div>
    """
    reopen_body = f"""
    <div class="body-copy">{html.escape(reopen_case['supervisor_language_summary'])}</div>
    <div class="label">why reopen now</div>
    <div class="chip-row">{''.join(_chip(item) for item in reopen_case['why_reopen_now'])}</div>
    <div class="label">reopen questions</div>
    <div class="chip-row">{''.join(_chip(item) for item in reopen_case['reopen_questions'])}</div>
    """
    reinjection_body = f"""
    <div class="body-copy">{html.escape(reinjection_stub['advisory_return_hint'])}</div>
    <div class="chip-row">
      {_chip('return_slot=' + selected_cell['return_slot'])}
      {_chip('next_probe=truer_external_source_record')}
    </div>
    """
    supervisor_decision_body = f"""
    <div class="chip-row">
      {_chip('mode=' + active_task['current_governance']['mode'])}
      {_chip('human_gate_required=' + str(active_task['current_governance']['human_gate_required']).lower())}
      {_chip('recommendation=' + synthesis_output['recommendation']['decision'])}
    </div>
    <div class="body-copy">{html.escape(synthesis_output['recommendation']['reason'])}</div>
    """
    next_loop_body = f"""
    <div class="body-copy">{html.escape(synthesis_output['next_loop_proposal']['why'])}</div>
    <div class="chip-row">{''.join(_chip(item) for item in synthesis_output['next_loop_proposal']['with_inputs'])}</div>
    """

    board_rules = "".join(_chip(item) for item in board_sections["global_rules"])
    worker_rules = "".join(_chip(item) for item in worker_sections["global_rules"])
    case_rules = "".join(_chip(item) for item in case_sections["global_rules"])
    trace_rules = "".join(_chip(item) for item in trace_sections["global_rules"])
    page_flow = "".join(_chip(item) for item in proper_tree["flow_rule"])
    reference_pack_block = html.escape(reference_pack)

    body = f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>VectorFL Paper Proper Mock</title>
      <style>
        :root {{
          --bg: #0b0c0e;
          --panel: #111317;
          --soft: #171a20;
          --line: rgba(255,255,255,0.1);
          --text: #eef2ff;
          --muted: #a5adc8;
          --accent: #818cf8;
          --radius: 24px;
        }}
        * {{ box-sizing: border-box; }}
        body {{
          margin: 0;
          font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
          background: radial-gradient(circle at top, rgba(129,140,248,0.16), transparent 22%), var(--bg);
          color: var(--text);
        }}
        .page {{ max-width: 1380px; margin: 0 auto; padding: 28px; display: grid; gap: 18px; }}
        .hero, .panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 18px; }}
        .panel.soft {{ background: var(--soft); }}
        .hero h1, .panel h2, .panel h3 {{ margin: 0; }}
        .kicker {{ color: var(--accent); font-size: 12px; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 10px; }}
        .meta {{ color: var(--muted); font-size: 13px; line-height: 1.5; }}
        .body-copy {{ line-height: 1.6; }}
        .grid {{ display: grid; gap: 18px; grid-template-columns: 1.05fr 0.95fr; }}
        .bridge-grid {{ display: grid; gap: 18px; grid-template-columns: 1fr 1fr; }}
        .stack {{ display: grid; gap: 18px; }}
        .dual {{ display: grid; gap: 18px; grid-template-columns: 1fr 1fr; }}
        .chip-row {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }}
        .chip {{ border: 1px solid rgba(129,140,248,0.35); background: rgba(129,140,248,0.12); border-radius: 999px; padding: 6px 10px; font-size: 12px; }}
        .list-row {{ border-top: 1px solid var(--line); padding: 12px 0; }}
        .list-row:first-child {{ border-top: 0; padding-top: 0; }}
        .entity-title {{ font-weight: 700; margin-bottom: 4px; }}
        .entity-sub {{ color: var(--text); line-height: 1.5; }}
        .label {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 10px; }}
        .code {{ white-space: pre-wrap; background: #0d1015; border: 1px solid var(--line); border-radius: 18px; padding: 14px; line-height: 1.5; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }}
        @media (max-width: 980px) {{
          .grid, .dual, .bridge-grid {{ grid-template-columns: 1fr; }}
        }}
      </style>
    </head>
    <body>
      <div class="page">
        <section class="hero">
          <div class="kicker">VectorFL Paper Proper Mock</div>
          <h1>Supervisor Bridge-Ready Paper Surface</h1>
          <div class="body-copy">Current live posture is {html.escape(supervisor_decision['decision'])}: Codex and Gemini both make the loop readable enough to operate, but the supervisor should still hold until the pending validations are directly evidenced through the same return and review path.</div>
          <div class="meta">Why hold: {html.escape(supervisor_decision['rationale'])}</div>
          <div class="meta">Continue gate: {html.escape(supervisor_decision['continue_gate'])}</div>
          <div class="chip-row">{page_flow}{_chip('posture=' + supervisor_decision['decision'])}{_chip('pending_validations=' + str(len(supervisor_decision['pending_validations'])))}{_chip('codex_return=' + codex_return['status'])}{_chip('gemini_review=' + str(gemini_review.get('review_status', 'not_run')) if gemini_review else 'gemini_review=not_run')}</div>
        </section>
        <div class="bridge-grid">
          {_section("Current Context", current_context_body, "Supervisor Bridge")}
          {_section("Worker Handoff Slot", worker_handoff_body, "Supervisor Bridge")}
          {_section("Result Intake Slot", result_intake_body, "Supervisor Bridge")}
          {_section("Supervisor Decision Slot", supervisor_decision_slot_body, "Supervisor Bridge")}
        </div>
        <div class="dual">
          {_section("Future Codex / Gemini Connection Memo", future_connection_body, "Bridge Memo")}
          {_section("Alive Operating Line", alive_line_body, "Bridge Memo")}
        </div>
        {_section("Shared Selection State", selection_block, "Operating Object")}
        {_section("Selection Variants", selection_variants_body, "Operating Object")}
        <section class="panel">
          <div class="kicker">Supporting Detail</div>
          <h2>Underlying Proof And Reference Panels</h2>
          <div class="meta">The panels below remain visible as supporting evidence. They no longer define the top-level operating line; they back the four supervisor bridge zones above.</div>
        </section>
        <div class="grid">
          <div class="stack">
            {_section("Current Proof", current_proof_body, "Operating Board")}
            {_section("Decision Queue", decision_queue_body, "Operating Board")}
            {_section("Active Cases", active_cases_body, "Operating Board")}
            {_section("Active Cells And CLI Runs", active_cells_body, "Operating Board")}
            {_section("Latest Returns", latest_returns_body, "Operating Board")}
            {_section("Remaining Gates", remaining_gates_body, "Operating Board")}
            {_section("Operating Board Rules", f'<div class="chip-row">{board_rules}</div>', "Board Contract")}
          </div>
          <div class="stack">
            {_section("Cell Registry", cell_registry_body, "Cell / Worker Panel")}
            {_section("Selected Cell Detail", selected_cell_body, "Cell / Worker Panel")}
            {_section("CLI Ownership", cli_ownership_body, "Cell / Worker Panel")}
            {_section("Contract Readout", contract_body, "Cell / Worker Panel")}
            {_section("Adapter Config", adapter_body, "Cell / Worker Panel")}
            {_section("Payload Preview", payload_body, "Cell / Worker Panel")}
            {_section("Launch Controls", launch_body, "Cell / Worker Panel")}
            {_section("Return Slot", return_body, "Cell / Worker Panel")}
            {_section("Cell / Worker Rules", f'<div class="chip-row">{worker_rules}</div>', "Panel Contract")}
          </div>
        </div>
        <div class="grid">
          <div class="stack">
            {_section("Case Header", case_header_body, "Case Detail")}
            {_section("Source Read", source_read_body, "Case Detail")}
            {_section("Line Seeds", line_seeds_body, "Case Detail")}
            {_section("Evidence Bundles", bundles_body, "Case Detail")}
            {_section("Human Translation", human_translation_body, "Case Detail")}
            {_section("Missing And Not Yet Read", missing_body, "Case Detail")}
            {_section("Next Action", next_action_body, "Case Detail")}
            {_section("Case Detail Rules", f'<div class="chip-row">{case_rules}</div>', "Case Contract")}
          </div>
          <div class="stack">
            {_section("Run Trace", run_trace_body, "Trace / Governance")}
            {_section("Governance Gate", governance_body, "Trace / Governance")}
            {_section("Reopen History", reopen_body, "Trace / Governance")}
            {_section("Reinjection", reinjection_body, "Trace / Governance")}
            {_section("Supervisor Decision", supervisor_decision_body, "Trace / Governance")}
            {_section("Next Loop Trigger", next_loop_body, "Trace / Governance")}
            {_section("Trace / Governance Rules", f'<div class="chip-row">{trace_rules}</div>', "Trace Contract")}
          </div>
        </div>
        <div class="dual">
          {_section("Canonical Pilot Refs", f'<div class="code">{html.escape(json.dumps(pilot_current["canonical_refs"], ensure_ascii=False, indent=2))}</div>', "Current Seam")}
          {_section("Internal Material Reference Pack", f'<div class="code">{reference_pack_block}</div>', "Always Reread")}
        </div>
      </div>
    </body>
    </html>
    """
    return body


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the VectorFL Paper proper supervisor surface.")
    parser.add_argument(
        "--emit-latest",
        action="store_true",
        help="Also emit latest handoff/decision manifests. Default render only refreshes the HTML surface.",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_path = OUTPUT_DIR / "index.html"
    html_path.write_text(render_proper_page(REPO_ROOT, emit_latest=args.emit_latest), encoding="utf-8")
    print(json.dumps({"html_path": str(html_path), "emit_latest": args.emit_latest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
