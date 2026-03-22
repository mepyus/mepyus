from pathlib import Path
import json

from app.runtime.observer import build_reactive_space_observation


def build_sparse_presence_review(runtime_root: Path) -> dict:
    observation = build_reactive_space_observation(runtime_root)
    local_spaces_root = runtime_root / "core" / "local_spaces"
    cells_root = runtime_root / "core" / "space_cells"
    materials_root = runtime_root / "core" / "materials"

    material_map = {}
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        material_map[record["material_id"]] = record

    quiet_local_space_ids = []
    quiet_role_counts = {}

    for path in sorted(local_spaces_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("state") != "forming" and record.get("bridge_refs"):
            continue

        quiet_local_space_ids.append(record["local_space_id"])
        family_roles = set()
        for cell_id in record.get("cell_refs", ()):
            cell_path = cells_root / ("%s.json" % cell_id)
            cell = json.loads(cell_path.read_text(encoding="utf-8"))
            for material_id in cell.get("material_refs", ()):
                material = material_map.get(material_id, {})
                role = material.get("metadata", {}).get("formation_role")
                if role:
                    family_roles.add(role)
        for role in family_roles:
            quiet_role_counts[role] = quiet_role_counts.get(role, 0) + 1

    return {
        "runtime_root": str(runtime_root),
        "quiet_local_space_count": len(quiet_local_space_ids),
        "quiet_local_space_ids": quiet_local_space_ids,
        "quiet_role_counts": quiet_role_counts,
        "bridge_exposed_local_space_count": observation["local_space_states"].get("bridge_exposed", 0),
        "forming_local_space_count": observation["local_space_states"].get("forming", 0),
        "sparse_retention_component_count": observation["terrain_retention_modes"].get("sparse_retention", 0),
        "light_forgetting_component_count": observation["terrain_forgetting_modes"].get("light_forgetting", 0),
        "terrain_component_count": len(observation["terrain_components"]),
        "process_summary": observation["process_summary"]["summary_line"],
    }
