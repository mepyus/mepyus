from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from app.runtime.process_console_history_loader import (
    load_engine_state_history,
    load_engine_state_update_event,
)
from app.runtime.process_console_history_selectors import build_history_timeline
from app.runtime.process_console_state_loader import (
    load_engine_state_items,
    load_engine_state_latest,
)


def build_operating_ui_history_shell_data(
    runtime_root: Path,
    *,
    asset_id: Optional[str] = None,
    sort_by: str = "updated_at",
) -> Dict[str, Any]:
    snapshots = _build_run_snapshot_vms(runtime_root, sort_by=sort_by)
    selected_asset_id = asset_id or (snapshots[0]["asset_id"] if snapshots else None)
    latest = load_engine_state_latest(runtime_root, selected_asset_id)
    history_rows = load_engine_state_history(runtime_root, selected_asset_id)
    update_event = load_engine_state_update_event(runtime_root, selected_asset_id)
    timeline = build_history_timeline(history_rows, recent_limit=8)
    clusters = _build_activity_cluster_vms(latest=latest, timeline=timeline, update_event=update_event)
    selected_cluster_id = clusters[0]["cluster_id"] if clusters else None
    trace_entries = _build_trace_entry_vms(clusters)
    replay_preview = _build_replayable_state_vm(latest=latest, clusters=clusters)
    phase1_href = "/operating-ui-phase1"
    if selected_asset_id:
        phase1_href += f"?asset_id={selected_asset_id}"

    return {
        "page_title": "history companion",
        "state": _surface_state(snapshots=snapshots, selected_asset_id=selected_asset_id, clusters=clusters),
        "selected_asset_id": selected_asset_id,
        "recent_snapshots": snapshots,
        "selected_cluster_id": selected_cluster_id,
        "activity_clusters": clusters,
        "trace_entries": trace_entries,
        "replayable_state": replay_preview,
        "phase1_href": phase1_href,
        "availability": {
            "recent_runs": "live" if snapshots else "unavailable",
            "activity_clusters": "live" if clusters else ("degraded" if selected_asset_id else "unavailable"),
            "trace_panel": "live" if trace_entries else ("degraded" if selected_asset_id else "unavailable"),
            "replay_preview": "live" if replay_preview.get("state") == "available" else "degraded",
        },
        "notes": {
            "recent_runs": "recent run snapshots translated from latest operating state",
            "activity_clusters": (
                "translated time-axis clusters from history lineage"
                if history_rows
                else "history sparse / latest-linked cluster only"
            ),
            "trace_panel": (
                "trace is rendered as operator-facing reading units, not raw logs"
            ),
            "replay_preview": (
                "reread preview is a prior state slice only / no rerun semantics"
            ),
        },
        "source_summary": {
            "recent_runs": "runtime latest snapshots",
            "activity_clusters": "history lineage + optional update-event assist",
            "trace_panel": "translated history trace units",
            "replay_preview": "canonical snapshot reread",
        },
    }


def render_operating_ui_history_shell_html(
    data: Dict[str, Any],
    *,
    api_path: str = "/api/operating-ui-history",
) -> str:
    payload = json.dumps(data, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{data.get("page_title") or "history companion"}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f5f1e8;
      --panel: #fffaf2;
      --panel-2: #f1eadb;
      --line: #d6ccb8;
      --ink: #2c251b;
      --muted: #6d6558;
      --accent: #8f4e2b;
      --live: #2a6a47;
      --degraded: #9a6a1d;
      --unavailable: #8a3c31;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      background: linear-gradient(180deg, #efe5d2 0%, var(--bg) 100%);
      color: var(--ink);
    }}
    a {{ color: inherit; }}
    .page {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 24px;
    }}
    .topbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--line);
    }}
    .nav-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }}
    .nav {{
      text-decoration: none;
      border: 1px solid var(--line);
      padding: 8px 12px;
      border-radius: 999px;
      background: rgba(255,255,255,0.5);
    }}
    .hero {{
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 16px;
      margin-bottom: 18px;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 16px;
      box-shadow: 0 10px 30px rgba(71, 51, 26, 0.06);
    }}
    .panel h1, .panel h2, .panel h3 {{ margin: 0 0 8px; }}
    .subhead, .meta, .soft-note {{
      color: var(--muted);
      font-size: 13px;
      line-height: 1.4;
    }}
    .pill-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin: 10px 0;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border-radius: 999px;
      padding: 5px 10px;
      border: 1px solid var(--line);
      font-size: 12px;
      background: #fff;
    }}
    .pill.live {{ border-color: rgba(42,106,71,0.3); color: var(--live); }}
    .pill.degraded {{ border-color: rgba(154,106,29,0.3); color: var(--degraded); }}
    .pill.unavailable {{ border-color: rgba(138,60,49,0.3); color: var(--unavailable); }}
    .layout {{
      display: grid;
      grid-template-columns: 0.85fr 0.95fr 1.2fr 0.95fr;
      gap: 16px;
    }}
    .stack {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 10px;
    }}
    .item {{
      width: 100%;
      text-align: left;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 12px;
      background: #fffdf8;
      cursor: pointer;
    }}
    .item.active {{
      border-color: var(--accent);
      background: #fff3e8;
      box-shadow: inset 0 0 0 1px rgba(143, 78, 43, 0.18);
    }}
    .item strong, .trace-card strong {{
      display: block;
      margin-bottom: 4px;
    }}
    .empty {{
      border: 1px dashed var(--line);
      border-radius: 14px;
      padding: 14px;
      color: var(--muted);
      background: rgba(255,255,255,0.45);
      margin-top: 10px;
    }}
    .trace-card {{
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 12px;
      background: #fffdf7;
      margin-top: 10px;
    }}
    .snapshot-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
      margin-top: 10px;
    }}
    .snapshot-cell {{
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 10px;
      background: #fff;
    }}
    .page-map {{
      display: grid;
      gap: 8px;
      margin-top: 8px;
    }}
    .page-map-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .map-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border-radius: 999px;
      padding: 6px 10px;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      font-size: 12px;
    }}
    .map-chip.companion {{
      background: #faf4ea;
      border-style: dashed;
    }}
    .cta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }}
    .cta {{
      text-decoration: none;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 9px 12px;
      background: #fff;
    }}
    @media (max-width: 1120px) {{
      .hero, .layout {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="topbar">
      <div class="nav-row">
        <a class="nav" href="/operating-ui-live">operating live</a>
        <a class="nav" href="/operating-ui-phase1">main operating set</a>
        <a class="nav" href="/operating-ui-history">history companion</a>
      </div>
      <div class="meta">state={data.get("state") or "unknown"} / api={api_path}</div>
    </div>
    <div class="hero">
      <div class="panel">
        <h1>History / Reread / Trace Companion</h1>
        <div class="subhead">time-axis reading companion</div>
        <div class="pill-row">
          <span class="pill">time-axis companion</span>
          <span class="pill">view-level reread only</span>
        </div>
        <div class="page-map">
          <div class="page-map-row">
            <a class="map-chip" href="/operating-ui-phase1">Operating: observe now</a>
            <a class="map-chip" href="/operating-ui-phase1">Explore: build path</a>
            <a class="map-chip" href="/operating-ui-phase1">Search: direct access</a>
            <a class="map-chip" href="/operating-ui-phase1">Memory: saved paths</a>
            <a class="map-chip" href="/operating-ui-phase1">Similar: local re-query</a>
          </div>
          <div class="page-map-row">
            <span class="map-chip companion">History Companion: time-axis read</span>
          </div>
        </div>
      </div>
      <div class="panel">
        <h3>Main Operating Set Link</h3>
        <div class="subhead">navigation only / historical reference may attach</div>
        <div class="cta-row">
          <a id="phase1-link" class="cta" href="{data.get("phase1_href") or "/operating-ui-phase1"}">Open in Main Operating Set</a>
        </div>
      </div>
    </div>
    <div id="app"></div>
  </div>
  <script id="operating-ui-history-data" type="application/json">{payload}</script>
  <script>
    const embedded = document.getElementById('operating-ui-history-data');
    const shell = embedded ? JSON.parse(embedded.textContent || '{{}}') : {{}};
    let selectedSnapshotId = shell.selected_asset_id || ((shell.recent_snapshots || [])[0] || {{}}).asset_id || null;
    let selectedClusterId = shell.selected_cluster_id || ((shell.activity_clusters || [])[0] || {{}}).cluster_id || null;

    function availabilityPill(label) {{
      const text = String(label || 'unavailable');
      const tone = text.includes('live') ? 'live' : (text.includes('degraded') ? 'degraded' : (text.includes('unavailable') ? 'unavailable' : ''));
      return `<span class="pill ${{tone}}">${{text}}</span>`;
    }}

    function currentSnapshot() {{
      return (shell.recent_snapshots || []).find((item) => item.asset_id === selectedSnapshotId) || null;
    }}

    function currentCluster() {{
      return (shell.activity_clusters || []).find((item) => item.cluster_id === selectedClusterId) || null;
    }}

    function currentTraceEntries() {{
      const cluster = currentCluster();
      if (!cluster) return [];
      return (shell.trace_entries || []).filter((item) => item.cluster_id === cluster.cluster_id);
    }}

    function currentReplayState() {{
      const cluster = currentCluster();
      const replay = shell.replayable_state || {{}};
      if (!cluster || !replay || replay.state !== 'available') return replay;
      return Object.assign({{}}, replay, {{
        title: cluster.replay_title || replay.title,
        snapshot_items: cluster.snapshot_items || replay.snapshot_items || [],
      }});
    }}

    function updatePhase1Link() {{
      const link = document.getElementById('phase1-link');
      if (!link) return;
      const cluster = currentCluster();
      const summary = cluster ? cluster.title : 'prior state slice reference';
      const note = cluster && cluster.summary ? cluster.summary : 'limited by available history source';
      if (!selectedSnapshotId) {{
        link.href = '/operating-ui-phase1';
        return;
      }}
      const url = new URL('/operating-ui-phase1', window.location.origin);
      url.searchParams.set('asset_id', selectedSnapshotId);
      url.searchParams.set('history_snapshot_ref', selectedSnapshotId);
      if (cluster && cluster.cluster_id) url.searchParams.set('history_cluster_ref', cluster.cluster_id);
      url.searchParams.set('history_reread_summary', summary);
      url.searchParams.set('history_source_note', note);
      link.href = url.toString();
    }}

    function renderRecentRuns(column) {{
      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `<h2>Recent Runs / Snapshots</h2><div class="subhead">recent checkpoints</div><div class="pill-row">${{availabilityPill((shell.availability || {{}}).recent_runs)}}<span class="pill">${{(shell.source_summary || {{}}).recent_runs || 'runtime latest snapshots'}}</span></div>`;
      const list = document.createElement('div');
      list.className = 'list';
      (shell.recent_snapshots || []).forEach((item) => {{
        const button = document.createElement('button');
        button.className = 'item' + (item.asset_id === selectedSnapshotId ? ' active' : '');
        button.innerHTML = `<strong>${{item.title}}</strong><div class="meta">${{item.time_hint || item.updated_at || 'unknown'}} / state=${{item.state_label}}</div><div class="soft-note">${{item.summary}}</div><div class="soft-note">${{item.context_hint || ''}}</div>`;
        button.addEventListener('click', () => {{
          const url = new URL(window.location.href);
          url.searchParams.set('asset_id', item.asset_id);
          window.location.href = url.toString();
        }});
        list.appendChild(button);
      }});
      if (!list.children.length) {{
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'no runs yet / source unavailable';
        panel.appendChild(empty);
      }} else {{
        panel.appendChild(list);
      }}
      column.appendChild(panel);
    }}

    function renderActivityClusters(column) {{
      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `<h2>Activity Cluster List</h2><div class="subhead">grouped activity slices</div><div class="pill-row">${{availabilityPill((shell.availability || {{}}).activity_clusters)}}<span class="pill">${{(shell.source_summary || {{}}).activity_clusters || 'history lineage + update assist'}}</span></div>`;
      const list = document.createElement('div');
      list.className = 'list';
      (shell.activity_clusters || []).forEach((item) => {{
        const button = document.createElement('button');
        button.className = 'item' + (item.cluster_id === selectedClusterId ? ' active' : '');
        button.innerHTML = `<strong>${{item.title}}</strong><div class="meta">${{item.order_hint || item.updated_at || 'unknown'}} / ${{item.cluster_tag || 'grouped slice'}}</div><div class="soft-note">${{item.grouping_note || ''}}</div><div class="soft-note">${{item.summary}}</div>`;
        button.addEventListener('click', () => {{
          selectedClusterId = item.cluster_id;
          render();
        }});
        list.appendChild(button);
      }});
      if (!list.children.length) {{
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = selectedSnapshotId ? 'partial trace only / no clusters for this snapshot yet' : 'choose a snapshot first';
        panel.appendChild(empty);
      }} else {{
        panel.appendChild(list);
      }}
      column.appendChild(panel);
    }}

    function renderTracePanel(column) {{
      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `<h2>Trace Reading Panel</h2><div class="subhead">translated trace units</div><div class="pill-row">${{availabilityPill((shell.availability || {{}}).trace_panel)}}<span class="pill">${{(shell.source_summary || {{}}).trace_panel || 'translated history trace units'}}</span></div>`;
      const entries = currentTraceEntries();
      const cluster = currentCluster();
      if (cluster) {{
        panel.innerHTML += `<div class="meta">selected cluster=${{cluster.title}}</div>`;
      }}
      if (!entries.length) {{
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = selectedSnapshotId ? 'trace read unavailable / partial source' : 'select a run snapshot first';
        panel.appendChild(empty);
      }} else {{
        entries.forEach((item) => {{
          const card = document.createElement('div');
          card.className = 'trace-card';
          const orderPrefix = item.order_hint ? (item.order_hint + ' / ') : '';
          card.innerHTML = `<strong>${{item.label}}</strong><div class="meta">${{orderPrefix}}${{item.kind}}</div><div class="soft-note">${{item.summary}}</div>`;
          if (item.honesty_note) {{
            card.innerHTML += `<div class="soft-note">${{item.honesty_note}}</div>`;
          }}
          if (item.badges && item.badges.length) {{
            const row = document.createElement('div');
            row.className = 'pill-row';
            item.badges.forEach((badge) => {{
              row.innerHTML += `<span class="pill">${{badge}}</span>`;
            }});
            card.appendChild(row);
          }}
          panel.appendChild(card);
        }});
      }}
      column.appendChild(panel);
    }}

    function renderReplayPreview(column) {{
      const panel = document.createElement('div');
      panel.className = 'panel';
      panel.innerHTML = `<h2>Rereadable State Preview</h2><div class="subhead">prior state slice only</div><div class="pill-row">${{availabilityPill((shell.availability || {{}}).replay_preview)}}<span class="pill">${{(shell.source_summary || {{}}).replay_preview || 'canonical snapshot reread'}}</span></div>`;
      const replay = currentReplayState();
      if (!replay || replay.state !== 'available') {{
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = selectedSnapshotId ? 'reread preview unavailable / source too sparse' : 'select a run snapshot first';
        panel.appendChild(empty);
      }} else {{
        panel.innerHTML += `<div class="meta">${{replay.title}}</div>`;
        const grid = document.createElement('div');
        grid.className = 'snapshot-grid';
        (replay.snapshot_items || []).forEach((item) => {{
          const cell = document.createElement('div');
          cell.className = 'snapshot-cell';
          cell.innerHTML = `<strong>${{item.label}}</strong><div class="soft-note">${{item.value}}</div>`;
          grid.appendChild(cell);
        }});
        panel.appendChild(grid);
      }}
      const ctas = document.createElement('div');
      ctas.className = 'cta-row';
      const phase1Link = document.createElement('a');
      phase1Link.className = 'cta';
      const cluster = currentCluster();
      const phase1Url = new URL('/operating-ui-phase1', window.location.origin);
      if (selectedSnapshotId) phase1Url.searchParams.set('asset_id', selectedSnapshotId);
      if (selectedSnapshotId) phase1Url.searchParams.set('history_snapshot_ref', selectedSnapshotId);
      if (cluster && cluster.cluster_id) phase1Url.searchParams.set('history_cluster_ref', cluster.cluster_id);
      phase1Url.searchParams.set('history_reread_summary', cluster ? cluster.title : 'prior state slice reference');
      phase1Url.searchParams.set('history_source_note', cluster && cluster.summary ? cluster.summary : 'limited by available history source');
      phase1Link.href = selectedSnapshotId ? phase1Url.toString() : '/operating-ui-phase1';
      phase1Link.textContent = 'Open in Main Operating Set';
      ctas.appendChild(phase1Link);
      panel.appendChild(ctas);
      column.appendChild(panel);
    }}

    function render() {{
      updatePhase1Link();
      const app = document.getElementById('app');
      app.innerHTML = '';
      const layout = document.createElement('div');
      layout.className = 'layout';
      const col1 = document.createElement('div');
      col1.className = 'stack';
      const col2 = document.createElement('div');
      col2.className = 'stack';
      const col3 = document.createElement('div');
      col3.className = 'stack';
      const col4 = document.createElement('div');
      col4.className = 'stack';
      renderRecentRuns(col1);
      renderActivityClusters(col2);
      renderTracePanel(col3);
      renderReplayPreview(col4);
      layout.appendChild(col1);
      layout.appendChild(col2);
      layout.appendChild(col3);
      layout.appendChild(col4);
      app.appendChild(layout);
    }}

    render();
  </script>
</body>
</html>"""


def _surface_state(
    *,
    snapshots: List[Dict[str, Any]],
    selected_asset_id: Optional[str],
    clusters: List[Dict[str, Any]],
) -> str:
    if not snapshots:
        return "source_unavailable"
    if selected_asset_id and not clusters:
        return "partial_trace_only"
    return "loaded"


def _build_run_snapshot_vms(runtime_root: Path, *, sort_by: str) -> List[Dict[str, Any]]:
    items = load_engine_state_items(runtime_root)
    if sort_by == "updated_at":
        items.sort(key=lambda row: str(row.get("updated_at") or ""), reverse=True)
    snapshots: List[Dict[str, Any]] = []
    for row in items[:10]:
        asset_id = str(row.get("asset_id") or "").strip()
        if not asset_id:
            continue
        updated_at = str(row.get("updated_at") or "").strip() or "unknown"
        snapshots.append(
            {
                "asset_id": asset_id,
                "title": _snapshot_title(row),
                "updated_at": updated_at,
                "time_hint": _time_hint(updated_at, recent_rank=len(snapshots)),
                "state_label": str(row.get("maturation_state") or "state unavailable"),
                "summary": _snapshot_summary(row),
                "context_hint": _context_hint(row),
            }
        )
    return snapshots


def _snapshot_summary(row: Dict[str, Any]) -> str:
    packet = str(row.get("packet_texture") or "unknown").replace("_", " ")
    grounding = str(row.get("grounding_status") or "unknown").replace("_", " ")
    traceability = str(row.get("traceability_status") or "unknown").replace("_", " ")
    return f"{packet} / grounded {grounding} / trace {traceability}"


def _build_activity_cluster_vms(
    *,
    latest: Optional[Dict[str, Any]],
    timeline: Dict[str, Any],
    update_event: Optional[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    clusters: List[Dict[str, Any]] = []
    items = timeline.get("items", []) if isinstance(timeline, dict) else []
    if items:
        for index, item in enumerate(items):
            labels = item.get("change_labels") or ["trace_read"]
            cluster_kind = labels[0]
            title = _cluster_title(item)
            updated_at = str(item.get("updated_at") or "").strip() or "unknown"
            summary_parts = [
                _cluster_reason_summary(item),
                _cluster_change_summary(item),
            ]
            if item.get("provenance_only_update"):
                summary_parts.append("partial trace only")
            if update_event:
                summary_parts.append("update assist available")
            clusters.append(
                {
                    "cluster_id": f"cluster-{index}",
                    "title": title,
                    "cluster_kind": cluster_kind,
                    "cluster_tag": _cluster_tag(item),
                    "updated_at": updated_at,
                    "order_hint": _time_hint(updated_at, recent_rank=index),
                    "grouping_note": _grouping_note(item),
                    "summary": " / ".join(summary_parts),
                    "timeline_item": item,
                    "replay_title": f"reread around {title.lower()}",
                    "snapshot_items": _snapshot_items_from_canonical(item.get("canonical_snapshot") or {}),
                }
            )
        return clusters
    if latest:
        updated_at = str(latest.get("updated_at") or "").strip() or "unknown"
        return [
            {
                "cluster_id": "cluster-latest-only",
                "title": "latest-linked reading group",
                "cluster_kind": "partial_trace_only",
                "cluster_tag": "partial trace",
                "updated_at": updated_at,
                "order_hint": _time_hint(updated_at, recent_rank=0),
                "grouping_note": "grouped from the latest readable state",
                "summary": "history sparse / latest-linked read only",
                "timeline_item": None,
                "replay_title": "reread the latest-linked state slice",
                "snapshot_items": _snapshot_items_from_canonical(latest),
            }
        ]
    return []


def _cluster_title(item: Dict[str, Any]) -> str:
    if item.get("provenance_only_update"):
        return "provenance-only slice"
    trigger = _humanize_trigger(item.get("update_trigger_type"))
    labels = item.get("change_labels") or []
    if "grounding_change" in labels:
        return f"{trigger} / grounding shift"
    if "emergence_change" in labels:
        return f"{trigger} / emergence shift"
    if "traceability_change" in labels:
        return f"{trigger} / traceability shift"
    return f"{trigger} / state shift"


def _build_trace_entry_vms(clusters: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    trace_entries: List[Dict[str, Any]] = []
    for cluster in clusters:
        item = cluster.get("timeline_item")
        if not item:
            trace_entries.append(
                {
                    "cluster_id": cluster["cluster_id"],
                    "label": "limited trace view",
                    "kind": "translated read",
                    "summary": "no detailed lineage rows yet / latest-linked read only",
                    "honesty_note": "partial source / partial read",
                    "order_hint": cluster.get("order_hint") or "",
                    "badges": ["partial trace only"],
                }
            )
            continue
        trace_entries.append(
                {
                    "cluster_id": cluster["cluster_id"],
                    "label": "what started it",
                    "kind": "translated read",
                    "summary": f"{_humanize_trigger(item.get('update_trigger_type'))} / {item.get('update_reason') or 'reason unavailable'}",
                    "honesty_note": "",
                "order_hint": cluster.get("order_hint") or "",
                "badges": [str(item.get("trigger_badge") or "unknown")],
            }
        )
        changed_fields = item.get("changed_fields") or []
        trace_entries.append(
                {
                    "cluster_id": cluster["cluster_id"],
                    "label": "what changed",
                    "kind": "translated read",
                    "summary": (
                        _humanize_fields(changed_fields)
                        if changed_fields
                        else "canonical drift not detected / provenance-only read"
                    ),
                    "honesty_note": "limited by available history comparison" if changed_fields else "no stronger change read from current source",
                    "order_hint": cluster.get("order_hint") or "",
                    "badges": list(item.get("change_labels") or []),
                }
            )
        evidence_refs = item.get("evidence_refs") or []
        if evidence_refs:
            trace_entries.append(
                {
                    "cluster_id": cluster["cluster_id"],
                    "label": "supporting evidence",
                    "kind": "translated read",
                    "summary": f"{len(evidence_refs)} linked evidence reference(s) available",
                    "honesty_note": "",
                    "order_hint": cluster.get("order_hint") or "",
                    "badges": ["evidence-linked"],
                }
            )
        notes = str(item.get("state_notes") or "").strip()
        if notes:
            trace_entries.append(
                {
                    "cluster_id": cluster["cluster_id"],
                    "label": "operator note",
                    "kind": "translated read",
                    "summary": notes,
                    "honesty_note": "",
                    "order_hint": cluster.get("order_hint") or "",
                    "badges": ["translated note"],
                }
            )
    return trace_entries


def _build_replayable_state_vm(
    *,
    latest: Optional[Dict[str, Any]],
    clusters: List[Dict[str, Any]],
) -> Dict[str, Any]:
    if clusters:
        first = clusters[0]
        return {
            "state": "available",
            "title": first.get("replay_title") or "rereadable state slice",
            "summary": "prior state slice anchored to the selected activity group",
            "snapshot_items": first.get("snapshot_items") or [],
        }
    if latest:
        return {
            "state": "available",
            "title": "reread the latest-linked state slice",
            "summary": "prior state slice / history depth limited",
            "snapshot_items": _snapshot_items_from_canonical(latest),
        }
    return {
        "state": "unavailable",
        "title": "reread preview unavailable",
        "summary": "no prior state slice from current source",
        "snapshot_items": [],
    }


def _snapshot_items_from_canonical(snapshot: Dict[str, Any]) -> List[Dict[str, str]]:
    fields = [
        ("packet texture", snapshot.get("packet_texture")),
        ("grounding", snapshot.get("grounding_status")),
        ("emergence", snapshot.get("emergence_status")),
        ("maturation", snapshot.get("maturation_state")),
        ("traceability", snapshot.get("traceability_status")),
    ]
    items: List[Dict[str, str]] = []
    for label, value in fields:
        items.append({"label": label, "value": str(value or "unknown")})
    return items


def _snapshot_title(row: Dict[str, Any]) -> str:
    asset_name = str(row.get("asset_name") or row.get("asset_id") or "unknown asset")
    return f"{asset_name} checkpoint"


def _context_hint(row: Dict[str, Any]) -> str:
    asset_id = str(row.get("asset_id") or "").strip() or "unknown asset"
    return f"asset={asset_id}"


def _time_hint(value: str, *, recent_rank: int) -> str:
    parsed = _parse_dt(value)
    prefix = "most recent" if recent_rank == 0 else ("older" if recent_rank > 1 else "recent")
    if not parsed:
        return f"{prefix} / time unavailable"
    now = datetime.now(timezone.utc)
    delta = now - parsed
    hours = int(delta.total_seconds() // 3600)
    if hours < 1:
        relative = "within the last hour"
    elif hours < 24:
        relative = f"{hours}h ago"
    else:
        relative = f"{delta.days}d ago"
    return f"{prefix} / {parsed.strftime('%Y-%m-%d %H:%M UTC')} / {relative}"


def _parse_dt(value: str) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def _cluster_title(item: Dict[str, Any]) -> str:
    if item.get("provenance_only_update"):
        return "provenance-only reading group"
    trigger = _humanize_trigger(item.get("update_trigger_type"))
    labels = item.get("change_labels") or []
    if "grounding_change" in labels:
        return f"{trigger} / grounding shift group"
    if "emergence_change" in labels:
        return f"{trigger} / emergence shift group"
    if "traceability_change" in labels:
        return f"{trigger} / traceability shift group"
    return f"{trigger} / state change group"


def _cluster_tag(item: Dict[str, Any]) -> str:
    if item.get("provenance_only_update"):
        return "provenance slice"
    labels = item.get("change_labels") or []
    if "grounding_change" in labels:
        return "grounding shift"
    if "emergence_change" in labels:
        return "emergence shift"
    if "traceability_change" in labels:
        return "traceability shift"
    return "state shift"


def _cluster_reason_summary(item: Dict[str, Any]) -> str:
    reason = str(item.get("update_reason") or "").strip()
    return reason or "reason unavailable"


def _cluster_change_summary(item: Dict[str, Any]) -> str:
    changed_fields = item.get("changed_fields") or []
    if not changed_fields:
        return "no strong state change read"
    return f"{len(changed_fields)} shift(s) visible"


def _grouping_note(item: Dict[str, Any]) -> str:
    changed_fields = item.get("changed_fields") or []
    if item.get("provenance_only_update"):
        return "grouped from provenance-only movement"
    if changed_fields:
        return "grouped around one visible state-change slice"
    return "grouped from the latest readable slice"


def _humanize_trigger(value: Any) -> str:
    mapping = {
        "runtime_evidence": "runtime evidence",
        "backfill": "backfill",
        "recompute": "recompute",
        "manual_correction": "manual correction",
    }
    text = str(value or "").strip()
    return mapping.get(text, text.replace("_", " ") or "trigger unavailable")


def _humanize_fields(fields: List[str]) -> str:
    return ", ".join(str(field).replace("_", " ") for field in fields)
