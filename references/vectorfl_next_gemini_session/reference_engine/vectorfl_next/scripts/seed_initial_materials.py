#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.runtime.observer import build_scoped_reactive_space_observation
from app.runtime.workspace_report import write_workspace_report


def _tail_worklog(worklog_path: Path, line_limit: int = 24) -> str:
    if not worklog_path.exists():
        return "codex worklog not found"
    lines = worklog_path.read_text(encoding="utf-8").splitlines()
    return "\n".join(lines[-line_limit:])


def _format_observation_summary(runtime_root: Path) -> str:
    observation = build_scoped_reactive_space_observation(runtime_root)
    lines = [
        "runtime_root: %s" % runtime_root,
        "cell_count: %s" % observation["cell_count"],
        "reaction_counts:",
    ]
    for key, value in sorted(observation["reaction_counts"].items()):
        lines.append("- %s: %s" % (key, value))
    lines.append("local_space_states:")
    if observation["local_space_states"]:
        for key, value in sorted(observation["local_space_states"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")
    lines.append("bridge_states:")
    if observation["bridge_states"]:
        for key, value in sorted(observation["bridge_states"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")
    return "\n".join(lines)


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    service = FormationService(runtime_root)
    report_path = write_workspace_report(runtime_root)

    fresh_note = service.ingest_material_with_role(
        raw_payload=(
            "Initial fresh note: treat this runtime as a space-first formation field. "
            "Observe whether engine-self and observer materials stay distinct before any point-first pull."
        ),
        actor_id="codex",
        session_id="bootstrap-initial-materials",
        project_id="vectorfl_next",
        source_type="note",
        source_ref="seed:fresh-note:initial",
        formation_role="fresh_material",
        family_id="seed-fresh-note",
    )
    engine_self = service.ingest_material_with_role(
        raw_payload=_tail_worklog(REPO_ROOT / "logs" / "runlogs" / "codex_worklog.md"),
        actor_id="codex",
        session_id="bootstrap-initial-materials",
        project_id="vectorfl_next",
        source_type="worklog",
        source_ref=str(REPO_ROOT / "logs" / "runlogs" / "codex_worklog.md"),
        formation_role="engine_self_material",
        family_id="seed-engine-self",
    )
    observer_material = service.ingest_material_with_role(
        raw_payload=_format_observation_summary(runtime_root),
        actor_id="codex",
        session_id="bootstrap-initial-materials",
        project_id="vectorfl_next",
        source_type="observer_output",
        source_ref=str(report_path),
        formation_role="observer_material",
        family_id="seed-observer",
        lineage_refs=[engine_self.material_id],
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "seeded_materials: 3",
        "fresh_note: %s" % fresh_note.material_id,
        "engine_self: %s" % engine_self.material_id,
        "observer_material: %s" % observer_material.material_id,
        "report_path: %s" % report_path,
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
