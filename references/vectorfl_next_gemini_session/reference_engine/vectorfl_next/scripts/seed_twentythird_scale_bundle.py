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

    web_chatgpt_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-third bundle web-chatgpt note: a web conversation residue enters the runtime as quiet material "
            "that may matter later even if it has no immediate relation now."
        ),
        session_id="bootstrap-twentythird-web-chatgpt",
        source_ref="bundle:twentythird:web-chatgpt",
        formation_role="web_chatgpt_material",
        family_id="seed-twentythird-web-chatgpt",
        evidence_kind="twentythird_web_chatgpt_presence",
        axes=[
            ("dialogue_pressure", 0.73),
            ("interpretation_pressure", 0.58),
            ("latency_pressure", 0.34),
        ],
        cohesion_note="A web-chatgpt residue space forms without needing immediate bridge exposure.",
    )
    gemini_cli_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-third bundle gemini-cli note: a command-line model residue enters the runtime as process material "
            "that can stay quiet before becoming useful."
        ),
        session_id="bootstrap-twentythird-gemini-cli",
        source_ref="bundle:twentythird:gemini-cli",
        formation_role="gemini_cli_material",
        family_id="seed-twentythird-gemini-cli",
        evidence_kind="twentythird_gemini_cli_presence",
        axes=[
            ("process_pressure", 0.68),
            ("tooling_pressure", 0.62),
            ("archive_pressure", 0.49),
        ],
        cohesion_note="A gemini-cli residue space forms as quiet tooling/process material.",
    )
    claude_code_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-third bundle claude-code note: a future coding-agent residue enters the runtime without any "
            "requirement to connect immediately."
        ),
        session_id="bootstrap-twentythird-claude-code",
        source_ref="bundle:twentythird:claude-code",
        formation_role="claude_code_material",
        family_id="seed-twentythird-claude-code",
        evidence_kind="twentythird_claude_code_presence",
        axes=[
            ("coding_pressure", 0.71),
            ("process_pressure", 0.57),
            ("unknown_pressure", 0.52),
        ],
        cohesion_note="A claude-code residue space forms as future-facing coding material without immediate relation.",
    )
    youtube_note_space = _open_independent_local_space(
        service,
        observer_material_id=observer["material_id"],
        raw_payload=(
            "Twenty-third bundle youtube note: a felt insight from a video enters the runtime as soft reading material "
            "that does not need immediate function to remain alive."
        ),
        session_id="bootstrap-twentythird-youtube-note",
        source_ref="bundle:twentythird:youtube-note",
        formation_role="youtube_note_material",
        family_id="seed-twentythird-youtube-note",
        evidence_kind="twentythird_youtube_note_presence",
        axes=[
            ("curiosity_pressure", 0.66),
            ("memory_pressure", 0.59),
            ("tone_pressure", 0.38),
        ],
        cohesion_note="A youtube-note local space forms as soft reading residue without immediate bridge pressure.",
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "web_chatgpt_local_space_id: %s" % web_chatgpt_space,
        "gemini_cli_local_space_id: %s" % gemini_cli_space,
        "claude_code_local_space_id: %s" % claude_code_space,
        "youtube_note_local_space_id: %s" % youtube_note_space,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
