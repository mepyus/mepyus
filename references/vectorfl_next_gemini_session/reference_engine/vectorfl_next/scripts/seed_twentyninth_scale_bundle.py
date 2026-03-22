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

    archive_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-ninth bundle archive fragment: a dormant archive shard enters as quiet residue without needing "
            "immediate relation."
        ),
        session_id="bootstrap-twentyninth-archive",
        source_ref="bundle:twentyninth:archive-fragment",
        formation_role="archive_fragment_material",
        family_id="seed-twentyninth-archive",
        evidence_kind="twentyninth_archive_presence",
        axes=[
            ("archive_pressure", 0.66),
            ("memory_pressure", 0.49),
            ("silence_pressure", 0.37),
        ],
        cohesion_note="An archive-fragment local space forms quietly without immediate bridge pressure.",
    )
    changelog_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-ninth bundle changelog residue: a small changelog fragment enters as quiet process residue "
            "without immediate exposure."
        ),
        session_id="bootstrap-twentyninth-changelog",
        source_ref="bundle:twentyninth:changelog-residue",
        formation_role="changelog_material",
        family_id="seed-twentyninth-changelog",
        evidence_kind="twentyninth_changelog_presence",
        axes=[
            ("process_pressure", 0.58),
            ("archive_pressure", 0.46),
            ("return_pressure", 0.42),
        ],
        cohesion_note="A changelog local space forms as quiet process residue without immediate relation.",
    )
    sketch_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-ninth bundle sketch note: a rough sketch fragment enters as quiet pre-form material that can "
            "remain unresolved."
        ),
        session_id="bootstrap-twentyninth-sketch",
        source_ref="bundle:twentyninth:sketch-note",
        formation_role="sketch_material",
        family_id="seed-twentyninth-sketch",
        evidence_kind="twentyninth_sketch_presence",
        axes=[
            ("future_pressure", 0.51),
            ("ambiguity_pressure", 0.55),
            ("curiosity_pressure", 0.44),
        ],
        cohesion_note="A sketch-note local space forms quietly without immediate bridge exposure.",
    )
    transcript_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-ninth bundle transcript residue: a partial transcript enters as quiet dialogue residue without "
            "needing immediate relation."
        ),
        session_id="bootstrap-twentyninth-transcript",
        source_ref="bundle:twentyninth:transcript-residue",
        formation_role="transcript_material",
        family_id="seed-twentyninth-transcript",
        evidence_kind="twentyninth_transcript_presence",
        axes=[
            ("dialogue_pressure", 0.57),
            ("archive_pressure", 0.43),
            ("latency_pressure", 0.38),
        ],
        cohesion_note="A transcript-residue local space forms quietly without immediate relation.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "archive_local_space_id: %s" % archive_space,
        "changelog_local_space_id: %s" % changelog_space,
        "sketch_local_space_id: %s" % sketch_space,
        "transcript_local_space_id: %s" % transcript_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
