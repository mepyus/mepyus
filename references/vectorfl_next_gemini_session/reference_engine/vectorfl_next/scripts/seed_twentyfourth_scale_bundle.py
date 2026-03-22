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

    mcp_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fourth bundle mcp note: an integration residue enters as quiet protocol material that should stay "
            "alive before any useful relation is demanded."
        ),
        session_id="bootstrap-twentyfourth-mcp",
        source_ref="bundle:twentyfourth:mcp",
        formation_role="mcp_material",
        family_id="seed-twentyfourth-mcp",
        evidence_kind="twentyfourth_mcp_presence",
        axes=[
            ("protocol_pressure", 0.74),
            ("latency_pressure", 0.43),
            ("unknown_pressure", 0.39),
        ],
        cohesion_note="An mcp residue space forms as quiet protocol material without bridge pressure.",
    )
    agent_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fourth bundle agent note: an agent residue enters as quiet orchestration material before any "
            "visible relation is required."
        ),
        session_id="bootstrap-twentyfourth-agent",
        source_ref="bundle:twentyfourth:agent",
        formation_role="agent_material",
        family_id="seed-twentyfourth-agent",
        evidence_kind="twentyfourth_agent_presence",
        axes=[
            ("orchestration_pressure", 0.68),
            ("process_pressure", 0.54),
            ("ambiguity_pressure", 0.36),
        ],
        cohesion_note="An agent residue space forms as quiet orchestration material without immediate bridge exposure.",
    )
    human_note_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fourth bundle human note: a felt note enters the runtime as soft human residue without any need "
            "to justify itself through immediate function."
        ),
        session_id="bootstrap-twentyfourth-human-note",
        source_ref="bundle:twentyfourth:human-note",
        formation_role="human_note_material",
        family_id="seed-twentyfourth-human-note",
        evidence_kind="twentyfourth_human_note_presence",
        axes=[
            ("feeling_pressure", 0.72),
            ("memory_pressure", 0.51),
            ("silence_pressure", 0.44),
        ],
        cohesion_note="A human-note space forms as quiet felt residue without immediate relation.",
    )
    reserve_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-fourth bundle reserve note: a reserve fragment enters the runtime simply to remain available for "
            "future rediscovery."
        ),
        session_id="bootstrap-twentyfourth-reserve",
        source_ref="bundle:twentyfourth:reserve",
        formation_role="reserve_fragment_material",
        family_id="seed-twentyfourth-reserve",
        evidence_kind="twentyfourth_reserve_presence",
        axes=[
            ("reserve_pressure", 0.77),
            ("archive_pressure", 0.46),
            ("silence_pressure", 0.53),
        ],
        cohesion_note="A reserve-fragment space forms as quiet future reserve without immediate bridge pressure.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "mcp_local_space_id: %s" % mcp_space,
        "agent_local_space_id: %s" % agent_space,
        "human_note_local_space_id: %s" % human_note_space,
        "reserve_local_space_id: %s" % reserve_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
