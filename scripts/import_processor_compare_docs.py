#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.formation_service import FormationService
from app.core.models.entities import PressureAxis, SupportRef
from app.runtime.graph_view import build_space_graph_view_data
from app.runtime.live_input import ingest_live_input
from app.runtime.terrain_map import build_terrain_map_data


DEFAULT_SOURCE_DIR = REPO_ROOT / "app" / "work" / "processor_compare" / "inputs" / "source_docs"
BRIDGE_STOP_TERMS = {
    "그래서",
    "이렇게",
    "이러한",
    "문제를",
    "있습니다",
    "것이다",
    "가지",
    "같은",
    "대한",
    "위해서",
    "때문에",
    "있다",
}


def main(argv: List[str]) -> int:
    runtime_root = Path(argv[1]).resolve() if len(argv) >= 2 else (REPO_ROOT / "runtime")
    source_dir = Path(argv[2]).resolve() if len(argv) >= 3 else DEFAULT_SOURCE_DIR
    service = FormationService(runtime_root)

    source_paths = sorted(source_dir.glob("doc_*.txt"))
    if not source_paths:
        print(json.dumps({"error": f"no source docs found in {source_dir}"}, ensure_ascii=False, indent=2))
        return 1

    imported_docs: List[Dict[str, object]] = []
    local_space_rows: List[Dict[str, object]] = []

    for path in source_paths:
        doc_id = path.stem
        raw_payload = path.read_text(encoding="utf-8").strip()
        if not raw_payload:
            continue
        source_type = _source_type_for_doc(doc_id)
        source_ref = f"processor_compare/{path.name}"
        ingest_result = ingest_live_input(
            runtime_root,
            {
                "raw_payload": raw_payload,
                "source_type": source_type,
                "source_ref": source_ref,
                "session_id": "processor-compare-doc-import-20260321",
                "actor_id": "replica_user",
                "family_id": doc_id,
            },
        )
        local_space = _form_doc_local_space(service, doc_id, ingest_result)
        imported_docs.append(
            {
                "doc_id": doc_id,
                "source_ref": source_ref,
                "source_type": source_type,
                "material_count": ingest_result["material_count"],
                "trace_count": ingest_result["trace_count"],
                "dust_count": ingest_result["dust_count"],
                "material_ids": ingest_result["material_ids"],
                "trace_ids": ingest_result["trace_ids"],
                "seed_ids": ingest_result["seed_ids"],
                "cell_id": local_space["cell_id"],
                "local_space_id": local_space["local_space_id"],
            }
        )
        local_space_rows.append(local_space)

    bridge_rows = _register_doc_bridges(service, imported_docs)
    graph_data = build_space_graph_view_data(runtime_root)
    terrain_data = build_terrain_map_data(runtime_root)

    report = {
        "runtime_root": str(runtime_root),
        "source_dir": str(source_dir),
        "doc_count": len(imported_docs),
        "imported_docs": imported_docs,
        "bridge_count": len(bridge_rows),
        "bridges": bridge_rows,
        "graph_summary": graph_data["summary"],
        "terrain_summary": terrain_data["summary"],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def _source_type_for_doc(doc_id: str) -> str:
    if doc_id == "doc_009":
        return "memo"
    if doc_id in {"doc_007", "doc_008"}:
        return "paper"
    return "review"


def _form_doc_local_space(service: FormationService, doc_id: str, ingest_result: Dict[str, object]) -> Dict[str, str]:
    material_ids = list(ingest_result.get("material_ids", []))
    trace_ids = list(ingest_result.get("trace_ids", []))
    seed_ids = list(ingest_result.get("seed_ids", []))

    axes = _doc_pressure_axes(service, material_ids)
    pressure = service.create_pressure_profile(
        axes=axes,
        support_refs=tuple(
            SupportRef(ref_kind="material", ref_id=material_id, note="doc_import")
            for material_id in material_ids[:4]
        ),
    )
    cell = service.create_space_cell_candidate(
        material_refs=material_ids,
        trace_refs=trace_ids,
        seed_refs=seed_ids,
        pressure_profile_id=pressure.profile_id,
        interior_refs=material_ids[:6],
        exterior_refs=[],
        cohesion_note=f"{doc_id} imported from processor_compare source_docs",
    )
    local_space = service.form_local_space([cell.cell_id], pressure_profile_id=pressure.profile_id)
    return {
        "doc_id": doc_id,
        "pressure_profile_id": pressure.profile_id,
        "cell_id": cell.cell_id,
        "local_space_id": local_space.local_space_id,
    }


def _doc_pressure_axes(service: FormationService, material_ids: List[str]) -> Tuple[PressureAxis, ...]:
    values = {"D": [], "I": [], "S": []}
    for material_id in material_ids:
        record = service.materials.get(material_id) or {}
        metadata = record.get("metadata", {})
        for axis in ("D", "I", "S"):
            try:
                values[axis].append(float(metadata.get(axis, 0.5)))
            except (TypeError, ValueError):
                pass
    return (
        PressureAxis(axis="doc_direction", strength_hint=_avg(values["D"], 0.5)),
        PressureAxis(axis="doc_intensity", strength_hint=_avg(values["I"], 0.5)),
        PressureAxis(axis="doc_stability", strength_hint=_avg(values["S"], 0.5)),
    )


def _register_doc_bridges(service: FormationService, imported_docs: List[Dict[str, object]]) -> List[Dict[str, object]]:
    anchor_doc_freq: Dict[str, set] = defaultdict(set)
    doc_anchor_keys: Dict[str, set] = defaultdict(set)
    doc_stats: Dict[str, Tuple[float, float, float]] = {}
    for row in imported_docs:
        doc_id = str(row["doc_id"])
        d_vals: List[float] = []
        i_vals: List[float] = []
        s_vals: List[float] = []
        for material_id in row["material_ids"]:
            record = service.materials.get(material_id) or {}
            metadata = record.get("metadata", {})
            d_vals.append(_safe_float(metadata.get("D"), 0.5))
            i_vals.append(_safe_float(metadata.get("I"), 0.5))
            s_vals.append(_safe_float(metadata.get("S"), 0.5))
            for anchor in metadata.get("anchors", []):
                key = str(anchor.get("value", "")).strip()
                if not key or len(key) < 3 or key in BRIDGE_STOP_TERMS:
                    continue
                doc_anchor_keys[doc_id].add(key)
                anchor_doc_freq[key].add(doc_id)
        doc_stats[doc_id] = (_avg(d_vals, 0.5), _avg(i_vals, 0.5), _avg(s_vals, 0.5))

    bridges: List[Dict[str, object]] = []
    scanned_pairs = set()
    doc_lookup = {str(row["doc_id"]): row for row in imported_docs}
    candidate_rows: List[Tuple[float, str, str, List[str]]] = []
    for left_id, left_keys in doc_anchor_keys.items():
        for right_id, right_keys in doc_anchor_keys.items():
            if left_id >= right_id:
                continue
            pair = (left_id, right_id)
            if pair in scanned_pairs:
                continue
            scanned_pairs.add(pair)
            shared_keys = sorted(left_keys & right_keys)
            if not shared_keys:
                continue
            weighted_anchor_score = sum(
                1.0 / max(1, len(anchor_doc_freq[key]))
                for key in shared_keys
                if len(anchor_doc_freq[key]) <= 3
            )
            left_stats = doc_stats.get(left_id, (0.5, 0.5, 0.5))
            right_stats = doc_stats.get(right_id, (0.5, 0.5, 0.5))
            pressure_similarity = 1.0 - (
                abs(left_stats[0] - right_stats[0])
                + abs(left_stats[1] - right_stats[1])
                + abs(left_stats[2] - right_stats[2])
            ) / 3.0
            soft_score = weighted_anchor_score + pressure_similarity * 1.2
            if soft_score < 2.2:
                continue
            candidate_rows.append((soft_score, left_id, right_id, shared_keys))

    candidate_rows.sort(reverse=True)
    accepted_docs: Dict[str, int] = defaultdict(int)
    accepted_pairs = set()
    for soft_score, left_id, right_id, shared_keys in candidate_rows:
        if accepted_docs[left_id] >= 2 or accepted_docs[right_id] >= 2:
            continue
        pair = (left_id, right_id)
        if pair in accepted_pairs:
            continue
        accepted_pairs.add(pair)
        left_space = doc_lookup[left_id]["local_space_id"]
        right_space = doc_lookup[right_id]["local_space_id"]
        bridge = service.register_bridge_trace(
            from_local_space_id=left_space,
            to_local_space_id=right_space,
            trace_refs=tuple(doc_lookup[left_id]["trace_ids"][:2] + doc_lookup[right_id]["trace_ids"][:2]),
            note=f"soft doc proximity: {', '.join(shared_keys[:4])}",
        )
        accepted_docs[left_id] += 1
        accepted_docs[right_id] += 1
        bridges.append(
            {
                "from_doc_id": left_id,
                "to_doc_id": right_id,
                "bridge_id": bridge.bridge_id,
                "from_local_space_id": left_space,
                "to_local_space_id": right_space,
                "shared_anchor_count": len(shared_keys),
                "shared_anchor_keys": shared_keys[:6],
                "soft_score": round(soft_score, 3),
                "state": bridge.state.value,
            }
        )
    return bridges


def _avg(values: List[float], fallback: float) -> float:
    if not values:
        return fallback
    return round(sum(values) / len(values), 4)


def _safe_float(value: object, fallback: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return fallback


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
