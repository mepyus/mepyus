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


def _open_independent_local_space(
    service: FormationService,
    *,
    observer_material_id: str,
    raw_payload: str,
    session_id: str,
    source_ref: str,
    formation_role: str,
    family_id: str,
    evidence_kind: str,
    axes,
    cohesion_note: str,
) -> str:
    material = service.ingest_material_with_role(
        raw_payload=raw_payload,
        actor_id="codex",
        session_id=session_id,
        project_id="vectorfl_next",
        source_type="note",
        source_ref=source_ref,
        formation_role=formation_role,
        family_id=family_id,
        lineage_refs=[observer_material_id],
    )
    trace = service.register_trace(
        material_refs=[material.material_id, observer_material_id],
        evidence_kind=evidence_kind,
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="bundle_material"),
            SupportRef(ref_kind="material", ref_id=observer_material_id, note="observer_anchor"),
        ],
        note="Bundle material enters the wider runtime without immediate bridge exposure.",
    )
    pressure = service.create_pressure_profile(
        axes=[PressureAxis(axis=axis, strength_hint=strength) for axis, strength in axes],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="bundle_material"),
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="bundle_trace"),
        ],
    )
    seed = service.create_point_seed_candidate(
        material_refs=[material.material_id],
        trace_refs=[trace.trace_id],
        pressure_profile_id=pressure.profile_id,
    )
    cell = service.create_space_cell_candidate(
        material_refs=[material.material_id, observer_material_id],
        trace_refs=[trace.trace_id],
        seed_refs=[seed.seed_id],
        pressure_profile_id=pressure.profile_id,
        interior_refs=[material.material_id, seed.seed_id, trace.trace_id],
        exterior_refs=[observer_material_id],
        cohesion_note=cohesion_note,
    )
    service.reactivate_space_cell(
        cell.cell_id,
        "relocation",
        pressure_profile_id=pressure.profile_id,
        note="Bundle material opens an independent local space without immediate bridge exposure.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)
    observer = _find_material_by_role(runtime_root, "observer_material")

    policy_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fifth bundle policy note: a policy fragment enters as quiet structural residue that may matter "
            "later without any need for immediate relation."
        ),
        session_id="bootstrap-twentyfifth-policy",
        source_ref="bundle:twentyfifth:policy-note",
        formation_role="policy_note_material",
        family_id="seed-twentyfifth-policy",
        evidence_kind="twentyfifth_policy_presence",
        axes=[
            ("policy_pressure", 0.72),
            ("archive_pressure", 0.44),
            ("silence_pressure", 0.41),
        ],
        cohesion_note="A policy-note local space forms as quiet structural residue without immediate bridge pressure.",
    )
    experiment_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fifth bundle experiment plan note: a future experiment plan enters as quiet prospective material "
            "without having to connect immediately."
        ),
        session_id="bootstrap-twentyfifth-experiment",
        source_ref="bundle:twentyfifth:experiment-plan",
        formation_role="experiment_plan_material",
        family_id="seed-twentyfifth-experiment",
        evidence_kind="twentyfifth_experiment_presence",
        axes=[
            ("future_pressure", 0.69),
            ("planning_pressure", 0.63),
            ("uncertainty_pressure", 0.47),
        ],
        cohesion_note="An experiment-plan local space forms as prospective material without immediate relation.",
    )
    book_highlight_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fifth bundle book highlight: a highlighted passage enters as quiet reading residue that can wait "
            "for future rediscovery."
        ),
        session_id="bootstrap-twentyfifth-book-highlight",
        source_ref="bundle:twentyfifth:book-highlight",
        formation_role="book_highlight_material",
        family_id="seed-twentyfifth-book-highlight",
        evidence_kind="twentyfifth_book_highlight_presence",
        axes=[
            ("curiosity_pressure", 0.64),
            ("memory_pressure", 0.62),
            ("archive_pressure", 0.51),
        ],
        cohesion_note="A book-highlight local space forms as quiet reading residue without immediate bridge pressure.",
    )
    codex_return_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fifth bundle codex return: a codex work residue enters as quiet self-return material that need not "
            "become visible relation immediately."
        ),
        session_id="bootstrap-twentyfifth-codex-return",
        source_ref="bundle:twentyfifth:codex-return",
        formation_role="codex_return_material",
        family_id="seed-twentyfifth-codex-return",
        evidence_kind="twentyfifth_codex_return_presence",
        axes=[
            ("return_pressure", 0.74),
            ("process_pressure", 0.56),
            ("reflection_pressure", 0.49),
        ],
        cohesion_note="A codex-return local space forms as quiet self-return material without immediate relation.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "policy_local_space_id: %s" % policy_space,
        "experiment_local_space_id: %s" % experiment_space,
        "book_highlight_local_space_id: %s" % book_highlight_space,
        "codex_return_local_space_id: %s" % codex_return_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
