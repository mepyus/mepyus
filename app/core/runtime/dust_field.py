from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple
import json

from app.runtime.connection_engine import (
    anchor_is_candidate,
    build_relation_profile,
    edge_color,
    edge_reasons_for_profile,
    edge_type_for_profile,
    normalize_anchor_list,
)
from app.fragment.store import FragmentStore
from app.measurement import MeasurementStore
from app.runtime.file_store import JsonDirectoryStore
from app.runtime.inputter import build_dust_inputs_for_material
from app.runtime.labeler import label_dust_inputs
from app.runtime.operator_ui_state import compact_payload


def build_dust_field_data(runtime_root: Path) -> Dict[str, object]:
    fragment_store = FragmentStore(runtime_root)
    measurement_store = MeasurementStore(runtime_root)
    material_store = JsonDirectoryStore(runtime_root / "core" / "materials")
    trace_store = JsonDirectoryStore(runtime_root / "core" / "traces")
    pressure_store = JsonDirectoryStore(runtime_root / "core" / "pressure_profiles")
    seed_store = JsonDirectoryStore(runtime_root / "core" / "point_seeds")
    fragments = sorted(fragment_store.read_all(), key=lambda row: row.created_at)
    materials = sorted(material_store.read_all(), key=lambda row: row.get("created_at", ""))
    traces = trace_store.read_all()
    pressures = pressure_store.read_all()
    seeds = seed_store.read_all()

    dust_nodes: List[Dict[str, object]] = []
    dust_by_id: Dict[str, Dict[str, object]] = {}
    origin_groups: Dict[str, List[str]] = defaultdict(list)
    measurement_summary = _measurement_summary_by_fragment(measurement_store)

    if fragments:
        grouped_fragments: Dict[str, List[object]] = defaultdict(list)
        for fragment in fragments:
            grouped_fragments[fragment.source_id].append(fragment)
        for source_id, group in grouped_fragments.items():
            ordered = sorted(
                group,
                key=lambda row: (
                    row.source_range.start if row.source_range.start is not None else -1,
                    row.fragment_id,
                ),
            )
            sibling_ids = [fragment.fragment_id for fragment in ordered]
            for fragment in ordered:
                node = _fragment_to_dust_node(fragment, sibling_ids, measurement_summary.get(fragment.fragment_id, {"count": 0, "types": []}))
                dust_nodes.append(node)
                dust_by_id[node["dust_id"]] = node
                origin_groups[node["origin_id"]].append(node["dust_id"])
        fragment_source_refs = {node.get("source_ref", "") for node in dust_nodes if node.get("source_ref")}
        material_groups: Dict[str, List[dict]] = defaultdict(list)
        for material in materials:
            source_ref = str(material.get("source_ref", "")).strip()
            metadata = dict(material.get("metadata", {}))
            if not source_ref or source_ref in fragment_source_refs:
                continue
            if "scene" not in metadata or "flow" not in metadata:
                continue
            material_groups[source_ref].append(material)
        for source_ref, group in material_groups.items():
            sibling_ids = [
                str((row.get("metadata") or {}).get("dust_input_id", "")).strip() or str(row.get("material_id", "")).strip()
                for row in group
            ]
            for material in group:
                node = _material_to_dust_node(material, sibling_ids)
                dust_nodes.append(node)
                dust_by_id[node["dust_id"]] = node
                origin_groups[node["origin_id"]].append(node["dust_id"])
    else:
        for material in materials:
            dust_inputs = build_dust_inputs_for_material(material)
            if not dust_inputs:
                continue
            for labeled in label_dust_inputs(dust_inputs):
                node = labeled.to_record()
                dust_nodes.append(node)
                dust_by_id[node["dust_id"]] = node
                origin_groups[node["origin_id"]].append(node["dust_id"])

    origin_preview = {
        origin_id: [dust_by_id[dust_id]["text"] for dust_id in dust_ids[:3]]
        for origin_id, dust_ids in origin_groups.items()
    }
    relation_lookup = _build_relation_lookup(traces, pressures, seeds, origin_preview)
    for node in dust_nodes:
        node["engine_relations"] = relation_lookup.get(
            node.get("projection_origin_id", node["origin_id"]),
            {"traces": [], "pressures": [], "seeds": []},
        )

    edges = _build_connection_edges(dust_nodes, dust_by_id)
    summary = _build_summary(materials, dust_nodes, edges)

    return {
        "summary": summary,
        "compact_summary": _build_dust_compact_summary(dust_nodes, edges),
        "filters": {
            "edge_types": ["direct", "weak", "tension"],
            "scenes": sorted({node["scene"] for node in dust_nodes}),
            "anchors": _top_anchor_values(dust_nodes),
            "observer_roles": sorted({node.get("observer_role", "") for node in dust_nodes if node.get("observer_role")}),
            "observer_signals": sorted(
                {signal for node in dust_nodes for signal in (node.get("observer_signals", []) or []) if signal}
            ),
        },
        "top_anchors": _build_top_anchor_summary(dust_nodes),
        "origins": _build_origin_summaries(dust_nodes),
        "dust_nodes": dust_nodes,
        "edges": edges,
    }


def _fragment_to_dust_node(fragment: object, sibling_ids: Sequence[str], measurement_summary: Dict[str, object]) -> Dict[str, object]:
    anchor = []
    for entry in getattr(fragment, "anchors", []) or []:
        anchor.append({"type": entry.anchor_type, "value": entry.key})
    if not anchor and getattr(fragment, "anchor", None) is not None:
        anchor.append({"type": fragment.anchor.anchor_type, "value": fragment.anchor.key})

    source_span = {
        "start": getattr(fragment.source_range, "start", None),
        "end": getattr(fragment.source_range, "end", None),
    }
    compact = " ".join(fragment.raw_text.split())
    short_label = compact[:18] + ("…" if len(compact) > 18 else "")
    scene = fragment.scene
    color = {
        "self": "#b45309",
        "work": "#2563eb",
        "evidence": "#047857",
        "explanation": "#2563eb",
        "comparison": "#7c3aed",
        "reflection": "#b45309",
        "meta": "#7c3aed",
        "unknown": "#64748b",
    }.get(scene, "#8b5e34")
    observer_role = fragment.metadata.get("observer_role", "")
    observer_ambiguity = fragment.metadata.get("observer_ambiguity")
    observer_confidence_numeric = fragment.metadata.get("observer_confidence_numeric")
    observer_signals = fragment.metadata.get("observer_signals", [])
    observer_compare = _observer_compare_from_fragment(fragment)

    return {
        "dust_id": fragment.fragment_id,
        "origin_id": fragment.source_id,
        "projection_origin_id": fragment.metadata.get("projected_material_id", ""),
        "source_type": fragment.source_type,
        "source_ref": fragment.source_path,
        "text": fragment.raw_text,
        "source_path": fragment.source_path,
        "source_span": source_span,
        "siblings": [value for value in sibling_ids if value != fragment.fragment_id],
        "created_at": fragment.created_at,
        "D": float(fragment.D),
        "I": float(fragment.I),
        "S": float(fragment.S),
        "scene": fragment.scene,
        "flow": fragment.flow,
        "anchors": anchor,
        "observer_role": observer_role,
        "observer_ambiguity": observer_ambiguity,
        "observer_confidence_numeric": observer_confidence_numeric,
        "observer_signals": observer_signals,
        "observer_compare": observer_compare,
        "time_in": fragment.time or fragment.created_at,
        "last_seen": fragment.created_at,
        "recurrence_count": 1,
        "short_label": short_label,
        "color": color,
        "radius": round(8 + (float(fragment.I) * 8) + (float(fragment.S) * 4), 1),
        "engine_relations": {"traces": [], "pressures": [], "seeds": []},
        "measurement_summary": measurement_summary,
        "provenance_steps": [entry.step for entry in getattr(fragment, "provenance_log", [])],
    }


def _observer_compare_from_fragment(fragment: object) -> Dict[str, object]:
    internal = fragment.metadata.get("internal_observer") or {}
    profiles = internal.get("profiles") or {}
    merged = internal.get("merged") or {}
    if not profiles:
        return {"available": False, "items": [], "merged": {}}

    scenes = {}
    roles = {}
    for profile_name, payload in profiles.items():
        scene = payload.get("scene")
        role = payload.get("role")
        if scene:
            scenes[str(profile_name)] = str(scene)
        if role:
            roles[str(profile_name)] = str(role)

    items = []
    if len(set(scenes.values())) > 1:
        items.append(
            {
                "kind": "scene",
                "summary": "scene disagreement: " + " / ".join(f"{k}={v}" for k, v in scenes.items()),
                "profiles": scenes,
            }
        )
    if len(set(roles.values())) > 1:
        items.append(
            {
                "kind": "role",
                "summary": "role disagreement: " + " / ".join(f"{k}={v}" for k, v in roles.items()),
                "profiles": roles,
            }
        )
    return {
        "available": True,
        "items": items,
        "merged": {
            "scene": merged.get("scene", ""),
            "role": merged.get("role", ""),
            "ambiguity": merged.get("ambiguity"),
            "confidence": merged.get("confidence"),
        },
    }


def _material_to_dust_node(material: Dict[str, object], sibling_ids: Sequence[str]) -> Dict[str, object]:
    metadata = dict(material.get("metadata", {}))
    anchors = []
    for entry in list(metadata.get("anchors", []) or [])[:8]:
        anchors.append(
            {
                "type": str(entry.get("type", "semantic")).strip() or "semantic",
                "value": str(entry.get("value") or entry.get("canonical_key") or "").strip(),
            }
        )
    payload = str(material.get("raw_payload", "")).strip()
    compact = " ".join(payload.split())
    short_label = compact[:18] + ("…" if len(compact) > 18 else "")
    scene = str(metadata.get("scene", "unknown")).strip() or "unknown"
    color = {
        "self": "#b45309",
        "work": "#2563eb",
        "evidence": "#047857",
        "explanation": "#2563eb",
        "comparison": "#7c3aed",
        "reflection": "#b45309",
        "meta": "#7c3aed",
        "unknown": "#64748b",
        "review": "#7c3aed",
    }.get(scene, "#8b5e34")
    dust_id = str(metadata.get("dust_input_id", "")).strip() or str(material.get("material_id", "")).strip()
    origin_id = str(metadata.get("source_origin_id", "")).strip() or str(material.get("source_ref", "")).strip() or dust_id
    observer_role = str(metadata.get("observer_role", "")).strip()
    observer_ambiguity = metadata.get("observer_ambiguity")
    observer_confidence_numeric = metadata.get("observer_confidence_numeric")
    observer_signals = list(metadata.get("observer_signals", []) or [])
    observer_trace = dict(metadata.get("observer_or_ambiguity_trace", {}) or {})
    observer_compare = {
        "available": False,
        "items": [],
        "merged": {
            "scene": scene,
            "role": observer_role,
            "ambiguity": observer_ambiguity,
            "confidence": observer_confidence_numeric,
        },
    }
    if observer_trace:
        observer_compare = {
            "available": bool(observer_trace.get("available", False)),
            "items": list(observer_trace.get("items", []) or []),
            "merged": {
                "scene": (observer_trace.get("merged", {}) or {}).get("scene", scene),
                "role": (observer_trace.get("merged", {}) or {}).get("role", observer_role),
                "ambiguity": (observer_trace.get("merged", {}) or {}).get("ambiguity", observer_ambiguity),
                "confidence": (observer_trace.get("merged", {}) or {}).get("confidence", observer_confidence_numeric),
            },
        }
    return {
        "dust_id": dust_id,
        "origin_id": origin_id,
        "projection_origin_id": "",
        "source_type": str(material.get("source_type", "memo")).strip() or "memo",
        "source_ref": str(material.get("source_ref", "")).strip(),
        "text": payload,
        "source_path": str(material.get("source_ref", "")).strip(),
        "source_span": {"start": None, "end": None},
        "siblings": [value for value in sibling_ids if value != dust_id],
        "created_at": str(material.get("created_at", "")).strip(),
        "D": float(metadata.get("D", 0.5)),
        "I": float(metadata.get("I", 0.5)),
        "S": float(metadata.get("S", 0.5)),
        "scene": scene,
        "flow": str(metadata.get("flow", "unknown")).strip() or "unknown",
        "anchors": anchors,
        "observer_role": observer_role,
        "observer_ambiguity": observer_ambiguity,
        "observer_confidence_numeric": observer_confidence_numeric,
        "observer_signals": observer_signals,
        "observer_compare": observer_compare,
        "time_in": str(metadata.get("time_in", "")).strip(),
        "last_seen": str(metadata.get("last_seen", "")).strip() or str(material.get("created_at", "")).strip(),
        "recurrence_count": int(metadata.get("recurrence_count", 1) or 1),
        "short_label": short_label,
        "color": color,
        "radius": round(8 + (float(metadata.get("I", 0.5)) * 8) + (float(metadata.get("S", 0.5)) * 4), 1),
        "engine_relations": {"traces": [], "pressures": [], "seeds": []},
        "measurement_summary": {"count": 0, "types": []},
        "provenance_steps": ["material_backed_dust"],
    }


def _build_dust_compact_summary(dust_nodes: List[Dict[str, object]], edges: List[Dict[str, object]]) -> Dict[str, object]:
    compare_items: List[str] = []
    disagreement_items: List[str] = []
    edge_reason_items: List[str] = []
    compare_available = False
    disagreement_available = False

    for node in dust_nodes:
        observer_compare = node.get("observer_compare") or {}
        if observer_compare.get("available") is True:
            compare_available = True
            merged = observer_compare.get("merged") or {}
            merged_line = "merged:%s / %s" % (
                str(merged.get("scene", "") or "-"),
                str(merged.get("role", "") or "-"),
            )
            if merged_line not in compare_items:
                compare_items.append(merged_line)
            for item in observer_compare.get("items", []):
                disagreement_available = True
                summary = str(item.get("summary", "")).strip()
                if summary and summary not in disagreement_items:
                    disagreement_items.append(summary)
                if len(disagreement_items) >= 3:
                    break
        if len(compare_items) >= 3 and len(disagreement_items) >= 3:
            break

    reason_counter: Counter[str] = Counter()
    for edge in edges:
        reasons = edge.get("reasons") or {}
        reason_family = str(reasons.get("reason_family", "")).strip()
        if reason_family:
            reason_counter[reason_family] += 1
        else:
            reason_type = str(reasons.get("type", "")).strip()
            if reason_type:
                reason_counter[reason_type] += 1
            else:
                reason_counter[str(edge.get("edge_type", "unknown"))] += 1
    for label, count in reason_counter.most_common(3):
        edge_reason_items.append(f"{label}:{count}")

    return {
        "observer_compare": compact_payload(
            available=compare_available,
            items=compare_items,
            limit=3,
        ),
        "observer_disagreement": compact_payload(
            available=compare_available,
            items=disagreement_items,
            limit=3,
        ),
        "edge_reason": compact_payload(
            available=True,
            items=edge_reason_items,
            limit=3,
        ),
    }


def _measurement_summary_by_fragment(store: MeasurementStore) -> Dict[str, Dict[str, object]]:
    grouped: Dict[str, List[str]] = defaultdict(list)
    for record in store.read_all():
        grouped[record.fragment_id].append(record.measurement_type)
    return {
        fragment_id: {
            "count": len(values),
            "types": sorted(set(values)),
        }
        for fragment_id, values in grouped.items()
    }


def write_dust_field_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_dust_field_data(runtime_root)
    reports_root = runtime_root / "reports"
    reports_root.mkdir(parents=True, exist_ok=True)
    json_path = reports_root / "dust_field_view.json"
    html_path = reports_root / "dust_field_view.html"
    json_path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    html_path.write_text(render_dust_field_html(data), encoding="utf-8")
    return {"json_path": json_path, "html_path": html_path}


def render_dust_field_html(data: Dict[str, object]) -> str:
    payload = json.dumps(data, ensure_ascii=True)
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dust Connection Viewer</title>
  <style>
    :root {
      --bg: #f1eadc;
      --panel: rgba(255, 250, 242, 0.94);
      --line: #d8ccb9;
      --ink: #1f2937;
      --muted: #6b7280;
      --direct: #2563eb;
      --weak: #94a3b8;
      --tension: #b91c1c;
      --node: #8b5e34;
      --node-stroke: #f8f3ea;
      --accent: #6d4c2f;
      --field-a: rgba(191, 149, 93, 0.12);
      --field-b: rgba(99, 102, 241, 0.10);
      --field-c: rgba(14, 116, 144, 0.10);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 18% 18%, rgba(255,255,255,0.95), transparent 24%),
        radial-gradient(circle at 82% 12%, rgba(191,149,93,0.14), transparent 18%),
        radial-gradient(circle at 72% 78%, rgba(14,116,144,0.12), transparent 22%),
        radial-gradient(circle at top, rgba(255,255,255,0.82), transparent 32%),
        linear-gradient(180deg, #fff8ed 0%, var(--bg) 100%);
    }
    .page {
      min-height: 100vh;
      display: grid;
      grid-template-columns: minmax(0, 1fr) 420px;
    }
    .sidebar {
      display: none;
    }
    .sidebar h1 { margin: 0 0 10px; font-size: 28px; }
    .muted { color: var(--muted); }
    .metric-grid {
      display: grid;
      gap: 10px;
      margin: 18px 0;
    }
    .metric {
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: var(--panel);
    }
    .metric strong { display: block; font-size: 24px; }
    .return-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 0 0 14px;
    }
    .return-link {
      display: inline-block;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      background: rgba(255, 250, 242, 0.94);
      color: var(--accent);
      text-decoration: none;
      font-size: 12px;
    }
    .summary-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 10px;
      margin: 16px 0;
    }
    .summary-card {
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: var(--panel);
    }
    .summary-card h3 {
      margin: 0 0 8px;
      font-size: 12px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--accent);
    }
    .toolbar {
      display: grid;
      gap: 8px;
      margin: 18px 0;
    }
    .toolbar label {
      display: grid;
      gap: 6px;
      font-size: 13px;
    }
    select {
      width: 100%;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: #fffdf9;
      color: var(--ink);
    }
    .legend {
      display: grid;
      gap: 8px;
      margin-top: 16px;
      font-size: 13px;
    }
    .legend div {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .swatch {
      width: 18px;
      height: 3px;
      border-radius: 999px;
    }
    .content {
      padding: 14px 12px 14px 14px;
      min-width: 0;
    }
    .detail-panel {
      border-left: 1px solid var(--line);
      background: rgba(255, 250, 242, 0.92);
      padding: 14px 14px 18px;
      overflow: auto;
    }
    .graph-panel, .list-panel, .modal-card {
      border: 1px solid var(--line);
      border-radius: 18px;
      background: rgba(255, 250, 242, 0.9);
      box-shadow: 0 10px 30px rgba(77, 55, 31, 0.08);
    }
    .graph-panel {
      position: relative;
      overflow: auto;
      background:
        radial-gradient(circle at 20% 22%, rgba(255,255,255,0.70), transparent 20%),
        radial-gradient(circle at 78% 30%, rgba(191,149,93,0.10), transparent 22%),
        radial-gradient(circle at 68% 72%, rgba(99,102,241,0.08), transparent 24%),
        linear-gradient(180deg, rgba(255,253,248,0.96) 0%, rgba(247,240,227,0.96) 100%);
    }
    .graph-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 14px 0;
      gap: 12px;
    }
    .graph-head h2 { margin: 0; font-size: 20px; }
    .graph-tools {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .graph-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 10px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      border-radius: 999px;
      background: rgba(255, 252, 247, 0.88);
      font-size: 12px;
      color: var(--accent);
    }
    .graph-tabs {
      display: flex;
      gap: 8px;
      padding: 10px 14px 0;
      flex-wrap: wrap;
    }
    .tab-btn {
      border: 1px solid rgba(216, 204, 185, 0.9);
      border-radius: 999px;
      padding: 7px 11px;
      background: rgba(255, 252, 247, 0.88);
      color: var(--accent);
      font-size: 12px;
      cursor: pointer;
    }
    .tab-btn.active {
      background: rgba(139, 94, 52, 0.12);
      border-color: rgba(139, 94, 52, 0.34);
      color: #5b4633;
      font-weight: 700;
    }
    .filter-bar {
      display: flex;
      gap: 8px;
      padding: 10px 14px 0;
      flex-wrap: wrap;
      align-items: center;
    }
    .filter-bar label {
      display: grid;
      gap: 4px;
      font-size: 12px;
      min-width: 130px;
    }
    .zoom-bar {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-left: auto;
    }
    .zoom-btn {
      border: 1px solid rgba(216, 204, 185, 0.9);
      border-radius: 10px;
      background: rgba(255, 252, 247, 0.95);
      color: var(--accent);
      cursor: pointer;
      min-width: 34px;
      height: 34px;
      font-size: 16px;
    }
    .graph-stage {
      position: relative;
      min-height: 76vh;
      overflow: hidden;
      border-top: 1px solid rgba(216, 204, 185, 0.55);
    }
    .graph-canvas {
      width: 100%;
      height: 76vh;
      display: block;
      cursor: grab;
    }
    .graph-canvas.dragging {
      cursor: grabbing;
    }
    .list-panel {
      padding: 0;
      border: 0;
      background: transparent;
      box-shadow: none;
    }
    .focus-panel {
      display: grid;
      gap: 12px;
      margin-top: 10px;
      margin-bottom: 12px;
    }
    .compare-card {
      padding: 12px 14px;
      border-radius: 16px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      background: #fffdf8;
      min-height: 180px;
    }
    .compare-card h3 {
      margin: 0 0 8px;
      font-size: 14px;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .compare-grid {
      display: grid;
      gap: 8px;
    }
    .compare-row {
      padding: 8px 10px;
      border-radius: 12px;
      border: 1px solid rgba(216, 204, 185, 0.85);
      background: rgba(255, 251, 245, 0.95);
      font-size: 12px;
      line-height: 1.45;
      cursor: pointer;
    }
    .list-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 10px;
      margin-top: 10px;
    }
    .card {
      padding: 12px;
      border-radius: 14px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      background: #fffdf8;
      font-size: 13px;
      line-height: 1.45;
    }
    .card strong { display: block; margin-bottom: 4px; }
    .section { margin-top: 14px; }
    .section h4 {
      margin: 0 0 8px;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--accent);
    }
    .pill-row {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .pill {
      display: inline-block;
      padding: 5px 8px;
      border-radius: 999px;
      background: #f3eadc;
      border: 1px solid rgba(216, 204, 185, 0.9);
      font-size: 12px;
    }
    .connection-row {
      padding: 8px 10px;
      border: 1px solid rgba(216, 204, 185, 0.85);
      border-radius: 12px;
      background: #fffdf8;
      margin-bottom: 8px;
      font-size: 12px;
      line-height: 1.45;
    }
    .inspector {
      position: absolute;
      left: 18px;
      bottom: 18px;
      width: min(360px, calc(100% - 36px));
      padding: 12px 14px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      border-radius: 16px;
      background: rgba(255, 251, 245, 0.94);
      box-shadow: 0 12px 24px rgba(77, 55, 31, 0.08);
      backdrop-filter: blur(6px);
      z-index: 10;
    }
    .inspector h3 {
      margin: 0 0 6px;
      font-size: 14px;
      color: var(--accent);
    }
    .inspector-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
      margin-top: 10px;
      font-size: 12px;
    }
    .inspector-metric {
      padding: 8px 9px;
      border-radius: 12px;
      background: #fffdf8;
      border: 1px solid rgba(216, 204, 185, 0.9);
    }
    .inspector-metric strong {
      display: block;
      font-size: 15px;
    }
    .origin-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-top: 8px;
      padding: 6px 10px;
      border-radius: 999px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      background: rgba(255, 252, 247, 0.9);
      font-size: 12px;
      color: var(--accent);
    }
    .detail-sections {
      display: grid;
      gap: 12px;
      margin-top: 12px;
    }
    .detail-card {
      padding: 12px 14px;
      border-radius: 16px;
      border: 1px solid rgba(216, 204, 185, 0.9);
      background: #fffdf8;
    }
    .detail-card h3 {
      margin: 0 0 8px;
      font-size: 14px;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .data-block {
      padding: 10px 12px;
      border-radius: 12px;
      border: 1px solid rgba(216, 204, 185, 0.85);
      background: #fcfaf5;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 12px;
      line-height: 1.5;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
    }
    .edge-data-row {
      padding: 10px 12px;
      border-radius: 12px;
      border: 1px solid rgba(216, 204, 185, 0.85);
      background: #fffdf8;
      margin-bottom: 8px;
      font-size: 12px;
      line-height: 1.5;
    }
    details.detail-card summary {
      cursor: pointer;
      list-style: none;
      font-size: 14px;
      color: var(--accent);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    details.detail-card summary::-webkit-details-marker {
      display: none;
    }
    @media (max-width: 980px) {
      .page { grid-template-columns: 1fr; }
      .detail-panel { border-left: 0; border-top: 1px solid var(--line); }
      .inspector {
        position: static;
        width: auto;
        margin: 0 18px 18px;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <main class="content">
      <section class="graph-panel">
        <div class="graph-head">
          <h2>Obsidian-like Dust Space</h2>
          <div class="graph-tools">
            <span class="graph-chip" id="graph-caption"></span>
            <span class="graph-chip" id="focus-caption">focus 없음</span>
          </div>
        </div>
        <div id="query-status" class="filter-bar" style="padding-top:8px;"></div>
        <div class="graph-tabs">
          <button type="button" class="tab-btn active" data-edge-mode="all">전체</button>
          <button type="button" class="tab-btn" data-edge-mode="direct">direct</button>
          <button type="button" class="tab-btn" data-edge-mode="weak">weak</button>
          <button type="button" class="tab-btn" data-edge-mode="tension">tension</button>
        </div>
        <div class="filter-bar">
          <label>scene
            <select id="scene-filter"></select>
          </label>
          <label>observer role
            <select id="observer-role-filter"></select>
          </label>
          <label>observer signal
            <select id="observer-signal-filter"></select>
          </label>
          <label>anchor
            <select id="anchor-filter"></select>
          </label>
          <div class="zoom-bar">
            <button type="button" class="zoom-btn" id="zoom-out">-</button>
            <span class="graph-chip" id="zoom-label">100%</span>
            <button type="button" class="zoom-btn" id="zoom-in">+</button>
            <button type="button" class="zoom-btn" id="zoom-reset">0</button>
          </div>
        </div>
        <div class="graph-stage">
          <canvas id="graph-canvas" class="graph-canvas"></canvas>
        </div>
        <div class="inspector">
          <h3>공간 현장</h3>
          <div id="graph-inspector-main" class="muted">먼지를 눌러서 원문과 연결의 흐름을 확인하세요.</div>
          <div class="inspector-grid">
            <div class="inspector-metric"><span>direct</span><strong id="inspector-direct">0</strong></div>
            <div class="inspector-metric"><span>weak</span><strong id="inspector-weak">0</strong></div>
            <div class="inspector-metric"><span>tension</span><strong id="inspector-tension">0</strong></div>
          </div>
        </div>
      </section>
      <section class="list-panel"></section>
    </main>
    <aside class="detail-panel">
      <h1 style="margin:0 0 6px; font-size:28px;">먼지 그래프</h1>
      <h2 style="margin:4px 0 10px">원본과 연결 보기</h2>
      <div id="return-bar" class="return-bar"></div>
      <div class="metric-grid">
        <div class="metric"><span>materials</span><strong id="metric-materials"></strong></div>
        <div class="metric"><span>dust</span><strong id="metric-dust"></strong></div>
        <div class="metric"><span>visible edges</span><strong id="metric-edges"></strong></div>
        <div class="metric"><span>origins</span><strong id="metric-origins"></strong></div>
      </div>
      <div class="legend">
        <div><span class="swatch" style="background: var(--direct)"></span>direct</div>
        <div><span class="swatch" style="background: var(--weak)"></span>weak</div>
        <div><span class="swatch" style="background: var(--tension)"></span>tension</div>
      </div>
      <div id="summary-strip" class="summary-strip"></div>
      <section class="list-panel">
        <div class="focus-panel">
          <div class="compare-card">
            <h3>선택 먼지</h3>
            <div id="focus-primary" class="compare-grid">
              <div class="muted">먼지를 선택하면 원문이 여기에 고정됩니다.</div>
            </div>
          </div>
          <div class="compare-card">
            <h3>연결 상대 비교</h3>
            <div id="focus-neighbors" class="compare-grid">
              <div class="muted">선택 먼지의 direct / weak / tension 상대가 여기에 나타납니다.</div>
            </div>
          </div>
        </div>
        <div class="detail-sections">
          <div class="detail-card">
            <h3>원본과 형제 먼지</h3>
            <div id="sidebar-origin" class="muted">먼지를 선택하면 원본과 형제 먼지가 고정됩니다.</div>
          </div>
          <div class="detail-card">
            <h3>연결된 원본</h3>
            <div id="sidebar-connections" class="muted">연결 상대 원문과 종류가 여기에 나타납니다.</div>
          </div>
          <div class="detail-card">
            <h3>연결 이유</h3>
            <div id="sidebar-reasons" class="muted">연결 이유가 여기에 나타납니다.</div>
          </div>
          <details class="detail-card">
            <summary>선택 먼지 데이터</summary>
            <div id="sidebar-node-data" class="muted" style="margin-top:10px;">선택 먼지의 실제 값이 여기에 나타납니다.</div>
          </details>
          <details class="detail-card">
            <summary>연결 데이터</summary>
            <div id="sidebar-edge-data" class="muted" style="margin-top:10px;">현재 보이는 연결의 실제 데이터가 여기에 나타납니다.</div>
          </details>
          <details class="detail-card">
            <summary>엔진 기록</summary>
            <div id="sidebar-engine" class="muted" style="margin-top:10px;">새 입력 경로 relation 기록이 여기에 나타납니다.</div>
          </details>
        </div>
        <div id="summary-grid" class="list-grid"></div>
      </section>
    </aside>
  </div>
  <script id="dust-data" type="application/json">""" + payload + """</script>
  <script>
    const data = JSON.parse(document.getElementById('dust-data').textContent);
    const canvas = document.getElementById('graph-canvas');
    const ctx = canvas.getContext('2d');
    const sceneFilter = document.getElementById('scene-filter');
    const observerRoleFilter = document.getElementById('observer-role-filter');
    const observerSignalFilter = document.getElementById('observer-signal-filter');
    const anchorFilter = document.getElementById('anchor-filter');
    const edgeModeButtons = Array.from(document.querySelectorAll('[data-edge-mode]'));
    const zoomLabel = document.getElementById('zoom-label');
    const zoomIn = document.getElementById('zoom-in');
    const zoomOut = document.getElementById('zoom-out');
    const zoomReset = document.getElementById('zoom-reset');
    const focusCaption = document.getElementById('focus-caption');
    const queryStatus = document.getElementById('query-status');
    const returnBar = document.getElementById('return-bar');
    const summaryStrip = document.getElementById('summary-strip');
    const inspectorMain = document.getElementById('graph-inspector-main');
    const inspectorDirect = document.getElementById('inspector-direct');
    const inspectorWeak = document.getElementById('inspector-weak');
    const inspectorTension = document.getElementById('inspector-tension');
    const focusPrimary = document.getElementById('focus-primary');
    const focusNeighbors = document.getElementById('focus-neighbors');
    const sidebarOrigin = document.getElementById('sidebar-origin');
    const sidebarNodeData = document.getElementById('sidebar-node-data');
    const sidebarConnections = document.getElementById('sidebar-connections');
    const sidebarEdgeData = document.getElementById('sidebar-edge-data');
    const sidebarReasons = document.getElementById('sidebar-reasons');
    const sidebarEngine = document.getElementById('sidebar-engine');
    const escapeHtml = (text) => String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    function prettyJson(value) {
      return escapeHtml(JSON.stringify(value, null, 2));
    }
    let selectedNodeId = null;
    let edgeMode = 'all';
    let zoomScale = 1;
    let currentVisibleNodeIds = new Set();
    let currentVisibleEdges = [];
    let currentNodes = [];
    let currentEdgeRows = [];
    let currentNodeMap = {};
    let currentOriginGroups = {};
    let animationFrame = null;
    let simulationTicks = 0;
    const params = new URLSearchParams(window.location.search);
    const requestedDustId = params.get('dust_id');
    const requestedFrom = params.get('from');
    const requestedReturnHref = params.get('return_href');
    const requestedReturnLabel = params.get('return_label');
    const originRoute = params.get('origin_route');
    const originLocalSpaceId = params.get('origin_local_space_id');
    const originRegionLabel = params.get('origin_region_label');
    const originBridgeId = params.get('origin_bridge_id');
    const originSourceRef = params.get('origin_source_ref');
    const originFragmentId = params.get('origin_fragment_id');
    const originDustId = params.get('origin_dust_id');
    const camera = { x: 40, y: 40, scale: 1 };
    const pointerState = {
      mode: null,
      nodeId: null,
      startX: 0,
      startY: 0,
      lastX: 0,
      lastY: 0,
      moved: false
    };

    document.getElementById('metric-materials').textContent = data.summary.material_count;
    document.getElementById('metric-dust').textContent = data.summary.dust_count;
    document.getElementById('metric-edges').textContent = data.summary.edge_count;
    document.getElementById('metric-origins').textContent = data.summary.origin_count;
    document.getElementById('graph-caption').textContent = 'dust ' + data.summary.dust_count + ' / edge ' + data.summary.edge_count;

    const sceneOptions = ['all'].concat(data.filters.scenes || []);
    sceneFilter.innerHTML = sceneOptions.map(value =>
      '<option value="' + escapeHtml(value) + '">' + escapeHtml(value === 'all' ? '전체' : value) + '</option>'
    ).join('');

    const anchorOptions = ['all'].concat(data.filters.anchors || []);
    anchorFilter.innerHTML = anchorOptions.map(value =>
      '<option value="' + escapeHtml(value) + '">' + escapeHtml(value === 'all' ? '전체' : value) + '</option>'
    ).join('');

    const observerRoleOptions = ['all'].concat(data.filters.observer_roles || []);
    observerRoleFilter.innerHTML = observerRoleOptions.map(value =>
      '<option value="' + escapeHtml(value) + '">' + escapeHtml(value === 'all' ? '전체' : value) + '</option>'
    ).join('');

    const observerSignalOptions = ['all'].concat(data.filters.observer_signals || []);
    observerSignalFilter.innerHTML = observerSignalOptions.map(value =>
      '<option value="' + escapeHtml(value) + '">' + escapeHtml(value === 'all' ? '전체' : value) + '</option>'
    ).join('');

    const nodesById = Object.fromEntries((data.dust_nodes || []).map(node => [node.dust_id, node]));
    const addReturnLink = (href, label) => {
      const link = document.createElement('a');
      link.className = 'return-link';
      link.href = href;
      link.textContent = label;
      returnBar.appendChild(link);
    };
    if (requestedReturnHref) {
      addReturnLink(requestedReturnHref, requestedReturnLabel || 'Back');
    } else if (requestedFrom === 'atlas') {
      addReturnLink('/atlas', 'Back to Atlas');
    } else if (requestedFrom === 'operator') {
      addReturnLink('/', 'Back to Operator');
    } else {
      addReturnLink('/', 'Operator');
      addReturnLink('/atlas', 'Atlas');
    }
    const contextBar = document.createElement('div');
    contextBar.className = 'chips';
    contextBar.style.marginBottom = '12px';
    const pushContextChip = (label, value) => {
      if (!value) return;
      const chip = document.createElement('span');
      chip.className = 'chip';
      chip.textContent = label + ': ' + value;
      contextBar.appendChild(chip);
    };
    pushContextChip('origin', originRoute || requestedFrom);
    pushContextChip('region', originRegionLabel);
    pushContextChip('local_space', originLocalSpaceId);
    pushContextChip('bridge', originBridgeId);
    pushContextChip('source_ref', originSourceRef);
    pushContextChip('fragment', originFragmentId);
    pushContextChip('dust', originDustId);
    if (contextBar.childElementCount) {
      returnBar.insertAdjacentElement('afterend', contextBar);
    }
    const edgesByNode = {};
    (data.edges || []).forEach(edge => {
      edgesByNode[edge.source] = edgesByNode[edge.source] || [];
      edgesByNode[edge.target] = edgesByNode[edge.target] || [];
      edgesByNode[edge.source].push(edge);
      edgesByNode[edge.target].push(edge);
    });

    function focusedNode() {
      if (selectedNodeId && nodesById[selectedNodeId]) return nodesById[selectedNodeId];
      return null;
    }

    function resizeCanvas() {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = Math.round(rect.width * dpr);
      canvas.height = Math.round(rect.height * dpr);
    }

    function worldPoint(clientX, clientY) {
      const rect = canvas.getBoundingClientRect();
      const x = (clientX - rect.left) / camera.scale - camera.x;
      const y = (clientY - rect.top) / camera.scale - camera.y;
      return { x, y };
    }

    function visibleEdgesForNode(nodeId) {
      return currentVisibleEdges.filter(edge => edge.source === nodeId || edge.target === nodeId);
    }

    function renderCompactSummary() {
      const compact = data.compact_summary || {};
      const dustJump = (() => {
        if (!requestedDustId) return { state: 'none', items: [] };
        if (nodesById[requestedDustId]) return { state: 'present', items: [requestedDustId] };
        return { state: 'present', items: ['requested dust not found'] };
      })();
      const cards = [
        ['Observer Compare', compact.observer_compare || { state: 'not_available_yet', items: [] }],
        ['Observer Disagreement', compact.observer_disagreement || { state: 'not_available_yet', items: [] }],
        ['Edge Reasons', compact.edge_reason || { state: 'none', items: [] }],
        ['Dust Jump', dustJump],
      ];
      summaryStrip.innerHTML = cards.map(([title, payload]) => {
        const state = payload.state || 'not_available_yet';
        let chips = '';
        if (state === 'not_available_yet') {
          chips = '<span class="chip">not available yet</span>';
        } else if (state === 'none') {
          chips = '<span class="chip">none</span>';
        } else {
          chips = (payload.items || []).slice(0, 3).map(item =>
            '<span class="chip">' + escapeHtml(String(item)) + '</span>'
          ).join('');
          if ((payload.overflow_count || 0) > 0) {
            chips += '<span class="chip">+' + escapeHtml(String(payload.overflow_count)) + ' more</span>';
          }
          if (!chips) chips = '<span class="chip">present</span>';
        }
        return '<div class="summary-card"><h3>' + escapeHtml(title) + '</h3><div class="chips">' + chips + '</div></div>';
      }).join('');
    }

    function updateInspector() {
      const node = focusedNode();
      if (!node) {
        focusCaption.textContent = 'focus 없음';
        inspectorMain.textContent = '먼지를 눌러서 원문과 연결의 흐름을 확인하세요.';
        inspectorDirect.textContent = '0';
        inspectorWeak.textContent = '0';
        inspectorTension.textContent = '0';
        focusPrimary.innerHTML = '<div class="muted">먼지를 선택하면 원문이 여기에 고정됩니다.</div>';
        focusNeighbors.innerHTML = '<div class="muted">선택 먼지의 direct / weak / tension 상대가 여기에 나타납니다.</div>';
        sidebarOrigin.innerHTML = '<div class="muted">먼지를 선택하면 원본과 형제 먼지가 고정됩니다.</div>';
        sidebarNodeData.innerHTML = '<div class="muted">선택 먼지의 실제 값이 여기에 나타납니다.</div>';
        sidebarConnections.innerHTML = '<div class="muted">연결 상대 원문과 종류가 여기에 나타납니다.</div>';
        sidebarEdgeData.innerHTML = '<div class="muted">현재 보이는 연결의 실제 데이터가 여기에 나타납니다.</div>';
        sidebarReasons.innerHTML = '<div class="muted">연결 이유가 여기에 나타납니다.</div>';
        sidebarEngine.innerHTML = '<div class="muted">새 입력 경로 relation 기록이 여기에 나타납니다.</div>';
        return;
      }
      const edges = visibleEdgesForNode(node.dust_id);
      const counts = {direct: 0, weak: 0, tension: 0};
      edges.forEach(edge => { counts[edge.edge_type] = (counts[edge.edge_type] || 0) + 1; });
      focusCaption.textContent = (node.source_ref || node.origin_id) + ' / ' + node.short_label;
      inspectorMain.innerHTML =
        '<strong>' + escapeHtml(node.text) + '</strong><br>' +
        '<span class="muted">origin=' + escapeHtml(node.source_ref || node.origin_id) +
        ' / scene=' + escapeHtml(node.scene) +
        ' / flow=' + escapeHtml(node.flow) +
        (node.observer_role ? ' / role=' + escapeHtml(node.observer_role) : '') +
        '</span>';
      inspectorDirect.textContent = String(counts.direct || 0);
      inspectorWeak.textContent = String(counts.weak || 0);
      inspectorTension.textContent = String(counts.tension || 0);
      focusPrimary.innerHTML =
        '<div class="compare-row">' +
        '<strong>' + escapeHtml(node.source_ref || node.origin_id) + '</strong><br>' +
        '<div>' + escapeHtml(node.text) + '</div>' +
        '<div class="muted" style="margin-top:6px">' + escapeHtml(node.source_type) +
        (node.source_path ? ' / ' + escapeHtml(node.source_path) : '') + '</div>' +
        '</div>';
      const rankedNeighbors = edges
        .slice()
        .sort((a, b) => Number(b.strength || 0) - Number(a.strength || 0))
        .slice(0, 6)
        .map(edge => {
          const other = nodesById[edge.source === node.dust_id ? edge.target : edge.source];
          if (!other) return '';
          return '<div class="compare-row" data-compare-dust="' + escapeHtml(other.dust_id) + '">' +
            '<strong>' + escapeHtml(edge.edge_type) + '</strong> ' + escapeHtml(other.source_ref || other.origin_id) + '<br>' +
            '<div>' + escapeHtml(other.text) + '</div>' +
            '<div class="muted" style="margin-top:6px">strength=' + escapeHtml(String(edge.strength)) +
            ' / scene=' + escapeHtml(other.scene) +
            ' / flow=' + escapeHtml(other.flow) + '</div>' +
            '</div>';
        })
        .join('');
      focusNeighbors.innerHTML = rankedNeighbors || '<div class="muted">현재 연결 상대 없음</div>';
      document.querySelectorAll('[data-compare-dust]').forEach(row => {
        row.addEventListener('click', () => {
          const nextNode = nodesById[row.getAttribute('data-compare-dust')];
          if (nextNode) selectNode(nextNode);
        });
      });
      sidebarOrigin.innerHTML =
        '<div><strong>원문</strong></div><div>' + escapeHtml(node.text) + '</div><div class="muted" style="margin-top:6px">' +
        escapeHtml(node.source_ref || node.origin_id) + ' / ' + escapeHtml(node.source_type) +
        (node.source_path ? ' / ' + escapeHtml(node.source_path) : '') + '</div>' +
        '<div class="muted" style="margin-top:6px">origin=' + escapeHtml(node.origin_id) +
        ' / siblings=' + escapeHtml(String((node.siblings || []).length)) + '</div>' +
        '<div class="muted" style="margin-top:6px">observer ambiguity=' + escapeHtml(String(node.observer_ambiguity ?? '-')) +
        ' / numeric confidence=' + escapeHtml(String(node.observer_confidence_numeric ?? '-')) + '</div>' +
        '<div class="section" style="margin-top:10px"><h4>Origin Siblings</h4>' + siblingRows(node) + '</div>';
      sidebarNodeData.innerHTML =
        '<div class="data-block">' + prettyJson({
          dust_id: node.dust_id,
          origin_id: node.origin_id,
          source_ref: node.source_ref,
          source_type: node.source_type,
          text: node.text,
          scene: node.scene,
          flow: node.flow,
          observer_role: node.observer_role,
          observer_ambiguity: node.observer_ambiguity,
          observer_confidence_numeric: node.observer_confidence_numeric,
          observer_signals: node.observer_signals,
          observer_compare: node.observer_compare,
          D: node.D,
          I: node.I,
          S: node.S,
          anchors: node.anchors,
          time_in: node.time_in,
          recurrence_count: node.recurrence_count,
          siblings: node.siblings
        }) + '</div>';
      sidebarConnections.innerHTML = connectionSourceRows(node, edges);
      sidebarEdgeData.innerHTML = edges.length ? edges.map(edge => {
        const other = nodesById[edge.source === node.dust_id ? edge.target : edge.source];
        return '<div class="edge-data-row"><strong>' + escapeHtml(edge.edge_type) + '</strong> ' +
          escapeHtml(edge.edge_id) + '<br>' +
          '<div><strong>target</strong>: ' + escapeHtml(other ? (other.source_ref || other.origin_id) : 'unknown') + '</div>' +
          '<div><strong>target_text</strong>: ' + escapeHtml(other ? other.text : 'unknown') + '</div>' +
          '<div><strong>state</strong>: ' + escapeHtml(edge.state) + ' / <strong>strength</strong>: ' + escapeHtml(String(edge.strength)) + '</div>' +
          '<div><strong>reasons</strong></div><div class="data-block" style="margin-top:6px">' + prettyJson(edge.reasons || {}) + '</div>' +
          '</div>';
      }).join('') : '<div class="muted">현재 보이는 연결 데이터 없음</div>';
      const observerCompare = node.observer_compare || { available: false, items: [], merged: {} };
      const observerRows = observerCompare.available
        ? '<div class="connection-row"><strong>merged</strong><br>' +
          'scene=' + escapeHtml(observerCompare.merged.scene || '-') +
          ' / role=' + escapeHtml(observerCompare.merged.role || '-') +
          ' / ambiguity=' + escapeHtml(String(observerCompare.merged.ambiguity ?? '-')) +
          ' / confidence=' + escapeHtml(String(observerCompare.merged.confidence ?? '-')) + '</div>' +
          ((observerCompare.items || []).map(item =>
            '<div class="connection-row"><strong>' + escapeHtml(item.kind) + '</strong><br>' +
            escapeHtml(item.summary || 'disagreement') + '</div>'
          ).join('') || '<div class="connection-row"><strong>observer</strong><br>explicit disagreement 없음</div>')
        : '<div class="connection-row"><strong>observer</strong><br>compare not available</div>';
      sidebarReasons.innerHTML = observerRows + reasonRows(edges);
      sidebarEngine.innerHTML = observerRows + engineRows(node);
    }

    function recentDustCards() {
      return (data.dust_nodes || []).filter(node => currentVisibleNodeIds.has(node.dust_id)).slice(-18).reverse().map(node => {
        const allEdges = visibleEdgesForNode(node.dust_id);
        const typeCounts = {direct: 0, weak: 0, tension: 0};
        allEdges.forEach(edge => { typeCounts[edge.edge_type] = (typeCounts[edge.edge_type] || 0) + 1; });
        const related = allEdges
          .slice()
          .sort((a, b) => Number(b.strength || 0) - Number(a.strength || 0))
          .slice(0, 3)
          .map(edge => {
            const other = nodesById[edge.source === node.dust_id ? edge.target : edge.source];
            if (!other) return '';
            return '<div class="muted" style="margin-top:4px">' +
              escapeHtml(edge.edge_type) + ' -> ' + escapeHtml(other.text) + '</div>';
          }).join('');
        return '<div class="card" data-dust-card="' + escapeHtml(node.dust_id) + '">' +
          '<strong>' + escapeHtml(node.source_ref || node.origin_id) + '</strong>' +
          '<div>' + escapeHtml(node.text) + '</div>' +
          '<div class="muted" style="margin-top:6px">scene=' + escapeHtml(node.scene) +
          ' / flow=' + escapeHtml(node.flow) +
          (node.observer_role ? ' / role=' + escapeHtml(node.observer_role) : '') + '</div>' +
          '<div class="muted" style="margin-top:4px">observer ambiguity=' + escapeHtml(String(node.observer_ambiguity ?? '-')) + '</div>' +
          (((node.observer_signals || []).length)
            ? '<div class="muted" style="margin-top:4px;color:#8f1d1d">signals=' + escapeHtml((node.observer_signals || []).join(', ')) + '</div>'
            : '') +
          '<div class="muted" style="margin-top:4px">direct=' + escapeHtml(String(typeCounts.direct || 0)) +
          ' / weak=' + escapeHtml(String(typeCounts.weak || 0)) +
          ' / tension=' + escapeHtml(String(typeCounts.tension || 0)) + '</div>' +
          related +
          '</div>';
      }).join('');
    }

    function renderSummaryCards() {
      document.getElementById('summary-grid').innerHTML = recentDustCards();
      document.querySelectorAll('[data-dust-card]').forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => {
          const node = nodesById[card.getAttribute('data-dust-card')];
          if (node) selectNode(node);
        });
      });
    }

    function matchesNode(node) {
      if (sceneFilter.value !== 'all' && node.scene !== sceneFilter.value) return false;
      if (observerRoleFilter.value !== 'all' && (node.observer_role || '') !== observerRoleFilter.value) return false;
      if (observerSignalFilter.value !== 'all' && !((node.observer_signals || []).includes(observerSignalFilter.value))) return false;
      if (anchorFilter.value !== 'all') {
        const values = (node.anchors || []).map(anchor => anchor.value);
        if (!values.includes(anchorFilter.value)) return false;
      }
      return true;
    }

    function matchesEdge(edge, visibleNodeIds) {
      if (edgeMode !== 'all' && edge.edge_type !== edgeMode) return false;
      return visibleNodeIds.has(edge.source) && visibleNodeIds.has(edge.target);
    }

    function applyZoom() {
      camera.scale = zoomScale;
      zoomLabel.textContent = Math.round(zoomScale * 100) + '%';
      drawGraph();
    }

    function selectNode(node) {
      selectedNodeId = node.dust_id;
      updateInspector();
      drawGraph();
    }

    function pickNode(worldX, worldY) {
      for (let index = currentNodes.length - 1; index >= 0; index -= 1) {
        const node = currentNodes[index];
        const dx = worldX - node.x;
        const dy = worldY - node.y;
        if ((dx * dx) + (dy * dy) <= Math.pow(node.radius + 4, 2)) {
          return node;
        }
      }
      return null;
    }

    function buildLayoutState(nodes, edges) {
      const previous = Object.fromEntries(currentNodes.map(node => [node.dust_id, node]));
      const origins = {};
      nodes.forEach(node => {
        origins[node.origin_id] = origins[node.origin_id] || [];
        origins[node.origin_id].push(node);
      });
      const originKeys = Object.keys(origins);
      const columns = Math.max(1, Math.ceil(Math.sqrt(originKeys.length || 1)));
      const rows = Math.max(1, Math.ceil(originKeys.length / columns));
      const columnWidth = 360;
      const rowHeight = 280;
      const worldWidth = Math.max(1400, columns * columnWidth + 240);
      const worldHeight = Math.max(980, rows * rowHeight + 260);
      const layoutNodes = [];
      const nodeMap = {};
      originKeys.forEach((originId, groupIndex) => {
        const col = groupIndex % columns;
        const row = Math.floor(groupIndex / columns);
        const centerX = 120 + col * columnWidth + columnWidth / 2;
        const centerY = 140 + row * rowHeight;
        const group = origins[originId];
        const radius = Math.max(60, Math.min(120, 34 + group.length * 10));
        group.forEach((node, nodeIndex) => {
          const old = previous[node.dust_id];
          const angle = ((Math.PI * 2) / Math.max(group.length, 1)) * nodeIndex - Math.PI / 2;
          const x = old ? old.x : centerX + Math.cos(angle) * radius;
          const y = old ? old.y : centerY + Math.sin(angle) * radius;
          const rowState = Object.assign({}, node, {
            x,
            y,
            vx: old ? old.vx : 0,
            vy: old ? old.vy : 0,
            clusterX: centerX,
            clusterY: centerY,
            clusterRadius: radius
          });
          layoutNodes.push(rowState);
          nodeMap[rowState.dust_id] = rowState;
        });
      });
      currentNodeMap = nodeMap;
      currentOriginGroups = origins;
      currentEdgeRows = edges;
      currentNodes = layoutNodes;
      if (camera.x === 40 && camera.y === 40) {
        const rect = canvas.getBoundingClientRect();
        camera.x = Math.max(20, rect.width * 0.08);
        camera.y = Math.max(20, rect.height * 0.08);
      }
      return { worldWidth, worldHeight };
    }

    function simulateStep() {
      if (!currentNodes.length) return;
      const nodeCount = currentNodes.length;
      for (let i = 0; i < nodeCount; i += 1) {
        const node = currentNodes[i];
        if (pointerState.mode === 'drag-node' && pointerState.nodeId === node.dust_id) {
          node.vx = 0;
          node.vy = 0;
          continue;
        }
        node.vx += (node.clusterX - node.x) * 0.0015;
        node.vy += (node.clusterY - node.y) * 0.0015;
      }
      for (let i = 0; i < nodeCount; i += 1) {
        const left = currentNodes[i];
        for (let j = i + 1; j < nodeCount; j += 1) {
          const right = currentNodes[j];
          let dx = right.x - left.x;
          let dy = right.y - left.y;
          let dist2 = dx * dx + dy * dy;
          if (!dist2) {
            dx = (Math.random() - 0.5) * 0.4;
            dy = (Math.random() - 0.5) * 0.4;
            dist2 = dx * dx + dy * dy;
          }
          if (dist2 > 42000) continue;
          const force = 220 / dist2;
          const fx = dx * force;
          const fy = dy * force;
          left.vx -= fx;
          left.vy -= fy;
          right.vx += fx;
          right.vy += fy;
        }
      }
      currentEdgeRows.forEach(edge => {
        const left = currentNodeMap[edge.source];
        const right = currentNodeMap[edge.target];
        if (!left || !right) return;
        const dx = right.x - left.x;
        const dy = right.y - left.y;
        const distance = Math.max(1, Math.hypot(dx, dy));
        const desired =
          edge.edge_type === 'direct' ? 92 :
          edge.edge_type === 'tension' ? 118 : 146;
        const strength =
          edge.edge_type === 'direct' ? 0.013 :
          edge.edge_type === 'tension' ? 0.010 : 0.006;
        const delta = (distance - desired) * strength;
        const fx = (dx / distance) * delta;
        const fy = (dy / distance) * delta;
        left.vx += fx;
        left.vy += fy;
        right.vx -= fx;
        right.vy -= fy;
      });
      currentNodes.forEach(node => {
        if (pointerState.mode === 'drag-node' && pointerState.nodeId === node.dust_id) return;
        node.vx *= 0.84;
        node.vy *= 0.84;
        node.x += node.vx;
        node.y += node.vy;
      });
    }

    function startSimulation(ticks) {
      simulationTicks = Math.max(simulationTicks, ticks);
      if (animationFrame) return;
      const step = () => {
        animationFrame = null;
        if (simulationTicks <= 0) {
          drawGraph();
          return;
        }
        simulationTicks -= 1;
        simulateStep();
        drawGraph();
        animationFrame = requestAnimationFrame(step);
      };
      animationFrame = requestAnimationFrame(step);
    }

    function drawGraph() {
      resizeCanvas();
      const dpr = window.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, rect.width, rect.height);
      ctx.save();
      ctx.scale(camera.scale, camera.scale);
      ctx.translate(camera.x, camera.y);

      const focusNode = focusedNode();
      const focusId = focusNode ? focusNode.dust_id : null;
      const focusNeighborIds = new Set();
      const focusEdgeIds = new Set();
      if (focusId) {
        visibleEdgesForNode(focusId).forEach(edge => {
          focusNeighborIds.add(edge.source);
          focusNeighborIds.add(edge.target);
          focusEdgeIds.add(edge.edge_id);
        });
        focusNeighborIds.add(focusId);
      }

      Object.entries(currentOriginGroups).forEach(([originId, rows]) => {
        const group = rows.map(row => currentNodeMap[row.dust_id]).filter(Boolean);
        if (!group.length) return;
        const cx = group.reduce((sum, row) => sum + row.clusterX, 0) / group.length;
        const cy = group.reduce((sum, row) => sum + row.clusterY, 0) / group.length;
        const radius = Math.max(...group.map(row => row.clusterRadius));
        const relatedEdges = currentEdgeRows.filter(edge => {
          const left = currentNodeMap[edge.source];
          const right = currentNodeMap[edge.target];
          return left && right && (left.origin_id === originId || right.origin_id === originId);
        });
        const visible = !focusId || group.some(row => focusNeighborIds.has(row.dust_id));
        ctx.save();
        ctx.globalAlpha = visible ? 1 : 0.16;
        ctx.fillStyle = 'rgba(139,94,52,0.05)';
        ctx.beginPath();
        ctx.arc(cx, cy, radius + 52, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = 'rgba(139,94,52,0.18)';
        ctx.setLineDash([6, 8]);
        ctx.beginPath();
        ctx.arc(cx, cy, radius + 26, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = 'rgba(37,99,235,0.06)';
        ctx.beginPath();
        ctx.arc(cx, cy, radius + 12 + Math.min(44, relatedEdges.length * 0.9), 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = 'rgba(191,149,93,0.18)';
        ctx.beginPath();
        ctx.arc(cx, cy, Math.max(10, Math.min(28, 8 + group.length + relatedEdges.length * 0.35)), 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = 'rgba(91,70,51,0.9)';
        ctx.font = '12px Georgia';
        ctx.textAlign = 'center';
        ctx.fillText(group[0].source_ref || originId, cx, cy - radius - 18);
        ctx.font = '10px Georgia';
        const directCount = relatedEdges.filter(edge => edge.edge_type === 'direct').length;
        const tensionCount = relatedEdges.filter(edge => edge.edge_type === 'tension').length;
        ctx.fillText('dust ' + group.length + ' / direct ' + directCount + ' / tension ' + tensionCount, cx, cy - radius - 4);
        ctx.restore();
      });

      currentEdgeRows.forEach(edge => {
        const left = currentNodeMap[edge.source];
        const right = currentNodeMap[edge.target];
        if (!left || !right) return;
        const visible = !focusId || focusEdgeIds.has(edge.edge_id);
        ctx.save();
        ctx.globalAlpha = visible ? (edge.edge_type === 'weak' ? 0.42 : 0.8) : 0.06;
        ctx.strokeStyle = edge.color;
        ctx.lineWidth = Math.max(1, edge.strength);
        if (edge.edge_type === 'weak') ctx.setLineDash([4, 10]);
        if (edge.edge_type === 'tension') ctx.setLineDash([12, 7]);
        const mx = (left.x + right.x) / 2;
        const my = (left.y + right.y) / 2;
        const dx = right.x - left.x;
        const dy = right.y - left.y;
        const curveLift = edge.edge_type === 'tension' ? 28 : (edge.edge_type === 'direct' ? 16 : 8);
        const norm = Math.max(1, Math.hypot(dx, dy));
        const nx = mx - (dy * curveLift / norm);
        const ny = my + (dx * curveLift / norm);
        ctx.beginPath();
        ctx.moveTo(left.x, left.y);
        ctx.quadraticCurveTo(nx, ny, right.x, right.y);
        ctx.stroke();
        ctx.restore();
      });

      currentNodes.forEach(node => {
        const localEdges = visibleEdgesForNode(node.dust_id);
        const visible = !focusId || focusNeighborIds.has(node.dust_id);
        const observerSignals = node.observer_signals || [];
        const hasObserverSignal = observerSignals.length > 0;
        ctx.save();
        ctx.globalAlpha = visible ? 1 : 0.18;
        if (hasObserverSignal) {
          ctx.fillStyle = 'rgba(185,28,28,0.18)';
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius + 8, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.fillStyle = 'rgba(191,149,93,0.12)';
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius + Math.min(12, localEdges.length * 1.3), 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = node.color;
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.lineWidth = selectedNodeId === node.dust_id ? 4 : (hasObserverSignal ? 3 : 2);
        ctx.strokeStyle = hasObserverSignal ? '#b91c1c' : '#f8f3ea';
        ctx.stroke();
        if (selectedNodeId === node.dust_id || localEdges.length >= 6) {
          ctx.fillStyle = '#5b4633';
          ctx.font = '10px Georgia';
          ctx.textAlign = 'center';
          ctx.fillText(node.short_label, node.x, node.y + node.radius + 14);
          if (hasObserverSignal) {
            ctx.fillStyle = '#8f1d1d';
            ctx.font = '9px Georgia';
            ctx.fillText(observerSignals.join(', '), node.x, node.y + node.radius + 26);
          }
        }
        ctx.restore();
      });

      ctx.restore();
    }

    function renderGraph() {
      const nodes = (data.dust_nodes || []).filter(matchesNode);
      const visibleNodeIds = new Set(nodes.map(node => node.dust_id));
      const edges = (data.edges || []).filter(edge => matchesEdge(edge, visibleNodeIds));
      currentVisibleNodeIds = visibleNodeIds;
      currentVisibleEdges = edges;
      document.getElementById('metric-edges').textContent = String(edges.length);
      document.getElementById('graph-caption').textContent = 'dust ' + nodes.length + ' / edge ' + edges.length;
      buildLayoutState(nodes, edges);
      renderSummaryCards();
      updateInspector();
      drawGraph();
      startSimulation(80);
    }

    function pointerDown(event) {
      const point = worldPoint(event.clientX, event.clientY);
      const picked = pickNode(point.x, point.y);
      pointerState.startX = event.clientX;
      pointerState.startY = event.clientY;
      pointerState.lastX = event.clientX;
      pointerState.lastY = event.clientY;
      pointerState.moved = false;
      if (picked) {
        pointerState.mode = 'drag-node';
        pointerState.nodeId = picked.dust_id;
      } else {
        pointerState.mode = 'pan';
        pointerState.nodeId = null;
        canvas.classList.add('dragging');
      }
    }

    function pointerMove(event) {
      if (!pointerState.mode) return;
      const dx = event.clientX - pointerState.lastX;
      const dy = event.clientY - pointerState.lastY;
      pointerState.lastX = event.clientX;
      pointerState.lastY = event.clientY;
      if (Math.abs(event.clientX - pointerState.startX) > 3 || Math.abs(event.clientY - pointerState.startY) > 3) {
        pointerState.moved = true;
      }
      if (pointerState.mode === 'pan') {
        camera.x += dx / camera.scale;
        camera.y += dy / camera.scale;
        drawGraph();
        return;
      }
      if (pointerState.mode === 'drag-node' && pointerState.nodeId) {
        const node = currentNodeMap[pointerState.nodeId];
        if (!node) return;
        const point = worldPoint(event.clientX, event.clientY);
        node.x = point.x;
        node.y = point.y;
        node.vx = 0;
        node.vy = 0;
        drawGraph();
      }
    }

    function pointerUp(event) {
      if (!pointerState.mode) return;
      canvas.classList.remove('dragging');
      if (pointerState.mode === 'drag-node' && pointerState.nodeId && !pointerState.moved) {
        const node = currentNodeMap[pointerState.nodeId] || nodesById[pointerState.nodeId];
        if (node) selectNode(node);
      } else if (pointerState.mode === 'drag-node') {
        startSimulation(36);
      }
      pointerState.mode = null;
      pointerState.nodeId = null;
    }

    function wheelZoom(event) {
      event.preventDefault();
      const delta = event.deltaY < 0 ? 0.12 : -0.12;
      zoomScale = Math.max(0.45, Math.min(2.8, zoomScale + delta));
      applyZoom();
    }

    function siblingRows(node) {
      const siblings = (node.siblings || [])
        .map(id => nodesById[id])
        .filter(Boolean);
      if (!siblings.length) return '<div class="muted">같은 origin에서 함께 들어온 다른 dust 없음</div>';
      return siblings.map(other =>
        '<div class="connection-row"><strong>' + escapeHtml(other.short_label) + '</strong><br>' +
        '<div>' + escapeHtml(other.text) + '</div><div class="muted">' +
        escapeHtml(other.source_ref || other.origin_id) + '</div></div>'
      ).join('');
    }

    function connectionGroupRows(node, targetType, edges) {
      const rows = edges.filter(edge => edge.edge_type === targetType);
      return rows.map(edge => {
        const other = nodesById[edge.source === node.dust_id ? edge.target : edge.source];
        const title = other ? other.short_label + ' (' + (other.source_ref || other.origin_id) + ')' : 'unknown';
        const reasons = edge.reasons || {};
        return '<div class="connection-row"><strong>' + escapeHtml(targetType) + '</strong> ' +
          escapeHtml(title) + '<br><div><strong>연결 상대 원문</strong></div><div>' + escapeHtml(other ? other.text : 'unknown') + '</div>' +
          '<span class="muted">state=' + escapeHtml(edge.state) +
          ' / strength=' + escapeHtml(String(edge.strength)) + '</span><br>' +
          '<span class="muted">anchor=' + escapeHtml(reasons.anchor_reason || '-') +
          ' / scene=' + escapeHtml(reasons.scene_reason || '-') +
          ' / flow=' + escapeHtml(reasons.flow_reason || '-') + '</span></div>';
      }).join('') || '<div class="muted">' + escapeHtml(targetType) + ' 연결 없음</div>';
    }

    function connectionSourceRows(node, edges) {
      if (!edges.length) return '<div class="muted">연결된 원본 없음</div>';
      const grouped = {};
      edges.forEach(edge => {
        const other = nodesById[edge.source === node.dust_id ? edge.target : edge.source];
        if (!other) return;
        const key = other.source_ref || other.origin_id;
        grouped[key] = grouped[key] || { source: key, rows: [] };
        grouped[key].rows.push({ edge, other });
      });
      return Object.values(grouped)
        .sort((left, right) => right.rows.length - left.rows.length)
        .map(group => {
          const previews = group.rows
            .slice()
            .sort((a, b) => Number(b.edge.strength || 0) - Number(a.edge.strength || 0))
            .slice(0, 3)
            .map(row =>
              '<div class="muted" style="margin-top:6px">' +
              escapeHtml(row.edge.edge_type) + ' / ' + escapeHtml(row.other.text) +
              '</div>'
            )
            .join('');
          const counts = { direct: 0, weak: 0, tension: 0 };
          group.rows.forEach(row => { counts[row.edge.edge_type] = (counts[row.edge.edge_type] || 0) + 1; });
          return '<div class="connection-row">' +
            '<strong>' + escapeHtml(group.source) + '</strong>' +
            '<div class="muted" style="margin-top:4px">dust=' + escapeHtml(String(group.rows.length)) +
            ' / direct=' + escapeHtml(String(counts.direct || 0)) +
            ' / weak=' + escapeHtml(String(counts.weak || 0)) +
            ' / tension=' + escapeHtml(String(counts.tension || 0)) + '</div>' +
            previews +
            '</div>';
        })
        .join('');
    }

    function reasonRows(edges) {
      return edges.map(edge => {
        const reasons = edge.reasons || {};
        return '<div class="connection-row"><strong>' + escapeHtml(edge.edge_type) + '</strong><br>' +
          'anchor: ' + escapeHtml(reasons.anchor_reason || '-') + '<br>' +
          'scene: ' + escapeHtml(reasons.scene_reason || '-') + '<br>' +
          'flow: ' + escapeHtml(reasons.flow_reason || '-') + '<br>' +
          'role: ' + escapeHtml(reasons.role_reason || '-') + '<br>' +
          'ambiguity: ' + escapeHtml(reasons.ambiguity_reason || '-') + '<br>' +
          'direction: ' + escapeHtml(reasons.direction_reason || '-') + '<br>' +
          'time: ' + escapeHtml(reasons.time_reason || '-') + '</div>';
      }).join('') || '<div class="muted">이유 기록 없음</div>';
    }

    function engineRows(node) {
      const engine = node.engine_relations || {};
      const traceRows = (engine.traces || []).map(row =>
        '<div class="connection-row"><strong>trace</strong> ' + escapeHtml(row.trace_id) +
        '<br><div>' + escapeHtml(row.evidence_kind) + ' / ' + escapeHtml(row.note || '-') + '</div>' +
        '<div class="muted">targets: ' + escapeHtml((row.target_previews || []).join(' | ') || '-') + '</div></div>'
      ).join('');
      const pressureRows = (engine.pressures || []).map(row =>
        '<div class="connection-row"><strong>pressure</strong> ' + escapeHtml(row.profile_id) +
        '<br><div class="muted">' + escapeHtml((row.axes || []).join(', ')) + '</div></div>'
      ).join('');
      const seedRows = (engine.seeds || []).map(row =>
        '<div class="connection-row"><strong>seed</strong> ' + escapeHtml(row.seed_id) +
        '<br><div class="muted">state=' + escapeHtml(row.state) + '</div></div>'
      ).join('');
      return (traceRows + pressureRows + seedRows) || '<div class="muted">새 입력 경로 relation 기록 없음</div>';
    }

    edgeModeButtons.forEach(button => {
      button.addEventListener('click', () => {
        edgeMode = button.getAttribute('data-edge-mode');
        edgeModeButtons.forEach(other => other.classList.toggle('active', other === button));
        renderGraph();
      });
    });
    sceneFilter.addEventListener('change', renderGraph);
    observerRoleFilter.addEventListener('change', renderGraph);
    observerSignalFilter.addEventListener('change', renderGraph);
    anchorFilter.addEventListener('change', renderGraph);
    zoomIn.addEventListener('click', () => {
      zoomScale = Math.min(2.4, zoomScale + 0.15);
      applyZoom();
    });
    zoomOut.addEventListener('click', () => {
      zoomScale = Math.max(0.55, zoomScale - 0.15);
      applyZoom();
    });
    zoomReset.addEventListener('click', () => {
      zoomScale = 1;
      applyZoom();
    });
    canvas.addEventListener('pointerdown', pointerDown);
    canvas.addEventListener('wheel', wheelZoom, { passive: false });
    window.addEventListener('pointermove', pointerMove);
    window.addEventListener('pointerup', pointerUp);
    window.addEventListener('resize', () => {
      drawGraph();
    });
    applyZoom();
    updateInspector();
    renderSummaryCards();
    renderCompactSummary();
    renderGraph();
    if (requestedDustId) {
      queryStatus.innerHTML = '';
      const chip = document.createElement('span');
      chip.className = 'graph-chip';
      const requestedNode = nodesById[requestedDustId];
      if (requestedNode) {
        chip.textContent = 'dust selected: ' + requestedDustId;
        selectNode(requestedNode);
      } else {
        chip.textContent = 'requested dust not found: ' + requestedDustId;
      }
      queryStatus.appendChild(chip);
    }
  </script>
</body>
</html>
"""


MAX_SAME_ORIGIN_DISTANCE = 1


def _build_connection_edges(
    dust_nodes: Sequence[Dict[str, object]],
    dust_by_id: Dict[str, Dict[str, object]],
) -> List[Dict[str, object]]:
    candidate_pairs = set()
    anchor_index: Dict[Tuple[str, str], List[str]] = defaultdict(list)
    origin_index: Dict[str, List[str]] = defaultdict(list)
    anchor_frequency: Counter[Tuple[str, str]] = Counter()

    order_in_origin: Dict[str, int] = {}
    for node in dust_nodes:
        for anchor in node["anchors"]:
            anchor_frequency[(anchor["type"], anchor["value"])] += 1
    for node in dust_nodes:
        filtered_anchors = []
        for anchor in normalize_anchor_list(node["anchors"]):
            if not anchor_is_candidate(anchor, anchor_frequency):
                continue
            filtered_anchors.append(anchor)
            anchor_index[(anchor["type"], anchor["value"])].append(node["dust_id"])
        node["candidate_anchors"] = filtered_anchors
        origin_index[node["origin_id"]].append(node["dust_id"])
        order_in_origin[node["dust_id"]] = len(origin_index[node["origin_id"]])

    def add_pairs(group: Iterable[str]) -> None:
        refs = list(dict.fromkeys(group))
        for index, left in enumerate(refs):
            for right in refs[index + 1 :]:
                candidate_pairs.add(tuple(sorted((left, right))))

    for dust_ids in anchor_index.values():
        add_pairs(dust_ids)
    for dust_ids in origin_index.values():
        add_pairs(dust_ids)

    edges: List[Dict[str, object]] = []
    for left_id, right_id in sorted(candidate_pairs):
        left = dust_by_id[left_id]
        right = dust_by_id[right_id]
        profile = build_relation_profile(left, right)
        if not _allow_edge(left, right, profile, order_in_origin):
            continue
        edge_type, score = edge_type_for_profile(profile)
        if edge_type is None:
            continue
        edges.append(
            {
                "edge_id": "edg_%s_%s" % (left_id[-6:], right_id[-6:]),
                "source": left_id,
                "target": right_id,
                "edge_type": edge_type,
                "strength": round(max(1.0, score * 4.0), 2),
                "state": "new" if left["origin_id"] == right["origin_id"] else "active",
                "reasons": edge_reasons_for_profile(profile),
                "scores": profile,
                "color": edge_color(edge_type),
            }
        )
    return edges


def _allow_edge(
    left: Dict[str, object],
    right: Dict[str, object],
    profile: Dict[str, object],
    order_in_origin: Dict[str, int],
) -> bool:
    shared_anchor_count = len(profile["shared_anchors"])
    same_origin = left["origin_id"] == right["origin_id"]

    if same_origin:
        distance = abs(order_in_origin[left["dust_id"]] - order_in_origin[right["dust_id"]])
        return distance <= MAX_SAME_ORIGIN_DISTANCE

    if shared_anchor_count == 0:
        return False

    if profile["anchor_score"] < 0.35:
        return False

    return True



def _build_summary(
    materials: Sequence[Dict[str, object]],
    dust_nodes: Sequence[Dict[str, object]],
    edges: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    return {
        "material_count": len(materials),
        "dust_count": len(dust_nodes),
        "edge_count": len(edges),
        "origin_count": len({node["origin_id"] for node in dust_nodes}),
        "direct_count": sum(1 for edge in edges if edge["edge_type"] == "direct"),
        "weak_count": sum(1 for edge in edges if edge["edge_type"] == "weak"),
        "tension_count": sum(1 for edge in edges if edge["edge_type"] == "tension"),
    }


def _build_top_anchor_summary(dust_nodes: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    counter: Counter[Tuple[str, str]] = Counter()
    for node in dust_nodes:
        for anchor in node["anchors"]:
            counter[(anchor["type"], anchor["value"])] += 1
    return [
        {"type": anchor_type, "value": value, "count": count}
        for (anchor_type, value), count in counter.most_common(20)
    ]


def _build_origin_summaries(dust_nodes: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    grouped: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for node in dust_nodes:
        grouped[node["origin_id"]].append(node)
    rows = []
    for origin_id, group in grouped.items():
        rows.append(
            {
                "origin_id": origin_id,
                "dust_count": len(group),
                "source_type": group[0]["source_type"],
                "source_ref": group[0]["source_ref"],
                "scenes": sorted({node["scene"] for node in group}),
            }
        )
    return sorted(rows, key=lambda row: (-row["dust_count"], row["origin_id"]))


def _top_anchor_values(dust_nodes: Sequence[Dict[str, object]]) -> List[str]:
    counter = Counter()
    for node in dust_nodes:
        for anchor in node["anchors"]:
            counter[anchor["value"]] += 1
    return [value for value, _ in counter.most_common(16)]


def _build_relation_lookup(
    traces: Sequence[Dict[str, object]],
    pressures: Sequence[Dict[str, object]],
    seeds: Sequence[Dict[str, object]],
    origin_preview: Dict[str, List[str]],
) -> Dict[str, Dict[str, object]]:
    lookup: Dict[str, Dict[str, object]] = defaultdict(lambda: {"traces": [], "pressures": [], "seeds": []})
    pressure_by_trace: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for pressure in pressures:
        for support in pressure.get("support_refs", []):
            if support.get("ref_kind") == "trace":
                pressure_by_trace[str(support.get("ref_id"))].append(pressure)

    seed_by_trace: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for seed in seeds:
        for trace_id in seed.get("trace_refs", []):
            seed_by_trace[str(trace_id)].append(seed)

    for trace in traces:
        material_refs = [str(ref) for ref in trace.get("material_refs", [])]
        for material_id in material_refs:
            target_previews: List[str] = []
            for other_id in material_refs:
                if other_id == material_id:
                    continue
                target_previews.extend(origin_preview.get(other_id, [])[:1])
            lookup[material_id]["traces"].append(
                {
                    "trace_id": trace["trace_id"],
                    "evidence_kind": trace.get("evidence_kind", ""),
                    "note": trace.get("note", ""),
                    "target_previews": target_previews[:3],
                }
            )
            for pressure in pressure_by_trace.get(str(trace["trace_id"]), []):
                lookup[material_id]["pressures"].append(
                    {
                        "profile_id": pressure["profile_id"],
                        "axes": [
                            "%s=%.2f" % (axis.get("axis", "unknown"), float(axis.get("strength_hint", 0.0)))
                            for axis in pressure.get("axes", [])
                        ],
                    }
                )
            for seed in seed_by_trace.get(str(trace["trace_id"]), []):
                if material_id not in [str(ref) for ref in seed.get("material_refs", [])]:
                    continue
                lookup[material_id]["seeds"].append(
                    {
                        "seed_id": seed["seed_id"],
                        "state": seed.get("state", ""),
                    }
                )
    return lookup
