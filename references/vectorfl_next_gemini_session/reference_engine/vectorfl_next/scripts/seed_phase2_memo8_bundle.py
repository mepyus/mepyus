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


def _read_excerpt(path: Path, limit: int = 3200) -> str:
    content = path.read_text(encoding="utf-8")
    return content[:limit]


def _open_file_backed_local_space(
    service: FormationService,
    *,
    observer_material_id: str,
    file_path: Path,
    session_id: str,
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
        source_type="memo",
        source_ref=str(file_path.relative_to(REPO_ROOT)),
        formation_role=formation_role,
        family_id=family_id,
        lineage_refs=[observer_material_id],
    )
    trace = service.register_trace(
        material_refs=[material.material_id, observer_material_id],
        evidence_kind=evidence_kind,
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="memo8_file"),
            SupportRef(ref_kind="material", ref_id=observer_material_id, note="observer_anchor"),
        ],
        note="Actual memo8 enters as file-backed material without forced bridge growth.",
    )
    pressure = service.create_pressure_profile(
        axes=[PressureAxis(axis=axis, strength_hint=strength) for axis, strength in axes],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="memo8_file"),
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="memo8_trace"),
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
        note="Actual memo8 opens an independent local space under the same physical laws.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def _open_related_memo_space(
    service: FormationService,
    *,
    left_path: Path,
    right_path: Path,
    left_role: str,
    right_role: str,
) -> str:
    left = service.ingest_material_with_role(
        raw_payload=_read_excerpt(left_path),
        actor_id="codex",
        session_id="phase2-memo8-left-linked",
        project_id="vectorfl_next",
        source_type="memo",
        source_ref=str(left_path.relative_to(REPO_ROOT)),
        formation_role=left_role,
        family_id="phase2-memo8-left-linked",
    )
    right = service.ingest_material_with_role(
        raw_payload=_read_excerpt(right_path),
        actor_id="codex",
        session_id="phase2-memo8-right-linked",
        project_id="vectorfl_next",
        source_type="memo",
        source_ref=str(right_path.relative_to(REPO_ROOT)),
        formation_role=right_role,
        family_id="phase2-memo8-right-linked",
    )
    trace = service.register_trace(
        material_refs=[left.material_id, right.material_id],
        evidence_kind="memo_bundle_absorption_repair_overlap",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=left.material_id, note="left_memo_bundle"),
            SupportRef(ref_kind="material", ref_id=right.material_id, note="right_memo_bundle"),
        ],
        note="Actual memo7 and memo8 are linked by reading absorption, repair loop, cadence, and delayed extraction overlap.",
    )
    pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="absorption_pressure", strength_hint=0.64),
            PressureAxis(axis="repair_pressure", strength_hint=0.58),
            PressureAxis(axis="cadence_pressure", strength_hint=0.52),
        ],
        support_refs=[
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="memo_absorption_repair_trace"),
            SupportRef(ref_kind="material", ref_id=left.material_id, note="memo_left"),
            SupportRef(ref_kind="material", ref_id=right.material_id, note="memo_right"),
        ],
    )
    seed = service.create_point_seed_candidate(
        material_refs=[left.material_id, right.material_id],
        trace_refs=[trace.trace_id],
        pressure_profile_id=pressure.profile_id,
    )
    cell = service.create_space_cell_candidate(
        material_refs=[left.material_id, right.material_id],
        trace_refs=[trace.trace_id],
        seed_refs=[seed.seed_id],
        pressure_profile_id=pressure.profile_id,
        interior_refs=[left.material_id, right.material_id, seed.seed_id, trace.trace_id],
        exterior_refs=[],
        cohesion_note="Memo7 and memo8 form a relation-aware local space from measurement-to-absorption, steering-to-repair, and cadence progression.",
    )
    service.reactivate_space_cell(
        cell.cell_id,
        "relocation",
        pressure_profile_id=pressure.profile_id,
        note="Actual memo progression forms another shared local space under the same physical rules.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)
    observer = _find_material_by_role(runtime_root, "observer_material")

    memo8_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "memo8.md",
        session_id="phase2-memo8",
        formation_role="memo8_material",
        family_id="phase2-memo8",
        evidence_kind="actual_memo8_presence",
        axes=[
            ("absorption_pressure", 0.66),
            ("repair_pressure", 0.58),
            ("cadence_pressure", 0.54),
        ],
        cohesion_note="Actual memo8 residue forms a file-backed local space.",
    )
    memo78_relation_space = _open_related_memo_space(
        service,
        left_path=REPO_ROOT / "memo7.md",
        right_path=REPO_ROOT / "memo8.md",
        left_role="memo7_measurement_archive_material",
        right_role="memo8_absorption_repair_material",
    )

    print("runtime_root: %s" % runtime_root)
    print("memo8_local_space_id: %s" % memo8_space)
    print("memo78_relation_local_space_id: %s" % memo78_relation_space)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
