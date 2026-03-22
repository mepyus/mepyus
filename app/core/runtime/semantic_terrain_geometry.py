from __future__ import annotations

from collections import defaultdict
from typing import Dict, List


def build_semantic_terrain_geometry(
    *,
    cells: List[Dict[str, object]],
    regions: List[Dict[str, object]],
    contour_lines: List[Dict[str, object]],
    region_flows: List[Dict[str, object]],
    fault_lines: List[Dict[str, object]],
    fields: Dict[str, object],
) -> Dict[str, object]:
    cell_field_lookup = {row["cell_id"]: row for row in fields.get("cell_fields", [])}
    region_field_lookup = {row["local_space_id"]: row for row in fields.get("region_fields", [])}
    edge_fields = fields.get("edge_fields", [])
    boundary_segments = _build_region_boundary_geometry(edge_fields, cells)
    ridge_segments = _build_score_segments(cells, cell_field_lookup, "ridge_axis_score", "ridge_segment", 0.5)
    valley_segments = _build_score_segments(cells, cell_field_lookup, "valley_channel_score", "valley_segment", 0.22)
    basin_regions = _build_basin_geometry(regions, region_field_lookup, 0.48)
    current_lines = _build_current_lines(region_flows)
    fault_geometry = _build_fault_geometry(fault_lines)
    contour_geometry = _build_contour_geometry(contour_lines)
    return {
        "region_boundaries": boundary_segments,
        "ridge_segments": ridge_segments,
        "valley_segments": valley_segments,
        "basin_regions": basin_regions,
        "current_lines": current_lines,
        "fault_geometry": fault_geometry,
        "contour_geometry": contour_geometry,
    }


def _build_region_boundary_geometry(edge_fields: List[Dict[str, object]], cells: List[Dict[str, object]]) -> List[Dict[str, object]]:
    lookup = {row["cell_id"]: row for row in cells}
    rows: List[Dict[str, object]] = []
    for edge in edge_fields:
        if float(edge["region_boundary_score"]) < 0.62:
            continue
        left = lookup.get(edge["from_cell_id"])
        right = lookup.get(edge["to_cell_id"])
        if not left or not right:
            continue
        rows.append(
            {
                "geometry_id": f"boundary_{edge['edge_id']}",
                "geometry_type": "region_boundary",
                "derived_field_name": "region_boundary_score",
                "path": [
                    {"x": left["x"], "y": left["y"]},
                    {"x": right["x"], "y": right["y"]},
                ],
                "value": edge["region_boundary_score"],
                "calculation_summary": {
                    "scene_divergence": edge["scene_divergence"],
                    "shared_anchor_ratio": edge["shared_anchor_ratio"],
                    "elevation_gradient": edge["elevation_gradient"],
                    "stability_gradient": edge["stability_gradient"],
                    "fog_gradient": edge["fog_gradient"],
                },
                "related_ids": [edge["from_cell_id"], edge["to_cell_id"]],
            }
        )
    return rows


def _build_score_segments(
    cells: List[Dict[str, object]],
    cell_field_lookup: Dict[str, Dict[str, object]],
    field_name: str,
    geometry_type: str,
    threshold: float,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for cell in cells:
        field = cell_field_lookup.get(cell["cell_id"])
        if not field:
            continue
        value = float(field.get(field_name, 0.0))
        if value < threshold:
            continue
        rows.append(
            {
                "geometry_id": f"{geometry_type}_{cell['cell_id']}",
                "geometry_type": geometry_type,
                "derived_field_name": field_name,
                "path": [
                    {"x": float(cell["x"]) - 10, "y": float(cell["y"])},
                    {"x": float(cell["x"]) + 10, "y": float(cell["y"])},
                ],
                "value": round(value, 3),
                "calculation_summary": field.get("region_identity_signature", {}),
                "related_ids": [cell["cell_id"]],
            }
        )
    return rows


def _build_basin_geometry(
    regions: List[Dict[str, object]],
    region_field_lookup: Dict[str, Dict[str, object]],
    threshold: float,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for region in regions:
        field = region_field_lookup.get(region["local_space_id"], {})
        value = float(field.get("basin_presence", 0.0))
        if value < threshold:
            continue
        rows.append(
            {
                "geometry_id": f"basin_{region['local_space_id']}",
                "geometry_type": "basin_region",
                "derived_field_name": "basin_retention_score",
                "center": {"x": region["x"], "y": region["y"]},
                "size": {"width": region["width"], "height": region["height"]},
                "value": round(value, 3),
                "calculation_summary": field,
                "related_ids": [region["local_space_id"]],
            }
        )
    return rows


def _build_current_lines(region_flows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for flow in region_flows:
        rows.append(
            {
                "geometry_id": f"current_{flow['bridge_id']}",
                "geometry_type": "current_line",
                "derived_field_name": "anchor_flow_field",
                "path": flow["path"],
                "value": flow["strength"],
                "calculation_summary": {
                    "anchor_hint_count": flow.get("anchor_hint_count", 0),
                    "note": flow.get("note", ""),
                },
                "related_ids": [flow["from_local_space_id"], flow["to_local_space_id"]],
            }
        )
    return rows


def _build_fault_geometry(fault_lines: List[Dict[str, object]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for fault in fault_lines:
        rows.append(
            {
                "geometry_id": fault["fault_id"],
                "geometry_type": "fault_line",
                "derived_field_name": "fault_line_score",
                "center": {"x": fault["x"], "y": fault["y"]},
                "value": fault["severity"],
                "calculation_summary": {
                    "signals": fault.get("signals", []),
                },
                "related_ids": [fault["fragment_id"]],
            }
        )
    return rows


def _build_contour_geometry(contour_lines: List[Dict[str, object]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for line in contour_lines:
        rows.append(
            {
                "geometry_id": line["line_id"],
                "geometry_type": "contour_line",
                "derived_field_name": "elevation_contour",
                "path": line["path"],
                "value": line["level"],
                "calculation_summary": {"level": line["level"]},
                "related_ids": [],
            }
        )
    return rows
