from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import json


def build_vectorfl_page_runtime_entry_data(repo_root: Path) -> Dict[str, object]:
    base = repo_root / "runtime" / "views"
    sections: List[Dict[str, object]] = [
        {
            "title": "Recommended Entry Order",
            "summary": "Current Reading stays canonical center, but the runtime entry should let the operator inspect shell, semi-live routes, organ detail, trace carry, and program boundary in one place.",
            "items": [
                {"label": "VectorFL Paper Launchpad", "href": str(base / "vectorfl_page" / "launchpad.html")},
                {"label": "Semi-Live Current Reading", "href": str(base / "vectorfl_page_shell" / "semi_live_routes" / "current-reading.html")},
                {"label": "Semi-Live Cases / Queue", "href": str(base / "vectorfl_page_shell" / "semi_live_routes" / "cases-queue.html")},
                {"label": "Semi-Live Inputs / Intake", "href": str(base / "vectorfl_page_shell" / "semi_live_routes" / "inputs-intake.html")},
            ],
        },
        {
            "title": "Operable Surface Reset",
            "summary": "Paperclip-native page classes reowned by VectorFL: work list, work detail, right-side inspector, routing editor, organ management, organ registry, operable organ editor, and trace audit.",
            "items": [
                {"label": "Operable Surface Index", "href": str(base / "vectorfl_operable_surface" / "index.html")},
                {"label": "Cases / Work List", "href": str(base / "vectorfl_operable_surface" / "cases.html")},
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
            "title": "Organ Drill-In",
            "summary": "Responsibility drill-in surfaces derived from the same semi-live runtime bridge.",
            "items": [
                {"label": "Input Organ Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "input.html")},
                {"label": "Current Organ Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "current.html")},
                {"label": "Governance Organ Detail", "href": str(base / "vectorfl_page_shell" / "semi_live_organ_detail" / "governance.html")},
            ],
        },
        {
            "title": "Carry Drill-In",
            "summary": "Trace and program boundary detail pages that keep residue, reentry, and external relation summaries inspectable.",
            "items": [
                {"label": "Trace Detail / Preflight", "href": str(base / "vectorfl_page_shell" / "semi_live_trace_detail" / "preflight_20260405T074526_912614_827bbb.html")},
                {"label": "Trace Detail / Runtime Phase Signals", "href": str(base / "vectorfl_page_shell" / "semi_live_trace_detail" / "trace-runtime_phase_signals.html")},
                {"label": "Program Detail / Saved Connection", "href": str(base / "vectorfl_page_shell" / "semi_live_program_detail" / "saved-connection-conn_choi_ai_classroom_vlm_state_grounding_status_inputs_external_cases_choi_ai_cl.html")},
                {"label": "Program Detail / Attention", "href": str(base / "vectorfl_page_shell" / "semi_live_program_detail" / "attention-choi_ai_classroom_vlm.html")},
            ],
        },
    ]
    return {
        "page_title": "VectorFL Paper Runtime Entry",
        "core_sentence": "This entry groups the current VectorFL Paper prototype into one runtime-facing inspection page so the local viewer can open the shell, the semi-live routes, and the bounded drill-in surfaces from one starting point.",
        "sections": sections,
        "viewer_note": "Serve the runtime root with the local viewer server and open the runtime entry or launchpad first; Current Reading remains the preferred semantic center.",
    }


def render_vectorfl_page_runtime_entry_html(data: Dict[str, object]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Paper Runtime Entry</title>
  <style>
    :root{--bg:#fff;--panel:#fff;--line:#e5e7eb;--ink:#111827;--muted:#6b7280}
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
  <script id="vectorfl-paper-runtime-entry-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-paper-runtime-entry-data').textContent);
    const app = document.getElementById('app');
    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Paper Runtime Entry</div>
          <div class="section-head">
            <h1>${data.page_title || 'VectorFL Paper Runtime Entry'}</h1>
            <div class="mono">current-reading-first local entry</div>
          </div>
          <div class="meta">${data.core_sentence || ''}</div>
          <div class="meta" style="margin-top:8px;">${data.viewer_note || ''}</div>
        </section>
        ${(data.sections || []).map((section) => `
          <section class="panel">
            <div class="section-head">
              <h2>${section.title}</h2>
              <div class="mono">${(section.items || []).length} links</div>
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


def write_vectorfl_page_runtime_entry(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_page_runtime_entry_data(repo_root)
    html = render_vectorfl_page_runtime_entry_html(data)
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "runtime_entry.html"
    json_path = root / "runtime_entry.json"
    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
