#!/usr/bin/env python3
from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef
from app.runtime.graph_view import write_space_graph_view
from app.runtime.scale_review import write_first_scale_review


def _find_material_by_role(runtime_root: Path, formation_role: str) -> dict:
    materials_root = runtime_root / "core" / "materials"
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("metadata", {}).get("formation_role") == formation_role:
            return record
    raise RuntimeError("missing material for role: %s" % formation_role)


def _read_excerpt(path: Path, limit: int = 1600) -> str:
    content = path.read_text(encoding="utf-8")
    return content[:limit]


def _open_file_backed_local_space(
    service: FormationService,
    *,
    observer_material_id: str,
    file_path: Path,
    session_id: str,
    source_type: str,
    formation_role: str,
    family_id: str,
    evidence_kind: str,
    axes,
    cohesion_note: str,
) -> str:
    material = service.ingest_material_with_role(
        raw_payload=_read_excerpt(file_path),
        actor_id="codex",
        session_id=session_id,
        project_id="vectorfl_next",
        source_type=source_type,
        source_ref=str(file_path.relative_to(REPO_ROOT)),
        formation_role=formation_role,
        family_id=family_id,
        lineage_refs=[observer_material_id],
    )
    trace = service.register_trace(
        material_refs=[material.material_id, observer_material_id],
        evidence_kind=evidence_kind,
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="file_material"),
            SupportRef(ref_kind="material", ref_id=observer_material_id, note="observer_anchor"),
        ],
        note="Actual file-backed material enters the runtime without immediate bridge exposure.",
    )
    pressure = service.create_pressure_profile(
        axes=[PressureAxis(axis=axis, strength_hint=strength) for axis, strength in axes],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="file_material"),
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="file_trace"),
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
        note="Actual file-backed material opens an independent local space.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def _open_related_file_space(
    service: FormationService,
    *,
    observer_material_id: str,
    left_path: Path,
    right_path: Path,
) -> str:
    left = service.ingest_material_with_role(
        raw_payload=_read_excerpt(left_path),
        actor_id="codex",
        session_id="phase2-real-left",
        project_id="vectorfl_next",
        source_type="report",
        source_ref=str(left_path.relative_to(REPO_ROOT)),
        formation_role="real_scale_review_material",
        family_id="phase2-real-scale-review",
        lineage_refs=[observer_material_id],
    )
    right = service.ingest_material_with_role(
        raw_payload=_read_excerpt(right_path),
        actor_id="codex",
        session_id="phase2-real-right",
        project_id="vectorfl_next",
        source_type="report",
        source_ref=str(right_path.relative_to(REPO_ROOT)),
        formation_role="real_graph_view_material",
        family_id="phase2-real-graph-view",
        lineage_refs=[observer_material_id],
    )
    trace = service.register_trace(
        material_refs=[left.material_id, right.material_id],
        evidence_kind="actual_report_overlap",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=left.material_id, note="scale_review_material"),
            SupportRef(ref_kind="material", ref_id=right.material_id, note="graph_view_material"),
        ],
        note="Actual review and graph view enter as related runtime artifacts with shared spatial concern.",
    )
    pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="verification_pressure", strength_hint=0.71),
            PressureAxis(axis="interpretation_pressure", strength_hint=0.62),
            PressureAxis(axis="archive_pressure", strength_hint=0.48),
        ],
        support_refs=[
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="overlap_trace"),
            SupportRef(ref_kind="material", ref_id=left.material_id, note="left_file"),
            SupportRef(ref_kind="material", ref_id=right.material_id, note="right_file"),
        ],
    )
    seed = service.create_point_seed_candidate(
        material_refs=[left.material_id, right.material_id],
        trace_refs=[trace.trace_id],
        pressure_profile_id=pressure.profile_id,
    )
    cell = service.create_space_cell_candidate(
        material_refs=[left.material_id, right.material_id, observer_material_id],
        trace_refs=[trace.trace_id],
        seed_refs=[seed.seed_id],
        pressure_profile_id=pressure.profile_id,
        interior_refs=[left.material_id, right.material_id, seed.seed_id, trace.trace_id],
        exterior_refs=[observer_material_id],
        cohesion_note="Actual review and graph artifacts form a relation-aware local space from real runtime data.",
    )
    service.reactivate_space_cell(
        cell.cell_id,
        "relocation",
        pressure_profile_id=pressure.profile_id,
        note="Actual review and graph artifacts form a shared local space under the same physical rules.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    write_first_scale_review(runtime_root)
    write_space_graph_view(runtime_root)
    service = FormationService(runtime_root)
    observer = _find_material_by_role(runtime_root, "observer_material")

    worklog_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "logs" / "runlogs" / "codex_worklog.md",
        session_id="phase2-real-worklog",
        source_type="log",
        formation_role="real_worklog_material",
        family_id="phase2-real-worklog",
        evidence_kind="actual_worklog_presence",
        axes=[
            ("process_pressure", 0.67),
            ("return_pressure", 0.58),
            ("archive_pressure", 0.44),
        ],
        cohesion_note="Actual worklog residue forms a file-backed quiet local space.",
    )
    space_report_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "docs" / "reports" / "VECTORFL_NEXT_SPACE_REPORT_FOR_WEB_CHATGPT.md",
        session_id="phase2-real-space-report",
        source_type="report",
        formation_role="real_space_report_material",
        family_id="phase2-real-space-report",
        evidence_kind="actual_space_report_presence",
        axes=[
            ("interpretation_pressure", 0.66),
            ("archive_pressure", 0.54),
            ("memory_pressure", 0.46),
        ],
        cohesion_note="Actual space-report residue forms a file-backed quiet local space.",
    )
    declaration_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "README.md",
        session_id="phase2-real-readme",
        source_type="doc",
        formation_role="real_readme_material",
        family_id="phase2-real-readme",
        evidence_kind="actual_readme_presence",
        axes=[
            ("policy_pressure", 0.52),
            ("future_pressure", 0.49),
            ("archive_pressure", 0.41),
        ],
        cohesion_note="Actual root-document residue forms a file-backed quiet local space.",
    )
    relation_space = _open_related_file_space(
        service,
        observer_material_id=observer["material_id"],
        left_path=REPO_ROOT / "runtime" / "reports" / "first_scale_review.md",
        right_path=REPO_ROOT / "runtime" / "reports" / "space_graph_view.json",
    )

    print("runtime_root: %s" % runtime_root)
    print("worklog_local_space_id: %s" % worklog_space)
    print("space_report_local_space_id: %s" % space_report_space)
    print("readme_local_space_id: %s" % declaration_space)
    print("actual_relation_local_space_id: %s" % relation_space)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
