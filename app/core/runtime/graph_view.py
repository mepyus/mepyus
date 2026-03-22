from pathlib import Path
import json
from math import ceil, cos, pi, sin
from typing import Dict, List

from app.runtime.file_store import JsonDirectoryStore
from app.runtime.observer import build_reactive_space_observation
from app.runtime.sparse_presence_review import build_sparse_presence_review


STATE_COLORS = {
    "forming": "#0f766e",
    "bridge_exposed": "#b45309",
}


def build_space_graph_view_data(runtime_root: Path) -> Dict[str, object]:
    observation = build_reactive_space_observation(runtime_root)
    sparse_review = build_sparse_presence_review(runtime_root)

    local_space_store = JsonDirectoryStore(runtime_root / "core" / "local_spaces")
    bridge_store = JsonDirectoryStore(runtime_root / "core" / "bridge_traces")
    cell_store = JsonDirectoryStore(runtime_root / "core" / "space_cells")
    material_store = JsonDirectoryStore(runtime_root / "core" / "materials")
    trace_store = JsonDirectoryStore(runtime_root / "core" / "traces")
    space_manifest_store = JsonDirectoryStore(runtime_root / "manifests" / "reactive_spaces")

    local_spaces = {record["local_space_id"]: record for record in local_space_store.read_all()}
    cells = {record["cell_id"]: record for record in cell_store.read_all()}
    materials = {record["material_id"]: record for record in material_store.read_all()}
    traces = {record["trace_id"]: record for record in trace_store.read_all()}
    space_manifests = {
        record["local_space_id"]: record for record in space_manifest_store.read_all()
    }
    quiet_ids = set(sparse_review["quiet_local_space_ids"])

    components = []
    nodes = []
    positions = _layout_components(observation["terrain_components"])
    bridge_records = {
        record["bridge_id"]: record for record in bridge_store.read_all() if record.get("bridge_id")
    }

    for index, component in enumerate(observation["terrain_components"]):
        component_id = "terrain_%02d" % (index + 1)
        component_local_space_ids = component["local_space_ids"]
        component_box = positions[index]
        components.append(
            {
                "component_id": component_id,
                "title": "%s (%s)" % (component["climate_mode"], component["local_space_count"]),
                "climate_mode": component["climate_mode"],
                "rhythm_mode": component["rhythm_mode"],
                "retention_mode": component["retention_mode"],
                "forgetting_mode": component["forgetting_mode"],
                "local_space_ids": component_local_space_ids,
                "x": component_box["x"],
                "y": component_box["y"],
                "width": component_box["width"],
                "height": component_box["height"],
            }
        )
        for local_space_id, x, y in _layout_nodes_in_component(component_local_space_ids, component_box):
            local_space = local_spaces[local_space_id]
            manifest = space_manifests.get(local_space_id, {})
            related_material_ids = _related_material_ids(local_space, cells)
            trace_ids = _related_trace_ids(local_space, cells)
            node = {
                "id": local_space_id,
                "label": _node_label(local_space, cells, materials),
                "state": local_space["state"],
                "component_id": component_id,
                "quiet": local_space_id in quiet_ids,
                "bridge_count": len(local_space.get("bridge_trace_refs", ())),
                "cell_count": len(local_space.get("cell_refs", ())),
                "coexistence_mode": manifest.get("coexistence_mode", "unknown"),
                "pressure_axes": manifest.get("terrain_pressure_axes", []),
                "cell_ids": list(local_space.get("cell_refs", ())),
                "material_ids": related_material_ids,
                "materials": [
                    _material_detail(materials[material_id])
                    for material_id in related_material_ids
                    if material_id in materials
                ],
                "trace_ids": trace_ids,
                "trace_details": [
                    _trace_detail(traces[trace_id]) for trace_id in trace_ids if trace_id in traces
                ],
                "representative_anchors": _normalize_anchor_objects(
                    local_space.get("representative_anchors", [])
                ),
                "supporting_anchors": _normalize_anchor_objects(
                    local_space.get("supporting_anchors", [])
                ),
                "dropped_weak_anchors": _dropped_weak_anchor_state(
                    local_space.get("dropped_weak_anchors")
                ),
                "x": x,
                "y": y,
                "color": STATE_COLORS.get(local_space["state"], "#475569"),
            }
            node["structure"] = _build_structure_layer(node)
            node["interpretation"] = _build_interpretation_layer(node)
            node["observer_compare"] = _build_observer_compare(node)
            nodes.append(node)

    edges = []
    node_degrees = {local_space_id: 0 for local_space_id in local_spaces}
    node_neighbors = {local_space_id: [] for local_space_id in local_spaces}
    for bridge in bridge_records.values():
        left = bridge["from_local_space_id"]
        right = bridge["to_local_space_id"]
        if left not in local_spaces or right not in local_spaces:
            continue
        node_degrees[left] += 1
        node_degrees[right] += 1
        node_neighbors[left].append(
            {
                "local_space_id": right,
                "bridge_id": bridge["bridge_id"],
                "state": bridge["state"],
            }
        )
        node_neighbors[right].append(
            {
                "local_space_id": left,
                "bridge_id": bridge["bridge_id"],
                "state": bridge["state"],
            }
        )
        edges.append(
            {
                "id": bridge["bridge_id"],
                "source": left,
                "target": right,
                "state": bridge["state"],
                "color": "#9a3412" if bridge["state"] == "observed" else "#64748b",
            }
        )

    for node in nodes:
        node["degree"] = node_degrees.get(node["id"], 0)
        node["radius"] = 10 + min(node["degree"], 4) * 2
        node["neighbors"] = node_neighbors.get(node["id"], [])
        node["bridge_reason_summary"] = _build_bridge_reason_summary(
            node["id"],
            node["neighbors"],
            bridge_records,
            local_spaces,
        )

    latest_intake = _build_latest_intake_summary(nodes)
    latest_local_space_ids = set(latest_intake.get("local_space_ids", []))
    for node in nodes:
        node["recent"] = node["id"] in latest_local_space_ids

    return {
        "summary": {
            "local_space_count": len(local_spaces),
            "bridge_count": len(edges),
            "terrain_component_count": len(components),
            "quiet_local_space_count": sparse_review["quiet_local_space_count"],
            "bridge_exposed_local_space_count": sparse_review["bridge_exposed_local_space_count"],
            "forming_local_space_count": sparse_review["forming_local_space_count"],
        },
        "latest_intake": latest_intake,
        "latest_materials": _build_latest_material_rows(nodes, latest_intake),
        "latest_traces": _build_latest_trace_rows(latest_intake, traces, materials),
        "process_summary": observation["process_summary"],
        "components": components,
        "nodes": nodes,
        "edges": edges,
    }


def write_space_graph_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_space_graph_view_data(runtime_root)

    reports_root = runtime_root / "reports"
    reports_root.mkdir(parents=True, exist_ok=True)
    json_path = reports_root / "space_graph_view.json"
    html_path = reports_root / "space_graph_view.html"

    json_path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    html_path.write_text(render_space_graph_view_html(data), encoding="utf-8")
    return {"json_path": json_path, "html_path": html_path}


def _layout_components(components: List[Dict[str, object]]) -> List[Dict[str, int]]:
    boxes = []
    column_count = 4
    x_gap = 32
    y_gap = 32
    base_width = 300
    base_height = 220
    column_heights = [40 for _ in range(column_count)]
    column_width = base_width + x_gap

    for component in components:
        local_count = component["local_space_count"]
        node_columns = min(4, max(1, ceil(local_count ** 0.5)))
        node_rows = ceil(local_count / node_columns)
        width = max(base_width, 120 + node_columns * 96)
        height = max(base_height, 120 + node_rows * 84)
        column_index = min(range(column_count), key=lambda idx: column_heights[idx])
        x = 40 + column_index * column_width
        y = column_heights[column_index]
        boxes.append({"x": x, "y": y, "width": width, "height": height})
        column_heights[column_index] += height + y_gap
    return boxes


def _layout_nodes_in_component(
    local_space_ids: List[str],
    component_box: Dict[str, int],
) -> List[tuple]:
    node_count = len(local_space_ids)
    if node_count == 1:
        return [(
            local_space_ids[0],
            component_box["x"] + component_box["width"] // 2,
            component_box["y"] + component_box["height"] // 2 + 10,
        )]

    if node_count <= 12:
        cx = component_box["x"] + component_box["width"] // 2
        cy = component_box["y"] + component_box["height"] // 2 + 10
        radius = min(component_box["width"], component_box["height"]) // 2 - 58
        positioned = []
        for index, local_space_id in enumerate(local_space_ids):
            angle = ((2 * pi) / node_count) * index - (pi / 2)
            x = int(cx + cos(angle) * radius)
            y = int(cy + sin(angle) * radius)
            positioned.append((local_space_id, x, y))
        return positioned

    node_columns = min(5, max(2, ceil(node_count ** 0.5)))
    x_step = max(82, (component_box["width"] - 92) // node_columns)
    y_step = 86
    positioned = []
    for index, local_space_id in enumerate(local_space_ids):
        row = index // node_columns
        col = index % node_columns
        x = component_box["x"] + 48 + col * x_step
        y = component_box["y"] + 78 + row * y_step
        positioned.append((local_space_id, x, y))
    return positioned


def _node_label(local_space: Dict[str, object], cells: Dict[str, dict], materials: Dict[str, dict]) -> str:
    labels = []
    for cell_id in local_space.get("cell_refs", ()):
        cell = cells.get(cell_id, {})
        for material_id in cell.get("material_refs", ()):
            material = materials.get(material_id, {})
            role = material.get("metadata", {}).get("formation_role")
            if role == "observer_material":
                continue
            label = _material_display_label(material)
            if label and label not in labels:
                labels.append(label)
    if labels:
        primary = labels[0]
    else:
        primary = local_space["local_space_id"][-6:]
    return "%s\n%s" % (primary, local_space["local_space_id"][-6:])


def _material_display_label(material: Dict[str, object]) -> str:
    source_ref = str(material.get("source_ref", ""))
    if source_ref:
        return Path(source_ref).name
    role = material.get("metadata", {}).get("formation_role", "")
    if role:
        return role.replace("_material", "")
    return material["material_id"][-8:]


def _related_material_ids(local_space: Dict[str, object], cells: Dict[str, dict]) -> List[str]:
    material_ids: List[str] = []
    for cell_id in local_space.get("cell_refs", ()):
        cell = cells.get(cell_id, {})
        for material_id in cell.get("material_refs", ()):
            if material_id not in material_ids:
                material_ids.append(material_id)
    return material_ids


def _related_trace_ids(local_space: Dict[str, object], cells: Dict[str, dict]) -> List[str]:
    trace_ids: List[str] = []
    for cell_id in local_space.get("cell_refs", ()):
        cell = cells.get(cell_id, {})
        for trace_id in cell.get("trace_refs", ()):
            if trace_id not in trace_ids:
                trace_ids.append(trace_id)
    return trace_ids


def _normalize_anchor_objects(values: List[object]) -> List[Dict[str, str]]:
    normalized: List[Dict[str, str]] = []
    seen = set()
    for value in values or []:
        if isinstance(value, dict):
            label = str(value.get("display_label") or value.get("value") or "").strip()
            canonical_key = str(value.get("canonical_key") or label).strip()
            anchor_type = str(value.get("anchor_type") or value.get("type") or "semantic").strip() or "semantic"
        else:
            label = str(value).strip()
            canonical_key = label.lower().replace(" ", "_")
            anchor_type = "semantic"
        if not label or not canonical_key:
            continue
        key = (canonical_key, label, anchor_type)
        if key in seen:
            continue
        seen.add(key)
        normalized.append(
            {
                "canonical_key": canonical_key,
                "display_label": label,
                "anchor_type": anchor_type,
            }
        )
    return normalized


def _dropped_weak_anchor_state(value: object) -> Dict[str, object]:
    if value is None:
        return {"available": False, "items": []}
    items = [str(item).strip() for item in (value or []) if str(item).strip()]
    return {"available": True, "items": items[:10]}


def _build_observer_compare(node: Dict[str, object]) -> Dict[str, object]:
    materials = list(node.get("materials", []))
    role = ""
    ambiguity = None
    confidence = None
    signals: List[str] = []
    for material in materials:
        if not role and material.get("observer_role"):
            role = str(material.get("observer_role", ""))
        if ambiguity is None and material.get("observer_ambiguity") is not None:
            ambiguity = material.get("observer_ambiguity")
        if confidence is None and material.get("observer_confidence_numeric") is not None:
            confidence = material.get("observer_confidence_numeric")
        for signal in material.get("observer_signals", []) or []:
            if signal and signal not in signals:
                signals.append(str(signal))
    return {
        "available": False,
        "merged": {
            "observer_role": role,
            "observer_ambiguity": ambiguity,
            "observer_confidence_numeric": confidence,
            "observer_signals": signals,
        },
        "note": "raw observer compare not available yet",
    }


def _build_bridge_reason_summary(
    local_space_id: str,
    neighbors: List[Dict[str, object]],
    bridge_records: Dict[str, Dict[str, object]],
    local_spaces: Dict[str, Dict[str, object]],
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for neighbor in neighbors:
        bridge_id = str(neighbor.get("bridge_id", "")).strip()
        if not bridge_id:
            continue
        bridge = bridge_records.get(bridge_id, {})
        peer_local_space_id = str(neighbor.get("local_space_id", "")).strip()
        peer_space = local_spaces.get(peer_local_space_id, {})
        shared_anchors = _normalize_anchor_objects(bridge.get("shared_anchors", []))
        anchor_hints = [row["display_label"] for row in shared_anchors[:4]]
        note = str(bridge.get("note", "")).strip()
        if anchor_hints:
            reason_line = "%s와 %s 축으로 연결" % (
                str(peer_space.get("source_label") or peer_local_space_id),
                " / ".join(anchor_hints[:2]),
            )
        elif note:
            reason_line = note
        else:
            reason_line = "bridge trace recorded"
        rows.append(
            {
                "peer_local_space_id": peer_local_space_id,
                "peer_label": str(peer_space.get("source_label") or peer_local_space_id),
                "anchor_hints": anchor_hints,
                "bridge_ids": [bridge_id],
                "reason_line": reason_line,
                "state": str(bridge.get("state", neighbor.get("state", ""))),
            }
        )
    return rows[:6]


def _material_detail(material: Dict[str, object]) -> Dict[str, object]:
    metadata = material.get("metadata", {})
    fragment_metadata = metadata.get("fragment_metadata", {})
    payload = str(material.get("raw_payload", ""))
    return {
        "material_id": material["material_id"],
        "display_label": _material_display_label(material),
        "formation_role": metadata.get("formation_role", "unknown"),
        "source_type": material.get("source_type", "unknown"),
        "source_ref": material.get("source_ref", ""),
        "family_id": material.get("family_id", ""),
        "session_id": material.get("session_id", ""),
        "actor_id": material.get("actor_id", ""),
        "created_at": material.get("created_at", ""),
        "lineage_refs": list(material.get("lineage_refs", ())),
        "excerpt": payload[:220],
        "raw_payload": payload,
        "source_document_id": metadata.get("source_document_id", ""),
        "run_id": metadata.get("run_id", ""),
        "bridge_id": metadata.get("bridge_id", ""),
        "event_id": metadata.get("event_id", ""),
        "fragment_id": metadata.get("fragment_id", ""),
        "candidate_id": metadata.get("candidate_id", ""),
        "fragment_count": metadata.get("fragment_count", 0),
        "candidate_count": metadata.get("candidate_count", 0),
        "bridge_count": metadata.get("bridge_count", 0),
        "bridge_status": metadata.get("bridge_status", ""),
        "bridge_status_reason": metadata.get("bridge_status_reason", ""),
        "decomposition_kind": metadata.get("decomposition_kind", ""),
        "scene_index": metadata.get("scene_index", 0),
        "block_label": metadata.get("block_label", "plain"),
        "axes": dict(metadata.get("axes", {})),
        "connectivity_keys": list(metadata.get("connectivity_keys", [])),
        "source_note_path": metadata.get("source_note_path", ""),
        "source_content_hash": metadata.get("source_content_hash", ""),
        "observer_role": fragment_metadata.get("observer_role", ""),
        "observer_ambiguity": fragment_metadata.get("observer_ambiguity"),
        "observer_confidence_numeric": fragment_metadata.get("observer_confidence_numeric"),
        "observer_signals": list(fragment_metadata.get("observer_signals", [])),
    }


def _build_latest_intake_summary(nodes: List[Dict[str, object]]) -> Dict[str, object]:
    material_rows = []
    for node in nodes:
        for material in node.get("materials", []):
            created_at = str(material.get("created_at", ""))
            if created_at:
                material_rows.append((created_at, node["id"], material))

    if not material_rows:
        return {
            "source_ref": "",
            "created_at": "",
            "material_count": 0,
            "local_space_ids": [],
            "candidate_ids": [],
        }

    material_rows.sort(key=lambda row: row[0], reverse=True)
    latest_created_at, _, latest_material = material_rows[0]
    latest_source_ref = str(latest_material.get("source_ref", ""))

    local_space_ids = []
    candidate_ids = []
    material_count = 0
    for created_at, local_space_id, material in material_rows:
        if str(material.get("source_ref", "")) != latest_source_ref:
            continue
        material_count += 1
        if local_space_id not in local_space_ids:
            local_space_ids.append(local_space_id)
        candidate_id = str(material.get("candidate_id", ""))
        if candidate_id and candidate_id not in candidate_ids:
            candidate_ids.append(candidate_id)

    return {
        "source_ref": latest_source_ref,
        "created_at": latest_created_at,
        "material_count": material_count,
        "local_space_ids": local_space_ids,
        "candidate_ids": candidate_ids,
    }


def _build_latest_material_rows(
    nodes: List[Dict[str, object]],
    latest_intake: Dict[str, object],
) -> List[Dict[str, object]]:
    latest_source_ref = str(latest_intake.get("source_ref", ""))
    if not latest_source_ref:
        return []

    rows = []
    for node in nodes:
        for material in node.get("materials", []):
            if str(material.get("source_ref", "")) != latest_source_ref:
                continue
            rows.append(
                {
                    "material_id": material.get("material_id", ""),
                    "display_label": material.get("display_label", ""),
                    "source_ref": material.get("source_ref", ""),
                    "source_type": material.get("source_type", ""),
                    "candidate_id": material.get("candidate_id", ""),
                    "bridge_id": material.get("bridge_id", ""),
                    "run_id": material.get("run_id", ""),
                    "fragment_id": material.get("fragment_id", ""),
                    "event_id": material.get("event_id", ""),
                    "source_document_id": material.get("source_document_id", ""),
                    "fragment_count": material.get("fragment_count", 0),
                    "candidate_count": material.get("candidate_count", 0),
                    "bridge_count": material.get("bridge_count", 0),
                    "bridge_status": material.get("bridge_status", ""),
                    "bridge_status_reason": material.get("bridge_status_reason", ""),
                    "source_note_path": material.get("source_note_path", ""),
                    "source_content_hash": material.get("source_content_hash", ""),
                    "local_space_id": node.get("id", ""),
                    "local_space_label": node.get("label", ""),
                    "raw_payload": material.get("raw_payload", ""),
                }
            )
    rows.sort(key=lambda row: (str(row.get("candidate_index", "")), str(row.get("material_id", ""))))
    return rows


def _build_latest_trace_rows(
    latest_intake: Dict[str, object],
    traces: Dict[str, dict],
    materials: Dict[str, dict],
) -> List[Dict[str, object]]:
    latest_source_ref = str(latest_intake.get("source_ref", ""))
    if not latest_source_ref:
        return []

    latest_material_ids = {
        material_id
        for material_id, material in materials.items()
        if str(material.get("source_ref", "")) == latest_source_ref
    }
    if not latest_material_ids:
        return []

    rows = []
    for trace in traces.values():
        material_refs = list(trace.get("material_refs", ()))
        if not latest_material_ids.intersection(material_refs):
            continue
        related_materials = []
        related_source_refs = []
        for material_id in material_refs:
            material = materials.get(material_id)
            if not material:
                continue
            source_ref = str(material.get("source_ref", ""))
            if source_ref and source_ref not in related_source_refs:
                related_source_refs.append(source_ref)
            related_materials.append(
                {
                    "material_id": material_id,
                    "source_ref": source_ref,
                    "display_label": _material_display_label(material),
                    "block_label": material.get("metadata", {}).get("block_label", "plain"),
                    "scene_index": material.get("metadata", {}).get("scene_index", 0),
                }
            )
        rows.append(
            {
                "trace_id": trace["trace_id"],
                "created_at": trace.get("created_at", ""),
                "evidence_kind": trace.get("evidence_kind", "unknown"),
                "note": trace.get("note", ""),
                "material_refs": material_refs,
                "support_refs": list(trace.get("support_refs", ())),
                "related_source_refs": related_source_refs,
                "cross_source_ref_count": len(related_source_refs),
                "cross_context": len(related_source_refs) > 1,
                "related_materials": related_materials,
            }
        )

    rows.sort(key=lambda row: str(row.get("created_at", "")), reverse=True)
    return rows


def _trace_detail(trace: Dict[str, object]) -> Dict[str, object]:
    return {
        "trace_id": trace["trace_id"],
        "created_at": trace.get("created_at", ""),
        "evidence_kind": trace.get("evidence_kind", "unknown"),
        "note": trace.get("note", ""),
        "material_refs": list(trace.get("material_refs", ())),
        "support_refs": list(trace.get("support_refs", ())),
    }


def _state_label(state: str) -> str:
    labels = {
        "forming": "형성 중",
        "bridge_exposed": "브리지 노출",
    }
    return labels.get(state, state)


def _build_structure_layer(node: Dict[str, object]) -> Dict[str, str]:
    quiet = node.get("quiet", False)
    bridge_count = node.get("bridge_count", 0)
    pressure_axes = node.get("pressure_axes", [])

    if bridge_count:
        relation_state = "관계 흔적이 드러난 공간"
    elif quiet:
        relation_state = "조용히 유지되는 공간"
    else:
        relation_state = "아직 확정되지 않은 형성 공간"

    if pressure_axes:
        axis_summary = ", ".join(str(axis) for axis in pressure_axes)
    else:
        axis_summary = "드러난 압력축 없음"

    return {
        "state_label": _state_label(str(node.get("state", "unknown"))),
        "relation_state_label": relation_state,
        "quiet_label": "조용한 공간" if quiet else "노출/형성 공간",
        "axis_summary": axis_summary,
    }


def _build_interpretation_layer(node: Dict[str, object]) -> Dict[str, str]:
    materials = node.get("materials", [])
    traces = node.get("trace_details", [])
    quiet = node.get("quiet", False)
    bridge_count = node.get("bridge_count", 0)

    display_labels = [
        material.get("display_label", material.get("material_id", "")) for material in materials[:3]
    ]
    material_summary = ", ".join(label for label in display_labels if label) or "unlabeled residue"

    evidence_kinds = []
    for trace in traces:
        evidence_kind = trace.get("evidence_kind", "")
        if evidence_kind and evidence_kind not in evidence_kinds:
            evidence_kinds.append(evidence_kind)
    evidence_summary = ", ".join(evidence_kinds[:3]) or "quiet persistence"

    if bridge_count:
        field_kind = "관계 감응 해석층"
        quiet_reason = (
            "이 공간은 자기 자리를 유지하고 있지만, 인접 공간을 향한 약한 노출 흔적도 함께 지니고 있습니다."
        )
    elif quiet:
        field_kind = "정지 유지 해석층"
        quiet_reason = (
            "이 공간은 현재 브리지 노출 상태가 아니므로, 눈에 띄는 관계 압력 없이 조용히 유지되고 있습니다."
        )
    else:
        field_kind = "형성 진행 해석층"
        quiet_reason = (
            "이 공간은 아직 형성 중이며, 조용한 유지 상태나 브리지 노출 상태로 완전히 굳어지지 않았습니다."
        )

    if len(materials) > 1:
        why_grouped = (
            "현재의 trace 근거가 이 재료들을 하나의 형성 포켓 안에 붙들고 있어서, 같은 로컬 공간 안에서 함께 읽히고 있습니다."
        )
    else:
        why_grouped = (
            "이 로컬 공간은 주로 하나의 재료 선을 싣고 있어서, 묶임이 아직 좁고 자립적인 편입니다."
        )

    if bridge_count:
        relation_reason = (
            "여기서는 이미 약한 브리지 노출이 보여서, 이 공간이 다른 지형으로 무너지지 않은 채 관계가 떠오르고 있습니다."
        )
    else:
        relation_reason = (
            "현재는 브리지 노출이 보이지 않으므로, 관계는 아직 희박하거나 늦게 오거나 아직 떠오르지 않은 상태입니다."
        )

    return {
        "field_kind": field_kind,
        "material_summary": material_summary,
        "evidence_summary": evidence_summary,
        "why_grouped": why_grouped,
        "relation_reason": relation_reason,
        "quiet_reason": quiet_reason,
    }


def render_space_graph_view_html(data: Dict[str, object], interactive: bool = False) -> str:
    payload = json.dumps(data, ensure_ascii=True)
    intake_panel = _render_intake_panel() if interactive else ""
    interactive_script = _render_interactive_script() if interactive else ""
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>VectorFL Next 공간 뷰어</title>
  <style>
    :root {
      --bg: #f6f1e8;
      --ink: #1f2937;
      --muted: #6b7280;
      --panel: #fffaf2;
      --line: #d6cbb7;
      --quiet: #f3e6c9;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--ink);
      background: radial-gradient(circle at top, #fff7eb, var(--bg) 52%);
    }
    .page {
      display: grid;
      grid-template-columns: 320px 1fr;
      min-height: 100vh;
    }
    .sidebar {
      border-right: 1px solid var(--line);
      background: rgba(255,250,242,0.92);
      padding: 24px 20px;
      overflow: auto;
      backdrop-filter: blur(6px);
    }
    .sidebar h1 { margin: 0 0 12px; font-size: 24px; }
    .sidebar p { margin: 0 0 18px; line-height: 1.45; color: var(--muted); }
    .metric {
      padding: 12px 14px;
      margin-bottom: 10px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
    }
    .metric strong { display: block; font-size: 22px; }
    .metric small {
      display: block;
      margin-top: 2px;
      color: var(--muted);
      font-size: 11px;
    }
    .legend-item {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 8px 0;
      color: var(--muted);
    }
    .swatch {
      width: 14px;
      height: 14px;
      border-radius: 999px;
      border: 1px solid rgba(0,0,0,0.12);
    }
    .viewer {
      position: relative;
      overflow: auto;
      padding: 24px;
    }
    .viewer-shell {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 380px;
      gap: 18px;
      align-items: start;
    }
    .viewer-main {
      min-width: 0;
    }
    .bottom-panels {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      margin-top: 16px;
    }
    .bottom-panel {
      min-width: 0;
      padding: 16px;
      background: rgba(255,250,242,0.94);
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: 0 10px 24px rgba(73, 52, 33, 0.06);
    }
    .bottom-panel h2 {
      margin: 0 0 10px;
      font-size: 16px;
    }
    .inspector-rail {
      position: sticky;
      top: 24px;
      display: grid;
      gap: 14px;
    }
    .inspector-card {
      padding: 16px;
      background: rgba(255,250,242,0.96);
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: 0 10px 26px rgba(73, 52, 33, 0.08);
    }
    .inspector-card h2 {
      margin: 0 0 8px;
      font-size: 18px;
    }
    .inspector-card h3 {
      margin: 0 0 8px;
      font-size: 14px;
      color: #6d4c2f;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .inspector-card p,
    .inspector-card li {
      margin: 0 0 7px;
      color: var(--muted);
      line-height: 1.45;
      font-size: 12px;
    }
    .inspector-card .chips {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 8px 0 12px;
    }
    .inspector-card .chip {
      background: #efe4d2;
      border-radius: 999px;
      padding: 4px 8px;
      font-size: 12px;
      color: var(--ink);
    }
    .compact-shelf {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
      margin-bottom: 14px;
    }
    .compact-card {
      padding: 10px 12px;
      background: #fff8ef;
      border: 1px solid var(--line);
      border-radius: 12px;
    }
    .compact-card h4 {
      margin: 0 0 8px;
      font-size: 12px;
      color: #6d4c2f;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .compact-card p {
      margin: 0 0 6px;
      font-size: 12px;
      color: var(--muted);
      line-height: 1.4;
    }
    .compact-card .chips {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin: 0;
    }
    .inspector-actions {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }
    .inspector-actions button,
    .inspector-actions a {
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 999px;
      padding: 8px 12px;
      cursor: pointer;
      text-decoration: none;
      font-size: 12px;
    }
    .toolbar {
      position: sticky;
      top: 0;
      display: flex;
      gap: 10px;
      align-items: center;
      justify-content: space-between;
      z-index: 2;
      margin-bottom: 12px;
    }
    .toolbar-actions {
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }
    .toolbar button {
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 999px;
      padding: 8px 12px;
      cursor: pointer;
    }
    .toolbar button.active {
      background: #ead8b5;
      border-color: #c8a96b;
    }
    .canvas-wrap {
      position: relative;
      width: 1480px;
      min-height: 1600px;
      transform-origin: top left;
    }
    .viewer-panel {
      display: block;
    }
    .material-list {
      display: grid;
      gap: 14px;
      max-height: 460px;
      overflow: auto;
    }
    .material-list-card {
      padding: 16px;
      background: rgba(255,250,242,0.92);
      border: 1px solid var(--line);
      border-radius: 18px;
      cursor: pointer;
    }
    .material-list-card.selected {
      border-color: #8b5e34;
      box-shadow: 0 12px 24px rgba(73, 52, 33, 0.10);
    }
    .material-list-card h3 {
      margin: 0 0 8px;
      font-size: 15px;
    }
    .material-list-card p {
      margin: 0 0 8px;
      color: var(--muted);
      line-height: 1.45;
      font-size: 12px;
    }
    .material-list-raw {
      max-height: 220px;
      overflow: auto;
      padding: 10px;
      white-space: pre-wrap;
      color: #334155;
      background: #f8f4ec;
      border: 1px solid rgba(214,203,183,0.82);
      border-radius: 12px;
    }
    .component {
      position: absolute;
      border: 1px dashed rgba(214,203,183,0.95);
      border-radius: 20px;
      background: rgba(255,250,242,0.34);
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.35);
      padding: 14px;
      transition: opacity 160ms ease, border-color 160ms ease, background 160ms ease;
    }
    .component h3 {
      margin: 0 0 4px;
      font-size: 15px;
    }
    .component p {
      margin: 0;
      color: var(--muted);
      font-size: 12px;
    }
    svg.edges {
      position: absolute;
      inset: 0;
      overflow: visible;
    }
    .edge-label {
      font-size: 10px;
      fill: #7c2d12;
      opacity: 0.75;
      pointer-events: none;
    }
    .node {
      position: absolute;
      width: 96px;
      margin-left: -48px;
      margin-top: -24px;
      text-align: center;
      pointer-events: auto;
    }
    .node-dot {
      width: 22px;
      height: 22px;
      border-radius: 999px;
      margin: 0 auto 6px;
      border: 2px solid rgba(0,0,0,0.18);
      background: #475569;
      transition: transform 140ms ease;
    }
    .node.quiet .node-dot {
      box-shadow: 0 0 0 6px rgba(243,230,201,0.9);
    }
    .node:hover .node-dot {
      transform: scale(1.18);
    }
    .node.recent .node-dot {
      box-shadow: 0 0 0 4px rgba(15,118,110,0.18), 0 0 0 10px rgba(234,216,181,0.82);
    }
    .node.selected .node-dot {
      box-shadow: 0 0 0 4px rgba(139,94,52,0.18), 0 0 0 10px rgba(234,216,181,0.92);
      transform: scale(1.14);
    }
    .node-label {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-size: 11px;
      line-height: 1.15;
      color: var(--ink);
      background: rgba(255,250,242,0.85);
      border: 1px solid rgba(214,203,183,0.7);
      border-radius: 10px;
      padding: 4px 6px;
    }
    .node-subtle {
      margin-top: 4px;
      font-size: 10px;
      color: var(--muted);
    }
    .footer-note {
      margin-top: 18px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.45;
    }
    .canvas-wrap.relation-mode .component {
      opacity: 0.18;
      background: rgba(255,250,242,0.12);
      border-color: rgba(148,163,184,0.45);
    }
    .canvas-wrap.relation-mode .node-label {
      border-color: rgba(154,52,18,0.35);
    }
    .canvas-wrap.terrain-mode .component {
      opacity: 0.95;
      background: rgba(255,250,242,0.72);
    }
    .canvas-wrap.terrain-mode svg.edges line,
    .canvas-wrap.terrain-mode svg.edges path,
    .canvas-wrap.terrain-mode svg.edges text {
      opacity: 0.22;
    }
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(31,41,55,0.34);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
      z-index: 10;
    }
    .modal-backdrop.open {
      display: flex;
    }
    .modal-card {
      width: min(920px, 100%);
      max-height: 86vh;
      overflow: auto;
      background: #fffaf2;
      border: 1px solid var(--line);
      border-radius: 22px;
      box-shadow: 0 18px 60px rgba(15,23,42,0.18);
      padding: 22px 22px 18px;
    }
    .modal-head {
      display: flex;
      justify-content: space-between;
      align-items: start;
      gap: 16px;
      margin-bottom: 14px;
    }
    .modal-head h2 {
      margin: 0 0 6px;
      font-size: 22px;
    }
    .modal-head p {
      margin: 0;
      color: var(--muted);
      line-height: 1.4;
      font-size: 13px;
    }
    .modal-close {
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 999px;
      padding: 8px 12px;
      cursor: pointer;
    }
    .modal-grid {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 18px;
    }
    .camera-tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 14px;
    }
    .camera-tab {
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--ink);
      border-radius: 999px;
      padding: 8px 12px;
      cursor: pointer;
    }
    .camera-tab.active {
      background: #ead8b5;
      border-color: #c8a96b;
    }
    .camera-panel {
      display: none;
    }
    .camera-panel.active {
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 18px;
    }
    .intake-modal-card {
      width: min(560px, 100%);
    }
    .intake-form label {
      display: block;
      margin-bottom: 10px;
      font-size: 12px;
    }
    .intake-form select,
    .intake-form textarea {
      width: 100%;
      margin-top: 4px;
      padding: 8px;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: #fffdf8;
    }
    .intake-form textarea {
      resize: vertical;
    }
    .intake-status {
      margin: 10px 0 0;
      font-size: 12px;
      color: var(--muted);
      min-height: 18px;
    }
    .reading-summary {
      margin-bottom: 14px;
      padding: 14px 16px;
      background: #f8efdf;
      border: 1px solid rgba(200,169,107,0.58);
      border-radius: 16px;
    }
    .reading-summary h3 {
      margin: 0 0 8px;
      font-size: 15px;
    }
    .reading-summary p {
      margin: 0 0 7px;
      color: #475569;
      line-height: 1.45;
      font-size: 13px;
    }
    .modal-section {
      padding: 14px;
      background: #fffdf8;
      border: 1px solid rgba(214,203,183,0.82);
      border-radius: 16px;
    }
    .modal-section h3 {
      margin: 0 0 8px;
      font-size: 14px;
    }
    .modal-section p,
    .modal-section li {
      margin: 0 0 7px;
      color: var(--muted);
      line-height: 1.45;
      font-size: 12px;
    }
    .modal-section .chips {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 8px 0 12px;
    }
    .modal-section .chip {
      background: #efe4d2;
      border-radius: 999px;
      padding: 4px 8px;
      font-size: 12px;
      color: var(--ink);
    }
    .modal-section a {
      color: #6d4c2f;
      text-decoration: none;
    }
    .modal-section ul {
      margin: 0;
      padding-left: 16px;
    }
    .modal-section code {
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      color: #7c2d12;
    }
    .material-card {
      padding: 10px 0 12px;
      border-top: 1px solid rgba(214,203,183,0.72);
    }
    .material-card:first-child {
      border-top: 0;
      padding-top: 0;
    }
    .material-card strong {
      display: block;
      margin-bottom: 4px;
      font-size: 13px;
      color: var(--ink);
    }
    .material-body {
      white-space: pre-wrap;
      color: #334155;
    }
    .material-raw {
      margin-top: 8px;
      max-height: 280px;
      overflow: auto;
      padding: 10px;
      white-space: pre-wrap;
      color: #334155;
      background: #f8f4ec;
      border: 1px solid rgba(214,203,183,0.82);
      border-radius: 12px;
    }
    .material-compare {
      padding: 10px 0 12px;
      border-top: 1px solid rgba(214,203,183,0.72);
    }
    .material-compare:first-child {
      border-top: 0;
      padding-top: 0;
    }
    .material-compare strong {
      display: block;
      margin-bottom: 4px;
      font-size: 13px;
      color: var(--ink);
    }
    @media (max-width: 1180px) {
      .viewer-shell {
        grid-template-columns: 1fr;
      }
      .inspector-rail {
        position: static;
      }
      .bottom-panels {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <aside class="sidebar">
      <h1>공간 뷰어</h1>
      <p>현재 런타임을 로컬 공간 중심으로 읽는 뷰어입니다. 이 화면은 설명용이며, 최종 폐쇄보다 먼저 넓어진 공간 상태를 보여줍니다.</p>
      <div class="metric"><span>로컬 공간 수</span><strong id="metric-local"></strong></div>
      <div class="metric"><span>조용한 로컬 공간</span><strong id="metric-quiet"></strong><small>브리지 없이 서 있는 공간</small></div>
      <div class="metric"><span>브리지 노출 공간</span><strong id="metric-bridge-exposed"></strong><small>노출 흔적을 지닌 로컬 공간</small></div>
      <div class="metric"><span>형성 중인 공간</span><strong id="metric-forming"></strong><small>아직 브리지 노출 전이며 계속 넓어지거나 머무는 공간</small></div>
      <div class="metric"><span>브리지 흔적 수</span><strong id="metric-bridge"></strong></div>
      <div class="metric"><span>지형 컴포넌트 수</span><strong id="metric-terrain"></strong></div>
      <div class="metric"><span>프로세스</span><strong id="metric-process" style="font-size:16px"></strong></div>
      <div class="metric">
        <span>최근 유입</span>
        <strong id="metric-latest" style="font-size:14px; line-height:1.35"></strong>
        <small id="metric-latest-sub"></small>
      </div>
      <h3>범례</h3>
      <div class="legend-item"><span class="swatch" style="background:#0f766e"></span> 형성 중인 로컬 공간</div>
      <div class="legend-item"><span class="swatch" style="background:#b45309"></span> 브리지 노출 로컬 공간</div>
      <div class="legend-item"><span class="swatch" style="background:#475569"></span> 기타 상태</div>
      <div class="legend-item"><span class="swatch" style="background:#f3e6c9"></span> 조용한 오라</div>
      <div class="footer-note">
        이 그래프는 공간의 모양을 먼저 보여줍니다. 브리지 선은 병합선이 아니라 노출 흔적입니다. 노드를 누르면 재료 내용과 관계 맥락을 별도 검사 모달에서 확인할 수 있습니다.
      </div>
    </aside>
    <main class="viewer">
      <div class="viewer-shell">
        <div class="viewer-main">
          <div class="toolbar">
            <div class="toolbar-actions">
              <button id="zoom-out">-</button>
              <button id="zoom-in">+</button>
              <button id="zoom-reset">초기화</button>
              <button id="mode-balanced" class="active">그래프</button>
              <button id="mode-relation">관계 보기</button>
              <button id="mode-terrain">지형 보기</button>
            </div>
            <div class="toolbar-actions">""" + intake_panel + """</div>
          </div>
          <div id="panel-graph" class="viewer-panel active">
            <div id="canvas" class="canvas-wrap">
              <svg class="edges" id="edges"></svg>
            </div>
          </div>
          <div class="bottom-panels">
            <section class="bottom-panel">
              <h2>Latest Materials</h2>
              <div id="panel-latest-materials" class="viewer-panel">
                <section id="latest-materials-list" class="material-list"></section>
              </div>
            </section>
            <section class="bottom-panel">
              <h2>Latest Traces</h2>
              <div id="panel-traces" class="viewer-panel">
                <section id="latest-traces-list" class="material-list"></section>
              </div>
            </section>
          </div>
        </div>
        <aside class="inspector-rail">
          <section class="inspector-card">
            <h2 id="inspector-title">Operator Inspector</h2>
            <p id="inspector-subtitle">local space를 선택하면 Summary / Why / Anchors / Evidence / Compare가 여기에 고정됩니다.</p>
            <div class="inspector-actions">
              <button id="inspector-open-modal" type="button">상세 모달</button>
            </div>
          </section>
          <section id="node-inspector" class="inspector-card">
            <div class="muted">선택된 local space가 없습니다.</div>
          </section>
        </aside>
      </div>
    </main>
  </div>
  <div id="modal-backdrop" class="modal-backdrop">
    <div class="modal-card">
      <div class="modal-head">
        <div>
          <h2 id="modal-title">공간 상세</h2>
          <p id="modal-subtitle">노드를 선택하면 재료 내용, trace 근거, 브리지 관계 맥락을 확인할 수 있습니다.</p>
        </div>
        <button id="modal-close" class="modal-close">닫기</button>
      </div>
      <div id="modal-body" class="modal-grid"></div>
    </div>
  </div>
  <div id="intake-backdrop" class="modal-backdrop">
    <div class="modal-card intake-modal-card">
      <div class="modal-head">
        <div>
          <h2>입력 투입</h2>
          <p>유형과 내용만 넣으면 제목은 자동으로 생성됩니다.</p>
        </div>
        <button id="intake-close" class="modal-close">닫기</button>
      </div>
      <form id="intake-form" class="intake-form">
        <label>입력 종류
          <select name="source_type">
            <option value="memo">메모</option>
            <option value="paper">논문</option>
            <option value="review">리뷰</option>
            <option value="code">코드</option>
          </select>
        </label>
        <label>내용
          <textarea name="raw_payload" rows="10" placeholder="공간에 넣을 내용을 적으세요."></textarea>
        </label>
        <button type="submit" style="width:100%; border:1px solid #c8a96b; background:#ead8b5; color:var(--ink); border-radius:999px; padding:10px 14px; cursor:pointer;">공간에 투입</button>
        <p id="intake-status" class="intake-status"></p>
      </form>
    </div>
  </div>
  <script id="graph-data" type="application/json">""" + payload + """</script>
  <script>
    const data = JSON.parse(document.getElementById('graph-data').textContent);
    const canvas = document.getElementById('canvas');
    const edgesSvg = document.getElementById('edges');
    const graphPanel = document.getElementById('panel-graph');
    const latestMaterialsPanel = document.getElementById('panel-latest-materials');
    const latestMaterialsList = document.getElementById('latest-materials-list');
    const tracePanel = document.getElementById('panel-traces');
    const latestTracesList = document.getElementById('latest-traces-list');
    const modalBackdrop = document.getElementById('modal-backdrop');
    const intakeBackdrop = document.getElementById('intake-backdrop');
    const modalTitle = document.getElementById('modal-title');
    const modalSubtitle = document.getElementById('modal-subtitle');
    const modalBody = document.getElementById('modal-body');
    const inspectorTitle = document.getElementById('inspector-title');
    const inspectorSubtitle = document.getElementById('inspector-subtitle');
    const inspectorBody = document.getElementById('node-inspector');
    const inspectorOpenModal = document.getElementById('inspector-open-modal');
    const summary = data.summary;
    document.getElementById('metric-local').textContent = summary.local_space_count;
    document.getElementById('metric-quiet').textContent = summary.quiet_local_space_count;
    document.getElementById('metric-bridge-exposed').textContent = summary.bridge_exposed_local_space_count;
    document.getElementById('metric-forming').textContent = summary.forming_local_space_count;
    document.getElementById('metric-bridge').textContent = summary.bridge_count;
    document.getElementById('metric-terrain').textContent = summary.terrain_component_count;
    document.getElementById('metric-process').textContent = data.process_summary.summary_line;
    const latestIntake = data.latest_intake || {};
    const latestMaterials = data.latest_materials || [];
    const latestTraces = data.latest_traces || [];
    let selectedMaterialId = '';
    let selectedTraceId = '';
    let selectedNodeId = '';
    document.getElementById('metric-latest').textContent =
      latestIntake.source_ref || '아직 없음';
    document.getElementById('metric-latest-sub').textContent =
      latestIntake.source_ref
        ? 'material ' + String(latestIntake.material_count || 0) + '개 / local space ' + String((latestIntake.local_space_ids || []).length) + '개'
        : '최근 유입 없음';

    const nodeById = {};
    data.components.forEach(component => {
      const box = document.createElement('section');
      box.className = 'component';
      box.style.left = component.x + 'px';
      box.style.top = component.y + 'px';
      box.style.width = component.width + 'px';
      box.style.height = component.height + 'px';
      box.innerHTML = '<h3>' + component.title + '</h3><p>' + component.rhythm_mode + ' / ' + component.retention_mode + '</p>';
      canvas.appendChild(box);
    });

    data.nodes.forEach(node => {
      nodeById[node.id] = node;
      const el = document.createElement('div');
      el.className = 'node' + (node.quiet ? ' quiet' : '') + (node.recent ? ' recent' : '');
      el.setAttribute('data-node-id', node.id);
      el.style.left = node.x + 'px';
      el.style.top = node.y + 'px';
      const observerRoles = Array.from(new Set((node.materials || []).map(material => material.observer_role).filter(Boolean)));
      const observerSignals = Array.from(new Set((node.materials || []).flatMap(material => material.observer_signals || []).filter(Boolean)));
      el.title = node.id + '\\nstate=' + node.state + '\\ncoexistence=' + node.coexistence_mode + '\\naxes=' + node.pressure_axes.join(', ') +
        (observerRoles.length ? '\\nobserver_roles=' + observerRoles.join(', ') : '') +
        (observerSignals.length ? '\\nobserver_signals=' + observerSignals.join(', ') : '');
      const dot = document.createElement('div');
      dot.className = 'node-dot';
      dot.style.background = node.color;
      dot.style.width = node.radius * 2 + 'px';
      dot.style.height = node.radius * 2 + 'px';
      const label = document.createElement('div');
      label.className = 'node-label';
      label.textContent = node.label;
      const subtle = document.createElement('div');
      subtle.className = 'node-subtle';
      subtle.textContent = (node.structure && node.structure.relation_state_label) || (node.quiet ? '조용한 공간' : node.state);
      el.appendChild(dot);
      el.appendChild(label);
      el.appendChild(subtle);
      el.onclick = () => selectNode(node);
      el.ondblclick = () => openModal(node);
      canvas.appendChild(el);
    });

    const width = 1480;
    const height = Math.max(1800, ...data.components.map(c => c.y + c.height + 40));
    canvas.style.height = height + 'px';
    edgesSvg.setAttribute('width', width);
    edgesSvg.setAttribute('height', height);

    data.edges.forEach(edge => {
      const source = nodeById[edge.source];
      const target = nodeById[edge.target];
      if (!source || !target) return;
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const curve = Math.max(18, Math.min(48, Math.abs(dx) * 0.12 + Math.abs(dy) * 0.06));
      const mx = (source.x + target.x) / 2;
      const my = (source.y + target.y) / 2 - curve;
      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', 'M ' + source.x + ' ' + source.y + ' Q ' + mx + ' ' + my + ' ' + target.x + ' ' + target.y);
      path.setAttribute('stroke', edge.color);
      path.setAttribute('stroke-width', edge.state === 'observed' ? '2.8' : '1.5');
      path.setAttribute('stroke-opacity', edge.state === 'observed' ? '0.84' : '0.46');
      path.setAttribute('fill', 'none');
      if (edge.state !== 'observed') path.setAttribute('stroke-dasharray', '6 5');
      edgesSvg.appendChild(path);

      const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', mx);
      label.setAttribute('y', my - 4);
      label.setAttribute('text-anchor', 'middle');
      label.setAttribute('class', 'edge-label');
      label.textContent = edge.state;
      edgesSvg.appendChild(label);
    });

    let zoom = 1;
    const applyZoom = () => { canvas.style.transform = 'scale(' + zoom + ')'; };
    document.getElementById('zoom-in').onclick = () => { zoom = Math.min(2.2, zoom + 0.15); applyZoom(); };
    document.getElementById('zoom-out').onclick = () => { zoom = Math.max(0.5, zoom - 0.15); applyZoom(); };
    document.getElementById('zoom-reset').onclick = () => { zoom = 1; applyZoom(); };

    const modeButtons = {
      balanced: document.getElementById('mode-balanced'),
      relation: document.getElementById('mode-relation'),
      terrain: document.getElementById('mode-terrain'),
    };
    const applyMode = (mode) => {
      canvas.classList.remove('relation-mode', 'terrain-mode');
      if (graphPanel) graphPanel.classList.toggle('active', true);
      if (latestMaterialsPanel) latestMaterialsPanel.classList.toggle('active', true);
      if (tracePanel) tracePanel.classList.toggle('active', true);
      if (mode === 'relation') canvas.classList.add('relation-mode');
      if (mode === 'terrain') canvas.classList.add('terrain-mode');
      Object.entries(modeButtons).forEach(([key, button]) => {
        button.classList.toggle('active', key === mode);
      });
    };
    modeButtons.balanced.onclick = () => applyMode('balanced');
    modeButtons.relation.onclick = () => applyMode('relation');
    modeButtons.terrain.onclick = () => applyMode('terrain');

    const escapeHtml = (text) => String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');

    const selectNodeById = (nodeId) => {
      if (nodeId && nodeById[nodeId]) {
        selectNode(nodeById[nodeId]);
      }
    };

    const renderLatestMaterialList = () => {
      if (!latestMaterialsList) return;
      if (!latestMaterials.length) {
        latestMaterialsList.innerHTML = '<div class="material-list-card"><h3>신규 물질 없음</h3><p>최근 유입된 material이 아직 없습니다.</p></div>';
        return;
      }
      latestMaterialsList.innerHTML = latestMaterials.map(material =>
        '<article class="material-list-card' + (selectedMaterialId === material.material_id ? ' selected' : '') + '" data-material-id="' + escapeHtml(material.material_id || '') + '" data-local-space-id="' + escapeHtml(material.local_space_id || '') + '">' +
        '<h3>' + escapeHtml(material.source_ref || material.display_label || material.material_id) + '</h3>' +
        '<p><strong>local space</strong><br>' + escapeHtml(material.local_space_label || material.local_space_id || '없음') + '</p>' +
        '<p><strong>stage0 run</strong><br>run=' + escapeHtml(material.run_id || '없음') +
        ' / bridge=' + escapeHtml(material.bridge_id || '없음') + '</p>' +
        '<p><strong>provenance</strong><br>doc=' + escapeHtml(material.source_document_id || '없음') +
        ' / event=' + escapeHtml(material.event_id || '없음') +
        ' / fragment=' + escapeHtml(material.fragment_id || '없음') +
        ' / candidate=' + escapeHtml(material.candidate_id || '없음') + '</p>' +
        '<p><strong>분해 정보</strong><br>fragment_count=' + escapeHtml(String(material.fragment_count || 0)) +
        ' / candidate_count=' + escapeHtml(String(material.candidate_count || 0)) +
        ' / bridge_count=' + escapeHtml(String(material.bridge_count || 0)) +
        ' / bridge_status=' + escapeHtml(material.bridge_status || '없음') + '</p>' +
        '<p><strong>source</strong><br>' + escapeHtml(material.source_note_path || '없음') +
        '<br>hash=' + escapeHtml(material.source_content_hash || '없음') + '</p>' +
        '<p><strong>유형</strong><br>' + escapeHtml(material.source_type || 'unknown') + '</p>' +
        '<div class="material-list-raw">' + escapeHtml(material.raw_payload || '') + '</div>' +
        '</article>'
      ).join('');
      latestMaterialsList.querySelectorAll('[data-material-id]').forEach((row) => {
        row.addEventListener('click', () => {
          selectedMaterialId = row.getAttribute('data-material-id') || '';
          selectedTraceId = '';
          renderLatestMaterialList();
          renderLatestTraceList();
          selectNodeById(row.getAttribute('data-local-space-id') || '');
        });
      });
    };
    renderLatestMaterialList();

    const traceTargetLocalSpaceId = (trace) => {
      const related = trace.related_materials || [];
      const row = latestMaterials.find((material) => related.some((ref) => ref.material_id === material.material_id));
      return row ? (row.local_space_id || '') : '';
    };

    const renderLatestTraceList = () => {
      if (!latestTracesList) return;
      if (!latestTraces.length) {
        latestTracesList.innerHTML = '<div class="material-list-card"><h3>trace 없음</h3><p>최근 유입과 연결된 trace가 아직 없습니다.</p></div>';
        return;
      }
      latestTracesList.innerHTML = latestTraces.map(trace =>
        '<article class="material-list-card' + (selectedTraceId === trace.trace_id ? ' selected' : '') + '" data-trace-id="' + escapeHtml(trace.trace_id || '') + '" data-local-space-id="' + escapeHtml(traceTargetLocalSpaceId(trace)) + '">' +
        '<h3>' + escapeHtml(trace.trace_id || 'trace') + '</h3>' +
        '<p><strong>evidence</strong><br>' + escapeHtml(trace.evidence_kind || 'unknown') + '</p>' +
        '<p><strong>note</strong><br>' + escapeHtml(trace.note || '없음') + '</p>' +
        '<p><strong>관련 source</strong><br>' + escapeHtml((trace.related_source_refs || []).join(' / ') || '없음') + '</p>' +
        '<p><strong>cross-context</strong><br>' + escapeHtml(trace.cross_context ? '예' : '아니오') +
        ' / source_count=' + escapeHtml(String(trace.cross_source_ref_count || 0)) + '</p>' +
        '<p><strong>material refs</strong><br>' + escapeHtml((trace.material_refs || []).join(', ') || '없음') + '</p>' +
        '<div class="material-list-raw">' +
        escapeHtml((trace.related_materials || []).map(material =>
          '[' + String(material.scene_index || '?') + '] ' + (material.source_ref || 'no-source') + ' / ' +
          (material.block_label || 'plain') + ' / ' + (material.display_label || material.material_id)
        ).join('\\n')) +
        '</div>' +
        '</article>'
      ).join('');
      latestTracesList.querySelectorAll('[data-trace-id]').forEach((row) => {
        row.addEventListener('click', () => {
          selectedTraceId = row.getAttribute('data-trace-id') || '';
          selectedMaterialId = '';
          renderLatestTraceList();
          renderLatestMaterialList();
          selectNodeById(row.getAttribute('data-local-space-id') || '');
        });
      });
    };
    renderLatestTraceList();

    const formatMaterial = (material) => {
      return '<div class="material-card">' +
        '<strong>' + escapeHtml(material.display_label || material.source_ref || material.material_id) + '</strong>' +
        '<p><code>' + escapeHtml(material.formation_role) + '</code></p>' +
        '<p>입력 원천=' + escapeHtml(material.source_type || 'unknown') +
        ' / ref=' + escapeHtml(material.source_ref || 'no-source-ref') + '</p>' +
        '<p>family=' + escapeHtml(material.family_id || 'none') +
        ' / 세션=' + escapeHtml(material.session_id || 'none') + '</p>' +
        '<p>계보=' + escapeHtml((material.lineage_refs || []).join(', ') || 'none') + '</p>' +
        '<p class="material-body">' + escapeHtml(material.excerpt || '') + '</p>' +
        '</div>';
    };

    const formatTrace = (trace) => {
      return '<li><code>' + escapeHtml(trace.evidence_kind) + '</code> ' +
        escapeHtml(trace.trace_id) + '<br>' +
        '<span>' + escapeHtml(trace.note || '') + '</span><br>' +
        '<span>재료 refs: ' + escapeHtml((trace.material_refs || []).join(', ')) + '</span></li>';
    };

    const formatNeighbor = (neighbor) => {
      return '<li><code>' + escapeHtml(neighbor.state) + '</code> ' +
        escapeHtml(neighbor.local_space_id) + ' via ' + escapeHtml(neighbor.bridge_id) + '</li>';
    };

    const formatAnchorGroup = (anchors, emptyText) => {
      if (!(anchors || []).length) {
        return '<p>' + escapeHtml(emptyText) + '</p>';
      }
      return '<div class="chips">' + anchors.map(anchor =>
        '<span class="chip" title="' + escapeHtml(anchor.canonical_key || '') + '">' +
        escapeHtml((anchor.anchor_type || 'semantic') + ': ' + (anchor.display_label || anchor.canonical_key || '')) +
        '</span>'
      ).join('') + '</div>';
    };

    const formatDroppedWeakAnchors = (state) => {
      if (!state || state.available === false) {
        return '<p>아직 미지원</p>';
      }
      if (!(state.items || []).length) {
        return '<p>제거된 약한 anchor 없음</p>';
      }
      return '<div class="chips">' + (state.items || []).map(value =>
        '<span class="chip">' + escapeHtml(value) + '</span>'
      ).join('') + '</div>';
    };

    const formatBridgeReasonSummary = (rows) => {
      if (!(rows || []).length) {
        return '<p>bridge reason summary 없음</p>';
      }
      return '<ul>' + rows.map(row =>
        '<li><strong>' + escapeHtml(row.peer_label || row.peer_local_space_id || 'unknown') + '</strong><br>' +
        escapeHtml(row.reason_line || 'reason unavailable') +
        (((row.anchor_hints || []).length) ? '<br><span>hints: ' + escapeHtml((row.anchor_hints || []).join(', ')) + '</span>' : '') +
        '</li>'
      ).join('') + '</ul>';
    };

    const params = new URLSearchParams(window.location.search);
    const requestedLocalSpaceId = params.get('local_space_id');

    const buildSourceLink = (node, material) => {
      const link = new URL('/source', window.location.origin);
      if (material.fragment_id) link.searchParams.set('fragment_id', material.fragment_id);
      else if (material.source_ref) link.searchParams.set('source_ref', material.source_ref);
      else return '';
      link.searchParams.set('from', 'operator');
      link.searchParams.set('return_href', '/?local_space_id=' + encodeURIComponent(node.id));
      link.searchParams.set('return_label', 'Back to Operator');
      link.searchParams.set('origin_route', 'operator');
      link.searchParams.set('origin_local_space_id', node.id);
      link.searchParams.set('origin_region_label', node.label || '');
      link.searchParams.set('origin_source_ref', material.source_ref || '');
      if (material.fragment_id) link.searchParams.set('origin_fragment_id', material.fragment_id);
      return link.pathname + '?' + link.searchParams.toString();
    };

    const buildDustLink = (node, material) => {
      const dustId = material.fragment_id || '';
      if (!dustId) return '';
      const link = new URL('/dust', window.location.origin);
      link.searchParams.set('dust_id', dustId);
      link.searchParams.set('from', 'operator');
      link.searchParams.set('return_href', '/?local_space_id=' + encodeURIComponent(node.id));
      link.searchParams.set('return_label', 'Back to Operator');
      link.searchParams.set('origin_route', 'operator');
      link.searchParams.set('origin_local_space_id', node.id);
      link.searchParams.set('origin_region_label', node.label || '');
      link.searchParams.set('origin_source_ref', material.source_ref || '');
      if (material.fragment_id) link.searchParams.set('origin_fragment_id', material.fragment_id);
      link.searchParams.set('origin_dust_id', dustId);
      return link.pathname + '?' + link.searchParams.toString();
    };

    const formatEvidenceRows = (node, materials, traces) => {
      const sections = [];
      if ((traces || []).length) {
        sections.push('<h3>trace 근거</h3><ul>' + traces.map(formatTrace).join('') + '</ul>');
      } else {
        sections.push('<h3>trace 근거</h3><p>없음</p>');
      }
      const evidenceRows = (materials || []).map(material => {
        const sourceLink = buildSourceLink(node, material);
        const dustLink = buildDustLink(node, material);
        const links = [
          sourceLink ? '<a href="' + sourceLink + '">source</a>' : '<span>source 없음</span>',
          dustLink ? '<a href="' + dustLink + '">dust</a>' : '<span>dust 없음</span>',
        ].join(' / ');
        return '<li><strong>' + escapeHtml(material.display_label || material.material_id) + '</strong><br>' +
          'source_ref=' + escapeHtml(material.source_ref || '없음') +
          (material.fragment_id ? '<br>fragment=' + escapeHtml(material.fragment_id) : '') +
          '<br>links: ' + links + '</li>';
      });
      sections.push('<h3>drill-down</h3>' + (evidenceRows.length ? '<ul>' + evidenceRows.join('') + '</ul>' : '<p>연결 가능한 evidence 없음</p>'));
      return sections.join('');
    };

    const formatObserverCompare = (observerCompare) => {
      const compare = observerCompare || { available: false, merged: {} };
      const merged = compare.merged || {};
      return '<p><strong>available</strong><br>' + escapeHtml(String(compare.available)) + '</p>' +
        '<p><strong>merged</strong><br>' +
        'role=' + escapeHtml(merged.observer_role || '없음') +
        ' / ambiguity=' + escapeHtml(String(merged.observer_ambiguity ?? '없음')) +
        ' / confidence=' + escapeHtml(String(merged.observer_confidence_numeric ?? '없음')) +
        (((merged.observer_signals || []).length) ? '<br>signals=' + escapeHtml((merged.observer_signals || []).join(', ')) : '') +
        '</p>' +
        '<p><strong>status</strong><br>' + escapeHtml(compare.note || 'raw compare not available yet') + '</p>';
    };

    const compactStateChip = (text) => '<span class="chip">' + escapeHtml(text) + '</span>';

    const formatCompactAnchorItems = (anchors, emptyText) => {
      if (!anchors || !anchors.length) return compactStateChip(emptyText);
      const visible = anchors.slice(0, 2).map(anchor =>
        compactStateChip((anchor.anchor_type || 'semantic') + ':' + (anchor.display_label || anchor.canonical_key || ''))
      );
      if (anchors.length > 2) visible.push(compactStateChip('+' + String(anchors.length - 2) + ' more'));
      return visible.join('');
    };

    const extractCompactObserverSignals = (node, merged) => {
      const directSignals = merged && Array.isArray(merged.observer_signals) ? merged.observer_signals.filter(Boolean) : [];
      if (directSignals.length) return directSignals.slice(0, 2);
      const signalSet = [];
      (node.materials || []).forEach((material) => {
        (material.observer_signals || []).forEach((signal) => {
          if (signal && !signalSet.includes(signal)) signalSet.push(signal);
        });
      });
      return signalSet.slice(0, 2);
    };

    const formatCompactShelf = (node) => {
      const representativeAnchors = node.representative_anchors || [];
      const supportingAnchors = node.supporting_anchors || [];
      const droppedWeakAnchors = node.dropped_weak_anchors || { available: false, items: [] };
      const bridgeReasons = node.bridge_reason_summary || [];
      const observerCompare = node.observer_compare || { available: false, merged: {} };
      const strongestBridge = bridgeReasons[0] || null;
      const merged = observerCompare.merged || {};
      const observerSignals = extractCompactObserverSignals(node, merged);

      const anchorsState = (!representativeAnchors.length && !supportingAnchors.length) ? 'none' : 'present';
      const bridgeState = strongestBridge ? 'present' : 'none';
      const observerState = observerCompare.available ? 'present' : 'not available yet';
      const droppedState = droppedWeakAnchors.available === false
        ? 'not available yet'
        : ((droppedWeakAnchors.items || []).length ? 'present' : 'none rejected');

      const droppedItems = (droppedWeakAnchors.items || []).slice(0, 2).map(value => compactStateChip(String(value)));
      if ((droppedWeakAnchors.items || []).length > 2) {
        droppedItems.push(compactStateChip('+' + String(droppedWeakAnchors.items.length - 2) + ' more'));
      }

      return '' +
        '<div class="compact-shelf">' +
          '<div class="compact-card">' +
            '<h4>Anchors</h4>' +
            '<p><strong>state</strong> ' + escapeHtml(anchorsState) + '</p>' +
            '<div class="chips">' + formatCompactAnchorItems(representativeAnchors, 'none') + '</div>' +
            '<div class="chips" style="margin-top:6px">' + formatCompactAnchorItems(supportingAnchors, 'none') + '</div>' +
          '</div>' +
          '<div class="compact-card">' +
            '<h4>Bridge</h4>' +
            '<p><strong>state</strong> ' + escapeHtml(bridgeState) + ' / count=' + escapeHtml(String(node.bridge_count || 0)) + '</p>' +
            (strongestBridge
              ? '<p><strong>peer</strong> ' + escapeHtml(strongestBridge.peer_label || strongestBridge.peer_local_space_id || '-') + '</p>' +
                '<p>' + escapeHtml(strongestBridge.reason_line || 'reason unavailable') + '</p>'
              : '<p>none</p>') +
          '</div>' +
          '<div class="compact-card">' +
            '<h4>Observer</h4>' +
            '<p><strong>state</strong> ' + escapeHtml(observerState) + '</p>' +
            (observerCompare.available
              ? '<p><strong>merged</strong> role=' + escapeHtml(merged.observer_role || '없음') +
                ' / ambiguity=' + escapeHtml(String(merged.observer_ambiguity ?? '없음')) +
                ' / confidence=' + escapeHtml(String(merged.observer_confidence_numeric ?? '없음')) + '</p>' +
                '<div class="chips">' +
                (observerSignals.length ? observerSignals.map(signal => compactStateChip(signal)).join('') : compactStateChip('none')) +
                '</div>'
              : '<p>not available yet</p>') +
          '</div>' +
          '<div class="compact-card">' +
            '<h4>Dropped Weak</h4>' +
            '<p><strong>state</strong> ' + escapeHtml(droppedState) + '</p>' +
            '<div class="chips">' +
            (droppedWeakAnchors.available === false
              ? compactStateChip('not available yet')
              : (droppedItems.length ? droppedItems.join('') : compactStateChip('none rejected'))) +
            '</div>' +
          '</div>' +
        '</div>';
    };

    const formatMaterialCompare = (material, node, traces) => {
      const relatedTraces = traces.filter(trace => (trace.material_refs || []).includes(material.material_id));
      const evidenceKinds = relatedTraces.map(trace => trace.evidence_kind).filter(Boolean);
      const evidenceSummary = evidenceKinds.length ? evidenceKinds.join(', ') : '직접 연결된 trace 없음';
      return '<div class="material-compare">' +
        '<strong>' + escapeHtml(material.display_label || material.material_id) + '</strong>' +
        '<p><strong>유형</strong><br>' + escapeHtml(material.source_type || 'unknown') + ' / ' + escapeHtml(material.formation_role || 'unknown') + '</p>' +
        '<p><strong>observer</strong><br>role=' + escapeHtml(material.observer_role || '없음') +
        ' / ambiguity=' + escapeHtml(String(material.observer_ambiguity ?? '없음')) +
        ' / confidence=' + escapeHtml(String(material.observer_confidence_numeric ?? '없음')) +
        ((material.observer_signals || []).length ? '<br>signals=' + escapeHtml((material.observer_signals || []).join(', ')) : '') + '</p>' +
        '<p><strong>자동 제목</strong><br>' + escapeHtml(material.source_ref || '없음') + '</p>' +
        '<p><strong>Stage0 provenance</strong><br>run=' + escapeHtml(material.run_id || '없음') +
        ' / bridge=' + escapeHtml(material.bridge_id || '없음') +
        '<br>doc=' + escapeHtml(material.source_document_id || '없음') +
        ' / event=' + escapeHtml(material.event_id || '없음') +
        ' / fragment=' + escapeHtml(material.fragment_id || '없음') +
        ' / candidate=' + escapeHtml(material.candidate_id || '없음') + '</p>' +
        '<p><strong>분해 상태</strong><br>fragment_count=' + escapeHtml(String(material.fragment_count || 0)) +
        ' / candidate_count=' + escapeHtml(String(material.candidate_count || 0)) +
        ' / bridge_count=' + escapeHtml(String(material.bridge_count || 0)) +
        ' / bridge_status=' + escapeHtml(material.bridge_status || '없음') +
        '<br>source_note_path=' + escapeHtml(material.source_note_path || '없음') + '</p>' +
        '<p><strong>이 공간에서의 위치</strong><br>' + escapeHtml(node.label) + ' 안에서 관찰되는 재료</p>' +
        '<p><strong>연결된 trace</strong><br>' + escapeHtml(evidenceSummary) + '</p>' +
        '<p><strong>원문</strong></p>' +
        '<div class="material-raw">' + escapeHtml(material.raw_payload || material.excerpt || '') + '</div>' +
        '</div>';
    };

    const buildNodeDetailHtml = (node) => {
      const materials = node.materials || [];
      const traces = node.trace_details || [];
      const structure = node.structure || {};
      const interpretation = node.interpretation || {};
      const representativeAnchors = node.representative_anchors || [];
      const supportingAnchors = node.supporting_anchors || [];
      const droppedWeakAnchors = node.dropped_weak_anchors || { available: false, items: [] };
      const bridgeReasons = node.bridge_reason_summary || [];
      const observerCompare = node.observer_compare || { available: false, merged: {} };
      return '' +
        formatCompactShelf(node) +
        '<section class="modal-section">' +
        '<h3>Summary</h3>' +
        '<p><strong>field</strong><br>' + escapeHtml(interpretation.field_kind || '해석층 없음') + '</p>' +
        '<p><strong>materials</strong><br>' + escapeHtml(interpretation.material_summary || '재료 혼합 미상') + '</p>' +
        '<p><strong>structure</strong><br>' + escapeHtml(structure.relation_state_label || '없음') + '</p>' +
        '<p><strong>pressure axes</strong><br>' + escapeHtml(structure.axis_summary || '없음') + '</p>' +
        '<p><strong>cell refs</strong><br>' + escapeHtml((node.cell_ids || []).join(', ') || '없음') + '</p>' +
        '</section>' +
        '<section class="modal-section">' +
        '<h3>Why</h3>' +
        '<p><strong>why grouped</strong><br>' + escapeHtml(interpretation.why_grouped || '아직 해석되지 않음') + '</p>' +
        '<p><strong>relation reason</strong><br>' + escapeHtml(interpretation.relation_reason || '아직 해석되지 않음') + '</p>' +
        '<p><strong>quiet reason</strong><br>' + escapeHtml(interpretation.quiet_reason || '아직 해석되지 않음') + '</p>' +
        '<p><strong>evidence summary</strong><br>' + escapeHtml(interpretation.evidence_summary || '없음') + '</p>' +
        '<h3>bridge reason</h3>' + formatBridgeReasonSummary(bridgeReasons) +
        '</section>' +
        '<section class="modal-section">' +
        '<h3>Anchors</h3>' +
        '<p><strong>representative</strong></p>' + formatAnchorGroup(representativeAnchors, '대표 anchor 없음') +
        '<p><strong>supporting</strong></p>' + formatAnchorGroup(supportingAnchors, '보조 anchor 없음') +
        '<p><strong>dropped weak</strong></p>' + formatDroppedWeakAnchors(droppedWeakAnchors) +
        '</section>' +
        '<section class="modal-section">' +
        '<h3>Evidence</h3>' +
        formatEvidenceRows(node, materials, traces) +
        '<h3>material compare</h3>' +
        (materials.length ? materials.map(material => formatMaterialCompare(material, node, traces)).join('') : '<p>없음</p>') +
        '</section>' +
        '<section class="modal-section">' +
        '<h3>Compare</h3>' +
        formatObserverCompare(observerCompare) +
        '</section>';
    };

    const renderInspector = (node) => {
      if (!node) {
        inspectorTitle.textContent = 'Operator Inspector';
        inspectorSubtitle.textContent = 'local space를 선택하면 Summary / Why / Anchors / Evidence / Compare가 여기에 고정됩니다.';
        inspectorBody.innerHTML = '<div class="muted">선택된 local space가 없습니다.</div>';
        return;
      }
      const structure = node.structure || {};
      inspectorTitle.textContent = node.label;
      inspectorSubtitle.textContent =
        '상태=' + (structure.state_label || node.state) +
        ' / 공존=' + node.coexistence_mode +
        ' / 브리지=' + node.bridge_count +
        ' / degree=' + node.degree;
      inspectorBody.innerHTML = buildNodeDetailHtml(node);
    };

    const openModal = (node) => {
      const structure = node.structure || {};
      modalTitle.textContent = node.label;
      modalSubtitle.innerHTML =
        '상태=' + escapeHtml(structure.state_label || node.state) +
        ' / 공존=' + escapeHtml(node.coexistence_mode) +
        ' / 조용함=' + escapeHtml(structure.quiet_label || (node.quiet ? '예' : '아니오')) +
        ' / 브리지=' + node.bridge_count +
        ' / degree=' + node.degree;
      modalBody.innerHTML = buildNodeDetailHtml(node);
      modalBackdrop.classList.add('open');
    };

    const selectNode = (node) => {
      selectedNodeId = node.id;
      renderInspector(node);
      document.querySelectorAll('.node').forEach(el => {
        const isSelected = el.getAttribute('data-node-id') === node.id;
        el.classList.toggle('selected', isSelected);
        el.style.zIndex = isSelected ? '2' : '1';
      });
    };

    document.getElementById('modal-close').onclick = () => modalBackdrop.classList.remove('open');
    modalBackdrop.onclick = (event) => {
      if (event.target === modalBackdrop) modalBackdrop.classList.remove('open');
    };
    inspectorOpenModal.onclick = () => {
      const node = nodeById[selectedNodeId];
      if (node) openModal(node);
    };
    if (requestedLocalSpaceId && nodeById[requestedLocalSpaceId]) {
      selectNode(nodeById[requestedLocalSpaceId]);
    } else if (latestIntake.local_space_ids && latestIntake.local_space_ids.length && nodeById[latestIntake.local_space_ids[0]]) {
      selectNode(nodeById[latestIntake.local_space_ids[0]]);
    } else if (data.nodes.length) {
      selectNode(data.nodes[0]);
    } else {
      renderInspector(null);
    }
""" + interactive_script + """
  </script>
</body>
</html>
"""


def _render_intake_panel() -> str:
    return """
      <button id="open-intake" title="입력 투입" aria-label="입력 투입" style="font-size:18px; line-height:1; min-width:42px;">+</button>
"""


def _render_interactive_script() -> str:
    return """
    const intakeForm = document.getElementById('intake-form');
    const intakeStatus = document.getElementById('intake-status');
    const intakeOpen = document.getElementById('open-intake');
    const intakeClose = document.getElementById('intake-close');
    if (intakeOpen && intakeBackdrop) {
      intakeOpen.addEventListener('click', () => {
        intakeBackdrop.classList.add('open');
      });
    }
    if (intakeClose && intakeBackdrop) {
      intakeClose.addEventListener('click', () => {
        intakeBackdrop.classList.remove('open');
      });
    }
    if (intakeBackdrop) {
      intakeBackdrop.addEventListener('click', (event) => {
        if (event.target === intakeBackdrop) intakeBackdrop.classList.remove('open');
      });
    }
    if (intakeForm && intakeStatus) {
      intakeForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        intakeStatus.textContent = '입력을 투입하는 중입니다...';
        const formData = new FormData(intakeForm);
        try {
          const response = await fetch('/api/ingest', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(Object.fromEntries(formData.entries())),
          });
          const result = await response.json();
          if (!response.ok) {
            throw new Error(result.error || '입력 처리에 실패했습니다.');
          }
          intakeStatus.textContent = '투입 완료: material ' + String(result.material_count || 1) + '개 / local space ' + String((result.local_space_ids || []).length || 1) + '개';
          window.setTimeout(() => window.location.reload(), 500);
        } catch (error) {
          intakeStatus.textContent = '실패: ' + (error.message || '알 수 없는 오류');
        }
      });
    }
"""
