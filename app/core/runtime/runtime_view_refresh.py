from __future__ import annotations

from pathlib import Path
from typing import Dict

from app.core.runtime.region_atlas import write_region_atlas_view
from app.core.runtime.terrain_map import write_terrain_map_view


def refresh_runtime_views(runtime_root: Path) -> Dict[str, Dict[str, str]]:
    atlas_paths = write_region_atlas_view(runtime_root)
    terrain_paths = write_terrain_map_view(runtime_root)
    return {
        "atlas_paths": {key: str(value) for key, value in atlas_paths.items()},
        "terrain_paths": {key: str(value) for key, value in terrain_paths.items()},
    }
