from __future__ import annotations

import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.operating_ui_phase1 import (
    build_operating_ui_phase1_shell_data,
    build_phase1_probe_state,
    phase1_probe_activate_seed_from_memory,
    phase1_probe_clear_active_seed,
    phase1_probe_clear_history_reread_context,
    phase1_probe_memory_select_sticker,
    phase1_probe_open_from_history,
    phase1_probe_apply_quick_start,
    phase1_probe_reset_blank,
    phase1_probe_restore_residue,
    phase1_probe_search_open_in_explore,
    phase1_probe_search_open_in_memory,
    phase1_probe_search_use_in_similar,
    phase1_probe_select_explore_path,
)


RUNTIME_ROOT = REPO_ROOT / "runtime"
RESULT_ROOT = REPO_ROOT / "runtime" / "validation"
RESULT_PATH = RESULT_ROOT / "phase1_interaction_invariant_probe_v1.json"
REPORT_PATH = REPO_ROOT / "docs" / "reports" / "phase1_interaction_invariant_and_regression_probe_v1.md"


def main() -> None:
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    shell_data = build_operating_ui_phase1_shell_data(RUNTIME_ROOT)
    base_state = build_phase1_probe_state(shell_data)
    results = {
        "initial_state": _check_initial_state(shell_data, base_state),
        "runtime_fallback_state": _check_runtime_fallback_state(),
        "scenario_blank_quickstart_manual": _check_blank_quickstart_manual(base_state),
        "scenario_search_jump_ownership": _check_search_jump_ownership(base_state),
        "scenario_memory_seed_clear": _check_memory_seed_clear(base_state),
        "scenario_residue_vs_blank": _check_residue_vs_blank(base_state),
        "scenario_history_reread_handoff": _check_history_reread_handoff(base_state),
        "manual_walkthrough_only": [
            "preset != taxonomy is still primarily wording/UI governance rather than pure-state assertion",
            "similar result != recommendation remains partly wording-bound because result card phrasing is not browser-asserted here",
            "imported current path != saved interpretation path is asserted by state separation, but surface readability still needs manual walkthrough confirmation",
        ],
    }
    RESULT_PATH.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_report(results)
    print(json.dumps({"result": str(RESULT_PATH.relative_to(REPO_ROOT)), "report": str(REPORT_PATH.relative_to(REPO_ROOT))}, ensure_ascii=False))


def _assert(condition: bool, label: str, bucket: list[str]) -> None:
    if condition:
        bucket.append(label)
    else:
        raise AssertionError(label)


def _check_initial_state(shell_data: dict, base_state: dict) -> dict:
    passed: list[str] = []
    shell = shell_data["phase1_shell"]
    spine = shell["shared_spine"]
    _assert(spine["selected_memory_sticker_id"] is None, "selected_memory_sticker_id is None", passed)
    _assert(spine["similar_seed_ref"] is None, "similar_seed_ref is None", passed)
    _assert(spine["selected_object_id"] is None, "blank start object is None", passed)
    _assert(spine["selected_lens_id"] is None, "blank start lens is None", passed)
    _assert(spine["selected_position_value"] is None, "blank start position is None", passed)
    _assert(spine["current_preview_connection"] is None, "blank start preview is None", passed)
    quick = shell["quick_start_suggestion"]
    _assert(bool(quick.get("object_id")), "quick-start has suggestion object", passed)
    _assert(bool(quick.get("preview_connection")), "quick-start has preview suggestion", passed)
    _assert(base_state["path_state"] == "blank", "probe state begins blank", passed)
    runtime_binding = shell["runtime_binding"]
    _assert("live runtime observation" in runtime_binding["operating_observation"]["provenance_summary"], "loaded mode shows live provenance summary", passed)
    _assert("runtime options" in runtime_binding["explore_binding"]["provenance_summary"], "loaded mode shows runtime option provenance", passed)
    _assert("stored saved paths" in runtime_binding["memory_binding"]["provenance_summary"], "memory provenance summary uses stored wording", passed)
    return {"passed": passed}


def _check_runtime_fallback_state() -> dict:
    passed: list[str] = []
    shell_data = build_operating_ui_phase1_shell_data(RUNTIME_ROOT, live_mode="unavailable")
    shell = shell_data["phase1_shell"]
    spine = shell["shared_spine"]
    runtime_binding = shell["runtime_binding"]
    _assert(shell_data["state"] == "live_unavailable", "runtime unavailable mode is exposed", passed)
    _assert(spine["selected_object_id"] is None, "runtime unavailable still keeps blank start", passed)
    _assert(spine["selected_memory_sticker_id"] is None, "runtime unavailable does not auto-select memory", passed)
    _assert(spine["similar_seed_ref"] is None, "runtime unavailable does not auto-activate seed", passed)
    _assert((runtime_binding["explore_binding"]["object_source_state"] in {"available", "fallback"}), "runtime unavailable still resolves object source state safely", passed)
    _assert(bool(runtime_binding["search_binding"]["source_note"]), "runtime unavailable exposes degraded search note", passed)
    _assert("degraded" in runtime_binding["operating_observation"]["provenance_summary"], "runtime unavailable uses degraded operating provenance wording", passed)
    _assert(("fallback" in runtime_binding["explore_binding"]["provenance_summary"]) or ("fallback" in runtime_binding["explore_binding"]["object_source_note"]), "runtime unavailable keeps fallback explore provenance wording", passed)
    return {"passed": passed}


def _check_blank_quickstart_manual(base_state: dict) -> dict:
    passed: list[str] = []
    quick = phase1_probe_apply_quick_start(base_state)
    _assert(quick["shared_spine"]["selected_object_id"] is not None, "quick-start imports object into current path", passed)
    _assert(quick["shared_spine"]["selected_memory_sticker_id"] is None, "quick-start does not create memory selection", passed)
    _assert(quick["shared_spine"]["similar_seed_ref"] is None, "quick-start does not activate seed", passed)
    _assert(quick["path_state"] == "quick-start applied", "quick-start path state is explicit", passed)
    manual = phase1_probe_select_explore_path(quick, object_id="manual_object")
    _assert(manual["path_state"] == "manually progressed", "manual selection changes path state", passed)
    _assert(manual["shared_spine"]["selected_object_id"] == "manual_object", "manual selection overrides object", passed)
    return {"passed": passed}


def _check_search_jump_ownership(base_state: dict) -> dict:
    passed: list[str] = []
    explore = phase1_probe_search_open_in_explore(base_state, object_id="obj_a", lens_id="structure", position_value="anchor")
    _assert(explore["shared_spine"]["selected_object_id"] == "obj_a", "Search open in Explore imports current path object", passed)
    _assert(explore["shared_spine"]["selected_memory_sticker_id"] is None, "Search open in Explore does not select memory", passed)
    _assert(explore["shared_spine"]["similar_seed_ref"] is None, "Search open in Explore does not activate seed", passed)
    memory = phase1_probe_search_open_in_memory(base_state, "stk_a")
    _assert(memory["shared_spine"]["selected_memory_sticker_id"] == "stk_a", "Search open in Memory selects sticker only", passed)
    _assert(memory["shared_spine"]["similar_seed_ref"] is None, "Search open in Memory does not activate seed", passed)
    similar = phase1_probe_search_use_in_similar(memory, "seed_a")
    _assert(similar["shared_spine"]["similar_seed_ref"] == "seed_a", "Search use in Similar activates seed", passed)
    _assert(similar["shared_spine"]["selected_memory_sticker_id"] == "stk_a", "Search use in Similar does not clear prior memory selection", passed)
    return {"passed": passed}


def _check_memory_seed_clear(base_state: dict) -> dict:
    passed: list[str] = []
    selected = phase1_probe_memory_select_sticker(base_state, "stk_m")
    _assert(selected["shared_spine"]["selected_memory_sticker_id"] == "stk_m", "Memory selection selects sticker", passed)
    _assert(selected["shared_spine"]["similar_seed_ref"] is None, "Memory selection alone does not auto-activate seed", passed)
    seeded = phase1_probe_activate_seed_from_memory(selected, "seed_m")
    _assert(seeded["shared_spine"]["similar_seed_ref"] == "seed_m", "explicit seed activation sets seed", passed)
    _assert(seeded["shared_spine"]["selected_memory_sticker_id"] == "stk_m", "explicit seed activation preserves Memory selection", passed)
    cleared = phase1_probe_clear_active_seed(seeded)
    _assert(cleared["shared_spine"]["similar_seed_ref"] is None, "clear active seed detaches seed", passed)
    _assert(cleared["shared_spine"]["selected_memory_sticker_id"] == "stk_m", "clear active seed does not mutate Memory selection", passed)
    return {"passed": passed}


def _check_residue_vs_blank(base_state: dict) -> dict:
    passed: list[str] = []
    residue = {
        "object_id": "obj_r",
        "lens_id": "memory",
        "position_value": "sticker",
        "preview_ready": True,
    }
    restored = phase1_probe_restore_residue(base_state, residue)
    _assert(restored["shared_spine"]["selected_object_id"] == "obj_r", "residue restore imports residue object", passed)
    _assert(restored["path_state"] == "residue restored", "residue restore has separate path state", passed)
    _assert(restored["shared_spine"]["selected_memory_sticker_id"] is None, "residue restore does not select memory", passed)
    blank = phase1_probe_reset_blank(restored)
    _assert(blank["shared_spine"]["selected_object_id"] is None, "blank reset clears object", passed)
    _assert(blank["shared_spine"]["current_preview_connection"] is None, "blank reset clears preview", passed)
    _assert(blank["path_state"] == "blank", "blank reset returns blank state", passed)
    return {"passed": passed}


def _check_history_reread_handoff(base_state: dict) -> dict:
    passed: list[str] = []
    opened = phase1_probe_open_from_history(
        base_state,
        asset_id="asset_h",
        snapshot_ref="asset_h",
        cluster_ref="cluster-1",
        trace_ref=None,
        summary="grounding shift group",
        source_note="limited by available history source",
    )
    _assert(opened["history_reread_context"] is not None, "history open attaches reread context", passed)
    _assert(opened["shared_spine"]["selected_memory_sticker_id"] is None, "history open does not set saved path", passed)
    _assert(opened["shared_spine"]["similar_seed_ref"] is None, "history open does not activate seed", passed)
    _assert(opened["shared_spine"]["selected_object_id"] is None, "history open does not overwrite blank authoring object", passed)
    _assert(opened["path_state"] == "blank", "history open keeps current path ownership unchanged", passed)
    cleared = phase1_probe_clear_history_reread_context(opened)
    _assert(cleared["history_reread_context"] is None, "clear history context detaches reread reference only", passed)
    _assert(cleared["shared_spine"]["selected_memory_sticker_id"] is None, "clear history context does not mutate saved path selection", passed)
    _assert(cleared["shared_spine"]["similar_seed_ref"] is None, "clear history context does not mutate seed", passed)
    return {"passed": passed}


def _write_report(results: dict) -> None:
    lines: list[str] = []
    lines.append("# phase1 interaction invariant and regression probe v1")
    lines.append("")
    lines.append("## package status")
    lines.append("")
    lines.append("complete for this turn")
    lines.append("")
    lines.append("## probe assets")
    lines.append("")
    lines.append(f"- script: [run_phase1_interaction_invariant_probe.py]({(REPO_ROOT / 'scripts' / 'run_phase1_interaction_invariant_probe.py').as_posix()})")
    lines.append(f"- result: [phase1_interaction_invariant_probe_v1.json]({RESULT_PATH.as_posix()})")
    lines.append("")
    lines.append("## invariants checked in code")
    lines.append("")
    for section in [
        "initial_state",
        "runtime_fallback_state",
        "scenario_blank_quickstart_manual",
        "scenario_search_jump_ownership",
        "scenario_memory_seed_clear",
        "scenario_residue_vs_blank",
        "scenario_history_reread_handoff",
    ]:
        lines.append(f"### {section}")
        lines.append("")
        for item in results[section]["passed"]:
            lines.append(f"- `{item}`")
        lines.append("")
    lines.append("## still manual walkthrough level")
    lines.append("")
    for item in results["manual_walkthrough_only"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## watchpoints")
    lines.append("")
    lines.append("- pure-state probe does not assert browser DOM wording, so UI anti-confusion language can still drift without failing this script")
    lines.append("- Search -> Similar ownership is asserted at shared-state level, but result-card rhetoric still needs periodic manual check")
    lines.append("- import-context readability is validated structurally, not visually")
    lines.append("- history reread context is asserted separately from shared spine mutation, but badge/helper-text readability still needs manual check")
    lines.append("")
    lines.append("## next candidates")
    lines.append("")
    lines.append("- add one short manual walkthrough report whenever phase1 wording around import or seed changes")
    lines.append("- keep the probe synced if phase1 shared spine fields change")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
