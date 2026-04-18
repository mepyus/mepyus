from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any, Dict
import json

from app.runtime.vectorfl_page_mock import load_vectorfl_current_reading_mock_fixture


def build_vectorfl_page_first_mock_data(repo_root: Path) -> Dict[str, Any]:
    fixture = load_vectorfl_current_reading_mock_fixture(repo_root)
    case_record = fixture.get("case_record") or {}
    lane_state = fixture.get("lane_state_record") or {}
    governance = fixture.get("governance_record") or {}
    surface = fixture.get("surface_packet") or {}
    traces = fixture.get("trace_preview_records") or []
    intake_caution = fixture.get("optional_intake_caution") or {}

    queue_item = {
        "case_id": case_record.get("case_id"),
        "case_kind": case_record.get("case_kind"),
        "case_status": case_record.get("case_status"),
        "current_organ_ref": "organ:flow_interpretation",
        "lane_kind": lane_state.get("lane_kind"),
        "lane_status": lane_state.get("lane_status"),
        "placement_reason_short": "flow interpretation is preserving unresolved edge before direct readout",
        "hold_state": governance.get("hold_state"),
        "restriction_flags": governance.get("restriction_flags") or [],
        "preferred_next_candidate": "organ:governance / lane_transition_preflight_reread",
        "held_candidate_exists": True,
        "headline": surface.get("headline"),
        "linked_program_refs": case_record.get("linked_program_refs") or [],
        "updated_at": case_record.get("updated_at"),
    }

    current_responsibility = {
        "current_organ_ref": "organ:flow_interpretation",
        "current_lane_ref": case_record.get("current_lane_ref"),
        "placement_reason": "Translation narrowed this case into transition-thickening grammar, and flow interpretation is currently responsible for preserving unresolved edge and next-hop readability.",
        "restriction_flags": governance.get("restriction_flags") or [],
        "next_hop_candidates": lane_state.get("next_hop_candidates") or [],
        "detail_entry_target": "organ_detail:flow_interpretation",
    }

    progression_preview = {
        "previous_step": {
            "organ_ref": "organ:translation",
            "summary": "Translated mixed intake into transition-thickening and explanation-first grammar."
        },
        "current_step": {
            "organ_ref": "organ:flow_interpretation",
            "summary": "Reading next hop and preserving unresolved edge before direct operator presentation."
        },
        "next_candidates": [
            {
                "organ_ref": "organ:governance",
                "lane_ref": "lane_transition_preflight_reread",
                "status": "preferred_candidate",
                "detail_entry_target": "organ_detail:governance"
            },
            {
                "organ_ref": "organ:current_reading_return",
                "lane_ref": "lane_operator_readout_review",
                "status": "held_candidate",
                "detail_entry_target": "organ_detail:current_reading_return"
            },
        ],
    }

    intake_preview = {
        "source_id": "source_external_transition_case_001",
        "source_kind": "mixed_runtime_material",
        "source_family": "external_case",
        "source_subgroup": "transition_case",
        "matched_context_layers": [
            "global:external_reference",
            "family:transition_thickening",
            "case:mixed_hold_transition"
        ],
        "intake_classification": "mixed_material",
        "next_lane_hint": "translation_first",
        "weakness_note": intake_caution.get("weakness_note"),
        "fallback_used": intake_caution.get("fallback_used"),
        "readiness_level": intake_caution.get("readiness_level"),
        "re_read_needed": intake_caution.get("re_read_needed"),
    }

    history_trace_preview = {
        "latest_trace_list": traces[:3],
        "decision_trace_anchor": governance.get("decision_trace_ref"),
        "residue_emphasis": [
            item.get("residue_note")
            for item in traces
            if item.get("residue_note")
        ],
        "reentry_cues": [
            item.get("reentry_hint")
            for item in traces
            if item.get("reentry_hint")
        ],
    }

    programs_connections_preview = {
        "linked_programs": case_record.get("linked_program_refs") or [],
        "connection_state": "read_connected_request_limited",
        "current_linked_surface": case_record.get("linked_program_refs") or [],
        "action_request_preview": "Hold direct presentation. Keep request at explanation-first or reread-first level until closure condition is satisfied.",
        "governance_restriction_summary": governance.get("restriction_flags") or [],
    }

    return {
        "state": "loaded",
        "page_title": "VectorFL Page / First Mock",
        "left_rail": {
            "enabled": False,
            "mode": "rail_minimal",
            "note": "Left rail remains optional at this stage; sidebar and center console stay primary."
        },
        "navigation_items": [
            {"key": "current-reading", "label": "Current Reading", "active": True},
            {"key": "inputs", "label": "Inputs / Intake", "active": False},
            {"key": "cases", "label": "Cases / Queue", "active": False},
            {"key": "history", "label": "History / Trace", "active": False},
            {"key": "programs", "label": "Programs / Connections", "active": False},
        ],
        "navigation_structure": {
            "primary": [
                "Current Reading",
                "Cases / Queue",
                "Inputs / Intake",
                "History / Trace",
                "Programs / Connections",
            ],
            "secondary": [
                "Organ Detail (contextual drill-in only)",
            ],
        },
        "scenario": fixture.get("scenario") or {},
        "current_responsibility": current_responsibility,
        "progression_preview": progression_preview,
        "queue_preview": [queue_item],
        "drill_in_navigation": {
            "queue_to_current_reading": {
                "entry_target": "current_reading:case_transition_surface_reentry_001",
                "carried_refs": [
                    case_record.get("case_id"),
                    case_record.get("current_lane_ref"),
                    case_record.get("current_surface_ref"),
                    case_record.get("governance_state_ref"),
                ],
            },
            "current_reading_to_organ_detail": {
                "entry_target": "organ_detail:flow_interpretation",
                "carried_refs": [
                    case_record.get("case_id"),
                    case_record.get("current_lane_ref"),
                    "organ:flow_interpretation",
                ],
            },
        },
        "current_reading": {
            "case_header": {
                "case_id": case_record.get("case_id"),
                "case_kind": case_record.get("case_kind"),
                "case_status": case_record.get("case_status"),
                "linked_program_refs": case_record.get("linked_program_refs") or [],
                "updated_at": case_record.get("updated_at"),
            },
            "body": {
                "headline": surface.get("headline"),
                "summary_body_text": surface.get("summary_body_text"),
                "supporting_unit_refs": surface.get("supporting_unit_refs") or [],
            },
            "lane": {
                "lane_kind": lane_state.get("lane_kind"),
                "lane_status": lane_state.get("lane_status"),
                "next_hop_candidates": lane_state.get("next_hop_candidates") or [],
            },
            "governance": {
                "hold_state": governance.get("hold_state"),
                "restriction_flags": governance.get("restriction_flags") or [],
                "reason_summary": governance.get("reason_summary"),
                "release_condition": governance.get("release_condition"),
                "next_check_trigger": governance.get("next_check_trigger"),
            },
            "trace_preview": traces[:2],
        },
        "inputs_preview": intake_preview,
        "history_trace_preview": history_trace_preview,
        "programs_connections_preview": programs_connections_preview,
    }


def render_vectorfl_page_first_mock_html(data: Dict[str, Any]) -> str:
    payload_block = (
        f'<script id="vectorfl-page-first-mock-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / First Mock</title>
  <style>
    :root {
      --bg: #f4efe7;
      --panel: #fffaf2;
      --line: #d7cab7;
      --line-strong: #7a5631;
      --text: #1f2937;
      --muted: #6b7280;
      --ink: #5b422a;
      --chip: #efe5d3;
      --warn: #8a5a2b;
      --warn-bg: #f7ecd7;
      --shadow: 0 12px 30px rgba(91, 66, 42, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: radial-gradient(circle at top, #fbf6ee 0%, var(--bg) 55%, #efe7d8 100%); color: var(--text); font-family: Georgia, serif; }
    .page { max-width: 1540px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .frame { display: grid; grid-template-columns: 280px minmax(0, 1fr) 320px; gap: 16px; align-items: start; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 20px; padding: 16px; box-shadow: var(--shadow); }
    .nav-stack, .stack { display: grid; gap: 12px; }
    .nav-item { display: block; padding: 10px 12px; border-radius: 14px; border: 1px solid #eadfcf; background: #fff; color: var(--ink); text-decoration: none; }
    .nav-item.active { background: #efe2c2; border-color: var(--line-strong); font-weight: 600; }
    .kicker { color: var(--muted); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    h1, h2, h3 { margin: 0 0 10px 0; color: var(--ink); }
    .meta { color: var(--muted); font-size: 13px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { display: inline-flex; align-items: center; border-radius: 999px; padding: 6px 10px; font-size: 12px; background: var(--chip); color: var(--ink); }
    .row-card, .trace-item, .slot { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 12px; display: grid; gap: 6px; }
    .body-copy { line-height: 1.7; white-space: pre-wrap; }
    .simple-list { display: grid; gap: 6px; margin: 0; padding-left: 18px; }
    .label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
    .warn { border: 1px solid #e5c28c; background: var(--warn-bg); color: var(--warn); border-radius: 16px; padding: 12px; display: grid; gap: 6px; }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-first-mock-data').textContent);
    const app = document.getElementById('app');

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    const navHtml = (data.navigation_items || []).map((item) =>
      `<a href="#" class="nav-item ${item.active ? 'active' : ''}">${item.label}</a>`
    ).join("");

    const queueHtml = (data.queue_preview || []).map((item) => `
      <div class="row-card">
        <strong>${item.headline || item.case_id}</strong>
        <div class="meta">case=${item.case_id} / kind=${item.case_kind} / status=${item.case_status}</div>
        <div class="chip-row">
          ${chip(`organ=${item.current_organ_ref || 'unknown'}`)}
          ${chip(`lane=${item.lane_kind || 'unknown'}`)}
          ${chip(`state=${item.lane_status || 'unknown'}`)}
          ${chip(`hold=${item.hold_state || 'unknown'}`)}
          ${(item.restriction_flags || []).map(chip).join("")}
        </div>
        <div class="body-copy">${item.placement_reason_short || 'no placement reason'}</div>
        <div class="meta">next=${item.preferred_next_candidate || 'none'} / held_candidate=${String(!!item.held_candidate_exists)}</div>
        <div class="meta">programs=${(item.linked_program_refs || []).join(', ') || 'none'} / updated=${item.updated_at || 'unknown'}</div>
      </div>
    `).join("");

    const current = data.current_reading || {};
    const caseHeader = current.case_header || {};
    const body = current.body || {};
    const lane = current.lane || {};
    const gov = current.governance || {};
    const traces = current.trace_preview || [];
    const responsibility = data.current_responsibility || {};
    const progression = data.progression_preview || {};
    const intake = data.inputs_preview || {};
    const history = data.history_trace_preview || {};
    const programs = data.programs_connections_preview || {};
    const drillins = data.drill_in_navigation || {};
    const navStructure = data.navigation_structure || {};
    const leftRail = data.left_rail || {};
    const traceHtml = traces.map((item) => `
      <div class="trace-item">
        <div class="label">${item.trace_kind || 'trace'}</div>
        <strong>${item.summary || 'no summary'}</strong>
        <div class="meta">residue=${item.residue_note || 'none'}</div>
        <div class="body-copy">${item.reentry_hint || 'no reentry hint'}</div>
      </div>
    `).join("");

    const historyRows = (history.latest_trace_list || []).map((item) => `
      <div class="trace-item">
        <div class="label">${item.trace_kind || 'trace'}</div>
        <strong>${item.summary || 'no summary'}</strong>
        <div class="meta">residue=${item.residue_note || 'none'}</div>
        <div class="body-copy">${item.reentry_hint || 'no reentry hint'}</div>
      </div>
    `).join("");

    const nextCandidatesHtml = (progression.next_candidates || []).map((item) => `
      <div class="row-card">
        <strong>${item.organ_ref || 'unknown organ'}</strong>
        <div class="meta">lane=${item.lane_ref || 'none'} / status=${item.status || 'unknown'}</div>
      </div>
    `).join("");

    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page / First Mock</div>
          <h1>${data.page_title || 'VectorFL Page'}</h1>
          <div class="meta">scenario=${(data.scenario || {}).name || 'unknown'} / intent=${(data.scenario || {}).intent || 'n/a'}</div>
          <div class="meta">rail=${leftRail.mode || 'unknown'} / enabled=${String(!!leftRail.enabled)}</div>
        </section>

        <div class="frame">
          <aside class="stack">
            <section class="panel">
              <h3>Navigation</h3>
              <div class="nav-stack">${navHtml}</div>
              <div class="label" style="margin-top:10px;">Primary</div>
              <div class="chip-row">${(navStructure.primary || []).map(chip).join("")}</div>
              <div class="label" style="margin-top:10px;">Secondary</div>
              <div class="chip-row">${(navStructure.secondary || []).map(chip).join("")}</div>
            </section>
            <section class="panel">
              <h3>Cases / Queue</h3>
              <div class="meta">current-reading entry queue</div>
              <div class="stack">${queueHtml}</div>
            </section>
            <section class="panel">
              <h3>Inputs / Intake</h3>
              <div class="slot">
                <div class="label">Source</div>
                <strong>${intake.source_id || 'no source id'}</strong>
                <div class="meta">kind=${intake.source_kind || 'unknown'} / family=${intake.source_family || 'unknown'} / subgroup=${intake.source_subgroup || 'unknown'}</div>
              </div>
              <div class="slot">
                <div class="label">Context / Hint</div>
                <div class="chip-row">${(intake.matched_context_layers || []).map(chip).join("")}</div>
                <div class="meta">classification=${intake.intake_classification || 'unknown'} / next=${intake.next_lane_hint || 'none'}</div>
              </div>
              <div class="warn">
                <strong>Weakness / Fallback</strong>
                <div>${intake.weakness_note || 'no weakness note'}</div>
                <div class="meta">fallback_used=${String(!!intake.fallback_used)} / readiness=${intake.readiness_level || 'unknown'} / re_read_needed=${String(!!intake.re_read_needed)}</div>
              </div>
            </section>
          </aside>

          <main class="stack">
            <section class="panel">
              <div class="kicker">Current Responsibility</div>
              <h2>${responsibility.current_organ_ref || 'no current organ'}</h2>
              <div class="meta">lane=${responsibility.current_lane_ref || 'none'}</div>
              <div class="body-copy">${responsibility.placement_reason || 'no placement reason'}</div>
              <div class="chip-row" style="margin-top:10px;">
                ${(responsibility.restriction_flags || []).map(chip).join("")}
              </div>
              <div class="meta">detail=${responsibility.detail_entry_target || 'none'}</div>
            </section>

            <section class="panel">
              <div class="kicker">Current Reading</div>
              <h2>${body.headline || 'Current Reading'}</h2>
              <div class="meta">case=${caseHeader.case_id || 'none'} / kind=${caseHeader.case_kind || 'unknown'} / status=${caseHeader.case_status || 'unknown'}</div>
              <div class="body-copy">${body.summary_body_text || 'no summary body'}</div>
              <div class="label" style="margin-top:10px;">Supporting Units</div>
              <ul class="simple-list">
                ${(body.supporting_unit_refs || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </section>

            <section class="panel">
              <h3>Lane Strip</h3>
              <div class="chip-row">
                ${chip(`lane=${lane.lane_kind || 'unknown'}`)}
                ${chip(`status=${lane.lane_status || 'unknown'}`)}
              </div>
              <div class="label" style="margin-top:10px;">Next Hop Candidates</div>
              <ul class="simple-list">
                ${(lane.next_hop_candidates || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </section>

            <section class="panel">
              <h3>Progression Strip</h3>
              <div class="slot">
                <div class="label">Previous</div>
                <strong>${(progression.previous_step || {}).organ_ref || 'none'}</strong>
                <div class="body-copy">${(progression.previous_step || {}).summary || 'none'}</div>
              </div>
              <div class="slot">
                <div class="label">Current</div>
                <strong>${(progression.current_step || {}).organ_ref || 'none'}</strong>
                <div class="body-copy">${(progression.current_step || {}).summary || 'none'}</div>
              </div>
              <div class="label" style="margin-top:10px;">Next Candidates</div>
              <div class="stack">${nextCandidatesHtml || '<div class="meta">no next candidates</div>'}</div>
              <div class="meta">drill-in=${(drillins.current_reading_to_organ_detail || {}).entry_target || 'none'}</div>
            </section>
          </main>

          <aside class="stack">
            <section class="panel">
              <h3>Governance</h3>
              <div class="chip-row">
                ${chip(`hold=${gov.hold_state || 'unknown'}`)}
                ${(gov.restriction_flags || []).map(chip).join("")}
              </div>
              <div class="label" style="margin-top:10px;">Reason</div>
              <div class="body-copy">${gov.reason_summary || 'none'}</div>
              <div class="label" style="margin-top:10px;">Release Condition</div>
              <div class="body-copy">${gov.release_condition || 'none'}</div>
              <div class="label" style="margin-top:10px;">Next Check Trigger</div>
              <div class="body-copy">${gov.next_check_trigger || 'none'}</div>
            </section>
            <section class="panel">
              <h3>History / Trace</h3>
              <div class="stack">${historyRows || '<div class="meta">no trace preview</div>'}</div>
              <div class="label" style="margin-top:10px;">Decision Anchor</div>
              <div class="body-copy">${history.decision_trace_anchor || 'none'}</div>
              <div class="label" style="margin-top:10px;">Reentry Cues</div>
              <ul class="simple-list">
                ${(history.reentry_cues || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </section>
            <section class="panel">
              <h3>Programs / Connections</h3>
              <div class="chip-row">
                ${chip(`state=${programs.connection_state || 'unknown'}`)}
                ${(programs.governance_restriction_summary || []).map(chip).join("")}
              </div>
              <div class="label" style="margin-top:10px;">Linked Programs</div>
              <div class="chip-row">${(programs.linked_programs || []).map(chip).join("") || '<span class="meta">none</span>'}</div>
              <div class="label" style="margin-top:10px;">Action Request Preview</div>
              <div class="body-copy">${programs.action_request_preview || 'none'}</div>
            </section>
          </aside>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_first_mock(
    repo_root: Path,
    *,
    output_dir: Path | None = None,
) -> Dict[str, str]:
    data = build_vectorfl_page_first_mock_data(repo_root)
    html = render_vectorfl_page_first_mock_html(data)

    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "first_shell_mock.html"
    json_path = root / "first_shell_mock.json"

    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "html_path": str(html_path),
        "json_path": str(json_path),
    }
