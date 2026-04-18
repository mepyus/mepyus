from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any, Dict
import json

from app.runtime.vectorfl_page_first_mock import build_vectorfl_page_first_mock_data


def _load_organ_fixture(repo_root: Path, organ_slug: str) -> Dict[str, Any]:
    fixture_path = repo_root / "runtime" / "manifests" / f"vectorfl_{organ_slug}_organ_detail_mock_fixture_v0.json"
    return json.loads(fixture_path.read_text(encoding="utf-8"))


def build_vectorfl_page_unified_mock_data(repo_root: Path) -> Dict[str, Any]:
    shell = build_vectorfl_page_first_mock_data(repo_root)
    current_detail = _load_organ_fixture(repo_root, "flow_interpretation")
    governance_detail = _load_organ_fixture(repo_root, "governance")

    shell["page_title"] = "VectorFL Page / Unified Shell Mock"
    shell["contextual_panels"] = {
        "active_panel": "organ_detail_current",
        "available_panels": [
            {
                "panel_id": "organ_detail_current",
                "entry_target": "organ_detail:flow_interpretation",
                "entry_label": "Current Organ Detail",
                "source": "current responsibility strip",
            },
            {
                "panel_id": "organ_detail_governance",
                "entry_target": "organ_detail:governance",
                "entry_label": "Preferred Next Candidate Detail",
                "source": "progression strip",
            },
        ],
    }
    shell["unified_shell"] = {
        "mode": "current_reading_centered_with_contextual_detail",
        "current_center": "Current Reading",
        "support_columns": [
            "Cases / Queue + Inputs / Intake",
            "Governance + History / Trace + Programs / Connections",
        ],
    }
    shell["sidebar_sections"] = [
        {
            "section_label": "Read",
            "items": [
                "Current Reading",
                "Cases / Queue",
                "Inputs / Intake",
            ],
        },
        {
            "section_label": "Carry",
            "items": [
                "History / Trace",
                "Programs / Connections",
            ],
        },
    ]
    shell["route_state_preview"] = {
        "active_primary_surface": "current-reading",
        "active_case_ref": shell.get("current_reading", {}).get("case_header", {}).get("case_id"),
        "active_contextual_panel": "organ_detail_current",
        "contextual_entry_targets": [
            "organ_detail:flow_interpretation",
            "organ_detail:governance",
        ],
        "note": "Current Reading remains the center route; organ detail stays contextual rather than becoming a primary route.",
    }
    shell["organ_detail_panels"] = {
        "current": current_detail,
        "governance_candidate": governance_detail,
    }
    return shell


def render_vectorfl_page_unified_mock_html(data: Dict[str, Any]) -> str:
    payload_block = (
        f'<script id="vectorfl-page-unified-mock-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Unified Shell Mock</title>
  <style>
    :root {
      --bg: #f4efe7;
      --panel: #fffaf2;
      --panel-soft: #f7f1e6;
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
    .page { max-width: 1820px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .header, .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 20px; box-shadow: var(--shadow); }
    .header { padding: 16px 18px; }
    .shell { display: grid; grid-template-columns: 220px 300px minmax(0, 1fr) 320px 360px; gap: 16px; align-items: start; }
    .panel { padding: 16px; display: grid; gap: 12px; }
    .panel.soft { background: var(--panel-soft); }
    .stack { display: grid; gap: 12px; }
    .kicker, .label { color: var(--muted); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    h1, h2, h3 { margin: 0; color: var(--ink); }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .nav-stack { display: grid; gap: 8px; }
    .nav-item, .subnav-item { display: grid; gap: 4px; text-decoration: none; color: var(--ink); border: 1px solid #eadfcf; border-radius: 14px; background: #fff; padding: 10px 12px; }
    .nav-item.active { background: #efe2c2; border-color: var(--line-strong); }
    .subnav-item { background: #fcf8f1; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { display: inline-flex; align-items: center; border-radius: 999px; padding: 6px 10px; font-size: 12px; background: var(--chip); color: var(--ink); }
    .card, .trace-item { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 12px; display: grid; gap: 6px; }
    .body-copy { line-height: 1.7; white-space: pre-wrap; }
    .simple-list { display: grid; gap: 6px; margin: 0; padding-left: 18px; }
    .warn { border: 1px solid #e5c28c; background: var(--warn-bg); color: var(--warn); border-radius: 16px; padding: 12px; display: grid; gap: 6px; }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-unified-mock-data').textContent);
    const app = document.getElementById('app');
    const current = data.current_reading || {};
    const body = current.body || {};
    const lane = current.lane || {};
    const gov = current.governance || {};
    const responsibility = data.current_responsibility || {};
    const progression = data.progression_preview || {};
    const intake = data.inputs_preview || {};
    const queue = data.queue_preview || [];
    const history = data.history_trace_preview || {};
    const programs = data.programs_connections_preview || {};
    const nav = data.navigation_items || [];
    const sidebarSections = data.sidebar_sections || [];
    const routeState = data.route_state_preview || {};
    const contextual = data.contextual_panels || {};
    const detailPanels = data.organ_detail_panels || {};
    const currentDetail = detailPanels.current || {};
    const governanceDetail = detailPanels.governance_candidate || {};

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    function navItem(item) {
      return `<a href="#" class="nav-item ${item.active ? 'active' : ''}"><strong>${item.label}</strong><span class="meta">${item.active ? 'current center or direct support surface' : 'available support surface'}</span></a>`;
    }

    function detailPanelHtml(detail, heading) {
      const organ = detail.organ_identity || {};
      const bundle = detail.instruction_bundle_preview || {};
      const handoff = detail.accepted_handoff_preview || {};
      const caution = detail.caution_profile || {};
      const recent = detail.recent_return_preview || {};
      return `
        <section class="panel soft">
          <div class="kicker">${heading}</div>
          <h3>${organ.organ_label || 'Organ Detail'}</h3>
          <div class="meta">organ=${organ.organ_ref || 'unknown'} / status=${organ.current_status || 'unknown'}</div>
          <div class="chip-row">${(organ.related_lane_refs || []).map(chip).join("")}</div>
          <div class="card">
            <div class="label">Role Sentence</div>
            <div class="body-copy">${bundle.role_sentence || 'none'}</div>
          </div>
          <div class="card">
            <div class="label">Accepted Inputs</div>
            <ul class="simple-list">${(handoff.accepted_input_kinds || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}</ul>
          </div>
          <div class="card">
            <div class="label">Stop / Hold Conditions</div>
            <ul class="simple-list">${(caution.stop_hold_conditions || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}</ul>
          </div>
          <div class="card">
            <div class="label">Recent Return</div>
            <div class="body-copy">${recent.summary_return || 'none'}</div>
            <div class="chip-row">${(recent.lane_hint_update || []).map(chip).join("")}</div>
          </div>
        </section>
      `;
    }

    const queueHtml = queue.map((item) => `
      <div class="card">
        <strong>${item.headline || item.case_id}</strong>
        <div class="meta">case=${item.case_id} / lane=${item.lane_kind || 'unknown'} / organ=${item.current_organ_ref || 'unknown'}</div>
        <div class="chip-row">
          ${chip(`hold=${item.hold_state || 'unknown'}`)}
          ${(item.restriction_flags || []).map(chip).join("")}
        </div>
        <div class="body-copy">${item.placement_reason_short || 'no placement reason'}</div>
        <div class="meta">next=${item.preferred_next_candidate || 'none'} / held=${String(!!item.held_candidate_exists)}</div>
      </div>
    `).join("");

    const historyHtml = (history.latest_trace_list || []).map((item) => `
      <div class="trace-item">
        <div class="label">${item.trace_kind || 'trace'}</div>
        <strong>${item.summary || 'no summary'}</strong>
        <div class="meta">residue=${item.residue_note || 'none'}</div>
        <div class="body-copy">${item.reentry_hint || 'no reentry hint'}</div>
      </div>
    `).join("");

    const nextHtml = (progression.next_candidates || []).map((item) => `
      <div class="card">
        <strong>${item.organ_ref || 'unknown organ'}</strong>
        <div class="meta">lane=${item.lane_ref || 'none'} / status=${item.status || 'unknown'}</div>
        <div class="meta">detail=${item.detail_entry_target || 'none'}</div>
      </div>
    `).join("");

    app.innerHTML = `
      <div class="page">
        <section class="header">
          <div class="kicker">VectorFL Page / Unified Shell Mock</div>
          <h1>${data.page_title || 'VectorFL Page'}</h1>
          <div class="meta">mode=${(data.unified_shell || {}).mode || 'unknown'} / current center=${(data.unified_shell || {}).current_center || 'unknown'}</div>
        </section>

        <div class="shell">
          <aside class="panel">
            <div class="kicker">Primary Navigation</div>
            <div class="nav-stack">${nav.map(navItem).join("")}</div>
            <div class="kicker" style="margin-top:6px;">Sidebar Sections</div>
            <div class="stack">${sidebarSections.map((section) => `
              <div class="card">
                <div class="label">${section.section_label || 'Section'}</div>
                <div class="chip-row">${(section.items || []).map(chip).join("")}</div>
              </div>
            `).join("")}</div>
            <div class="kicker" style="margin-top:6px;">Contextual Panels</div>
            <div class="nav-stack">${(contextual.available_panels || []).map((panel) => `<div class="subnav-item"><strong>${panel.entry_label}</strong><span class="meta">${panel.source}</span><span class="meta">${panel.entry_target}</span></div>`).join("")}</div>
            <div class="kicker" style="margin-top:6px;">Route State</div>
            <div class="card">
              <div class="meta">primary=${routeState.active_primary_surface || 'unknown'}</div>
              <div class="meta">case=${routeState.active_case_ref || 'none'}</div>
              <div class="meta">panel=${routeState.active_contextual_panel || 'none'}</div>
              <div class="body-copy">${routeState.note || 'no note'}</div>
            </div>
          </aside>

          <aside class="stack">
            <section class="panel">
              <div class="kicker">Cases / Queue</div>
              <div class="meta">progression entry before current-reading drill-in</div>
              <div class="stack">${queueHtml}</div>
            </section>
            <section class="panel">
              <div class="kicker">Inputs / Intake</div>
              <strong>${intake.source_id || 'no source id'}</strong>
              <div class="meta">kind=${intake.source_kind || 'unknown'} / family=${intake.source_family || 'unknown'} / next=${intake.next_lane_hint || 'none'}</div>
              <div class="chip-row">${(intake.matched_context_layers || []).map(chip).join("")}</div>
              <div class="warn">
                <strong>Weak / Fallback Carry</strong>
                <div>${intake.weakness_note || 'no weakness note'}</div>
                <div class="meta">fallback=${String(!!intake.fallback_used)} / readiness=${intake.readiness_level || 'unknown'} / reread=${String(!!intake.re_read_needed)}</div>
              </div>
            </section>
          </aside>

          <main class="stack">
            <section class="panel">
              <div class="kicker">Current Responsibility</div>
              <h2>${responsibility.current_organ_ref || 'no current organ'}</h2>
              <div class="meta">lane=${responsibility.current_lane_ref || 'none'} / detail=${responsibility.detail_entry_target || 'none'}</div>
              <div class="body-copy">${responsibility.placement_reason || 'no placement reason'}</div>
              <div class="chip-row">${(responsibility.restriction_flags || []).map(chip).join("")}</div>
            </section>

            <section class="panel">
              <div class="kicker">Current Reading</div>
              <h2>${body.headline || 'Current Reading'}</h2>
              <div class="body-copy">${body.summary_body_text || 'no summary body'}</div>
              <div class="label">Supporting Units</div>
              <ul class="simple-list">${(body.supporting_unit_refs || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}</ul>
            </section>

            <section class="panel">
              <div class="kicker">Lane + Progression</div>
              <div class="chip-row">
                ${chip(`lane=${lane.lane_kind || 'unknown'}`)}
                ${chip(`status=${lane.lane_status || 'unknown'}`)}
              </div>
              <div class="label" style="margin-top:10px;">Current Step</div>
              <div class="card">
                <strong>${(progression.current_step || {}).organ_ref || 'none'}</strong>
                <div class="body-copy">${(progression.current_step || {}).summary || 'none'}</div>
              </div>
              <div class="label">Next Candidates</div>
              <div class="stack">${nextHtml || '<div class="meta">no next candidates</div>'}</div>
            </section>
          </main>

          <aside class="stack">
            <section class="panel">
              <div class="kicker">Governance</div>
              <div class="chip-row">
                ${chip(`hold=${gov.hold_state || 'unknown'}`)}
                ${(gov.restriction_flags || []).map(chip).join("")}
              </div>
              <div class="body-copy">${gov.reason_summary || 'none'}</div>
              <div class="label">Release Condition</div>
              <div class="body-copy">${gov.release_condition || 'none'}</div>
            </section>
            <section class="panel">
              <div class="kicker">History / Trace</div>
              <div class="stack">${historyHtml || '<div class="meta">no trace preview</div>'}</div>
            </section>
            <section class="panel">
              <div class="kicker">Programs / Connections</div>
              <div class="chip-row">
                ${chip(`state=${programs.connection_state || 'unknown'}`)}
                ${(programs.linked_programs || []).map(chip).join("")}
              </div>
              <div class="body-copy">${programs.action_request_preview || 'none'}</div>
            </section>
          </aside>

          <aside class="stack">
            ${detailPanelHtml(currentDetail, 'Contextual Panel / Current Organ')}
            ${detailPanelHtml(governanceDetail, 'Contextual Panel / Preferred Next Candidate')}
          </aside>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_unified_mock(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_page_unified_mock_data(repo_root)
    html = render_vectorfl_page_unified_mock_html(data)

    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "unified_shell_mock.html"
    json_path = root / "unified_shell_mock.json"

    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
