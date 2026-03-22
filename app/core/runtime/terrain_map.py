from __future__ import annotations

from pathlib import Path
from typing import Dict
import json

from app.fragment.store import FragmentStore
from app.runtime.file_store import JsonDirectoryStore
from app.core.runtime.semantic_terrain_fields import build_semantic_terrain_fields
from app.core.runtime.semantic_terrain_geometry import build_semantic_terrain_geometry
from app.core.runtime.terrain_map_regions import build_region_flows, build_regions
from app.core.runtime.terrain_map_builders import (
    build_contour_lines,
    build_fault_lines,
    build_fragment_points,
    build_imported_material_points,
    build_material_features,
    build_terrain_cells,
    build_water_flows,
    build_wind_fields,
)
from app.core.runtime.terrain_map_render import render_terrain_map_html


def build_terrain_map_data(runtime_root: Path) -> Dict[str, object]:
    fragment_store = FragmentStore(runtime_root)
    material_store = JsonDirectoryStore(runtime_root / "core" / "materials")
    local_space_store = JsonDirectoryStore(runtime_root / "core" / "local_spaces")
    cell_store = JsonDirectoryStore(runtime_root / "core" / "space_cells")
    bridge_store = JsonDirectoryStore(runtime_root / "core" / "bridge_traces")

    fragments = sorted(fragment_store.read_all(), key=lambda row: row.created_at)
    materials = sorted(material_store.read_all(), key=lambda row: row.get("created_at", ""))
    local_spaces = local_space_store.read_all()
    cells = cell_store.read_all()
    bridges = bridge_store.read_all()

    fragment_points, fragment_lookup, source_summary = build_fragment_points(fragments)
    imported_material_points = build_imported_material_points(materials, fragment_lookup, len(source_summary))
    sample_points = fragment_points + imported_material_points
    terrain_cells = build_terrain_cells(sample_points)
    contour_lines = build_contour_lines(terrain_cells)
    material_features = build_material_features(materials, fragment_lookup, imported_material_points)
    regions = build_regions(local_spaces, cells, material_features, bridges)
    region_flows = build_region_flows(regions, bridges)
    water_flows = build_water_flows(sample_points)
    wind_fields = build_wind_fields(sample_points)
    fault_lines = build_fault_lines(sample_points)

    semantic_fields = build_semantic_terrain_fields(
        cells=terrain_cells,
        sample_points=sample_points,
        regions=regions,
        water_flows=water_flows,
        wind_fields=wind_fields,
        fault_lines=fault_lines,
    )
    semantic_geometry = build_semantic_terrain_geometry(
        cells=terrain_cells,
        regions=regions,
        contour_lines=contour_lines,
        region_flows=region_flows,
        fault_lines=fault_lines,
        fields=semantic_fields,
    )

    return {
        "summary": {
            "fragment_count": len(fragment_points),
            "imported_point_count": len(imported_material_points),
            "sample_point_count": len(sample_points),
            "material_count": len(material_features),
            "local_space_count": len(local_spaces),
            "bridge_count": len(bridges),
            "terrain_cell_count": len(terrain_cells),
            "contour_line_count": len(contour_lines),
            "water_flow_count": len(water_flows),
            "wind_field_count": len(wind_fields),
            "region_flow_count": len(region_flows),
            "semantic_cell_field_count": len(semantic_fields["cell_fields"]),
            "semantic_edge_field_count": len(semantic_fields["edge_fields"]),
            "semantic_region_field_count": len(semantic_fields["region_fields"]),
            "semantic_geometry_count": sum(len(rows) for rows in semantic_geometry.values()),
            "source_count": len(source_summary),
        },
        "sources": source_summary,
        "cells": terrain_cells,
        "contour_lines": contour_lines,
        "fragment_points": fragment_points,
        "imported_material_points": imported_material_points,
        "sample_points": sample_points,
        "material_features": material_features,
        "regions": regions,
        "region_flows": region_flows,
        "water_flows": water_flows,
        "wind_fields": wind_fields,
        "fault_lines": fault_lines,
        "semantic_fields": semantic_fields,
        "semantic_geometry": semantic_geometry,
    }


def write_terrain_map_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_terrain_map_data(runtime_root)
    reports_root = runtime_root / "reports"
    reports_root.mkdir(parents=True, exist_ok=True)
    json_path = reports_root / "terrain_map_view.json"
    html_path = reports_root / "terrain_map_view.html"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    html_path.write_text(render_terrain_map_html(data), encoding="utf-8")
    return {"json_path": json_path, "html_path": html_path}
