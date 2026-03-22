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
    cells_root = runtime_root / "core" / "space_cells"
    matches = []
    for path in sorted(cells_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if set(record.get("material_refs", ())) & family_material_ids:
            matches.append(record)
    if not matches:
        raise RuntimeError("missing cell for family: %s" % family_id)
    return matches[-1]


def _pressure_profile(runtime_root: Path, profile_id: str) -> dict:
    path = runtime_root / "core" / "pressure_profiles" / ("%s.json" % profile_id)
    if not path.exists():
        raise RuntimeError("missing pressure profile: %s" % profile_id)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    third_cell = _latest_cell_for_family(runtime_root, "seed-third-wave")
    fourth_trace = _latest_trace_by_kind(runtime_root, "fourth_wave_temporal_return")
    third_profile = _pressure_profile(runtime_root, third_cell["pressure_profile_id"])

    fifth_wave_material = service.ingest_material_with_role(
        raw_payload=(
            "Fifth wave note: temporal-project terrain returns again and should leave repeated thickening "
            "inside the same third terrain without opening a new branch."
        ),
        actor_id="codex",
        session_id="bootstrap-fifth-wave",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:fifth-wave:temporal-project-return",
        formation_role="fresh_material",
        family_id="seed-third-wave",
        lineage_refs=list(third_cell.get("material_refs", ())),
    )
    fifth_wave_trace = service.register_trace(
        material_refs=[fifth_wave_material.material_id],
        evidence_kind="fifth_wave_temporal_return",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fifth_wave_material.material_id, note="fifth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=fourth_trace["trace_id"], note="fourth_wave_temporal_return"),
        ],
        note="Fifth wave returns again to the same temporal-project terrain.",
    )
    fifth_wave_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis=axis["axis"], strength_hint=axis["strength_hint"])
            for axis in third_profile.get("axes", [])
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=fifth_wave_material.material_id, note="fifth_wave_fresh"),
            SupportRef(ref_kind="trace", ref_id=fifth_wave_trace.trace_id, note="fifth_wave_temporal_return"),
        ],
    )
    fifth_wave_seed = service.create_reentry_seed_for_family(
        family_id="seed-third-wave",
        material_refs=[fifth_wave_material.material_id],
        trace_refs=[fifth_wave_trace.trace_id],
        pressure_profile_id=fifth_wave_pressure.profile_id,
    )
    updated_cell = service.create_or_branch_space_cell_for_family(
        family_id="seed-third-wave",
        material_refs=[fifth_wave_material.material_id],
        trace_refs=[fifth_wave_trace.trace_id],
        seed_refs=[fifth_wave_seed.seed_id],
        pressure_profile_id=fifth_wave_pressure.profile_id,
        interior_refs=[fifth_wave_material.material_id, fifth_wave_seed.seed_id, fifth_wave_trace.trace_id],
        exterior_refs=third_cell["boundary"]["exterior_refs"],
        cohesion_note="Fifth wave continues thickening the same temporal-project terrain.",
    )
    reactivated = service.reactivate_space_cell(
        updated_cell.cell_id,
        "thickening",
        pressure_profile_id=fifth_wave_pressure.profile_id,
        note="Fifth wave adds repeated thickening to the temporal-project terrain.",
        triggered_by_seed_ids=[fifth_wave_seed.seed_id],
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "fifth_wave_material_id: %s" % fifth_wave_material.material_id,
        "fifth_wave_trace_id: %s" % fifth_wave_trace.trace_id,
        "fifth_wave_pressure_id: %s" % fifth_wave_pressure.profile_id,
        "fifth_wave_seed_id: %s" % fifth_wave_seed.seed_id,
        "cell_id: %s" % reactivated["cell_id"],
        "cell_state: %s" % reactivated["state"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
