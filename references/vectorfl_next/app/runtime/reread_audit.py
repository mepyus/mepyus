from pathlib import Path
from typing import Dict, List

from app.runtime.observer import build_reactive_space_observation


def build_reread_audit(runtime_root: Path) -> Dict[str, object]:
    observation = build_reactive_space_observation(runtime_root)

    layer_counts = {
        "terrain_climate": sum(observation.get("terrain_climate_modes", {}).values()),
        "terrain_rhythm": sum(observation.get("terrain_rhythm_modes", {}).values()),
        "terrain_recurrence": sum(observation.get("terrain_recurrence_modes", {}).values()),
        "terrain_memory": sum(observation.get("terrain_memory_modes", {}).values()),
        "terrain_retention": sum(observation.get("terrain_retention_modes", {}).values()),
        "terrain_forgetting": sum(observation.get("terrain_forgetting_modes", {}).values()),
    }
    active_layers = [key for key, value in layer_counts.items() if value > 0]

    risks: List[str] = []
    if len(active_layers) >= 5:
        risks.append("reread_stack_is_deep")
    if observation.get("cell_count", 0) <= 3 and len(active_layers) >= 4:
        risks.append("reread_density_exceeds_runtime_scale")
    if not observation.get("local_space_states"):
        risks.append("reread_without_local_space_visibility")

    posture = "balanced_reread"
    if "reread_density_exceeds_runtime_scale" in risks:
        posture = "reread_heavy"
    elif not active_layers:
        posture = "reread_light"

    return {
        "runtime_root": str(runtime_root),
        "posture": posture,
        "active_layers": active_layers,
        "layer_counts": layer_counts,
        "cell_count": observation.get("cell_count", 0),
        "local_space_states": observation.get("local_space_states", {}),
        "bridge_states": observation.get("bridge_states", {}),
        "risks": risks,
        "advice": _build_advice(risks),
    }


def write_reread_audit(runtime_root: Path) -> Path:
    audit = build_reread_audit(runtime_root)
    report_path = runtime_root / "reports" / "reread_audit.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Reread Audit",
        "",
        "## Posture",
        "",
        "- runtime_root: %s" % audit["runtime_root"],
        "- posture: %s" % audit["posture"],
        "- cell_count: %s" % audit["cell_count"],
        "",
        "## Active Layers",
        "",
    ]
    if audit["active_layers"]:
        for key in audit["active_layers"]:
            lines.append("- %s: %s" % (key, audit["layer_counts"][key]))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Risks",
            "",
        ]
    )
    if audit["risks"]:
        for item in audit["risks"]:
            lines.append("- %s" % item)
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Advice",
            "",
        ]
    )
    for item in audit["advice"]:
        lines.append("- %s" % item)

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def _build_advice(risks: List[str]) -> List[str]:
    advice = [
        "Treat reread layers as descriptive only.",
        "Do not move terrain reread vocabulary into core ontology.",
    ]
    if "reread_stack_is_deep" in risks:
        advice.append("Prefer growing runtime material before adding new reread layers.")
    if "reread_density_exceeds_runtime_scale" in risks:
        advice.append("Pause and compare reread density against actual multi-local terrain growth.")
    if "reread_without_local_space_visibility" in risks:
        advice.append("Do not expand reread until local-space formation is visible in runtime.")
    return advice
