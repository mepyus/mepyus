from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json

from app.runtime.vectorfl_page_semi_live_shell import build_vectorfl_page_semi_live_state


def _slug(prefix: str, value: str) -> str:
    return f"{prefix}-{value.replace(':', '-').replace('/', '-').replace(' ', '-')}"


def build_vectorfl_page_semi_live_program_detail_set(repo_root: Path) -> List[Dict[str, Any]]:
    base = build_vectorfl_page_semi_live_state(repo_root)
    programs = base.get("programs_connections_preview") or {}
    outputs: List[Dict[str, Any]] = []

    for item in programs.get("saved_connection_preview") or []:
        item_id = item.get("id") or "connection"
        outputs.append(
            {
                "detail_kind": "saved_connection",
                "detail_slug": _slug("saved-connection", item_id),
                "page_title": f"VectorFL Page / Semi-Live / Saved Connection / {item_id}",
                "title": item.get("value_label") or item_id,
                "summary": item.get("relation_summary"),
                "source_pointer": item.get("source_pointer"),
                "linked_programs": programs.get("linked_programs") or [],
                "connection_state": programs.get("connection_state"),
                "governance_restriction_summary": programs.get("governance_restriction_summary") or [],
                "context_links": {
                    "programs_connections": "../semi_live_routes/programs-connections.html",
                    "current_reading": "../semi_live_routes/current-reading.html",
                },
            }
        )

    for item in programs.get("attention_memory_preview") or []:
        asset_id = item.get("asset_id") or "attention"
        outputs.append(
            {
                "detail_kind": "attention_memory",
                "detail_slug": _slug("attention", asset_id),
                "page_title": f"VectorFL Page / Semi-Live / Attention / {asset_id}",
                "title": item.get("attention_pattern_summary") or asset_id,
                "summary": ", ".join(item.get("dominant_attention_reasons") or []) or "no dominant attention reasons",
                "source_pointer": asset_id,
                "active_attention_count": item.get("active_attention_count"),
                "linked_programs": programs.get("linked_programs") or [],
                "connection_state": programs.get("connection_state"),
                "governance_restriction_summary": programs.get("governance_restriction_summary") or [],
                "context_links": {
                    "programs_connections": "../semi_live_routes/programs-connections.html",
                    "current_reading": "../semi_live_routes/current-reading.html",
                },
            }
        )

    return outputs


def render_vectorfl_page_semi_live_program_detail_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Semi-Live Program Detail</title>
  <style>
    :root { --bg:#f3f5f7; --panel:#fcfcfd; --line:#d7dde4; --ink:#111827; --muted:#667085; --chip:#eef2f6; }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .page { max-width: 1100px; margin: 0 auto; padding: 16px; display: grid; gap: 12px; }
    .panel { background: var(--panel); border: 1px solid var(--line); padding: 14px; display: grid; gap: 10px; }
    .card { background: #fcfcfd; border: 1px solid var(--line); padding: 10px; display: grid; gap: 6px; }
    .kicker, .label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .08em; font-weight: 600; }
    h1, h2 { margin: 0; color: var(--ink); }
    h1 { font-size: 18px; font-weight: 700; }
    h2 { font-size: 15px; font-weight: 600; }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .body-copy { line-height: 1.65; white-space: pre-wrap; font-size: 13px; }
    .chip { display: inline-flex; background: var(--chip); border: 1px solid var(--line); border-radius: 999px; padding: 4px 8px; font-size: 11px; margin: 0 6px 6px 0; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 8px; }
    .nav-link { background: #fcfcfd; border: 1px solid var(--line); padding: 5px 8px; color: var(--ink); text-decoration: none; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
  </style>
</head>
<body>
  <script id="vectorfl-page-semi-live-program-detail-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-semi-live-program-detail-data').textContent);
    const app = document.getElementById('app');
    function chip(text) { return `<span class="chip">${text}</span>`; }
    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page / Semi-Live Program Detail</div>
          <h1>${data.title || 'Program Detail'}</h1>
          <div class="meta">kind=${data.detail_kind || 'unknown'} / state=${data.connection_state || 'unknown'}</div>
          <div class="nav-links">
            <a class="nav-link" href="${(data.context_links || {}).programs_connections || '#'}">Programs / Connections</a>
            <a class="nav-link" href="${(data.context_links || {}).current_reading || '#'}">Current Reading</a>
          </div>
        </section>
        <section class="panel">
          <div class="kicker">Relation Summary</div>
          <div class="body-copy">${data.summary || 'none'}</div>
          <div class="label">Source Pointer</div>
          <div class="meta">${data.source_pointer || 'none'}</div>
        </section>
        <section class="panel">
          <div class="kicker">Boundary Conditions</div>
          <div class="chip-row">${(data.linked_programs || []).map(chip).join('') || chip('no linked program')}</div>
          <div class="chip-row">${(data.governance_restriction_summary || []).map(chip).join('') || chip('no restriction')}</div>
          ${data.active_attention_count !== undefined ? `<div class="meta">active_attention_count=${data.active_attention_count}</div>` : ''}
        </section>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_semi_live_program_detail_set(
    repo_root: Path,
    *,
    output_dir: Path | None = None,
) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell" / "semi_live_program_detail")
    root.mkdir(parents=True, exist_ok=True)

    outputs = []
    for item in build_vectorfl_page_semi_live_program_detail_set(repo_root):
        html = render_vectorfl_page_semi_live_program_detail_html(item)
        html_path = root / f"{item['detail_slug']}.html"
        json_path = root / f"{item['detail_slug']}.json"
        html_path.write_text(html, encoding="utf-8")
        json_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append(
            {
                "detail_kind": item["detail_kind"],
                "detail_slug": item["detail_slug"],
                "html_path": str(html_path),
                "json_path": str(json_path),
            }
        )
    return {"output_dir": str(root), "outputs": outputs}
