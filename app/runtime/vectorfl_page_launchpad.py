from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import json


def build_vectorfl_page_launchpad_data(repo_root: Path) -> Dict[str, object]:
    base = repo_root / "runtime" / "views"
    sections: List[Dict[str, object]] = [
        {
            "title": "VectorFL Page / Mock Set",
            "summary": "Pure mock surfaces for semantic inspection before runtime bridging.",
            "items": [
                {"label": "Mock Index", "href": str(base / "vectorfl_page_mock" / "index.html")},
                {"label": "Unified Shell Mock", "href": str(base / "vectorfl_page_mock" / "unified_shell_mock.html")},
            ],
        },
        {
            "title": "VectorFL Page / App Shell",
            "summary": "Route-aware personal shell set with shared frame and contextual organ detail.",
            "items": [
                {"label": "App Shell Index", "href": str(base / "vectorfl_page_shell" / "index.html")},
                {"label": "Current Reading", "href": str(base / "vectorfl_page_shell" / "current-reading.html")},
                {"label": "Cases / Queue", "href": str(base / "vectorfl_page_shell" / "cases-queue.html")},
            ],
        },
        {
            "title": "VectorFL Operable Surface Reset",
            "summary": "Paperclip-native page classes reinterpreted as Cases, Case Detail, Case Inspector, Case Routing, Organs, Organ Registry, Organ Editor, and Trace Audit while keeping VectorFL core semantics intact.",
            "items": [
                {"label": "Operable Surface Index", "href": str(base / "vectorfl_operable_surface" / "index.html")},
                {"label": "Cases", "href": str(base / "vectorfl_operable_surface" / "cases.html")},
                {"label": "Case Detail", "href": str(base / "vectorfl_operable_surface" / "case-detail.html")},
                {"label": "Case Inspector", "href": str(base / "vectorfl_operable_surface" / "case-inspector.html")},
                {"label": "Line Review", "href": str(base / "vectorfl_operable_surface" / "line-review.html")},
                {"label": "Case Routing", "href": str(base / "vectorfl_operable_surface" / "case-routing.html")},
                {"label": "Internal Recall", "href": str(base / "vectorfl_operable_surface" / "internal-recall.html")},
                {"label": "External Resources", "href": str(base / "vectorfl_operable_surface" / "external-resources.html")},
                {"label": "Lanes", "href": str(base / "vectorfl_operable_surface" / "lanes.html")},
                {"label": "Lane Runs", "href": str(base / "vectorfl_operable_surface" / "lane-runs.html")},
                {"label": "Organs", "href": str(base / "vectorfl_operable_surface" / "organs.html")},
                {"label": "Organ Registry", "href": str(base / "vectorfl_operable_surface" / "organ-registry.html")},
                {"label": "ChatGPT Lane Editor", "href": str(base / "vectorfl_operable_surface" / "lane-editor-chatgpt.html")},
                {"label": "Translation Organ Editor", "href": str(base / "vectorfl_operable_surface" / "organ-editor-translation.html")},
                {"label": "Trace Audit", "href": str(base / "vectorfl_operable_surface" / "trace-audit.html")},
            ],
        },
        {
            "title": "VectorFL Page / Semi-Live",
            "summary": "Runtime-bridged shell and route set using current_phase, preflight, and engine_state surfaces.",
            "items": [
                {"label": "Semi-Live Current Reading", "href": str(base / "vectorfl_page_shell" / "semi_live" / "current-reading.html")},
                {"label": "Semi-Live Route Index", "href": str(base / "vectorfl_page_shell" / "semi_live_routes" / "index.html")},
                {"label": "Semi-Live Programs / Connections", "href": str(base / "vectorfl_page_shell" / "semi_live_routes" / "programs-connections.html")},
                {"label": "Semi-Live Current Organ Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "current.html")},
                {"label": "Semi-Live Governance Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "governance.html")},
                {"label": "Semi-Live Input Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "input.html")},
                {"label": "Semi-Live Trace Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_trace_detail" / "preflight_20260405T074526_912614_827bbb.html")},
                {"label": "Semi-Live Program Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_program_detail" / "saved-connection-conn_choi_ai_classroom_vlm_state_grounding_status_inputs_external_cases_choi_ai_cl.html")},
            ],
        },
    ]
    return {
        "page_title": "VectorFL Paper Launchpad",
        "core_sentence": "VectorFL Paper launchpad groups mock, app-shell, and semi-live shell states so the current prototype can be inspected as one evolving personal program.",
        "sections": sections,
    }


def render_vectorfl_page_launchpad_html(data: Dict[str, object]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Paper Launchpad</title>
  <style>
    :root{--bg:#fff;--panel:#fff;--panel-soft:#fafafa;--line:#e5e7eb;--ink:#111827;--muted:#6b7280;--active:#f5f5f5}
    *{box-sizing:border-box}
    body{margin:0;background:var(--bg);color:var(--ink);font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
    .page{max-width:1180px;margin:0 auto;padding:16px;display:grid;gap:12px}
    .panel{background:var(--panel);border:1px solid var(--line);padding:14px;display:grid;gap:12px}
    .grid{display:grid;gap:10px}
    .list-shell{border:1px solid var(--line);background:#fff}
    .card{padding:12px 14px;display:grid;gap:6px;border-bottom:1px solid var(--line)}
    .card:last-child{border-bottom:0}
    .kicker{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}
    h1,h2{margin:0;color:var(--ink)}
    h1{font-size:18px;font-weight:700}
    h2{font-size:14px;font-weight:600}
    .meta{color:#6b7280;font-size:13px;line-height:1.5}
    .mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--muted)}
    .section-head{display:flex;align-items:end;justify-content:space-between;gap:12px}
    a{color:inherit;text-decoration:none}
  </style>
</head>
<body>
  <script id="vectorfl-paper-launchpad-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-paper-launchpad-data').textContent);
    const app = document.getElementById('app');
    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Paper Launchpad</div>
          <div class="section-head">
            <h1>${data.page_title || 'VectorFL Paper Launchpad'}</h1>
            <div class="mono">runtime-oriented inspection index</div>
          </div>
          <div class="meta">${data.core_sentence || ''}</div>
        </section>
        ${(data.sections || []).map((section) => `
          <section class="panel">
            <div class="section-head">
              <h2>${section.title}</h2>
              <div class="mono">${(section.items || []).length} entries</div>
            </div>
            <div class="meta">${section.summary}</div>
            <div class="list-shell">
              ${(section.items || []).map((item) => `
              <div class="card">
                <a href="${item.href}">${item.label}</a>
              </div>
            `).join('')}
            </div>
          </section>
        `).join('')}
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_launchpad(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_page_launchpad_data(repo_root)
    html = render_vectorfl_page_launchpad_html(data)
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "launchpad.html"
    json_path = root / "launchpad.json"
    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
