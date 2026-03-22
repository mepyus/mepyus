#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.observer import build_scoped_reactive_space_observation, build_session_timeline


def main() -> int:
    runtime_root = Path("runtime")
    recent_limit = None
    recent_seconds = None
    family_id = None
    session_id = None

    args = sys.argv[1:]
    index = 0
    while index < len(args):
        token = args[index]
        if token == "--recent":
            recent_limit = int(args[index + 1])
            index += 2
            continue
        if token == "--recent-seconds":
            recent_seconds = int(args[index + 1])
            index += 2
            continue
        if token == "--family":
            family_id = args[index + 1]
            index += 2
            continue
        if token == "--session":
            session_id = args[index + 1]
            index += 2
            continue
        runtime_root = Path(token)
        index += 1

    observation = build_scoped_reactive_space_observation(
        runtime_root,
        recent_limit=recent_limit,
        recent_seconds=recent_seconds,
        family_id=family_id,
        session_id=session_id,
    )

    lines = [
        "runtime_root: %s" % runtime_root,
        "scope_recent_limit: %s" % recent_limit,
        "scope_recent_seconds: %s" % recent_seconds,
        "scope_family_id: %s" % family_id,
        "scope_session_id: %s" % session_id,
        "cell_count: %s" % observation["cell_count"],
        "process_mode: %s" % observation["process_summary"]["dominant_mode"],
        "process_tags: %s" % ", ".join(observation["process_summary"]["phase_tags"]),
        "process_summary: %s" % observation["process_summary"]["summary_line"],
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

    lines.append("local_space_maturation:")
    if observation["local_space_maturation_signals"]:
        for key, value in sorted(observation["local_space_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("bridge_states:")
    if observation["bridge_states"]:
        for key, value in sorted(observation["bridge_states"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("bridge_maturation:")
    if observation["bridge_maturation_signals"]:
        for key, value in sorted(observation["bridge_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_climate_modes:")
    if observation["terrain_climate_modes"]:
        for key, value in sorted(observation["terrain_climate_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_climate_signals:")
    if observation["terrain_climate_signals"]:
        for key, value in sorted(observation["terrain_climate_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_rhythm_modes:")
    if observation["terrain_rhythm_modes"]:
        for key, value in sorted(observation["terrain_rhythm_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_rhythm_signals:")
    if observation["terrain_rhythm_signals"]:
        for key, value in sorted(observation["terrain_rhythm_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_recurrence_modes:")
    if observation["terrain_recurrence_modes"]:
        for key, value in sorted(observation["terrain_recurrence_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_recurrence_signals:")
    if observation["terrain_recurrence_signals"]:
        for key, value in sorted(observation["terrain_recurrence_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_memory_modes:")
    if observation["terrain_memory_modes"]:
        for key, value in sorted(observation["terrain_memory_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_memory_signals:")
    if observation["terrain_memory_signals"]:
        for key, value in sorted(observation["terrain_memory_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_retention_modes:")
    if observation["terrain_retention_modes"]:
        for key, value in sorted(observation["terrain_retention_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_retention_signals:")
    if observation["terrain_retention_signals"]:
        for key, value in sorted(observation["terrain_retention_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_forgetting_modes:")
    if observation["terrain_forgetting_modes"]:
        for key, value in sorted(observation["terrain_forgetting_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_forgetting_signals:")
    if observation["terrain_forgetting_signals"]:
        for key, value in sorted(observation["terrain_forgetting_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("terrain_components:")
    if observation["terrain_components"]:
        for item in observation["terrain_components"]:
            lines.append(
                "- spaces=%s climate=%s rhythm=%s recurrence=%s memory=%s retention=%s forgetting=%s"
                % (
                    ",".join(item["local_space_ids"]),
                    item["climate_mode"],
                    item["rhythm_mode"],
                    item["recurrence_mode"],
                    item["memory_mode"],
                    item["retention_mode"],
                    item["forgetting_mode"],
                )
            )
    else:
        lines.append("- none")

    lines.append("reactive_cells:")
    has_reactive_cells = False
    for key, value in sorted(observation["reactive_cell_ids"].items()):
        has_reactive_cells = True
        lines.append("- %s: %s" % (key, ", ".join(value)))
    if not has_reactive_cells:
        lines.append("- none")

    lines.append("pressure_signatures:")
    if observation["pressure_signatures"]:
        for key, value in sorted(observation["pressure_signatures"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("pressure_axes:")
    if observation["pressure_axis_distribution"]:
        for axis_name, buckets in sorted(observation["pressure_axis_distribution"].items()):
            bucket_text = ", ".join("%s=%s" % (bucket, count) for bucket, count in sorted(buckets.items()))
            lines.append("- %s: %s" % (axis_name, bucket_text))
    else:
        lines.append("- none")

    lines.append("pressure_axis_combinations:")
    if observation["pressure_axis_combinations"]:
        for key, value in sorted(observation["pressure_axis_combinations"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("pressure_transitions:")
    if observation["pressure_transitions"]:
        for key, value in sorted(observation["pressure_transitions"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("branch_reasons:")
    if observation["branch_reason_counts"]:
        for key, value in sorted(observation["branch_reason_counts"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.append("branched_cells:")
    has_branched_cells = False
    for key, value in sorted(observation["branched_cell_ids"].items()):
        has_branched_cells = True
        lines.append("- %s: %s" % (key, ", ".join(value)))
    if not has_branched_cells:
        lines.append("- none")

    lines.append("branch_sequence:")
    if observation["branch_sequence"]:
        for item in observation["branch_sequence"]:
            lines.append(
                "- %s %s %s %s"
                % (item["occurred_at"], item["cell_id"], item["reason"], item["family_id"])
            )
    else:
        lines.append("- none")

    lines.append("reaction_sequence:")
    if observation["reaction_sequence"]:
        for item in observation["reaction_sequence"]:
            lines.append(
                "- %s %s %s %s"
                % (item["occurred_at"], item["cell_id"], item["reaction_kind"], item["pressure_signature"])
            )
    else:
        lines.append("- none")

    if session_id is not None:
        timeline = build_session_timeline(runtime_root, session_id)
        lines.append("session_timeline:")
        if timeline["timeline"]:
            for item in timeline["timeline"]:
                lines.append(
                    "- %s %s %s %s"
                    % (
                        item["occurred_at"],
                        item["cell_id"],
                        item["reaction_kind"],
                        item["pressure_signature"],
                    )
                )
        else:
            lines.append("- none")
        lines.append("session_phases:")
        if timeline["phases"]:
            for item in timeline["phases"]:
                lines.append(
                    "- %s[%s] %s..%s count=%s cells=%s"
                    % (
                        item["reaction_kind"],
                        item["pressure_signature"],
                        item["start_at"],
                        item["end_at"],
                        item["event_count"],
                        ",".join(item["cell_ids"]),
                    )
                )
        else:
            lines.append("- none")

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
