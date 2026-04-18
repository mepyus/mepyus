from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from app.core.events.event_append_guard import load_jsonl_with_tail_recovery


def load_engine_state_history(runtime_root: Path, asset_id: Optional[str]) -> List[Dict[str, Any]]:
    if not asset_id:
        return []
    path = runtime_root / "state" / "engine_state_history" / f"{asset_id}.jsonl"
    rows, _recovered = load_jsonl_with_tail_recovery(path)
    return rows


def load_engine_state_update_event(runtime_root: Path, asset_id: Optional[str]) -> Optional[Dict[str, Any]]:
    if not asset_id:
        return None
    path = runtime_root / "views" / "engine_state_update_events" / f"{asset_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
