from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Sequence
from collections import Counter
import json
import math
import statistics

from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs


def build_pre_materialization_profile(*, source_ref: str, source_type: str, raw_payload: str) -> Dict[str, object]:
    dust_inputs = build_dust_inputs_from_source(
        source_id="probe",
        source_type=source_type,
        source_ref=source_ref,
        raw_payload=raw_payload,
        created_at="2026-03-21T00:00:00Z",
    )
    labeled_dusts = label_dust_inputs(dust_inputs)
    lengths = [len(row.text) for row in dust_inputs]
    processing_signatures = [
        "|".join(
            [
                row.scene,
                row.flow,
                str(row.D),
                str(row.I),
                str(row.S),
            ]
        )
        for row in labeled_dusts
    ]
    scene_flow_pairs = [f"{row.scene}|{row.flow}" for row in labeled_dusts]
    return {
        "source_ref": source_ref,
        "source_type": source_type,
        "unit_count": len(dust_inputs),
        "avg_span_width": round(sum(lengths) / len(lengths), 2) if lengths else 0.0,
        "max_span_width": max(lengths) if lengths else 0,
        "min_span_width": min(lengths) if lengths else 0,
        "sample_units": [row.text[:120] for row in dust_inputs[:3]],
        "sibling_density": len(dust_inputs[0].siblings) if dust_inputs else 0,
        "pre_processing_signature_unique_ratio": _ratio(len(set(processing_signatures)), len(processing_signatures)),
        "pre_processing_signature_entropy": _normalized_entropy(processing_signatures),
        "pre_scene_flow_uniqueness_ratio": _ratio(len(set(scene_flow_pairs)), len(scene_flow_pairs)),
        "pre_direction_variance": _variance([row.D for row in labeled_dusts]),
        "pre_intensity_variance": _variance([row.I for row in labeled_dusts]),
        "pre_stability_variance": _variance([row.S for row in labeled_dusts]),
        "pre_scene_counts": dict(Counter(row.scene for row in labeled_dusts)),
        "pre_flow_counts": dict(Counter(row.flow for row in labeled_dusts)),
    }


def build_post_materialization_profile(materials: Sequence[Dict[str, object]]) -> Dict[str, object]:
    anchor_bundle_count = 0
    processing_values_count = 0
    transformable_handles_count = 0
    dropped_weak_count = 0
    observer_trace_count = 0
    observer_available_count = 0
    local_ref_count = 0
    translated_handle_material_count = 0
    translated_handle_total_count = 0
    anchor_density_values: List[int] = []
    processing_key_counts: List[int] = []
    handle_key_counts: List[int] = []
    local_refs: List[str] = []
    translated_local_refs: List[str] = []
    anchor_signatures: List[str] = []
    processing_signatures: List[str] = []
    handle_signatures: List[str] = []
    translated_signatures: List[str] = []
    role_values: List[str] = []
    scene_values: List[str] = []
    flow_values: List[str] = []
    d_values: List[float] = []
    i_values: List[float] = []
    s_values: List[float] = []
    translation_broadcast_leak = False

    source_refs = set()
    for material in materials:
        source_ref = str(material.get("source_ref", "")).strip()
        if source_ref:
            source_refs.add(source_ref)
        metadata = dict(material.get("metadata", {}) or {})
        if "anchor_bundle" in metadata:
            anchor_bundle_count += 1
            anchor_bundle = dict(metadata.get("anchor_bundle", {}) or {})
            rep = list(anchor_bundle.get("representative_anchors", []) or [])
            sup = list(anchor_bundle.get("supporting_anchors", []) or [])
            anchor_density_values.append(
                len(rep) + len(sup)
            )
            anchor_signatures.append(
                "|".join(
                    [
                        *(str(row.get("canonical_key", "")).strip() for row in rep[:4]),
                        *(str(row).strip() for row in sup[:4]),
                    ]
                )
            )
        else:
            anchor_density_values.append(0)
            anchor_signatures.append("")
        if "processing_values" in metadata:
            processing_values_count += 1
            processing_payload = dict(metadata.get("processing_values", {}) or {})
            processing_key_counts.append(len(processing_payload))
            processing_signatures.append(
                "|".join(
                    [
                        str(processing_payload.get("scene", "")).strip(),
                        str(processing_payload.get("flow", "")).strip(),
                        str(processing_payload.get("D", "")),
                        str(processing_payload.get("I", "")),
                        str(processing_payload.get("S", "")),
                    ]
                )
            )
        else:
            processing_key_counts.append(0)
            processing_signatures.append("")
        if "transformable_handles" in metadata:
            transformable_handles_count += 1
            handles = dict(metadata.get("transformable_handles", {}) or {})
            handle_key_counts.append(len(handles))
            local_ref = str(handles.get("source_local_ref", "")).strip()
            local_refs.append(local_ref)
            handle_signatures.append(
                "|".join(
                    [
                        local_ref,
                        str(handles.get("dust_input_id", "")).strip(),
                        str(handles.get("source_origin_id", "")).strip(),
                    ]
                )
            )
            if local_ref:
                local_ref_count += 1
        else:
            handle_key_counts.append(0)
            local_refs.append("")
            handle_signatures.append("")
        translated_handles = list(metadata.get("translated_handles", []) or [])
        if translated_handles:
            translated_handle_material_count += 1
            translated_handle_total_count += len(translated_handles)
            translated_local_refs.append(local_refs[-1])
            translated_signatures.append(
                "|".join(
                    sorted(
                        {
                            str(row.get("translated_handle", "")).strip()
                            for row in translated_handles
                            if str(row.get("translated_handle", "")).strip()
                        }
                    )[:8]
                )
            )
            for row in translated_handles:
                scope = str(row.get("translation_scope", "")).strip()
                source_local_ref = str(row.get("translation_source_local_ref", "")).strip()
                if scope != "local_ref" or (source_local_ref and local_refs[-1] and source_local_ref != local_refs[-1]):
                    translation_broadcast_leak = True
        else:
            translated_signatures.append("")
        if "dropped_weak_anchors" in metadata:
            dropped_weak_count += 1
        trace = dict(metadata.get("observer_or_ambiguity_trace", {}) or {})
        if trace:
            observer_trace_count += 1
            if trace.get("available") is True:
                observer_available_count += 1
        role_values.append(str(metadata.get("observer_role", "")).strip())
        scene_values.append(str(metadata.get("scene", "")).strip())
        flow_values.append(str(metadata.get("flow", "")).strip())
        d_values.append(float(metadata.get("D", 0.5) or 0.5))
        i_values.append(float(metadata.get("I", 0.5) or 0.5))
        s_values.append(float(metadata.get("S", 0.5) or 0.5))

    material_count = len(list(materials))
    local_ref_counter = Counter(value for value in local_refs if value)
    anchor_counter = Counter(value for value in anchor_signatures if value)
    processing_counter = Counter(value for value in processing_signatures if value)
    handle_counter = Counter(value for value in handle_signatures if value)
    translated_counter = Counter(value for value in translated_signatures if value)
    processing_signature_unique_ratio = _signature_unique_ratio(processing_counter, material_count)
    scene_flow_role_uniqueness_ratio = _ratio(
        len(
            {
                (scene_values[idx], flow_values[idx], role_values[idx])
                for idx in range(material_count)
                if scene_values[idx] or flow_values[idx] or role_values[idx]
            }
        ),
        material_count,
    )
    processing_value_variance = {
        "D": _variance(d_values),
        "I": _variance(i_values),
        "S": _variance(s_values),
    }
    return {
        "material_count": material_count,
        "source_ref_count": len(source_refs),
        "anchor_bundle_presence_ratio": _ratio(anchor_bundle_count, material_count),
        "processing_values_presence_ratio": _ratio(processing_values_count, material_count),
        "transformable_handles_presence_ratio": _ratio(transformable_handles_count, material_count),
        "source_local_ref_presence_ratio": _ratio(local_ref_count, material_count),
        "dropped_weak_presence_ratio": _ratio(dropped_weak_count, material_count),
        "observer_trace_presence_ratio": _ratio(observer_trace_count, material_count),
        "observer_trace_available_ratio": _ratio(observer_available_count, material_count),
        "avg_anchor_density": round(sum(anchor_density_values) / len(anchor_density_values), 2) if anchor_density_values else 0.0,
        "avg_processing_key_count": round(sum(processing_key_counts) / len(processing_key_counts), 2) if processing_key_counts else 0.0,
        "avg_handle_key_count": round(sum(handle_key_counts) / len(handle_key_counts), 2) if handle_key_counts else 0.0,
        "unique_source_local_ref_count": len(local_ref_counter),
        "materials_per_local_ref_max": max(local_ref_counter.values()) if local_ref_counter else 0,
        "translation_applied_local_ref_count": len({value for value in translated_local_refs if value}),
        "translation_handle_gain_ratio": _ratio(translated_handle_material_count, material_count),
        "translation_handle_total_count": translated_handle_total_count,
        "translation_broadcast_leak": translation_broadcast_leak,
        "anchor_signature_unique_ratio": _signature_unique_ratio(anchor_counter, material_count),
        "processing_signature_unique_ratio": processing_signature_unique_ratio,
        "processing_signature_entropy": _normalized_entropy(processing_signatures),
        "local_ref_processing_uniqueness": _ratio(len(processing_counter), len(local_ref_counter)),
        "scene_flow_role_uniqueness_ratio": scene_flow_role_uniqueness_ratio,
        "processing_value_variance": processing_value_variance,
        "handle_signature_unique_ratio": _signature_unique_ratio(handle_counter, material_count),
        "translated_signature_unique_ratio": _signature_unique_ratio(translated_counter, material_count),
        "scene_unique_count": len({value for value in scene_values if value}),
        "flow_unique_count": len({value for value in flow_values if value}),
        "role_unique_count": len({value for value in role_values if value}),
        "processing_profile_flatness_score": _processing_profile_flatness_score(
            processing_signature_unique_ratio=processing_signature_unique_ratio,
            scene_flow_role_uniqueness_ratio=scene_flow_role_uniqueness_ratio,
            processing_value_variance=processing_value_variance,
        ),
        "local_alignment_readiness": _local_alignment_readiness(
            material_count=material_count,
            unique_local_ref_count=len(local_ref_counter),
            anchor_signature_unique_ratio=_signature_unique_ratio(anchor_counter, material_count),
            processing_signature_unique_ratio=processing_signature_unique_ratio,
            handle_signature_unique_ratio=_signature_unique_ratio(handle_counter, material_count),
        ),
        "flatten_indicators": _flatten_indicators(
            material_count=material_count,
            source_ref_count=len(source_refs),
            anchor_bundle_ratio=_ratio(anchor_bundle_count, material_count),
            processing_ratio=_ratio(processing_values_count, material_count),
            handle_ratio=_ratio(transformable_handles_count, material_count),
            avg_anchor_density=(sum(anchor_density_values) / len(anchor_density_values)) if anchor_density_values else 0.0,
        ),
    }


def load_materials_by_source(runtime_root: Path, source_ref: str) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    material_dir = runtime_root / "core" / "materials"
    for path in material_dir.glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if str(payload.get("source_ref", "")).strip() == source_ref:
            rows.append(payload)
    return rows


def _ratio(numerator: int, denominator: int) -> float:
    return round((numerator / denominator), 4) if denominator else 0.0


def _signature_unique_ratio(counter: Counter[str], material_count: int) -> float:
    return _ratio(len(counter), material_count)


def _variance(values: Sequence[float]) -> float:
    if len(values) <= 1:
        return 0.0
    return round(statistics.pvariance(values), 4)


def _normalized_entropy(values: Sequence[str]) -> float:
    rows = [value for value in values if value]
    if not rows:
        return 0.0
    counts = Counter(rows)
    total = sum(counts.values())
    if total <= 1 or len(counts) <= 1:
        return 0.0
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log(p, 2)
    max_entropy = math.log(len(counts), 2)
    return round(entropy / max_entropy, 4) if max_entropy > 0 else 0.0


def _processing_profile_flatness_score(
    *,
    processing_signature_unique_ratio: float,
    scene_flow_role_uniqueness_ratio: float,
    processing_value_variance: Dict[str, float],
) -> float:
    d_norm = min(1.0, processing_value_variance.get("D", 0.0) / 0.02)
    i_norm = min(1.0, processing_value_variance.get("I", 0.0) / 0.02)
    s_norm = min(1.0, processing_value_variance.get("S", 0.0) / 0.02)
    richness = (
        processing_signature_unique_ratio * 0.45
        + scene_flow_role_uniqueness_ratio * 0.25
        + d_norm * 0.1
        + i_norm * 0.1
        + s_norm * 0.1
    )
    return round(max(0.0, min(1.0, 1.0 - richness)), 4)


def _flatten_indicators(
    *,
    material_count: int,
    source_ref_count: int,
    anchor_bundle_ratio: float,
    processing_ratio: float,
    handle_ratio: float,
    avg_anchor_density: float,
) -> List[str]:
    rows: List[str] = []
    if material_count > 8 and anchor_bundle_ratio == 0.0:
        rows.append("material_count_high_but_anchor_bundle_absent")
    if material_count > 8 and processing_ratio == 0.0:
        rows.append("material_count_high_but_processing_values_absent")
    if material_count > 8 and handle_ratio == 0.0:
        rows.append("material_count_high_but_transformable_handles_absent")
    if source_ref_count == 1 and material_count > 8:
        rows.append("single_source_ref_spread_over_many_materials")
    if avg_anchor_density == 0.0 and material_count > 1:
        rows.append("localizable_anchor_density_absent")
    return rows


def _local_alignment_readiness(
    *,
    material_count: int,
    unique_local_ref_count: int,
    anchor_signature_unique_ratio: float,
    processing_signature_unique_ratio: float,
    handle_signature_unique_ratio: float,
) -> Dict[str, object]:
    readiness = "low"
    blockers: List[str] = []
    if material_count > 8 and unique_local_ref_count == material_count:
        # local refs exist, so spread is not collapsed into one ref
        pass
    else:
        blockers.append("local_ref_not_discriminative")
    if anchor_signature_unique_ratio < 0.35:
        blockers.append("imported_material_similarity_high")
    if processing_signature_unique_ratio < 0.2:
        blockers.append("processing_profile_too_flat")
    if handle_signature_unique_ratio < 0.9:
        blockers.append("handle_discriminability_low")
    if not blockers:
        readiness = "high"
    elif len(blockers) <= 2:
        readiness = "partial"
    return {
        "level": readiness,
        "blockers": blockers,
    }
