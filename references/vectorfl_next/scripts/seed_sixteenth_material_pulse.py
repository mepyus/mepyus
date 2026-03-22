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


def _latest_bridge_between_spaces(runtime_root: Path, left_space_id: str, right_space_id: str) -> dict:
    bridges_root = runtime_root / "core" / "bridge_traces"
    normalized = tuple(sorted((left_space_id, right_space_id)))
    matches = []
    for path in sorted(bridges_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        pair = tuple(sorted((record["from_local_space_id"], record["to_local_space_id"])))
        if pair == normalized:
            matches.append(record)
    if not matches:
        raise RuntimeError("missing bridge between spaces: %s %s" % normalized)
    return matches[-1]


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    temporal_space = _latest_local_space_for_family(runtime_root, "seed-third-wave")
    reflective_space = _latest_local_space_for_family(runtime_root, "seed-seventh-wave")
    fifteenth_bridge = _latest_bridge_between_spaces(
        runtime_root,
        temporal_space["local_space_id"],
        reflective_space["local_space_id"],
    )

    pulse_material = service.ingest_material_with_role(
        raw_payload=(
            "Sixteenth pulse note: a single mixed temporal-reflective pulse enters between two already mature terrains "
            "and should open a small pulse terrain without collapsing either side."
        ),
        actor_id="codex",
        session_id="bootstrap-sixteenth-pulse",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="pulse:sixteenth:temporal-reflective",
        formation_role="fresh_material",
        family_id="seed-sixteenth-pulse",
        lineage_refs=[observer["material_id"]],
    )
    pulse_trace = service.register_trace(
        material_refs=[pulse_material.material_id, observer["material_id"]],
        evidence_kind="sixteenth_temporal_reflective_pulse",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=pulse_material.material_id, note="pulse_fresh"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
            SupportRef(ref_kind="bridge_trace", ref_id=fifteenth_bridge["bridge_id"], note="prior_bridge_exposure"),
        ],
        note="A single pulse lands near the temporal-reflective exposure without collapsing either terrain.",
    )
    pulse_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="temporal_pressure", strength_hint=0.79),
            PressureAxis(axis="reflection_pressure", strength_hint=0.76),
            PressureAxis(axis="recurrence_pressure", strength_hint=0.41),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=pulse_material.material_id, note="pulse_fresh"),
            SupportRef(ref_kind="trace", ref_id=pulse_trace.trace_id, note="pulse_trace"),
        ],
    )
    pulse_seed = service.create_point_seed_candidate(
        material_refs=[pulse_material.material_id],
        trace_refs=[pulse_trace.trace_id],
        pressure_profile_id=pulse_pressure.profile_id,
    )
    pulse_cell = service.create_space_cell_candidate(
        material_refs=[pulse_material.material_id, observer["material_id"]],
        trace_refs=[pulse_trace.trace_id],
        seed_refs=[pulse_seed.seed_id],
        pressure_profile_id=pulse_pressure.profile_id,
        interior_refs=[pulse_material.material_id, pulse_seed.seed_id, pulse_trace.trace_id],
        exterior_refs=[observer["material_id"], engine_self["material_id"], temporal_space["local_space_id"], reflective_space["local_space_id"]],
        cohesion_note="A pulse terrain forms near temporal-project and reflective fields without becoming either one.",
    )
    service.reactivate_space_cell(
        pulse_cell.cell_id,
        "relocation",
        pressure_profile_id=pulse_pressure.profile_id,
        note="The pulse lands between temporal-project and reflective terrains as a small passing field.",
        triggered_by_seed_ids=[pulse_seed.seed_id],
    )
    pulse_local_space = service.form_local_space([pulse_cell.cell_id], pulse_pressure.profile_id)

    bridge_one = service.derive_bridge_trace_from_local_spaces(
        from_local_space_id=temporal_space["local_space_id"],
        to_local_space_id=pulse_local_space.local_space_id,
        note="Pulse opens a weak exposure toward the temporal-project terrain.",
    )
    bridge_two = service.derive_bridge_trace_from_local_spaces(
        from_local_space_id=reflective_space["local_space_id"],
        to_local_space_id=pulse_local_space.local_space_id,
        note="Pulse opens a weak exposure toward the reflective terrain.",
    )
    if bridge_one is None or bridge_two is None:
        raise RuntimeError("failed to derive pulse bridge exposure")

    lines = [
        "runtime_root: %s" % runtime_root,
        "pulse_material_id: %s" % pulse_material.material_id,
        "pulse_trace_id: %s" % pulse_trace.trace_id,
        "pulse_pressure_id: %s" % pulse_pressure.profile_id,
        "pulse_seed_id: %s" % pulse_seed.seed_id,
        "pulse_cell_id: %s" % pulse_cell.cell_id,
        "pulse_local_space_id: %s" % pulse_local_space.local_space_id,
        "bridge_ids: %s,%s" % (bridge_one.bridge_id, bridge_two.bridge_id),
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
