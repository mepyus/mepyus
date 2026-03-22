#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService


def _family_material_ids(runtime_root: Path, family_id: str) -> set:
    materials_root = runtime_root / "core" / "materials"
    material_ids = set()
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("family_id") == family_id:
            material_ids.add(record["material_id"])
    if not material_ids:
        raise RuntimeError("missing family materials for: %s" % family_id)
    return material_ids


def _latest_local_space_for_family(runtime_root: Path, family_id: str) -> dict:
    family_material_ids = _family_material_ids(runtime_root, family_id)
    cells_root = runtime_root / "core" / "space_cells"
    local_spaces_root = runtime_root / "core" / "local_spaces"

    matching_cell_ids = set()
    for path in sorted(cells_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if set(record.get("material_refs", ())) & family_material_ids:
            matching_cell_ids.add(record["cell_id"])
    if not matching_cell_ids:
        raise RuntimeError("missing cells for family: %s" % family_id)

    matches = []
    for path in sorted(local_spaces_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if set(record.get("cell_refs", ())) & matching_cell_ids:
            matches.append(record)
    if not matches:
        raise RuntimeError("missing local space for family: %s" % family_id)
    return matches[-1]


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    temporal_space = _latest_local_space_for_family(runtime_root, "seed-third-wave")
    reflective_space = _latest_local_space_for_family(runtime_root, "seed-seventh-wave")

    bridge = service.derive_bridge_trace_from_local_spaces(
        from_local_space_id=temporal_space["local_space_id"],
        to_local_space_id=reflective_space["local_space_id"],
        note="Fifteenth step opens a weak bridge-facing exposure between temporal-project and reflective terrains.",
    )
    if bridge is None:
        raise RuntimeError("failed to derive bridge-facing exposure")

    lines = [
        "runtime_root: %s" % runtime_root,
        "from_local_space_id: %s" % temporal_space["local_space_id"],
        "to_local_space_id: %s" % reflective_space["local_space_id"],
        "bridge_id: %s" % bridge.bridge_id,
        "bridge_state: %s" % bridge.state.value,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
