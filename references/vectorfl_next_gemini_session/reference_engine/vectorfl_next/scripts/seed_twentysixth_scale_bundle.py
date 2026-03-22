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
        note="Bundle material enters the widened runtime without immediate bridge exposure.",
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

    handoff_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-sixth bundle handoff residue: a quiet handoff fragment enters the field without needing immediate "
            "relation or extraction."
        ),
        session_id="bootstrap-twentysixth-handoff",
        source_ref="bundle:twentysixth:handoff-residue",
        formation_role="handoff_residue_material",
        family_id="seed-twentysixth-handoff",
        evidence_kind="twentysixth_handoff_presence",
        axes=[
            ("handoff_pressure", 0.68),
            ("silence_pressure", 0.46),
            ("archive_pressure", 0.43),
        ],
        cohesion_note="A handoff-residue local space forms quietly without immediate bridge pressure.",
    )
    tool_error_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-sixth bundle tool error note: a small tool-failure residue enters as quiet operational material "
            "that may matter later without immediate relation."
        ),
        session_id="bootstrap-twentysixth-tool-error",
        source_ref="bundle:twentysixth:tool-error",
        formation_role="tool_error_material",
        family_id="seed-twentysixth-tool-error",
        evidence_kind="twentysixth_tool_error_presence",
        axes=[
            ("failure_pressure", 0.58),
            ("tooling_pressure", 0.61),
            ("archive_pressure", 0.42),
        ],
        cohesion_note="A tool-error local space forms as quiet operational residue without immediate bridge exposure.",
    )
    unread_quote_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-sixth bundle unread quote: a quote fragment enters as quiet reading residue that can wait for "
            "future rediscovery."
        ),
        session_id="bootstrap-twentysixth-unread-quote",
        source_ref="bundle:twentysixth:unread-quote",
        formation_role="unread_quote_material",
        family_id="seed-twentysixth-unread-quote",
        evidence_kind="twentysixth_unread_quote_presence",
        axes=[
            ("memory_pressure", 0.57),
            ("archive_pressure", 0.56),
            ("curiosity_pressure", 0.49),
        ],
        cohesion_note="An unread-quote local space forms as quiet reading residue without immediate relation.",
    )
    question_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-sixth bundle question residue: an unresolved question enters as quiet conceptual material that "
            "need not become visible relation immediately."
        ),
        session_id="bootstrap-twentysixth-question",
        source_ref="bundle:twentysixth:question-residue",
        formation_role="question_residue_material",
        family_id="seed-twentysixth-question",
        evidence_kind="twentysixth_question_presence",
        axes=[
            ("unknown_pressure", 0.63),
            ("curiosity_pressure", 0.55),
            ("silence_pressure", 0.41),
        ],
        cohesion_note="A question-residue local space forms quietly without immediate bridge pressure.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "handoff_local_space_id: %s" % handoff_space,
        "tool_error_local_space_id: %s" % tool_error_space,
        "unread_quote_local_space_id: %s" % unread_quote_space,
        "question_local_space_id: %s" % question_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
