from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json

from app.runtime.vectorfl_page_route_aware_mock import (
    PRIMARY_SURFACES,
    build_vectorfl_page_route_aware_mock_data,
)


SURFACE_LABELS = {
    "current-reading": "Current Reading",
    "cases-queue": "Cases / Queue",
    "inputs-intake": "Inputs / Intake",
    "history-trace": "History / Trace",
    "programs-connections": "Programs / Connections",
}


def _read_json_if_present(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"_error": f"malformed json: {path}"}


def _list_count(value: Any) -> int:
    return len(value) if isinstance(value, list) else 0


def _build_paper_operating_bridge_preview(repo_root: Path) -> Dict[str, Any]:
    manifest_root = repo_root / "runtime" / "manifests"
    paths = {
        "handoff": manifest_root / "vectorfl_paper_codex_handoff_latest_v0.json",
        "codex_return": manifest_root / "vectorfl_paper_codex_return_latest_v0.json",
        "gemini_review": manifest_root / "vectorfl_paper_gemini_review_latest_v0.json",
        "supervisor_decision": manifest_root / "vectorfl_paper_supervisor_decision_latest_v0.json",
        "slot": manifest_root / "vectorfl_paper_actual_export_host_record_slot_v0.json",
        "validation_latest": manifest_root / "vectorfl_paper_actual_export_gate_validation_latest_v0.json",
        "validation_dry_run": manifest_root / "vectorfl_paper_actual_export_gate_validation_dry_run_v0.json",
        "comparison": manifest_root / "vectorfl_paper_reference_candidate_validation_comparison_v0.json",
    }
    manifests = {key: _read_json_if_present(path) for key, path in paths.items()}
    decision = manifests["supervisor_decision"]
    latest = manifests["validation_latest"]
    dry_run = manifests["validation_dry_run"]
    comparison = manifests["comparison"]
    comparison_answers = comparison.get("supervisor_answers") or {}

    return {
        "kind": "paper_operating_bridge_preview",
        "mode": "read_only_projection",
        "source_manifests": {key: str(path.relative_to(repo_root)) for key, path in paths.items()},
        "current_posture": decision.get("decision") or "unknown",
        "current_ssot_label": "current_ssot: actual_export_host_record_slot remains unchanged",
        "preview_only_label": "preview_only: dry-run candidate does not replace current slot",
        "summary_only_label": "summary_only: reference comparison is a supervisor reading aid",
        "codex_bridge_status": manifests["codex_return"].get("status") or manifests["handoff"].get("status") or "unknown",
        "gemini_review_status": manifests["gemini_review"].get("review_status") or "unknown",
        "supervisor_decision": decision.get("decision") or "unknown",
        "supervisor_rationale": decision.get("rationale") or "none",
        "gate_effect": latest.get("gate_effect") or "unknown",
        "validation_status": latest.get("validation_status") or "unknown",
        "honesty_class": latest.get("honesty_class") or "unknown",
        "dry_run_gate_effect": dry_run.get("gate_effect") or "none",
        "dry_run_honesty_class": dry_run.get("honesty_class") or "none",
        "comparison_repeatable_reopen": comparison_answers.get("is_candidate_for_reopen_validation_repeatable_across_references"),
        "comparison_gate_close_candidate": comparison_answers.get("is_any_candidate_close_to_actual_export_only_gate_close"),
        "comparison_candidate_count": _list_count(comparison.get("candidate_results")),
        "next_gate": decision.get("continue_gate") or latest.get("recommendation") or "wait_for_true_host_export_candidate",
        "return_route": "current-reading -> programs-connections -> history-trace -> current-reading",
        "guard_language": [
            "no gate close",
            "no slot replacement",
            "no candidate promotion",
            "proper/weekend surfaces are not imported wholesale",
        ],
    }


def _build_paper_proper_translation_payload(repo_root: Path) -> Dict[str, Any]:
    contract_root = repo_root / "runtime" / "contracts"
    page_tree = _read_json_if_present(contract_root / "vectorfl_paper_proper_page_tree_v0.json")
    operating_board = _read_json_if_present(contract_root / "vectorfl_paper_operating_board_sections_v0.json")
    cell_worker = _read_json_if_present(contract_root / "vectorfl_paper_cell_worker_panel_sections_v0.json")
    trace_governance = _read_json_if_present(contract_root / "vectorfl_paper_trace_governance_sections_v0.json")

    return {
        "kind": "paper_proper_translation_payload",
        "mode": "paperclip_design_reference_translated_to_vectorfl",
        "source_contracts": {
            "page_tree": "runtime/contracts/vectorfl_paper_proper_page_tree_v0.json",
            "operating_board": "runtime/contracts/vectorfl_paper_operating_board_sections_v0.json",
            "cell_worker_panel": "runtime/contracts/vectorfl_paper_cell_worker_panel_sections_v0.json",
            "trace_governance": "runtime/contracts/vectorfl_paper_trace_governance_sections_v0.json",
        },
        "source_design_locks": [
            "docs/specs/vectorfl_paper_ui_design_reference_lock_v0.md",
            "docs/specs/paperclip_frame_component_extraction_reading_v0.md",
            "docs/reports/paperclip_git_search_surface_translation_v0.md",
        ],
        "top_direction": page_tree.get("top_direction") or "VectorFL Paper proper should preserve one operating loop.",
        "flow_rule": page_tree.get("flow_rule") or [],
        "paperclip_translation": page_tree.get("paperclip_translation") or {},
        "operating_board_sections": operating_board.get("section_order") or [],
        "operating_board_rules": operating_board.get("global_rules") or [],
        "cell_worker_sections": cell_worker.get("section_order") or [],
        "cell_worker_rules": cell_worker.get("global_rules") or [],
        "trace_governance_sections": trace_governance.get("section_order") or [],
        "trace_governance_rules": trace_governance.get("global_rules") or [],
        "design_translation_rules": [
            "compact metric and status strips before hero presentation",
            "border-led operating lists over soft card stacks",
            "bounded panel roles: navigation, primary surface, governance carry, contextual detail",
            "Paperclip frame grammar is reused; company/issue/agent ontology is not imported",
        ],
        "operator_language_rule": (
            "Use Paper proper operating language: supervisor entrypoint, active loop, cell/CLI ownership, "
            "governance gate, return slot, reopen, and next-loop trigger."
        ),
    }


def build_vectorfl_page_app_shell_state(repo_root: Path, *, active_surface: str) -> Dict[str, Any]:
    data = build_vectorfl_page_route_aware_mock_data(repo_root, active_surface=active_surface)
    surface_links = {
        surface: f"{surface}.html"
        for surface in PRIMARY_SURFACES
    }
    data["paper_operating_bridge_preview"] = _build_paper_operating_bridge_preview(repo_root)
    data["paper_proper_translation_payload"] = _build_paper_proper_translation_payload(repo_root)
    data["shell_runtime"] = {
        "kind": "vectorfl_page_app_shell",
        "active_surface": active_surface,
        "surface_links": surface_links,
        "index_href": "index.html",
    }
    return data


def render_vectorfl_page_app_shell_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page Shell</title>
  <style>
    :root {
      --bg: #f3f5f7;
      --panel: #fcfcfd;
      --panel-soft: #f7f8fa;
      --line: #d7dde4;
      --line-strong: #0f172a;
      --ink: #111827;
      --muted: #667085;
      --chip: #eef2f6;
      --accent-soft: #f0f4f8;
      --warn-bg: #f8f2df;
      --warn-line: #b98a32;
      --active-bg: #eef2f6;
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    a { color: inherit; text-decoration: none; }
    .page { max-width: 1860px; margin: 0 auto; padding: 12px; display: grid; gap: 10px; }
    .topbar, .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 0; }
    .topbar { padding: 12px 14px; display: grid; gap: 10px; }
    .frame { display: grid; grid-template-columns: 228px minmax(0, 1.6fr) 336px; gap: 14px; align-items: start; }
    .panel { padding: 12px; display: grid; gap: 10px; }
    .panel.soft { background: var(--panel-soft); }
    .stack { display: grid; gap: 10px; }
    .primary-panel { gap: 12px; }
    .list-panel { gap: 8px; }
    .log-panel { gap: 8px; }
    .inspector-panel { background: var(--panel-soft); gap: 8px; }
    .nav-panel { align-self: start; position: sticky; top: 12px; }
    .main-column { display: grid; gap: 10px; }
    .right-column { display: grid; gap: 10px; }
    .nav-stack { display: grid; gap: 0; border: 1px solid var(--line); }
    .nav-item, .context-link { display: grid; gap: 4px; border-bottom: 1px solid var(--line); padding: 10px 12px; background: #fcfcfd; color: var(--ink); }
    .nav-item:last-child, .context-link:last-child { border-bottom: 0; }
    .nav-item.active { background: var(--active-bg); }
    .context-link { background: var(--panel-soft); }
    .kicker, .label { color: var(--muted); font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; font-weight: 600; }
    .eyebrow { color: var(--muted); font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 700; }
    h1, h2, h3 { margin: 0; color: var(--ink); }
    h1 { font-size: 19px; font-weight: 700; letter-spacing: -0.01em; }
    h2 { font-size: 15px; font-weight: 600; }
    h3 { font-size: 14px; font-weight: 600; }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--muted); }
    .chip-row { display: flex; flex-wrap: wrap; gap: 6px; }
    .chip { display: inline-flex; align-items: center; border-radius: 999px; padding: 4px 8px; font-size: 11px; background: var(--chip); color: var(--ink); border: 1px solid var(--line); }
    .card { border: 1px solid var(--line); background: #fcfcfd; padding: 10px; display: grid; gap: 6px; }
    .trace-item { background: #fcfcfd; padding: 10px 0; display: grid; gap: 6px; border-bottom: 1px solid var(--line); }
    .trace-item:first-child { padding-top: 0; }
    .trace-item:last-child { border-bottom: 0; padding-bottom: 0; }
    .list-shell { border: 1px solid var(--line); background: #fcfcfd; }
    .list-row { display: grid; gap: 6px; padding: 10px 12px; border-bottom: 1px solid var(--line); }
    .list-row:last-child { border-bottom: 0; }
    .row-head { display: flex; align-items: baseline; justify-content: space-between; gap: 8px; }
    .metric-strip { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0; border: 1px solid var(--line); background: #fcfcfd; }
    .metric-cell { padding: 10px 12px; border-right: 1px solid var(--line); display: grid; gap: 4px; }
    .metric-cell:last-child { border-right: 0; }
    .metric-value { font-size: 19px; font-weight: 700; line-height: 1; letter-spacing: -0.02em; }
    .body-copy { line-height: 1.65; white-space: pre-wrap; font-size: 13px; }
    .simple-list { display: grid; gap: 4px; margin: 0; padding-left: 18px; font-size: 13px; }
    .warn { border: 1px solid var(--warn-line); background: var(--warn-bg); color: #8a5a2b; padding: 10px; display: grid; gap: 6px; }
    .breadcrumb { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .breadcrumb .sep { color: var(--muted); }
    .toolbar-links { display: flex; flex-wrap: wrap; gap: 8px; }
    .toolbar-link { border: 1px solid var(--line); padding: 5px 8px; background: #fcfcfd; color: var(--ink); font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; }
    .section-head { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
    .panel-divider { border-top: 1px solid var(--line); margin-top: 2px; padding-top: 10px; }
    .surface-head { display: grid; gap: 5px; padding-bottom: 10px; border-bottom: 1px solid var(--line); }
    .shell-note { color: var(--muted); font-size: 12px; line-height: 1.45; }
    .dense-row { display: grid; gap: 2px; }
    .main-reading { display: grid; gap: 12px; }
    .reading-block { border-left: 2px solid var(--line); padding-left: 12px; }
    .inspector-block { border-top: 1px solid var(--line); padding-top: 10px; display: grid; gap: 8px; }
    .page-toolbar { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 10px 0 0; border-top: 1px solid var(--line); }
    .page-tabs { display: flex; flex-wrap: wrap; gap: 0; border: 1px solid var(--line); background: #fcfcfd; }
    .page-tab { padding: 7px 11px; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; border-right: 1px solid var(--line); background: #fcfcfd; color: var(--muted); }
    .page-tab:last-child { border-right: 0; }
    .page-tab.active { color: var(--ink); background: var(--active-bg); }
    .entity-list { border: 1px solid var(--line); background: #fcfcfd; }
    .entity-row { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, .8fr) auto; gap: 12px; align-items: center; padding: 11px 12px; border-bottom: 1px solid var(--line); }
    .entity-row:last-child { border-bottom: 0; }
    .entity-main { display: grid; gap: 4px; min-width: 0; }
    .entity-title { font-size: 13px; font-weight: 600; color: var(--ink); }
    .entity-sub { font-size: 12px; color: var(--muted); line-height: 1.45; }
    .entity-meta { display: grid; gap: 2px; justify-items: start; }
    .entity-actions { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 6px; }
    .summary-grid { display: grid; grid-template-columns: 1.3fr .9fr; gap: 10px; }
    .detail-grid { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, .9fr); gap: 10px; }
    .reading-slab { border: 1px solid var(--line); background: #fcfcfd; padding: 12px; display: grid; gap: 8px; }
    .activity-list { border: 1px solid var(--line); background: #fcfcfd; }
    .activity-row { display: grid; gap: 4px; padding: 10px 12px; border-bottom: 1px solid var(--line); }
    .activity-row:last-child { border-bottom: 0; }
    .mini-stat-row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0; border: 1px solid var(--line); background: #fcfcfd; }
    .mini-stat { padding: 9px 10px; border-right: 1px solid var(--line); display: grid; gap: 3px; }
    .mini-stat:last-child { border-right: 0; }
    .inspector-title { font-size: 12px; font-weight: 600; color: var(--ink); }
  </style>
</head>
<body>
  <script id="vectorfl-page-app-shell-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-app-shell-data').textContent);
    const app = document.getElementById('app');
    const runtime = data.shell_runtime || {};
    const routeState = data.route_state_preview || {};
    const current = data.current_reading || {};
    const body = current.body || {};
    const lane = current.lane || {};
    const governance = current.governance || {};
    const responsibility = data.current_responsibility || {};
    const progression = data.progression_preview || {};
    const queue = data.queue_preview || [];
    const intake = data.inputs_preview || {};
    const history = data.history_trace_preview || {};
    const programs = data.programs_connections_preview || {};
    const detailPanels = data.organ_detail_panels || {};
    const contextualLinkMap = routeState.contextual_link_map || {};
    const bridge = data.paper_operating_bridge_preview || {};
    const paper = data.paper_proper_translation_payload || {};
    const metricStrip = [
      { label: 'Active Surface', value: routeState.active_primary_surface || runtime.active_surface || 'unknown', note: routeState.active_nav_key || 'none' },
      { label: 'Current Organ', value: responsibility.current_organ_ref || 'unknown', note: lane.lane_kind || 'no lane' },
      { label: 'Restrictions', value: String((governance.restriction_flags || []).length), note: (governance.hold_state || 'none') },
      { label: 'Trace Rows', value: String((history.latest_trace_list || []).length), note: programs.connection_state || 'no connection state' },
    ];

    function esc(value) {
      return String(value ?? '')
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
    }

    function chip(text) {
      return `<span class="chip">${esc(text)}</span>`;
    }

    function renderBridgePostureStrip() {
      if (!bridge.kind) return '';
      return `
        <section class="panel inspector-panel">
          <div class="section-head">
            <div>
              <div class="kicker">Paper Operating Bridge</div>
              <h3>Current supervisor posture</h3>
            </div>
            <div class="mono">${esc(bridge.current_posture || 'unknown')}</div>
          </div>
          <div class="chip-row">
            ${chip(bridge.current_ssot_label || 'current_ssot')}
            ${chip(bridge.preview_only_label || 'preview_only')}
            ${chip(bridge.summary_only_label || 'summary_only')}
          </div>
          <div class="body-copy">${esc(bridge.supervisor_rationale || 'none')}</div>
          <div class="meta">next gate: ${esc(bridge.next_gate || 'none')}</div>
        </section>
      `;
    }

    function renderBridgeAuditBlock() {
      if (!bridge.kind) return '';
      return `
        <section class="panel inspector-panel">
          <div class="section-head">
            <div>
              <div class="kicker">Paper Bridge Audit</div>
              <h3>Gate / validation reading</h3>
            </div>
            <div class="mono">${esc(bridge.gate_effect || 'unknown')}</div>
          </div>
          <div class="mini-stat-row">
            <div class="mini-stat"><div class="kicker">latest</div><div class="mono">${esc(bridge.validation_status || 'unknown')}</div></div>
            <div class="mini-stat"><div class="kicker">honesty</div><div class="mono">${esc(bridge.honesty_class || 'unknown')}</div></div>
            <div class="mini-stat"><div class="kicker">dry-run</div><div class="mono">${esc(bridge.dry_run_gate_effect || 'none')}</div></div>
          </div>
          <div class="chip-row">
            ${chip(`comparison candidates=${bridge.comparison_candidate_count ?? 0}`)}
            ${chip(`repeatable_reopen=${bridge.comparison_repeatable_reopen === true ? 'yes' : 'no'}`)}
            ${chip(`gate_close_candidate=${bridge.comparison_gate_close_candidate === true ? 'yes' : 'no'}`)}
          </div>
          <div class="meta">guard: ${(bridge.guard_language || []).map(esc).join(' / ') || 'none'}</div>
        </section>
      `;
    }

    function renderBridgeConnectionBlock() {
      if (!bridge.kind) return '';
      return `
        <section class="panel inspector-panel">
          <div class="section-head">
            <div>
              <div class="kicker">Paper Bridge Connections</div>
              <h3>Codex / Gemini availability</h3>
            </div>
            <div class="mono">${esc(bridge.mode || 'read_only_projection')}</div>
          </div>
          <div class="metric-strip">
            <div class="metric-cell"><div class="kicker">codex</div><div class="mono">${esc(bridge.codex_bridge_status || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">gemini</div><div class="mono">${esc(bridge.gemini_review_status || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">decision</div><div class="mono">${esc(bridge.supervisor_decision || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">route</div><div class="mono">${esc(bridge.return_route || 'none')}</div></div>
          </div>
          <div class="meta">This shell reads the bridge state only. It does not run workers, replace slots, promote candidates, or close gates.</div>
        </section>
      `;
    }

    function renderPaperProperCurrentSurface() {
      if (!paper.kind) return '';
      return `
        <section class="panel primary-panel">
          <div class="surface-head">
            <div class="section-head">
              <div>
                <div class="kicker">Primary Surface / VectorFL Paper Proper</div>
                <h2>Supervisor operating board</h2>
              </div>
              <div class="mono">${esc(paper.mode || 'translated')}</div>
            </div>
            <div class="shell-note">${esc(paper.top_direction || 'one operating loop')}</div>
          </div>
          ${renderBridgePostureStrip()}
          <div class="metric-strip">
            <div class="metric-cell"><div class="kicker">posture</div><div class="mono">${esc(bridge.current_posture || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">codex</div><div class="mono">${esc(bridge.codex_bridge_status || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">gemini</div><div class="mono">${esc(bridge.gemini_review_status || 'unknown')}</div></div>
            <div class="metric-cell"><div class="kicker">gate</div><div class="mono">${esc(bridge.gate_effect || 'unknown')}</div></div>
          </div>
          <div class="detail-grid">
            <div class="reading-slab">
              <div class="label">Operating board sections</div>
              <div class="entity-list">
                ${(paper.operating_board_sections || []).map((item) => `
                  <div class="list-row">
                    <div class="row-head"><strong>${esc(item)}</strong><span class="mono">board</span></div>
                  </div>
                `).join('')}
              </div>
              <div class="label">Paperclip translation map</div>
              <div class="list-shell">
                ${Object.entries(paper.paperclip_translation || {}).map(([source, target]) => `
                  <div class="list-row">
                    <div class="row-head"><strong>${esc(source)}</strong><span class="mono">${esc(target)}</span></div>
                  </div>
                `).join('')}
              </div>
            </div>
            <div class="reading-slab">
              <div class="label">Flow rule</div>
              <div class="chip-row">${(paper.flow_rule || []).map(chip).join('') || chip('none')}</div>
              <div class="label">Design translation</div>
              <ul class="simple-list">${(paper.design_translation_rules || []).map((item) => `<li>${esc(item)}</li>`).join('') || '<li>none</li>'}</ul>
              <div class="label">Operator language</div>
              <div class="body-copy">${esc(paper.operator_language_rule || 'none')}</div>
            </div>
          </div>
        </section>
      `;
    }

    function renderPrimarySurface() {
      switch (runtime.active_surface) {
        case 'cases-queue':
          return `
            <section class="panel list-panel">
              <div class="surface-head">
                <div class="section-head">
                  <div>
                    <div class="kicker">Primary Surface</div>
                    <h2>Cases / Queue</h2>
                  </div>
                  <div class="mono">progression entry surface</div>
                </div>
                <div class="shell-note">Assigned work, current organ placement, and next-hop visibility come before deep detail.</div>
              </div>
              <div class="page-toolbar">
                <div class="page-tabs">
                  <span class="page-tab active">all active</span>
                  <span class="page-tab">observer-only</span>
                  <span class="page-tab">mixed hold</span>
                </div>
                <div class="mono">${queue.length} visible cases</div>
              </div>
              <div class="entity-list">
                ${queue.map((item) => `
                  <div class="entity-row">
                    <div class="entity-main">
                      <div class="row-head">
                        <span class="entity-title">${item.headline || item.case_id}</span>
                        <span class="mono">${item.case_id}</span>
                      </div>
                      <div class="entity-sub">${item.placement_reason_short || 'no placement reason'}</div>
                      <div class="entity-sub">update=${item.recent_update_reason || 'none'} / attention_pattern=${item.attention_pattern_summary || 'none'}</div>
                    </div>
                    <div class="entity-meta">
                      <div class="mono">organ=${item.current_organ_ref || 'unknown'}</div>
                      <div class="meta">lane=${item.lane_kind || 'unknown'} / updated=${item.updated_at || 'unknown'}</div>
                      <div class="chip-row">${(item.restriction_flags || []).map(chip).join("")}</div>
                      <div class="meta">next=${item.preferred_next_candidate || 'none'} / saved=${item.saved_connection_count ?? 0} / attention=${item.attention_flag ? 'yes' : 'no'}</div>
                    </div>
                    <div class="entity-actions">
                      ${item.detail_href ? `<a class="toolbar-link" href="${item.detail_href}">Current Organ Detail</a>` : ''}
                      ${item.next_detail_href ? `<a class="toolbar-link" href="${item.next_detail_href}">Next Candidate Detail</a>` : ''}
                    </div>
                  </div>
                `).join('')}
              </div>
            </section>
          `;
        case 'inputs-intake':
          return `
            <section class="panel inspector-panel">
              <div class="surface-head">
                <div class="section-head">
                  <div>
                    <div class="kicker">Primary Surface</div>
                    <h2>Inputs / Intake</h2>
                  </div>
                  <div class="mono">${intake.intake_classification || 'unknown classification'}</div>
                </div>
                <div class="shell-note">Source and context stay visible before any later lane meaning is assumed.</div>
              </div>
              <div class="summary-grid">
              <div class="card">
                <strong>${intake.source_id || 'no source id'}</strong>
                <div class="meta">kind=${intake.source_kind || 'unknown'} / family=${intake.source_family || 'unknown'}</div>
                <div class="chip-row">${(intake.matched_context_layers || []).map(chip).join('')}</div>
                <div class="label">Selected Artifact Refs</div>
                <ul class="simple-list">${(intake.selected_artifact_refs || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
              </div>
              <div class="card">
                <div class="label">Artifact Roots</div>
                <div class="chip-row">${(intake.artifact_roots || []).map(chip).join('') || chip('none')}</div>
                <div class="meta">first_read=${intake.first_read_ref || 'none'} / requested=${intake.requested_artifact_ref || 'none'}</div>
                <div class="meta">phase_source_turn=${intake.phase_source_turn || 'none'} / mode_source=${intake.mode_source || 'none'}</div>
                <div class="toolbar-links">
                  ${intake.detail_href ? `<a class="toolbar-link" href="${intake.detail_href}">Input Organ Detail</a>` : ''}
                  ${intake.current_reading_href ? `<a class="toolbar-link" href="${intake.current_reading_href}">Current Reading Center</a>` : ''}
                </div>
                <div class="warn">
                  <strong>Weak / Fallback Carry</strong>
                  <div>${intake.weakness_note || 'none'}</div>
                  <div class="meta">fallback=${String(!!intake.fallback_used)} / readiness=${intake.readiness_level || 'unknown'}</div>
                </div>
              </div>
              </div>
            </section>
          `;
        case 'history-trace':
          return `
            <section class="panel log-panel">
              <div class="surface-head">
                <div class="section-head">
                  <div>
                    <div class="kicker">Primary Surface</div>
                    <h2>History / Trace</h2>
                  </div>
                  <div class="mono">append-only carry surface</div>
                </div>
                <div class="shell-note">Trace rows read as operational carry, not as generic activity cards.</div>
              </div>
              ${renderBridgeAuditBlock()}
              ${paper.kind ? `
                <section class="panel inspector-panel">
                  <div class="section-head">
                    <div><div class="kicker">Trace Governance Contract</div><h3>Loop closure sections</h3></div>
                    <div class="mono">append-only / decision-readable</div>
                  </div>
                  <div class="chip-row">${(paper.trace_governance_sections || []).map(chip).join('') || chip('none')}</div>
                  <ul class="simple-list">${(paper.trace_governance_rules || []).map((item) => `<li>${esc(item)}</li>`).join('') || '<li>none</li>'}</ul>
                </section>
              ` : ''}
              <div class="mini-stat-row">
                <div class="mini-stat"><div class="kicker">trace rows</div><div class="metric-value" style="font-size:16px;">${(history.latest_trace_list || []).length}</div></div>
                <div class="mini-stat"><div class="kicker">decision anchor</div><div class="mono">${history.decision_trace_anchor || 'none'}</div></div>
                <div class="mini-stat"><div class="kicker">residue cues</div><div class="mono">${(history.reentry_cues || []).length}</div></div>
              </div>
              <div class="activity-list">
                ${(history.latest_trace_list || []).map((item) => `
                  <div class="activity-row">
                    <div class="row-head">
                      <div class="label">${item.trace_kind || 'trace'}</div>
                      <span class="mono">${item.trace_id || 'unknown trace'}</span>
                    </div>
                    <strong>${item.detail_href ? `<a href="${item.detail_href}">${item.summary || 'none'}</a>` : (item.summary || 'none')}</strong>
                    <div class="meta">residue=${item.residue_note || 'none'}</div>
                    <div class="body-copy">${item.reentry_hint || 'none'}</div>
                  </div>
                `).join('')}
              </div>
            </section>
          `;
        case 'programs-connections':
          return `
            <section class="panel list-panel">
              <div class="surface-head">
                <div class="section-head">
                  <div>
                    <div class="kicker">Primary Surface</div>
                    <h2>Programs / Connections</h2>
                  </div>
                  <div class="mono">${programs.connection_state || 'unknown connection state'}</div>
                </div>
                <div class="shell-note">Boundary state, linked programs, attention memory, and update evidence stay inspectable from one surface.</div>
              </div>
              ${renderBridgeConnectionBlock()}
              ${paper.kind ? `
                <section class="panel inspector-panel">
                  <div class="section-head">
                    <div><div class="kicker">Cell / Worker Panel Contract</div><h3>CLI ownership setup</h3></div>
                    <div class="mono">payload -> return slot</div>
                  </div>
                  <div class="chip-row">${(paper.cell_worker_sections || []).map(chip).join('') || chip('none')}</div>
                  <ul class="simple-list">${(paper.cell_worker_rules || []).map((item) => `<li>${esc(item)}</li>`).join('') || '<li>none</li>'}</ul>
                </section>
              ` : ''}
              <div class="detail-grid">
              <div class="card">
                <div class="chip-row">
                  ${chip(`state=${programs.connection_state || 'unknown'}`)}
                  ${(programs.linked_programs || []).map(chip).join('')}
                </div>
                <div class="body-copy">${programs.action_request_preview || 'none'}</div>
                <div class="panel-divider">
                <div class="label">Saved Connections</div>
                <div class="list-shell" style="padding:0 12px;">
                  ${(programs.saved_connection_preview || []).map((item) => `
                    <div class="trace-item">
                      <div class="row-head">
                        <strong>${item.detail_href ? `<a href="${item.detail_href}">${item.value_label || item.id || 'saved connection'}</a>` : (item.value_label || item.id || 'saved connection')}</strong>
                        <span class="mono">${item.id || 'connection'}</span>
                      </div>
                      <div class="body-copy">${item.relation_summary || 'none'}</div>
                      <div class="meta">${item.source_pointer || 'no source pointer'}</div>
                    </div>
                  `).join('') || '<div class="meta">none</div>'}
                </div>
                </div>
                <div class="panel-divider">
                <div class="label">Attention / Update</div>
                <div class="list-shell" style="padding:0 12px;">
                  ${(programs.attention_memory_preview || []).map((item) => `
                    <div class="trace-item">
                      <div class="row-head">
                        <strong>${item.detail_href ? `<a href="${item.detail_href}">${item.attention_pattern_summary || 'attention pattern'}</a>` : (item.attention_pattern_summary || 'attention pattern')}</strong>
                        <span class="mono">${item.asset_id || 'attention'}</span>
                      </div>
                      <div class="meta">active=${item.active_attention_count || 0}</div>
                      <div class="body-copy">${(item.dominant_attention_reasons || []).join(' / ') || 'none'}</div>
                    </div>
                  `).join('')}
                  ${(programs.update_event_preview || []).map((item) => `
                    <div class="trace-item">
                      <strong>${item.update_reason || 'runtime update'}</strong>
                      <div class="meta">trigger=${item.trigger_type || 'unknown'} / updated=${item.updated_at || 'unknown'}</div>
                    </div>
                  `).join('') || '<div class="meta">none</div>'}
                </div>
                </div>
              </div>
              <div class="card">
                <div class="label">Restriction Carry</div>
                <div class="chip-row">${(programs.governance_restriction_summary || []).map(chip).join('') || chip('none')}</div>
                <div class="label">Linked Programs</div>
                <div class="simple-list">${(programs.linked_programs || []).map((item) => `<div>${item}</div>`).join('') || '<div>none</div>'}</div>
              </div>
              </div>
            </section>
          `;
        default:
          return renderPaperProperCurrentSurface() || `
            <section class="panel primary-panel">
              <div class="surface-head">
                <div class="section-head">
                  <div>
                    <div class="kicker">Primary Surface</div>
                    <h2>${body.headline || 'Current Reading'}</h2>
                  </div>
                  <div class="mono">${(body.supporting_unit_refs || [])[0] || 'no supporting unit'}</div>
                </div>
                <div class="shell-note">This is the semantic center. Responsibility, reading body, and progression stay in one continuous work surface.</div>
              </div>
              ${renderBridgePostureStrip()}
              <div class="main-reading">
                <div class="summary-grid">
                <div class="reading-slab dense-row">
                  <div class="label">Current Responsibility</div>
                  <strong>${responsibility.detail_href ? `<a href="${responsibility.detail_href}">${responsibility.current_organ_ref || 'unknown organ'}</a>` : (responsibility.current_organ_ref || 'unknown organ')}</strong>
                  <div class="meta">${responsibility.placement_reason || 'none'}</div>
                  <div class="chip-row">${(responsibility.restriction_flags || []).map(chip).join('')}</div>
                </div>
                <div class="reading-slab">
                  <div class="label">Reading Status</div>
                  <div class="mini-stat-row">
                    <div class="mini-stat"><div class="kicker">lane</div><div class="mono">${lane.lane_kind || 'unknown'}</div></div>
                    <div class="mini-stat"><div class="kicker">status</div><div class="mono">${lane.lane_status || 'unknown'}</div></div>
                    <div class="mini-stat"><div class="kicker">next</div><div class="mono">${(progression.next_candidates || []).length}</div></div>
                  </div>
                </div>
                </div>
                <div class="reading-block">
                  <div class="label">Current Reading Body</div>
                  <div class="body-copy">${body.summary_body_text || 'none'}</div>
                </div>
                <div class="inspector-block">
                  <div class="section-head">
                    <div class="label">Lane + Progression</div>
                    <div class="mono">${lane.lane_status || 'unknown'}</div>
                  </div>
                  <div class="chip-row">
                    ${chip(`lane=${lane.lane_kind || 'unknown'}`)}
                    ${chip(`status=${lane.lane_status || 'unknown'}`)}
                  </div>
                  <div class="body-copy">${(progression.current_step || {}).summary || 'none'}</div>
                  <div class="toolbar-links">
                    ${(progression.next_candidates || []).map((item) => item.detail_href ? `<a class="toolbar-link" href="${item.detail_href}">${item.organ_ref || 'next candidate'}</a>` : '').join('')}
                  </div>
                </div>
              </div>
            </section>
          `;
      }
    }

    function renderDetail(detail, heading) {
      const organ = detail.organ_identity || {};
      const bundle = detail.instruction_bundle_preview || {};
      const handoff = detail.accepted_handoff_preview || {};
      const recent = detail.recent_return_preview || {};
      const semiLive = detail.semi_live_status || {};
      const detailHref = organ.organ_ref === 'organ:governance'
        ? contextualLinkMap['organ_detail:governance']
        : contextualLinkMap['organ_detail:flow_interpretation'];
      return `
        <section class="panel inspector-panel">
          <div class="kicker">${heading}</div>
          <h3>${detailHref ? `<a href="${detailHref}">${organ.organ_label || 'Organ Detail'}</a>` : (organ.organ_label || 'Organ Detail')}</h3>
          <div class="meta">organ=${organ.organ_ref || 'unknown'} / status=${organ.current_status || 'unknown'}</div>
          <div class="body-copy">${bundle.role_sentence || 'none'}</div>
          <div class="label">Accepted Inputs</div>
          <ul class="simple-list">${(handoff.accepted_input_kinds || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
          <div class="label">Semi-Live Status</div>
          <div class="meta">phase=${semiLive.phase || 'none'} / decision=${semiLive.decision || 'none'} / candidates=${semiLive.candidate_count ?? 0}</div>
          <div class="body-copy">${(semiLive.restriction_flags || []).join(' / ') || semiLive.decision_reason || 'no semi-live status'}</div>
          <div class="label">Recent Return</div>
          <div class="body-copy">${recent.summary_return || 'none'}</div>
        </section>
      `;
    }

    const navHtml = (data.navigation_items || []).map((item) => {
      const href = (runtime.surface_links || {})[item.key === 'cases' ? 'cases-queue' : item.key === 'inputs' ? 'inputs-intake' : item.key === 'history' ? 'history-trace' : item.key === 'programs' ? 'programs-connections' : 'current-reading'] || '#';
      return `<a class="nav-item ${item.active ? 'active' : ''}" href="${href}"><strong>${item.label}</strong><span class="meta">${item.active ? 'active primary surface' : 'switch primary surface'}</span></a>`;
    }).join('');

    const breadcrumb = (routeState.breadcrumb_chain || ['VectorFL Page']).map((item, idx, arr) => `
      <span>${item}</span>${idx < arr.length - 1 ? '<span class="sep">/</span>' : ''}
    `).join('');

    app.innerHTML = `
      <div class="page">
        <section class="topbar">
          <div class="eyebrow">VectorFL Page / App Shell</div>
          <div class="section-head">
            <div style="display:grid;gap:4px;">
              <h1>Operational Reading Console</h1>
              <div class="breadcrumb">${breadcrumb}</div>
            </div>
            <div class="mono">contextual_panel=${routeState.active_contextual_panel || 'none'}</div>
          </div>
          <div class="metric-strip">
            ${metricStrip.map((item) => `
              <div class="metric-cell">
                <div class="kicker">${item.label}</div>
                <div class="metric-value">${item.value}</div>
                <div class="meta">${item.note}</div>
              </div>
            `).join('')}
          </div>
          <div class="toolbar-links">
            <a class="toolbar-link" href="${runtime.index_href || 'index.html'}">Mock Index</a>
            <a class="toolbar-link" href="${(runtime.surface_links || {})['current-reading'] || '#'}">Current Reading Center</a>
          </div>
        </section>
        <div class="frame">
          <aside class="panel nav-panel inspector-panel stack">
            <div class="kicker">Navigation</div>
            <div class="nav-stack">${navHtml}</div>
          </aside>
          <main class="main-column">
            ${renderPrimarySurface()}
            <section class="panel inspector-panel">
              <div class="section-head">
                <div class="kicker">Core Governance Carry</div>
                <div class="mono">${governance.hold_state || 'no hold state'}</div>
              </div>
              <div class="chip-row">${(governance.restriction_flags || []).map(chip).join('')}</div>
              <div class="body-copy">${governance.reason_summary || 'none'}</div>
              <div class="meta">release=${governance.release_condition || 'none'} / next_check=${governance.next_check_trigger || 'none'}</div>
            </section>
          </main>
          <aside class="right-column">
            ${renderDetail(detailPanels.current || {}, 'Contextual Panel / Current Organ')}
            ${renderDetail(detailPanels.governance_candidate || {}, 'Contextual Panel / Preferred Next Candidate')}
          </aside>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_app_shell_set(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell")
    root.mkdir(parents=True, exist_ok=True)

    routes: List[Dict[str, str]] = []
    for surface in PRIMARY_SURFACES:
      data = build_vectorfl_page_app_shell_state(repo_root, active_surface=surface)
      html = render_vectorfl_page_app_shell_html(data)
      html_path = root / f"{surface}.html"
      json_path = root / f"{surface}.json"
      html_path.write_text(html, encoding="utf-8")
      json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
      routes.append(
          {
              "surface": surface,
              "html_path": str(html_path),
              "json_path": str(json_path),
          }
      )

    index_path = root / "index.html"
    index_html = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>VectorFL Page Shell</title>
<style>:root{--bg:#f3f5f7;--panel:#fcfcfd;--line:#d7dde4;--ink:#111827;--muted:#667085}*{box-sizing:border-box}body{font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);margin:0;color:var(--ink)}.page{max-width:1080px;margin:0 auto;padding:16px;display:grid;gap:12px}.panel{background:var(--panel);border:1px solid var(--line);padding:14px;display:grid;gap:12px}.card{background:#fcfcfd;border-bottom:1px solid var(--line);padding:12px 14px;display:grid;gap:6px}.card:last-child{border-bottom:0}.grid{display:grid;gap:0;border:1px solid var(--line);background:#fcfcfd}a{color:inherit;text-decoration:none}.meta{color:var(--muted);font-size:13px;line-height:1.5}.kicker{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--muted)}.section-head{display:flex;align-items:end;justify-content:space-between;gap:12px}h1,h2{margin:0;color:var(--ink)}h1{font-size:18px;font-weight:700}h2{font-size:14px;font-weight:600}</style>
</head><body><div class="page"><section class="panel"><div class="kicker">VectorFL Page Shell</div><h1>Route-Aware App Shell Set</h1><div class="meta">Current Reading stays canonical center; other surfaces remain entry/material/carry/boundary states.</div></section><section class="panel grid">""" + "".join(
        f"""<div class="card"><div class="section-head"><h2>{SURFACE_LABELS[surface]}</h2><div class="mono">{surface}</div></div><div><a href="{surface}.html">HTML View</a></div><div><a href="{surface}.json">JSON Payload</a></div></div>"""
        for surface in PRIMARY_SURFACES
    ) + """</section></div></body></html>"""
    index_path.write_text(index_html, encoding="utf-8")

    return {
        "output_dir": str(root),
        "index_path": str(index_path),
        "routes": routes,
    }
