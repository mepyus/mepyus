from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import json

from app.runtime.vectorfl_page_semi_live_shell import build_vectorfl_page_semi_live_state


DETAIL_KEYS = {
    "input": {
        "panel_key": "input",
        "title": "Input Organ Detail",
        "surface_key": "organ-detail-input",
    },
    "current": {
        "panel_key": "current",
        "title": "Current Organ Detail",
        "surface_key": "organ-detail-current",
    },
    "governance": {
        "panel_key": "governance_candidate",
        "title": "Governance Candidate Detail",
        "surface_key": "organ-detail-governance",
    },
}


def build_vectorfl_page_semi_live_organ_detail_state(
    repo_root: Path,
    *,
    detail_kind: str,
) -> Dict[str, Any]:
    if detail_kind not in DETAIL_KEYS:
        raise ValueError(f"Unsupported detail kind: {detail_kind}")

    base = build_vectorfl_page_semi_live_state(repo_root)
    spec = DETAIL_KEYS[detail_kind]
    detail = ((base.get("organ_detail_panels") or {}).get(spec["panel_key"]) or {})
    if detail_kind == "input" and not detail:
        intake = base.get("inputs_preview") or {}
        detail = {
            "organ_identity": {
                "organ_ref": "organ:input",
                "organ_label": "Input Organ",
                "current_status": intake.get("readiness_level") or "usable_with_caution",
            },
            "instruction_bundle_preview": {
                "role_sentence": "Register runtime-selected source material, keep context layers intact, and emit a cautious intake contract without pretending closure.",
                "primary_obligation": "Preserve provenance, context, weakness, and readiness while preparing material for downstream line-aware work.",
                "expected_return_fields": [
                    "source_ref",
                    "context_layers",
                    "classification",
                    "weakness_note",
                    "next_lane_hint",
                ],
            },
            "accepted_handoff_preview": {
                "accepted_input_kinds": [
                    "runtime_selected_artifact_group",
                    "surface_snapshot",
                    "trace_artifact",
                ],
                "required_carries": [
                    "provenance",
                    "context_layers",
                    "weakness",
                    "fallback",
                ],
                "next_preferred_targets": [
                    "organ:translation",
                    "organ:flow_interpretation",
                ],
            },
            "recent_return_preview": {
                "summary_return": f"Input bridge prepared {len(intake.get('selected_artifact_refs') or [])} artifact refs under {intake.get('source_subgroup') or 'unknown subgroup'} with fallback carry preserved.",
                "trace_anchor": intake.get("phase_source_turn"),
                "recommended_handoff_target": intake.get("next_lane_hint"),
            },
            "caution_profile": {
                "do_not": [
                    "Do not flatten runtime-selected artifacts into a fake canonical case packet.",
                    "Do not hide weak intake status or fallback use.",
                ],
                "escalation_triggers": [
                    "context layers missing",
                    "artifact roots ambiguous",
                    "requested artifact and first read diverge without note",
                ],
            },
            "semi_live_status": {
                "phase": intake.get("source_subgroup"),
                "decision": intake.get("next_lane_hint"),
                "candidate_count": len(intake.get("selected_artifact_refs") or []),
                "restriction_flags": [
                    "weak_intake_visible",
                    "fallback_carry_required",
                ],
                "recent_trace_ids": [intake.get("phase_source_turn")] if intake.get("phase_source_turn") else [],
            },
        }
    organ_identity = detail.get("organ_identity") or {}
    instruction_bundle = detail.get("instruction_bundle_preview") or {}
    accepted_handoff = detail.get("accepted_handoff_preview") or {}
    recent_return = detail.get("recent_return_preview") or {}
    caution_profile = detail.get("caution_profile") or {}
    semi_live_status = detail.get("semi_live_status") or {}

    return {
        "page_title": f"VectorFL Page / Semi-Live / {spec['surface_key']}",
        "detail_kind": detail_kind,
        "surface_key": spec["surface_key"],
        "title": spec["title"],
        "organ_identity": organ_identity,
        "instruction_bundle_preview": instruction_bundle,
        "accepted_handoff_preview": accepted_handoff,
        "recent_return_preview": recent_return,
        "caution_profile": caution_profile,
        "semi_live_status": semi_live_status,
        "context_links": {
            "current_reading": "../semi_live_routes/current-reading.html",
            "cases_queue": "../semi_live_routes/cases-queue.html",
            "inputs_intake": "../semi_live_routes/inputs-intake.html",
            "history_trace": "../semi_live_routes/history-trace.html",
            "programs_connections": "../semi_live_routes/programs-connections.html",
        },
    }


def render_vectorfl_page_semi_live_organ_detail_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Page / Semi-Live Organ Detail</title>
  <style>
    :root { --bg:#f3f5f7; --panel:#fcfcfd; --panel-soft:#f7f8fa; --line:#d7dde4; --ink:#111827; --muted:#667085; --chip:#eef2f6; }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--ink); font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .page { max-width: 1400px; margin: 0 auto; padding: 16px; display: grid; gap: 12px; }
    .panel { background: var(--panel); border: 1px solid var(--line); padding: 14px; display: grid; gap: 10px; }
    .grid { display: grid; grid-template-columns: 1.2fr 1fr; gap: 16px; align-items: start; }
    .stack { display: grid; gap: 10px; }
    .card { background: #fcfcfd; border: 1px solid var(--line); padding: 10px; display: grid; gap: 6px; }
    .kicker, .label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .08em; font-weight: 600; }
    h1, h2, h3 { margin: 0; color: var(--ink); }
    h1 { font-size: 18px; font-weight: 700; }
    h2 { font-size: 15px; font-weight: 600; }
    h3 { font-size: 14px; font-weight: 600; }
    .meta { color: var(--muted); font-size: 13px; line-height: 1.5; }
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--muted); }
    .body-copy { line-height: 1.65; white-space: pre-wrap; font-size: 13px; }
    .chip { display: inline-flex; background: var(--chip); border: 1px solid var(--line); border-radius: 999px; padding: 4px 8px; font-size: 11px; margin: 0 6px 6px 0; }
    .nav-links { display: flex; flex-wrap: wrap; gap: 8px; }
    .nav-link { background: #fcfcfd; border: 1px solid var(--line); padding: 5px 8px; color: var(--ink); text-decoration: none; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
    .simple-list { display: grid; gap: 4px; margin: 0; padding-left: 18px; font-size: 13px; }
    .section-head { display: flex; align-items: end; justify-content: space-between; gap: 12px; }
  </style>
</head>
<body>
  <script id="vectorfl-page-semi-live-organ-detail-data" type="application/json">""" + payload + """</script>
  <div id="app"></div>
  <script>
    const data = JSON.parse(document.getElementById('vectorfl-page-semi-live-organ-detail-data').textContent);
    const app = document.getElementById('app');
    const organ = data.organ_identity || {};
    const bundle = data.instruction_bundle_preview || {};
    const handoff = data.accepted_handoff_preview || {};
    const recent = data.recent_return_preview || {};
    const caution = data.caution_profile || {};
    const status = data.semi_live_status || {};
    const contextLinks = data.context_links || {};

    function chip(text) {
      return `<span class="chip">${text}</span>`;
    }

    app.innerHTML = `
      <div class="page">
        <section class="panel">
          <div class="kicker">VectorFL Page / Semi-Live Organ Detail</div>
          <div class="section-head">
            <h1>${data.title || 'Organ Detail'}</h1>
            <div class="mono">${data.surface_key || 'unknown surface'}</div>
          </div>
          <div class="meta">surface=${data.surface_key || 'unknown'} / organ=${organ.organ_ref || 'unknown'} / status=${organ.current_status || 'unknown'}</div>
          <div class="nav-links">
            <a class="nav-link" href="${contextLinks.current_reading || '#'}">Current Reading</a>
            <a class="nav-link" href="${contextLinks.cases_queue || '#'}">Cases / Queue</a>
            <a class="nav-link" href="${contextLinks.inputs_intake || '#'}">Inputs / Intake</a>
            <a class="nav-link" href="${contextLinks.history_trace || '#'}">History / Trace</a>
            <a class="nav-link" href="${contextLinks.programs_connections || '#'}">Programs / Connections</a>
          </div>
        </section>
        <div class="grid">
          <main class="stack">
            <section class="panel">
              <div class="kicker">Instruction Bundle</div>
              <h2>${organ.organ_label || 'Unknown Organ'}</h2>
              <div class="body-copy">${bundle.role_sentence || 'none'}</div>
              <div class="label">Primary Obligation</div>
              <div class="body-copy">${bundle.primary_obligation || 'none'}</div>
              <div class="label">Return Shape</div>
              <ul class="simple-list">${(bundle.expected_return_fields || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
            </section>
            <section class="panel">
              <div class="kicker">Accepted Handoff</div>
              <div class="label">Accepted Input Kinds</div>
              <ul class="simple-list">${(handoff.accepted_input_kinds || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
              <div class="label">Required Carries</div>
              <div class="chip-row">${(handoff.required_carries || []).map(chip).join('') || chip('none')}</div>
              <div class="label">Next Preferred Targets</div>
              <div class="chip-row">${(handoff.next_preferred_targets || []).map(chip).join('') || chip('none')}</div>
            </section>
          </main>
          <aside class="stack">
            <section class="panel">
              <div class="kicker">Semi-Live Status</div>
              <div class="meta">phase=${status.phase || 'none'} / decision=${status.decision || 'none'} / candidates=${status.candidate_count || 0}</div>
              <div class="body-copy">${(status.restriction_flags || []).join(' / ') || status.decision_reason || 'no semi-live restriction'}</div>
              <div class="meta">release=${status.release_condition || 'none'} / next_check=${status.next_check_trigger || 'none'}</div>
              <div class="meta">recent_traces=${(status.recent_trace_ids || []).join(', ') || 'none'}</div>
            </section>
            <section class="panel">
              <div class="kicker">Caution Profile</div>
              <div class="label">Do Not</div>
              <ul class="simple-list">${(caution.do_not || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
              <div class="label">Escalation Triggers</div>
              <ul class="simple-list">${(caution.escalation_triggers || []).map((item) => `<li>${item}</li>`).join('') || '<li>none</li>'}</ul>
            </section>
            <section class="panel">
              <div class="kicker">Recent Return</div>
              <div class="body-copy">${recent.summary_return || 'none'}</div>
              <div class="meta">trace=${recent.trace_anchor || 'none'} / handoff=${recent.recommended_handoff_target || 'none'}</div>
            </section>
          </aside>
        </div>
      </div>
    `;
  </script>
</body>
</html>"""


def write_vectorfl_page_semi_live_organ_detail_set(
    repo_root: Path,
    *,
    output_dir: Path | None = None,
) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell" / "semi_live_organ_detail")
    root.mkdir(parents=True, exist_ok=True)

    outputs = []
    for detail_kind in DETAIL_KEYS:
        data = build_vectorfl_page_semi_live_organ_detail_state(repo_root, detail_kind=detail_kind)
        html = render_vectorfl_page_semi_live_organ_detail_html(data)
        html_path = root / f"{detail_kind}.html"
        json_path = root / f"{detail_kind}.json"
        html_path.write_text(html, encoding="utf-8")
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append(
            {
                "detail_kind": detail_kind,
                "html_path": str(html_path),
                "json_path": str(json_path),
            }
        )

    return {"output_dir": str(root), "outputs": outputs}
