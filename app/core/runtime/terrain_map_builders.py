from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple
import math


SCENE_COLORS = {
    "explanation": "#c58f4c",
    "comparison": "#7c3aed",
    "reflection": "#8f5c2c",
    "evidence": "#0f766e",
    "unknown": "#64748b",
}

def build_fragment_points(fragments: List[object]) -> Tuple[List[Dict[str, object]], Dict[str, Dict[str, object]], List[Dict[str, object]]]:
    by_source: Dict[str, List[object]] = defaultdict(list)
    for fragment in fragments:
        by_source[fragment.source_id].append(fragment)

    source_ids = sorted(by_source)
    points: List[Dict[str, object]] = []
    lookup: Dict[str, Dict[str, object]] = {}
    source_summary: List[Dict[str, object]] = []

    for source_index, source_id in enumerate(source_ids):
        group = sorted(
            by_source[source_id],
            key=lambda row: (
                row.source_range.start if row.source_range.start is not None else -1,
                row.fragment_id,
            ),
        )
        source_summary.append(
            {
                "source_id": source_id,
                "source_ref": group[0].source_path if group else "",
                "source_type": group[0].source_type if group else "unknown",
                "fragment_count": len(group),
            }
        )
        for index, fragment in enumerate(group):
            scene = normalize_scene(str(fragment.scene or "unknown"))
            role = str(fragment.metadata.get("observer_role", ""))
            ambiguity = safe_float(fragment.metadata.get("observer_ambiguity"), 0.5)
            confidence = safe_float(fragment.metadata.get("observer_confidence_numeric"), 0.5)
            x = 120 + source_index * 220 + (scene_offset(scene) * 24) + (float(fragment.D) - 0.5) * 36
            y = 100 + index * 108 + (1.0 - float(fragment.S)) * 26
            point = {
                "fragment_id": fragment.fragment_id,
                "source_id": fragment.source_id,
                "source_ref": fragment.source_path,
                "source_type": fragment.source_type,
                "text": fragment.raw_text,
                "x": round(x, 2),
                "y": round(y, 2),
                "elevation": round(float(fragment.I), 3),
                "stability": round(float(fragment.S), 3),
                "direction": round(float(fragment.D), 3),
                "scene": scene,
                "observer_role": role,
                "observer_ambiguity": round(ambiguity, 3),
                "observer_confidence_numeric": round(confidence, 3),
                "observer_signals": list(fragment.metadata.get("observer_signals", [])),
                "anchors": [
                    {
                        "type": anchor.anchor_type,
                        "key": anchor.key,
                        "label": anchor.label,
                    }
                    for anchor in (fragment.anchors or [])
                ],
            }
            points.append(point)
            lookup[fragment.fragment_id] = point
    return points, lookup, source_summary


def build_terrain_cells(points: List[Dict[str, object]]) -> List[Dict[str, object]]:
    if not points:
        return []
    max_x = max(point["x"] for point in points) + 140
    max_y = max(point["y"] for point in points) + 140
    step = 28
    cells: List[Dict[str, object]] = []
    for gx in range(0, int(max_x), step):
        for gy in range(0, int(max_y), step):
            weights = []
            scene_weight = Counter()
            elevation_sum = 0.0
            stability_sum = 0.0
            fog_sum = 0.0
            for point in points:
                dx = gx - point["x"]
                dy = gy - point["y"]
                distance = math.hypot(dx, dy)
                weight = 1.0 / (1.0 + (distance / 90.0) ** 2)
                if weight < 0.12:
                    continue
                weights.append(weight)
                elevation_sum += point["elevation"] * weight
                stability_sum += point["stability"] * weight
                fog_sum += point["observer_ambiguity"] * weight
                scene_weight[point["scene"]] += weight
            if not weights:
                continue
            total = sum(weights)
            elevation = elevation_sum / total
            stability = stability_sum / total
            fog = fog_sum / total
            dominant_scene = scene_weight.most_common(1)[0][0] if scene_weight else "unknown"
            cells.append(
                {
                    "cell_id": f"terrain_{gx}_{gy}",
                    "x": gx,
                    "y": gy,
                    "elevation": round(elevation, 3),
                    "stability": round(stability, 3),
                    "fog": round(fog, 3),
                    "dominant_scene": dominant_scene,
                    "color": terrain_color(dominant_scene, elevation, fog),
                }
            )
    return cells


def build_contour_lines(cells: List[Dict[str, object]]) -> List[Dict[str, object]]:
    if not cells:
        return []
    thresholds = (0.34, 0.5, 0.66, 0.82)
    lookup = {(row["x"], row["y"]): row for row in cells}
    segments: List[Dict[str, object]] = []
    step = 28
    for row in cells:
        x = row["x"]
        y = row["y"]
        right = lookup.get((x + step, y))
        down = lookup.get((x, y + step))
        for threshold in thresholds:
            if right and crosses_threshold(row["elevation"], right["elevation"], threshold):
                segments.append(
                    {
                        "line_id": f"contour_h_{x}_{y}_{int(threshold*100)}",
                        "level": threshold,
                        "path": [
                            {"x": x + step / 2, "y": y},
                            {"x": x + step / 2, "y": y + step},
                        ],
                    }
                )
            if down and crosses_threshold(row["elevation"], down["elevation"], threshold):
                segments.append(
                    {
                        "line_id": f"contour_v_{x}_{y}_{int(threshold*100)}",
                        "level": threshold,
                        "path": [
                            {"x": x, "y": y + step / 2},
                            {"x": x + step, "y": y + step / 2},
                        ],
                    }
                )
    return segments


def build_imported_material_points(
    materials: List[Dict[str, object]],
    fragment_lookup: Dict[str, Dict[str, object]],
    source_offset: int,
) -> List[Dict[str, object]]:
    grouped: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for material in materials:
        source_ref = str(material.get("source_ref", ""))
        metadata = material.get("metadata", {})
        fragment_id = str(metadata.get("fragment_id", ""))
        if not source_ref.startswith("processor_compare/"):
            continue
        if fragment_id and fragment_id in fragment_lookup:
            continue
        grouped[source_ref].append(material)

    points: List[Dict[str, object]] = []
    for source_index, source_ref in enumerate(sorted(grouped), start=source_offset):
        rows = grouped[source_ref]
        for index, material in enumerate(rows):
            metadata = material.get("metadata", {})
            scene = normalize_scene(str(metadata.get("scene", "unknown")))
            direction = safe_float(metadata.get("D"), 0.5)
            stability = safe_float(metadata.get("S"), 0.5)
            elevation = safe_float(metadata.get("I"), 0.5)
            x = 120 + source_index * 220 + (scene_offset(scene) * 24) + (direction - 0.5) * 36
            y = 100 + index * 24 + (1.0 - stability) * 26
            point = {
                "fragment_id": f"matpt_{material['material_id']}",
                "source_id": material.get("family_id", source_ref),
                "source_ref": source_ref,
                "source_type": material.get("source_type", "review"),
                "text": material.get("raw_payload", ""),
                "x": round(x, 2),
                "y": round(y, 2),
                "elevation": round(elevation, 3),
                "stability": round(stability, 3),
                "direction": round(direction, 3),
                "scene": scene,
                "observer_role": str(metadata.get("fragment_metadata", {}).get("observer_role", "")),
                "observer_ambiguity": round(safe_float(metadata.get("fragment_metadata", {}).get("observer_ambiguity"), 0.35), 3),
                "observer_confidence_numeric": round(safe_float(metadata.get("fragment_metadata", {}).get("observer_confidence_numeric"), 0.5), 3),
                "observer_signals": list(metadata.get("fragment_metadata", {}).get("observer_signals", [])),
                "anchors": [
                    {
                        "type": str(anchor.get("type", "")),
                        "key": str(anchor.get("value", "")),
                        "label": str(anchor.get("value", "")),
                    }
                    for anchor in metadata.get("anchors", [])
                    if str(anchor.get("value", "")).strip()
                ],
                "short_label": str(metadata.get("short_label", "")),
                "source_family": str(material.get("family_id", "")),
            }
            points.append(point)
    return points


def build_material_features(
    materials: List[Dict[str, object]],
    fragment_lookup: Dict[str, Dict[str, object]],
    imported_material_points: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    point_lookup = {row["fragment_id"]: row for row in imported_material_points}
    rows: List[Dict[str, object]] = []
    for index, material in enumerate(materials):
        metadata = material.get("metadata", {})
        fragment_id = metadata.get("fragment_id", "")
        fragment_point = fragment_lookup.get(fragment_id)
        imported_point = point_lookup.get(f"matpt_{material['material_id']}")
        if fragment_point:
            base_x = fragment_point["x"]
            base_y = fragment_point["y"]
        elif imported_point:
            base_x = imported_point["x"]
            base_y = imported_point["y"]
        else:
            base_x = 80 + (index % 8) * 84
            base_y = 120 + (index // 8) * 64
        observer_role = metadata.get("fragment_metadata", {}).get("observer_role", "")
        observer_ambiguity = safe_float(metadata.get("fragment_metadata", {}).get("observer_ambiguity"), 0.5)
        observer_signals = list(metadata.get("fragment_metadata", {}).get("observer_signals", []))
        rows.append(
            {
                "material_id": material["material_id"],
                "label": material_label(material),
                "x": round(base_x + ((index % 3) - 1) * 10, 2),
                "y": round(base_y + (((index // 3) % 3) - 1) * 10, 2),
                "source_ref": material.get("source_ref", ""),
                "observer_role": observer_role,
                "observer_ambiguity": round(observer_ambiguity, 3),
                "observer_signals": observer_signals,
                "scene": normalize_scene(str(metadata.get("scene", "unknown"))),
                "elevation": round(safe_float(metadata.get("I"), 0.5), 3),
                "stability": round(safe_float(metadata.get("S"), 0.5), 3),
                "source_family": material.get("family_id", ""),
                "short_label": str(metadata.get("short_label", "")),
                "anchors": [
                    str(anchor.get("value", "")).strip()
                    for anchor in metadata.get("anchors", [])
                    if str(anchor.get("value", "")).strip()
                ],
            }
        )
    return rows


def build_water_flows(points: List[Dict[str, object]]) -> List[Dict[str, object]]:
    flows: List[Dict[str, object]] = []
    seen = set()
    for index, left in enumerate(points):
        left_anchor_keys = {anchor["key"] for anchor in left["anchors"]}
        for right in points[index + 1 :]:
            shared = sorted(left_anchor_keys & {anchor["key"] for anchor in right["anchors"]})
            if not shared:
                continue
            if left["observer_ambiguity"] > 0.5 or right["observer_ambiguity"] > 0.5:
                continue
            pair = tuple(sorted((left["fragment_id"], right["fragment_id"])))
            if pair in seen:
                continue
            seen.add(pair)
            flows.append(
                {
                    "flow_id": f"water_{left['fragment_id'][-4:]}_{right['fragment_id'][-4:]}",
                    "from_fragment_id": left["fragment_id"],
                    "to_fragment_id": right["fragment_id"],
                    "path": [
                        {"x": left["x"], "y": left["y"]},
                        {"x": (left["x"] + right["x"]) / 2, "y": (left["y"] + right["y"]) / 2},
                        {"x": right["x"], "y": right["y"]},
                    ],
                    "anchor_family": shared[0].split(".")[0] if shared else "anchor",
                    "strength": round(min(1.0, 0.32 * len(shared) + 0.18 * (1.0 - abs(left["elevation"] - right["elevation"]))), 3),
                    "shared_anchor_keys": shared[:4],
                }
            )
    flows.sort(key=lambda row: row["strength"], reverse=True)
    return flows[:18]


def build_wind_fields(points: List[Dict[str, object]]) -> List[Dict[str, object]]:
    winds: List[Dict[str, object]] = []
    for point in points:
        for signal in point["observer_signals"]:
            winds.append(
                {
                    "wind_id": f"wind_{point['fragment_id']}_{signal}",
                    "fragment_id": point["fragment_id"],
                    "x": point["x"],
                    "y": point["y"],
                    "direction": round((point["direction"] - 0.5) * 180, 1),
                    "strength": round(0.55 + point["observer_ambiguity"] * 0.35, 3),
                    "reason_type": signal,
                }
            )
        if point["scene"] == "comparison" or point["observer_role"] == "contrast":
            winds.append(
                {
                    "wind_id": f"wind_{point['fragment_id']}_contrast",
                    "fragment_id": point["fragment_id"],
                    "x": point["x"],
                    "y": point["y"],
                    "direction": round((point["direction"] - 0.5) * 180, 1),
                    "strength": 0.52,
                    "reason_type": "contrast_flow",
                }
            )
    return winds[:24]


def build_fault_lines(points: List[Dict[str, object]]) -> List[Dict[str, object]]:
    faults = []
    for point in points:
        if point["observer_role"] == "problem" or point["observer_signals"]:
            faults.append(
                {
                    "fault_id": f"fault_{point['fragment_id']}",
                    "fragment_id": point["fragment_id"],
                    "x": point["x"],
                    "y": point["y"],
                    "severity": round(0.4 + point["observer_ambiguity"] * 0.6, 3),
                    "signals": point["observer_signals"],
                }
            )
    return faults


def scene_offset(scene: str) -> float:
    return {
        "explanation": 0.0,
        "comparison": 0.9,
        "reflection": -0.6,
        "evidence": 0.45,
    }.get(scene, 0.0)


def normalize_scene(scene: str) -> str:
    value = (scene or "").strip().lower()
    if value in {"review", "explanation", "summary"}:
        return "explanation"
    if value in {"memo", "reflection", "journal"}:
        return "reflection"
    if value in {"paper", "evidence", "reference"}:
        return "evidence"
    if value in {"compare", "comparison", "contrast"}:
        return "comparison"
    return scene if scene in SCENE_COLORS else "unknown"


def safe_float(value: object, fallback: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return fallback


def terrain_color(scene: str, elevation: float, fog: float) -> str:
    base = SCENE_COLORS.get(scene, SCENE_COLORS["unknown"])
    return f"{base}:{round(elevation, 3)}:{round(fog, 3)}"


def crosses_threshold(left: float, right: float, threshold: float) -> bool:
    return (left < threshold <= right) or (right < threshold <= left)

def material_label(material: Dict[str, object]) -> str:
    source_ref = str(material.get("source_ref", ""))
    if source_ref:
        return Path(source_ref).name
    return material["material_id"][-8:]
