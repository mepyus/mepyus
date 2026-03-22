#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input_space import register_possibility_bridges
from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata


def _local_space_payload(service: FormationService, local_space_id: str) -> tuple[list[str], list[str]]:
    local_space = service.local_spaces.get(local_space_id) or {}
    material_ids: list[str] = []
    trace_ids: list[str] = []
    for cell_id in local_space.get("cell_refs", []):
        cell = service.cells.get(str(cell_id)) or {}
        material_ids.extend(str(row) for row in cell.get("material_refs", []))
        trace_ids.extend(str(row) for row in cell.get("trace_refs", []))
    return sorted(set(material_ids)), sorted(set(trace_ids))


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    service = FormationService(runtime_root)
    updates: list[dict[str, object]] = []
    touched_spaces: set[str] = set()
    for local_space in service.local_spaces.read_all():
        local_space_id = str(local_space.get("local_space_id", "")).strip()
        if not local_space_id:
            continue
        material_ids, trace_ids = _local_space_payload(service, local_space_id)
        if not material_ids or not trace_ids:
            continue
        rows = register_possibility_bridges(
            service,
            new_local_space_id=local_space_id,
            material_ids=material_ids,
            trace_ids=trace_ids,
        )
        if rows:
            updates.extend(rows)
            touched_spaces.add(local_space_id)
            for row in rows:
                touched_spaces.add(str(row.get("to_local_space_id", "")))
    synced = []
    for local_space_id in sorted(space for space in touched_spaces if space):
        payload = sync_local_space_anchor_metadata(runtime_root, local_space_id)
        if payload:
            synced.append(payload)
    print(json.dumps({"updates": updates, "synced_local_spaces": synced}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
