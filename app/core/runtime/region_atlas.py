from __future__ import annotations

from typing import Dict, List
import json
from pathlib import Path

from app.core.runtime.region_atlas_render import render_region_atlas_html
from app.runtime.terrain_map import build_terrain_map_data


def build_region_atlas_data(runtime_root) -> Dict[str, object]:
    terrain = build_terrain_map_data(runtime_root)
    regions = list(terrain.get("regions", []))
    flows = list(terrain.get("region_flows", []))
    runtime_root = Path(runtime_root)
    local_space_meta = _load_local_space_meta(runtime_root)
    local_space_links = _load_local_space_links(runtime_root, local_space_meta)

    flow_map: Dict[str, List[Dict[str, object]]] = {}
    for flow in flows:
        left = str(flow.get("from_local_space_id", ""))
        right = str(flow.get("to_local_space_id", ""))
        flow_map.setdefault(left, []).append(flow)
        flow_map.setdefault(right, []).append(flow)

    region_cards = []
    for region in regions:
        local_space_id = str(region.get("local_space_id", ""))
        related = sorted(flow_map.get(local_space_id, []), key=lambda row: row.get("strength", 0), reverse=True)
        preferred_related = [row for row in related if list(row.get("anchor_hints", []))]
        fallback_related = [row for row in related if not list(row.get("anchor_hints", []))]
        shown_related = preferred_related[:6]
        if len(shown_related) < 6:
            shown_related.extend(fallback_related[: max(0, 2 - len(preferred_related))])
        representative_anchors = _normalize_anchor_objects(
            local_space_meta.get(local_space_id, {}).get("representative_anchors", [])
        )
        supporting_anchors = _normalize_anchor_objects(
            local_space_meta.get(local_space_id, {}).get("supporting_anchors", [])
        )
        connection_rows = [
            _build_connection_row(local_space_id, flow, local_space_links)
            for flow in shown_related
        ]
        region_cards.append(
            {
                "local_space_id": local_space_id,
                "label": str(region.get("label", "")),
                "dominant_scene": str(region.get("dominant_scene", "unknown")),
                "dominant_role": str(region.get("dominant_role", "")),
                "material_count": int(region.get("material_count", 0)),
                "representative_anchors": representative_anchors,
                "supporting_anchors": supporting_anchors,
                "anchor_summary": list(region.get("anchor_summary", []))[:6],
                "supporting_anchor_summary": [row["display_label"] for row in supporting_anchors[:6]],
                "landmarks": list(region.get("landmarks", []))[:4],
                "connections": connection_rows,
                "why_region_exists": _why_region_exists(region, representative_anchors, connection_rows),
                "bridge_reason_summary": [row["reason_line"] for row in connection_rows],
                "source_links": local_space_links.get(local_space_id, {}).get("source_links", []),
                "dust_links": local_space_links.get(local_space_id, {}).get("dust_links", []),
                "rejected_overlap_state": {"available": False, "items": []},
            }
        )

    region_cards.sort(key=lambda row: (len(row["connections"]), row["material_count"]), reverse=True)

    return {
        "summary": {
            "region_count": len(region_cards),
            "bridge_count": len(flows),
        },
        "regions": region_cards,
        "bridges": [
            _build_bridge_row(flow, local_space_links)
            for flow in sorted(
                flows,
                key=lambda row: (1 if list(row.get("anchor_hints", [])) else 0, row.get("strength", 0)),
                reverse=True,
            )
            if list(flow.get("anchor_hints", [])) or float(flow.get("strength", 0)) >= 0.7
        ],
    }


def _load_local_space_meta(runtime_root: Path) -> Dict[str, Dict[str, object]]:
    rows: Dict[str, Dict[str, object]] = {}
    local_space_dir = runtime_root / "core" / "local_spaces"
    for path in local_space_dir.glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        local_space_id = str(payload.get("local_space_id", "")).strip()
        if not local_space_id:
            continue
        rows[local_space_id] = payload
    return rows


def _load_local_space_links(
    runtime_root: Path,
    local_space_meta: Dict[str, Dict[str, object]],
) -> Dict[str, Dict[str, List[Dict[str, str]]]]:
    cell_dir = runtime_root / "core" / "space_cells"
    material_dir = runtime_root / "core" / "materials"
    rows: Dict[str, Dict[str, List[Dict[str, str]]]] = {}
    for local_space_id, payload in local_space_meta.items():
        seen_source = set()
        seen_dust = set()
        source_links: List[Dict[str, str]] = []
        dust_links: List[Dict[str, str]] = []
        for cell_id in payload.get("cell_refs", []):
            cell_path = cell_dir / f"{cell_id}.json"
            if not cell_path.exists():
                continue
            try:
                cell = json.loads(cell_path.read_text(encoding="utf-8"))
            except Exception:
                continue
            for material_id in cell.get("material_refs", []):
                material_path = material_dir / f"{material_id}.json"
                if not material_path.exists():
                    continue
                try:
                    material = json.loads(material_path.read_text(encoding="utf-8"))
                except Exception:
                    continue
                source_ref = str(material.get("source_ref", "")).strip()
                if source_ref and source_ref not in seen_source:
                    seen_source.add(source_ref)
                    source_links.append(
                        {
                            "label": Path(source_ref).stem or source_ref,
                            "source_ref": source_ref,
                        }
                    )
                metadata = material.get("metadata") or {}
                dust_id = (
                    str(metadata.get("dust_input_id", "")).strip()
                    or str(material.get("material_id", "")).strip()
                    or str(metadata.get("fragment_id", "")).strip()
                )
                if dust_id and dust_id not in seen_dust:
                    seen_dust.add(dust_id)
                    dust_links.append(
                        {
                            "label": dust_id,
                            "dust_id": dust_id,
                        }
                    )
        rows[local_space_id] = {
            "source_links": source_links[:6],
            "dust_links": dust_links[:6],
        }
    return rows


def _normalize_anchor_objects(values: List[object]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
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
        rows.append(
            {
                "canonical_key": canonical_key,
                "display_label": label,
                "anchor_type": anchor_type,
            }
        )
    return rows


def _build_connection_row(
    local_space_id: str,
    flow: Dict[str, object],
    local_space_links: Dict[str, Dict[str, List[Dict[str, str]]]],
) -> Dict[str, object]:
    from_local_space_id = str(flow.get("from_local_space_id", ""))
    to_local_space_id = str(flow.get("to_local_space_id", ""))
    peer_local_space_id = to_local_space_id if from_local_space_id == local_space_id else from_local_space_id
    source_links = list(local_space_links.get(peer_local_space_id, {}).get("source_links", []))[:3]
    dust_links = list(local_space_links.get(peer_local_space_id, {}).get("dust_links", []))[:3]
    return {
        "bridge_id": str(flow.get("bridge_id", "")),
        "peer_local_space_id": peer_local_space_id,
        "peer_label": str(flow.get("to_label") if flow.get("from_local_space_id") == local_space_id else flow.get("from_label")),
        "strength": float(flow.get("strength", 0)),
        "anchor_hints": list(flow.get("anchor_hints", []))[:4],
        "reason_line": _bridge_reason_line(local_space_id, flow),
        "source_links": source_links,
        "dust_links": dust_links,
    }


def _build_bridge_row(
    flow: Dict[str, object],
    local_space_links: Dict[str, Dict[str, List[Dict[str, str]]]],
) -> Dict[str, object]:
    from_local_space_id = str(flow.get("from_local_space_id", ""))
    to_local_space_id = str(flow.get("to_local_space_id", ""))
    source_links: List[Dict[str, str]] = []
    dust_links: List[Dict[str, str]] = []
    for local_space_id in (from_local_space_id, to_local_space_id):
        link_payload = local_space_links.get(local_space_id, {})
        for row in list(link_payload.get("source_links", [])):
            if row not in source_links:
                source_links.append(row)
        for row in list(link_payload.get("dust_links", [])):
            if row not in dust_links:
                dust_links.append(row)
    return {
        "bridge_id": str(flow.get("bridge_id", "")),
        "from_label": str(flow.get("from_label", "")),
        "to_label": str(flow.get("to_label", "")),
        "strength": float(flow.get("strength", 0)),
        "anchor_hints": list(flow.get("anchor_hints", []))[:4],
        "reason_line": _bridge_reason_line("", flow),
        "source_links": source_links[:3],
        "dust_links": dust_links[:3],
    }


def _why_region_exists(
    region: Dict[str, object],
    representative_anchors: List[Dict[str, str]],
    connection_rows: List[Dict[str, object]],
) -> str:
    anchor_labels = [row["display_label"] for row in representative_anchors[:2]]
    if anchor_labels:
        anchor_phrase = "대표 anchor %s" % " / ".join(anchor_labels)
    else:
        anchor_phrase = "대표 anchor 단서"
    if connection_rows:
        return "%s와 material %s개, 연결 %s개가 이 region을 지지함" % (
            anchor_phrase,
            int(region.get("material_count", 0)),
            len(connection_rows),
        )
    return "%s와 material %s개가 이 region을 지지함" % (
        anchor_phrase,
        int(region.get("material_count", 0)),
    )


def _bridge_reason_line(local_space_id: str, flow: Dict[str, object]) -> str:
    if flow.get("anchor_hints"):
        peer_label = str(flow.get("to_label") if flow.get("from_local_space_id") == local_space_id else flow.get("from_label") or "")
        if not peer_label:
            peer_label = str(flow.get("to_label") or flow.get("from_label") or "peer region")
        return "%s와 %s 축으로 연결" % (peer_label, " / ".join(list(flow.get("anchor_hints", []))[:2]))
    return "shared bridge trace로 연결"

def write_region_atlas_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_region_atlas_data(runtime_root)
    reports_root = runtime_root / "reports"
    reports_root.mkdir(parents=True, exist_ok=True)
    json_path = reports_root / "region_atlas_view.json"
    html_path = reports_root / "region_atlas_view.html"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    html_path.write_text(render_region_atlas_html(data), encoding="utf-8")
    return {"json": json_path, "html": html_path}
