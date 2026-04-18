from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
import json


def load_engine_state_index(runtime_root: Path) -> Dict[str, object]:
    path = runtime_root / "views" / "engine_state_latest" / "index.json"
    if not path.exists():
        return {"items": [], "schema_version": "engine_state_schema_v1"}
    return json.loads(path.read_text(encoding="utf-8"))


def load_engine_state_latest(runtime_root: Path, asset_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not asset_id:
        return None
    path = runtime_root / "views" / "engine_state_latest" / f"{asset_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def load_engine_state_items(runtime_root: Path) -> List[Dict[str, Any]]:
    latest_root = runtime_root / "views" / "engine_state_latest"
    index = load_engine_state_index(runtime_root)
    rows: List[Dict[str, Any]] = []
    for item in index.get("items", []):
        full = load_engine_state_latest(runtime_root, item.get("asset_id"))
        if full:
            rows.append(full)
    return rows
