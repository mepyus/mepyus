from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.operating_ui_history import (  # noqa: E402
    build_operating_ui_history_shell_data,
    render_operating_ui_history_shell_html,
)
from app.runtime.operating_ui_phase1 import build_operating_ui_phase1_shell_data  # noqa: E402


RUNTIME_ROOT = REPO_ROOT / "runtime"
RESULT_ROOT = RUNTIME_ROOT / "validation"
RESULT_PATH = RESULT_ROOT / "phase2_history_surface_probe_v1.json"
REPORT_PATH = REPO_ROOT / "docs" / "reports" / "phase2_semantic_boundary_and_invariant_probe_lock_v1.md"


def main() -> None:
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    loaded = build_operating_ui_history_shell_data(RUNTIME_ROOT)
    loaded_html = render_operating_ui_history_shell_html(loaded)
    history_context_phase1 = build_operating_ui_phase1_shell_data(
        RUNTIME_ROOT,
        asset_id=loaded.get("selected_asset_id"),
        history_snapshot_ref=loaded.get("selected_asset_id"),
        history_cluster_ref=((loaded.get("activity_clusters") or [{}])[0] or {}).get("cluster_id"),
        history_reread_summary=((loaded.get("activity_clusters") or [{}])[0] or {}).get("title"),
        history_source_note=((loaded.get("activity_clusters") or [{}])[0] or {}).get("summary"),
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        sparse_root = Path(tmpdir)
        sparse = build_operating_ui_history_shell_data(sparse_root)
        sparse_html = render_operating_ui_history_shell_html(sparse)

    results = {
        "history_surface_invariants": _check_history_surface_invariants(loaded, loaded_html, sparse, sparse_html),
        "cross_surface_handoff_invariants": _check_cross_surface_handoff_invariants(history_context_phase1),
        "wording_presence_sanity": _check_wording_presence_sanity(loaded_html),
        "manual_governance_only": [
            "cluster quality still needs periodic manual reading because grouping quality cannot be fully asserted from tokens alone",
            "translated trace readability is only partially assertable in shell data; final operator-facing nuance still needs manual walkthrough",
            "degraded honesty tone can still drift visually without failing these token checks",
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


def _check_history_surface_invariants(loaded: dict, loaded_html: str, sparse: dict, sparse_html: str) -> dict:
    passed: list[str] = []
    _assert(loaded["state"] in {"loaded", "partial_trace_only"}, "history surface is readable with available runtime data", passed)
    _assert(loaded["replayable_state"]["state"] == "available", "reread preview stays available as view-level slice when source exists", passed)
    _assert(all(item.get("kind") == "translated trace read" for item in loaded.get("trace_entries", [])), "trace entries remain translated/operator-facing units", passed)
    _assert(sparse["state"] == "source_unavailable", "sparse root resolves to source_unavailable rather than execution failure", passed)
    _assert("no runs yet / latest snapshot source unavailable" in sparse_html, "sparse mode shows honest unavailable wording", passed)
    _assert("reread preview unavailable" in sparse_html, "sparse mode keeps reread preview honesty wording", passed)
    return {"passed": passed}


def _check_cross_surface_handoff_invariants(phase1_shell_data: dict) -> dict:
    passed: list[str] = []
    shell = phase1_shell_data["phase1_shell"]
    spine = shell["shared_spine"]
    context = shell.get("history_reread_context")
    _assert(bool(context), "open from history attaches reread context only", passed)
    _assert(spine["selected_memory_sticker_id"] is None, "history handoff does not create saved path selection", passed)
    _assert(spine["similar_seed_ref"] is None, "history handoff does not activate seed", passed)
    _assert(spine["selected_object_id"] is None, "history handoff does not overwrite current path authoring", passed)
    _assert(context.get("summary"), "history handoff carries summary reference only", passed)
    return {"passed": passed}


def _check_wording_presence_sanity(loaded_html: str) -> dict:
    passed: list[str] = []
    _assert("History / Reread / Trace" in loaded_html, "history surface title uses reread wording", passed)
    _assert("open in phase1 with reread context" in loaded_html, "phase1 handoff wording uses reread context", passed)
    _assert("prior state slice only / no rerun / no simulation" in loaded_html, "reread preview wording keeps execution boundary explicit", passed)
    _assert("translated state and activity units / not raw event lines" in loaded_html, "trace wording stays translated rather than raw", passed)
    _assert("replay in phase1" not in loaded_html, "forbidden replay-in-phase1 wording is absent", passed)
    _assert("restore state in phase1" not in loaded_html, "forbidden restore-state wording is absent", passed)
    _assert("load this state into phase1" not in loaded_html, "forbidden load-state wording is absent", passed)
    return {"passed": passed}


def _write_report(results: dict) -> None:
    lines: list[str] = []
    lines.append("# phase2 semantic boundary and invariant probe lock v1")
    lines.append("")
    lines.append("## package status")
    lines.append("")
    lines.append("complete for this turn")
    lines.append("")
    lines.append("## wording audit and cleanup")
    lines.append("")
    lines.append("- kept `history`, `trace`, `reread preview`, `prior state slice`, and `open in phase1 with reread context`")
    lines.append("- reduced replay drift by shifting the visible page title from `history / replay / trace` to `history / reread / trace`")
    lines.append("- renamed `Replayable State Preview` to `Rereadable State Preview`")
    lines.append("- kept degraded/unavailable wording honest without making it sound like execution failure")
    lines.append("")
    lines.append("## invariants checked in probe")
    lines.append("")
    for section in [
        "history_surface_invariants",
        "cross_surface_handoff_invariants",
        "wording_presence_sanity",
    ]:
        lines.append(f"### {section}")
        lines.append("")
        for item in results[section]["passed"]:
            lines.append(f"- `{item}`")
        lines.append("")
    lines.append("## still governance-level only")
    lines.append("")
    for item in results["manual_governance_only"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## freeze-candidate note")
    lines.append("")
    lines.append("### already locked")
    lines.append("")
    lines.append("- read-oriented time-axis companion")
    lines.append("- replay means view-level reread only")
    lines.append("- trace means translated operator-facing reading unit")
    lines.append("- phase1 handoff remains explicit contextual reference only")
    lines.append("")
    lines.append("### still open")
    lines.append("")
    lines.append("- richer clustering quality")
    lines.append("- source sparsity handling polish")
    lines.append("- readability and wording trim")
    lines.append("")
    lines.append("## anti-drift rules")
    lines.append("")
    lines.append("- history surface must not become command center")
    lines.append("- replay must not drift into execution")
    lines.append("- trace must not drift into raw audit console")
    lines.append("- phase1 handoff must remain contextual reference only")
    lines.append("- saved-path curation is still outside this surface")
    lines.append("")
    lines.append("## watchpoints")
    lines.append("")
    lines.append("- `replay` still exists in internal naming, so visible wording must keep favoring `reread`")
    lines.append("- sparse history can still make cluster quality feel thinner than the labels imply")
    lines.append("- token probes do not fully guarantee visual tone or operator trust")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
