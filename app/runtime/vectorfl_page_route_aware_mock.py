from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List
import json

from app.runtime.vectorfl_page_unified_mock import build_vectorfl_page_unified_mock_data


PRIMARY_SURFACES = [
    "current-reading",
    "cases-queue",
    "inputs-intake",
    "history-trace",
    "programs-connections",
]

NAV_KEY_BY_SURFACE = {
    "current-reading": "current-reading",
    "cases-queue": "cases",
    "inputs-intake": "inputs",
    "history-trace": "history",
    "programs-connections": "programs",
}


def _with_active_navigation(items: Iterable[Dict[str, Any]], active_key: str) -> List[Dict[str, Any]]:
    updated: List[Dict[str, Any]] = []
    for item in items:
        copied = dict(item)
        copied["active"] = copied.get("key") == active_key
        updated.append(copied)
    return updated


def build_vectorfl_page_route_aware_mock_data(repo_root: Path, *, active_surface: str) -> Dict[str, Any]:
    if active_surface not in PRIMARY_SURFACES:
        raise ValueError(f"Unsupported primary surface: {active_surface}")

    data = build_vectorfl_page_unified_mock_data(repo_root)
    data["page_title"] = f"VectorFL Page / Route Mock / {active_surface}"
    active_nav_key = NAV_KEY_BY_SURFACE[active_surface]
    data["navigation_items"] = _with_active_navigation(data.get("navigation_items") or [], active_nav_key)
    route_state = data.get("route_state_preview") or {}
    route_state["active_primary_surface"] = active_surface
    route_state["active_nav_key"] = active_nav_key
    route_state["breadcrumb_chain"] = [
        "VectorFL Page",
        active_surface,
    ]
    route_state["contextual_panel_entry"] = {
        "active_panel": data.get("contextual_panels", {}).get("active_panel"),
        "entry_targets": data.get("route_state_preview", {}).get("contextual_entry_targets")
        or data.get("contextual_panels", {}).get("available_panels", []),
    }
    route_state["route_note"] = (
        "Current Reading remains the semantic center even when another primary surface is opened as the active page state."
    )
    data["route_state_preview"] = route_state
    data["active_primary_surface"] = active_surface
    return data


def render_vectorfl_page_route_aware_mock_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Route-Aware Mock</title>
  <style>
    :root {
      --bg: #f4efe7;
      --panel: #fffaf2;
      --panel-soft: #f7f1e6;
      --line: #d7cab7;
      --line-strong: #7a5631;
      --ink: #5b422a;
      --muted: #6b7280;
      --chip: #efe5d3;
      --shadow: 0 12px 30px rgba(91, 66, 42, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: #1f2937; font-family: Georgia, serif; }
    .page { max-width: 1700px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .header, .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 20px; box-shadow: var(--shadow); }
    .header { padding: 16px 18px; }
    .shell { display: grid; grid-template-columns: 240px minmax(0, 1fr) 340px; gap: 16px; align-items: start; }
    .panel { padding: 16px; display: grid; gap: 12px; }
    .panel.soft { background: var(--panel-soft); }
    .stack { display: grid; gap: 12px; }
    .nav-item { display: grid; gap: 4px; text-decoration: none; color: var(--ink); border: 1px solid #eadfcf; border-radius: 14px; background: #fff; padding: 10px 12px; }
    .nav-item.active { background: #efe2c2; border-color: var(--line-strong); }
    .kicker, .label { color: var(--muted); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    h1, h2, h3 { margin: 0; color: var(--ink); }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { display: inline-flex; align-items: center; border-radius: 999px; padding: 6px 10px; font-size: 12px; background: var(--chip); color: var(--ink); }
    .card, .trace-item { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 12px; display: grid; gap: 6px; }
    .body-copy { line-height: 1.7; white-space: pre-wrap; }
    .simple-list { display: grid; gap: 6px; margin: 0; padding-left: 18px; }
  </style>
</head>
<body>
  <script id="vectorfl-page-route-aware-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-route-aware-data').textContent);
    const app = document.getElementById('app');
    const active = data.active_primary_surface;
    const nav = data.navigation_items || [];
    const routeState = data.route_state_preview || {};
    const queue = data.queue_preview || [];
    const intake = data.inputs_preview || {};
    const current = data.current_reading || {};
    const history = data.history_trace_preview || {};
    const programs = data.programs_connections_preview || {};
    const responsibility = data.current_responsibility || {};
    const progression = data.progression_preview || {};
    const contextual = data.organ_detail_panels || {};

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    function navItem(item) {
      return `<a href="#" class="nav-item ${item.active ? 'active' : ''}"><strong>${item.label}</strong><span class="meta">${item.active ? 'active primary surface' : 'support surface'}</span></a>`;
    }

    function renderPrimarySurface() {
      if (active === 'cases-queue') {
        return `
          <section class="panel">
            <div class="kicker">Primary Surface / Cases / Queue</div>
            <h2>Cases / Queue</h2>
            <div class="meta">Entry surface before current-reading drill-in.</div>
            <div class="stack">
              ${queue.map((item) => `
                <div class="card">
                  <strong>${item.headline || item.case_id}</strong>
                  <div class="meta">case=${item.case_id} / organ=${item.current_organ_ref || 'unknown'} / lane=${item.lane_kind || 'unknown'}</div>
                  <div class="chip-row">
                    ${chip(`hold=${item.hold_state || 'unknown'}`)}
                    ${(item.restriction_flags || []).map(chip).join("")}
                  </div>
                  <div class="body-copy">${item.placement_reason_short || 'no placement reason'}</div>
                  <div class="meta">preferred next=${item.preferred_next_candidate || 'none'}</div>
                </div>
              `).join("")}
            </div>
          </section>
        `;
      }
      if (active === 'inputs-intake') {
        return `
          <section class="panel">
            <div class="kicker">Primary Surface / Inputs / Intake</div>
            <h2>Inputs / Intake</h2>
            <div class="meta">Material surface before case/lane meaning is finalized.</div>
            <div class="card">
              <strong>${intake.source_id || 'no source id'}</strong>
              <div class="meta">kind=${intake.source_kind || 'unknown'} / family=${intake.source_family || 'unknown'} / classification=${intake.intake_classification || 'unknown'}</div>
              <div class="chip-row">${(intake.matched_context_layers || []).map(chip).join("")}</div>
              <div class="body-copy">${intake.weakness_note || 'no weakness note'}</div>
              <div class="meta">fallback=${String(!!intake.fallback_used)} / readiness=${intake.readiness_level || 'unknown'} / reread=${String(!!intake.re_read_needed)}</div>
            </div>
          </section>
        `;
      }
      if (active === 'history-trace') {
        return `
          <section class="panel">
            <div class="kicker">Primary Surface / History / Trace</div>
            <h2>History / Trace</h2>
            <div class="meta">Retrospective carry surface for residue, reentry, and decision anchors.</div>
            <div class="stack">
              ${(history.latest_trace_list || []).map((item) => `
                <div class="trace-item">
                  <div class="label">${item.trace_kind || 'trace'}</div>
                  <strong>${item.summary || 'no summary'}</strong>
                  <div class="meta">residue=${item.residue_note || 'none'}</div>
                  <div class="body-copy">${item.reentry_hint || 'no reentry hint'}</div>
                </div>
              `).join("")}
            </div>
          </section>
        `;
      }
      if (active === 'programs-connections') {
        return `
          <section class="panel">
            <div class="kicker">Primary Surface / Programs / Connections</div>
            <h2>Programs / Connections</h2>
            <div class="meta">Boundary surface for linked programs and request constraints.</div>
            <div class="card">
              <div class="chip-row">
                ${chip(`state=${programs.connection_state || 'unknown'}`)}
                ${(programs.linked_programs || []).map(chip).join("")}
              </div>
              <div class="body-copy">${programs.action_request_preview || 'no action request preview'}</div>
            </div>
          </section>
        `;
      }
      return `
        <section class="panel">
          <div class="kicker">Primary Surface / Current Reading</div>
          <h2>${(current.body || {}).headline || 'Current Reading'}</h2>
          <div class="meta">Current Reading remains the semantic center.</div>
          <div class="card">
            <div class="label">Current Responsibility</div>
            <strong>${responsibility.current_organ_ref || 'unknown organ'}</strong>
            <div class="body-copy">${responsibility.placement_reason || 'no placement reason'}</div>
            <div class="chip-row">${(responsibility.restriction_flags || []).map(chip).join("")}</div>
          </div>
          <div class="card">
            <div class="label">Current Reading Body</div>
            <div class="body-copy">${(current.body || {}).summary_body_text || 'no body text'}</div>
          </div>
          <div class="card">
            <div class="label">Progression</div>
            <strong>${(progression.current_step || {}).organ_ref || 'none'}</strong>
            <div class="body-copy">${(progression.current_step || {}).summary || 'none'}</div>
          </div>
        </section>
      `;
    }

    function renderContextPanel(detail, heading) {
      const organ = detail.organ_identity || {};
      const bundle = detail.instruction_bundle_preview || {};
      const recent = detail.recent_return_preview || {};
      return `
        <section class="panel soft">
          <div class="kicker">${heading}</div>
          <h3>${organ.organ_label || 'Organ Detail'}</h3>
          <div class="meta">organ=${organ.organ_ref || 'unknown'} / status=${organ.current_status || 'unknown'}</div>
          <div class="body-copy">${bundle.role_sentence || 'none'}</div>
          <div class="label">Recent Return</div>
          <div class="body-copy">${recent.summary_return || 'none'}</div>
        </section>
      `;
    }

    app.innerHTML = `
      <div class="page">
        <section class="header">
          <div class="kicker">VectorFL Page / Route-Aware Mock</div>
          <h1>${data.page_title || 'VectorFL Page'}</h1>
          <div class="meta">active_primary=${routeState.active_primary_surface || active} / active_nav=${routeState.active_nav_key || 'unknown'} / contextual_panel=${routeState.active_contextual_panel || 'none'}</div>
          <div class="meta">breadcrumb=${(routeState.breadcrumb_chain || []).join(' / ')}</div>
          <div class="meta">${routeState.route_note || routeState.note || ''}</div>
        </section>
        <div class="shell">
          <aside class="panel stack">
            <div class="kicker">Primary Navigation</div>
            ${nav.map(navItem).join("")}
          </aside>
          <main class="stack">
            ${renderPrimarySurface()}
          </main>
          <aside class="stack">
            ${renderContextPanel(contextual.current || {}, 'Contextual Panel / Current Organ')}
            ${renderContextPanel(contextual.governance_candidate || {}, 'Contextual Panel / Preferred Next Candidate')}
          </aside>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_route_aware_mock_set(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock" / "routes")
    root.mkdir(parents=True, exist_ok=True)

    written: List[Dict[str, str]] = []
    for surface in PRIMARY_SURFACES:
        data = build_vectorfl_page_route_aware_mock_data(repo_root, active_surface=surface)
        html = render_vectorfl_page_route_aware_mock_html(data)
        html_path = root / f"{surface}.html"
        json_path = root / f"{surface}.json"
        html_path.write_text(html, encoding="utf-8")
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        written.append(
            {
                "surface": surface,
                "html_path": str(html_path),
                "json_path": str(json_path),
            }
        )
    return {"output_dir": str(root), "routes": written}
