#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.fragment.schema import FragmentAnchor, FragmentRecord, PageRef, ProvenanceEntry, SourceRange
from app.fragment.store import FragmentStore
from app.fragment.projector import project_fragment_to_material
from app.input_layer.anchorizer import enrich_fragment_with_anchors
from app.input_layer.source_locator import enrich_fragment_with_source_location
from app.measurement import (
    MeasurementRecord,
    MeasurementStore,
    build_ambient_anchor_probe,
    load_anchor_seed_bank,
)
from app.work.processor_compare.anchor_engine import extract_promoted_anchors_for_text
from app.work.processor_compare.observer_engine import run_internal_observers


def _usage() -> int:
    print("usage: ingest_fragments.py <runtime_root> <fragments.json> [--project]")
    return 1


def _utc_now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _load_fragments(path: Path) -> List[FragmentRecord]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload if isinstance(payload, list) else payload.get("fragments", [])
    fragments: List[FragmentRecord] = []
    for row in rows:
        source_range = SourceRange(**row.get("source_range", {}))
        page_ref = PageRef(**row.get("page_ref", {}))
        anchor = row.get("anchor")
        provenance_rows = row.get("provenance_log", [])
        fragments.append(
            FragmentRecord(
                fragment_id=row["fragment_id"],
                source_id=row["source_id"],
                source_type=row["source_type"],
                source_path=row["source_path"],
                raw_text=row["raw_text"],
                unit_scale=row["unit_scale"],
                created_at=row.get("created_at", FragmentRecord.__dataclass_fields__["created_at"].default_factory()),
                source_range=source_range,
                page_ref=page_ref,
                paragraph_index=row.get("paragraph_index"),
                anchor=_load_anchor(anchor) if anchor else None,
                anchors=[_load_anchor(entry) for entry in row.get("anchors", [])],
                D=float(row.get("D", 0.5)),
                I=float(row.get("I", 0.5)),
                S=float(row.get("S", 0.5)),
                scene=row.get("scene", "unknown"),
                flow=row.get("flow", "unknown"),
                time=row.get("time", ""),
                confidence=row.get("confidence", "mid"),
                provenance_log=[ProvenanceEntry(**entry) for entry in provenance_rows],
                metadata=row.get("metadata", {}),
            )
        )
    return fragments


def _load_anchor(payload: Dict[str, object]) -> FragmentAnchor:
    row = dict(payload)
    if "key" not in row:
        row["key"] = str(row.get("value", ""))
    if "canonical_key" not in row:
        row["canonical_key"] = row["key"]
    if "evidence_text" not in row:
        row["evidence_text"] = str(row.get("value", ""))
    if "confidence" not in row:
        row["confidence"] = 0.0
    if "origin" not in row:
        row["origin"] = "manual"
    if "aliases" not in row:
        row["aliases"] = []
    if "status" not in row:
        row["status"] = "active"
    return FragmentAnchor(**row)


def main(argv: List[str]) -> int:
    if len(argv) < 3:
        return _usage()

    runtime_root = Path(argv[1]).resolve()
    input_path = Path(argv[2]).resolve()
    project_to_material = "--project" in argv[3:]
    ingest_batch_id = _build_ingest_batch_id(input_path)
    ingest_session_id = f"ingest_session:{_utc_now_compact()}"

    store = FragmentStore(runtime_root)
    measurement_store = MeasurementStore(runtime_root)
    seeds = load_anchor_seed_bank(runtime_root)
    fragments = _load_fragments(input_path)
    material_ids: List[str] = []
    measurement_ids: List[str] = []
    for fragment in fragments:
        fragment = _attach_ingest_lineage(
            fragment,
            ingest_batch_id=ingest_batch_id,
            ingest_session_id=ingest_session_id,
            input_path=input_path,
        )
        enriched = enrich_fragment_with_anchors(fragment)
        enriched = _apply_canonical_anchor_engine(enriched, ingest_batch_id=ingest_batch_id)
        enriched = _append_provenance(
            enriched,
            step="anchorizer",
            note="applied anchor enrichment",
            payload={
                "anchor_count": len(enriched.anchors),
                "primary_anchor": enriched.anchor.key if enriched.anchor else "",
                "ingest_batch_id": ingest_batch_id,
            },
        )
        measurement_ids.extend(
            _store_anchor_measurements(
                measurement_store,
                enriched,
                ingest_batch_id=ingest_batch_id,
                ingest_session_id=ingest_session_id,
            )
        )

        enriched = enrich_fragment_with_source_location(runtime_root, enriched)
        enriched = _append_provenance(
            enriched,
            step="source_locator",
            note="applied source location enrichment",
            payload={
                "source_range": enriched.source_range.__dict__,
                "paragraph_index": enriched.paragraph_index,
                "page_ref": enriched.page_ref.__dict__,
                "ingest_batch_id": ingest_batch_id,
            },
        )
        enriched = _apply_internal_observer(enriched, ingest_batch_id=ingest_batch_id)
        measurement_ids.append(
            _store_source_location_measurement(
                measurement_store,
                enriched,
                ingest_batch_id=ingest_batch_id,
                ingest_session_id=ingest_session_id,
            )
        )
        measurement_ids.append(
            _store_processing_measurement(
                measurement_store,
                enriched,
                ingest_batch_id=ingest_batch_id,
                ingest_session_id=ingest_session_id,
            )
        )
        ambient_probe = build_ambient_anchor_probe(
            enriched,
            seeds=seeds,
            ingest_batch_id=ingest_batch_id,
            ingest_session_id=ingest_session_id,
            seed_bank_version="seed_bank_20260318_a",
        )
        if ambient_probe is not None:
            measurement_store.put(ambient_probe)
            measurement_ids.append(ambient_probe.measurement_id)
            enriched = _append_provenance(
                enriched,
                step="ambient_probe",
                note="attached ambient anchor probe measurement",
                payload={
                    "measurement_id": ambient_probe.measurement_id,
                    "candidate_count": (ambient_probe.value.get("summary") or {}).get("candidate_count", 0),
                    "top_handle": (ambient_probe.value.get("summary") or {}).get("top_handle", ""),
                },
            )
        if project_to_material:
            material = project_fragment_to_material(runtime_root, enriched)
            material_id = str(material.get("material_id", ""))
            if material_id:
                material_ids.append(material_id)
                metadata = dict(enriched.metadata)
                metadata["projected_material_id"] = material_id
                enriched = enriched.with_updates(metadata=metadata)
                measurement_ids.append(
                    _store_projection_measurement(
                        measurement_store,
                        enriched,
                        material_id,
                        ingest_batch_id=ingest_batch_id,
                        ingest_session_id=ingest_session_id,
                    )
                )
                enriched = _append_provenance(
                    enriched,
                    step="projector",
                    note="projected fragment to material",
                    payload={
                        "material_id": material_id,
                        "ingest_batch_id": ingest_batch_id,
                    },
                )
        store.put(enriched)

    result: Dict[str, object] = {
        "runtime_root": str(runtime_root),
        "input_path": str(input_path),
        "ingest_batch_id": ingest_batch_id,
        "ingest_session_id": ingest_session_id,
        "fragment_count": len(fragments),
        "measurement_count": len([item for item in measurement_ids if item]),
        "measurement_ids": [item for item in measurement_ids if item],
        "projected_material_count": len([item for item in material_ids if item]),
        "material_ids": [item for item in material_ids if item],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def _append_provenance(
    fragment: FragmentRecord,
    *,
    step: str,
    note: str,
    payload: Dict[str, object],
) -> FragmentRecord:
    entries = list(fragment.provenance_log)
    entries.append(ProvenanceEntry(step=step, note=note, payload=payload))
    return fragment.with_updates(provenance_log=entries)


def _apply_internal_observer(
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
) -> FragmentRecord:
    observer_payload = run_internal_observers(fragment.raw_text)
    merged = observer_payload["merged"]

    observer_anchors = [
        FragmentAnchor(
            key=f"observer.{anchor['anchor_type']}.{anchor['label']}",
            canonical_key=f"observer.{anchor['anchor_type']}.{anchor['label']}",
            label=anchor["label"],
            value=anchor["label"],
            anchor_type=anchor["anchor_type"],
            evidence_text=anchor.get("evidence_text", ""),
            confidence=float(anchor.get("score", 0.0)),
            origin="internal_observer",
            aliases=[],
            status="active",
        )
        for anchor in merged.get("anchors", [])
    ]
    anchors = _merge_fragment_anchors(fragment.anchors, observer_anchors)
    primary_anchor = anchors[0] if anchors else fragment.anchor

    metadata = dict(fragment.metadata)
    metadata["internal_observer"] = {
        "version": "v0_1",
        "ingest_batch_id": ingest_batch_id,
        "features": observer_payload["features"],
        "profiles": {
            "codex_like": observer_payload["codex_like"],
            "chatgpt_like": observer_payload["chatgpt_like"],
            "gemini_like": observer_payload["gemini_like"],
        },
        "merged": {
            "scene": merged["scene"],
            "role": merged["role"],
            "confidence": merged["confidence"],
            "ambiguity": merged["ambiguity"],
            "signals": merged.get("signals", []),
            "why_short": merged.get("why_short", ""),
            "semantic_tags": merged.get("semantic_tags", []),
            "structural_tags": merged.get("structural_tags", []),
            "evidence_text": merged.get("evidence_text", []),
        },
    }
    metadata["observer_role"] = merged["role"]
    metadata["observer_ambiguity"] = float(merged["ambiguity"])
    metadata["observer_confidence_numeric"] = float(merged["confidence"])
    metadata["observer_signals"] = list(merged.get("signals", []))

    updated = fragment.with_updates(
        anchor=primary_anchor,
        anchors=anchors,
        D=float(merged["direction"]),
        I=float(merged["intensity"]),
        S=float(merged["stability"]),
        scene=str(merged["scene"]),
        confidence=_confidence_bucket(float(merged["confidence"])),
        metadata=metadata,
    )
    return _append_provenance(
        updated,
        step="internal_observer",
        note="applied internal observer ensemble",
        payload={
            "scene": merged["scene"],
            "role": merged["role"],
            "confidence": merged["confidence"],
            "ambiguity": merged["ambiguity"],
            "signals": merged.get("signals", []),
        },
    )


def _apply_canonical_anchor_engine(
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
) -> FragmentRecord:
    promoted = extract_promoted_anchors_for_text(
        fragment.raw_text,
        doc_id=fragment.fragment_id,
        title=fragment.fragment_id,
        source_type=fragment.source_type,
    )
    if not promoted:
        return fragment

    canonical_anchors = [
        FragmentAnchor(
            key=str(row.get("canonical_key", "")),
            canonical_key=str(row.get("canonical_key", "")),
            label=str(row.get("display_label", "")),
            value=str(row.get("display_label", "")),
            anchor_type=str(row.get("anchor_type", "semantic")),
            evidence_text=str(row.get("surface_text", "")) or str(row.get("display_label", "")),
            confidence=float(row.get("strong_score", 0.0)),
            origin="canonical_anchor_engine",
            aliases=list(row.get("surface_forms", [])) if isinstance(row.get("surface_forms"), list) else [],
            status="active",
        )
        for row in promoted[:8]
        if str(row.get("canonical_key", "")).strip() and str(row.get("display_label", "")).strip()
    ]
    merged = _merge_fragment_anchors(canonical_anchors, fragment.anchors)
    metadata = dict(fragment.metadata)
    metadata["canonical_anchor_engine"] = {
        "version": "v0_1",
        "ingest_batch_id": ingest_batch_id,
        "promoted_count": len(canonical_anchors),
        "representative_keys": [anchor.canonical_key or anchor.key for anchor in canonical_anchors[:5]],
    }
    updated = fragment.with_updates(
        anchor=merged[0] if merged else fragment.anchor,
        anchors=merged,
        metadata=metadata,
    )
    return _append_provenance(
        updated,
        step="canonical_anchor_engine",
        note="applied canonical anchor normalization and promotion",
        payload={
            "promoted_count": len(canonical_anchors),
            "representative_keys": [anchor.canonical_key or anchor.key for anchor in canonical_anchors[:5]],
        },
    )


def _merge_fragment_anchors(
    existing: List[FragmentAnchor],
    observer: List[FragmentAnchor],
) -> List[FragmentAnchor]:
    merged: List[FragmentAnchor] = []
    seen = set()
    for anchor in list(existing) + list(observer):
        key = (anchor.key, anchor.anchor_type)
        if key in seen:
            continue
        seen.add(key)
        merged.append(anchor)
    return merged[:8]


def _confidence_bucket(value: float) -> str:
    if value >= 0.8:
        return "high"
    if value >= 0.55:
        return "mid"
    return "low"


def _measurement_id(fragment_id: str, measurement_type: str, column_key: str, suffix: str) -> str:
    digest = hashlib.sha1(f"{fragment_id}|{measurement_type}|{column_key}|{suffix}".encode("utf-8")).hexdigest()
    return f"msr_{digest[:16]}"


def _build_ingest_batch_id(input_path: Path) -> str:
    digest = hashlib.sha1(f"{input_path}|{_utc_now_compact()}".encode("utf-8")).hexdigest()
    return f"batch_{digest[:12]}"


def _attach_ingest_lineage(
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
    ingest_session_id: str,
    input_path: Path,
) -> FragmentRecord:
    metadata = dict(fragment.metadata)
    ingest_history = list(metadata.get("ingest_history", []))
    ingest_history.append(
        {
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
            "input_path": str(input_path),
            "recorded_at": _utc_now_compact(),
        }
    )
    metadata.update(
        {
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
            "ingest_input_path": str(input_path),
            "ingest_history": ingest_history,
        }
    )
    fragment = fragment.with_updates(metadata=metadata)
    return _append_provenance(
        fragment,
        step="ingest_batch",
        note="registered ingest batch lineage",
        payload={
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
            "input_path": str(input_path),
        },
    )


def _store_anchor_measurements(
    store: MeasurementStore,
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
    ingest_session_id: str,
) -> List[str]:
    ids: List[str] = []
    for index, anchor in enumerate(fragment.anchors):
        measurement = MeasurementRecord(
            measurement_id=_measurement_id(fragment.fragment_id, "anchor", anchor.key, f"{ingest_batch_id}:{index}"),
            fragment_id=fragment.fragment_id,
            measurement_type="anchor",
            column_key=anchor.key,
            value={
                "anchor_type": anchor.anchor_type,
                "key": anchor.key,
                "label": anchor.label,
                "value": anchor.value,
                "canonical_key": anchor.canonical_key or anchor.key,
                "aliases": anchor.aliases,
                "status": anchor.status,
            },
            basis="anchor extraction result",
            evidence_text=anchor.evidence_text,
            confidence=anchor.confidence,
            origin=anchor.origin,
            status=anchor.status,
            provisional=anchor.origin != "manual",
            related_source_path=fragment.source_path,
            metadata={
                "position": index,
                "time": fragment.time,
                "ingest_batch_id": ingest_batch_id,
                "ingest_session_id": ingest_session_id,
            },
        )
        store.put(measurement)
        ids.append(measurement.measurement_id)
    return ids


def _store_source_location_measurement(
    store: MeasurementStore,
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
    ingest_session_id: str,
) -> str:
    measurement = MeasurementRecord(
        measurement_id=_measurement_id(fragment.fragment_id, "source_location", "source_range", ingest_batch_id),
        fragment_id=fragment.fragment_id,
        measurement_type="source_location",
        column_key="source_range",
        value={
            "start": fragment.source_range.start,
            "end": fragment.source_range.end,
            "paragraph_index": fragment.paragraph_index,
            "page_index": fragment.page_ref.page_index,
            "page_label": fragment.page_ref.page_label,
        },
        basis="source locator result",
        evidence_text=fragment.raw_text[:160],
        confidence=1.0 if fragment.source_range.start is not None else 0.2,
        origin="rule",
        status="active",
        provisional=fragment.source_range.start is None,
        related_source_path=fragment.source_path,
        metadata={
            "unit_scale": fragment.unit_scale,
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
        },
    )
    store.put(measurement)
    return measurement.measurement_id


def _store_processing_measurement(
    store: MeasurementStore,
    fragment: FragmentRecord,
    *,
    ingest_batch_id: str,
    ingest_session_id: str,
) -> str:
    measurement = MeasurementRecord(
        measurement_id=_measurement_id(fragment.fragment_id, "processing_values", "axis_bundle", ingest_batch_id),
        fragment_id=fragment.fragment_id,
        measurement_type="processing_values",
        column_key="axis_bundle",
        value={
            "D": fragment.D,
            "I": fragment.I,
            "S": fragment.S,
            "scene": fragment.scene,
            "flow": fragment.flow,
            "time": fragment.time,
            "confidence": fragment.confidence,
        },
        basis="fragment processing bundle",
        evidence_text=fragment.raw_text[:160],
        confidence=0.6,
        origin="input_payload",
        status="active",
        provisional=True,
        related_source_path=fragment.source_path,
        metadata={
            "unit_scale": fragment.unit_scale,
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
        },
    )
    store.put(measurement)
    return measurement.measurement_id


def _store_projection_measurement(
    store: MeasurementStore,
    fragment: FragmentRecord,
    material_id: str,
    *,
    ingest_batch_id: str,
    ingest_session_id: str,
) -> str:
    measurement = MeasurementRecord(
        measurement_id=_measurement_id(fragment.fragment_id, "projection", "material_projection", f"{ingest_batch_id}:{material_id}"),
        fragment_id=fragment.fragment_id,
        measurement_type="projection",
        column_key="material_projection",
        value={
            "material_id": material_id,
            "scene": fragment.scene,
            "flow": fragment.flow,
            "anchor_keys": [anchor.key for anchor in fragment.anchors],
        },
        basis="fragment projected to space material",
        evidence_text=fragment.raw_text[:160],
        confidence=1.0,
        origin="system",
        status="active",
        provisional=False,
        related_source_path=fragment.source_path,
        related_material_id=material_id,
        metadata={
            "projected_material_id": material_id,
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
        },
    )
    store.put(measurement)
    return measurement.measurement_id


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
