from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input_space import enrich_bridge_trace, register_live_input_bridges
from app.core.runtime.region_atlas import write_region_atlas_view
from app.core.runtime.terrain_map import write_terrain_map_view


def _local_space_payload(service: FormationService, local_space_id: str) -> tuple[list[str], list[str]]:
    local_space = service.local_spaces.get(local_space_id) or {}
    material_ids: list[str] = []
    trace_ids: list[str] = []
    for cell_id in local_space.get("cell_refs", []):
        cell = service.cells.get(str(cell_id)) or {}
        material_ids.extend(str(row) for row in cell.get("material_refs", []))
        trace_ids.extend(str(row) for row in cell.get("trace_refs", []))
    return sorted(set(material_ids)), sorted(set(trace_ids))


def main() -> None:
    runtime_root = Path("runtime")
    service = FormationService(runtime_root)
    updates: list[dict[str, object]] = []
    for local_space in service.local_spaces.read_all():
        local_space_id = str(local_space.get("local_space_id", "")).strip()
        if not local_space_id:
            continue
        material_ids, trace_ids = _local_space_payload(service, local_space_id)
        if not material_ids or not trace_ids:
            continue
        bridge_rows = register_live_input_bridges(
            service,
            new_local_space_id=local_space_id,
            material_ids=material_ids,
            trace_ids=trace_ids,
        )
        if bridge_rows:
            updates.extend(bridge_rows)

    for bridge in service.bridges.read_all():
        note = str(bridge.get("note", ""))
        if bridge.get("shared_anchors") or not note.startswith("canonical shared anchors: "):
            if bridge.get("bridge_id"):
                enrich_bridge_trace(service, str(bridge.get("bridge_id", "")))
            continue
        labels = [row.strip() for row in note.split(":", 1)[1].split(",") if row.strip()]
        if labels:
            bridge["shared_anchors"] = [
                {
                    "canonical_key": label.lower().replace(" ", "_"),
                    "display_label": label,
                    "anchor_type": "semantic",
                    "bridge_score": 0.72,
                }
                for label in labels[:4]
            ]
            service.bridges.put(str(bridge.get("bridge_id", "")), bridge)
        if bridge.get("bridge_id"):
            enrich_bridge_trace(service, str(bridge.get("bridge_id", "")))

    atlas_paths = write_region_atlas_view(runtime_root)
    terrain_paths = write_terrain_map_view(runtime_root)
    summary = {
        "updated_bridge_count": len(updates),
        "updates": updates,
        "atlas_json": str(atlas_paths["json"]),
        "atlas_html": str(atlas_paths["html"]),
        "terrain_json": str(terrain_paths["json"]),
        "terrain_html": str(terrain_paths["html"]),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
