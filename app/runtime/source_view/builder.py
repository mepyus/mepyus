from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Dict, List
import json

from app.fragment.store import FragmentStore
from app.measurement import MeasurementStore
from app.runtime.file_store import JsonDirectoryStore
from app.runtime.operator_ui_state import compact_payload
from app.runtime.source_view.render import render_source_fragment_html


def build_source_fragment_view_data(runtime_root: Path) -> Dict[str, object]:
    store = FragmentStore(runtime_root)
    measurement_store = MeasurementStore(runtime_root)
    material_store = JsonDirectoryStore(runtime_root / "core" / "materials")
    fragments = store.read_all()
    materials = material_store.read_all()
    measurement_records = measurement_store.read_all()
    measurements_by_fragment = _group_measurements_by_fragment(measurement_records)
    connection_index = _build_connection_observation_index(measurement_records)
    related_by_fragment = _build_related_fragment_index(fragments, connection_index)
    grouped: Dict[str, List[dict]] = defaultdict(list)

    for fragment in fragments:
        row = fragment.to_record()
        row["measurement_summary"] = measurements_by_fragment.get(fragment.fragment_id, {"count": 0, "types": [], "records": []})
        related_rows = related_by_fragment.get(fragment.fragment_id, [])
        row["related_fragments"] = related_rows
        row["related_cross_source"] = [item for item in related_rows if not item.get("same_source")]
        row["related_same_source"] = [item for item in related_rows if item.get("same_source")]
        row["canonical_promotion"] = _build_canonical_promotion_summary(row)
        row["dropped_weak_anchor_state"] = _build_dropped_weak_anchor_state(row)
        row["observer_disagreement"] = _build_observer_disagreement_summary(row)
        row["ingest_lineage"] = _build_ingest_lineage_summary(row)
        grouped[fragment.source_path].append(row)

    existing_source_paths = set(grouped.keys())
    synthetic_rows_by_source = _build_synthetic_source_rows(materials, existing_source_paths)
    for source_path, rows in synthetic_rows_by_source.items():
        grouped[source_path].extend(rows)

    sources = []
    for source_path, rows in sorted(grouped.items()):
        source_text = _read_source_text(runtime_root, source_path)
        rows.sort(key=lambda row: ((row.get("source_range") or {}).get("start") or -1, row["fragment_id"]))
        compact_summary = _build_source_compact_summary(rows)
        sources.append(
            {
                "source_path": source_path,
                "source_text": source_text,
                "fragment_count": len(rows),
                "compact_summary": compact_summary,
                "fragments": rows,
            }
        )

    return {
        "summary": {
            "source_count": len(sources),
            "fragment_count": len(fragments),
        },
        "compact_summary": _build_global_compact_summary(sources),
        "sources": sources,
    }


def write_source_fragment_view(runtime_root: Path) -> Dict[str, Path]:
    data = build_source_fragment_view_data(runtime_root)
    reports_root = runtime_root / "reports"
    manifests_root = runtime_root / "manifests" / "source_views"
    reports_root.mkdir(parents=True, exist_ok=True)
    manifests_root.mkdir(parents=True, exist_ok=True)

    json_path = reports_root / "source_fragment_view.json"
    html_path = reports_root / "source_fragment_view.html"
    manifest_path = manifests_root / "latest_source_fragment_view.json"

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    html_path.write_text(render_source_fragment_html(data), encoding="utf-8")
    return {"json_path": json_path, "html_path": html_path, "manifest_path": manifest_path}


def _read_source_text(runtime_root: Path, source_path: str) -> str:
    if not source_path:
        return ""
    path = Path(source_path)
    candidates = [path] if path.is_absolute() else [runtime_root / "source_documents" / source_path, runtime_root / source_path]
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.read_text(encoding="utf-8")
    return ""


def _group_measurements_by_fragment(records: List[object]) -> Dict[str, Dict[str, object]]:
    grouped: Dict[str, List[dict]] = defaultdict(list)
    for record in records:
        grouped[record.fragment_id].append(record.to_record())

    result: Dict[str, Dict[str, object]] = {}
    for fragment_id, rows in grouped.items():
        rows.sort(key=lambda row: (row.get("measurement_type", ""), row.get("column_key", ""), row.get("recorded_at", "")))
        anchor_history = _build_anchor_history_summary(rows)
        observer_summary = _build_observer_summary(rows)
        result[fragment_id] = {
            "count": len(rows),
            "types": sorted({row.get("measurement_type", "") for row in rows if row.get("measurement_type")}),
            "records": rows,
            "anchor_history": anchor_history,
            "observer_summary": observer_summary,
        }
    return result


def _build_anchor_history_summary(rows: List[dict]) -> Dict[str, object]:
    anchor_rows = [row for row in rows if row.get("measurement_type") == "anchor"]
    if not anchor_rows:
        return {
            "version_count": 0,
            "latest_batch_id": "",
            "latest_keys": [],
            "previous_batch_id": "",
            "previous_keys": [],
            "added_keys": [],
            "removed_keys": [],
        }

    grouped: Dict[str, List[dict]] = defaultdict(list)
    batch_order: List[str] = []
    for row in sorted(anchor_rows, key=lambda row: row.get("recorded_at", "")):
        metadata = row.get("metadata") or {}
        batch_id = metadata.get("ingest_batch_id") or "unbatched"
        if batch_id not in grouped:
            batch_order.append(batch_id)
        grouped[batch_id].append(row)

    latest_batch_id = batch_order[-1]
    previous_batch_id = batch_order[-2] if len(batch_order) >= 2 else ""
    latest_keys = sorted({row.get("column_key", "") for row in grouped[latest_batch_id] if row.get("column_key")})
    previous_keys = sorted({row.get("column_key", "") for row in grouped.get(previous_batch_id, []) if row.get("column_key")})

    return {
        "version_count": len(batch_order),
        "latest_batch_id": latest_batch_id,
        "latest_keys": latest_keys,
        "previous_batch_id": previous_batch_id,
        "previous_keys": previous_keys,
        "added_keys": [key for key in latest_keys if key not in previous_keys],
        "removed_keys": [key for key in previous_keys if key not in latest_keys],
    }


def _build_observer_summary(rows: List[dict]) -> Dict[str, object]:
    observer_rows = [
        row for row in rows
        if row.get("measurement_type") in {"revision_judgment", "connection_observation"}
    ]
    if not observer_rows:
        return {
            "count": 0,
            "types": [],
            "revision_count": 0,
            "accepted_count": 0,
            "deferred_count": 0,
            "rejected_count": 0,
            "records": [],
        }

    summary = {
        "count": len(observer_rows),
        "types": sorted({row.get("measurement_type", "") for row in observer_rows if row.get("measurement_type")}),
        "revision_count": 0,
        "accepted_count": 0,
        "deferred_count": 0,
        "rejected_count": 0,
        "records": [],
    }

    compact_records: List[dict] = []
    for row in observer_rows:
        if row.get("measurement_type") == "revision_judgment":
            summary["revision_count"] += 1
        if row.get("measurement_type") == "connection_observation":
            relation_status = (row.get("value") or {}).get("relation_status", "")
            if relation_status == "accepted_connection":
                summary["accepted_count"] += 1
            elif relation_status == "deferred_connection":
                summary["deferred_count"] += 1
            elif relation_status == "rejected_connection":
                summary["rejected_count"] += 1
        compact_records.append(
            {
                "measurement_type": row.get("measurement_type", ""),
                "column_key": row.get("column_key", ""),
                "evidence_text": row.get("evidence_text", ""),
                "recorded_at": row.get("recorded_at", ""),
                "origin": row.get("origin", ""),
                "value": row.get("value", {}),
            }
        )

    compact_records.sort(key=lambda row: (row.get("recorded_at", ""), row.get("measurement_type", "")), reverse=True)
    summary["records"] = compact_records[:6]
    return summary


def _build_connection_observation_index(records: List[object]) -> Dict[tuple, dict]:
    latest: Dict[tuple, dict] = {}
    for record in records:
        row = record.to_record()
        if row.get("measurement_type") != "connection_observation":
            continue
        value = row.get("value") or {}
        counterpart = value.get("counterpart_fragment_id", "")
        if not counterpart:
            continue
        pair = (row.get("fragment_id", ""), counterpart)
        previous = latest.get(pair)
        payload = {
            "relation_status": value.get("relation_status", ""),
            "reason": value.get("reason", ""),
            "reason_family": value.get("reason_family", ""),
            "confidence": row.get("confidence", 0.0),
            "recorded_at": row.get("recorded_at", ""),
        }
        if previous is None or row.get("recorded_at", "") >= previous.get("recorded_at", ""):
            latest[pair] = payload
        reverse_pair = (counterpart, row.get("fragment_id", ""))
        reverse_previous = latest.get(reverse_pair)
        if reverse_previous is None or row.get("recorded_at", "") >= reverse_previous.get("recorded_at", ""):
            latest[reverse_pair] = {
                "relation_status": value.get("relation_status", ""),
                "reason": value.get("reason", ""),
                "reason_family": value.get("reason_family", ""),
                "confidence": row.get("confidence", 0.0),
                "recorded_at": row.get("recorded_at", ""),
            }
    return latest


def _build_related_fragment_index(fragments: List[object], connection_index: Dict[tuple, dict]) -> Dict[str, List[dict]]:
    anchor_map: Dict[str, List[object]] = defaultdict(list)
    family_map: Dict[str, List[object]] = defaultdict(list)
    for fragment in fragments:
        for anchor in getattr(fragment, "anchors", []) or []:
            if anchor.key:
                anchor_map[anchor.key].append(fragment)
                family = _anchor_family(anchor.key)
                if family:
                    family_map[family].append(fragment)

    related: Dict[str, List[dict]] = {}
    for fragment in fragments:
        scored: Dict[str, dict] = {}
        own_keys = [anchor.key for anchor in (getattr(fragment, "anchors", []) or []) if anchor.key]
        for key in own_keys:
            for other in anchor_map.get(key, []):
                if other.fragment_id == fragment.fragment_id:
                    continue
                row = scored.setdefault(
                    other.fragment_id,
                    {
                        "fragment_id": other.fragment_id,
                        "source_path": other.source_path,
                        "same_source": other.source_path == fragment.source_path,
                        "scene": other.scene,
                        "flow": other.flow,
                        "shared_anchor_keys": [],
                        "shared_anchor_count": 0,
                        "preview_text": " ".join(other.raw_text.split())[:140],
                        "shared_anchor_families": [],
                        "family_match_count": 0,
                        "observer_relation": connection_index.get((fragment.fragment_id, other.fragment_id), {}),
                    },
                )
                if key not in row["shared_anchor_keys"]:
                    row["shared_anchor_keys"].append(key)
        own_families = sorted({_anchor_family(key) for key in own_keys if _anchor_family(key)})
        for family in own_families:
            for other in family_map.get(family, []):
                if other.fragment_id == fragment.fragment_id:
                    continue
                row = scored.setdefault(
                    other.fragment_id,
                    {
                        "fragment_id": other.fragment_id,
                        "source_path": other.source_path,
                        "same_source": other.source_path == fragment.source_path,
                        "scene": other.scene,
                        "flow": other.flow,
                        "shared_anchor_keys": [],
                        "shared_anchor_count": 0,
                        "preview_text": " ".join(other.raw_text.split())[:140],
                        "shared_anchor_families": [],
                        "family_match_count": 0,
                        "observer_relation": connection_index.get((fragment.fragment_id, other.fragment_id), {}),
                    },
                )
                if family and family not in row["shared_anchor_families"]:
                    row["shared_anchor_families"].append(family)
        rows = list(scored.values())
        for row in rows:
            row["shared_anchor_keys"].sort()
            row["shared_anchor_count"] = len(row["shared_anchor_keys"])
            row["shared_anchor_families"].sort()
            row["family_match_count"] = len(row["shared_anchor_families"])
        rows.sort(
            key=lambda row: (
                row.get("same_source", False),
                -row["shared_anchor_count"],
                -row["family_match_count"],
                row["fragment_id"],
            )
        )
        related[fragment.fragment_id] = rows[:6]
    return related


def _anchor_family(key: str) -> str:
    parts = [part for part in key.split(".") if part]
    if len(parts) >= 2:
        return ".".join(parts[:2])
    return parts[0] if parts else ""


def _build_canonical_promotion_summary(row: Dict[str, object]) -> Dict[str, object]:
    anchors = list(row.get("anchors", []) or [])
    items = []
    for anchor in anchors[:8]:
        items.append(
            {
                "canonical_key": anchor.get("canonical_key") or anchor.get("key") or "",
                "display_label": anchor.get("label") or anchor.get("value") or "",
                "anchor_type": anchor.get("anchor_type", ""),
                "origin": anchor.get("origin", ""),
                "confidence": anchor.get("confidence"),
                "status": anchor.get("status", ""),
            }
        )
    return {
        "available": bool(anchors),
        "count": len(anchors),
        "items": items,
    }


def _build_dropped_weak_anchor_state(row: Dict[str, object]) -> Dict[str, object]:
    metadata = row.get("metadata") or {}
    dropped = metadata.get("dropped_weak_anchors")
    if dropped is None:
        return {"available": False, "items": []}
    items = [str(item).strip() for item in dropped if str(item).strip()]
    return {"available": True, "items": items[:10]}


def _build_observer_disagreement_summary(row: Dict[str, object]) -> Dict[str, object]:
    metadata = row.get("metadata") or {}
    fallback_trace = metadata.get("observer_or_ambiguity_trace") or {}
    internal = metadata.get("internal_observer") or {}
    profiles = internal.get("profiles") or {}
    merged = internal.get("merged") or {}
    if not profiles:
        if fallback_trace:
            return {
                "available": bool(fallback_trace.get("available", False)),
                "items": list(fallback_trace.get("items", []) or []),
                "merged": dict(fallback_trace.get("merged", {}) or {}),
            }
        return {"available": False, "items": [], "merged": {}}

    scenes = {}
    roles = {}
    for profile_name, payload in profiles.items():
        scene = payload.get("scene")
        role = payload.get("role")
        if scene:
            scenes[str(profile_name)] = str(scene)
        if role:
            roles[str(profile_name)] = str(role)

    items = []
    unique_scenes = sorted(set(scenes.values()))
    unique_roles = sorted(set(roles.values()))
    if len(unique_scenes) > 1:
        items.append(
            {
                "kind": "scene",
                "profiles": scenes,
                "summary": "scene disagreement: " + " / ".join(f"{k}={v}" for k, v in scenes.items()),
            }
        )
    if len(unique_roles) > 1:
        items.append(
            {
                "kind": "role",
                "profiles": roles,
                "summary": "role disagreement: " + " / ".join(f"{k}={v}" for k, v in roles.items()),
            }
        )
    return {
        "available": True,
        "items": items,
        "merged": {
            "scene": merged.get("scene", ""),
            "role": merged.get("role", ""),
            "ambiguity": merged.get("ambiguity"),
            "confidence": merged.get("confidence"),
        },
    }


def _build_ingest_lineage_summary(row: Dict[str, object]) -> Dict[str, object]:
    metadata = row.get("metadata") or {}
    return {
        "ingest_batch_id": metadata.get("ingest_batch_id", ""),
        "ingest_session_id": metadata.get("ingest_session_id", "") or row.get("session_id", ""),
        "ingest_input_path": metadata.get("ingest_input_path", "") or row.get("source_path", ""),
        "provenance_steps": [entry.get("step", "") for entry in (row.get("provenance_log") or []) if entry.get("step")],
    }


def _build_synthetic_source_rows(
    materials: List[Dict[str, object]],
    existing_source_paths: set,
) -> Dict[str, List[Dict[str, object]]]:
    grouped: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    source_seen = set()
    for material in materials:
        source_ref = str(material.get("source_ref", "")).strip()
        if not source_ref or source_ref in existing_source_paths:
            continue
        metadata = dict(material.get("metadata", {}))
        if "scene" not in metadata or "flow" not in metadata:
            continue
        fragment_id = str(metadata.get("dust_input_id", "")).strip() or str(material.get("material_id", "")).strip()
        if not fragment_id:
            continue
        dedupe = (source_ref, fragment_id)
        if dedupe in source_seen:
            continue
        source_seen.add(dedupe)
        row = {
            "fragment_id": fragment_id,
            "source_id": str(metadata.get("source_origin_id", "")).strip() or source_ref,
            "source_path": source_ref,
            "source_type": str(material.get("source_type", "memo")).strip() or "memo",
            "raw_text": str(material.get("raw_payload", "")).strip(),
            "scene": str(metadata.get("scene", "unknown")).strip() or "unknown",
            "flow": str(metadata.get("flow", "unknown")).strip() or "unknown",
            "time": str(metadata.get("time_in", "")).strip(),
            "unit_scale": "",
            "source_range": {"start": None, "end": None},
            "anchors": _material_anchor_rows(metadata),
            "metadata": {
                "ingest_batch_id": str(metadata.get("ingest_batch_id", "")).strip(),
                "ingest_session_id": str(metadata.get("ingest_session_id", "")).strip() or str(material.get("session_id", "")).strip(),
                "ingest_input_path": str(metadata.get("ingest_input_path", "")).strip() or source_ref,
                "dropped_weak_anchors": list(metadata.get("dropped_weak_anchors", []) or []),
                "observer_or_ambiguity_trace": dict(metadata.get("observer_or_ambiguity_trace", {}) or {}),
            },
            "provenance_log": [],
            "measurement_summary": {"count": 0, "types": [], "records": [], "anchor_history": {"version_count": 0, "latest_batch_id": "", "latest_keys": [], "previous_batch_id": "", "previous_keys": [], "added_keys": [], "removed_keys": []}, "observer_summary": {"count": 0, "types": [], "revision_count": 0, "accepted_count": 0, "deferred_count": 0, "rejected_count": 0, "records": []}},
            "related_fragments": [],
            "related_cross_source": [],
            "related_same_source": [],
        }
        row["canonical_promotion"] = _build_canonical_promotion_summary(row)
        row["dropped_weak_anchor_state"] = _build_dropped_weak_anchor_state(row)
        row["observer_disagreement"] = _build_observer_disagreement_summary(row)
        row["ingest_lineage"] = {
            "ingest_batch_id": str(metadata.get("ingest_batch_id", "")).strip(),
            "ingest_session_id": str(material.get("session_id", "")).strip(),
            "ingest_input_path": source_ref,
            "provenance_steps": ["material_backed_source"],
        }
        grouped[source_ref].append(row)
    return grouped


def _material_anchor_rows(metadata: Dict[str, object]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for anchor in list(metadata.get("anchors", []) or [])[:8]:
        rows.append(
            {
                "anchor_type": str(anchor.get("type", "semantic")).strip() or "semantic",
                "key": str(anchor.get("canonical_key") or anchor.get("key") or anchor.get("value") or "").strip(),
                "label": str(anchor.get("value") or anchor.get("canonical_key") or "").strip(),
                "value": str(anchor.get("value") or anchor.get("canonical_key") or "").strip(),
                "origin": "material_backed_source",
                "confidence": 0.7,
            }
        )
    return rows


def _build_source_compact_summary(rows: List[Dict[str, object]]) -> Dict[str, object]:
    canonical_items: List[Dict[str, str]] = []
    seen_canonical = set()
    dropped_items: List[str] = []
    disagreement_items: List[str] = []
    lineage_items: List[str] = []
    dropped_available = False
    disagreement_available = False
    lineage_available = False

    for row in rows:
        promo = row.get("canonical_promotion") or {}
        for item in promo.get("items", []):
            canonical_key = str(item.get("canonical_key", "")).strip()
            if not canonical_key or canonical_key in seen_canonical:
                continue
            seen_canonical.add(canonical_key)
            canonical_items.append(
                {
                    "canonical_key": canonical_key,
                    "display_label": str(item.get("display_label", "")).strip(),
                    "anchor_type": str(item.get("anchor_type", "semantic")).strip() or "semantic",
                }
            )
            if len(canonical_items) >= 3:
                break
        dropped = row.get("dropped_weak_anchor_state") or {}
        if dropped.get("available") is True:
            dropped_available = True
            for value in dropped.get("items", []):
                text = str(value).strip()
                if text and text not in dropped_items:
                    dropped_items.append(text)
                if len(dropped_items) >= 3:
                    break
        disagreement = row.get("observer_disagreement") or {}
        if disagreement.get("available") is True:
            disagreement_available = True
            for item in disagreement.get("items", []):
                summary = str(item.get("summary", "")).strip()
                if summary and summary not in disagreement_items:
                    disagreement_items.append(summary)
                if len(disagreement_items) >= 3:
                    break
        lineage = row.get("ingest_lineage") or {}
        lineage_values = [
            lineage.get("ingest_batch_id", ""),
            lineage.get("ingest_session_id", ""),
            lineage.get("ingest_input_path", ""),
        ]
        lineage_steps = list(lineage.get("provenance_steps", []))
        for value in [*lineage_values, *lineage_steps]:
            text = str(value).strip()
            if text:
                lineage_available = True
            if text and text not in lineage_items:
                lineage_items.append(text)
            if len(lineage_items) >= 3:
                break

    return {
        "canonical_promotion": compact_payload(
            available=bool(canonical_items),
            items=canonical_items,
            limit=3,
        ),
        "dropped_weak": compact_payload(
            available=dropped_available,
            items=dropped_items,
            limit=3,
        ),
        "observer_disagreement": compact_payload(
            available=disagreement_available,
            items=disagreement_items,
            limit=3,
        ),
        "ingest_lineage": compact_payload(
            available=lineage_available,
            items=lineage_items,
            limit=3,
        ),
    }


def _build_global_compact_summary(sources: List[Dict[str, object]]) -> Dict[str, object]:
    all_rows: List[Dict[str, object]] = []
    for source in sources:
        all_rows.extend(list(source.get("fragments", [])))
    return _build_source_compact_summary(all_rows)
