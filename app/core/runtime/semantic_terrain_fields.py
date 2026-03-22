from __future__ import annotations

from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import math


def build_semantic_terrain_fields(
    *,
    cells: List[Dict[str, object]],
    sample_points: List[Dict[str, object]],
    regions: List[Dict[str, object]],
    water_flows: List[Dict[str, object]],
    wind_fields: List[Dict[str, object]],
    fault_lines: List[Dict[str, object]],
) -> Dict[str, object]:
    cell_lookup = {(int(cell["x"]), int(cell["y"])): cell for cell in cells}
    neighbors = _build_cell_neighbors(cells, cell_lookup)
    point_index = _build_point_index(sample_points, cells)
    edge_fields = _build_edge_fields(cells, neighbors, point_index)
    cell_fields = _build_cell_fields(cells, neighbors, point_index, edge_fields, water_flows, wind_fields, fault_lines)
    region_fields = _build_region_fields(regions, cells, cell_fields)
    return {
        "cell_fields": cell_fields,
        "edge_fields": edge_fields,
        "region_fields": region_fields,
    }


def _build_cell_neighbors(
    cells: List[Dict[str, object]],
    cell_lookup: Dict[Tuple[int, int], Dict[str, object]],
) -> Dict[str, List[Dict[str, object]]]:
    neighbors: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    step = 28
    for cell in cells:
        x = int(cell["x"])
        y = int(cell["y"])
        for dx, dy in ((step, 0), (-step, 0), (0, step), (0, -step)):
            peer = cell_lookup.get((x + dx, y + dy))
            if peer:
                neighbors[cell["cell_id"]].append(peer)
    return neighbors


def _build_point_index(
    sample_points: List[Dict[str, object]],
    cells: List[Dict[str, object]],
) -> Dict[str, List[Dict[str, object]]]:
    index: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    if not cells:
        return index
    step = 28
    for point in sample_points:
        cell_x = int(point["x"] // step) * step
        cell_y = int(point["y"] // step) * step
        index[f"terrain_{cell_x}_{cell_y}"].append(point)
    return index


def _build_edge_fields(
    cells: List[Dict[str, object]],
    neighbors: Dict[str, List[Dict[str, object]]],
    point_index: Dict[str, List[Dict[str, object]]],
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    seen = set()
    for cell in cells:
        for peer in neighbors.get(cell["cell_id"], []):
            pair = tuple(sorted((cell["cell_id"], peer["cell_id"])))
            if pair in seen:
                continue
            seen.add(pair)
            left_points = point_index.get(cell["cell_id"], [])
            right_points = point_index.get(peer["cell_id"], [])
            left_anchors = {anchor["key"] for point in left_points for anchor in point.get("anchors", []) if anchor.get("key")}
            right_anchors = {anchor["key"] for point in right_points for anchor in point.get("anchors", []) if anchor.get("key")}
            shared_anchor_ratio = (
                len(left_anchors & right_anchors) / max(1, len(left_anchors | right_anchors))
                if (left_anchors or right_anchors)
                else 0.0
            )
            scene_divergence = 0.0 if cell["dominant_scene"] == peer["dominant_scene"] else 1.0
            elevation_gradient = abs(float(cell["elevation"]) - float(peer["elevation"]))
            stability_gradient = abs(float(cell["stability"]) - float(peer["stability"]))
            fog_gradient = abs(float(cell["fog"]) - float(peer["fog"]))
            boundary_score = min(
                1.0,
                scene_divergence * 0.35
                + (1.0 - shared_anchor_ratio) * 0.3
                + elevation_gradient * 0.18
                + stability_gradient * 0.1
                + fog_gradient * 0.07,
            )
            flow_direction = math.degrees(math.atan2(float(peer["y"]) - float(cell["y"]), float(peer["x"]) - float(cell["x"])))
            flow_magnitude = min(1.0, shared_anchor_ratio * 0.6 + (1.0 - fog_gradient) * 0.2 + (1.0 - boundary_score) * 0.2)
            rows.append(
                {
                    "edge_id": f"edge_{cell['cell_id']}_{peer['cell_id']}",
                    "from_cell_id": cell["cell_id"],
                    "to_cell_id": peer["cell_id"],
                    "region_boundary_score": round(boundary_score, 3),
                    "shared_anchor_ratio": round(shared_anchor_ratio, 3),
                    "scene_divergence": round(scene_divergence, 3),
                    "elevation_gradient": round(elevation_gradient, 3),
                    "stability_gradient": round(stability_gradient, 3),
                    "fog_gradient": round(fog_gradient, 3),
                    "flow_magnitude": round(flow_magnitude, 3),
                    "flow_direction": round(flow_direction, 1),
                }
            )
    return rows


def _build_cell_fields(
    cells: List[Dict[str, object]],
    neighbors: Dict[str, List[Dict[str, object]]],
    point_index: Dict[str, List[Dict[str, object]]],
    edge_fields: List[Dict[str, object]],
    water_flows: List[Dict[str, object]],
    wind_fields: List[Dict[str, object]],
    fault_lines: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    edge_index: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for edge in edge_fields:
        edge_index[edge["from_cell_id"]].append(edge)
        edge_index[edge["to_cell_id"]].append(edge)

    water_hits = _count_path_hits(water_flows)
    wind_hits = _count_point_hits(wind_fields)
    fault_hits = _count_point_hits(fault_lines)

    rows: List[Dict[str, object]] = []
    for cell in cells:
        peers = neighbors.get(cell["cell_id"], [])
        cell_edges = edge_index.get(cell["cell_id"], [])
        points = point_index.get(cell["cell_id"], [])
        neighbor_elevations = [float(peer["elevation"]) for peer in peers] or [float(cell["elevation"])]
        local_max_delta = max(0.0, float(cell["elevation"]) - max(neighbor_elevations))
        local_min_delta = max(0.0, min(neighbor_elevations) - float(cell["elevation"]))
        mean_boundary = sum(edge["region_boundary_score"] for edge in cell_edges) / max(1, len(cell_edges))
        anchor_counts = Counter(
            anchor["key"]
            for point in points
            for anchor in point.get("anchors", [])
            if anchor.get("key")
        )
        scene_mix = Counter(point.get("scene", "unknown") for point in points)
        role_mix = Counter(point.get("observer_role", "") for point in points if point.get("observer_role"))
        water_count = water_hits.get(cell["cell_id"], 0)
        wind_count = wind_hits.get(cell["cell_id"], 0)
        fault_count = fault_hits.get(cell["cell_id"], 0)

        ridge_score = min(
            1.0,
            float(cell["elevation"]) * 0.45
            + float(cell["stability"]) * 0.25
            + local_max_delta * 0.55
            + mean_boundary * 0.15,
        )
        valley_score = min(
            1.0,
            (1.0 - float(cell["elevation"])) * 0.4
            + local_min_delta * 0.55
            + min(1.0, water_count / 3.0) * 0.25
            + min(1.0, len(anchor_counts) / 6.0) * 0.08,
        )
        basin_score = min(
            1.0,
            (1.0 - float(cell["elevation"])) * 0.35
            + float(cell["fog"]) * 0.3
            + (1.0 - min(1.0, water_count / 4.0)) * 0.15
            + (1.0 - float(cell["stability"])) * 0.1
            + min(1.0, len(anchor_counts) / 8.0) * 0.1,
        )
        wind_pressure = min(
            1.0,
            float(cell["fog"]) * 0.35
            + min(1.0, wind_count / 3.0) * 0.35
            + min(1.0, fault_count / 2.0) * 0.2
            + mean_boundary * 0.1,
        )
        rows.append(
            {
                "cell_id": cell["cell_id"],
                "region_identity_signature": {
                    "dominant_scene": cell["dominant_scene"],
                    "dominant_role": role_mix.most_common(1)[0][0] if role_mix else "",
                    "top_anchors": [name for name, _ in anchor_counts.most_common(5)],
                    "scene_mix": dict(scene_mix),
                    "role_mix": dict(role_mix),
                    "dis_vector": [
                        round(float(cell["elevation"]), 3),
                        round(float(cell["stability"]), 3),
                        round(1.0 - float(cell["fog"]), 3),
                    ],
                    "material_density": len(points),
                },
                "region_boundary_mean": round(mean_boundary, 3),
                "ridge_axis_score": round(ridge_score, 3),
                "valley_channel_score": round(valley_score, 3),
                "basin_retention_score": round(basin_score, 3),
                "anchor_flow_field": {
                    "flow_magnitude_mean": round(
                        sum(edge["flow_magnitude"] for edge in cell_edges) / max(1, len(cell_edges)), 3
                    ),
                    "shared_anchor_count": len(anchor_counts),
                },
                "climate_zone_signature": _climate_zone(cell["dominant_scene"], float(cell["fog"]), float(cell["stability"]), wind_pressure, float(cell["elevation"])),
                "wind_pressure_field": round(wind_pressure, 3),
            }
        )
    return rows


def _build_region_fields(
    regions: List[Dict[str, object]],
    cells: List[Dict[str, object]],
    cell_fields: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    field_lookup = {row["cell_id"]: row for row in cell_fields}
    cell_lookup = {row["cell_id"]: row for row in cells}
    rows: List[Dict[str, object]] = []
    for region in regions:
        field_rows = []
        left = float(region["x"]) - float(region["width"]) / 2
        right = float(region["x"]) + float(region["width"]) / 2
        top = float(region["y"]) - float(region["height"]) / 2
        bottom = float(region["y"]) + float(region["height"]) / 2
        for cell_id, cell in cell_lookup.items():
            if left <= float(cell["x"]) <= right and top <= float(cell["y"]) <= bottom:
                field = field_lookup.get(cell_id)
                if field:
                    field_rows.append(field)
        if field_rows:
            ridge = sum(row["ridge_axis_score"] for row in field_rows) / len(field_rows)
            valley = sum(row["valley_channel_score"] for row in field_rows) / len(field_rows)
            basin = sum(row["basin_retention_score"] for row in field_rows) / len(field_rows)
            wind = sum(row["wind_pressure_field"] for row in field_rows) / len(field_rows)
            climate = Counter(row["climate_zone_signature"] for row in field_rows).most_common(1)[0][0]
        else:
            ridge = valley = basin = wind = 0.0
            climate = "unknown_zone"
        rows.append(
            {
                "local_space_id": region["local_space_id"],
                "region_boundary_intensity": round(min(1.0, 0.25 + len(region.get("bridge_trace_refs", [])) * 0.18), 3),
                "ridge_presence": round(ridge, 3),
                "valley_presence": round(valley, 3),
                "basin_presence": round(basin, 3),
                "wind_pressure_mean": round(wind, 3),
                "climate_zone": climate,
            }
        )
    return rows


def _count_path_hits(flows: List[Dict[str, object]]) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for flow in flows:
        for key in ("from_fragment_id", "to_fragment_id"):
            frag_id = flow.get(key)
            if frag_id:
                counts[str(frag_id).replace("matpt_", "terrain_approx_")] += 1
    return counts


def _count_point_hits(rows: List[Dict[str, object]]) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    step = 28
    for row in rows:
        x = int(float(row["x"]) // step) * step
        y = int(float(row["y"]) // step) * step
        counts[f"terrain_{x}_{y}"] += 1
    return counts


def _climate_zone(scene: str, fog: float, stability: float, wind_pressure: float, elevation: float) -> str:
    if fog >= 0.48 and wind_pressure >= 0.45:
        return "storm_fog"
    if fog >= 0.46:
        return "mist_basin"
    if scene == "comparison" and stability >= 0.62:
        return "ridge_divide"
    if elevation >= 0.68 and stability >= 0.64:
        return "dry_highland"
    if scene == "evidence":
        return "rock_exposure"
    return "temperate_plain"
