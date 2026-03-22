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
) -> dict:
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

    agent_log_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-second bundle agent-log note: a low-legibility trace from agent work enters the runtime and "
            "should remain as process residue before it becomes useful."
        ),
        session_id="bootstrap-twentysecond-agent-log",
        source_ref="bundle:twentysecond:agent-log",
        formation_role="agent_log_material",
        family_id="seed-twentysecond-agent-log",
        evidence_kind="twentysecond_agent_log_presence",
        axes=[
            ("archive_pressure", 0.63),
            ("process_pressure", 0.59),
            ("latency_pressure", 0.37),
        ],
        cohesion_note="An agent-log local space forms as quiet process residue without immediate relation.",
    )
    failure_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-second bundle failure note: a failed experiment enters the runtime and should stay alive as "
            "material even before it gains relation or explanation."
        ),
        session_id="bootstrap-twentysecond-failure",
        source_ref="bundle:twentysecond:failure-note",
        formation_role="failed_experiment_material",
        family_id="seed-twentysecond-failure",
        evidence_kind="twentysecond_failure_presence",
        axes=[
            ("failure_pressure", 0.74),
            ("uncertainty_pressure", 0.66),
            ("memory_pressure", 0.41),
        ],
        cohesion_note="A failed-experiment local space forms and stays present without immediate bridge exposure.",
    )
    book_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-second bundle book note: a reading trace enters the runtime with no current function other than "
            "staying available for later rediscovery."
        ),
        session_id="bootstrap-twentysecond-book",
        source_ref="bundle:twentysecond:book-note",
        formation_role="book_note_material",
        family_id="seed-twentysecond-book",
        evidence_kind="twentysecond_book_presence",
        axes=[
            ("curiosity_pressure", 0.69),
            ("archive_pressure", 0.52),
            ("memory_pressure", 0.64),
        ],
        cohesion_note="A book-note local space forms as quiet future-facing material rather than immediate relation.",
    )
    unknown_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-second bundle unknown fragment: a fragment with no current purpose enters the runtime and should "
            "remain spatially alive without being forced into legibility."
        ),
        session_id="bootstrap-twentysecond-unknown",
        source_ref="bundle:twentysecond:unknown-fragment",
        formation_role="unknown_fragment_material",
        family_id="seed-twentysecond-unknown",
        evidence_kind="twentysecond_unknown_presence",
        axes=[
            ("ambiguity_pressure", 0.57),
            ("silence_pressure", 0.48),
            ("unknown_pressure", 0.77),
        ],
        cohesion_note="An unknown-fragment local space forms and remains quiet without immediate bridge pressure.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "agent_log_local_space_id: %s" % agent_log_space,
        "failure_local_space_id: %s" % failure_space,
        "book_local_space_id: %s" % book_space,
        "unknown_local_space_id: %s" % unknown_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
