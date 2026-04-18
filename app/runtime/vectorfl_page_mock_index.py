from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import json


def build_vectorfl_page_mock_index_data(repo_root: Path) -> Dict[str, object]:
    view_root = repo_root / "runtime" / "views" / "vectorfl_page_mock"
    route_root = view_root / "routes"
    items: List[Dict[str, str]] = [
        {
            "title": "Unified Shell Mock",
            "slug": "unified_shell_mock",
            "html_path": str(view_root / "unified_shell_mock.html"),
            "json_path": str(view_root / "unified_shell_mock.json"),
            "summary": "Current Reading centered app-like shell with queue, intake, governance, trace, programs, and contextual organ detail in one frame.",
        },
        {
            "title": "First Shell Mock",
            "slug": "first_shell_mock",
            "html_path": str(view_root / "first_shell_mock.html"),
            "json_path": str(view_root / "first_shell_mock.json"),
            "summary": "Earlier multi-surface shell mock focused on current responsibility and progression preview.",
        },
        {
            "title": "Current Reading Mock",
            "slug": "current_reading_mock",
            "html_path": str(view_root / "current_reading_mock.html"),
            "json_path": str(view_root / "current_reading_mock.json"),
            "summary": "Single-surface current-reading console mock centered on case, governance, and trace.",
        },
        {
            "title": "Organ Detail Mock",
            "slug": "organ_detail_mock",
            "html_path": str(view_root / "organ_detail_mock.html"),
            "json_path": str(view_root / "organ_detail_mock.json"),
            "summary": "Contextual organ detail surface showing instruction bundle, handoff, caution, and return structure.",
        },
    ]

    route_items: List[Dict[str, str]] = [
        {
            "title": "Current Reading Route",
            "slug": "route_current_reading",
            "html_path": str(route_root / "current-reading.html"),
            "json_path": str(route_root / "current-reading.json"),
            "summary": "Canonical center route with current-reading as active primary surface.",
        },
        {
            "title": "Cases / Queue Route",
            "slug": "route_cases_queue",
            "html_path": str(route_root / "cases-queue.html"),
            "json_path": str(route_root / "cases-queue.json"),
            "summary": "Entry route where queue/progression preview is primary but current-reading remains semantic center.",
        },
        {
            "title": "Inputs / Intake Route",
            "slug": "route_inputs_intake",
            "html_path": str(route_root / "inputs-intake.html"),
            "json_path": str(route_root / "inputs-intake.json"),
            "summary": "Material route where intake, weakness, and packet readiness become the active surface.",
        },
        {
            "title": "History / Trace Route",
            "slug": "route_history_trace",
            "html_path": str(route_root / "history-trace.html"),
            "json_path": str(route_root / "history-trace.json"),
            "summary": "Carry route for residue, reentry, and decision trace review.",
        },
        {
            "title": "Programs / Connections Route",
            "slug": "route_programs_connections",
            "html_path": str(route_root / "programs-connections.html"),
            "json_path": str(route_root / "programs-connections.json"),
            "summary": "Boundary route for linked program state and request limitations.",
        },
    ]

    return {
        "page_title": "VectorFL Page Mock Index",
        "core_sentence": "VectorFL Page mock set is read current-reading-first, with unified shell as the primary app-like surface and organ detail as a contextual drill-in rather than a separate product center.",
        "entry_order": [
            "Unified Shell Mock",
            "Route-Aware Surface Set",
            "Organ Detail Mock",
            "Current Reading Mock",
            "First Shell Mock",
        ],
        "items": items,
        "route_items": route_items,
    }


def render_vectorfl_page_mock_index_html(data: Dict[str, object]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page Mock Index</title>
  <style>
    :root {
      --bg: #f4efe7;
      --panel: #fffaf2;
      --line: #d7cab7;
      --ink: #5b422a;
      --muted: #6b7280;
      --shadow: 0 12px 30px rgba(91, 66, 42, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: #1f2937; font-family: Georgia, serif; }
    .page { max-width: 1080px; margin: 0 auto; padding: 24px; display: grid; gap: 16px; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 18px; box-shadow: var(--shadow); }
    .grid { display: grid; gap: 14px; }
    .card { background: #fff; border: 1px solid #eadfcf; border-radius: 14px; padding: 14px; display: grid; gap: 8px; }
    .kicker { color: var(--muted); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    h1, h2 { margin: 0; color: var(--ink); }
    .meta { color: var(--muted); font-size: 13px; }
    a { color: #7a5631; text-decoration: none; }
  </style>
</head>
<body>
  <script id="vectorfl-page-mock-index-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-mock-index-data').textContent);
    const app = document.getElementById('app');
    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page Mock Index</div>
          <h1>${data.page_title || 'VectorFL Page Mock Index'}</h1>
          <div class="meta">${data.core_sentence || ''}</div>
          <div class="meta" style="margin-top:8px;">entry order: ${(data.entry_order || []).join(' -> ')}</div>
        </section>
        <section class="panel grid">
          ${(data.items || []).map((item) => `
            <div class="card">
              <h2>${item.title}</h2>
              <div class="meta">${item.summary}</div>
              <div><a href="${item.html_path}">HTML View</a></div>
              <div><a href="${item.json_path}">JSON Payload</a></div>
            </div>
          `).join("")}
        </section>
        <section class="panel grid">
          ${(data.route_items || []).map((item) => `
            <div class="card">
              <h2>${item.title}</h2>
              <div class="meta">${item.summary}</div>
              <div><a href="${item.html_path}">HTML View</a></div>
              <div><a href="${item.json_path}">JSON Payload</a></div>
            </div>
          `).join("")}
        </section>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_mock_index(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_page_mock_index_data(repo_root)
    html = render_vectorfl_page_mock_index_html(data)

    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "index.html"
    json_path = root / "index.json"

    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
