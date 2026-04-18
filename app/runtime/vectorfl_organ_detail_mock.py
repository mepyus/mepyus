from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json


def load_vectorfl_translation_organ_detail_mock_fixture(repo_root: Path) -> Dict[str, Any]:
    fixture_path = repo_root / "runtime" / "manifests" / "vectorfl_translation_organ_detail_mock_fixture_v0.json"
    return json.loads(fixture_path.read_text(encoding="utf-8"))


def build_vectorfl_organ_detail_mock_data(repo_root: Path) -> Dict[str, Any]:
    fixture = load_vectorfl_translation_organ_detail_mock_fixture(repo_root)
    return {
        "state": "loaded",
        "page_title": "VectorFL Page / Organ Detail Mock",
        "fixture_id": fixture.get("fixture_id"),
        "organ_identity": fixture.get("organ_identity") or {},
        "instruction_bundle_preview": fixture.get("instruction_bundle_preview") or {},
        "accepted_handoff_preview": fixture.get("accepted_handoff_preview") or {},
        "caution_profile": fixture.get("caution_profile") or {},
        "recent_return_preview": fixture.get("recent_return_preview") or {},
    }


def render_vectorfl_organ_detail_mock_html(data: Dict[str, Any]) -> str:
    payload_block = (
        f'<script id="vectorfl-organ-detail-mock-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>'
    )
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Organ Detail Mock</title>
  <style>
    :root {
      --bg: #f3ede3;
      --panel: #fff9f0;
      --line: #d9cdbb;
      --ink: #5b422a;
      --muted: #6b7280;
      --chip: #efe4d1;
      --shadow: 0 10px 26px rgba(91, 66, 42, 0.08);
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: #1f2937; font-family: Georgia, serif; }
    .page { max-width: 1320px; margin: 0 auto; padding: 20px; display: grid; gap: 16px; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 16px; box-shadow: var(--shadow); }
    .grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 16px; }
    .stack { display: grid; gap: 12px; }
    h1, h2, h3 { margin: 0 0 10px; color: var(--ink); }
    .kicker, .label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
    .meta { color: var(--muted); font-size: 13px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; }
    .chip { display: inline-flex; padding: 6px 10px; border-radius: 999px; background: var(--chip); color: var(--ink); font-size: 12px; }
    .card { border: 1px solid #eadfcf; background: #fff; border-radius: 14px; padding: 12px; display: grid; gap: 6px; }
    .simple-list { display: grid; gap: 6px; margin: 0; padding-left: 18px; }
    .body-copy { line-height: 1.7; white-space: pre-wrap; }
  </style>
</head>
<body>
  """ + payload_block + """
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-organ-detail-mock-data').textContent);
    const app = document.getElementById('app');
    const organ = data.organ_identity || {};
    const bundle = data.instruction_bundle_preview || {};
    const handoff = data.accepted_handoff_preview || {};
    const caution = data.caution_profile || {};
    const recent = data.recent_return_preview || {};

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page / Organ Detail Mock</div>
          <h1>${organ.organ_label || 'Organ Detail'}</h1>
          <div class="meta">fixture=${data.fixture_id || 'unknown'} / organ=${organ.organ_ref || 'unknown'} / status=${organ.current_status || 'unknown'}</div>
          <div class="chip-row" style="margin-top:10px;">
            ${(organ.related_lane_refs || []).map(chip).join("")}
          </div>
        </section>

        <div class="grid">
          <section class="panel stack">
            <div class="card">
              <div class="label">Role Sentence</div>
              <div class="body-copy">${bundle.role_sentence || 'none'}</div>
            </div>
            <div class="card">
              <div class="label">Reading Priorities</div>
              <ul class="simple-list">
                ${(bundle.reading_priorities || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
            <div class="card">
              <div class="label">Output Contract</div>
              <ul class="simple-list">
                ${(bundle.output_contract || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
          </section>

          <section class="panel stack">
            <div class="card">
              <div class="label">Accepted Inputs</div>
              <ul class="simple-list">
                ${(handoff.accepted_input_kinds || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
            <div class="card">
              <div class="label">Required Packet Fields</div>
              <ul class="simple-list">
                ${(handoff.required_packet_fields || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
            <div class="card">
              <div class="label">Common Triggers</div>
              <ul class="simple-list">
                ${(handoff.common_triggers || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
          </section>
        </div>

        <div class="grid">
          <section class="panel stack">
            <div class="card">
              <div class="label">Stop / Hold Conditions</div>
              <ul class="simple-list">
                ${(caution.stop_hold_conditions || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
            <div class="card">
              <div class="label">Preserve-First Rules</div>
              <ul class="simple-list">
                ${(caution.preserve_first_rules || []).map((item) => `<li>${item}</li>`).join("") || '<li>none</li>'}
              </ul>
            </div>
          </section>

          <section class="panel stack">
            <div class="card">
              <div class="label">Recent Summary Return</div>
              <div class="body-copy">${recent.summary_return || 'none'}</div>
            </div>
            <div class="card">
              <div class="label">Lane Hint Update</div>
              <div class="chip-row">${(recent.lane_hint_update || []).map(chip).join("")}</div>
            </div>
            <div class="card">
              <div class="label">Recent Trace Carry</div>
              <div class="chip-row">${(recent.recent_trace_carry || []).map(chip).join("")}</div>
              <div class="meta">next handoff=${recent.recent_handoff_target || 'none'}</div>
            </div>
          </section>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_organ_detail_mock(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_organ_detail_mock_data(repo_root)
    html = render_vectorfl_organ_detail_mock_html(data)

    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_mock")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "organ_detail_mock.html"
    json_path = root / "organ_detail_mock.json"

    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
