#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.lower_support_layers import (
    build_camera_support_bundles_for_split_units,
    build_content_role_tags_for_split_units,
    build_line_seed_bundles_for_split_units,
    build_support_layers_for_preprocess_comparison,
    write_support_payload,
)


OBSERVER_OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "observer_ingest_min" / "generated"


def _observer_paths(run_id: str) -> tuple[Path, Path, Path, Path, Path, Path]:
    manifest_path = OBSERVER_OUTPUT_ROOT / f"source_manifest_{run_id}.json"
    split_units_path = OBSERVER_OUTPUT_ROOT / f"split_units_{run_id}.json"
    processing_trace_path = OBSERVER_OUTPUT_ROOT / f"processing_trace_{run_id}.json"
    role_path = OBSERVER_OUTPUT_ROOT / f"content_role_tags_{run_id}.json"
    seed_path = OBSERVER_OUTPUT_ROOT / f"line_seed_bundles_{run_id}.json"
    camera_path = OBSERVER_OUTPUT_ROOT / f"camera_support_bundles_{run_id}.json"
    return manifest_path, split_units_path, processing_trace_path, role_path, seed_path, camera_path


def build_for_observer_run(run_id: str) -> dict[str, str]:
    manifest_path, split_units_path, _, role_path, seed_path, camera_path = _observer_paths(run_id)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    split_units = json.loads(split_units_path.read_text(encoding="utf-8"))
    source_ref = manifest.get("source_path") or manifest.get("input_id") or run_id
    role_tags = build_content_role_tags_for_split_units(source_ref, split_units)
    line_seeds = build_line_seed_bundles_for_split_units(source_ref, split_units, role_tags)
    camera_support_bundles = build_camera_support_bundles_for_split_units(
        source_ref,
        split_units,
        role_tags,
        line_seeds,
    )
    write_support_payload(role_path, role_tags)
    write_support_payload(seed_path, line_seeds)
    write_support_payload(camera_path, camera_support_bundles)
    return {
        "content_role_tags": str(role_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "line_seed_bundles": str(seed_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "camera_support_bundles": str(camera_path.relative_to(REPO_ROOT)).replace("\\", "/"),
    }


def build_for_preprocess_comparison(path: Path) -> dict[str, str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    support_layers = build_support_layers_for_preprocess_comparison(payload)
    role_path = path.with_name(f"{path.stem}_content_role_tags.json")
    seed_path = path.with_name(f"{path.stem}_line_seed_bundles.json")
    camera_path = path.with_name(f"{path.stem}_camera_support_bundles.json")
    write_support_payload(role_path, support_layers["content_role_tags"])
    write_support_payload(seed_path, support_layers["line_seed_bundles"])
    write_support_payload(camera_path, support_layers["camera_support_bundles"])
    return {
        "content_role_tags": str(role_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "line_seed_bundles": str(seed_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        "camera_support_bundles": str(camera_path.relative_to(REPO_ROOT)).replace("\\", "/"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--observer-run-id", default="")
    parser.add_argument("--preprocess-comparison", default="")
    args = parser.parse_args()

    if not args.observer_run_id and not args.preprocess_comparison:
        raise SystemExit("use --observer-run-id or --preprocess-comparison")

    result: dict[str, str] = {}
    if args.observer_run_id:
        result.update(build_for_observer_run(args.observer_run_id))
    if args.preprocess_comparison:
        comparison_path = Path(args.preprocess_comparison)
        if not comparison_path.is_absolute():
            comparison_path = (REPO_ROOT / comparison_path).resolve()
        result.update(build_for_preprocess_comparison(comparison_path))

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
