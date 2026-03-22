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


def _read_excerpt(path: Path, limit: int = 2200) -> str:
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
            SupportRef(ref_kind="material", ref_id=material.material_id, note="memo_file"),
            SupportRef(ref_kind="material", ref_id=observer_material_id, note="observer_anchor"),
        ],
        note="Actual memo bundle enters the runtime as file-backed material without immediate bridge exposure.",
    )
    pressure = service.create_pressure_profile(
        axes=[PressureAxis(axis=axis, strength_hint=strength) for axis, strength in axes],
        support_refs=[
            SupportRef(ref_kind="material", ref_id=material.material_id, note="memo_file"),
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="memo_trace"),
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
        note="Actual memo-backed material opens an independent local space.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def _open_related_memo_space(
    service: FormationService,
    *,
    observer_material_id: str,
    left_path: Path,
    right_path: Path,
) -> str:
    left = service.ingest_material_with_role(
        raw_payload=_read_excerpt(left_path),
        actor_id="codex",
        session_id="phase2-memo-left",
        project_id="vectorfl_next",
        source_type="memo",
        source_ref=str(left_path.relative_to(REPO_ROOT)),
        formation_role="memo_bundle_v1_material",
        family_id="phase2-memo-v1",
        lineage_refs=[observer_material_id],
    )
    right = service.ingest_material_with_role(
        raw_payload=_read_excerpt(right_path),
        actor_id="codex",
        session_id="phase2-memo-right",
        project_id="vectorfl_next",
        source_type="memo",
        source_ref=str(right_path.relative_to(REPO_ROOT)),
        formation_role="memo_bundle_v2v5_material",
        family_id="phase2-memo-v2v5",
        lineage_refs=[observer_material_id],
    )
    trace = service.register_trace(
        material_refs=[left.material_id, right.material_id],
        evidence_kind="memo_bundle_overlap",
        support_refs=[
            SupportRef(ref_kind="material", ref_id=left.material_id, note="memo_v1"),
            SupportRef(ref_kind="material", ref_id=right.material_id, note="memo_v2v5"),
        ],
        note="Actual memo bundles enter as related materials with shared code/design/space concerns.",
    )
    pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="interpretation_pressure", strength_hint=0.64),
            PressureAxis(axis="memory_pressure", strength_hint=0.57),
            PressureAxis(axis="coding_pressure", strength_hint=0.52),
        ],
        support_refs=[
            SupportRef(ref_kind="trace", ref_id=trace.trace_id, note="memo_overlap_trace"),
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
        material_refs=[left.material_id, right.material_id, observer_material_id],
        trace_refs=[trace.trace_id],
        seed_refs=[seed.seed_id],
        pressure_profile_id=pressure.profile_id,
        interior_refs=[left.material_id, right.material_id, seed.seed_id, trace.trace_id],
        exterior_refs=[observer_material_id],
        cohesion_note="Memo bundles form a relation-aware local space from actual memo and code/design residue.",
    )
    service.reactivate_space_cell(
        cell.cell_id,
        "relocation",
        pressure_profile_id=pressure.profile_id,
        note="Actual memo bundles form a shared local space under the same physical rules.",
        triggered_by_seed_ids=[seed.seed_id],
    )
    local_space = service.form_local_space([cell.cell_id], pressure.profile_id)
    return local_space.local_space_id


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)
    observer = _find_material_by_role(runtime_root, "observer_material")

    memo1_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "memo1.md",
        session_id="phase2-memo1",
        source_type="memo",
        formation_role="memo1_material",
        family_id="phase2-memo1",
        evidence_kind="actual_memo1_presence",
        axes=[
            ("policy_pressure", 0.55),
            ("quiet_pressure", 0.61),
            ("memory_pressure", 0.47),
        ],
        cohesion_note="Actual memo1 residue forms a file-backed local space.",
    )
    memo2_space = _open_file_backed_local_space(
        service,
        observer_material_id=observer["material_id"],
        file_path=REPO_ROOT / "memo2.md",
        session_id="phase2-memo2",
        source_type="memo",
        formation_role="memo2_material",
        family_id="phase2-memo2",
        evidence_kind="actual_memo2_presence",
        axes=[
            ("coding_pressure", 0.58),
            ("future_pressure", 0.53),
            ("archive_pressure", 0.45),
        ],
        cohesion_note="Actual memo2 residue forms a file-backed local space.",
    )
    relation_space = _open_related_memo_space(
        service,
        observer_material_id=observer["material_id"],
        left_path=REPO_ROOT / "memo1.md",
        right_path=REPO_ROOT / "memo2.md",
    )

    print("runtime_root: %s" % runtime_root)
    print("memo1_local_space_id: %s" % memo1_space)
    print("memo2_local_space_id: %s" % memo2_space)
    print("memo_relation_local_space_id: %s" % relation_space)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
