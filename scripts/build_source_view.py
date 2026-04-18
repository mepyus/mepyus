#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.line_thickening import RereadObservation, record_reread_observation, refresh_line_registry_entry
from app.runtime.source_view import write_source_fragment_view


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the source fragment view.")
    parser.add_argument("runtime_root", nargs="?", default="runtime")
    parser.add_argument(
        "--record-line-thickening",
        action="store_true",
        help="append a bounded source-view line_thickening observation for one fragment row",
    )
    parser.add_argument(
        "--fragment-id",
        help="target one concrete fragment row when recording line_thickening",
    )
    return parser.parse_args()


def _load_current_thickness(runtime_root: Path, line_name: str) -> str:
    registry_path = runtime_root / "manifests" / "line_registry.json"
    if not registry_path.exists():
        return "thin"
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    for row in payload.get("lines", []):
        if str(row.get("line_name") or "") == line_name:
            return str(row.get("thickness_level") or "thin")
    return "thin"


def _select_fragment_row(payload: dict, fragment_id: str | None) -> dict | None:
    candidates: list[dict] = []
    for source in payload.get("sources", []):
        source_path = str(source.get("source_path") or "").strip()
        for row in source.get("fragments", []):
            if fragment_id and str(row.get("fragment_id") or "").strip() != fragment_id:
                continue
            source_range = row.get("source_range") or {}
            if source_range.get("start") is None:
                continue
            if not (row.get("related_cross_source") or []):
                continue
            candidates.append(
                {
                    "source_path": source_path,
                    "row": row,
                }
            )
    if not candidates:
        return None
    return candidates[0]


def _record_line_thickening(runtime_root: Path, json_path: Path, fragment_id: str | None) -> dict | None:
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    selected = _select_fragment_row(payload, fragment_id)
    if selected is None:
        return None

    row = selected["row"]
    source_path = str(selected["source_path"] or "").strip()
    source_range = row.get("source_range") or {}
    paragraph_index = row.get("paragraph_index")
    transition_count = len(row.get("related_cross_source") or [])
    fragment_id_value = str(row.get("fragment_id") or "").strip()
    line_name = "transition_over_surface"
    thickness_before = _load_current_thickness(runtime_root, line_name)
    pointer = (
        f"runtime/reports/source_fragment_view.json#fragment_id={fragment_id_value};"
        f"source_range={source_range.get('start')}-{source_range.get('end')};"
        f"paragraph_index={paragraph_index}"
    )
    observation = RereadObservation(
        run_id=f"source_fragment_view:{fragment_id_value}",
        asset_or_surface=source_path or fragment_id_value,
        view_type="source_fragment_view",
        line_name=line_name,
        evidence=(
            f"source view row {fragment_id_value} keeps source_range and {transition_count} cross-source related fragments "
            f"in one source-sorted state surface"
        ),
        grounding_type="fallback",
        support_points=[
            f"source_view_fragment={fragment_id_value}",
            f"source_range={source_range.get('start')}-{source_range.get('end')}",
            f"related_cross_source={transition_count}",
        ],
        weakness_points=[
            "state-surface reread still depends on stored fragment rows",
        ],
        caution_points=[
            "single source-view route observation only",
            "primary structured row, not a raw-direct reread span",
        ],
        next_probe_surface=pointer,
        thickness_before=thickness_before,
        thickness_after=thickness_before,
        observed_at=_now_iso(),
        source_kind="state_surface",
        source_path_or_ref=source_path,
        source_run_id_or_event_id=fragment_id_value,
        source_pointer=pointer,
        evidence_mode="source_linked",
        validation_path_id="source_fragment_view",
    )
    return record_reread_observation(runtime_root, observation)


def main() -> int:
    args = _parse_args()
    runtime_root = Path(args.runtime_root)
    paths = write_source_fragment_view(runtime_root.resolve())
    print(paths["json_path"])
    print(paths["html_path"])
    if args.record_line_thickening:
        result = _record_line_thickening(runtime_root.resolve(), paths["json_path"], args.fragment_id)
        if result is None:
            print("line_thickening: no pointer-bearing source-view row matched")
        else:
            if result.get("duplicate"):
                refreshed = refresh_line_registry_entry(runtime_root.resolve(), "transition_over_surface")
                if refreshed is not None:
                    result["registry_entry"] = refreshed
            print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
