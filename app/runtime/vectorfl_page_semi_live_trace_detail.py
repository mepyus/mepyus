from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json

from app.runtime.vectorfl_page_semi_live_shell import build_vectorfl_page_semi_live_state


def _slugify_trace_id(trace_id: str) -> str:
    return (
        trace_id.replace(":", "-")
        .replace("/", "-")
        .replace(" ", "-")
    )


def build_vectorfl_page_semi_live_trace_detail_set(repo_root: Path) -> List[Dict[str, Any]]:
    base = build_vectorfl_page_semi_live_state(repo_root)
    history = base.get("history_trace_preview") or {}
    trace_items = history.get("latest_trace_list") or []
    result: List[Dict[str, Any]] = []
    for item in trace_items:
        trace_id = item.get("trace_id") or "trace-unknown"
        result.append(
            {
                "page_title": f"VectorFL Page / Semi-Live / Trace / {trace_id}",
                "trace_id": trace_id,
                "trace_slug": _slugify_trace_id(trace_id),
                "trace_kind": item.get("trace_kind"),
                "summary": item.get("summary"),
                "residue_note": item.get("residue_note"),
                "reentry_hint": item.get("reentry_hint"),
                "created_at": item.get("created_at"),
                "decision_trace_anchor": history.get("decision_trace_anchor"),
                "residue_emphasis": history.get("residue_emphasis") or [],
                "reentry_cues": history.get("reentry_cues") or [],
                "context_links": {
                    "history_trace": "../semi_live_routes/history-trace.html",
                    "current_reading": "../semi_live_routes/current-reading.html",
                },
            }
        )
    return result


def render_vectorfl_page_semi_live_trace_detail_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Semi-Live Trace Detail</title>
  <style>
    :root { --bg:#f3f5f7; --panel:#fcfcfd; --line:#d7dde4; --ink:#111827; --muted:#667085; }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .page { max-width: 1200px; margin: 0 auto; padding: 16px; display: grid; gap: 12px; }
    .panel { background: var(--panel); border: 1px solid var(--line); padding: 14px; display: grid; gap: 10px; }
    .stack { display: grid; gap: 10px; }
    .card { background: #fcfcfd; border: 1px solid var(--line); padding: 10px; display: grid; gap: 6px; }
    .kicker, .label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .08em; font-weight: 600; }
    h1, h2 { margin: 0; color: var(--ink); }
    h1 { font-size: 18px; font-weight: 700; }
    h2 { font-size: 15px; font-weight: 600; }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--muted); }
    .body-copy { line-height: 1.65; white-space: pre-wrap; font-size: 13px; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 8px; }
    .nav-link { background: #fcfcfd; border: 1px solid var(--line); padding: 5px 8px; color: var(--ink); text-decoration: none; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
    .simple-list { display: grid; gap: 4px; margin: 0; padding-left: 18px; font-size: 13px; }
    .section-head { display: flex; align-items: end; justify-content: space-between; gap: 12px; }
  </style>
</head>
<body>
  <script id="vectorfl-page-semi-live-trace-detail-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-semi-live-trace-detail-data').textContent);
    const app = document.getElementById('app');
    const hints = Array.isArray(data.reentry_hint) ? data.reentry_hint : [data.reentry_hint].filter(Boolean);
    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page / Semi-Live Trace Detail</div>
          <div class="section-head">
            <h1>${data.trace_id || 'Trace Detail'}</h1>
            <div class="mono">${data.trace_kind || 'unknown trace kind'}</div>
          </div>
          <div class="meta">kind=${data.trace_kind || 'unknown'} / created=${data.created_at || 'unknown'} / anchor=${data.decision_trace_anchor || 'none'}</div>
          <div class="nav-links">
            <a class="nav-link" href="${(data.context_links || {}).history_trace || '#'}">History / Trace</a>
            <a class="nav-link" href="${(data.context_links || {}).current_reading || '#'}">Current Reading</a>
          </div>
        </section>
        <section class="panel">
          <div class="kicker">Trace Summary</div>
          <div class="body-copy">${data.summary || 'none'}</div>
          <div class="label">Residue Note</div>
          <div class="body-copy">${data.residue_note || 'none'}</div>
        </section>
        <section class="panel stack">
          <div class="kicker">Reentry Reading</div>
          <div class="card">
            <div class="label">Direct Reentry Hint</div>
            <ul class="simple-list">${hints.map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
          </div>
          <div class="card">
            <div class="label">Residue Emphasis</div>
            <ul class="simple-list">${(data.residue_emphasis || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
          </div>
          <div class="card">
            <div class="label">Reentry Cues</div>
            <ul class="simple-list">${(data.reentry_cues || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
          </div>
        </section>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_semi_live_trace_detail_set(
    repo_root: Path,
    *,
    output_dir: Path | None = None,
) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell" / "semi_live_trace_detail")
    root.mkdir(parents=True, exist_ok=True)

    items = build_vectorfl_page_semi_live_trace_detail_set(repo_root)
    outputs = []
    for item in items:
        html = render_vectorfl_page_semi_live_trace_detail_html(item)
        html_path = root / f"{item['trace_slug']}.html"
        json_path = root / f"{item['trace_slug']}.json"
        html_path.write_text(html, encoding="utf-8")
        json_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append(
            {
                "trace_id": item["trace_id"],
                "trace_slug": item["trace_slug"],
                "html_path": str(html_path),
                "json_path": str(json_path),
            }
        )
    return {"output_dir": str(root), "outputs": outputs}
