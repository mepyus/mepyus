#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Sequence, Set

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.runtime.inputter import DustInput
from app.core.runtime.labeler import label_dust_input
from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    source_refs = argv[2:] if len(argv) > 2 else [
        "processor_compare/doc_004.txt",
        "processor_compare/doc_005.txt",
        "processor_compare/doc_006.txt",
    ]
    payload = refine_imported_processing_profiles(runtime_root, source_refs=source_refs)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def refine_imported_processing_profiles(runtime_root: Path, *, source_refs: Sequence[str]) -> Dict[str, object]:
    service = FormationService(runtime_root)
    target_refs = set(source_refs)
    updated: List[Dict[str, object]] = []
    touched_material_ids: Set[str] = set()
    for path in (runtime_root / "core" / "materials").glob("*.json"):
        try:
            material = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        source_ref = str(material.get("source_ref", "")).strip()
        if source_ref not in target_refs:
            continue
        metadata = dict(material.get("metadata", {}) or {})
        labeled = _relabel_material(material, metadata)
        before = (
            float(metadata.get("D", 0.5) or 0.5),
            float(metadata.get("I", 0.5) or 0.5),
            float(metadata.get("S", 0.5) or 0.5),
            str(metadata.get("scene", "")).strip(),
            str(metadata.get("flow", "")).strip(),
        )
        after = (labeled.D, labeled.I, labeled.S, labeled.scene, labeled.flow)
        if before == after:
            continue
        metadata.update(
            {
                "D": labeled.D,
                "I": labeled.I,
                "S": labeled.S,
                "scene": labeled.scene,
                "flow": labeled.flow,
                "processing_values": {
                    "D": labeled.D,
                    "I": labeled.I,
                    "S": labeled.S,
                    "scene": labeled.scene,
                    "flow": labeled.flow,
                },
            }
        )
        material["metadata"] = metadata
        service.materials.put(str(material.get("material_id", "")), material)
        touched_material_ids.add(str(material.get("material_id", "")))
        updated.append(
            {
                "material_id": str(material.get("material_id", "")),
                "source_ref": source_ref,
                "before": {
                    "D": before[0],
                    "I": before[1],
                    "S": before[2],
                    "scene": before[3],
                    "flow": before[4],
                },
                "after": {
                    "D": after[0],
                    "I": after[1],
                    "S": after[2],
                    "scene": after[3],
                    "flow": after[4],
                },
            }
        )
    return {
        "updated_material_count": len(updated),
        "updated_materials": updated[:50],
        "synced_local_spaces": _sync_touched_local_spaces(runtime_root, touched_material_ids),
    }


def _relabel_material(material: Dict[str, object], metadata: Dict[str, object]):
    dust = DustInput(
        dust_id=str(metadata.get("dust_input_id", "")).strip() or str(material.get("material_id", "")),
        origin_id=str(metadata.get("source_origin_id", "")).strip() or str(material.get("material_id", "")),
        source_type=str(material.get("source_type", "")).strip() or "text",
        source_ref=str(material.get("source_ref", "")).strip() or None,
        text=str(material.get("raw_payload", "")).strip(),
        source_path=str(material.get("source_ref", "")).strip() or None,
        source_span={"start": None, "end": None},
        siblings=tuple((metadata.get("transformable_handles", {}) or {}).get("sibling_ids", []) or []),
        created_at=str(material.get("created_at", "")).strip() or str(metadata.get("time_in", "")).strip(),
    )
    return label_dust_input(dust)


def _sync_touched_local_spaces(runtime_root: Path, material_ids: Set[str]) -> List[str]:
    if not material_ids:
        return []
    service = FormationService(runtime_root)
    touched_cells: Set[str] = set()
    for cell in service.cells.read_all():
        refs = {str(row) for row in cell.get("material_refs", [])}
        if refs & material_ids:
            touched_cells.add(str(cell.get("cell_id", "")))
    touched_spaces: List[str] = []
    for local_space in service.local_spaces.read_all():
        cell_refs = {str(row) for row in local_space.get("cell_refs", [])}
        if cell_refs & touched_cells:
            local_space_id = str(local_space.get("local_space_id", ""))
            sync_local_space_anchor_metadata(runtime_root, local_space_id)
            touched_spaces.append(local_space_id)
    return touched_spaces


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
