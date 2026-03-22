#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Set


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.live_input_space import enrich_bridge_trace
from app.core.runtime.runtime_observer_baseline import (
    apply_observer_baseline_to_metadata,
    build_material_observer_baseline,
)
from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    service = FormationService(runtime_root)
    material_rows = _commonize_materials(service)
    local_space_rows = _sync_target_local_spaces(runtime_root, service, material_rows["touched_local_spaces"])
    bridge_rows = _enrich_target_bridges(service, local_space_rows["touched_local_spaces"])
    payload = {
        "runtime_root": str(runtime_root),
        "material_updates": material_rows["updates"],
        "local_space_updates": local_space_rows["updates"],
        "bridge_updates": bridge_rows,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def _commonize_materials(service: FormationService) -> Dict[str, object]:
    updates: List[Dict[str, object]] = []
    touched_local_spaces: Set[str] = set()
    for material in service.materials.read_all():
        source_ref = str(material.get("source_ref", "")).strip()
        if not _is_target_source(source_ref):
            continue
        metadata = dict(material.get("metadata", {}))
        trace = dict(metadata.get("observer_or_ambiguity_trace", {}) or {})
        if trace and trace.get("generation_path") and ("unavailable_reason" in trace):
            continue
        raw_payload = str(material.get("raw_payload", "")).strip()
        if not raw_payload:
            metadata["observer_or_ambiguity_trace"] = {
                "available": False,
                "generation_path": "runtime_commonization",
                "profiles": {},
                "items": [],
                "merged": {
                    "scene": str(metadata.get("scene", "")),
                    "role": "",
                    "ambiguity": None,
                    "confidence": None,
                    "signals": [],
                },
                "unavailable_reason": "raw_payload_missing",
                "note": "observer baseline unavailable during runtime commonization",
            }
        else:
            trace = build_material_observer_baseline(
                raw_payload,
                generation_path="runtime_commonization",
            )
            metadata = apply_observer_baseline_to_metadata(metadata, trace)
        material["metadata"] = metadata
        service.materials.put(str(material.get("material_id", "")), material)
        updates.append(
            {
                "material_id": str(material.get("material_id", "")),
                "source_ref": source_ref,
                "available": bool(metadata.get("observer_or_ambiguity_trace", {}).get("available", False)),
                "generation_path": str(metadata.get("observer_or_ambiguity_trace", {}).get("generation_path", "")),
            }
        )
    for local_space in service.local_spaces.read_all():
        local_space_id = str(local_space.get("local_space_id", "")).strip()
        if not local_space_id:
            continue
        for material_id in _local_space_material_ids(service, local_space_id):
            material = service.materials.get(material_id) or {}
            if _is_target_source(str(material.get("source_ref", "")).strip()):
                touched_local_spaces.add(local_space_id)
                break
    return {"updates": updates, "touched_local_spaces": touched_local_spaces}


def _sync_target_local_spaces(runtime_root: Path, service: FormationService, touched_local_spaces: Set[str]) -> Dict[str, object]:
    updates: List[Dict[str, object]] = []
    for local_space_id in sorted(touched_local_spaces):
        payload = sync_local_space_anchor_metadata(runtime_root, local_space_id)
        if payload:
            updates.append(payload)
    return {"updates": updates, "touched_local_spaces": touched_local_spaces}


def _enrich_target_bridges(service: FormationService, touched_local_spaces: Set[str]) -> List[Dict[str, object]]:
    updates: List[Dict[str, object]] = []
    for bridge in service.bridges.read_all():
        bridge_id = str(bridge.get("bridge_id", "")).strip()
        if not bridge_id:
            continue
        left = str(bridge.get("from_local_space_id", "")).strip()
        right = str(bridge.get("to_local_space_id", "")).strip()
        if left not in touched_local_spaces and right not in touched_local_spaces:
            continue
        payload = enrich_bridge_trace(service, bridge_id)
        if not payload:
            continue
        observer = dict(payload.get("observer_contribution", {}) or {})
        updates.append(
            {
                "bridge_id": bridge_id,
                "bridge_reason_kind": str(payload.get("bridge_reason_kind", "")),
                "observer_available": bool(observer.get("available", False)),
                "rejected_overlap_count": len(list(payload.get("rejected_overlap_anchors", []) or [])),
            }
        )
    return updates


def _local_space_material_ids(service: FormationService, local_space_id: str) -> Set[str]:
    local_space = service.local_spaces.get(local_space_id) or {}
    material_ids: Set[str] = set()
    for cell_id in local_space.get("cell_refs", []):
        cell = service.cells.get(str(cell_id)) or {}
        for material_id in cell.get("material_refs", []):
            material_ids.add(str(material_id))
    return material_ids


def _is_target_source(source_ref: str) -> bool:
    return (
        source_ref.startswith("processor_compare/")
        or source_ref.startswith("manual/")
        or source_ref.startswith("engine_phase1_")
        or source_ref.startswith("operator_phase1_")
    )


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
