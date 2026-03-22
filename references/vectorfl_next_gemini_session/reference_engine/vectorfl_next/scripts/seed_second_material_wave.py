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


def _latest_cell(runtime_root: Path) -> dict:
    cells_root = runtime_root / "core" / "space_cells"
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(cells_root.glob("*.json"))]
    if not records:
        raise RuntimeError("expected at least one existing cell before second wave")
    return records[-1]


def _ensure_local_space_for_cell(service: FormationService, cell_id: str, pressure_profile_id: str) -> str:
    for record in service.local_spaces.read_all():
        if cell_id in record.get("cell_refs", ()):
            return record["local_space_id"]
    local_space = service.form_local_space([cell_id], pressure_profile_id)
    return local_space.local_space_id


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    fresh = _find_material_by_role(runtime_root, "fresh_material")
    observer = _find_material_by_role(runtime_root, "observer_material")
    engine_self = _find_material_by_role(runtime_root, "engine_self_material")
    first_cell = _latest_cell(runtime_root)
    observer_reflection = _latest_trace_by_kind(runtime_root, "observer_reflection")

    second_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Second wave note: a new observer-facing pressure enters with stronger tone pressure. "
            "It should not overwrite the first cell, but open another local terrain near it."
        ),
        actor_id="codex",
        session_id="bootstrap-second-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:second-wave:observer-facing",
        formation_role="fresh_material",
        family_id="seed-fresh-note",
        lineage_refs=[fresh["material_id"], observer["material_id"]],
    )
    second_wave_trace = service.register_trace(
        material_refs=[second_wave_material.material_id, observer["material_id"]],
        evidence_kind="second_wave_observer_resonance",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=second_wave_material.material_id, note="second_wave_fresh"),
            SupportRef(ref_kind="material", ref_id=observer["material_id"], note="observer_material"),
            SupportRef(ref_kind="trace", ref_id=observer_reflection["trace_id"], note="observer_reflection"),
        ],
        note="Second wave trace keeps observer-facing pressure but shifts the terrain away from the first cell.",
    )
    second_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="session_pressure", strength_hint=0.7),
            PressureAxis(axis="tone_pressure", strength_hint=0.88),
            PressureAxis(axis="recurrence_pressure", strength_hint=0.45),
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=second_wave_material.material_id, note="second_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=second_wave_trace.trace_id, note="second_wave_observer_resonance"),
        ],
    )
    second_wave_seed = service.create_reentry_seed_for_family(
        family_id="seed-fresh-note",
        material_refs=[second_wave_material.material_id],
        trace_refs=[second_wave_trace.trace_id],
        pressure_profile_id=second_wave_pressure.profile_id,
    )
    second_cell = service.create_or_branch_space_cell_for_family(
        family_id="seed-fresh-note",
        material_refs=[second_wave_material.material_id, observer["material_id"]],
        trace_refs=[second_wave_trace.trace_id, observer_reflection["trace_id"]],
        seed_refs=[second_wave_seed.seed_id],
        pressure_profile_id=second_wave_pressure.profile_id,
        interior_refs=[
            second_wave_material.material_id,
            observer["material_id"],
            second_wave_seed.seed_id,
            second_wave_trace.trace_id,
        ],
        exterior_refs=[
            engine_self["material_id"],
            first_cell["cell_id"],
        ],
        cohesion_note="Second wave opens a neighboring observer-facing cell instead of thickening the first one.",
    )
    service.reactivate_space_cell(
        second_cell.cell_id,
        "relocation",
        pressure_profile_id=second_wave_pressure.profile_id,
        note="Second wave shifts into a neighboring terrain rather than returning to the first one.",
        triggered_by_seed_ids=[second_wave_seed.seed_id],
    )

    first_local_space_id = _ensure_local_space_for_cell(service, first_cell["cell_id"], first_cell["pressure_profile_id"])
    second_local_space_id = _ensure_local_space_for_cell(service, second_cell.cell_id, second_wave_pressure.profile_id)
    bridge = service.register_bridge_trace(
        from_local_space_id=first_local_space_id,
        to_local_space_id=second_local_space_id,
        trace_refs=[second_wave_trace.trace_id],
        note="Second wave bridge keeps terrains adjacent without collapsing them.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "second_wave_material_id: %s" % second_wave_material.material_id,
        "second_wave_trace_id: %s" % second_wave_trace.trace_id,
        "second_wave_pressure_id: %s" % second_wave_pressure.profile_id,
        "second_wave_seed_id: %s" % second_wave_seed.seed_id,
        "second_cell_id: %s" % second_cell.cell_id,
        "first_local_space_id: %s" % first_local_space_id,
        "second_local_space_id: %s" % second_local_space_id,
        "bridge_id: %s" % bridge.bridge_id,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
