#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef
from app.runtime.reactive_space_report import write_reactive_space_report
from app.runtime.workspace_report import write_workspace_report


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
    return {
        "material_id": material.material_id,
        "trace_id": trace.trace_id,
        "pressure_id": pressure.profile_id,
        "seed_id": seed.seed_id,
        "cell_id": cell.cell_id,
        "local_space_id": local_space.local_space_id,
    }


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)
    observer = _find_material_by_role(runtime_root, "observer_material")

    workspace_report_path = write_workspace_report(runtime_root)
    reactive_report_path = write_reactive_space_report(runtime_root)
    workspace_report_text = workspace_report_path.read_text(encoding="utf-8")
    reactive_report_text = reactive_report_path.read_text(encoding="utf-8")

    sparse_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-first bundle sparse note: a thin, quiet presence enters the runtime and should remain "
            "spatially present even without immediate bridge exposure."
        ),
        session_id="bootstrap-twentyfirst-sparse",
        source_ref="bundle:twentyfirst:sparse-presence",
        formation_role="sparse_presence_material",
        family_id="seed-twentyfirst-sparse",
        evidence_kind="twentyfirst_sparse_presence",
        axes=[
            ("ambiguity_pressure", 0.31),
            ("latency_pressure", 0.44),
            ("silence_pressure", 0.62),
        ],
        cohesion_note="A sparse local space forms and stays quiet without asking for immediate relation.",
    )
    reflux_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-first bundle reflux note:\n\n"
            + workspace_report_text
            + "\n\n---\n\n"
            + reactive_report_text
        ),
        session_id="bootstrap-twentyfirst-reflux",
        source_ref="bundle:twentyfirst:reflux-report",
        formation_role="engine_self_return_material",
        family_id="seed-twentyfirst-reflux",
        evidence_kind="twentyfirst_reflux_presence",
        axes=[
            ("reflection_pressure", 0.67),
            ("return_pressure", 0.72),
            ("archive_pressure", 0.58),
        ],
        cohesion_note="A reflux local space forms from generated reports without needing immediate bridge exposure.",
    )
    reading_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-first bundle reading note: a non-purpose reading fragment enters the runtime as a reminder that "
            "not every material has to justify itself immediately through visible relation or function."
        ),
        session_id="bootstrap-twentyfirst-reading",
        source_ref="bundle:twentyfirst:reading-note",
        formation_role="reading_note_material",
        family_id="seed-twentyfirst-reading",
        evidence_kind="twentyfirst_reading_presence",
        axes=[
            ("curiosity_pressure", 0.71),
            ("drift_pressure", 0.53),
            ("memory_pressure", 0.47),
        ],
        cohesion_note="A reading-note local space forms as non-purpose presence rather than immediate relation.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "sparse_local_space_id: %s" % sparse_space["local_space_id"],
        "reflux_local_space_id: %s" % reflux_space["local_space_id"],
        "reading_local_space_id: %s" % reading_space["local_space_id"],
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
