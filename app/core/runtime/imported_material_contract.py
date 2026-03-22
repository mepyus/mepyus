from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Sequence, Set
import json

from app.core.formation_service import FormationService
from app.core.runtime.local_ref_handle_translation import build_local_ref_translated_handles
from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata


def recover_imported_material_contract(runtime_root: Path, *, source_refs: Sequence[str] | None = None) -> Dict[str, object]:
    service = FormationService(runtime_root)
    material_dir = runtime_root / "core" / "materials"
    target_source_refs = set(source_refs or [])
    grouped: Dict[str, List[Dict[str, object]]] = {}
    for path in material_dir.glob("*.json"):
        try:
            material = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        source_ref = str(material.get("source_ref", "")).strip()
        if not source_ref.startswith("processor_compare/"):
            continue
        if target_source_refs and source_ref not in target_source_refs:
            continue
        grouped.setdefault(source_ref, []).append(material)

    touched_material_ids: Set[str] = set()
    updates: List[Dict[str, object]] = []
    for source_ref, rows in grouped.items():
        sibling_map = _build_sibling_map(rows)
        for material in rows:
            metadata = dict(material.get("metadata", {}) or {})
            changed = False
            if "anchor_bundle" not in metadata:
                metadata["anchor_bundle"] = _build_anchor_bundle(metadata)
                changed = True
            if "processing_values" not in metadata:
                metadata["processing_values"] = _build_processing_values(metadata)
                changed = True
            if "transformable_handles" not in metadata:
                metadata["transformable_handles"] = _build_transformable_handles(
                    material,
                    metadata,
                    sibling_map.get(str(metadata.get("dust_input_id", "")).strip(), []),
                )
                changed = True
            translated_handles = build_local_ref_translated_handles(metadata)
            if metadata.get("translated_handles") != translated_handles:
                metadata["translated_handles"] = translated_handles
                changed = True
            if "dropped_weak_anchors" not in metadata:
                metadata["dropped_weak_anchors"] = []
                changed = True
            if changed:
                material["metadata"] = metadata
                service.materials.put(str(material.get("material_id", "")), material)
                touched_material_ids.add(str(material.get("material_id", "")))
                updates.append(
                    {
                        "material_id": str(material.get("material_id", "")),
                        "source_ref": source_ref,
                    }
                )

    touched_local_spaces = _sync_touched_local_spaces(runtime_root, touched_material_ids)
    return {
        "updated_material_count": len(updates),
        "updated_materials": updates[:50],
        "synced_local_spaces": touched_local_spaces,
    }


def _build_anchor_bundle(metadata: Dict[str, object]) -> Dict[str, object]:
    anchors = list(metadata.get("anchors", []) or [])
    representative = []
    supporting = []
    for anchor in anchors[:8]:
        label = str(anchor.get("value", "")).strip()
        anchor_type = str(anchor.get("type", "semantic")).strip() or "semantic"
        canonical_key = str(anchor.get("canonical_key", "") or anchor.get("key", "")).strip()
        if not label:
            continue
        if not canonical_key:
            canonical_key = label.lower().replace(" ", "_")
        row = {
            "canonical_key": canonical_key,
            "display_label": label,
            "anchor_type": anchor_type,
        }
        if len(representative) < 4:
            representative.append(row)
        else:
            supporting.append(label)
    return {
        "representative_anchors": representative,
        "supporting_anchors": supporting[:4],
        "promoted_anchor_count": len(anchors),
        "dropped_weak_count": len(list(metadata.get("dropped_weak_anchors", []) or [])),
        "convergence_source": "imported_material_contract_recovery",
    }


def _build_processing_values(metadata: Dict[str, object]) -> Dict[str, object]:
    return {
        "D": float(metadata.get("D", 0.5)),
        "I": float(metadata.get("I", 0.5)),
        "S": float(metadata.get("S", 0.5)),
        "scene": str(metadata.get("scene", "")).strip(),
        "flow": str(metadata.get("flow", "")).strip(),
    }


def _build_transformable_handles(
    material: Dict[str, object],
    metadata: Dict[str, object],
    sibling_ids: Sequence[str],
) -> Dict[str, object]:
    source_ref = str(material.get("source_ref", "")).strip()
    dust_input_id = str(metadata.get("dust_input_id", "")).strip()
    source_origin_id = str(metadata.get("source_origin_id", "")).strip()
    short_label = str(metadata.get("short_label", "")).strip() or str(material.get("raw_payload", "")).strip()[:80]
    local_ref = f"{source_ref}::{dust_input_id}" if source_ref and dust_input_id else source_ref
    return {
        "dust_input_id": dust_input_id,
        "source_origin_id": source_origin_id,
        "source_ref": source_ref,
        "source_local_ref": local_ref,
        "short_label": short_label,
        "sibling_ids": list(sibling_ids)[:24],
    }


def _build_sibling_map(rows: Sequence[Dict[str, object]]) -> Dict[str, List[str]]:
    dust_ids = [str((row.get("metadata", {}) or {}).get("dust_input_id", "")).strip() for row in rows]
    dust_ids = [row for row in dust_ids if row]
    mapping: Dict[str, List[str]] = {}
    for dust_id in dust_ids:
        mapping[dust_id] = [row for row in dust_ids if row != dust_id]
    return mapping


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
