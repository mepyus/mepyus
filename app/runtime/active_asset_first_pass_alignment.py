from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from app.fragment.schema import FragmentRecord, ProvenanceEntry
from app.fragment.store import FragmentStore
from app.input_layer.anchorizer import enrich_fragment_with_anchors
from app.input_layer.source_locator import enrich_fragment_with_source_location
from app.runtime.segment_to_source_context_extractor import (
    extract_object_source_context,
    extract_segment_source_context,
)


DEFAULT_ROW_SCENE_FLOW = {
    "packet_texture": ("explanation", "expand"),
    "grounding_status": ("comparison", "contract"),
    "emergence_status": ("evidence", "expand"),
    "carryover_risk": ("comparison", "tension"),
    "maturation_state": ("explanation", "bridge"),
    "traceability_status": ("evidence", "bridge"),
}


def assess_active_asset_canonical_onboarding(*, raw_asset: Dict[str, Any]) -> Dict[str, Any]:
    asset_id = str(raw_asset.get("id") or "").strip()
    source_pointer = _find_source_pointer(raw_asset.get("evidenceRefs") or [])
    rows = [row for row in (raw_asset.get("canonicalStateRows") or []) if isinstance(row, dict)]
    missing: List[str] = []
    if not asset_id:
        missing.append("asset_id")
    if not source_pointer:
        missing.append("source_pointer")
    if not rows:
        missing.append("canonical_rows")
    return {
        "asset_id": asset_id,
        "source_pointer": source_pointer,
        "row_keys": [str(row.get("key") or "").strip() for row in rows if str(row.get("key") or "").strip()],
        "ready_for_fragment_generation": not missing,
        "missing": missing,
    }


def ensure_active_asset_first_pass_fragments(runtime_root: Path, *, raw_asset: Dict[str, Any]) -> List[str]:
    assessment = assess_active_asset_canonical_onboarding(raw_asset=raw_asset)
    if not assessment.get("ready_for_fragment_generation"):
        return []
    asset_id = str(assessment.get("asset_id") or "").strip()
    source_pointer = str(assessment.get("source_pointer") or "").strip()
    rows = [row for row in (raw_asset.get("canonicalStateRows") or []) if isinstance(row, dict)]
    store = FragmentStore(runtime_root)
    existing = {
        fragment.fragment_id
        for fragment in store.read_all()
        if str(fragment.source_path or "") == source_pointer and str(fragment.source_id or "").startswith(f"src_active_{asset_id}")
    }
    created: List[str] = []

    object_fragment = _build_object_fragment(runtime_root=runtime_root, asset_id=asset_id, source_pointer=source_pointer)
    if object_fragment and object_fragment.fragment_id not in existing:
        store.put(object_fragment)
        created.append(object_fragment.fragment_id)

    for row in rows:
        row_key = str(row.get("key") or "").strip()
        if not row_key:
            continue
        fragment = _build_row_fragment(
            runtime_root=runtime_root,
            asset_id=asset_id,
            source_pointer=source_pointer,
            row_key=row_key,
        )
        if fragment is None or fragment.fragment_id in existing:
            continue
        store.put(fragment)
        created.append(fragment.fragment_id)
    return created


def _build_object_fragment(*, runtime_root: Path, asset_id: str, source_pointer: str) -> FragmentRecord | None:
    try:
        context = extract_object_source_context(source_pointer=source_pointer)
    except Exception:
        return None
    text = str(context.get("paragraph_text") or "").strip()
    if not text:
        return None
    fragment = FragmentRecord(
        fragment_id=f"frag_active_{asset_id}_object",
        source_id=f"src_active_{asset_id}",
        source_type="dialogue_asset",
        source_path=source_pointer,
        raw_text=text,
        unit_scale="paragraph",
        scene="explanation",
        flow="expand",
        provenance_log=[
            ProvenanceEntry(
                step="active_asset_alignment",
                note="generated active asset object first-pass fragment",
                payload={"asset_id": asset_id, "kind": "object"},
            )
        ],
        metadata={"alignment_kind": "active_asset_object"},
    )
    fragment = enrich_fragment_with_anchors(fragment)
    return enrich_fragment_with_source_location(runtime_root, fragment)


def _build_row_fragment(
    *,
    runtime_root: Path,
    asset_id: str,
    source_pointer: str,
    row_key: str,
) -> FragmentRecord | None:
    try:
        context = extract_segment_source_context(
            asset_id=asset_id,
            state_row_key=row_key,
            source_pointer=source_pointer,
        )
    except Exception:
        return None
    text = str(context.get("paragraph_text") or "").strip()
    if not text:
        return None
    scene, flow = DEFAULT_ROW_SCENE_FLOW.get(row_key, ("explanation", "expand"))
    fragment = FragmentRecord(
        fragment_id=f"frag_active_{asset_id}_{row_key}",
        source_id=f"src_active_{asset_id}",
        source_type="dialogue_asset",
        source_path=source_pointer,
        raw_text=text,
        unit_scale="paragraph",
        scene=scene,
        flow=flow,
        provenance_log=[
            ProvenanceEntry(
                step="active_asset_alignment",
                note="generated active asset row first-pass fragment",
                payload={"asset_id": asset_id, "row_key": row_key},
            )
        ],
        metadata={"alignment_kind": "active_asset_row", "row_key": row_key},
    )
    fragment = enrich_fragment_with_anchors(fragment)
    return enrich_fragment_with_source_location(runtime_root, fragment)


def _find_source_pointer(evidence_refs: List[Dict[str, Any]]) -> str:
    for ref in evidence_refs:
        if not isinstance(ref, dict):
            continue
        if str(ref.get("kind") or "") == "source_file":
            return str(ref.get("id") or "").strip()
    return ""
