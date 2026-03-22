#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService


def _find_material_by_role(runtime_root: Path, formation_role: str) -> dict:
    materials_root = runtime_root / "core" / "materials"
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("metadata", {}).get("formation_role") == formation_role:
            return record
    raise RuntimeError("missing material for role: %s" % formation_role)


def _find_trace_by_kind(runtime_root: Path, evidence_kind: str) -> dict:
    traces_root = runtime_root / "core" / "traces"
    for path in sorted(traces_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("evidence_kind") == evidence_kind:
            return record
    raise RuntimeError("missing trace for evidence kind: %s" % evidence_kind)


def _require_single_seed(runtime_root: Path) -> dict:
    seeds_root = runtime_root / "core" / "point_seeds"
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(seeds_root.glob("*.json"))]
    if len(records) != 1:
        raise RuntimeError("expected exactly one seed before first convergence, found %s" % len(records))
    return records[0]


def _require_no_cells(runtime_root: Path) -> None:
    cells_root = runtime_root / "core" / "space_cells"
    count = len(list(cells_root.glob("*.json")))
    if count != 0:
        raise RuntimeError("expected no preexisting space cells before first convergence, found %s" % count)


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    _require_no_cells(runtime_root)
    fresh = _find_material_by_role(runtime_root, "fresh_material")
    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    observer_reflection = _find_trace_by_kind(runtime_root, "observer_reflection")
    fresh_pressure_hint = _find_trace_by_kind(runtime_root, "fresh_pressure_hint")
    seed = _require_single_seed(runtime_root)

    cell = service.create_space_cell_candidate(
        material_refs=[fresh["material_id"], observer["material_id"]],
        trace_refs=[observer_reflection["trace_id"], fresh_pressure_hint["trace_id"]],
        seed_refs=[seed["seed_id"]],
        pressure_profile_id=seed["pressure_profile_id"],
        interior_refs=[
            fresh["material_id"],
            observer["material_id"],
            seed["seed_id"],
            fresh_pressure_hint["trace_id"],
        ],
        exterior_refs=[
            engine_self["material_id"],
            observer_reflection["trace_id"],
        ],
        cohesion_note="Initial convergence cell: fresh pressure terrain meets observer-facing weak relation while engine-self remains exterior.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "cell_id: %s" % cell.cell_id,
        "cell_state: %s" % cell.state.value,
        "material_refs: %s" % ",".join(cell.material_refs),
        "trace_refs: %s" % ",".join(cell.trace_refs),
        "exterior_refs: %s" % ",".join(cell.boundary.exterior_refs),
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
