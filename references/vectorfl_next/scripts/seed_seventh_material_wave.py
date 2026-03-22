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
        raise RuntimeError("expected existing local spaces before seventh wave")
    return records[-1]["local_space_id"]


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    latest_temporal_trace = _latest_trace_by_kind(runtime_root, "fifth_wave_temporal_return")
    adjacent_local_space_id = _latest_local_space_id(runtime_root)

    seventh_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Seventh wave note: a reflective terrain opens on its own axis and should remain separate from both "
            "the resonant observer-facing terrain and the temporal-project terrain."
        ),
        actor_id="codex",
        session_id="bootstrap-seventh-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:seventh-wave:reflective-field",
        formation_role="fresh_material",
        family_id="seed-seventh-wave",
        lineage_refs=[observer["material_id"]],
    )
    seventh_wave_trace = service.register_trace(
        material_refs=[seventh_wave_material.material_id, observer["material_id"]],
        evidence_kind="seventh_wave_reflective_field",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=seventh_wave_material.material_id, note="seventh_wave_fresh"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
            SupportRef(ref_kind="trace", ref_id=latest_temporal_trace["trace_id"], note="temporal_field_reference"),
        ],
        note="Seventh wave keeps only a weak reference to prior terrain while opening its own reflective field.",
    )
    seventh_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="reflection_pressure", strength_hint=0.93),
            PressureAxis(axis="recurrence_pressure", strength_hint=0.74),
            PressureAxis(axis="project_pressure", strength_hint=0.36),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=seventh_wave_material.material_id, note="seventh_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=seventh_wave_trace.trace_id, note="seventh_wave_reflective_field"),
        ],
    )
    seventh_wave_seed = service.create_point_seed_candidate(
        material_refs=[seventh_wave_material.material_id],
        trace_refs=[seventh_wave_trace.trace_id],
        pressure_profile_id=seventh_wave_pressure.profile_id,
    )
    seventh_cell = service.create_space_cell_candidate(
        material_refs=[seventh_wave_material.material_id, observer["material_id"]],
        trace_refs=[seventh_wave_trace.trace_id],
        seed_refs=[seventh_wave_seed.seed_id],
        pressure_profile_id=seventh_wave_pressure.profile_id,
        interior_refs=[
            seventh_wave_material.material_id,
            seventh_wave_seed.seed_id,
            seventh_wave_trace.trace_id,
        ],
        exterior_refs=[
            observer["material_id"],
            engine_self["material_id"],
            adjacent_local_space_id,
        ],
        cohesion_note="Seventh wave opens a reflective terrain on a distinct axis without creating another adjacency bridge.",
    )
    service.reactivate_space_cell(
        seventh_cell.cell_id,
        "relocation",
        pressure_profile_id=seventh_wave_pressure.profile_id,
        note="Seventh wave lands as another independent terrain on a reflective axis.",
        triggered_by_seed_ids=[seventh_wave_seed.seed_id],
    )
    seventh_local_space = service.form_local_space([seventh_cell.cell_id], seventh_wave_pressure.profile_id)

    lines = [
        "runtime_root: %s" % runtime_root,
        "seventh_wave_material_id: %s" % seventh_wave_material.material_id,
        "seventh_wave_trace_id: %s" % seventh_wave_trace.trace_id,
        "seventh_wave_pressure_id: %s" % seventh_wave_pressure.profile_id,
        "seventh_wave_seed_id: %s" % seventh_wave_seed.seed_id,
        "seventh_cell_id: %s" % seventh_cell.cell_id,
        "seventh_local_space_id: %s" % seventh_local_space.local_space_id,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
