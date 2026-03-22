from pathlib import Path
from typing import Iterable, List


RUNTIME_DIRECTORIES = (
    "core/materials",
    "core/traces",
    "core/pressure_profiles",
    "core/point_seeds",
    "core/space_cells",
    "core/local_spaces",
    "core/bridge_traces",
    "events",
    "manifests/reactive_spaces",
    "manifests/reactive_cells",
    "manifests/bridges",
    "reports",
    "tmp",
)


LEGACY_DIRECTORIES = (
    "bridges/manifests",
    "bridges/traces",
    "events/cells",
    "events/local_spaces",
    "events/seeds",
    "spaces/adjacent_candidates",
    "spaces/reference_center",
)


def bootstrap_runtime_layout(runtime_root: Path) -> List[Path]:
    created: List[Path] = []
    for relative_path in RUNTIME_DIRECTORIES:
        path = runtime_root / relative_path
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return created


def find_legacy_runtime_directories(runtime_root: Path) -> List[Path]:
    legacy_paths: List[Path] = []
    for relative_path in LEGACY_DIRECTORIES:
        path = runtime_root / relative_path
        if path.exists():
            legacy_paths.append(path)
    return legacy_paths
