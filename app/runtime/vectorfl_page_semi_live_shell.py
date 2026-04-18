from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json

from app.runtime.vectorfl_page_app_shell import write_vectorfl_page_app_shell_set
from app.runtime.vectorfl_page_unified_mock import build_vectorfl_page_unified_mock_data
from app.runtime.saved_connections import load_saved_connections


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def build_vectorfl_page_semi_live_state(repo_root: Path) -> Dict[str, Any]:
    base = build_vectorfl_page_unified_mock_data(repo_root)
    current_phase = _read_json(repo_root / "runtime" / "current_phase.json")
    preflight = _read_json(repo_root / "runtime" / "preflight_last_decision.json")
    engine_index = _read_json(repo_root / "runtime" / "views" / "engine_state_latest" / "index.json")
    update_events = _read_json(repo_root / "runtime" / "views" / "engine_state_update_events" / "index.json")
    attention_memory = _read_json(repo_root / "runtime" / "views" / "state_attention_memory" / "index.json")
    reconstruction = _read_json(repo_root / "runtime" / "views" / "reconstruction_supervisor" / "index.json")
    saved_connections = load_saved_connections(repo_root / "runtime")

    items: List[Dict[str, Any]] = engine_index.get("items") or []
    top_item = items[0] if items else {}
    top_asset_id = str(top_item.get("asset_id") or "").strip()

    case_header = (base.get("current_reading") or {}).get("case_header") or {}
    body = (base.get("current_reading") or {}).get("body") or {}
    governance = (base.get("current_reading") or {}).get("governance") or {}
    queue_preview = base.get("queue_preview") or []
    history_trace = base.get("history_trace_preview") or {}
    intake = base.get("inputs_preview") or {}

    phase_name = current_phase.get("phase") or "unknown_phase"
    decision_reason = current_phase.get("decision_reason") or "no decision reason"
    reading_frame = current_phase.get("reading_frame") or "no reading frame"
    next_check = current_phase.get("next_check_trigger") or governance.get("next_check_trigger")
    latent_lines = current_phase.get("active_latent_lines") or []
    signals = current_phase.get("signals") or {}
    drift_risks = preflight.get("drift_risks") or []
    guard_actions = preflight.get("guard_actions") or []
    why_selected = preflight.get("why_selected") or ""
    selected_group = (preflight.get("selected_artifact_group") or {}).get("group_id") or "unknown_group"
    connection_rows = [row for row in saved_connections if str(row.get("source_asset") or "").strip() == top_asset_id][:3]
    update_rows = [row for row in (update_events.get("items") or []) if str(row.get("asset_id") or "").strip() == top_asset_id][:3]
    attention_rows = [row for row in (attention_memory.get("items") or []) if str(row.get("asset_id") or "").strip() == top_asset_id][:1]
    reconstruction_rows = [row for row in (reconstruction.get("items") or []) if str(row.get("scope_ref") or "").strip() == top_asset_id][:2]

    if top_item:
        case_header["case_id"] = f"semi_live:{top_item.get('asset_id') or 'runtime'}"
        case_header["case_kind"] = "runtime_surface_case"
        case_header["case_status"] = current_phase.get("status") or "active"
        case_header["updated_at"] = top_item.get("updated_at") or current_phase.get("last_updated")
        body["headline"] = f"{top_item.get('asset_name') or top_item.get('asset_id') or 'runtime asset'} / {phase_name}"
        body["summary_body_text"] = (
            f"Runtime currently reads this surface through phase `{phase_name}`. "
            f"Decision reason: {decision_reason}. "
            f"Reading frame: {reading_frame}."
        )
        body["supporting_unit_refs"] = [
            f"runtime_phase:{current_phase.get('phase_source_turn') or 'unknown'}",
            f"runtime_preflight:{preflight.get('preflight_id') or 'unknown'}",
            f"runtime_asset:{top_item.get('asset_id') or 'unknown'}",
        ]

    base["page_title"] = "VectorFL Page / Semi-Live Shell"
    base["scenario"] = {
        "name": "semi_live_runtime_bridge",
        "intent": "Translate current runtime phase and engine state into current-reading-first shell without losing VectorFL semantics.",
        "status": current_phase.get("status") or "runtime_unknown",
    }
    base["current_responsibility"] = {
        **(base.get("current_responsibility") or {}),
        "placement_reason": (
            f"Current runtime phase is `{phase_name}` with decision `{current_phase.get('decision') or 'unknown'}`. "
            f"Latent lines: {', '.join(latent_lines) if latent_lines else 'none'}."
        ),
        "restriction_flags": governance.get("restriction_flags") or [
            "observer_only",
            "promotion_forbidden",
        ],
    }
    base["progression_preview"] = {
        "previous_step": {
            "organ_ref": "organ:runtime_preflight",
            "summary": why_selected or "preflight selection rationale unavailable",
        },
        "current_step": {
            "organ_ref": "organ:flow_interpretation",
            "summary": decision_reason,
        },
        "next_candidates": [
            {
                "organ_ref": "organ:governance",
                "lane_ref": current_phase.get("decision") or "unknown_lane",
                "status": "preferred_candidate",
                "detail_entry_target": "organ_detail:governance",
            }
        ],
    }

    def _saved_count(asset_id: str) -> int:
        return sum(1 for row in saved_connections if str(row.get("source_asset") or "").strip() == asset_id)

    def _attention_summary(asset_id: str) -> Dict[str, Any]:
        for row in (attention_memory.get("items") or []):
            if str(row.get("asset_id") or "").strip() == asset_id:
                return row
        return {}

    def _update_summary(asset_id: str) -> Dict[str, Any]:
        for row in (update_events.get("items") or []):
            if str(row.get("asset_id") or "").strip() == asset_id:
                return row
        return {}

    if items:
        queue_preview = []
        for item in items[:5]:
            asset_id = str(item.get("asset_id") or "").strip()
            attention_row = _attention_summary(asset_id)
            update_row = _update_summary(asset_id)
            queue_preview.append(
                {
                    "case_id": f"semi_live:{asset_id or 'runtime'}",
                    "case_kind": "runtime_surface_case",
                    "case_status": current_phase.get("status") or "active",
                    "current_organ_ref": "organ:flow_interpretation",
                    "lane_kind": current_phase.get("decision") or "unknown_lane",
                    "lane_status": current_phase.get("status") or "unknown_status",
                    "placement_reason_short": f"{item.get('asset_name') or item.get('asset_id') or 'runtime asset'} is being held under {phase_name} reading.",
                    "hold_state": governance.get("hold_state") or "mixed_hold",
                    "restriction_flags": governance.get("restriction_flags") or ["observer_only"],
                    "preferred_next_candidate": "organ:governance",
                    "held_candidate_exists": True,
                    "headline": f"{item.get('asset_name') or item.get('asset_id')} / maturation={item.get('maturation_state') or 'unknown'} / trace={item.get('traceability_status') or 'unknown'}",
                    "linked_program_refs": base.get("programs_connections_preview", {}).get("linked_programs") or [],
                    "updated_at": item.get("updated_at") or current_phase.get("last_updated"),
                    "saved_connection_count": _saved_count(asset_id),
                    "attention_flag": bool(attention_row.get("active_attention_count")),
                    "attention_pattern_summary": attention_row.get("attention_pattern_summary"),
                    "recent_update_reason": update_row.get("update_reason"),
                }
            )
    base["queue_preview"] = queue_preview

    base["current_reading"]["case_header"] = case_header
    base["current_reading"]["body"] = body
    base["current_reading"]["lane"] = {
        "lane_kind": current_phase.get("decision") or "unknown_lane",
        "lane_status": current_phase.get("status") or "unknown_status",
        "next_hop_candidates": current_phase.get("related_candidate_ids") or [],
    }
    base["current_reading"]["governance"] = {
        "hold_state": governance.get("hold_state") or "mixed_hold",
        "restriction_flags": governance.get("restriction_flags") or ["observer_only", "promotion_forbidden"],
        "reason_summary": decision_reason,
        "release_condition": "Re-evaluate after next runtime refresh and preflight guard recheck.",
        "next_check_trigger": next_check,
    }
    base["current_reading"]["trace_preview"] = [
        {
            "trace_id": preflight.get("preflight_id") or "trace:runtime_preflight",
            "trace_kind": "runtime_preflight_reason",
            "summary": why_selected or "no why_selected",
            "residue_note": selected_group,
            "reentry_hint": ", ".join(guard_actions[:2]) if guard_actions else "no guard actions",
            "created_at": preflight.get("selected_at") or current_phase.get("last_updated"),
        },
        {
            "trace_id": "trace:runtime_phase_signals",
            "trace_kind": "runtime_phase_signal",
            "summary": f"signals={signals}",
            "residue_note": ", ".join(latent_lines) if latent_lines else "no latent lines",
            "reentry_hint": next_check or "no next check trigger",
            "created_at": current_phase.get("last_updated"),
        },
    ]
    base["inputs_preview"] = {
        **intake,
        "source_id": selected_group,
        "source_kind": "runtime_selected_artifact_group",
        "source_family": "runtime_bridge",
        "source_subgroup": current_phase.get("phase") or "unknown_phase",
        "matched_context_layers": [
            f"runtime:phase={phase_name}",
            f"runtime:mode={preflight.get('selected_mode') or 'unknown'}",
            f"runtime:group={selected_group}",
        ],
        "intake_classification": "runtime_surface_bridge",
        "next_lane_hint": current_phase.get("decision") or "unknown_lane",
        "weakness_note": "Semi-live bridge uses runtime summary surfaces rather than canonical case packets.",
        "fallback_used": True,
        "readiness_level": "usable_with_caution",
        "re_read_needed": True,
        "selected_artifact_refs": (preflight.get("selected_artifact_group") or {}).get("selected_artifacts") or [],
        "artifact_roots": (preflight.get("selected_artifact_group") or {}).get("artifact_roots") or [],
        "first_read_ref": (current_phase.get("notes") or {}).get("first_read_ref"),
        "requested_artifact_ref": (current_phase.get("notes") or {}).get("requested_artifact_ref"),
        "phase_source_turn": current_phase.get("phase_source_turn"),
        "mode_source": preflight.get("mode_source"),
    }
    base["history_trace_preview"] = {
        "latest_trace_list": base["current_reading"]["trace_preview"],
        "decision_trace_anchor": preflight.get("preflight_id"),
        "residue_emphasis": drift_risks[:3],
        "reentry_cues": guard_actions[:3],
    }
    base["programs_connections_preview"] = {
        **(base.get("programs_connections_preview") or {}),
        "linked_programs": ["program:runtime_bridge"],
        "connection_state": "read_runtime_surfaces_only",
        "action_request_preview": "Semi-live shell is read-only; runtime surfaces are translated into current-reading without live control.",
        "governance_restriction_summary": base["current_reading"]["governance"]["restriction_flags"],
        "saved_connection_preview": [
            {
                "id": row.get("id"),
                "relation_summary": row.get("relation_summary"),
                "value_label": row.get("value_label"),
                "source_pointer": row.get("value_source_pointer") or row.get("object_source_pointer"),
            }
            for row in connection_rows
        ],
        "update_event_preview": [
            {
                "asset_id": row.get("asset_id"),
                "update_reason": row.get("update_reason"),
                "trigger_type": row.get("update_trigger_type"),
                "updated_at": row.get("updated_at"),
            }
            for row in update_rows
        ],
        "attention_memory_preview": [
            {
                "asset_id": row.get("asset_id"),
                "attention_pattern_summary": row.get("attention_pattern_summary"),
                "active_attention_count": row.get("active_attention_count"),
                "dominant_attention_reasons": row.get("dominant_attention_reasons"),
            }
            for row in attention_rows
        ],
        "reconstruction_preview": [
            {
                "reconstruction_id": row.get("reconstruction_id"),
                "scope_ref": row.get("scope_ref"),
                "read_mode": (row.get("surface_summary") or {}).get("read_mode"),
                "linked_view_count": (row.get("surface_summary") or {}).get("linked_view_count"),
            }
            for row in reconstruction_rows
        ],
    }
    current_detail = ((base.get("organ_detail_panels") or {}).get("current") or {})
    if current_detail:
        current_detail["semi_live_status"] = {
            "phase": phase_name,
            "decision": current_phase.get("decision"),
            "restriction_flags": base["current_reading"]["governance"]["restriction_flags"],
            "candidate_count": len(base.get("progression_preview", {}).get("next_candidates") or []),
            "recent_trace_ids": [
                item.get("trace_id")
                for item in base["current_reading"]["trace_preview"]
                if item.get("trace_id")
            ],
        }
        base["organ_detail_panels"]["current"] = current_detail
    governance_detail = ((base.get("organ_detail_panels") or {}).get("governance_candidate") or {})
    if governance_detail:
        governance_detail["semi_live_status"] = {
            "phase": phase_name,
            "decision_reason": decision_reason,
            "release_condition": base["current_reading"]["governance"]["release_condition"],
            "next_check_trigger": base["current_reading"]["governance"]["next_check_trigger"],
        }
        base["organ_detail_panels"]["governance_candidate"] = governance_detail
    return base


def _render_simple_html(data: Dict[str, Any]) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>VectorFL Page / Semi-Live</title>
<style>
:root{--bg:#f3f5f7;--panel:#fcfcfd;--panel-soft:#f7f8fa;--line:#d7dde4;--ink:#111827;--muted:#667085;--chip:#eef2f6}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink)}
.page{max-width:1500px;margin:0 auto;padding:16px;display:grid;gap:12px}
.panel{background:var(--panel);border:1px solid var(--line);padding:14px}
.grid{display:grid;grid-template-columns:260px minmax(0,1fr) 320px;gap:16px;align-items:start}
.stack{display:grid;gap:10px}.card{background:#fcfcfd;border:1px solid var(--line);padding:10px;display:grid;gap:6px}
.kicker,.label{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}h1,h2,h3{margin:0;color:var(--ink)}h1{font-size:18px;font-weight:700}h2{font-size:15px;font-weight:600}h3{font-size:14px;font-weight:600}.meta{color:var(--muted);font-size:13px;line-height:1.5}.chip{display:inline-flex;background:var(--chip);border:1px solid var(--line);border-radius:999px;padding:4px 8px;font-size:11px;margin:0 6px 6px 0}.body-copy{line-height:1.65;white-space:pre-wrap;font-size:13px}.nav{display:block;background:#fcfcfd;border:1px solid var(--line);padding:10px 12px;margin-bottom:8px}
</style></head><body>
<script id="vectorfl-page-semi-live-data" type="application/json">""" + payload + """</script>
<div id="app"></div>
<script>
const data=JSON.parse(document.getElementById('vectorfl-page-semi-live-data').textContent);
const app=document.getElementById('app');
const nav=(data.navigation_items||[]).map(item=>`<a class="nav" href="#"><strong>${item.label}</strong><div class="meta">${item.active ? 'active' : 'support'}</div></a>`).join('');
const queue=(data.queue_preview||[]).map(item=>`<div class="card"><strong>${item.headline||item.case_id}</strong><div class="meta">${item.case_id}</div><div class="body-copy">${item.placement_reason_short||''}</div><div class="meta">saved=${item.saved_connection_count||0} / attention=${item.attention_flag ? 'yes' : 'no'} / update=${item.recent_update_reason||'none'}</div></div>`).join('');
const traces=((data.current_reading||{}).trace_preview||[]).map(item=>`<div class="card"><div class="label">${item.trace_kind||'trace'}</div><strong>${item.summary||''}</strong><div class="meta">${item.residue_note||''}</div><div class="body-copy">${Array.isArray(item.reentry_hint) ? item.reentry_hint.join(' / ') : (item.reentry_hint||'')}</div></div>`).join('');
const programs=data.programs_connections_preview||{};
const currentDetail=((data.organ_detail_panels||{}).current||{});
const currentDetailStatus=currentDetail.semi_live_status||{};
const govDetail=((data.organ_detail_panels||{}).governance_candidate||{});
const govDetailStatus=govDetail.semi_live_status||{};
const savedConnections=(programs.saved_connection_preview||[]).map(item=>`<div class="card"><strong>${item.value_label||item.id||'saved connection'}</strong><div class="body-copy">${item.relation_summary||''}</div><div class="meta">${item.source_pointer||''}</div></div>`).join('');
const updateEvents=(programs.update_event_preview||[]).map(item=>`<div class="card"><strong>${item.update_reason||'runtime update'}</strong><div class="meta">trigger=${item.trigger_type||'unknown'} / updated=${item.updated_at||'unknown'}</div></div>`).join('');
const attention=(programs.attention_memory_preview||[]).map(item=>`<div class="card"><strong>${item.attention_pattern_summary||'attention pattern'}</strong><div class="meta">active=${item.active_attention_count||0}</div><div class="body-copy">${(item.dominant_attention_reasons||[]).join(' / ')}</div></div>`).join('');
const recon=(programs.reconstruction_preview||[]).map(item=>`<div class="card"><strong>${item.reconstruction_id||'reconstruction'}</strong><div class="meta">scope=${item.scope_ref||'unknown'} / views=${item.linked_view_count||0}</div><div class="body-copy">${item.read_mode||''}</div></div>`).join('');
app.innerHTML=`<div class="page">
  <section class="panel"><div class="kicker">VectorFL Page / Semi-Live Shell</div><h1>${data.page_title||'VectorFL Page / Semi-Live'}</h1><div class="meta">runtime-driven current-reading bridge / read-only translation of current runtime surfaces</div></section>
  <div class="grid">
    <aside class="panel stack"><div class="kicker">Navigation</div>${nav}<div class="card"><div class="label">Runtime Context</div><div class="meta">${(data.scenario||{}).intent||''}</div></div></aside>
    <main class="stack">
      <section class="panel"><div class="kicker">Current Reading</div><h2>${((data.current_reading||{}).body||{}).headline||'Current Reading'}</h2><div class="body-copy">${((data.current_reading||{}).body||{}).summary_body_text||''}</div></section>
      <section class="panel"><div class="kicker">Current Responsibility</div><strong>${(data.current_responsibility||{}).current_organ_ref||'unknown organ'}</strong><div class="body-copy">${(data.current_responsibility||{}).placement_reason||''}</div></section>
      <section class="panel"><div class="kicker">Cases / Queue</div><div class="stack">${queue}</div></section>
    </main>
    <aside class="stack">
      <section class="panel"><div class="kicker">Governance</div><div class="body-copy">${((data.current_reading||{}).governance||{}).reason_summary||''}</div><div class="meta">next_check=${((data.current_reading||{}).governance||{}).next_check_trigger||'none'}</div></section>
      <section class="panel"><div class="kicker">History / Trace</div><div class="stack">${traces}</div></section>
      <section class="panel"><div class="kicker">Programs / Connections</div><div class="body-copy">${programs.action_request_preview||''}</div><div class="meta">state=${programs.connection_state||'unknown'} / linked=${(programs.linked_programs||[]).join(', ')||'none'}</div><div class="stack">${savedConnections||''}${updateEvents||''}${attention||''}${recon||''}</div></section>
      <section class="panel"><div class="kicker">Current Organ Detail Status</div><div class="meta">phase=${currentDetailStatus.phase||'unknown'} / decision=${currentDetailStatus.decision||'unknown'} / candidates=${currentDetailStatus.candidate_count||0}</div><div class="body-copy">${(currentDetailStatus.restriction_flags||[]).join(' / ')}</div><div class="meta">traces=${(currentDetailStatus.recent_trace_ids||[]).join(', ')||'none'}</div></section>
      <section class="panel"><div class="kicker">Governance Organ Detail Status</div><div class="body-copy">${govDetailStatus.decision_reason||''}</div><div class="meta">release=${govDetailStatus.release_condition||'none'}</div><div class="meta">next_check=${govDetailStatus.next_check_trigger||'none'}</div></section>
    </aside>
  </div>
</div>`; 
</script></body></html>"""


def write_vectorfl_page_semi_live_shell(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, str]:
    data = build_vectorfl_page_semi_live_state(repo_root)
    html = _render_simple_html(data)
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell" / "semi_live")
    root.mkdir(parents=True, exist_ok=True)
    html_path = root / "current-reading.html"
    json_path = root / "current-reading.json"
    html_path.write_text(html, encoding="utf-8")
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"html_path": str(html_path), "json_path": str(json_path)}
