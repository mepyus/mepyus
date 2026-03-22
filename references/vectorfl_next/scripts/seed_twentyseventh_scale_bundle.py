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

    pipeline_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-seventh bundle pipeline residue: a partial extraction residue returns to the field without "
            "needing immediate relation or reuse."
        ),
        session_id="bootstrap-twentyseventh-pipeline",
        source_ref="bundle:twentyseventh:pipeline-residue",
        formation_role="pipeline_residue_material",
        family_id="seed-twentyseventh-pipeline",
        evidence_kind="twentyseventh_pipeline_presence",
        axes=[
            ("pipeline_pressure", 0.67),
            ("archive_pressure", 0.47),
            ("silence_pressure", 0.38),
        ],
        cohesion_note="A pipeline-residue local space forms quietly without immediate bridge pressure.",
    )
    meeting_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-seventh bundle meeting residue: a meeting trace enters as quiet operational material without "
            "having to connect immediately."
        ),
        session_id="bootstrap-twentyseventh-meeting",
        source_ref="bundle:twentyseventh:meeting-residue",
        formation_role="meeting_residue_material",
        family_id="seed-twentyseventh-meeting",
        evidence_kind="twentyseventh_meeting_presence",
        axes=[
            ("dialogue_pressure", 0.59),
            ("memory_pressure", 0.46),
            ("archive_pressure", 0.44),
        ],
        cohesion_note="A meeting-residue local space forms as quiet operational material without immediate relation.",
    )
    diff_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-seventh bundle code diff residue: a diff fragment enters as quiet implementation residue that can "
            "remain without immediate extraction."
        ),
        session_id="bootstrap-twentyseventh-diff",
        source_ref="bundle:twentyseventh:diff-residue",
        formation_role="code_diff_material",
        family_id="seed-twentyseventh-diff",
        evidence_kind="twentyseventh_diff_presence",
        axes=[
            ("coding_pressure", 0.63),
            ("process_pressure", 0.52),
            ("archive_pressure", 0.43),
        ],
        cohesion_note="A code-diff local space forms as quiet implementation residue without immediate bridge exposure.",
    )
    voice_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-seventh bundle voice memo residue: a short voice memo note enters as quiet feeling-thought "
            "material that can remain without immediate relation."
        ),
        session_id="bootstrap-twentyseventh-voice",
        source_ref="bundle:twentyseventh:voice-memo",
        formation_role="voice_memo_material",
        family_id="seed-twentyseventh-voice",
        evidence_kind="twentyseventh_voice_presence",
        axes=[
            ("feeling_pressure", 0.54),
            ("memory_pressure", 0.48),
            ("silence_pressure", 0.42),
        ],
        cohesion_note="A voice-memo local space forms quietly without immediate bridge pressure.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "pipeline_local_space_id: %s" % pipeline_space,
        "meeting_local_space_id: %s" % meeting_space,
        "diff_local_space_id: %s" % diff_space,
        "voice_local_space_id: %s" % voice_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
