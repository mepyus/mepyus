from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple
from uuid import uuid4

from app.core.formation_service import FormationService
from app.models.entities import PressureAxis, SupportRef
from app.runtime.connection_engine import (
    build_relation_profile,
    edge_reasons_for_profile,
    edge_type_for_profile,
    event_type_for_edge,
    normalize_anchor_list,
)
from app.runtime.inputter import build_dust_inputs_from_source
from app.runtime.labeler import LabeledDust, label_dust_inputs


SOURCE_ROLE_MAP = {
    "memo": "memo_material",
    "paper": "paper_material",
    "review": "review_material",
    "code": "code_material",
    "log": "log_material",
    "bullet": "bullet_material",
}

MAX_CANDIDATES_PER_DUST = 4


def ingest_live_input(runtime_root: Path, payload: Dict[str, str]) -> Dict[str, object]:
    raw_payload = str(payload.get("raw_payload", "")).strip()
    if not raw_payload:
        raise ValueError("raw_payload is required")

    source_type = _normalized_source_type(str(payload.get("source_type", "memo")))
    source_ref = str(payload.get("source_ref", "")).strip() or _default_source_ref(source_type)
    session_id = str(payload.get("session_id", "")).strip() or _default_session_id()
    actor_id = str(payload.get("actor_id", "")).strip() or "local_viewer_user"
    family_id = str(payload.get("family_id", "")).strip() or None
    created_at = datetime.utcnow().isoformat() + "Z"
    source_id = "src_%s" % uuid4().hex[:12]

    service = FormationService(runtime_root)
    prior_materials = service.materials.read_all()

    dust_inputs = build_dust_inputs_from_source(
        source_id=source_id,
        source_type=source_type,
        source_ref=source_ref,
        raw_payload=raw_payload,
        created_at=created_at,
    )
    labeled_dusts = label_dust_inputs(dust_inputs)
    if not labeled_dusts:
        raise ValueError("no dust units produced")

    material_rows: List[Tuple[dict, LabeledDust]] = []
    material_ids: List[str] = []
    trace_ids: List[str] = []
    pressure_profile_ids: List[str] = []
    seed_ids: List[str] = []
    edge_events: List[Dict[str, object]] = []

    for labeled in labeled_dusts:
        material = service.ingest_material_with_role(
            raw_payload=labeled.text,
            actor_id=actor_id,
            session_id=session_id,
            project_id="vectorfl-next",
            source_type=source_type,
            source_ref=source_ref,
            formation_role=SOURCE_ROLE_MAP.get(source_type, "memo_material"),
            family_id=family_id,
            lineage_refs=tuple(labeled.siblings),
        )
        persisted = service.materials.get(material.material_id) or {}
        metadata = dict(persisted.get("metadata", {}))
        metadata.update(
            {
                "source_origin_id": labeled.origin_id,
                "dust_input_id": labeled.dust_id,
                "D": labeled.D,
                "I": labeled.I,
                "S": labeled.S,
                "scene": labeled.scene,
                "flow": labeled.flow,
                "anchors": [anchor.__dict__ for anchor in labeled.anchors],
                "time_in": labeled.time_in,
                "last_seen": labeled.last_seen,
                "recurrence_count": labeled.recurrence_count,
                "short_label": labeled.short_label,
            }
        )
        persisted["metadata"] = metadata
        service.materials.put(material.material_id, persisted)
        material_rows.append((persisted, labeled))
        material_ids.append(material.material_id)

    relation_candidates = _build_relation_candidates(prior_materials, material_rows)
    for candidate in relation_candidates:
        support_refs = [
            SupportRef(ref_kind="material", ref_id=candidate["left_material_id"], note="dust_emit"),
            SupportRef(ref_kind="material", ref_id=candidate["right_material_id"], note="candidate_scan"),
            SupportRef(ref_kind="scene", ref_id=candidate["scene"], note="scene_match" if candidate["same_scene"] else "scene_mismatch"),
            SupportRef(ref_kind="flow", ref_id=candidate["flow"], note="flow_match" if candidate["same_flow"] else "flow_partial"),
        ]
        for anchor in candidate["shared_anchors"][:2]:
            support_refs.append(
                SupportRef(ref_kind=anchor["type"], ref_id=anchor["value"], note="anchor_overlap")
            )

        trace = service.register_trace(
            material_refs=[candidate["left_material_id"], candidate["right_material_id"]],
            evidence_kind="dust_candidate_scan",
            support_refs=support_refs,
            note=candidate["edge_type"],
        )
        pressure = service.create_pressure_profile(
            axes=[
                PressureAxis(axis="relation_strength", strength_hint=candidate["score"]),
                PressureAxis(axis="direction_pressure", strength_hint=candidate["direction_strength"]),
            ],
            support_refs=[
                SupportRef(ref_kind="trace", ref_id=trace.trace_id, note=candidate["edge_type"]),
                SupportRef(ref_kind="material", ref_id=candidate["left_material_id"], note="left"),
                SupportRef(ref_kind="material", ref_id=candidate["right_material_id"], note="right"),
            ],
        )
        seed = service.create_point_seed_candidate(
            material_refs=[candidate["left_material_id"], candidate["right_material_id"]],
            trace_refs=[trace.trace_id],
            pressure_profile_id=pressure.profile_id,
            reentering=False,
        )
        service._append_event(
            _event_type_for_edge(candidate["edge_type"]),
            "material",
            candidate["left_material_id"],
            {
                "target_material_id": candidate["right_material_id"],
                "edge_type": candidate["edge_type"],
                "score": candidate["score"],
                "reasons": candidate["reasons"],
            },
        )
        if candidate["bridge_candidate"]:
            service._append_event(
                "bridge_candidate_found",
                "material",
                candidate["left_material_id"],
                {
                    "target_material_id": candidate["right_material_id"],
                    "bridge_reason": candidate["reasons"]["anchor_reason"],
                },
            )

        trace_ids.append(trace.trace_id)
        pressure_profile_ids.append(pressure.profile_id)
        seed_ids.append(seed.seed_id)
        edge_events.append(
            {
                "left_material_id": candidate["left_material_id"],
                "right_material_id": candidate["right_material_id"],
                "edge_type": candidate["edge_type"],
                "score": candidate["score"],
            }
        )

    return {
        "source_ref": source_ref,
        "source_type": source_type,
        "source_id": source_id,
        "material_ids": material_ids,
        "trace_ids": trace_ids,
        "pressure_profile_ids": pressure_profile_ids,
        "seed_ids": seed_ids,
        "cell_ids": [],
        "local_space_ids": [],
        "bridge_ids": [],
        "material_count": len(material_ids),
        "trace_count": len(trace_ids),
        "edge_event_count": len(edge_events),
        "dust_count": len(material_rows),
        "edge_events": edge_events[:24],
    }


def _build_relation_candidates(
    prior_materials: Sequence[Dict[str, object]],
    material_rows: Sequence[Tuple[dict, LabeledDust]],
) -> List[Dict[str, object]]:
    current_records = [row[0] for row in material_rows]
    emitted_materials = current_records + [row for row in prior_materials if _has_dust_metadata(row)]
    candidates: List[Dict[str, object]] = []

    for index, record in enumerate(current_records):
        scored: List[Tuple[float, Dict[str, object]]] = []
        for other in emitted_materials:
            if other["material_id"] == record["material_id"]:
                continue
            profile = _relation_profile(record, other)
            if profile is None:
                continue
            scored.append((profile["score"], profile))
        scored.sort(key=lambda row: row[0], reverse=True)
        for _, profile in scored[:MAX_CANDIDATES_PER_DUST]:
            candidates.append(profile)
    return candidates


def _relation_profile(left: Dict[str, object], right: Dict[str, object]) -> Optional[Dict[str, object]]:
    left_meta = dict(left.get("metadata", {}))
    right_meta = dict(right.get("metadata", {}))
    if not left_meta or not right_meta:
        return None

    left_anchors = {(anchor["type"], anchor["value"]) for anchor in normalize_anchor_list(left_meta.get("anchors", []))}
    right_anchors = {(anchor["type"], anchor["value"]) for anchor in normalize_anchor_list(right_meta.get("anchors", []))}
    shared_anchors = [
        {"type": anchor_type, "value": anchor_value}
        for anchor_type, anchor_value in sorted(left_anchors & right_anchors)
    ]
    same_origin = left.get("source_ref") == right.get("source_ref")
    same_scene = left_meta.get("scene") == right_meta.get("scene")
    same_flow = left_meta.get("flow") == right_meta.get("flow")

    if not same_origin and not shared_anchors:
        return None

    profile = build_relation_profile(
        {
            "anchors": normalize_anchor_list(left_meta.get("anchors", [])),
            "scene": str(left_meta.get("scene", "unknown")),
            "flow": str(left_meta.get("flow", "unknown")),
            "D": float(left_meta.get("D", 0.5)),
            "time_in": str(left_meta.get("time_in", "")),
        },
        {
            "anchors": normalize_anchor_list(right_meta.get("anchors", [])),
            "scene": str(right_meta.get("scene", "unknown")),
            "flow": str(right_meta.get("flow", "unknown")),
            "D": float(right_meta.get("D", 0.5)),
            "time_in": str(right_meta.get("time_in", "")),
        },
    )
    edge_type, score = edge_type_for_profile(profile)
    if edge_type is None:
        return None

    reasons = edge_reasons_for_profile(profile)
    reasons["time_reason"] = "same recent session" if profile["time_score"] >= 1.0 else "loose time proximity"
    return {
        "left_material_id": left["material_id"],
        "right_material_id": right["material_id"],
        "shared_anchors": shared_anchors,
        "same_scene": same_scene,
        "same_flow": same_flow,
        "scene": str(left_meta.get("scene", "unknown")),
        "flow": str(left_meta.get("flow", "unknown")),
        "edge_type": edge_type,
        "score": round(score, 4),
        "direction_strength": round(
            max(profile["direction_same_score"], profile["direction_opposition_score"], 0.5),
            4,
        ),
        "bridge_candidate": len(shared_anchors) >= 2 and not same_origin,
        "reasons": reasons,
    }


def _has_dust_metadata(material: Dict[str, object]) -> bool:
    metadata = dict(material.get("metadata", {}))
    return "scene" in metadata and "flow" in metadata and "anchors" in metadata


def _normalized_source_type(source_type: str) -> str:
    normalized = source_type.strip().lower()
    if normalized in {"memo", "paper", "review", "code", "log", "bullet"}:
        return normalized
    return "memo"


def _default_source_ref(source_type: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    return "%s-%s" % (source_type, timestamp)


def _default_session_id() -> str:
    return "live-session-%s" % datetime.utcnow().strftime("%Y%m%d")
