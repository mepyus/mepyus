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

    browser_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-eighth bundle browser residue: a browser excerpt enters as quiet external residue without "
            "needing immediate relation."
        ),
        session_id="bootstrap-twentyeighth-browser",
        source_ref="bundle:twentyeighth:browser-residue",
        formation_role="browser_residue_material",
        family_id="seed-twentyeighth-browser",
        evidence_kind="twentyeighth_browser_presence",
        axes=[
            ("interpretation_pressure", 0.58),
            ("archive_pressure", 0.46),
            ("latency_pressure", 0.39),
        ],
        cohesion_note="A browser-residue local space forms quietly without immediate bridge pressure.",
    )
    shell_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-eighth bundle shell transcript residue: a shell interaction fragment enters as quiet tooling "
            "material without having to connect immediately."
        ),
        session_id="bootstrap-twentyeighth-shell",
        source_ref="bundle:twentyeighth:shell-residue",
        formation_role="shell_residue_material",
        family_id="seed-twentyeighth-shell",
        evidence_kind="twentyeighth_shell_presence",
        axes=[
            ("tooling_pressure", 0.62),
            ("process_pressure", 0.53),
            ("archive_pressure", 0.41),
        ],
        cohesion_note="A shell-residue local space forms as quiet tooling material without immediate relation.",
    )
    disagreement_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-eighth bundle disagreement note: a policy disagreement fragment enters as quiet unresolved "
            "material that can remain without immediate exposure."
        ),
        session_id="bootstrap-twentyeighth-disagreement",
        source_ref="bundle:twentyeighth:disagreement-note",
        formation_role="disagreement_material",
        family_id="seed-twentyeighth-disagreement",
        evidence_kind="twentyeighth_disagreement_presence",
        axes=[
            ("conflict_pressure", 0.51),
            ("policy_pressure", 0.56),
            ("silence_pressure", 0.37),
        ],
        cohesion_note="A disagreement local space forms quietly without immediate bridge exposure.",
    )
    test_report_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-eighth bundle test report residue: a test outcome fragment enters as quiet verification residue "
            "that can remain without immediate relation."
        ),
        session_id="bootstrap-twentyeighth-test-report",
        source_ref="bundle:twentyeighth:test-report",
        formation_role="test_report_material",
        family_id="seed-twentyeighth-test-report",
        evidence_kind="twentyeighth_test_report_presence",
        axes=[
            ("verification_pressure", 0.61),
            ("archive_pressure", 0.48),
            ("process_pressure", 0.44),
        ],
        cohesion_note="A test-report local space forms as quiet verification residue without immediate relation.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "browser_local_space_id: %s" % browser_space,
        "shell_local_space_id: %s" % shell_space,
        "disagreement_local_space_id: %s" % disagreement_space,
        "test_report_local_space_id: %s" % test_report_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
