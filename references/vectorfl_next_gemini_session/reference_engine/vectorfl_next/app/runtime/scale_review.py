from pathlib import Path
import json

from app.core.formation_service import FormationService
from app.runtime.observer import build_reactive_space_observation
from app.runtime.sparse_presence_review import build_sparse_presence_review


NON_PURPOSE_ROLES = {
    "sparse_presence_material",
    "reserve_fragment_material",
    "unknown_fragment_material",
    "question_residue_material",
    "unread_quote_material",
    "failed_experiment_material",
    "book_note_material",
    "book_highlight_material",
    "reading_note_material",
}


def _role_counts(runtime_root: Path) -> dict:
    counts = {}
    materials_root = runtime_root / "core" / "materials"
    if not materials_root.exists():
        return counts
    for path in sorted(materials_root.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        role = record.get("metadata", {}).get("formation_role", "unknown")
        counts[role] = counts.get(role, 0) + 1
    return counts


def build_first_scale_review(runtime_root: Path) -> dict:
    service = FormationService(runtime_root)
    observation = build_reactive_space_observation(runtime_root)
    sparse_review = build_sparse_presence_review(runtime_root)
    role_counts = _role_counts(runtime_root)

    local_space_count = len(list(service.local_spaces.list_ids()))
    bridge_count = len(list(service.bridges.list_ids()))
    terrain_component_count = len(observation["terrain_components"])

    bridge_state_total = sum(observation["bridge_states"].values())
    local_space_state_total = sum(observation["local_space_states"].values())
    quiet_non_bridge_local_spaces = (
        sparse_review["quiet_local_space_count"] - sparse_review["bridge_exposed_local_space_count"]
    )
    return_role_count = sum(
        count for role, count in role_counts.items() if "return" in role or "reflux" in role
    )
    non_purpose_role_count = sum(
        count for role, count in role_counts.items() if role in NON_PURPOSE_ROLES
    )

    return {
        "runtime_root": str(runtime_root),
        "local_space_count": local_space_count,
        "bridge_count": bridge_count,
        "terrain_component_count": terrain_component_count,
        "axes": {
            "quiet_persistence": {
                "summary": (
                    "quiet_non_bridge=%s quiet_total=%s sparse_retention=%s"
                    % (
                        quiet_non_bridge_local_spaces,
                        sparse_review["quiet_local_space_count"],
                        sparse_review["sparse_retention_component_count"],
                    )
                ),
                "quiet_local_spaces": sparse_review["quiet_local_space_count"],
                "bridge_free_quiet_local_spaces": quiet_non_bridge_local_spaces,
                "forming_local_spaces": sparse_review["forming_local_space_count"],
                "sparse_retention_components": sparse_review["sparse_retention_component_count"],
            },
            "multi_speed_coexistence": {
                "summary": (
                    "forming=%s bridge_exposed=%s thickening=%s relocation=%s"
                    % (
                        observation["local_space_states"].get("forming", 0),
                        observation["local_space_states"].get("bridge_exposed", 0),
                        observation["reaction_counts"].get("thickening", 0),
                        observation["reaction_counts"].get("relocation", 0),
                    )
                ),
                "forming_local_spaces": observation["local_space_states"].get("forming", 0),
                "bridge_exposed_local_spaces": observation["local_space_states"].get(
                    "bridge_exposed", 0
                ),
                "thickening_reactions": observation["reaction_counts"].get("thickening", 0),
                "relocation_reactions": observation["reaction_counts"].get("relocation", 0),
                "single_local_climate_components": observation["terrain_climate_modes"].get(
                    "single_local_climate", 0
                ),
                "resonant_climate_components": observation["terrain_climate_modes"].get(
                    "resonant_climate", 0
                ),
            },
            "reflux_effect": {
                "summary": "return_roles=%s bridge_memory=%s" % (
                    return_role_count,
                    observation["terrain_memory_signals"].get("bridge_memory_present", 0),
                ),
                "return_role_count": return_role_count,
                "bridge_memory_present": observation["terrain_memory_signals"].get(
                    "bridge_memory_present", 0
                ),
                "persistent_bridge_memory": observation["terrain_memory_signals"].get(
                    "persistent_bridge_memory", 0
                ),
            },
            "perspective_invariance": {
                "summary": (
                    "local_space_totals_align=%s terrain_totals_align=%s bridge_totals_align=%s"
                    % (
                        local_space_count == local_space_state_total,
                        terrain_component_count == sparse_review["terrain_component_count"],
                        bridge_count == bridge_state_total,
                    )
                ),
                "service_local_space_count": local_space_count,
                "observer_local_space_state_total": local_space_state_total,
                "observer_terrain_components": terrain_component_count,
                "sparse_review_terrain_components": sparse_review["terrain_component_count"],
                "service_bridge_count": bridge_count,
                "observer_bridge_state_total": bridge_state_total,
            },
            "non_purpose_survival": {
                "summary": "non_purpose_roles=%s unknown_like=%s" % (
                    non_purpose_role_count,
                    role_counts.get("unknown_fragment_material", 0)
                    + role_counts.get("question_residue_material", 0),
                ),
                "non_purpose_role_count": non_purpose_role_count,
                "unknown_fragment_count": role_counts.get("unknown_fragment_material", 0),
                "reserve_fragment_count": role_counts.get("reserve_fragment_material", 0),
                "question_residue_count": role_counts.get("question_residue_material", 0),
                "unread_quote_count": role_counts.get("unread_quote_material", 0),
                "failed_experiment_count": role_counts.get("failed_experiment_material", 0),
            },
        },
    }


def write_first_scale_review(runtime_root: Path) -> Path:
    review = build_first_scale_review(runtime_root)
    report_path = runtime_root / "reports" / "first_scale_review.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# First Scale Review",
        "",
        "- local_space_count: %s" % review["local_space_count"],
        "- bridge_count: %s" % review["bridge_count"],
        "- terrain_component_count: %s" % review["terrain_component_count"],
    ]
    for axis_name, axis in review["axes"].items():
        lines.extend(["", "## %s" % axis_name.replace("_", " ").title(), ""])
        lines.append("- summary: %s" % axis["summary"])
        for key, value in axis.items():
            if key == "summary":
                continue
            lines.append("- %s: %s" % (key, value))
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path
