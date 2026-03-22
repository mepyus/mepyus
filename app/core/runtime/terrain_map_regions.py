from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Dict, List
import math


VISUAL_STOP_TERMS = {
    "그래서",
    "이렇게",
    "이러한",
    "문제를",
    "있습니다",
    "것이다",
    "가지고",
    "같은",
    "대한",
    "위해서",
    "때문에",
    "있다",
    "그리고",
    "그러나",
    "것처럼",
    "왜냐하면",
}


def build_regions(
    local_spaces: List[Dict[str, object]],
    cells: List[Dict[str, object]],
    material_features: List[Dict[str, object]],
    bridges: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    cell_lookup = {row["cell_id"]: row for row in cells}
    material_lookup = {row["material_id"]: row for row in material_features}
    regions: List[Dict[str, object]] = []
    for local_space in local_spaces:
        region_materials: List[Dict[str, object]] = []
        for cell_id in local_space.get("cell_refs", []):
            cell = cell_lookup.get(cell_id, {})
            for material_id in cell.get("material_refs", []):
                material = material_lookup.get(material_id)
                if material:
                    region_materials.append(material)
        local_space_rep_anchors = list(local_space.get("representative_anchors", []))
        if region_materials:
            center_x = sum(row["x"] for row in region_materials) / len(region_materials)
            center_y = sum(row["y"] for row in region_materials) / len(region_materials)
            avg_elevation = sum(row["elevation"] for row in region_materials) / len(region_materials)
            avg_fog = sum(row["observer_ambiguity"] for row in region_materials) / len(region_materials)
            scene = Counter(row["scene"] for row in region_materials).most_common(1)[0][0]
            role_counts = Counter(row["observer_role"] for row in region_materials if row["observer_role"])
            source_counts = Counter(Path(str(row["source_ref"])).name for row in region_materials if row["source_ref"])
            family_counts = Counter(str(row.get("source_family", "")).strip() for row in region_materials if str(row.get("source_family", "")).strip())
            anchor_counts = Counter()
            for row in region_materials:
                for anchor in row.get("anchors", []):
                    if len(anchor) < 3 or anchor in VISUAL_STOP_TERMS:
                        continue
                    anchor_counts[anchor] += 1
            min_x = min(row["x"] for row in region_materials)
            max_x = max(row["x"] for row in region_materials)
            min_y = min(row["y"] for row in region_materials)
            max_y = max(row["y"] for row in region_materials)
            landmarks = _select_region_landmarks(region_materials)
        else:
            center_x = 0.0
            center_y = 0.0
            avg_elevation = 0.0
            avg_fog = 0.0
            scene = "unknown"
            role_counts = Counter()
            source_counts = Counter()
            family_counts = Counter()
            anchor_counts = Counter()
            min_x = max_x = min_y = max_y = 0.0
            landmarks = []
        region_label = str(local_space.get("source_label", "")).strip() or (
            family_counts.most_common(1)[0][0] if family_counts else (source_counts.most_common(1)[0][0] if source_counts else local_space["local_space_id"])
        )
        anchor_summary = [str(row.get("display_label", "")).strip() for row in local_space_rep_anchors if str(row.get("display_label", "")).strip()]
        if not anchor_summary:
            anchor_summary = [name for name, _count in anchor_counts.most_common(4)]
        regions.append(
            {
                "local_space_id": local_space["local_space_id"],
                "label": region_label,
                "cell_refs": list(local_space.get("cell_refs", [])),
                "bridge_trace_refs": list(local_space.get("bridge_trace_refs", [])),
                "state": local_space.get("state", "forming"),
                "x": round(center_x, 2),
                "y": round(center_y, 2),
                "elevation": round(avg_elevation, 3),
                "fog": round(avg_fog, 3),
                "dominant_scene": scene,
                "dominant_role": role_counts.most_common(1)[0][0] if role_counts else "",
                "material_count": len(region_materials),
                "anchor_summary": anchor_summary[:4],
                "landmarks": landmarks,
                "min_x": round(min_x, 2),
                "max_x": round(max_x, 2),
                "min_y": round(min_y, 2),
                "max_y": round(max_y, 2),
                "width": round(max(72.0, (max_x - min_x) + 54.0), 2) if region_materials else 72.0,
                "height": round(max(48.0, (max_y - min_y) + 42.0), 2) if region_materials else 48.0,
            }
        )
    return regions


def build_region_flows(
    regions: List[Dict[str, object]],
    bridges: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    region_lookup = {row["local_space_id"]: row for row in regions}
    flows: List[Dict[str, object]] = []
    for bridge in bridges:
        left = region_lookup.get(bridge.get("from_local_space_id", ""))
        right = region_lookup.get(bridge.get("to_local_space_id", ""))
        if not left or not right:
            continue
        note = str(bridge.get("note", ""))
        strength = 0.55
        anchors: List[str] = [str(row.get("display_label", "")).strip() for row in bridge.get("shared_anchors", []) if str(row.get("display_label", "")).strip()]
        if anchors:
            size_factor = min(0.18, math.log1p(max(1, min(left["material_count"], right["material_count"]))) * 0.03)
            fog_penalty = ((left["fog"] + right["fog"]) / 2.0) * 0.12
            strength = min(0.95, max(0.42, 0.34 + len(anchors) * 0.08 + size_factor - fog_penalty))
        elif "soft doc proximity:" in note:
            continue
        flows.append(
            {
                "bridge_id": bridge.get("bridge_id", ""),
                "from_local_space_id": left["local_space_id"],
                "to_local_space_id": right["local_space_id"],
                "path": [
                    {"x": left["x"], "y": left["y"]},
                    {"x": round((left["x"] + right["x"]) / 2, 2), "y": round((left["y"] + right["y"]) / 2 - 32, 2)},
                    {"x": right["x"], "y": right["y"]},
                ],
                "strength": round(strength, 3),
                "note": note,
                "anchor_hint_count": len(anchors),
                "anchor_hints": anchors[:4],
                "from_label": left["label"],
                "to_label": right["label"],
            }
        )
    return flows


def _select_region_landmarks(region_materials: List[Dict[str, object]]) -> List[Dict[str, object]]:
    scored = []
    for row in region_materials:
        score = (
            float(row.get("elevation", 0.5)) * 0.45
            + (1.0 - float(row.get("observer_ambiguity", 0.5))) * 0.25
            + min(0.3, len(row.get("anchors", [])) * 0.04)
            + (0.15 if row.get("observer_signals") else 0.0)
        )
        scored.append((score, row))
    scored.sort(key=lambda item: item[0], reverse=True)
    landmarks: List[Dict[str, object]] = []
    seen_labels = set()
    for _score, row in scored:
        label = str(row.get("short_label") or row.get("label") or "").strip()
        if not label or label in seen_labels:
            continue
        seen_labels.add(label)
        landmarks.append(
            {
                "material_id": row["material_id"],
                "x": row["x"],
                "y": row["y"],
                "label": label[:28],
                "scene": row["scene"],
                "observer_role": row.get("observer_role", ""),
            }
        )
        if len(landmarks) >= 4:
            break
    return landmarks
