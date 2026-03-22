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


def _latest_tone_pressure_cell(runtime_root: Path, family_id: str) -> dict:
    family_material_ids = _family_material_ids(runtime_root, family_id)
    cells_root = runtime_root / "core" / "space_cells"
    pressure_root = runtime_root / "core" / "pressure_profiles"
    matches = []
    for path in sorted(cells_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if not (set(record.get("material_refs", ())) & family_material_ids):
            continue
        pressure_path = pressure_root / ("%s.json" % record["pressure_profile_id"])
        pressure = json.loads(pressure_path.read_text(encoding="utf-8"))
        axes = {axis["axis"] for axis in pressure.get("axes", [])}
        if "tone_pressure" in axes:
            matches.append((record, pressure))
    if not matches:
        raise RuntimeError("missing tone-pressure cell for family: %s" % family_id)
    return {"cell": matches[-1][0], "pressure": matches[-1][1]}


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    target = _latest_tone_pressure_cell(runtime_root, "seed-fresh-note")
    second_cell = target["cell"]
    second_pressure = target["pressure"]
    second_trace = _latest_trace_by_kind(runtime_root, "second_wave_observer_resonance")

    sixth_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Sixth wave note: the observer-facing neighboring terrain returns again under the same tone-heavy "
            "pressure and should thicken without opening another bridge or another local terrain."
        ),
        actor_id="codex",
        session_id="bootstrap-sixth-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:sixth-wave:observer-facing-return",
        formation_role="fresh_material",
        family_id="seed-fresh-note",
        lineage_refs=list(second_cell.get("material_refs", ())),
    )
    sixth_wave_trace = service.register_trace(
        material_refs=[sixth_wave_material.material_id],
        evidence_kind="sixth_wave_observer_return",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=sixth_wave_material.material_id, note="sixth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=second_trace["trace_id"], note="second_wave_observer_resonance"),
        ],
        note="Sixth wave returns to the observer-facing neighboring terrain under matching tone-heavy pressure.",
    )
    sixth_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis=axis["axis"], strength_hint=axis["strength_hint"])
            for axis in second_pressure.get("axes", [])
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=sixth_wave_material.material_id, note="sixth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=sixth_wave_trace.trace_id, note="sixth_wave_observer_return"),
        ],
    )
    sixth_wave_seed = service.create_reentry_seed_for_family(
        family_id="seed-fresh-note",
        material_refs=[sixth_wave_material.material_id],
        trace_refs=[sixth_wave_trace.trace_id],
        pressure_profile_id=sixth_wave_pressure.profile_id,
    )
    updated_cell = service.create_or_branch_space_cell_for_family(
        family_id="seed-fresh-note",
        material_refs=[sixth_wave_material.material_id],
        trace_refs=[sixth_wave_trace.trace_id],
        seed_refs=[sixth_wave_seed.seed_id],
        pressure_profile_id=sixth_wave_pressure.profile_id,
        interior_refs=[sixth_wave_material.material_id, sixth_wave_seed.seed_id, sixth_wave_trace.trace_id],
        exterior_refs=second_cell["boundary"]["exterior_refs"],
        cohesion_note="Sixth wave thickens the neighboring observer-facing terrain instead of branching it again.",
    )
    reactivated = service.reactivate_space_cell(
        updated_cell.cell_id,
        "thickening",
        pressure_profile_id=sixth_wave_pressure.profile_id,
        note="Sixth wave adds repeated thickening to the observer-facing neighboring terrain.",
        triggered_by_seed_ids=[sixth_wave_seed.seed_id],
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "sixth_wave_material_id: %s" % sixth_wave_material.material_id,
        "sixth_wave_trace_id: %s" % sixth_wave_trace.trace_id,
        "sixth_wave_pressure_id: %s" % sixth_wave_pressure.profile_id,
        "sixth_wave_seed_id: %s" % sixth_wave_seed.seed_id,
        "cell_id: %s" % reactivated["cell_id"],
        "cell_state: %s" % reactivated["state"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
