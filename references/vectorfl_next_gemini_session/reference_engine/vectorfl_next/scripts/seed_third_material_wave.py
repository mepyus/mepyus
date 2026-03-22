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
        raise RuntimeError("expected existing local spaces before third wave")
    return records[-1]["local_space_id"]


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    second_wave_trace = _latest_trace_by_kind(runtime_root, "second_wave_observer_resonance")
    adjacent_local_space_id = _latest_local_space_id(runtime_root)

    third_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Third wave note: this terrain should open with stronger temporal and project pressure, "
            "not as another observer-facing neighbor but as a distinct returning field."
        ),
        actor_id="codex",
        session_id="bootstrap-third-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:third-wave:temporal-project",
        formation_role="fresh_material",
        family_id="seed-third-wave",
        lineage_refs=[observer["material_id"]],
    )
    third_wave_trace = service.register_trace(
        material_refs=[third_wave_material.material_id, observer["material_id"]],
        evidence_kind="third_wave_temporal_project_resonance",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=third_wave_material.material_id, note="third_wave_fresh"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
            SupportRef(ref_kind="trace", ref_id=second_wave_trace["trace_id"], note="second_wave_reference"),
        ],
        note="Third wave keeps a weak observer-facing reference but opens under temporal/project pressure instead.",
    )
    third_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="temporal_pressure", strength_hint=0.92),
            PressureAxis(axis="project_pressure", strength_hint=0.83),
            PressureAxis(axis="session_pressure", strength_hint=0.42),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=third_wave_material.material_id, note="third_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=third_wave_trace.trace_id, note="third_wave_temporal_project_resonance"),
        ],
    )
    third_wave_seed = service.create_point_seed_candidate(
        material_refs=[third_wave_material.material_id],
        trace_refs=[third_wave_trace.trace_id],
        pressure_profile_id=third_wave_pressure.profile_id,
    )
    third_cell = service.create_space_cell_candidate(
        material_refs=[third_wave_material.material_id, observer["material_id"]],
        trace_refs=[third_wave_trace.trace_id],
        seed_refs=[third_wave_seed.seed_id],
        pressure_profile_id=third_wave_pressure.profile_id,
        interior_refs=[
            third_wave_material.material_id,
            third_wave_seed.seed_id,
            third_wave_trace.trace_id,
        ],
        exterior_refs=[
            observer["material_id"],
            engine_self["material_id"],
            adjacent_local_space_id,
        ],
        cohesion_note="Third wave opens a distinct temporal-project terrain rather than another observer-facing adjacency.",
    )
    service.reactivate_space_cell(
        third_cell.cell_id,
        "relocation",
        pressure_profile_id=third_wave_pressure.profile_id,
        note="Third wave lands as its own terrain with shifted temporal-project pressure.",
        triggered_by_seed_ids=[third_wave_seed.seed_id],
    )
    third_local_space = service.form_local_space([third_cell.cell_id], third_wave_pressure.profile_id)

    lines = [
        "runtime_root: %s" % runtime_root,
        "third_wave_material_id: %s" % third_wave_material.material_id,
        "third_wave_trace_id: %s" % third_wave_trace.trace_id,
        "third_wave_pressure_id: %s" % third_wave_pressure.profile_id,
        "third_wave_seed_id: %s" % third_wave_seed.seed_id,
        "third_cell_id: %s" % third_cell.cell_id,
        "third_local_space_id: %s" % third_local_space.local_space_id,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
