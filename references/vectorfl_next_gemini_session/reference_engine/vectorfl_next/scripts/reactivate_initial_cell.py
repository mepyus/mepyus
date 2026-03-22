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


def _find_trace_by_kind(runtime_root: Path, evidence_kind: str) -> dict:
    traces_root = runtime_root / "core" / "traces"
    for path in sorted(traces_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("evidence_kind") == evidence_kind:
            return record
    raise RuntimeError("missing trace for evidence kind: %s" % evidence_kind)


def _require_single_cell(runtime_root: Path) -> dict:
    cells_root = runtime_root / "core" / "space_cells"
    records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(cells_root.glob("*.json"))]
    if len(records) != 1:
        raise RuntimeError("expected exactly one candidate cell before first reactivation, found %s" % len(records))
    return records[0]


def _get_pressure_profile(runtime_root: Path, profile_id: str) -> dict:
    path = runtime_root / "core" / "pressure_profiles" / ("%s.json" % profile_id)
    if not path.exists():
        raise RuntimeError("missing pressure profile: %s" % profile_id)
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)

    original_fresh = _find_material_by_role(runtime_root, "fresh_material")
    observer_reflection = _find_trace_by_kind(runtime_root, "observer_reflection")
    current_cell = _require_single_cell(runtime_root)
    current_profile = _get_pressure_profile(runtime_root, current_cell["pressure_profile_id"])

    reentry_material = service.ingest_material_with_role(
        raw_payload=(
            "Fresh reentry note: the initial fresh pressure remains near the prior cell and should thicken it "
            "before any split or relocation rule is considered."
        ),
        actor_id="codex",
        session_id="bootstrap-fresh-reentry",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:fresh-note:reentry-1",
        formation_role="fresh_material",
        family_id="seed-fresh-note",
        lineage_refs=[original_fresh["material_id"]],
    )
    reentry_trace = service.register_trace(
        material_refs=[reentry_material.material_id],
        evidence_kind="fresh_reentry_hint",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=reentry_material.material_id, note="fresh_material"),
            SupportRef(ref_kind="material", ref_id=original_fresh["material_id"], note="prior_fresh_material"),
        ],
        note="Second fresh input stays near the prior pressure path and should thicken the first cell.",
    )
    reentry_pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis=axis["axis"], strength_hint=axis["strength_hint"])
            for axis in current_profile.get("axes", [])
        ],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=reentry_material.material_id, note="fresh_material"),
            SupportRef(ref_kind="trace", ref_id=reentry_trace.trace_id, note="fresh_reentry_hint"),
        ],
    )
    reentry_seed = service.create_reentry_seed_for_family(
        family_id="seed-fresh-note",
        material_refs=[reentry_material.material_id],
        trace_refs=[reentry_trace.trace_id],
        pressure_profile_id=reentry_pressure.profile_id,
    )
    cell = service.create_or_branch_space_cell_for_family(
        family_id="seed-fresh-note",
        material_refs=[reentry_material.material_id],
        trace_refs=[reentry_trace.trace_id],
        seed_refs=[reentry_seed.seed_id],
        pressure_profile_id=reentry_pressure.profile_id,
        interior_refs=[reentry_material.material_id, reentry_seed.seed_id, reentry_trace.trace_id],
        exterior_refs=current_cell["boundary"]["exterior_refs"],
        cohesion_note="First reentry keeps pressure continuity and should thicken the candidate cell.",
    )
    updated = service.reactivate_space_cell(
        cell.cell_id,
        "thickening",
        pressure_profile_id=reentry_pressure.profile_id,
        note="First reactivation thickens the initial convergence cell under similar fresh pressure.",
        triggered_by_seed_ids=[reentry_seed.seed_id],
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "reentry_material_id: %s" % reentry_material.material_id,
        "reentry_trace_id: %s" % reentry_trace.trace_id,
        "reentry_pressure_id: %s" % reentry_pressure.profile_id,
        "reentry_seed_id: %s" % reentry_seed.seed_id,
        "cell_id: %s" % cell.cell_id,
        "cell_state: %s" % updated["state"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
