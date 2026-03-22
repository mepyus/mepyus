from pathlib import Path

from app.runtime.file_store import JsonDirectoryStore
from app.runtime.observer import build_reactive_space_observation


def write_reactive_space_report(runtime_root: Path) -> Path:
    observation = build_reactive_space_observation(runtime_root)
    space_manifest_store = JsonDirectoryStore(runtime_root / "manifests" / "reactive_spaces")
    cell_manifest_store = JsonDirectoryStore(runtime_root / "manifests" / "reactive_cells")
    bridge_manifest_store = JsonDirectoryStore(runtime_root / "manifests" / "bridges")

    report_path = runtime_root / "reports" / "reactive_space_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reactive Space Report",
        "",
        "## Process",
        "",
        "- mode: %s" % observation["process_summary"]["dominant_mode"],
        "- summary: %s" % observation["process_summary"]["summary_line"],
        "",
        "## Local Space Signals",
        "",
    ]
    if observation["local_space_maturation_signals"]:
        for key, value in sorted(observation["local_space_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Local Space Coexistence",
            "",
        ]
    )
    if observation["local_space_coexistence_modes"]:
        for key, value in sorted(observation["local_space_coexistence_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Bridge Signals",
            "",
        ]
    )
    if observation["bridge_maturation_signals"]:
        for key, value in sorted(observation["bridge_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Climate",
            "",
        ]
    )
    if observation["terrain_climate_modes"]:
        for key, value in sorted(observation["terrain_climate_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Climate Signals",
            "",
        ]
    )
    if observation["terrain_climate_signals"]:
        for key, value in sorted(observation["terrain_climate_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Rhythm",
            "",
        ]
    )
    if observation["terrain_rhythm_modes"]:
        for key, value in sorted(observation["terrain_rhythm_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Rhythm Signals",
            "",
        ]
    )
    if observation["terrain_rhythm_signals"]:
        for key, value in sorted(observation["terrain_rhythm_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Recurrence",
            "",
        ]
    )
    if observation["terrain_recurrence_modes"]:
        for key, value in sorted(observation["terrain_recurrence_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Recurrence Signals",
            "",
        ]
    )
    if observation["terrain_recurrence_signals"]:
        for key, value in sorted(observation["terrain_recurrence_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Memory",
            "",
        ]
    )
    if observation["terrain_memory_modes"]:
        for key, value in sorted(observation["terrain_memory_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Memory Signals",
            "",
        ]
    )
    if observation["terrain_memory_signals"]:
        for key, value in sorted(observation["terrain_memory_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Retention",
            "",
        ]
    )
    if observation["terrain_retention_modes"]:
        for key, value in sorted(observation["terrain_retention_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Retention Signals",
            "",
        ]
    )
    if observation["terrain_retention_signals"]:
        for key, value in sorted(observation["terrain_retention_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Forgetting",
            "",
        ]
    )
    if observation["terrain_forgetting_modes"]:
        for key, value in sorted(observation["terrain_forgetting_modes"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Forgetting Signals",
            "",
        ]
    )
    if observation["terrain_forgetting_signals"]:
        for key, value in sorted(observation["terrain_forgetting_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Terrain Components",
            "",
        ]
    )
    if observation["terrain_components"]:
        for index, component in enumerate(observation["terrain_components"], start=1):
            bridge_text = ", ".join(
                "%s=%s" % (key, value) for key, value in sorted(component["bridge_state_counts"].items())
            ) or "none"
            evidence = ", ".join(component.get("climate_evidence", {}).get("signals", ())) or "none"
            rhythm = ", ".join(component.get("rhythm_evidence", {}).get("signals", ())) or "none"
            recurrence = ", ".join(component.get("recurrence_evidence", {}).get("signals", ())) or "none"
            memory = ", ".join(component.get("memory_evidence", {}).get("signals", ())) or "none"
            retention = ", ".join(component.get("retention_evidence", {}).get("signals", ())) or "none"
            forgetting = ", ".join(component.get("forgetting_evidence", {}).get("signals", ())) or "none"
            lines.append(
                "- component-%s climate=%s rhythm=%s recurrence=%s memory=%s retention=%s forgetting=%s shared_axes=%s union_axes=%s climate_evidence=%s rhythm_evidence=%s recurrence_evidence=%s memory_evidence=%s retention_evidence=%s forgetting_evidence=%s spaces=%s states=%s bridges=%s"
                % (
                    index,
                    component.get("climate_mode", "unknown_climate"),
                    component.get("rhythm_mode", "sparse_rhythm"),
                    component.get("recurrence_mode", "sparse_recurrence"),
                    component.get("memory_mode", "sparse_memory"),
                    component.get("retention_mode", "sparse_retention"),
                    component.get("forgetting_mode", "held_memory"),
                    ",".join(component.get("shared_pressure_axes", ())) or "none",
                    ",".join(component.get("union_pressure_axes", ())) or "none",
                    evidence,
                    rhythm,
                    recurrence,
                    memory,
                    retention,
                    forgetting,
                    ",".join(component["local_space_ids"]),
                    ",".join(component["states"]),
                    bridge_text,
                )
            )
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Local Spaces",
            "",
        ]
    )
    space_manifests = sorted(
        space_manifest_store.read_all(),
        key=lambda item: (item.get("boundary_durability_score", 0), item.get("shared_boundary_strength", 0)),
        reverse=True,
    )
    if space_manifests:
        for manifest in space_manifests:
            evidence = ", ".join(manifest.get("maturation_evidence", {}).get("signals", ())) or "none"
            pressure_axes = ",".join(manifest.get("terrain_pressure_axes", ())) or "none"
            lines.append(
                "- %s state=%s coexistence=%s pressure_axes=%s boundary_durability=%s evidence=%s"
                % (
                    manifest["local_space_id"],
                    manifest["state"],
                    manifest.get("coexistence_mode", "isolated_local"),
                    pressure_axes,
                    manifest.get("boundary_durability_score", 0),
                    evidence,
                )
            )
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Cells",
            "",
        ]
    )
    cell_manifests = sorted(
        cell_manifest_store.read_all(),
        key=lambda item: (item.get("boundary_strength", 0), item.get("seed_count", 0)),
        reverse=True,
    )
    if cell_manifests:
        for manifest in cell_manifests:
            lines.append(
                "- %s state=%s boundary_strength=%s seeds=%s"
                % (
                    manifest["cell_id"],
                    manifest["state"],
                    manifest.get("boundary_strength", 0),
                    manifest.get("seed_count", 0),
                )
            )
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Bridges",
            "",
        ]
    )
    bridge_manifests = sorted(
        bridge_manifest_store.read_all(),
        key=lambda item: (item.get("support_round_count", 0), item.get("trace_ref_count", 0)),
        reverse=True,
    )
    if bridge_manifests:
        for manifest in bridge_manifests:
            evidence = ", ".join(manifest.get("maturation_evidence", {}).get("signals", ())) or "none"
            lines.append(
                "- %s state=%s durability=%s evidence=%s"
                % (
                    manifest["bridge_id"],
                    manifest["state"],
                    manifest.get("durability_mode", "unknown"),
                    evidence,
                )
            )
    else:
        lines.append("- none")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
