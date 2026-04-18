from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Any, Dict
import json


def load_vectorfl_current_reading_mock_fixture(repo_root: Path) -> Dict[str, Any]:
    fixture_path = repo_root / "runtime" / "manifests" / "vectorfl_current_reading_mock_fixture_v0.json"
    return json.loads(fixture_path.read_text(encoding="utf-8"))


def build_vectorfl_current_reading_mock_shell_data(repo_root: Path) -> Dict[str, Any]:
    fixture = load_vectorfl_current_reading_mock_fixture(repo_root)
    case_record = fixture.get("case_record") or {}
    lane_state = fixture.get("lane_state_record") or {}
    governance = fixture.get("governance_record") or {}
    surface = fixture.get("surface_packet") or {}
    traces = fixture.get("trace_preview_records") or []
    intake_caution = fixture.get("optional_intake_caution") or {}

    return {
        "state": "loaded",
        "page_title": "VectorFL Page / Current Reading Mock",
        "fixture_id": fixture.get("fixture_id"),
        "scenario": fixture.get("scenario") or {},
        "case_header": {
            "case_id": case_record.get("case_id"),
            "case_kind": case_record.get("case_kind"),
            "case_status": case_record.get("case_status"),
            "linked_program_refs": case_record.get("linked_program_refs") or [],
            "updated_at": case_record.get("updated_at"),
        },
        "current_reading_body": {
            "surface_id": surface.get("surface_id"),
            "surface_kind": surface.get("surface_kind"),
            "headline": surface.get("headline"),
            "summary_body_text": surface.get("summary_body_text"),
            "supporting_unit_refs": surface.get("supporting_unit_refs") or [],
        },
        "lane_strip": {
            "current_lane_ref": case_record.get("current_lane_ref"),
            "lane_kind": lane_state.get("lane_kind"),
            "lane_status": lane_state.get("lane_status"),
            "current_output_refs": lane_state.get("current_output_refs") or [],
            "next_hop_candidates": lane_state.get("next_hop_candidates") or [],
        },
        "governance_card": {
            "governance_id": governance.get("governance_id"),
            "restriction_flags": governance.get("restriction_flags") or [],
            "hold_state": governance.get("hold_state"),
            "reason_summary": governance.get("reason_summary"),
            "release_condition": governance.get("release_condition"),
            "next_check_trigger": governance.get("next_check_trigger"),
        },
        "trace_strip": {
            "items": traces,
        },
        "caution_note": {
            "weakness_note": intake_caution.get("weakness_note"),
            "fallback_used": intake_caution.get("fallback_used"),
            "readiness_level": intake_caution.get("readiness_level"),
            "re_read_needed": intake_caution.get("re_read_needed"),
        },
        "raw_fixture": fixture,
    }


def render_vectorfl_current_reading_mock_shell_html(data: Dict[str, Any]) -> str:
    payload_block = (
        f'<script id="vectorfl-page-mock-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Current Reading Mock</title>
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
    .page { max-width: 1500px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .top { display: grid; gap: 8px; background: var(--panel); border: 1px solid var(--line); border-radius: 20px; padding: 16px; box-shadow: var(--shadow); }
    .kicker { color: var(--muted); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    .top h1 { margin: 0; font-size: 28px; color: var(--ink); }
    .meta { color: var(--muted); font-size: 13px; }
    .layout { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 16px; align-items: start; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 20px; padding: 16px; box-shadow: var(--shadow); }
    .panel h2, .panel h3 { margin: 0 0 10px 0; color: var(--ink); }
    .header-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { display: inline-flex; align-items: center; gap: 6px; border-radius: 999px; padding: 6px 10px; font-size: 12px; background: var(--chip); color: var(--ink); }
    .body-copy { line-height: 1.7; white-space: pre-wrap; }
    .stack { display: grid; gap: 16px; }
    .strip { display: grid; gap: 10px; }
    .trace-item { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 12px; display: grid; gap: 6px; }
    .label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
    .warn { border: 1px solid #e5c28c; background: var(--warn-bg); color: var(--warn); border-radius: 16px; padding: 12px; display: grid; gap: 6px; }
    .support-list, .simple-list { display: grid; gap: 6px; padding-left: 18px; margin: 0; }
    .slot { border: 1px solid #eadfcf; background: #fff; border-radius: 16px; padding: 12px; display: grid; gap: 8px; }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-mock-data').textContent);
    const app = document.getElementById('app');

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    const caseHeader = data.case_header || {};
    const body = data.current_reading_body || {};
    const lane = data.lane_strip || {};
    const gov = data.governance_card || {};
    const traces = (data.trace_strip || {}).items || [];
    const caution = data.caution_note || {};
    const scenario = data.scenario || {};

    const traceHtml = traces.length
      ? traces.map((item) => `
          <div class="trace-item">
            <div class="label">${item.trace_kind || 'trace'}</div>
            <strong>${item.summary || 'no summary'}</strong>
            <div class="meta">residue=${item.residue_note || 'none'}</div>
            <div class="body-copy">${item.reentry_hint || 'no reentry hint'}</div>
            <div class="meta">${item.created_at || ''}</div>
          </div>
        `).join("")
      : `<div class="meta">no trace preview</div>`;

    const cautionVisible = caution.weakness_note || caution.fallback_used || caution.re_read_needed;

    app.innerHTML = `
      <div class="page">
        <section class="top">
          <div class="kicker">VectorFL Page / Current Reading Mock</div>
          <h1>${body.headline || 'Current Reading'}</h1>
          <div class="meta">fixture=${data.fixture_id || 'unknown'} / scenario=${scenario.name || 'unknown'} / state=${data.state || 'unknown'}</div>
          <div class="header-grid">
            <div class="slot">
              <div class="label">Case</div>
              <strong>${caseHeader.case_id || 'no case id'}</strong>
              <div class="meta">kind=${caseHeader.case_kind || 'unknown'} / status=${caseHeader.case_status || 'unknown'}</div>
            </div>
            <div class="slot">
              <div class="label">Linked Programs</div>
              <div class="chip-row">${(caseHeader.linked_program_refs || []).map(chip).join("") || '<span class="meta">none</span>'}</div>
              <div class="meta">updated=${caseHeader.updated_at || 'unknown'}</div>
            </div>
          </div>
        </section>

        <div class="layout">
          <div class="stack">
            <section class="panel">
              <h2>Current Reading</h2>
              <div class="meta">surface=${body.surface_kind || 'unknown'} / id=${body.surface_id || 'none'}</div>
              <div class="body-copy">${body.summary_body_text || 'no current-reading summary'}</div>
              <div class="label" style="margin-top:10px;">Supporting Units</div>
              <ul class="support-list">
                ${(body.supporting_unit_refs || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </section>

            <section class="panel">
              <h3>Lane Strip</h3>
              <div class="chip-row">
                ${chip(`lane=${lane.lane_kind || 'unknown'}`)}
                ${chip(`status=${lane.lane_status || 'unknown'}`)}
                ${chip(`ref=${lane.current_lane_ref || 'none'}`)}
              </div>
              <div class="label" style="margin-top:10px;">Current Outputs</div>
              <ul class="simple-list">
                ${(lane.current_output_refs || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
              <div class="label" style="margin-top:10px;">Next Hop Candidates</div>
              <ul class="simple-list">
                ${(lane.next_hop_candidates || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </section>

            <section class="panel">
              <h3>Trace Strip</h3>
              ${traceHtml}
            </section>
          </div>

          <div class="stack">
            <section class="panel">
              <h3>Governance</h3>
              <div class="chip-row">
                ${chip(`hold=${gov.hold_state || 'unknown'}`)}
                ${(gov.restriction_flags || []).map(chip).join("")}
              </div>
              <div class="label" style="margin-top:10px;">Reason</div>
              <div class="body-copy">${gov.reason_summary || 'no reason summary'}</div>
              <div class="label" style="margin-top:10px;">Release Condition</div>
              <div class="body-copy">${gov.release_condition || 'none'}</div>
              <div class="label" style="margin-top:10px;">Next Check Trigger</div>
              <div class="body-copy">${gov.next_check_trigger || 'none'}</div>
            </section>

            ${cautionVisible ? `
              <section class="warn">
                <strong>Caution</strong>
                <div>${caution.weakness_note || 'no weakness note'}</div>
                <div class="meta">fallback_used=${String(!!caution.fallback_used)} / readiness=${caution.readiness_level || 'unknown'} / re_read_needed=${String(!!caution.re_read_needed)}</div>
              </section>
            ` : ''}
          </div>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_current_reading_mock_shell(
    repo_root: Path,
    *,
    output_dir: Path | None = None,
) -> Dict[str, str]:
    data = build_vectorfl_current_reading_mock_shell_data(repo_root)
    html = render_vectorfl_current_reading_mock_shell_html(data)

    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "current_reading_mock.html"
    json_path = root / "current_reading_mock.json"

    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "html_path": str(html_path),
        "json_path": str(json_path),
    }
