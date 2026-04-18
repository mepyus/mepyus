from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json

from app.runtime.vectorfl_page_app_shell import (
    PRIMARY_SURFACES,
    render_vectorfl_page_app_shell_html,
)
from app.runtime.vectorfl_page_route_aware_mock import NAV_KEY_BY_SURFACE
from app.runtime.vectorfl_page_semi_live_shell import build_vectorfl_page_semi_live_state
from app.runtime.vectorfl_page_semi_live_trace_detail import _slugify_trace_id


def _with_active_navigation(items: List[Dict[str, Any]], active_nav_key: str) -> List[Dict[str, Any]]:
    result: List[Dict[str, Any]] = []
    for item in items:
        copied = dict(item)
        copied["active"] = copied.get("key") == active_nav_key
        result.append(copied)
    return result


def build_vectorfl_page_semi_live_route_state(repo_root: Path, *, active_surface: str) -> Dict[str, Any]:
    if active_surface not in PRIMARY_SURFACES:
        raise ValueError(f"Unsupported primary surface: {active_surface}")

    data = build_vectorfl_page_semi_live_state(repo_root)
    active_nav_key = NAV_KEY_BY_SURFACE[active_surface]
    data["page_title"] = f"VectorFL Page / Semi-Live / {active_surface}"
    data["active_primary_surface"] = active_surface
    data["navigation_items"] = _with_active_navigation(data.get("navigation_items") or [], active_nav_key)
    contextual_link_map = {
        "organ_detail:input": "../semi_live_organ_detail/input.html",
        "organ_detail:flow_interpretation": "../semi_live_organ_detail/current.html",
        "organ_detail:governance": "../semi_live_organ_detail/governance.html",
    }
    data["route_state_preview"] = {
        "active_primary_surface": active_surface,
        "active_nav_key": active_nav_key,
        "active_contextual_panel": "organ_detail_input" if active_surface == "inputs-intake" else "organ_detail_current",
        "contextual_entry_targets": [
            "organ_detail:input",
            "organ_detail:flow_interpretation",
            "organ_detail:governance",
        ],
        "contextual_link_map": contextual_link_map,
        "breadcrumb_chain": [
            "VectorFL Page",
            "semi-live",
            active_surface,
        ],
        "route_note": "Semi-live runtime bridge is active; current-reading remains the semantic center even when another surface is primary.",
    }
    responsibility = data.get("current_responsibility") or {}
    if responsibility:
        responsibility["detail_href"] = contextual_link_map["organ_detail:flow_interpretation"]
        data["current_responsibility"] = responsibility

    progression = data.get("progression_preview") or {}
    next_candidates = progression.get("next_candidates") or []
    for item in next_candidates:
        target = item.get("detail_entry_target")
        if target in contextual_link_map:
            item["detail_href"] = contextual_link_map[target]
    progression["next_candidates"] = next_candidates
    data["progression_preview"] = progression

    queue_preview = data.get("queue_preview") or []
    for item in queue_preview:
        item["detail_href"] = contextual_link_map["organ_detail:flow_interpretation"]
        item["next_detail_href"] = contextual_link_map["organ_detail:governance"]
    data["queue_preview"] = queue_preview
    if active_surface == "inputs-intake":
        inputs_preview = data.get("inputs_preview") or {}
        inputs_preview["detail_href"] = contextual_link_map["organ_detail:input"]
        inputs_preview["current_reading_href"] = "current-reading.html"
        data["inputs_preview"] = inputs_preview
    history_preview = data.get("history_trace_preview") or {}
    latest_trace_list = history_preview.get("latest_trace_list") or []
    for item in latest_trace_list:
        trace_id = item.get("trace_id") or "trace-unknown"
        item["detail_href"] = f"../semi_live_trace_detail/{_slugify_trace_id(trace_id)}.html"
    history_preview["latest_trace_list"] = latest_trace_list
    data["history_trace_preview"] = history_preview
    programs_preview = data.get("programs_connections_preview") or {}
    for item in programs_preview.get("saved_connection_preview") or []:
        item_id = item.get("id") or "connection"
        item["detail_href"] = f"../semi_live_program_detail/saved-connection-{item_id.replace(':', '-').replace('/', '-').replace(' ', '-')}.html"
    for item in programs_preview.get("attention_memory_preview") or []:
        asset_id = item.get("asset_id") or "attention"
        item["detail_href"] = f"../semi_live_program_detail/attention-{asset_id.replace(':', '-').replace('/', '-').replace(' ', '-')}.html"
    data["programs_connections_preview"] = programs_preview
    data["shell_runtime"] = {
        "kind": "vectorfl_page_semi_live_shell",
        "active_surface": active_surface,
        "surface_links": {
            surface: f"{surface}.html"
            for surface in PRIMARY_SURFACES
        },
        "index_href": "index.html",
    }
    return data


def write_vectorfl_page_semi_live_route_set(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, object]:
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_page_shell" / "semi_live_routes")
    root.mkdir(parents=True, exist_ok=True)

    routes: List[Dict[str, str]] = []
    for surface in PRIMARY_SURFACES:
        data = build_vectorfl_page_semi_live_route_state(repo_root, active_surface=surface)
        html = render_vectorfl_page_app_shell_html(data)
        html_path = root / f"{surface}.html"
        json_path = root / f"{surface}.json"
        html_path.write_text(html, encoding="utf-8")
        json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        routes.append(
            {
                "surface": surface,
                "html_path": str(html_path),
                "json_path": str(json_path),
            }
        )

    index_path = root / "index.html"
    index_html = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>VectorFL Page / Semi-Live Routes</title>
<style>:root{--bg:#f3f5f7;--panel:#fcfcfd;--line:#d7dde4;--ink:#111827;--muted:#667085}*{box-sizing:border-box}body{font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:var(--bg);margin:0;color:var(--ink)}.page{max-width:1080px;margin:0 auto;padding:16px;display:grid;gap:12px}.panel{background:var(--panel);border:1px solid var(--line);padding:14px;display:grid;gap:12px}.card{background:#fcfcfd;border-bottom:1px solid var(--line);padding:12px 14px;display:grid;gap:6px}.card:last-child{border-bottom:0}.grid{display:grid;gap:0;border:1px solid var(--line);background:#fcfcfd}a{color:inherit;text-decoration:none}.meta{color:var(--muted);font-size:13px;line-height:1.5}.kicker{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--muted)}.section-head{display:flex;align-items:end;justify-content:space-between;gap:12px}h1,h2{margin:0;color:var(--ink)}h1{font-size:18px;font-weight:700}h2{font-size:14px;font-weight:600}</style>
</head><body><div class="page"><section class="panel"><div class="kicker">VectorFL Page / Semi-Live Route Set</div><h1>Semi-Live Primary Surfaces</h1><div class="meta">All primary surfaces are runtime-bridged while keeping current-reading-first semantics.</div></section><section class="panel grid">""" + "".join(
        f"""<div class="card"><div class="section-head"><h2>{surface}</h2><div class="mono">semi-live</div></div><div><a href="{surface}.html">HTML View</a></div><div><a href="{surface}.json">JSON Payload</a></div></div>"""
        for surface in PRIMARY_SURFACES
    ) + """</section></div></body></html>"""
    index_path.write_text(index_html, encoding="utf-8")

    return {
        "output_dir": str(root),
        "index_path": str(index_path),
        "routes": routes,
    }
