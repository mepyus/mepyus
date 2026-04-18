#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.line_thickening import (
    RereadObservation,
    record_reread_observation,
    refresh_line_registry_entry,
)


def _now_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _line_summary(runtime_root: Path, line_name: str) -> dict:
    registry = json.loads((runtime_root / "manifests" / "line_registry.json").read_text(encoding="utf-8"))
    row = next((item for item in registry.get("lines", []) if item.get("line_name") == line_name), {})
    return {
        "status": row.get("status"),
        "thickness_level": row.get("thickness_level"),
        "promotion_scope": row.get("promotion_scope"),
        "validation_profile": row.get("validation_profile"),
        "primary_only_validation_profile": row.get("primary_only_validation_profile"),
        "derived_residue_trend": row.get("derived_residue_trend"),
        "derived_residue_persistence": row.get("derived_residue_persistence"),
        "derived_residue_robustness": row.get("derived_residue_robustness"),
        "derived_reintroduction_status": row.get("derived_reintroduction_status"),
        "derived_reintroduction_trigger": row.get("derived_reintroduction_trigger"),
        "last_derived_reintroduction_offset": row.get("last_derived_reintroduction_offset"),
        "recent_window_size_used": row.get("recent_window_size_used"),
        "recent_decay_streak": row.get("recent_decay_streak"),
        "recent_primary_vs_derived_summary": row.get("recent_primary_vs_derived_summary"),
        "trend_window_agreement_summary": row.get("trend_window_agreement_summary"),
        "persistence_basis_summary": row.get("persistence_basis_summary"),
    }


def _prepare_minimal_sandbox_runtime(main_runtime: Path, sandbox_root: Path) -> None:
    (sandbox_root / "logs").mkdir(parents=True, exist_ok=True)
    (sandbox_root / "manifests").mkdir(parents=True, exist_ok=True)
    for relative_path in (
        Path("logs/reread_observation_log.jsonl"),
        Path("logs/line_promotion_log.jsonl"),
        Path("manifests/line_registry.json"),
    ):
        source = main_runtime / relative_path
        target = sandbox_root / relative_path
        if source.exists():
            shutil.copy2(source, target)


def _load_line_rows(runtime_root: Path, line_name: str) -> list[dict]:
    log_path = runtime_root / "logs" / "reread_observation_log.jsonl"
    rows = []
    for raw_line in log_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        row = json.loads(line)
        if row.get("line_name") == line_name:
            rows.append(row)
    return rows


def _load_latest_structured_doc_row(runtime_root: Path, line_name: str) -> dict:
    rows = [
        row
        for row in _load_line_rows(runtime_root, line_name)
        if str(row.get("validation_path_id") or "") == "structured_doc_routing"
    ]
    if not rows:
        raise RuntimeError(f"no structured_doc_routing row found for {line_name}")
    return rows[-1]


def _select_primary_recovery_rows(runtime_root: Path, line_name: str, limit: int = 5) -> list[dict]:
    candidates = []
    seen_materials: set[str] = set()
    seen_runs: set[str] = set()
    for row in reversed(_load_line_rows(runtime_root, line_name)):
        origin = str(row.get("evidence_origin_kind") or "")
        if origin not in {"primary_raw", "primary_structured"}:
            continue
        material_anchor_id = str(row.get("material_anchor_id") or "").strip()
        if not material_anchor_id:
            continue
        if material_anchor_id in seen_materials:
            continue
        run_id = str(row.get("run_id") or "").strip()
        if run_id and run_id in seen_runs:
            continue
        seen_materials.add(material_anchor_id)
        if run_id:
            seen_runs.add(run_id)
        candidates.append(row)
        if len(candidates) >= limit:
            break
    return list(reversed(candidates))


def _observation_from_row(row: dict, slug: str, suffix: str, evidence_suffix: str) -> RereadObservation:
    return RereadObservation(
        run_id=f"{row.get('run_id') or row.get('validation_path_id') or 'row'}_{suffix}_{slug}",
        asset_or_surface=str(row.get("asset_or_surface") or ""),
        view_type=str(row.get("view_type") or ""),
        line_name=str(row.get("line_name") or ""),
        evidence=f"{row.get('evidence') or ''} {evidence_suffix}",
        grounding_type=str(row.get("grounding_type") or "direct"),
        support_points=[str(item) for item in (row.get("support_points") or [])],
        weakness_points=[str(item) for item in (row.get("weakness_points") or [])],
        contradiction_points=[str(item) for item in (row.get("contradiction_points") or [])],
        caution_points=[str(item) for item in (row.get("caution_points") or [])],
        next_probe_surface=str(row.get("next_probe_surface") or ""),
        thickness_before=str(row.get("thickness_before") or "thin"),
        thickness_after=str(row.get("thickness_after") or "thin"),
        observed_at=datetime.now(timezone.utc).isoformat(),
        source_kind=str(row.get("source_kind") or "other"),
        source_path_or_ref=str(row.get("source_path_or_ref") or ""),
        source_run_id_or_event_id=f"{row.get('source_run_id_or_event_id') or row.get('run_id') or 'event'}_{suffix}_{slug}",
        source_pointer=str(row.get("source_pointer") or ""),
        evidence_mode=str(row.get("evidence_mode") or "source_linked"),
        validation_path_id=str(row.get("validation_path_id") or ""),
        evidence_origin_kind=str(row.get("evidence_origin_kind") or "primary_structured"),
        independence_class=str(row.get("independence_class") or "primary"),
        material_anchor_id=str(row.get("material_anchor_id") or ""),
        material_anchor_kind=str(row.get("material_anchor_kind") or ""),
        material_source_path=str(row.get("material_source_path") or ""),
    )


def main(argv: list[str]) -> int:
    main_runtime = Path(argv[1]).resolve() if len(argv) > 1 else (REPO_ROOT / "runtime").resolve()
    slug = _now_slug()
    sandbox_base = Path(tempfile.gettempdir()) / "vectorfl_line_thickening_sandboxes"
    sandbox_root = (sandbox_base / f"transition_over_surface_recovery_trip_{slug}" / "runtime").resolve()
    sandbox_root.parent.mkdir(parents=True, exist_ok=True)
    _prepare_minimal_sandbox_runtime(main_runtime, sandbox_root)

    for line_name in (
        "transition_over_surface",
        "input_to_reading_organ",
        "pre_read_eye",
        "raw_return_preservation",
    ):
        refresh_line_registry_entry(sandbox_root, line_name)

    before = _line_summary(sandbox_root, "transition_over_surface")

    structured_doc_row = _load_latest_structured_doc_row(main_runtime, "transition_over_surface")
    trip_observation = _observation_from_row(
        structured_doc_row,
        slug,
        "sandbox_trip",
        "[sandbox reintroduction trip]",
    )
    trip_result = record_reread_observation(sandbox_root, trip_observation)
    refresh_line_registry_entry(sandbox_root, "transition_over_surface")
    after_trip = _line_summary(sandbox_root, "transition_over_surface")

    recovery_rows = _select_primary_recovery_rows(main_runtime, "transition_over_surface", limit=5)
    recovery_results = []
    for index, row in enumerate(recovery_rows, start=1):
        observation = _observation_from_row(
            row,
            slug,
            f"sandbox_recovery_{index}",
            "[sandbox recovery refresh]",
        )
        recovery_results.append(record_reread_observation(sandbox_root, observation))
    refresh_line_registry_entry(sandbox_root, "transition_over_surface")
    after_recovery = _line_summary(sandbox_root, "transition_over_surface")

    print(
        json.dumps(
            {
                "main_runtime": str(main_runtime),
                "sandbox_runtime": str(sandbox_root),
                "trip_method": "clone_latest_structured_doc_routing_row_into_sandbox",
                "recovery_method": "append_distinct_primary_rows_into_sandbox_until_last_derived_exits_recent_window",
                "before": before,
                "trip_source": {
                    "validation_path_id": structured_doc_row.get("validation_path_id"),
                    "run_id": structured_doc_row.get("run_id"),
                    "source_pointer": structured_doc_row.get("source_pointer"),
                },
                "trip_result": trip_result,
                "after_trip": after_trip,
                "recovery_sources": [
                    {
                        "run_id": row.get("run_id"),
                        "validation_path_id": row.get("validation_path_id"),
                        "material_anchor_id": row.get("material_anchor_id"),
                        "source_pointer": row.get("source_pointer"),
                    }
                    for row in recovery_rows
                ],
                "recovery_results": recovery_results,
                "after_recovery": after_recovery,
                "expected_loop": {
                    "before_status": "observed_but_outside_window",
                    "after_trip_status": "observed_recently",
                    "after_recovery_status": "observed_but_outside_window",
                    "expected_trigger": "derived_route_refresh",
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
