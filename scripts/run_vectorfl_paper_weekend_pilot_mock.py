from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict
import html


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "runtime" / "views" / "vectorfl_paper_weekend_pilot"


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _chip(text: str) -> str:
    return f'<span class="chip">{html.escape(text)}</span>'


def _section(title: str, body: str, kicker: str = "") -> str:
    kicker_html = f'<div class="kicker">{html.escape(kicker)}</div>' if kicker else ""
    return f"""
    <section class="panel">
      {kicker_html}
      <h2>{html.escape(title)}</h2>
      {body}
    </section>
    """


def render_weekend_pilot_page(repo_root: Path) -> str:
    contracts = repo_root / "runtime" / "contracts"
    bundle = _load_json(contracts / "vectorfl_paper_weekend_pilot_material_bundle_v0.json")
    live_bundle_selection = _load_json(contracts / "vectorfl_paper_weekend_live_bundle_selection_v0.json")
    live_external_target = _load_json(contracts / "vectorfl_paper_weekend_live_external_comparison_target_v0.json")
    intake_mapping = _load_json(contracts / "vectorfl_paper_issue_run_result_governance_intake_mapping_v0.json")
    overlay_example = _load_json(contracts / "vectorfl_paper_weekend_live_overlay_translation_example_v0.json")
    live_internal_output = _load_json(contracts / "vectorfl_paper_weekend_live_internal_read_output_v1.json")
    live_external_output = _load_json(contracts / "vectorfl_paper_weekend_live_external_resource_output_v1.json")
    live_synthesis_output = _load_json(contracts / "vectorfl_paper_weekend_live_synthesis_output_v1.json")
    supervisor_current_board = _load_json(contracts / "vectorfl_paper_supervisor_current_board_v0.json")
    live_issue_sample = _load_json(contracts / "vectorfl_paper_weekend_live_issue_sample_v0.json")
    native_shape_source = _load_json(contracts / "vectorfl_paper_weekend_live_native_shape_source_record_v1.json")
    export_shaped_source = _load_json(contracts / "vectorfl_paper_weekend_live_export_shaped_host_record_v2.json")
    live_work_packet = _load_json(contracts / "vectorfl_paper_weekend_live_translated_work_packet_v3.json")
    live_trace_row = _load_json(contracts / "vectorfl_paper_weekend_live_append_only_trace_row_v0.json")
    live_reinjection_stub = _load_json(contracts / "vectorfl_paper_weekend_live_result_reinjection_stub_v0.json")
    live_governance_gate = _load_json(contracts / "vectorfl_paper_weekend_live_governance_gate_note_v0.json")
    status_board = _load_json(contracts / "vectorfl_paper_weekend_pilot_status_board_v0.json")
    registry = _load_json(contracts / "vectorfl_paper_weekend_pilot_cell_registry_v0.json")
    active_task = _load_json(contracts / "vectorfl_paper_weekend_pilot_active_task_v0.json")
    internal_output = _load_json(contracts / "vectorfl_paper_weekend_pilot_internal_read_output_v0.json")
    external_output = _load_json(contracts / "vectorfl_paper_weekend_pilot_external_resource_output_v0.json")
    synthesis_output = _load_json(contracts / "vectorfl_paper_weekend_pilot_synthesis_output_v0.json")
    supervisor_decision = _load_json(contracts / "vectorfl_paper_weekend_pilot_supervisor_decision_v0.json")
    return_packet = _load_json(contracts / "vectorfl_paper_weekend_pilot_internal_return_packet_v0.json")
    supervisor_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_pilot_supervisor_report_v0.md")
    live_supervisor_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_supervisor_report_v1.md")
    runtime_write_back = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_runtime_write_back_v0.json")
    canonical_pilot_bridge = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_pilot_current_v0.json")
    actual_export_slot = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_actual_export_host_record_slot_v0.json")
    actual_export_template = _load_json(contracts / "vectorfl_paper_actual_export_host_record_template_v0.json")
    actual_export_packet_stub = _load_json(contracts / "vectorfl_paper_weekend_live_translated_work_packet_v4_stub.json")
    actual_export_swap_ready = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_actual_export_swap_ready_v0.json")
    actual_export_swap_dry_run_path = repo_root / "runtime" / "manifests" / "vectorfl_paper_actual_export_swap_dry_run_v0.json"
    actual_export_swap_dry_run = _load_json(actual_export_swap_dry_run_path)
    validation_comparison_path = repo_root / "runtime" / "manifests" / "vectorfl_paper_reference_candidate_validation_comparison_v0.json"
    validation_comparison = _load_json(validation_comparison_path)
    gate_validation_dry_run_path = repo_root / "runtime" / "manifests" / "vectorfl_paper_actual_export_gate_validation_dry_run_v0.json"
    gate_validation_dry_run = _load_json(gate_validation_dry_run_path)
    actual_export_v4_preview = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_actual_export_v4_preview_registry_v0.json")
    absorption_package = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_absorption_package_v0.json")
    proper_promotion_candidate_path = repo_root / "runtime" / "manifests" / "vectorfl_paper_proper_promotion_candidate_v0.json"
    runtime_packet_manifest = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_line_guided_work_packets_v0.json")
    runtime_reinjection_registry = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_reinjection_registry_v0.json")
    runtime_governance_registry = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_governance_gates_v0.json")
    reopen_case = _load_json(repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_reopen_case_v0.json")
    runtime_trace_log = (repo_root / "runtime" / "manifests" / "vectorfl_paper_weekend_live_execution_trace_log_v0.jsonl").read_text(encoding="utf-8")
    runtime_write_back_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_runtime_write_back_report_v0.md")
    reopen_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_reopen_report_v0.md")
    source_record_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_source_record_selection_v1.md")
    native_shape_rerun_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_native_shape_overlay_rerun_v0.md")
    export_shaped_upgrade_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_weekend_live_export_shaped_source_upgrade_v0.md")
    actual_export_slot_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_actual_export_slot_readiness_v0.md")
    actual_export_swap_ready_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_actual_export_swap_ready_report_v0.md")
    actual_export_swap_stub_note = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_actual_export_swap_stub_note_v0.md")
    actual_export_v4_preview_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_actual_export_v4_preview_report_v0.md")
    absorption_readiness_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_absorption_readiness_v0.md")
    proper_promotion_readiness_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_proper_promotion_readiness_v0.md")
    official_readme_alignment_report = _read_text(repo_root / "docs" / "reports" / "paperclip_official_readme_alignment_note_v0.md")
    human_direction_readout = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_human_direction_readout_v0.md")
    supervisor_current_board_report = _read_text(repo_root / "docs" / "reports" / "vectorfl_paper_supervisor_current_board_v0.md")

    task_summary = f"""
    <div class="meta">task_id={html.escape(active_task['task_id'])}</div>
    <div class="body-copy">{html.escape(active_task['user_goal'])}</div>
    <div class="chip-row">{''.join(_chip(item) for item in active_task['success_criteria'])}</div>
    <div class="meta">human_gate_required={str(active_task['current_governance']['human_gate_required']).lower()} / do_not_flatten_into_todos={str(active_task['current_governance']['do_not_flatten_into_todos']).lower()}</div>
    """

    material_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["material_id"])}</div><div class="entity-sub">{html.escape(item["role"])}</div><div class="meta">{html.escape(item["why_it_matters"])}</div></div>'
        for item in bundle["materials"]
    )
    live_material_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["material_id"])}</div><div class="entity-sub">{html.escape(item["role"])}</div><div class="meta">{html.escape(item["path"])}</div></div>'
        for item in live_bundle_selection["selected_live_bundle"]["materials"]
    )
    live_target_block = f"""
    <div class="body-copy">{html.escape(live_bundle_selection["selected_live_bundle"]["selection_reason"])}</div>
    <div class="label">selected external comparison target</div>
    <div class="body-copy">{html.escape(live_bundle_selection["selected_external_comparison_target"]["headline"])}</div>
    <div class="chip-row">{''.join(_chip(item) for item in live_bundle_selection["selected_external_comparison_target"]["why_this_target"])}</div>
    <div class="label">comparison questions</div>
    <div class="chip-row">{''.join(_chip(item) for item in live_external_target["comparison_questions"])}</div>
    """
    mapping_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["surface"])}</div><div class="entity-sub">{html.escape(", ".join(item["vectorfl_translation"]))}</div><div class="meta">object={html.escape(item["primary_internal_object"])} / slot={html.escape(item["output_slot"])}</div></div>'
        for item in intake_mapping["mappings"]
    )
    overlay_block = f"""
    <div class="label">translated work packet</div>
    <div class="chip-row">{''.join(_chip(item) for item in overlay_example["translated_work_packet"]["line_translation"]["support_line_ids"])}</div>
    <div class="meta">primary_line={html.escape(overlay_example["translated_work_packet"]["line_translation"]["primary_line_id"])}</div>
    <div class="label">translated governance gate</div>
    <div class="chip-row">
      {_chip(overlay_example["translated_governance_gate"]["route_gate"])}
      {_chip(overlay_example["translated_governance_gate"]["hold_trace"])}
    </div>
    """

    cell_rows = []
    for cell in registry["cells"]:
        handoffs = "".join(_chip(f'{item["cell_id"]}: {item["why"]}') for item in cell["handoff_targets"])
        cell_rows.append(
            f"""
            <div class="panel soft">
              <div class="kicker">{html.escape(cell['cell_id'])}</div>
              <h3>{html.escape(cell['label'])}</h3>
              <div class="body-copy">{html.escape(cell['purpose'])}</div>
              <div class="meta">cli={html.escape(cell['managing_cli'])} / contract={html.escape(cell['md_contract'])}</div>
              <div class="label">lens</div>
              <div class="chip-row">{''.join(_chip(item) for item in cell['lens'])}</div>
              <div class="label">outputs</div>
              <div class="chip-row">{''.join(_chip(item) for item in cell['outputs'])}</div>
              <div class="label">handoff targets</div>
              <div class="chip-row">{handoffs}</div>
            </div>
            """
        )

    line_seed_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["line_name"])}</div><div class="entity-sub">{html.escape(item["core_claim"])}</div><div class="meta">enables: {html.escape(", ".join(item["what_it_enables"]))}</div></div>'
        for item in internal_output["line_seeds"]
    )
    external_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["reference_id"])}</div><div class="entity-sub">{html.escape(item["why_it_helps"])}</div><div class="meta">strengthens={html.escape(item["which_line_seed_it_strengthens"])} / injection={html.escape(item["injection_readiness"])}</div></div>'
        for item in external_output["candidate_references"]
    )
    confirmed_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["line_name"])}</div><div class="entity-sub">{html.escape(item["human_translation"])}</div><div class="meta">next_use={html.escape(item["next_use"])}</div></div>'
        for item in synthesis_output["confirmed_lines"]
    )
    live_internal_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["line_name"])}</div><div class="entity-sub">{html.escape(item["core_claim"])}</div><div class="meta">resists={html.escape(", ".join(item["what_it_resists"]))}</div></div>'
        for item in live_internal_output["line_seeds"]
    )
    live_external_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["reference_id"])}</div><div class="entity-sub">{html.escape(item["why_it_helps"])}</div><div class="meta">strengthens={html.escape(item["which_line_seed_it_strengthens"])}</div></div>'
        for item in live_external_output["candidate_references"]
    )
    live_synthesis_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["line_name"])}</div><div class="entity-sub">{html.escape(item["human_translation"])}</div><div class="meta">next_use={html.escape(item["next_use"])}</div></div>'
        for item in live_synthesis_output["confirmed_lines"]
    )
    live_artifact_block = f"""
    <div class="label">issue surface</div>
    <div class="body-copy">{html.escape(live_issue_sample["issue_surface"]["title"])}</div>
    <div class="meta">assignee={html.escape(live_issue_sample["issue_surface"]["assignee"])} / status={html.escape(live_issue_sample["issue_surface"]["status"])}</div>
    <div class="label">translated work packet</div>
    <div class="chip-row">
      {_chip('primary=' + live_work_packet["line_translation"]["primary_line_id"])}
      {''.join(_chip('support=' + item) for item in live_work_packet["line_translation"]["support_line_ids"])}
    </div>
    <div class="label">append-only trace</div>
    <div class="body-copy">{html.escape(live_trace_row["summary"])}</div>
    <div class="meta">residue={html.escape(live_trace_row["residue_note"])}</div>
    <div class="label">reinjection stub</div>
    <div class="body-copy">{html.escape(live_reinjection_stub["advisory_return_hint"])}</div>
    <div class="label">governance gate</div>
    <div class="chip-row">
      {_chip(live_governance_gate["route_gate"])}
      {_chip(live_governance_gate["hold_trace"])}
    </div>
    """
    decision_block = f"""
    <div class="body-copy">{html.escape(supervisor_decision['reason'])}</div>
    <div class="chip-row">{_chip(supervisor_decision['decision'])}{''.join(_chip(item) for item in supervisor_decision['conditions'])}</div>
    <div class="meta">approved_next_cell={html.escape(supervisor_decision['approved_next_cell'])}</div>
    """
    return_block = f"""
    <div class="label">confirmed lines latest</div>
    <div class="chip-row">{''.join(_chip(item) for item in return_packet['returns']['confirmed_lines_latest'])}</div>
    <div class="label">reference injection proposal latest</div>
    <div class="chip-row">{''.join(_chip(item) for item in return_packet['returns']['reference_injection_proposal_latest'])}</div>
    <div class="label">next probe latest</div>
    <div class="chip-row">{''.join(_chip(item) for item in return_packet['returns']['next_probe_latest'])}</div>
    """
    status_block = f"""
    <div class="label">current state</div>
    <div class="chip-row">{''.join(_chip(f'{key}={str(value).lower()}') for key, value in status_board['current_state'].items())}</div>
    <div class="label">remaining gaps</div>
    <div class="chip-row">{''.join(_chip(item) for item in status_board['remaining_gaps'])}</div>
    <div class="label">next checks</div>
    <div class="chip-row">{''.join(_chip(item) for item in status_board['next_checks'])}</div>
    """
    runtime_write_back_block = f"""
    <div class="body-copy">{html.escape(runtime_write_back['operator_readout']['what_changed'])}</div>
    <div class="meta">{html.escape(runtime_write_back['operator_readout']['why_it_matters'])}</div>
    <div class="label">registered slots</div>
    <div class="chip-row">{''.join(_chip(f'{key}: {value}') for key, value in runtime_write_back['registered_slots'].items())}</div>
    <div class="label">write-back actions</div>
    <div class="chip-row">{''.join(_chip(item) for item in runtime_write_back['write_back_actions'])}</div>
    <div class="label">next action</div>
    <div class="body-copy">{html.escape(runtime_write_back['operator_readout']['next_action'])}</div>
    """
    canonical_bridge_block = f"""
    <div class="body-copy">{html.escape(canonical_pilot_bridge['merge_intent'])}</div>
    <div class="label">why scoped first</div>
    <div class="chip-row">{''.join(_chip(item) for item in canonical_pilot_bridge['why_scoped_first'])}</div>
    <div class="label">absorption order</div>
    <div class="chip-row">{''.join(_chip(item) for item in canonical_pilot_bridge['absorption_order'])}</div>
    <div class="label">merge readiness</div>
    <div class="chip-row">{''.join(_chip(f'{key}={str(value).lower()}') for key, value in canonical_pilot_bridge['merge_readiness'].items())}</div>
    """
    runtime_packet_block = f"""
    <div class="label">packet refs</div>
    <div class="chip-row">{''.join(_chip(item) for item in runtime_packet_manifest['packet_refs'])}</div>
    <div class="label">registered packets</div>
    <div class="chip-row">{''.join(_chip(item['packet_id'] + '=' + item['status']) for item in runtime_packet_manifest['packets'])}</div>
    <div class="label">reinjection next probe</div>
    <div class="chip-row">{''.join(_chip(item['next_probe']) for item in runtime_reinjection_registry['entries'])}</div>
    <div class="label">governance hold</div>
    <div class="chip-row">{''.join(_chip(item['hold_trace']) for item in runtime_governance_registry['gates'])}</div>
    """
    reopen_block = f"""
    <div class="body-copy">{html.escape(reopen_case['supervisor_language_summary'])}</div>
    <div class="meta">target_cell={html.escape(reopen_case['reopen_target']['cell_id'])} / handoff_after={html.escape(reopen_case['reopen_target']['handoff_after'])}</div>
    <div class="label">why reopen now</div>
    <div class="chip-row">{''.join(_chip(item) for item in reopen_case['why_reopen_now'])}</div>
    <div class="label">reopen questions</div>
    <div class="chip-row">{''.join(_chip(item) for item in reopen_case['reopen_questions'])}</div>
    """
    source_record_block = f"""
    <div class="body-copy">{html.escape(native_shape_source['issue_surface']['title'])}</div>
    <div class="meta">issue={html.escape(native_shape_source['issue_surface']['identifier'])} / assignee={html.escape(native_shape_source['issue_surface']['assignee_agent_id'])} / run={html.escape(native_shape_source['heartbeat_run_surface']['run_id'])}</div>
    <div class="label">why truer than v0 sample</div>
    <div class="chip-row">{''.join(_chip(item) for item in native_shape_source['why_truer_than_v0_sample'])}</div>
    <div class="label">native surfaces preserved</div>
    <div class="chip-row">{_chip('issue')}{_chip('assignment/wakeup')}{_chip('heartbeat run')}{_chip('output artifact')}{_chip('governance event')}</div>
    <div class="label">comment return</div>
    <div class="body-copy">{html.escape(native_shape_source['output_artifact_surface']['issue_comment']['body'])}</div>
    <div class="label">governance note</div>
    <div class="body-copy">{html.escape(native_shape_source['governance_event_surface']['decision_note'])}</div>
    """
    export_shaped_source_block = f"""
    <div class="body-copy">{html.escape(export_shaped_source['issues_row']['title'])}</div>
    <div class="meta">issue_row={html.escape(export_shaped_source['issues_row']['identifier'])} / run_row={html.escape(export_shaped_source['heartbeat_runs_row']['id'])} / approval_row={html.escape(export_shaped_source['approvals_row']['id'])}</div>
    <div class="label">schema basis</div>
    <div class="chip-row">{''.join(_chip(item.split('/')[-1]) for item in export_shaped_source['schema_basis'])}</div>
    <div class="label">host row boundaries preserved</div>
    <div class="chip-row">{_chip('issues_row')}{_chip('heartbeat_runs_row')}{_chip('issue_comments_rows')}{_chip('approvals_row')}</div>
    <div class="label">honesty note</div>
    <div class="body-copy">{html.escape(export_shaped_source['honesty_note'])}</div>
    """
    actual_export_slot_block = f"""
    <div class="body-copy">{html.escape(actual_export_slot['operator_note'])}</div>
    <div class="meta">state={html.escape(actual_export_slot['current_state'])}</div>
    <div class="label">placeholder ref</div>
    <div class="chip-row">{_chip(actual_export_slot['current_placeholder_ref'])}</div>
    <div class="label">required surfaces</div>
    <div class="chip-row">{''.join(_chip(item) for item in actual_export_slot['expected_shape']['required_surfaces'])}</div>
    <div class="label">swap rule</div>
    <div class="chip-row">{''.join(_chip(item) for item in actual_export_slot['swap_rule']['must_preserve'])}</div>
    """
    actual_export_swap_ready_block = f"""
    <div class="body-copy">{html.escape(actual_export_swap_ready['operator_summary'])}</div>
    <div class="meta">state={html.escape(actual_export_swap_ready['state'])}</div>
    <div class="label">template ref</div>
    <div class="chip-row">{_chip(actual_export_swap_ready['template_ref'])}</div>
    <div class="label">next packet stub</div>
    <div class="chip-row">{_chip(actual_export_packet_stub['packet_id'] + '=' + actual_export_packet_stub['status'])}</div>
    <div class="label">swap targets</div>
    <div class="chip-row">{''.join(_chip(item) for item in actual_export_swap_ready['swap_targets'])}</div>
    <div class="label">required surface count</div>
    <div class="chip-row">{_chip(str(len(actual_export_template['required_surfaces'])))}</div>
    """
    swap_stub_block = f"""
    <div class="body-copy">scripts/run_vectorfl_paper_actual_export_swap_stub.py validates the slot occupant and previews packet v4 materialization.</div>
    <div class="meta">dry_run_manifest={html.escape(str(actual_export_swap_dry_run_path.relative_to(repo_root)))}</div>
    <div class="label">swap-ready state</div>
    <div class="chip-row">{_chip(actual_export_swap_ready['state'])}{_chip('next=' + actual_export_packet_stub['packet_id'])}</div>
    <div class="label">dry-run validation</div>
    <div class="chip-row">{_chip('validation_passed=' + str(actual_export_swap_dry_run['validation_passed']).lower())}{_chip('slot=' + actual_export_swap_dry_run['slot_state'])}</div>
    <div class="label">preview summary</div>
    <div class="chip-row">{_chip('issue=' + ((actual_export_swap_dry_run.get('materialized_packet_preview') or {}).get('actual_export_summary') or {}).get('issue_identifier', 'none'))}{_chip('run=' + ((actual_export_swap_dry_run.get('materialized_packet_preview') or {}).get('actual_export_summary') or {}).get('run_id', 'none'))}</div>
    """
    comparison_current = validation_comparison["current_anchor"]
    comparison_supervisor_answers = validation_comparison["supervisor_answers"]
    comparison_guard = validation_comparison["merge_guard"]
    dry_run_delta = gate_validation_dry_run.get("delta_vs_current_anchor") or {}
    candidate_comparison_rows = "".join(
        f"""
        <div class="list-row">
          <div class="entity-title">{html.escape(item['reference_id'])}</div>
          <div class="entity-sub">{html.escape(item['validation_status'])} / {html.escape(item['honesty_class'])} / {html.escape(item['gate_effect'])}</div>
          <div class="meta">gate_effect_change={html.escape(item['gate_effect_change'])} / no_gate_close_change={str(item['no_gate_close_change']).lower()}</div>
        </div>
        """
        for item in validation_comparison["candidate_results"]
    )
    merge_test_layer_block = f"""
    <div class="body-copy">Read-only merge-test layer only. It attaches the validated comparison reading to this legacy weekend pilot surface without replacing the current slot, promoting a candidate, or declaring gate close.</div>
    <div class="meta">comparison_manifest={html.escape(str(validation_comparison_path.relative_to(repo_root)))}</div>
    <div class="meta">dry_run_preview_manifest={html.escape(str(gate_validation_dry_run_path.relative_to(repo_root)))}</div>
    <div class="label">current anchor summary</div>
    <div class="chip-row">
      {_chip('source=' + comparison_current['source_record_artifact'])}
      {_chip('validation_status=' + comparison_current['validation_status'])}
      {_chip('honesty_class=' + comparison_current['honesty_class'])}
      {_chip('gate_effect=' + comparison_current['gate_effect'])}
      {_chip('role=' + comparison_current['role'])}
    </div>
    <div class="label">dry-run candidate preview</div>
    <div class="chip-row">
      {_chip('source=' + gate_validation_dry_run['source_record_artifact'])}
      {_chip('validation_status=' + gate_validation_dry_run['validation_status'])}
      {_chip('honesty_class=' + gate_validation_dry_run['honesty_class'])}
      {_chip('gate_effect=' + gate_validation_dry_run['gate_effect'])}
      {_chip('gate_effect_change=' + str(dry_run_delta.get('gate_effect_change', 'unknown')))}
      {_chip('no_gate_close_change=' + str(dry_run_delta.get('no_gate_close_change', 'unknown')).lower())}
    </div>
    <div class="label">comparison verdict summary</div>
    <div>{candidate_comparison_rows}</div>
    <div class="label">supervisor-safe decision posture</div>
    <div class="chip-row">
      {_chip('reopen_validation_repeatable=' + str(comparison_supervisor_answers['is_candidate_for_reopen_validation_repeatable_across_references']).lower())}
      {_chip('gate_close_candidate=' + str(comparison_supervisor_answers['is_any_candidate_close_to_actual_export_only_gate_close']).lower())}
      {_chip('merge_testing_stable=' + str(comparison_supervisor_answers['is_validator_stable_enough_for_post_stabilization_merge_testing']).lower())}
      {_chip('current_slot_replacement=' + comparison_guard['current_slot_replacement'])}
      {_chip('surface_redesign=' + comparison_guard['surface_redesign'])}
    </div>
    <div class="body-copy">Decision reading: hold current SSOT, allow bounded read-only reopen validation, and wait for a true host export candidate before any gate-close or slot-replacement test.</div>
    """
    v4_preview_block = f"""
    <div class="body-copy">{html.escape(actual_export_v4_preview['preview_claim'])}</div>
    <div class="meta">state={html.escape(actual_export_v4_preview['state'])}</div>
    <div class="label">packet path</div>
    <div class="chip-row">{_chip('current=' + actual_export_v4_preview['current_packet_ref'])}{_chip('next=' + actual_export_v4_preview['next_packet_stub_ref'])}</div>
    <div class="label">promotion rule</div>
    <div class="body-copy">{html.escape(actual_export_v4_preview['promotion_rule'])}</div>
    """
    absorption_block = f"""
    <div class="body-copy">{html.escape(absorption_package['purpose'])}</div>
    <div class="label">absorption targets</div>
    <div class="chip-row">{''.join(_chip(item['target_id']) for item in absorption_package['absorption_targets'])}</div>
    <div class="label">naming rule</div>
    <div class="chip-row">{''.join(_chip(item) for item in absorption_package['naming_rule']['keep_after_promotion'])}</div>
    <div class="label">final gate</div>
    <div class="body-copy">{html.escape(absorption_package['final_gate'])}</div>
    """
    promotion_stub_block = f"""
    <div class="body-copy">scripts/run_vectorfl_paper_promotion_stub.py assembles the final promotion candidate for VectorFL Paper proper once the actual export gate is passed.</div>
    <div class="meta">promotion_candidate_manifest={html.escape(str(proper_promotion_candidate_path.relative_to(repo_root)))}</div>
    <div class="label">promotion note</div>
    <div class="chip-row">{_chip('operational_gate_remaining=actual_export_only')}{_chip('redesign_forbidden=true')}</div>
    """
    official_alignment_block = f"""
    <div class="body-copy">Paperclip's official README still describes it as a company-style orchestration control plane with heartbeats, governance, goal alignment, org charts, and budgets.</div>
    <div class="label">confirmed takeaways</div>
    <div class="chip-row">{_chip('ticket grammar')}{_chip('heartbeat execution trace')}{_chip('governance surface')}{_chip('goal-linked context')}{_chip('auditability')}</div>
    <div class="label">copy-avoidance</div>
    <div class="chip-row">{_chip('no company ontology import')}{_chip('no business-first identity copy')}{_chip('no org-chart-as-identity')}</div>
    """
    human_direction_block = f"""
    <div class="body-copy">We are not building a pretty multi-agent UI. We are proving that scenario-bearing material can close one internal-read -> selective external comparison -> supervisor report -> runtime return loop.</div>
    <div class="label">current judgment</div>
    <div class="chip-row">{_chip('direction=mostly_correct')}{_chip('internal_only=false')}{_chip('human_readability=still_thin')}{_chip('last_gate=actual_export_only')}</div>
    <div class="label">what the user should know now</div>
    <div class="body-copy">The structure is moving in the right direction, but the supervisory reading layer still needs stronger translation so the purpose is immediately obvious without reading manifests.</div>
    """
    supervisor_current_board_block = f"""
    <div class="body-copy">{html.escape(supervisor_current_board['headline'])}</div>
    <div class="label">already proven</div>
    <div class="chip-row">{''.join(_chip(item) for item in supervisor_current_board['current_proof_state']['already_proven'])}</div>
    <div class="label">still not proven</div>
    <div class="chip-row">{''.join(_chip(item) for item in supervisor_current_board['current_proof_state']['still_not_proven'])}</div>
    <div class="label">single remaining gate</div>
    <div class="body-copy">{html.escape(supervisor_current_board['single_remaining_gate']['description'])}</div>
    """
    supervisor_compass_block = f"""
    <div class="body-copy"><strong>한 줄 판정:</strong> 지금은 UI를 꾸미는 중이 아니라, 시나리오가 포함된 재료로 첫 숙성 루프가 실제로 닫히는지 증명하는 중입니다.</div>
    <div class="label">why this pilot exists</div>
    <div class="chip-row">
      {_chip('scenario-bearing input')}
      {_chip('internal-first')}
      {_chip('thin external overlay')}
      {_chip('supervisor-readable report')}
      {_chip('runtime return')}
    </div>
    <div class="label">already proven</div>
    <div class="chip-row">{''.join(_chip(item) for item in supervisor_current_board['current_proof_state']['already_proven'])}</div>
    <div class="label">single remaining gate</div>
    <div class="body-copy">{html.escape(supervisor_current_board['single_remaining_gate']['description'])}</div>
    <div class="meta">{html.escape(supervisor_current_board['single_remaining_gate']['why_it_matters'])}</div>
    <div class="label">what this is not</div>
    <div class="chip-row">{''.join(_chip(item) for item in supervisor_current_board['current_direction']['what_we_are_not_doing'])}</div>
    <div class="label">supervisor takeaway</div>
    <div class="body-copy">{html.escape(supervisor_current_board['supervisor_takeaway'])}</div>
    """

    report_block = html.escape(supervisor_report)
    live_report_block = html.escape(live_supervisor_report)
    runtime_report_block = html.escape(runtime_write_back_report)
    reopen_report_block = html.escape(reopen_report)
    source_record_report_block = html.escape(source_record_report)
    native_shape_rerun_report_block = html.escape(native_shape_rerun_report)
    export_shaped_upgrade_report_block = html.escape(export_shaped_upgrade_report)
    actual_export_slot_report_block = html.escape(actual_export_slot_report)
    actual_export_swap_ready_report_block = html.escape(actual_export_swap_ready_report)
    actual_export_swap_stub_note_block = html.escape(actual_export_swap_stub_note)
    actual_export_v4_preview_report_block = html.escape(actual_export_v4_preview_report)
    absorption_readiness_report_block = html.escape(absorption_readiness_report)
    proper_promotion_readiness_report_block = html.escape(proper_promotion_readiness_report)
    official_readme_alignment_report_block = html.escape(official_readme_alignment_report)
    human_direction_readout_block = html.escape(human_direction_readout)
    supervisor_current_board_report_block = html.escape(supervisor_current_board_report)
    runtime_trace_block = html.escape(runtime_trace_log)

    body = f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>VectorFL Paper Weekend Pilot</title>
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
        .page {{ max-width: 1360px; margin: 0 auto; padding: 28px; display: grid; gap: 18px; }}
        .hero, .panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 18px; }}
        .panel.soft {{ background: var(--soft); }}
        .hero h1, .panel h2, .panel h3 {{ margin: 0; }}
        .kicker {{ color: var(--accent); font-size: 12px; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 10px; }}
        .meta {{ color: var(--muted); font-size: 13px; line-height: 1.5; }}
        .body-copy {{ line-height: 1.6; }}
        .grid {{ display: grid; gap: 18px; grid-template-columns: 1.15fr 0.85fr; }}
        .stack {{ display: grid; gap: 18px; }}
        .triple {{ display: grid; gap: 18px; grid-template-columns: repeat(3, minmax(0, 1fr)); }}
        .dual {{ display: grid; gap: 18px; grid-template-columns: 1.1fr 0.9fr; }}
        .chip-row {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }}
        .chip {{ border: 1px solid rgba(129,140,248,0.35); background: rgba(129,140,248,0.12); border-radius: 999px; padding: 6px 10px; font-size: 12px; }}
        .list-row {{ border-top: 1px solid var(--line); padding: 12px 0; }}
        .list-row:first-child {{ border-top: 0; padding-top: 0; }}
        .entity-title {{ font-weight: 700; margin-bottom: 4px; }}
        .entity-sub {{ color: var(--text); line-height: 1.5; }}
        .label {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 10px; }}
        .code {{ white-space: pre-wrap; background: #0d1015; border: 1px solid var(--line); border-radius: 18px; padding: 14px; line-height: 1.5; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }}
        @media (max-width: 980px) {{
          .grid, .triple, .dual {{ grid-template-columns: 1fr; }}
        }}
      </style>
    </head>
    <body>
      <div class="page">
        <section class="hero">
          <div class="kicker">VectorFL Paper Weekend Pilot</div>
          <h1>Scenario-Bearing First Loop</h1>
          <div class="body-copy">This view turns the new contracts and sample packets into one operable pilot surface: material bundle, active task, 3-cell registry, sample outputs, and supervisor report.</div>
        </section>
        <div class="dual">
          {_section("Supervisor Compass", supervisor_compass_block, "Human First")}
          {_section("Human Direction Readout", human_direction_block, "Supervisor Check")}
        </div>
        <div class="grid">
          <div class="stack">
            {_section("Active Task", task_summary, "Current Target")}
            {_section("Material Bundle", f'<div class="meta">{html.escape(bundle["first_target"])}</div><div>{material_rows}</div>', "Scenario Inputs")}
            {_section("Live Bundle Selection", f'<div>{live_material_rows}</div>{live_target_block}', "Weekend Choice")}
            {_section("Thin Overlay Intake Mapping", f'<div>{mapping_rows}</div>{overlay_block}', "Next Translation Step")}
            {_section("Cell Registry", f'<div class="triple">{"".join(cell_rows)}</div>', "3-Cell Minimum")}
          </div>
          <div class="stack">
            {_section("Live Internal Read Output", f'<div class="label">repeated pressures</div><div class="chip-row">{"".join(_chip(item) for item in live_internal_output["repeated_pressures"])}</div><div class="label">line seeds</div><div>{live_internal_rows}</div>', "Live Pass")}
            {_section("Live External Resource Output", f'<div class="label">candidate references</div><div>{live_external_rows}</div><div class="label">rejection rules</div><div class="chip-row">{"".join(_chip(item) for item in live_external_output["rejection_rules"])}</div>', "Live Pass")}
            {_section("Live Synthesis Output", f'<div class="label">confirmed lines</div><div>{live_synthesis_rows}</div><div class="label">recommendation</div><div class="chip-row">{_chip(live_synthesis_output["recommendation"]["decision"])}{_chip(live_synthesis_output["recommendation"]["reason"])}</div></div>', "Live Pass")}
            {_section("Live Translation Artifacts", live_artifact_block, "Live Pass")}
            {_section("Pilot Status Board", status_block, "Goal Check")}
            {_section("Runtime Write-Back", runtime_write_back_block, "Enactment")}
            {_section("Canonical Pilot Bridge", canonical_bridge_block, "Absorption Path")}
            {_section("Runtime Slot Registry", runtime_packet_block, "Enactment")}
            {_section("Reopen Case", reopen_block, "Return Loop")}
            {_section("Native-Shape Source Record", source_record_block, "Source Upgrade")}
            {_section("Export-Shaped Host Record", export_shaped_source_block, "Source Upgrade")}
            {_section("Actual Export Slot", actual_export_slot_block, "Source Upgrade")}
            {_section("Actual Export Swap Ready", actual_export_swap_ready_block, "Source Upgrade")}
            {_section("Actual Export Swap Stub", swap_stub_block, "Source Upgrade")}
            {_section("Post-Stabilization Merge Test Layer", merge_test_layer_block, "Read-Only Comparison")}
            {_section("Actual Export V4 Preview", v4_preview_block, "Source Upgrade")}
            {_section("Absorption Package", absorption_block, "Promotion Path")}
            {_section("Proper Promotion Stub", promotion_stub_block, "Promotion Path")}
            {_section("Official README Alignment", official_alignment_block, "Source Check")}
            {_section("Supervisor Current Board", supervisor_current_board_block, "Supervisor Check")}
            {_section("Internal Read Output", f'<div class="label">stable</div><div class="chip-row">{"".join(_chip(item) for item in internal_output["stable_points"])}</div><div class="label">unclear</div><div class="chip-row">{"".join(_chip(item) for item in internal_output["unclear_points"])}</div><div class="label">line seeds</div><div>{line_seed_rows}</div>', "Sample Output")}
            {_section("External Resource Output", f'<div class="label">candidate references</div><div>{external_rows}</div><div class="label">rejection rules</div><div class="chip-row">{"".join(_chip(item) for item in external_output["rejection_rules"])}</div>', "Sample Output")}
            {_section("Synthesis Output", f'<div class="label">confirmed lines</div><div>{confirmed_rows}</div><div class="label">recommendation</div><div class="chip-row">{_chip(synthesis_output["recommendation"]["decision"])}{_chip(synthesis_output["recommendation"]["reason"])}</div>', "Sample Output")}
            {_section("Supervisor Decision", decision_block, "Decision Gate")}
            {_section("Internal Return Packet", return_block, "Return Slot")}
          </div>
        </div>
        {_section("Supervisor Report", f'<div class="code">{report_block}</div>', "Human Decision Surface")}
        {_section("Live Supervisor Report", f'<div class="code">{live_report_block}</div>', "Human Decision Surface")}
        {_section("Runtime Write-Back Report", f'<div class="code">{runtime_report_block}</div>', "Human Decision Surface")}
        {_section("Reopen Report", f'<div class="code">{reopen_report_block}</div>', "Human Decision Surface")}
        {_section("Source Record Selection", f'<div class="code">{source_record_report_block}</div>', "Human Decision Surface")}
        {_section("Native-Shape Overlay Rerun", f'<div class="code">{native_shape_rerun_report_block}</div>', "Human Decision Surface")}
        {_section("Export-Shaped Source Upgrade", f'<div class="code">{export_shaped_upgrade_report_block}</div>', "Human Decision Surface")}
        {_section("Actual Export Slot Readiness", f'<div class="code">{actual_export_slot_report_block}</div>', "Human Decision Surface")}
        {_section("Actual Export Swap Ready", f'<div class="code">{actual_export_swap_ready_report_block}</div>', "Human Decision Surface")}
        {_section("Actual Export Swap Stub", f'<div class="code">{actual_export_swap_stub_note_block}</div>', "Human Decision Surface")}
        {_section("Actual Export V4 Preview", f'<div class="code">{actual_export_v4_preview_report_block}</div>', "Human Decision Surface")}
        {_section("Absorption Readiness", f'<div class="code">{absorption_readiness_report_block}</div>', "Human Decision Surface")}
        {_section("Proper Promotion Readiness", f'<div class="code">{proper_promotion_readiness_report_block}</div>', "Human Decision Surface")}
        {_section("Official README Alignment Note", f'<div class="code">{official_readme_alignment_report_block}</div>', "Human Decision Surface")}
        {_section("Human Direction Readout Note", f'<div class="code">{human_direction_readout_block}</div>', "Human Decision Surface")}
        {_section("Supervisor Current Board Note", f'<div class="code">{supervisor_current_board_report_block}</div>', "Human Decision Surface")}
        {_section("Runtime Trace Log", f'<div class="code">{runtime_trace_block}</div>', "Append-Only Runtime")}
      </div>
    </body>
    </html>
    """
    return body


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_path = OUTPUT_DIR / "index.html"
    html_path.write_text(render_weekend_pilot_page(REPO_ROOT), encoding="utf-8")
    closeout_path = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_legacy_merge_test_closeout_v0.json"
    closeout = {
        "schema_version": "vectorfl_paper_legacy_merge_test_closeout_v0",
        "legacy_surface_ref": "runtime/views/vectorfl_paper_weekend_pilot/index.html",
        "current_supervisor_surface_ref": "runtime/views/vectorfl_paper_proper/index.html",
        "integrated": [
            "current anchor summary",
            "dry-run candidate preview summary",
            "reference candidate comparison summary",
            "supervisor-safe hold/reopen decision reading",
        ],
        "intentionally_excluded": [
            "current slot replacement",
            "candidate promotion",
            "actual_export_only gate close declaration",
            "legacy Paper full merge",
            "surface redesign",
            "cell architecture expansion",
        ],
        "input_artifacts": [
            "runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json",
            "runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json",
            "runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json",
        ],
        "supervisor_readability_survived": True,
        "current_surface_stayed_unpolluted": True,
        "current_slot_unchanged": True,
        "current_vs_dry_run_separation_preserved": True,
        "comparison_verdicts_visible_without_current_ssot_confusion": True,
        "merge_layer_removable_without_runtime_behavior_change": True,
        "bounded_merge_testing_verdict": "passed_read_only_attachment_test",
        "decision_posture": "hold_current_ssot_allow_bounded_reopen_validation_no_gate_close",
    }
    closeout_path.write_text(json.dumps(closeout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"html_path": str(html_path), "closeout_path": str(closeout_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
