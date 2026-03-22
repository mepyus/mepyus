from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


def sync_local_space_anchor_metadata(runtime_root: Path, local_space_id: str) -> Dict[str, object] | None:
    local_space_path = runtime_root / "core" / "local_spaces" / f"{local_space_id}.json"
    if not local_space_path.exists():
        return None
    local_space = _read_json(local_space_path)
    materials = _collect_materials(runtime_root, local_space)
    if not materials:
        return None
    source_label = _suggest_source_label(materials, local_space)
    rep_anchors, supporting, dropped_weak = _summarize_material_anchors(materials)
    processing_baseline = _summarize_processing_values(materials)
    observer_trace = _summarize_observer_trace(materials)
    possibility_refs = _collect_possibility_bridge_refs(runtime_root, local_space_id)
    transition_summary = _build_state_transition_summary(local_space, materials, possibility_refs)
    local_space["source_label"] = source_label
    if rep_anchors:
        local_space["representative_anchors"] = rep_anchors
    if supporting:
        local_space["supporting_anchors"] = supporting
    if dropped_weak:
        local_space["dropped_weak_anchors"] = dropped_weak
    if processing_baseline:
        local_space["processing_baseline"] = processing_baseline
    if observer_trace:
        local_space["observer_or_ambiguity_trace"] = observer_trace
    if transition_summary:
        local_space["state_transition_summary"] = transition_summary
        local_space["canonical_bridge_exposure_count"] = transition_summary.get("canonical_bridge_exposure_count", 0)
        local_space["possibility_bridge_exposure_count"] = transition_summary.get("possibility_bridge_exposure_count", 0)
    local_space["possibility_bridge_refs"] = possibility_refs
    _write_json(local_space_path, local_space)
    return {
        "local_space_id": local_space_id,
        "source_label": source_label,
        "representative_anchor_labels": [row["display_label"] for row in rep_anchors],
    }


def _collect_materials(runtime_root: Path, local_space: Dict[str, object]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    cell_dir = runtime_root / "core" / "space_cells"
    material_dir = runtime_root / "core" / "materials"
    for cell_id in local_space.get("cell_refs", []):
        cell_path = cell_dir / f"{cell_id}.json"
        if not cell_path.exists():
            continue
        cell = _read_json(cell_path)
        for material_id in cell.get("material_refs", []):
            material_path = material_dir / f"{material_id}.json"
            if material_path.exists():
                rows.append(_read_json(material_path))
    return rows


def _suggest_source_label(materials: List[Dict[str, object]], local_space: Dict[str, object]) -> str:
    existing = _clean_label(local_space.get("source_label"))
    if existing:
        return existing
    family_counts = Counter(
        _clean_label(row.get("family_id"))
        for row in materials
        if _clean_label(row.get("family_id"))
    )
    if family_counts:
        return family_counts.most_common(1)[0][0]
    source_counts = Counter(
        Path(ref).stem
        for row in materials
        for ref in [_clean_label(row.get("source_ref"))]
        if ref
    )
    if source_counts:
        return source_counts.most_common(1)[0][0]
    return str(local_space.get("local_space_id", ""))


def _summarize_material_anchors(materials: List[Dict[str, object]]) -> Tuple[List[Dict[str, object]], List[str], List[str]]:
    grouped: Dict[Tuple[str, str, str], Dict[str, object]] = {}
    counts: Counter[Tuple[str, str, str]] = Counter()
    dropped_counts: Counter[str] = Counter()
    for material in materials:
        metadata = material.get("metadata", {})
        for anchor in metadata.get("anchors", []):
            canonical_key = str(anchor.get("canonical_key") or anchor.get("key") or "").strip()
            display_label = str(anchor.get("value") or anchor.get("display_label") or "").strip()
            anchor_type = str(anchor.get("type", "semantic")).strip() or "semantic"
            if not canonical_key or not display_label:
                continue
            key = (canonical_key, display_label, anchor_type)
            counts[key] += 1
            grouped[key] = {
                "canonical_key": canonical_key,
                "display_label": display_label,
                "anchor_type": anchor_type,
            }
        for value in list(metadata.get("dropped_weak_anchors", []) or []):
            label = str(value).strip()
            if label:
                dropped_counts[label] += 1
    ordered = sorted(counts.items(), key=lambda row: (-row[1], row[0][1]))
    rep = [grouped[key] for key, _count in ordered[:4]]
    supporting = [grouped[key]["display_label"] for key, _count in ordered[4:8]]
    dropped_weak = [label for label, _count in dropped_counts.most_common(10)]
    return rep, supporting, dropped_weak


def _summarize_processing_values(materials: List[Dict[str, object]]) -> Dict[str, object]:
    d_vals: List[float] = []
    i_vals: List[float] = []
    s_vals: List[float] = []
    scene_counts: Counter[str] = Counter()
    flow_counts: Counter[str] = Counter()
    for material in materials:
        metadata = material.get("metadata", {})
        payload = dict(metadata.get("processing_values", {}))
        d_vals.append(float(payload.get("D", metadata.get("D", 0.5))))
        i_vals.append(float(payload.get("I", metadata.get("I", 0.5))))
        s_vals.append(float(payload.get("S", metadata.get("S", 0.5))))
        scene = _clean_label(payload.get("scene")) or _clean_label(metadata.get("scene"))
        flow = _clean_label(payload.get("flow")) or _clean_label(metadata.get("flow"))
        if scene:
            scene_counts[scene] += 1
        if flow:
            flow_counts[flow] += 1
    if not d_vals:
        return {}
    return {
        "D": round(sum(d_vals) / len(d_vals), 4),
        "I": round(sum(i_vals) / len(i_vals), 4),
        "S": round(sum(s_vals) / len(s_vals), 4),
        "dominant_scene": scene_counts.most_common(1)[0][0] if scene_counts else "",
        "dominant_flow": flow_counts.most_common(1)[0][0] if flow_counts else "",
    }


def _summarize_observer_trace(materials: List[Dict[str, object]]) -> Dict[str, object]:
    roles: Counter[str] = Counter()
    signals: Counter[str] = Counter()
    scenes: Counter[str] = Counter()
    available_count = 0
    ambiguity_values: List[float] = []
    confidence_values: List[float] = []
    item_count = 0
    trace_seen = False
    for material in materials:
        metadata = material.get("metadata", {})
        trace = dict(metadata.get("observer_or_ambiguity_trace", {}))
        if trace:
            trace_seen = True
            available_count += 1 if bool(trace.get("available")) else 0
            merged = dict(trace.get("merged", {}))
            role = _clean_label(merged.get("role")) or _clean_label(metadata.get("observer_role"))
            scene = _clean_label(merged.get("scene")) or _clean_label(metadata.get("scene"))
            if role:
                roles[role] += 1
            if scene:
                scenes[scene] += 1
            for signal in list(merged.get("signals", []) or metadata.get("observer_signals", []) or []):
                label = _clean_label(signal)
                if label:
                    signals[label] += 1
            ambiguity = merged.get("ambiguity", metadata.get("observer_ambiguity"))
            confidence = merged.get("confidence", metadata.get("observer_confidence_numeric"))
            if isinstance(ambiguity, (int, float)):
                ambiguity_values.append(float(ambiguity))
            if isinstance(confidence, (int, float)):
                confidence_values.append(float(confidence))
            item_count += len(list(trace.get("items", []) or []))
            continue
        role = _clean_label(metadata.get("observer_role"))
        scene = _clean_label(metadata.get("scene"))
        if role:
            roles[role] += 1
        if scene:
            scenes[scene] += 1
        for signal in list(metadata.get("observer_signals", []) or []):
            label = _clean_label(signal)
            if label:
                signals[label] += 1
        ambiguity = metadata.get("observer_ambiguity")
        confidence = metadata.get("observer_confidence_numeric")
        if isinstance(ambiguity, (int, float)):
            ambiguity_values.append(float(ambiguity))
        if isinstance(confidence, (int, float)):
            confidence_values.append(float(confidence))
    if not roles and not signals and not ambiguity_values and not confidence_values and not available_count and not trace_seen:
        return {}
    return {
        "available": bool(available_count),
        "merged": {
            "role": roles.most_common(1)[0][0] if roles else "",
            "scene": scenes.most_common(1)[0][0] if scenes else "",
            "ambiguity": round(sum(ambiguity_values) / len(ambiguity_values), 4) if ambiguity_values else None,
            "confidence": round(sum(confidence_values) / len(confidence_values), 4) if confidence_values else None,
            "signals": [label for label, _count in signals.most_common(3)],
        },
        "items": [],
        "item_count": item_count,
        "unavailable_reason": "" if available_count or trace_seen else "observer_trace_missing",
        "note": "observer compare propagated from material baseline" if trace_seen else "",
    }


def _build_state_transition_summary(
    local_space: Dict[str, object],
    materials: List[Dict[str, object]],
    possibility_refs: List[str],
) -> Dict[str, object]:
    bridge_refs = [str(value).strip() for value in local_space.get("bridge_trace_refs", []) if str(value).strip()]
    state = _clean_label(local_space.get("state")) or "unknown"
    source_refs = sorted(
        {
            ref
            for material in materials
            for ref in [_clean_label(material.get("source_ref"))]
            if ref
        }
    )
    if bridge_refs and state == "bridge_exposed":
        inferred_transition = "forming -> bridge_exposed"
    elif possibility_refs:
        inferred_transition = "forming -> possibility_exposed"
    else:
        inferred_transition = f"forming -> {state}"
    return {
        "available": True,
        "current_state": state,
        "inferred_transition": inferred_transition,
        "bridge_exposure_count": len(bridge_refs),
        "canonical_bridge_exposure_count": len(bridge_refs),
        "possibility_bridge_exposure_count": len(possibility_refs),
        "material_count": len(materials),
        "source_ref_count": len(source_refs),
        "source_refs": source_refs[:4],
    }


def _clean_label(value: object) -> str:
    text = str(value or "").strip()
    if text.lower() in {"none", "null"}:
        return ""
    return text


def _collect_possibility_bridge_refs(runtime_root: Path, local_space_id: str) -> List[str]:
    possibility_dir = runtime_root / "core" / "possibility_bridges"
    if not possibility_dir.exists():
        return []
    refs: List[str] = []
    for path in possibility_dir.glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        left = str(payload.get("from_local_space_id", "")).strip()
        right = str(payload.get("to_local_space_id", "")).strip()
        if local_space_id in {left, right}:
            ref = str(payload.get("possibility_bridge_id", "")).strip()
            if ref:
                refs.append(ref)
    return sorted(set(refs))


def _read_json(path: Path) -> Dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: Dict[str, object]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
