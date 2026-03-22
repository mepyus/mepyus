#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef


def _latest_trace_by_kind(runtime_root: Path, evidence_kind: str) -> dict:
    traces_root = runtime_root / "core" / "traces"
    matches = []
    for path in sorted(traces_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("evidence_kind") == evidence_kind:
            matches.append(record)
    if not matches:
        raise RuntimeError("missing trace for evidence kind: %s" % evidence_kind)
    return matches[-1]


def _latest_cell_for_family(runtime_root: Path, family_id: str) -> dict:
    materials_root = runtime_root / "core" / "materials"
    family_material_ids = set()
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("family_id") == family_id:
            family_material_ids.add(record["material_id"])
    if not family_material_ids:
        raise RuntimeError("missing family materials for: %s" % family_id)
    cells_root = runtime_root / "core" / "space_cells"
    matches = []
    for path in sorted(cells_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if set(record.get("material_refs", ())) & family_material_ids:
            matches.append(record)
    if not matches:
        raise RuntimeError("missing cell for family: %s" % family_id)
    return matches[-1]


def _local_space_for_cell(service: FormationService, cell_id: str) -> str:
    for record in service.local_spaces.read_all():
        if cell_id in record.get("cell_refs", ()):
            return record["local_space_id"]
    raise RuntimeError("missing local space for cell: %s" % cell_id)


def _pressure_profile(runtime_root: Path, profile_id: str) -> dict:
    path = runtime_root / "core" / "pressure_profiles" / ("%s.json" % profile_id)
    if not path.exists():
        raise RuntimeError("missing pressure profile: %s" % profile_id)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    third_cell = _latest_cell_for_family(runtime_root, "seed-third-wave")
    third_trace = _latest_trace_by_kind(runtime_root, "third_wave_temporal_project_resonance")
    third_local_space_id = _local_space_for_cell(service, third_cell["cell_id"])
    third_profile = _pressure_profile(runtime_root, third_cell["pressure_profile_id"])

    fourth_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Fourth wave note: temporal-project terrain returns under nearly the same pressure and should "
            "thicken the independent third terrain without creating a new bridge."
        ),
        actor_id="codex",
        session_id="bootstrap-fourth-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:fourth-wave:temporal-project-reentry",
        formation_role="fresh_material",
        family_id="seed-third-wave",
        lineage_refs=list(third_cell.get("material_refs", ())),
    )
    fourth_wave_trace = service.register_trace(
        material_refs=[fourth_wave_material.material_id],
        evidence_kind="fourth_wave_temporal_return",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fourth_wave_material.material_id, note="fourth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=third_trace["trace_id"], note="third_wave_temporal_project_resonance"),
        ],
        note="Fourth wave returns to the temporal-project terrain without opening another neighboring terrain.",
    )
    fourth_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis=axis["axis"], strength_hint=axis["strength_hint"])
            for axis in third_profile.get("axes", [])
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fourth_wave_material.material_id, note="fourth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=fourth_wave_trace.trace_id, note="fourth_wave_temporal_return"),
        ],
    )
    fourth_wave_seed = service.create_reentry_seed_for_family(
        family_id="seed-third-wave",
        material_refs=[fourth_wave_material.material_id],
        trace_refs=[fourth_wave_trace.trace_id],
        pressure_profile_id=fourth_wave_pressure.profile_id,
    )
    updated_cell = service.create_or_branch_space_cell_for_family(
        family_id="seed-third-wave",
        material_refs=[fourth_wave_material.material_id],
        trace_refs=[fourth_wave_trace.trace_id],
        seed_refs=[fourth_wave_seed.seed_id],
        pressure_profile_id=fourth_wave_pressure.profile_id,
        interior_refs=[fourth_wave_material.material_id, fourth_wave_seed.seed_id, fourth_wave_trace.trace_id],
        exterior_refs=third_cell["boundary"]["exterior_refs"],
        cohesion_note="Fourth wave thickens the third terrain instead of branching it again.",
    )
    reactivated = service.reactivate_space_cell(
        updated_cell.cell_id,
        "thickening",
        pressure_profile_id=fourth_wave_pressure.profile_id,
        note="Fourth wave thickens the temporal-project terrain under matching pressure.",
        triggered_by_seed_ids=[fourth_wave_seed.seed_id],
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "fourth_wave_material_id: %s" % fourth_wave_material.material_id,
        "fourth_wave_trace_id: %s" % fourth_wave_trace.trace_id,
        "fourth_wave_pressure_id: %s" % fourth_wave_pressure.profile_id,
        "fourth_wave_seed_id: %s" % fourth_wave_seed.seed_id,
        "third_local_space_id: %s" % third_local_space_id,
        "cell_id: %s" % reactivated["cell_id"],
        "cell_state: %s" % reactivated["state"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
