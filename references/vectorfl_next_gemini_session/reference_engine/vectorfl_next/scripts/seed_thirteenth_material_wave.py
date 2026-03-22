#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef


def _find_material_by_role(runtime_root: Path, formation_role: str) -> dict:
    materials_root = runtime_root / "core" / "materials"
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("metadata", {}).get("formation_role") == formation_role:
            return record
    raise RuntimeError("missing material for role: %s" % formation_role)


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


def _latest_local_space_id(runtime_root: Path) -> str:
    root = runtime_root / "core" / "local_spaces"
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(root.glob("*.json"))]
    if not records:
        raise RuntimeError("expected existing local spaces before thirteenth wave")
    return records[-1]["local_space_id"]


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    constraint_trace = _latest_trace_by_kind(runtime_root, "twelfth_wave_constraint_return")
    latest_local_space_id = _latest_local_space_id(runtime_root)

    thirteenth_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Thirteenth wave note: a latency-drift-ambiguity field enters the runtime and should open as its own "
            "terrain rather than collapsing into the existing observer-facing, temporal-project, reflective, or constraint terrains."
        ),
        actor_id="codex",
        session_id="bootstrap-thirteenth-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:thirteenth-wave:drift-band",
        formation_role="fresh_material",
        family_id="seed-thirteenth-wave",
        lineage_refs=[observer["material_id"]],
    )
    thirteenth_wave_trace = service.register_trace(
        material_refs=[thirteenth_wave_material.material_id, observer["material_id"]],
        evidence_kind="thirteenth_wave_drift_field",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=thirteenth_wave_material.material_id, note="thirteenth_wave_fresh"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
            SupportRef(ref_kind="trace", ref_id=constraint_trace["trace_id"], note="constraint_reference"),
        ],
        note="Thirteenth wave opens a drift-heavy field with only weak reference to prior terrain.",
    )
    thirteenth_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="latency_pressure", strength_hint=0.91),
            PressureAxis(axis="drift_pressure", strength_hint=0.87),
            PressureAxis(axis="ambiguity_pressure", strength_hint=0.84),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=thirteenth_wave_material.material_id, note="thirteenth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=thirteenth_wave_trace.trace_id, note="thirteenth_wave_drift_field"),
        ],
    )
    thirteenth_wave_seed = service.create_point_seed_candidate(
        material_refs=[thirteenth_wave_material.material_id],
        trace_refs=[thirteenth_wave_trace.trace_id],
        pressure_profile_id=thirteenth_wave_pressure.profile_id,
    )
    thirteenth_cell = service.create_space_cell_candidate(
        material_refs=[thirteenth_wave_material.material_id, observer["material_id"]],
        trace_refs=[thirteenth_wave_trace.trace_id],
        seed_refs=[thirteenth_wave_seed.seed_id],
        pressure_profile_id=thirteenth_wave_pressure.profile_id,
        interior_refs=[
            thirteenth_wave_material.material_id,
            thirteenth_wave_seed.seed_id,
            thirteenth_wave_trace.trace_id,
        ],
        exterior_refs=[
            observer["material_id"],
            engine_self["material_id"],
            latest_local_space_id,
        ],
        cohesion_note="Thirteenth wave opens a drift-heavy terrain on a distinct pressure band without creating adjacency.",
    )
    service.reactivate_space_cell(
        thirteenth_cell.cell_id,
        "relocation",
        pressure_profile_id=thirteenth_wave_pressure.profile_id,
        note="Thirteenth wave lands as its own independent drift-heavy terrain.",
        triggered_by_seed_ids=[thirteenth_wave_seed.seed_id],
    )
    thirteenth_local_space = service.form_local_space([thirteenth_cell.cell_id], thirteenth_wave_pressure.profile_id)

    lines = [
        "runtime_root: %s" % runtime_root,
        "thirteenth_wave_material_id: %s" % thirteenth_wave_material.material_id,
        "thirteenth_wave_trace_id: %s" % thirteenth_wave_trace.trace_id,
        "thirteenth_wave_pressure_id: %s" % thirteenth_wave_pressure.profile_id,
        "thirteenth_wave_seed_id: %s" % thirteenth_wave_seed.seed_id,
        "thirteenth_cell_id: %s" % thirteenth_cell.cell_id,
        "thirteenth_local_space_id: %s" % thirteenth_local_space.local_space_id,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
