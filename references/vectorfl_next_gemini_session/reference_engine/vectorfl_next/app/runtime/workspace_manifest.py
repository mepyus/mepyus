from pathlib import Path
from typing import Dict, List

from app.runtime.bootstrap import find_legacy_runtime_directories
from app.runtime.observer import build_reactive_space_observation


CORE_DIRECTORIES = {
    "materials": "core/materials",
    "traces": "core/traces",
    "pressure_profiles": "core/pressure_profiles",
    "point_seeds": "core/point_seeds",
    "space_cells": "core/space_cells",
    "local_spaces": "core/local_spaces",
    "bridge_traces": "core/bridge_traces",
}


MANIFEST_DIRECTORIES = {
    "reactive_spaces": "manifests/reactive_spaces",
    "reactive_cells": "manifests/reactive_cells",
    "bridges": "manifests/bridges",
}


def build_workspace_manifest(runtime_root: Path) -> Dict[str, object]:
    core_counts = {
        name: _count_json_files(runtime_root / relative_path)
        for name, relative_path in CORE_DIRECTORIES.items()
    }
    manifest_counts = {
        name: _count_json_files(runtime_root / relative_path)
        for name, relative_path in MANIFEST_DIRECTORIES.items()
    }
    legacy_paths = [str(path.relative_to(runtime_root)) for path in find_legacy_runtime_directories(runtime_root)]
    reactive_observation = build_reactive_space_observation(runtime_root)
    return {
        "manifest_id": "workspace_manifest",
        "runtime_root": str(runtime_root),
        "core_counts": core_counts,
        "manifest_counts": manifest_counts,
        "legacy_paths": legacy_paths,
        "coexistence_status": _derive_coexistence_status(core_counts, legacy_paths),
        "process_summary": reactive_observation["process_summary"],
        "local_space_maturation_signals": reactive_observation["local_space_maturation_signals"],
        "bridge_maturation_signals": reactive_observation["bridge_maturation_signals"],
    }


def write_workspace_manifest(runtime_root: Path) -> Path:
    import json

    manifest = build_workspace_manifest(runtime_root)
    manifest_path = runtime_root / "manifests" / "workspace_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return manifest_path


def _count_json_files(path: Path) -> int:
    if not path.exists():
        return 0
    return len(list(path.glob("*.json")))


def _derive_coexistence_status(core_counts: Dict[str, int], legacy_paths: List[str]) -> str:
    core_total = sum(core_counts.values())
    if core_total == 0 and legacy_paths:
        return "legacy_only"
    if core_total > 0 and legacy_paths:
        return "hybrid"
    if core_total > 0:
        return "core_only"
    return "empty"
