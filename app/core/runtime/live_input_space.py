from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Set
import json

from app.core.formation_service import FormationService
from app.core.runtime.runtime_space_anchor_sync import sync_local_space_anchor_metadata
from app.core.runtime.runtime_view_refresh import refresh_runtime_views
from app.core.runtime.review_output_surface import assemble_promotion_review_surface
from app.core.runtime.review_output_surface import assemble_cross_path_review_surface
from app.core.runtime.approval_policies import (
    evaluate_bridge_mode_approval_policy,
    evaluate_canonical_approval_status_policy,
    evaluate_canonical_review_decision_policy,
    evaluate_canonical_anchor_approval_policy,
)
from app.core.runtime.review_policies import (
    evaluate_canonicalization_family_policy,
    evaluate_direct_overlap_aggregate_policy,
    evaluate_direct_overlap_family_policy,
    evaluate_cross_path_overlap_policy,
    evaluate_promotion_review_policy,
    evaluate_review_lifecycle_policy,
    evaluate_space_entry_policy,
)
from app.core.runtime.approval_policy_types import (
    BridgeModeApprovalContext,
    CanonicalApprovalStatusContext,
    CanonicalReviewDecisionContext,
    CanonicalAnchorApprovalContext,
)
from app.core.runtime.review_policy_types import (
    CanonicalizationPolicyContext,
    CrossPathPolicyContext,
    LifecyclePolicyContext,
    DirectOverlapAggregatePolicyContext,
    DirectOverlapFamilyPolicyContext,
    PromotionPolicyContext,
    PromotionPolicyResult,
    PromotionReviewAssembly,
    ReviewTimestamp,
    SpaceEntryPolicyContext,
)
from app.models.entities import PressureAxis, SupportRef
import re


def form_live_input_local_space(runtime_root: Path, ingest_result: Dict[str, object], *, family_id: str = "") -> Dict[str, object]:
    service = FormationService(runtime_root)
    material_ids = list(ingest_result.get("material_ids", []))
    trace_ids = list(ingest_result.get("trace_ids", []))
    if not material_ids:
        raise ValueError("ingest_result has no materials")

    d_vals: List[float] = []
    i_vals: List[float] = []
    s_vals: List[float] = []
    for material_id in material_ids:
        record = service.materials.get(material_id) or {}
        metadata = record.get("metadata", {})
        d_vals.append(float(metadata.get("D", 0.5)))
        i_vals.append(float(metadata.get("I", 0.5)))
        s_vals.append(float(metadata.get("S", 0.5)))

    pressure = service.create_pressure_profile(
        axes=[
            PressureAxis(axis="live_direction", strength_hint=_avg(d_vals)),
            PressureAxis(axis="live_intensity", strength_hint=_avg(i_vals)),
            PressureAxis(axis="live_stability", strength_hint=_avg(s_vals)),
        ],
        support_refs=tuple(
            SupportRef(ref_kind="material", ref_id=material_id, note="live_input")
            for material_id in material_ids[:4]
        ),
    )
    cell = service.create_space_cell_candidate(
        material_refs=material_ids,
        trace_refs=trace_ids,
        seed_refs=list(ingest_result.get("seed_ids", [])),
        pressure_profile_id=pressure.profile_id,
        interior_refs=material_ids,
        exterior_refs=[],
        cohesion_note=(family_id or str(ingest_result.get("source_ref", ""))) + " live input local space",
    )
    local_space = service.form_local_space([cell.cell_id], pressure_profile_id=pressure.profile_id)
    sync_payload = sync_local_space_anchor_metadata(runtime_root, local_space.local_space_id)
    bridge_payloads = _register_live_input_bridges(
        service,
        new_local_space_id=local_space.local_space_id,
        material_ids=material_ids,
        trace_ids=trace_ids,
    )
    possibility_payloads = _register_possibility_bridges(
        service,
        new_local_space_id=local_space.local_space_id,
        material_ids=material_ids,
        trace_ids=trace_ids,
    )
    sync_payload = sync_local_space_anchor_metadata(runtime_root, local_space.local_space_id)
    refresh_payload = refresh_runtime_views(runtime_root)
    return {
        "pressure_profile_id": pressure.profile_id,
        "cell_id": cell.cell_id,
        "local_space_id": local_space.local_space_id,
        "anchor_sync": sync_payload,
        "bridge_sync": bridge_payloads,
        "possibility_sync": possibility_payloads,
        **refresh_payload,
    }


def register_live_input_bridges(
    service: FormationService,
    *,
    new_local_space_id: str,
    material_ids: Sequence[str],
    trace_ids: Sequence[str],
) -> List[Dict[str, object]]:
    return _register_live_input_bridges(
        service,
        new_local_space_id=new_local_space_id,
        material_ids=material_ids,
        trace_ids=trace_ids,
    )


def register_possibility_bridges(
    service: FormationService,
    *,
    new_local_space_id: str,
    material_ids: Sequence[str],
    trace_ids: Sequence[str],
) -> List[Dict[str, object]]:
    return _register_possibility_bridges(
        service,
        new_local_space_id=new_local_space_id,
        material_ids=material_ids,
        trace_ids=trace_ids,
    )


def evaluate_mixed_path_pair(
    service: FormationService,
    *,
    left_local_space_id: str,
    right_local_space_id: str,
) -> Dict[str, object]:
    # Executor section: collect current materials/evidence only. New approval rules
    # belong in review_policies.py, not in this orchestrator.
    left_material_ids = sorted(_local_space_material_ids(service, left_local_space_id))
    right_material_ids = sorted(_local_space_material_ids(service, right_local_space_id))
    left_materials = [service.materials.get(material_id) or {} for material_id in left_material_ids]
    right_materials = [service.materials.get(material_id) or {} for material_id in right_material_ids]
    cross_path_type = _classify_cross_path_type(left_materials, right_materials)
    canonical_pairs = {
        tuple(sorted((str(row.get("from_local_space_id", "")), str(row.get("to_local_space_id", "")))))
        for row in service.bridges.read_all()
    }
    pair = tuple(sorted((left_local_space_id, right_local_space_id)))
    trace = _find_best_cross_path_trace(service, left_material_ids, right_material_ids)
    possibility_basis = _build_possibility_basis(trace, left_materials, right_materials)
    translation_gap_details = _build_translation_gap_details(
        trace,
        possibility_basis,
        cross_path_type,
        left_materials,
        right_materials,
    )
    promotion_blockers = _build_promotion_blockers(
        trace,
        possibility_basis,
        cross_path_type,
        left_materials,
        right_materials,
    )
    promotion_review = _build_promotion_review(
        possibility_basis,
        promotion_blockers,
        cross_path_type,
        left_materials,
        right_materials,
    )
    # Executor section: coarse bridge approval also belongs to approval policy.
    mode = evaluate_bridge_mode_approval_policy(
        BridgeModeApprovalContext(
            canonical_pair_present=pair in canonical_pairs,
            cross_path_type=cross_path_type,
            possibility_basis_available=_has_possibility_basis(possibility_basis),
        )
    ).bridge_mode
    none_reason_kind = (
        _build_none_reason_kind(possibility_basis, promotion_blockers, translation_gap_details)
        if mode == "none"
        else ""
    )
    promotion_review_data = dict(promotion_review or {})
    # Lifecycle section: stable operating grammar for hot/warm/cold and active/blocked stages.
    lifecycle_review = evaluate_review_lifecycle_policy(
        LifecyclePolicyContext(
            bridge_mode=mode,
            review_state=str(promotion_review_data.get("review_state", "")).strip(),
            translation_gate=bool(promotion_review_data.get("translation_gate")),
            processing_gate=bool(promotion_review_data.get("processing_gate")),
            observer_gate=bool(promotion_review_data.get("observer_gate")),
            best_local_ref=str(promotion_review_data.get("best_local_ref", "")).strip(),
            direct_overlap_candidate_count=len(list(promotion_review_data.get("direct_overlap_candidate_families", []) or [])),
            canonicalizable_token_pair_count=int(promotion_review_data.get("canonicalizable_token_pair_count", 0) or 0),
            space_entry_state=str(promotion_review_data.get("space_entry_state", "")).strip(),
            next_review_blocker=str(promotion_review_data.get("next_review_blocker", "")).strip(),
        )
    )
    top_level_timestamp = _build_review_timestamp(
        bridge_mode=mode,
        review_state=str(promotion_review_data.get("review_state", "")).strip(),
        trace_temperature=lifecycle_review.trace_temperature,
        lifecycle_stage=lifecycle_review.lifecycle_stage,
        space_entry_state=str(promotion_review_data.get("space_entry_state", "")).strip(),
        next_review_blocker=str(promotion_review_data.get("next_review_blocker", "")).strip(),
        left_ref=left_local_space_id,
        right_ref=right_local_space_id,
    )
    # Output surface section: return assembled state without embedding new policy logic here.
    return {
        "from_local_space_id": left_local_space_id,
        "to_local_space_id": right_local_space_id,
        "from_label": _local_space_label(service, left_local_space_id),
        "to_label": _local_space_label(service, right_local_space_id),
        "cross_path_type": cross_path_type,
        "bridge_mode": mode,
        "trace_note": str(trace.get("note", "")).strip(),
        "trace_support_refs": list(trace.get("support_refs", []) or [])[:8],
        "possibility_basis": possibility_basis,
        "promotion_blockers": promotion_blockers,
        "promotion_review": promotion_review,
        "evaluated_at": top_level_timestamp.evaluated_at,
        "state_signature": top_level_timestamp.state_signature,
        "trace_temperature": lifecycle_review.trace_temperature,
        "lifecycle_stage": lifecycle_review.lifecycle_stage,
        "lifecycle_reason": lifecycle_review.lifecycle_reason,
        "translation_gap_details": translation_gap_details,
        "none_reason_kind": none_reason_kind,
        "weak_support_summary": _build_weak_support_summary(possibility_basis),
        "blocked_alignment_evidence": _build_blocked_alignment_evidence(possibility_basis),
    }


def enrich_bridge_trace(service: FormationService, bridge_id: str) -> Dict[str, object] | None:
    bridge = service.bridges.get(bridge_id) or {}
    if not bridge:
        return None
    left_material_ids = sorted(_local_space_material_ids(service, str(bridge.get("from_local_space_id", ""))))
    right_material_ids = sorted(_local_space_material_ids(service, str(bridge.get("to_local_space_id", ""))))
    if not left_material_ids or not right_material_ids:
        return None
    left_materials = [service.materials.get(material_id) or {} for material_id in left_material_ids]
    right_materials = [service.materials.get(material_id) or {} for material_id in right_material_ids]
    trace_note = ""
    support_refs: List[Dict[str, str]] = []
    trace_refs = [str(value).strip() for value in bridge.get("trace_refs", []) if str(value).strip()]
    if trace_refs:
        trace = service.traces.get(trace_refs[0]) or {}
        trace_note = str(trace.get("note", ""))
        support_refs = [
            {
                "ref_kind": str(ref.get("ref_kind", "")),
                "ref_id": str(ref.get("ref_id", "")),
                "note": str(ref.get("note", "")),
            }
            for ref in trace.get("support_refs", [])
        ]
    processing_overlap = {
        "trace_note": trace_note,
        "support_refs": [row for row in support_refs if row["ref_kind"] in {"scene", "flow", "material"}][:8],
    }
    shared_anchors = list(bridge.get("shared_anchors", []) or [])
    bridge["bridge_reason_kind"] = (
        "canonical_shared_anchor_with_processing_overlap"
        if shared_anchors and processing_overlap.get("support_refs")
        else "canonical_shared_anchor"
        if shared_anchors
        else f"trace_{trace_note}" if trace_note else "trace_link"
    )
    bridge["processing_overlap"] = processing_overlap
    bridge["observer_contribution"] = _build_observer_contribution(left_materials, right_materials)
    bridge["rejected_overlap_anchors"] = _build_rejected_overlap(left_materials, right_materials)
    service.bridges.put(bridge_id, bridge)
    return bridge


def _avg(values: List[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.5


def _register_live_input_bridges(
    service: FormationService,
    *,
    new_local_space_id: str,
    material_ids: Sequence[str],
    trace_ids: Sequence[str],
) -> List[Dict[str, object]]:
    material_to_spaces = _material_to_local_spaces(service)
    existing_pairs = {
        tuple(sorted((str(row.get("from_local_space_id", "")), str(row.get("to_local_space_id", "")))))
        for row in service.bridges.read_all()
    }
    updates: List[Dict[str, object]] = []
    seen_targets: Set[str] = set()
    for trace_id in trace_ids:
        trace = service.traces.get(trace_id) or {}
        note = str(trace.get("note", ""))
        if note not in {"direct", "tension"}:
            continue
        left_materials = [service.materials.get(material_id) or {} for material_id in material_ids]
        target_spaces: Set[str] = set()
        for material_id in trace.get("material_refs", []):
            if material_id in material_ids:
                continue
            target_spaces.update(material_to_spaces.get(material_id, set()))
        for target_space_id in sorted(target_spaces):
            if target_space_id == new_local_space_id or target_space_id in seen_targets:
                continue
            pair = tuple(sorted((new_local_space_id, target_space_id)))
            if pair in existing_pairs:
                continue
            anchor_hints = [
                str(ref.get("ref_id", "")).strip()
                for ref in trace.get("support_refs", [])
                if str(ref.get("ref_kind", "")).strip() in {"semantic", "object", "process", "structural"}
                and str(ref.get("ref_id", "")).strip()
            ]
            target_material_ids = sorted(_local_space_material_ids(service, target_space_id))
            right_materials = [service.materials.get(material_id) or {} for material_id in target_material_ids]
            bridge = service.register_bridge_trace(
                from_local_space_id=new_local_space_id,
                to_local_space_id=target_space_id,
                trace_refs=[trace_id],
                note=(
                    "canonical shared anchors: " + ", ".join(anchor_hints[:4])
                    if anchor_hints
                    else "recursive_stage_progression_from_trace"
                ),
            )
            bridge_record = service.bridges.get(bridge.bridge_id) or {}
            if anchor_hints:
                bridge_record["shared_anchors"] = [
                    {
                        "canonical_key": hint.lower().replace(" ", "_"),
                        "display_label": hint,
                        "anchor_type": "semantic",
                        "bridge_score": 0.72,
                    }
                    for hint in anchor_hints[:4]
                ]
            service.bridges.put(bridge.bridge_id, bridge_record)
            enriched = enrich_bridge_trace(service, bridge.bridge_id) or bridge_record
            payload = {
                "bridge_id": bridge.bridge_id,
                "from_local_space_id": new_local_space_id,
                "to_local_space_id": target_space_id,
                "trace_id": trace_id,
                "anchor_hints": anchor_hints[:4],
                "note": bridge.note,
                "bridge_reason_kind": enriched.get("bridge_reason_kind", ""),
                "rejected_overlap_anchors": list(enriched.get("rejected_overlap_anchors", []) or [])[:4],
            }
            updates.append(payload)
            existing_pairs.add(pair)
            seen_targets.add(target_space_id)
    return updates


def _register_possibility_bridges(
    service: FormationService,
    *,
    new_local_space_id: str,
    material_ids: Sequence[str],
    trace_ids: Sequence[str],
) -> List[Dict[str, object]]:
    material_to_spaces = _material_to_local_spaces(service)
    canonical_pairs = {
        tuple(sorted((str(row.get("from_local_space_id", "")), str(row.get("to_local_space_id", "")))))
        for row in service.bridges.read_all()
    }
    existing = _load_existing_possibility_pairs(service.runtime_root)
    updates: List[Dict[str, object]] = []
    left_materials = [service.materials.get(material_id) or {} for material_id in material_ids]
    for trace_id in trace_ids:
        trace = service.traces.get(trace_id) or {}
        note = str(trace.get("note", ""))
        if note != "weak":
            continue
        target_spaces: Set[str] = set()
        for material_id in trace.get("material_refs", []):
            if material_id in material_ids:
                continue
            target_spaces.update(material_to_spaces.get(material_id, set()))
        for target_space_id in sorted(target_spaces):
            if target_space_id == new_local_space_id:
                continue
            pair = tuple(sorted((new_local_space_id, target_space_id)))
            target_material_ids = sorted(_local_space_material_ids(service, target_space_id))
            right_materials = [service.materials.get(material_id) or {} for material_id in target_material_ids]
            cross_path_type = _classify_cross_path_type(left_materials, right_materials)
            if cross_path_type not in {"live-imported", "live-legacy"}:
                continue
            possibility_basis = _build_possibility_basis(trace, left_materials, right_materials)
            promotion_blockers = _build_promotion_blockers(
                trace,
                possibility_basis,
                cross_path_type,
                left_materials,
                right_materials,
            )
            promotion_review = _build_promotion_review(
                possibility_basis,
                promotion_blockers,
                cross_path_type,
                left_materials,
                right_materials,
            )
            translation_gap_details = _build_translation_gap_details(
                trace,
                possibility_basis,
                cross_path_type,
                left_materials,
                right_materials,
            )
            mode = "none"
            blocked_reason = ""
            if pair in canonical_pairs:
                mode = "canonical"
                blocked_reason = ""
            elif pair in existing:
                mode = "possibility_candidate"
                blocked_reason = promotion_blockers[0] if promotion_blockers else ""
            elif _has_possibility_basis(possibility_basis):
                mode = "possibility_candidate"
                blocked_reason = promotion_blockers[0] if promotion_blockers else ""
                payload = {
                    "possibility_bridge_id": _possibility_bridge_id(pair),
                    "bridge_mode": "possibility_candidate",
                    "from_local_space_id": new_local_space_id,
                    "to_local_space_id": target_space_id,
                    "from_label": _local_space_label(service, new_local_space_id),
                    "to_label": _local_space_label(service, target_space_id),
                    "trace_refs": [trace_id],
                    "cross_path_type": cross_path_type,
                    "bridge_reason_kind": "mixed_path_possibility_candidate",
                    "possibility_basis": possibility_basis,
                    "promotion_blockers": promotion_blockers,
                    "promotion_review": promotion_review,
                    "translation_gap_details": translation_gap_details,
                    "blocked_reason": blocked_reason,
                    "state": "candidate",
                }
                _write_possibility_bridge(service.runtime_root, payload)
                existing.add(pair)
                updates.append(payload)
            else:
                blocked_reason = _build_none_reason_kind(
                    possibility_basis,
                    promotion_blockers,
                    translation_gap_details,
                )
            _write_possibility_bridge_evaluation(
                service.runtime_root,
                {
                    "possibility_bridge_evaluation_id": _possibility_bridge_evaluation_id(pair),
                    "from_local_space_id": new_local_space_id,
                    "to_local_space_id": target_space_id,
                    "from_label": _local_space_label(service, new_local_space_id),
                    "to_label": _local_space_label(service, target_space_id),
                    "trace_refs": [trace_id],
                    "cross_path_type": cross_path_type,
                    "bridge_mode": mode,
                    "bridge_reason_kind": (
                        "mixed_path_possibility_candidate"
                        if mode == "possibility_candidate"
                        else "canonical_bridge_already_open"
                        if mode == "canonical"
                        else "mixed_path_none"
                    ),
                    "possibility_basis": possibility_basis,
                    "promotion_blockers": promotion_blockers,
                    "promotion_review": promotion_review,
                    "translation_gap_details": translation_gap_details,
                    "none_reason_kind": blocked_reason if mode == "none" else "",
                    "blocked_reason": blocked_reason,
                    "weak_support_summary": _build_weak_support_summary(possibility_basis),
                    "blocked_alignment_evidence": _build_blocked_alignment_evidence(possibility_basis),
                    "state": "recorded",
                },
            )
    return updates


def _material_to_local_spaces(service: FormationService) -> Dict[str, Set[str]]:
    cell_to_spaces: Dict[str, Set[str]] = {}
    for local_space in service.local_spaces.read_all():
        local_space_id = str(local_space.get("local_space_id", ""))
        for cell_id in local_space.get("cell_refs", []):
            cell_to_spaces.setdefault(str(cell_id), set()).add(local_space_id)
    mapping: Dict[str, Set[str]] = {}
    for cell in service.cells.read_all():
        spaces = cell_to_spaces.get(str(cell.get("cell_id", "")), set())
        if not spaces:
            continue
        for material_id in cell.get("material_refs", []):
            mapping.setdefault(str(material_id), set()).update(spaces)
    return mapping


def _local_space_material_ids(service: FormationService, local_space_id: str) -> Set[str]:
    local_space = service.local_spaces.get(local_space_id) or {}
    material_ids: Set[str] = set()
    for cell_id in local_space.get("cell_refs", []):
        cell = service.cells.get(str(cell_id)) or {}
        for material_id in cell.get("material_refs", []):
            material_ids.add(str(material_id))
    return material_ids


def _possibility_bridge_id(pair: Sequence[str]) -> str:
    joined = "__".join(sorted(str(value) for value in pair))
    return "pbg_" + joined.replace("/", "_").replace("-", "_")[:64]


def _possibility_bridge_evaluation_id(pair: Sequence[str]) -> str:
    joined = "__".join(sorted(str(value) for value in pair))
    return "pbe_" + joined.replace("/", "_").replace("-", "_")[:64]


def _possibility_bridge_dir(runtime_root: Path) -> Path:
    path = runtime_root / "core" / "possibility_bridges"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_possibility_bridge(runtime_root: Path, payload: Dict[str, object]) -> None:
    bridge_id = str(payload.get("possibility_bridge_id", "")).strip()
    if not bridge_id:
        return
    path = _possibility_bridge_dir(runtime_root) / f"{bridge_id}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _possibility_bridge_evaluation_dir(runtime_root: Path) -> Path:
    path = runtime_root / "core" / "possibility_bridge_evaluations"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_possibility_bridge_evaluation(runtime_root: Path, payload: Dict[str, object]) -> None:
    evaluation_id = str(payload.get("possibility_bridge_evaluation_id", "")).strip()
    if not evaluation_id:
        return
    path = _possibility_bridge_evaluation_dir(runtime_root) / f"{evaluation_id}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _find_best_cross_path_trace(
    service: FormationService,
    left_material_ids: Sequence[str],
    right_material_ids: Sequence[str],
) -> Dict[str, object]:
    left_set = set(str(value) for value in left_material_ids)
    right_set = set(str(value) for value in right_material_ids)
    best: Dict[str, object] = {}
    best_score = -1
    for trace in service.traces.read_all():
        refs = {str(value) for value in trace.get("material_refs", [])}
        if not (refs & left_set) or not (refs & right_set):
            continue
        note = str(trace.get("note", "")).strip()
        support_refs = list(trace.get("support_refs", []) or [])
        score = 0
        if note == "weak":
            score += 5
        elif note in {"direct", "tension"}:
            score += 3
        score += len(support_refs)
        if score > best_score:
            best = dict(trace)
            best_score = score
    return best


def _load_existing_possibility_pairs(runtime_root: Path) -> Set[tuple[str, str]]:
    rows: Set[tuple[str, str]] = set()
    for path in _possibility_bridge_dir(runtime_root).glob("*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        left = str(payload.get("from_local_space_id", "")).strip()
        right = str(payload.get("to_local_space_id", "")).strip()
        if left and right:
            rows.add(tuple(sorted((left, right))))
    return rows


def _build_observer_contribution(left_materials: Sequence[Dict[str, object]], right_materials: Sequence[Dict[str, object]]) -> Dict[str, object]:
    left_roles = _collect_roles(left_materials)
    right_roles = _collect_roles(right_materials)
    left_signals = _collect_signals(left_materials)
    right_signals = _collect_signals(right_materials)
    shared_signals = sorted(set(left_signals) & set(right_signals))
    left_seen = _has_observer_trace(left_materials)
    right_seen = _has_observer_trace(right_materials)
    unavailable_reason = ""
    if not (left_roles or right_roles or left_signals or right_signals):
        if not left_seen and not right_seen:
            unavailable_reason = "observer_trace_missing_on_both_sides"
        elif not left_seen:
            unavailable_reason = "observer_trace_missing_on_left"
        elif not right_seen:
            unavailable_reason = "observer_trace_missing_on_right"
        else:
            unavailable_reason = "observer_trace_present_but_no_role_or_signal_overlap"
    return {
        "available": bool(left_roles or right_roles or left_signals or right_signals),
        "left_roles": left_roles[:3],
        "right_roles": right_roles[:3],
        "shared_signals": shared_signals[:4],
        "unavailable_reason": unavailable_reason,
    }


def _build_rejected_overlap(left_materials: Sequence[Dict[str, object]], right_materials: Sequence[Dict[str, object]]) -> List[str]:
    left_labels = set(_collect_dropped_weak(left_materials))
    right_labels = set(_collect_dropped_weak(right_materials))
    return sorted(left_labels & right_labels)[:10]


def _collect_roles(materials: Sequence[Dict[str, object]]) -> List[str]:
    roles: List[str] = []
    for material in materials:
        metadata = material.get("metadata", {})
        trace = dict(metadata.get("observer_or_ambiguity_trace", {}))
        merged = dict(trace.get("merged", {}))
        role = str(merged.get("role") or metadata.get("observer_role") or "").strip()
        if role and role not in roles:
            roles.append(role)
    return roles


def _collect_signals(materials: Sequence[Dict[str, object]]) -> List[str]:
    signals: List[str] = []
    for material in materials:
        metadata = material.get("metadata", {})
        trace = dict(metadata.get("observer_or_ambiguity_trace", {}))
        merged = dict(trace.get("merged", {}))
        rows = list(merged.get("signals", []) or metadata.get("observer_signals", []) or [])
        for value in rows:
            label = str(value).strip()
            if label and label not in signals:
                signals.append(label)
    return signals


def _collect_dropped_weak(materials: Sequence[Dict[str, object]]) -> List[str]:
    labels: List[str] = []
    for material in materials:
        metadata = material.get("metadata", {})
        for value in list(metadata.get("dropped_weak_anchors", []) or []):
            label = str(value).strip()
            if label and label not in labels:
                labels.append(label)
    return labels


def _has_observer_trace(materials: Sequence[Dict[str, object]]) -> bool:
    for material in materials:
        metadata = material.get("metadata", {})
        if metadata.get("observer_or_ambiguity_trace") is not None:
            return True
    return False


def _classify_cross_path_type(left_materials: Sequence[Dict[str, object]], right_materials: Sequence[Dict[str, object]]) -> str:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    ordered = tuple(sorted((left_kind, right_kind)))
    mapping = {
        ("imported", "imported"): "imported-imported",
        ("imported", "legacy"): "imported-legacy",
        ("imported", "live"): "live-imported",
        ("legacy", "legacy"): "legacy-legacy",
        ("legacy", "live"): "live-legacy",
        ("live", "live"): "live-live",
    }
    return mapping.get(ordered, "unknown")


def _dominant_path_kind(materials: Sequence[Dict[str, object]]) -> str:
    counts: Dict[str, int] = {"imported": 0, "legacy": 0, "live": 0}
    for material in materials:
        source_ref = str(material.get("source_ref", "")).strip()
        if source_ref.startswith("processor_compare/"):
            counts["imported"] += 1
        elif source_ref.startswith("manual/"):
            counts["legacy"] += 1
        elif source_ref.startswith("engine_phase1_") or source_ref.startswith("operator_phase1_") or source_ref.startswith("memo-") or source_ref.startswith("review-"):
            counts["live"] += 1
    return max(counts.items(), key=lambda row: row[1])[0] if any(counts.values()) else "legacy"


def _build_possibility_basis(
    trace: Dict[str, object],
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    anchor_hints = [
        str(ref.get("ref_id", "")).strip()
        for ref in trace.get("support_refs", [])
        if str(ref.get("ref_kind", "")).strip() in {"semantic", "object", "process", "structural"}
        and str(ref.get("ref_id", "")).strip()
    ]
    processing_refs = [
        {
            "ref_kind": str(ref.get("ref_kind", "")),
            "ref_id": str(ref.get("ref_id", "")),
            "note": str(ref.get("note", "")),
        }
        for ref in trace.get("support_refs", [])
        if str(ref.get("ref_kind", "")) in {"scene", "flow"}
    ]
    observer = _build_observer_contribution(left_materials, right_materials)
    left_labels = {str(material.get("source_ref", "")).strip() for material in left_materials if str(material.get("source_ref", "")).strip()}
    right_labels = {str(material.get("source_ref", "")).strip() for material in right_materials if str(material.get("source_ref", "")).strip()}
    return {
        "partial_anchor_alignment": anchor_hints[:3],
        "weak_processing_overlap": processing_refs[:4],
        "observer_affinity": {
            "available": observer.get("available", False),
            "left_roles": list(observer.get("left_roles", []))[:2],
            "right_roles": list(observer.get("right_roles", []))[:2],
            "shared_signals": list(observer.get("shared_signals", []))[:2],
        },
        "structural_echo": [row["note"] for row in processing_refs if row["note"] in {"scene_match", "flow_match"}][:2],
        "partial_handle_overlap": sorted({value.split("/")[-1] for value in left_labels | right_labels})[:2],
        "shared_scene_or_flow_hint": [row["ref_id"] for row in processing_refs[:2]],
        "translation_assisted_alignment": _build_translation_assisted_alignment(left_materials, right_materials),
        "translation_processing_interplay": _build_translation_processing_interplay(left_materials, right_materials),
    }


def _has_possibility_basis(payload: Dict[str, object]) -> bool:
    translation_alignment = dict(payload.get("translation_assisted_alignment", {}) or {})
    observer_affinity = dict(payload.get("observer_affinity", {}) or {})
    return bool(
        payload.get("partial_anchor_alignment")
        or payload.get("weak_processing_overlap")
        or payload.get("structural_echo")
        or payload.get("shared_scene_or_flow_hint")
        or (
            translation_alignment.get("available")
            and (
                observer_affinity.get("available")
                or payload.get("weak_processing_overlap")
                or payload.get("shared_scene_or_flow_hint")
            )
        )
    )


def _build_promotion_blockers(
    trace: Dict[str, object],
    possibility_basis: Dict[str, object],
    cross_path_type: str,
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> List[str]:
    blockers: List[str] = []
    if len(list(possibility_basis.get("partial_anchor_alignment", []))) < 2:
        blockers.append("missing_canonical_anchor_alignment")
    if not list(possibility_basis.get("weak_processing_overlap", [])):
        blockers.append("processing_overlap_below_canonical")
    elif str(trace.get("note", "")) == "weak":
        blockers.append("processing_overlap_below_canonical")
    observer_affinity = dict(possibility_basis.get("observer_affinity", {}) or {})
    translation_alignment = dict(possibility_basis.get("translation_assisted_alignment", {}) or {})
    if not observer_affinity.get("available"):
        blockers.append("observer_support_insufficient")
    if cross_path_type in {"live-imported", "live-legacy"}:
        blockers.append("cross_path_translation_gap")
    if translation_alignment.get("available") and cross_path_type == "live-imported":
        blockers.append("translation_assisted_possibility_only")
    blockers.extend(_build_translation_gap_details(trace, possibility_basis, cross_path_type, left_materials, right_materials))
    return blockers


def _build_translation_gap_details(
    trace: Dict[str, object],
    possibility_basis: Dict[str, object],
    cross_path_type: str,
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> List[str]:
    details: List[str] = []
    partial_anchors = list(possibility_basis.get("partial_anchor_alignment", []) or [])
    weak_processing = list(possibility_basis.get("weak_processing_overlap", []) or [])
    observer_affinity = dict(possibility_basis.get("observer_affinity", {}) or {})
    structural_echo = list(possibility_basis.get("structural_echo", []) or [])
    partial_handles = list(possibility_basis.get("partial_handle_overlap", []) or [])
    shared_scene_or_flow = list(possibility_basis.get("shared_scene_or_flow_hint", []) or [])
    translation_alignment = dict(possibility_basis.get("translation_assisted_alignment", {}) or {})
    if not partial_anchors and not translation_alignment.get("available"):
        details.append("anchor_vocabulary_translation_gap")
        details.append("one_sided_anchor_presence")
    if cross_path_type == "live-imported" and translation_alignment.get("available"):
        details.append("translation_scope_local_ref")
        if translation_alignment.get("matched_local_ref_count", 0) <= 1:
            details.append("translation_assisted_alignment_narrow")
    if not weak_processing:
        details.append("processing_projection_mismatch")
        details.append("scene_flow_alignment_insufficient")
    if weak_processing and str(trace.get("note", "")) == "weak":
        details.append("processing_overlap_below_possibility")
    if not observer_affinity.get("available"):
        details.append("observer_affinity_too_weak")
        details.append("observer_support_non_discriminative")
    if not structural_echo:
        details.append("weak_trace_not_compounding")
    if len(partial_handles) < 2:
        details.append("source_handle_translation_missing")
    if not shared_scene_or_flow:
        details.append("scene_flow_alignment_insufficient")
    if cross_path_type == "live-imported":
        details.append("imported_doc_signal_not_reconciled")
        right_kind = _dominant_path_kind(right_materials)
        imported_materials = right_materials if right_kind == "imported" else left_materials
        if len(imported_materials) > 3:
            details.append("document_span_too_broad_for_local_alignment")
            details.append("granularity_mismatch")
        if len({str(row.get('source_ref', '')).strip() for row in imported_materials if str(row.get('source_ref', '')).strip()}) <= 1:
            details.append("imported_semantics_flattened")
    if cross_path_type == "live-legacy" and not partial_handles:
        details.append("legacy_like_resonance_absent")
    deduped: List[str] = []
    for item in details:
        if item and item not in deduped:
            deduped.append(item)
    return deduped


def _build_none_reason_kind(
    possibility_basis: Dict[str, object],
    promotion_blockers: Sequence[str],
    translation_gap_details: Sequence[str],
) -> str:
    if "anchor_vocabulary_translation_gap" in translation_gap_details:
        return "anchor_vocabulary_translation_gap"
    if "imported_doc_signal_not_reconciled" in translation_gap_details:
        return "imported_doc_signal_not_reconciled"
    if "processing_projection_mismatch" in translation_gap_details:
        return "processing_projection_mismatch"
    if "observer_affinity_too_weak" in translation_gap_details:
        return "observer_affinity_too_weak"
    if "weak_trace_not_compounding" in translation_gap_details:
        return "weak_trace_not_compounding"
    if promotion_blockers:
        return str(promotion_blockers[0])
    if not _has_possibility_basis(possibility_basis):
        return "insufficient_possibility_basis"
    return "mixed_path_none"


def _build_promotion_review(
    possibility_basis: Dict[str, object],
    promotion_blockers: Sequence[str],
    cross_path_type: str,
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    # Orchestration only: gather evidence, call policy functions, then assemble
    # readable review surface. New approval rules should be added to review_policies.py.
    translation_alignment = dict(possibility_basis.get("translation_assisted_alignment", {}) or {})
    interplay = dict(possibility_basis.get("translation_processing_interplay", {}) or {})
    observer_affinity = dict(possibility_basis.get("observer_affinity", {}) or {})
    partial_anchor_alignment = list(possibility_basis.get("partial_anchor_alignment", []) or [])
    policy_context = PromotionPolicyContext(
        cross_path_type=cross_path_type,
        translation_available=bool(translation_alignment.get("available")),
        translation_scope_used=str(translation_alignment.get("translation_scope_used", "")).strip(),
        matched_local_ref_count=int(translation_alignment.get("matched_local_ref_count", 0) or 0),
        matched_handles=list(translation_alignment.get("matched_handles", []) or []),
        best_local_ref=str(interplay.get("best_local_ref", "")).strip(),
        best_processing_score=float(interplay.get("best_score", 0.0) or 0.0),
        processing_convergence_level=str(interplay.get("convergence_level", "")).strip() or "none",
        observer_available=bool(observer_affinity.get("available")),
        partial_anchor_alignment_count=len(partial_anchor_alignment),
        promotion_blockers=list(promotion_blockers),
    )
    policy_result = evaluate_promotion_review_policy(policy_context)
    if not policy_result.available:
        return {"available": False, "review_state": policy_result.review_state}
    anchor_review = _build_anchor_review(
        left_materials,
        right_materials,
        translation_alignment,
        policy_context.best_local_ref,
    )
    live_side_review = _build_live_side_anchor_support_review(left_materials, right_materials)
    canonicalization_review = _build_cross_path_canonicalization_review(
        left_materials,
        right_materials,
        policy_context.best_local_ref,
        live_side_review,
        anchor_review,
    )
    direct_overlap_review = _build_direct_overlap_review(anchor_review, canonicalization_review)
    gate_vector = dict(policy_result.gate_vector)
    gate_vector["canonical_anchor_gate"] = bool(anchor_review.get("canonical_anchor_gate", False))
    gate_vector["canonical_anchor_alignment_count"] = int(anchor_review.get("canonical_anchor_alignment_count", 0) or 0)
    next_review_blocker = (
        str(anchor_review.get("next_review_blocker", "")).strip()
        or policy_result.next_review_blocker
    )
    threshold_review = _build_threshold_review(anchor_review, gate_vector)
    cross_path_review = _build_cross_path_review(anchor_review, translation_alignment, live_side_review)
    space_entry_review = _build_space_entry_review(
        gate_vector=gate_vector,
        anchor_review=anchor_review,
        direct_overlap_review=direct_overlap_review,
    )
    canonical_review_decision = evaluate_canonical_review_decision_policy(
        CanonicalReviewDecisionContext(
            promotion_readiness_class=policy_result.promotion_readiness_class,
            anchor_next_review_blocker=next_review_blocker,
            threshold_gap_class=str(threshold_review.get("threshold_gap_class", "")).strip(),
            cross_path_threshold_gap_class=str(cross_path_review.get("cross_path_threshold_gap_class", "")).strip(),
            direct_overlap_gap_class=str(direct_overlap_review.get("direct_overlap_gap_class", "")).strip(),
        )
    )
    next_review_blocker = canonical_review_decision.next_review_blocker
    canonical_approval_status = evaluate_canonical_approval_status_policy(
        CanonicalApprovalStatusContext(
            canonical_anchor_gate=bool(gate_vector.get("canonical_anchor_gate")),
            cross_path_overlap_family_count=int(cross_path_review.get("cross_path_overlap_family_count", 0) or 0),
            direct_overlap_candidate_count=len(list(direct_overlap_review.get("direct_overlap_candidate_families", []) or [])),
            canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),
            space_entry_state=str(space_entry_review.get("space_entry_state", "")).strip(),
            canonical_review_focus_class=canonical_review_decision.canonical_review_focus_class,
        )
    )
    lifecycle_review = evaluate_review_lifecycle_policy(
        LifecyclePolicyContext(
            bridge_mode="possibility_candidate",
            review_state=policy_result.review_state,
            translation_gate=bool(gate_vector.get("translation_gate")),
            processing_gate=bool(gate_vector.get("processing_gate")),
            observer_gate=bool(gate_vector.get("observer_gate")),
            best_local_ref=policy_context.best_local_ref,
            direct_overlap_candidate_count=len(list(direct_overlap_review.get("direct_overlap_candidate_families", []) or [])),
            canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),
            space_entry_state=str(space_entry_review.get("space_entry_state", "")).strip(),
            next_review_blocker=next_review_blocker,
        )
    )
    review_timestamp = _build_review_timestamp(
        bridge_mode="possibility_candidate",
        review_state=policy_result.review_state,
        trace_temperature=lifecycle_review.trace_temperature,
        lifecycle_stage=lifecycle_review.lifecycle_stage,
        space_entry_state=str(space_entry_review.get("space_entry_state", "")).strip(),
        next_review_blocker=next_review_blocker,
        left_ref=_material_side_ref(left_materials),
        right_ref=_material_side_ref(right_materials),
    )
    adjusted_policy = PromotionPolicyResult(
        available=policy_result.available,
        review_state=policy_result.review_state,
        review_kind=policy_result.review_kind,
        recommendation=policy_result.recommendation,
        translation_coverage_class=policy_result.translation_coverage_class,
        processing_residual_class=policy_result.processing_residual_class,
        next_review_blocker=next_review_blocker,
        gate_vector=gate_vector,
        promotion_readiness_class=policy_result.promotion_readiness_class,
        promotion_decision=canonical_review_decision.promotion_decision,
    )
    review_surface = assemble_promotion_review_surface(
        context=policy_context,
        policy=adjusted_policy,
        assembly=PromotionReviewAssembly(
            anchor_review=anchor_review,
            live_side_review=live_side_review,
            threshold_review=threshold_review,
            cross_path_review=cross_path_review,
            canonicalization_review=canonicalization_review,
            direct_overlap_review=direct_overlap_review,
            space_entry_review=space_entry_review,
            residual_blockers=list(promotion_blockers),
        ),
        lifecycle=lifecycle_review,
        timestamp=review_timestamp,
    )
    review_surface["canonical_review_focus_class"] = canonical_review_decision.canonical_review_focus_class
    review_surface["canonical_approval_readiness_class"] = canonical_approval_status.canonical_approval_readiness_class
    review_surface["canonical_approval_next_step"] = canonical_approval_status.canonical_approval_next_step
    review_surface["canonical_approval_vector"] = canonical_approval_status.canonical_approval_vector
    return review_surface


def _build_threshold_review(anchor_review: Dict[str, object], gate_vector: Dict[str, object]) -> Dict[str, object]:
    same_strength = int(dict(anchor_review.get("anchor_family_support_strength", {}) or {}).get("same_local_ref", 0) or 0)
    nearby_strength = int(dict(anchor_review.get("anchor_family_support_strength", {}) or {}).get("nearby_local_ref", 0) or 0)
    canonical_alignment_count = int(gate_vector.get("canonical_anchor_alignment_count", 0) or 0)
    support_density_class = "sparse"
    if same_strength >= 3:
        support_density_class = "dense_same_local_ref"
    elif same_strength >= 2:
        support_density_class = "moderate_same_local_ref"
    elif same_strength >= 1:
        support_density_class = "single_family_same_local_ref"
    elif nearby_strength >= 2:
        support_density_class = "dense_nearby_only"
    elif nearby_strength >= 1:
        support_density_class = "weak_nearby_only"
    corroboration_scope = str(anchor_review.get("compound_support_scope", "")).strip()
    corroboration_scope_class = corroboration_scope or "none"
    threshold_gap_class = ""
    if bool(gate_vector.get("canonical_anchor_gate")):
        threshold_gap_class = ""
    elif support_density_class == "dense_same_local_ref" and canonical_alignment_count < 2:
        threshold_gap_class = "cross_path_anchor_overlap_below_threshold"
    elif support_density_class in {"moderate_same_local_ref", "single_family_same_local_ref"}:
        threshold_gap_class = "same_local_ref_support_density_below_threshold"
    elif corroboration_scope_class == "nearby_local_ref":
        threshold_gap_class = "compound_scope_too_broad"
    else:
        threshold_gap_class = "canonical_review_support_below_threshold"
    return {
        "support_density_class": support_density_class,
        "corroboration_scope_class": corroboration_scope_class,
        "threshold_gap_class": threshold_gap_class,
        "threshold_review_vector": {
            "same_local_ref_support_strength": same_strength,
            "nearby_local_ref_support_strength": nearby_strength,
            "canonical_anchor_alignment_count": canonical_alignment_count,
        },
    }


def _build_cross_path_review(
    anchor_review: Dict[str, object],
    translation_alignment: Dict[str, object],
    live_side_review: Dict[str, object],
) -> Dict[str, object]:
    evidence = dict(anchor_review.get("anchor_alignment_evidence", {}) or {})
    semantic_overlap = list(evidence.get("semantic_overlap", []) or [])
    structural_overlap = list(evidence.get("structural_overlap", []) or [])
    process_overlap = list(evidence.get("process_overlap", []) or [])
    object_overlap = list(evidence.get("object_overlap", []) or [])
    translated_hits = list(evidence.get("translated_handle_hits", []) or [])
    overlap_families: List[str] = []
    if semantic_overlap:
        overlap_families.append("semantic")
    if structural_overlap:
        overlap_families.append("structural")
    if process_overlap:
        overlap_families.append("process")
    if object_overlap:
        overlap_families.append("object")
    raw_anchor_overlap_count = len(semantic_overlap) + len(structural_overlap) + len(process_overlap) + len(object_overlap)
    translation_assisted_overlap_count = len(translated_hits)
    overlap_tokens = set(semantic_overlap + structural_overlap + process_overlap + object_overlap)
    translated_but_not_canonicalized_count = len([value for value in translated_hits if value not in overlap_tokens])
    canonicalizable_overlap_count = raw_anchor_overlap_count
    family_count = len(overlap_families)
    live_side_families = list(live_side_review.get("live_side_support_families", []) or [])
    imported_candidate_families = ["semantic"] + list(anchor_review.get("compound_candidate_families", []) or [])
    uncorr_live_families = [
        family
        for family in imported_candidate_families
        if family in live_side_families and family not in overlap_families
    ]
    canonicalization_candidate_families = [family for family in uncorr_live_families if family != "semantic"]
    context = CrossPathPolicyContext(
        family_count=family_count,
        overlap_families=overlap_families,
        raw_anchor_overlap_count=raw_anchor_overlap_count,
        translation_assisted_overlap_count=translation_assisted_overlap_count,
        canonicalizable_overlap_count=canonicalizable_overlap_count,
        translated_but_not_canonicalized_count=translated_but_not_canonicalized_count,
        live_side_families=live_side_families,
        imported_candidate_families=imported_candidate_families,
        canonicalization_candidate_families=canonicalization_candidate_families,
        uncorroborated_live_families=uncorr_live_families,
    )
    policy = evaluate_cross_path_overlap_policy(context)
    return assemble_cross_path_review_surface(
        context=context,
        policy=policy,
        overlap_evidence={
            "translation_assisted_overlap_count": translation_assisted_overlap_count,
            "canonicalizable_overlap_count": canonicalizable_overlap_count,
            "translated_but_not_canonicalized_count": translated_but_not_canonicalized_count,
            "raw_anchor_overlap_count": raw_anchor_overlap_count,
            "derived_anchor_overlap_count": translation_assisted_overlap_count,
            "translated_handles": translated_hits[:6],
            "live_side_support_families": live_side_families,
            "imported_candidate_families": imported_candidate_families,
            "canonicalization_candidate_families": canonicalization_candidate_families,
        },
    )


def _build_anchor_review(
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
    translation_alignment: Dict[str, object],
    best_local_ref: str,
) -> Dict[str, object]:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    live_materials = left_materials if left_kind == "live" else right_materials
    imported_materials = right_materials if left_kind == "live" else left_materials
    live_profile = _collect_anchor_type_profile(live_materials)
    imported_profile = _collect_anchor_type_profile(imported_materials)
    semantic_overlap_set = live_profile["semantic"] & imported_profile["semantic"]
    structural_overlap_set = live_profile["structural"] & imported_profile["structural"]
    process_overlap_set = live_profile["process"] & imported_profile["process"]
    object_overlap_set = live_profile["object"] & imported_profile["object"]
    overlap_set = semantic_overlap_set | structural_overlap_set | process_overlap_set | object_overlap_set
    overlap = sorted(overlap_set)
    translated_handles = {
        _normalize_token(str(value).strip())
        for value in list(translation_alignment.get("matched_handles", []) or [])
        if str(value).strip()
    }
    local_accumulation = _build_local_anchor_accumulation(imported_materials, best_local_ref)
    semantic_supported = bool(semantic_overlap_set)
    structural_supported = bool(structural_overlap_set)
    process_supported = bool(process_overlap_set)
    object_supported = bool(object_overlap_set)
    anchor_policy = evaluate_canonical_anchor_approval_policy(
        CanonicalAnchorApprovalContext(
            semantic_supported=semantic_supported,
            structural_supported=structural_supported,
            process_supported=process_supported,
            object_supported=object_supported,
            translated_handle_count=len(translated_handles),
            local_compound_state=str(local_accumulation.get("compound_state", "")).strip(),
            local_review_anchor_support_class=str(local_accumulation.get("review_anchor_support_class", "")).strip(),
            local_review_anchor_gap_class=str(local_accumulation.get("review_anchor_gap_class", "")).strip(),
            local_next_review_blocker=str(local_accumulation.get("next_review_blocker", "")).strip(),
            has_local_compound_candidates=bool(local_accumulation.get("compound_candidate_families")),
        )
    )
    return {
        "canonical_anchor_gate": anchor_policy.canonical_anchor_gate,
        "canonical_anchor_alignment_count": anchor_policy.canonical_anchor_alignment_count,
        "review_anchor_gap_class": anchor_policy.review_anchor_gap_class,
        "review_anchor_support_class": anchor_policy.review_anchor_support_class,
        "anchor_alignment_evidence": {
            "semantic_overlap": sorted(semantic_overlap_set)[:6],
            "structural_overlap": sorted(structural_overlap_set)[:6],
            "process_overlap": sorted(process_overlap_set)[:6],
            "object_overlap": sorted(object_overlap_set)[:6],
            "translated_handle_hits": sorted(translated_handles)[:6],
            "structural_supported": structural_supported,
            "process_supported": process_supported,
            "object_supported": object_supported,
        },
        "anchor_alignment_missing_types": anchor_policy.anchor_alignment_missing_types,
        "anchor_alignment_subcritical_types": anchor_policy.anchor_alignment_subcritical_types,
        "anchor_alignment_compound_state": anchor_policy.anchor_alignment_compound_state,
        "anchor_support_scope": str(local_accumulation.get("anchor_support_scope", "")).strip(),
        "anchor_family_additions": dict(local_accumulation.get("anchor_family_additions", {}) or {}),
        "anchor_family_support_strength": dict(local_accumulation.get("anchor_family_support_strength", {}) or {}),
        "compound_candidate_families": list(local_accumulation.get("compound_candidate_families", []) or []),
        "compound_support_scope": str(local_accumulation.get("compound_support_scope", "")).strip(),
        "next_review_blocker": anchor_policy.next_review_blocker,
    }


def _collect_anchor_tokens(materials: Sequence[Dict[str, object]]) -> Set[str]:
    tokens: Set[str] = set()
    for material in materials:
        metadata = dict(material.get("metadata", {}) or {})
        bundle = dict(metadata.get("anchor_bundle", {}) or {})
        for item in list(bundle.get("representative_anchors", []) or []):
            for value in (
                str(item.get("canonical_key", "")).strip(),
                str(item.get("display_label", "")).strip(),
            ):
                token = _normalize_token(value)
                if token:
                    tokens.add(token)
        for value in list(bundle.get("supporting_anchors", []) or []):
            token = _normalize_token(str(value).strip())
            if token:
                tokens.add(token)
    return tokens


def _collect_anchor_type_profile(materials: Sequence[Dict[str, object]]) -> Dict[str, Set[str]]:
    profile: Dict[str, Set[str]] = {
        "semantic": set(),
        "structural": set(),
        "process": set(),
        "object": set(),
    }
    for token in _collect_anchor_tokens(materials):
        kinds = _anchor_token_kinds(token)
        if not kinds:
            profile["semantic"].add(token)
            continue
        for kind in kinds:
            profile.setdefault(kind, set()).add(token)
    return profile


def _anchor_token_kinds(token: str) -> Set[str]:
    lowered = _normalize_token(token)
    kinds: Set[str] = set()
    if lowered in {"graph", "rag", "graph rag", "ontology", "property", "object"}:
        kinds.add("semantic")
    if any(value in lowered for value in {"structure", "graph db", "database", "node", "relationship", "relation", "구조", "관계"}):
        kinds.add("structural")
    if any(value in lowered for value in {"retrieval", "generation", "query", "검색", "질의", "추론", "multi hop", "multi-hop", "처리"}):
        kinds.add("process")
    if any(value in lowered for value in {"property", "object", "ontology", "속성", "객체"}):
        kinds.add("object")
    return kinds


def _build_local_anchor_accumulation(
    imported_materials: Sequence[Dict[str, object]],
    best_local_ref: str,
) -> Dict[str, object]:
    if not best_local_ref:
        return {
            "anchor_support_scope": "",
            "anchor_family_additions": {},
            "anchor_family_support_strength": {},
            "compound_candidate_families": [],
            "compound_support_scope": "",
            "compound_state": "single_family_only",
            "review_anchor_support_class": "",
            "review_anchor_gap_class": "",
            "next_review_blocker": "",
        }
    local_profiles: Dict[str, Dict[str, Set[str]]] = {}
    local_texts: Dict[str, str] = {}
    for material in imported_materials:
        metadata = dict(material.get("metadata", {}) or {})
        local_ref = str(dict(metadata.get("transformable_handles", {}) or {}).get("source_local_ref", "")).strip()
        if not local_ref:
            continue
        local_profiles.setdefault(local_ref, _collect_anchor_type_profile([material]))
        local_texts[local_ref] = str(material.get("raw_payload", "") or "")
    same_profile = local_profiles.get(best_local_ref, {"semantic": set(), "structural": set(), "process": set(), "object": set()})
    nearby_refs = _nearby_local_refs(best_local_ref, list(local_profiles.keys()))
    nearby_profile = {"semantic": set(), "structural": set(), "process": set(), "object": set()}
    for local_ref in nearby_refs:
        profile = local_profiles.get(local_ref, {})
        for key in nearby_profile:
            nearby_profile[key].update(profile.get(key, set()))
    same_text_hints = _text_family_hints(local_texts.get(best_local_ref, ""))
    nearby_text_hints = {"structural": set(), "process": set(), "object": set()}
    for local_ref in nearby_refs:
        hints = _text_family_hints(local_texts.get(local_ref, ""))
        for key in nearby_text_hints:
            nearby_text_hints[key].update(hints.get(key, set()))
    family_additions = {"same_local_ref": [], "nearby_local_ref": []}
    for family in ("structural", "process", "object"):
        if same_profile.get(family) or same_text_hints.get(family):
            family_additions["same_local_ref"].append(family)
        elif nearby_profile.get(family) or nearby_text_hints.get(family):
            family_additions["nearby_local_ref"].append(family)
    support_strength = {
        "same_local_ref": len(family_additions["same_local_ref"]),
        "nearby_local_ref": len(family_additions["nearby_local_ref"]),
    }
    compound_candidate_families = list(family_additions["same_local_ref"]) + list(family_additions["nearby_local_ref"])
    compound_support_scope = (
        "same_local_ref"
        if family_additions["same_local_ref"]
        else "nearby_local_ref"
        if family_additions["nearby_local_ref"]
        else ""
    )
    compound_state = "single_family_only"
    review_support_class = ""
    review_gap_class = ""
    next_blocker = ""
    if family_additions["same_local_ref"]:
        if len(family_additions["same_local_ref"]) >= 2:
            compound_state = "multi_family_compound_candidate"
            review_support_class = "multi_family_same_local_ref_support_present"
            review_gap_class = "multi_family_support_below_canonical"
            next_blocker = "multi_family_support_below_canonical"
        else:
            family = family_additions["same_local_ref"][0]
            compound_state = f"semantic_plus_{family}_weak"
            review_support_class = f"semantic_plus_{family}_same_local_ref"
            review_gap_class = f"semantic_plus_{family}_weak"
            next_blocker = f"{family}_anchor_present_but_uncompounded"
    elif family_additions["nearby_local_ref"]:
        if len(family_additions["nearby_local_ref"]) >= 2:
            compound_state = "multi_family_present_but_uncompounded"
        else:
            family = family_additions["nearby_local_ref"][0]
            compound_state = f"semantic_plus_{family}_nearby"
        review_support_class = "multi_family_nearby_support_present"
        review_gap_class = "compound_scope_too_broad"
        next_blocker = "compound_scope_too_broad"
    return {
        "anchor_support_scope": compound_support_scope,
        "anchor_family_additions": family_additions,
        "anchor_family_support_strength": support_strength,
        "compound_candidate_families": compound_candidate_families,
        "compound_support_scope": compound_support_scope,
        "compound_state": compound_state,
        "review_anchor_support_class": review_support_class,
        "review_anchor_gap_class": review_gap_class,
        "next_review_blocker": next_blocker,
    }


def _build_live_side_anchor_support_review(
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    live_materials = left_materials if left_kind == "live" else right_materials
    live_profile = _collect_anchor_type_profile(live_materials)
    raw_text = "\n".join(str(material.get("raw_payload", "") or "") for material in live_materials)
    text_hints = _text_family_hints(raw_text)
    families: List[str] = []
    for family in ("semantic", "structural", "process", "object"):
        if family == "semantic":
            if live_profile.get("semantic"):
                families.append(family)
        elif live_profile.get(family) or text_hints.get(family):
            families.append(family)
    support_class = "missing"
    if len(families) >= 3:
        support_class = "multi_family_live_support_present"
    elif len(families) == 2:
        support_class = "dual_family_live_support_present"
    elif len(families) == 1:
        support_class = f"{families[0]}_only_live_support"
    return {
        "live_side_support_class": support_class,
        "live_side_support_families": families,
        "live_side_missing_families": [family for family in ("semantic", "structural", "process", "object") if family not in families],
        "live_side_anchor_evidence": {
            "semantic_tokens": sorted(list(live_profile.get("semantic", set())))[:6],
            "structural_tokens": sorted(list(live_profile.get("structural", set())))[:6],
            "process_tokens": sorted(list(live_profile.get("process", set())))[:6],
            "object_tokens": sorted(list(live_profile.get("object", set())))[:6],
            "text_hint_families": [family for family in ("structural", "process", "object") if text_hints.get(family)],
        },
    }


def _build_cross_path_canonicalization_review(
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
    best_local_ref: str,
    live_side_review: Dict[str, object],
    anchor_review: Dict[str, object],
) -> Dict[str, object]:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    live_materials = left_materials if left_kind == "live" else right_materials
    imported_materials = right_materials if left_kind == "live" else left_materials
    imported_best_text = ""
    imported_best_profile = {"semantic": set(), "structural": set(), "process": set(), "object": set()}
    for material in imported_materials:
        metadata = dict(material.get("metadata", {}) or {})
        local_ref = str(dict(metadata.get("transformable_handles", {}) or {}).get("source_local_ref", "")).strip()
        if local_ref == best_local_ref:
            imported_best_text = str(material.get("raw_payload", "") or "")
            imported_best_profile = _collect_anchor_type_profile([material])
            break
    live_text = "\n".join(str(material.get("raw_payload", "") or "") for material in live_materials)
    live_hints = _text_family_hints(live_text)
    imported_hints = _text_family_hints(imported_best_text)
    uncorr = set(list(anchor_review.get("compound_candidate_families", []) or [])) & set(list(live_side_review.get("live_side_support_families", []) or []))
    uncorr -= set(list((anchor_review.get("anchor_alignment_evidence", {}) or {}).get("semantic_overlap", [])))
    strengths: Dict[str, str] = {}
    ready: List[str] = []
    hint_only: List[str] = []
    evidence: Dict[str, Dict[str, object]] = {}
    proposals: Dict[str, List[str]] = {}
    proposal_blockers: Dict[str, str] = {}
    semantic_roots = list((anchor_review.get("anchor_alignment_evidence", {}) or {}).get("semantic_overlap", []) or [])
    for family in sorted(set(list(anchor_review.get("compound_candidate_families", []) or [])) & set(list(live_side_review.get("live_side_support_families", []) or []))):
        raw_live_tokens = list((live_side_review.get("live_side_anchor_evidence", {}) or {}).get(f"{family}_tokens", []) or [])
        live_tokens = list(raw_live_tokens)
        if not live_tokens:
            live_tokens = _derived_live_canonicalization_tokens(
                family=family,
                semantic_roots=semantic_roots,
                live_hint=family in list((live_side_review.get("live_side_anchor_evidence", {}) or {}).get("text_hint_families", []) or []),
            )
        raw_imported_tokens = sorted(list(imported_best_profile.get(family, set())))[:6]
        imported_tokens = list(raw_imported_tokens)
        if not imported_tokens:
            imported_tokens = _derived_imported_canonicalization_tokens(
                family=family,
                semantic_roots=semantic_roots,
                imported_hint=bool(imported_hints.get(family)),
            )
        live_hint = family in list((live_side_review.get("live_side_anchor_evidence", {}) or {}).get("text_hint_families", []) or [])
        imported_hint = bool(imported_hints.get(family))
        family_policy = evaluate_canonicalization_family_policy(
            CanonicalizationPolicyContext(
                family=family,
                has_live_tokens=bool(live_tokens),
                has_imported_tokens=bool(imported_tokens),
                live_hint=live_hint,
                imported_hint=imported_hint,
                raw_live_token_source="direct" if raw_live_tokens else "missing",
                raw_imported_token_source="direct" if raw_imported_tokens else "missing",
            )
        )
        strengths[family] = family_policy.strength
        if family_policy.strength == "token_supported":
            ready.append(family)
        elif family_policy.strength in {"text_hint_supported", "one_sided_hint"}:
            hint_only.append(family)
        proposals[family] = _build_canonicalization_proposals(
            family=family,
            semantic_roots=semantic_roots,
            live_tokens=live_tokens,
            imported_tokens=imported_tokens,
            live_hint=live_hint,
            imported_hint=imported_hint,
        )
        proposal_blockers[family] = family_policy.proposal_blocker
        evidence[family] = {
            "live_tokens": live_tokens[:6],
            "imported_tokens": imported_tokens[:6],
            "live_token_source": family_policy.live_token_source,
            "imported_token_source": family_policy.imported_token_source,
            "live_hint": live_hint,
            "imported_hint": imported_hint,
            "best_local_ref": best_local_ref,
        }
    proposal_state = "missing"
    if ready and hint_only:
        proposal_state = "partial_tokenization_progress"
    elif ready:
        proposal_state = "token_supported_candidates_present"
    elif hint_only:
        proposal_state = "hint_only_candidates_present"
    return {
        "cross_path_canonicalization_scope": "best_local_ref",
        "cross_path_canonicalization_strengths": strengths,
        "cross_path_canonicalization_evidence": evidence,
        "cross_path_canonicalization_ready_families": ready,
        "cross_path_canonicalization_hint_only_families": hint_only,
        "cross_path_canonicalization_proposal_state": proposal_state,
        "cross_path_canonicalization_proposals": proposals,
        "cross_path_canonicalization_proposal_blockers": proposal_blockers,
    }


def _build_direct_overlap_review(
    anchor_review: Dict[str, object],
    canonicalization_review: Dict[str, object],
) -> Dict[str, object]:
    overlap_evidence = dict(anchor_review.get("anchor_alignment_evidence", {}) or {})
    canonicalization_evidence = dict(canonicalization_review.get("cross_path_canonicalization_evidence", {}) or {})
    strengths = dict(canonicalization_review.get("cross_path_canonicalization_strengths", {}) or {})
    candidate_families = list(canonicalization_review.get("cross_path_canonicalization_ready_families", []) or [])
    direct_candidates: List[str] = []
    family_ready: Dict[str, bool] = {}
    family_blockers: Dict[str, str] = {}
    family_rule_state: Dict[str, str] = {}
    evidence: Dict[str, Dict[str, object]] = {}
    canonicalizable_token_pair_count = 0
    noncanonical_token_pair_count = 0
    any_live_form_missing = False
    any_alignment_rule_missing = False
    for family in candidate_families:
        family_overlap = list(overlap_evidence.get(f"{family}_overlap", []) or [])
        family_evidence = dict(canonicalization_evidence.get(family, {}) or {})
        live_tokens = [_normalize_token(str(v)) for v in list(family_evidence.get("live_tokens", []) or []) if _normalize_token(str(v))]
        imported_tokens = [_normalize_token(str(v)) for v in list(family_evidence.get("imported_tokens", []) or []) if _normalize_token(str(v))]
        live_token_source = str(family_evidence.get("live_token_source", "")).strip() or "missing"
        imported_token_source = str(family_evidence.get("imported_token_source", "")).strip() or "missing"
        pair_overlap = sorted(set(live_tokens) & set(imported_tokens))
        canonicalizable_token_pair_count += len(pair_overlap)
        direct_candidates.append(family)
        family_policy = evaluate_direct_overlap_family_policy(
            DirectOverlapFamilyPolicyContext(
                family=family,
                family_overlap_count=len(family_overlap),
                pair_overlap_count=len(pair_overlap),
                live_token_source=live_token_source,
                imported_token_source=imported_token_source,
                has_live_tokens=bool(live_tokens),
            )
        )
        family_ready[family] = family_policy.ready
        family_blockers[family] = family_policy.blocker
        family_rule_state[family] = family_policy.rule_state
        if family_policy.blocker == "token_pair_exists_but_alignment_rule_not_satisfied":
            any_alignment_rule_missing = True
            noncanonical_token_pair_count += len(pair_overlap)
        elif family_policy.blocker == "live_side_anchor_form_missing":
            any_live_form_missing = True
        evidence[family] = {
            "direct_overlap_tokens": family_overlap[:6],
            "canonicalizable_token_pairs": pair_overlap[:6],
            "live_tokens": live_tokens[:6],
            "imported_tokens": imported_tokens[:6],
            "live_token_source": live_token_source,
            "imported_token_source": imported_token_source,
        }
    aggregate_policy = evaluate_direct_overlap_aggregate_policy(
        DirectOverlapAggregatePolicyContext(
            candidate_families=direct_candidates,
            any_alignment_rule_missing=any_alignment_rule_missing,
            any_live_form_missing=any_live_form_missing,
            canonicalizable_token_pair_count=canonicalizable_token_pair_count,
            family_rule_states=family_rule_state,
            has_live_anchor_form=any(
        list((canonicalization_evidence.get(family, {}) or {}).get("live_tokens", []) or [])
        for family in candidate_families
            ),
        )
    )
    return {
        "direct_overlap_candidate_families": direct_candidates,
        "direct_overlap_gap_class": aggregate_policy.direct_overlap_gap_class,
        "direct_overlap_evidence": evidence,
        "family_canonicalization_strengths": {family: str(strengths.get(family, "")).strip() for family in candidate_families},
        "family_direct_overlap_ready": family_ready,
        "family_direct_overlap_blockers": family_blockers,
        "family_rule_refinement_state": family_rule_state,
        "direct_overlap_candidate_lead_family": aggregate_policy.direct_overlap_candidate_lead_family,
        "token_pair_alignment_state": aggregate_policy.token_pair_alignment_state,
        "live_anchor_form_state": aggregate_policy.live_anchor_form_state,
        "canonicalizable_token_pair_count": canonicalizable_token_pair_count,
        "noncanonical_token_pair_count": noncanonical_token_pair_count,
        "family_mapping_state": aggregate_policy.family_mapping_state,
    }


def _build_space_entry_review(
    *,
    gate_vector: Dict[str, object],
    anchor_review: Dict[str, object],
    direct_overlap_review: Dict[str, object],
) -> Dict[str, object]:
    translation_gate = bool(gate_vector.get("translation_gate"))
    processing_gate = bool(gate_vector.get("processing_gate"))
    observer_gate = bool(gate_vector.get("observer_gate"))
    canonical_anchor_gate = bool(gate_vector.get("canonical_anchor_gate"))
    same_local_strength = int(dict(anchor_review.get("anchor_family_support_strength", {}) or {}).get("same_local_ref", 0) or 0)
    direct_candidates = list(direct_overlap_review.get("direct_overlap_candidate_families", []) or [])
    lead_family = str(direct_overlap_review.get("direct_overlap_candidate_lead_family", "")).strip()
    policy = evaluate_space_entry_policy(
        SpaceEntryPolicyContext(
            translation_gate=translation_gate,
            processing_gate=processing_gate,
            observer_gate=observer_gate,
            canonical_anchor_gate=canonical_anchor_gate,
            same_local_ref_support_strength=same_local_strength,
            direct_overlap_candidate_count=len(direct_candidates),
            canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),
            direct_overlap_gap_class=str(direct_overlap_review.get("direct_overlap_gap_class", "")).strip(),
            direct_overlap_candidate_lead_family=lead_family,
            direct_overlap_candidate_families=direct_candidates,
        )
    )
    return {
        "space_entry_state": policy.space_entry_state,
        "space_entry_vector": {
            "translation_gate": translation_gate,
            "processing_gate": processing_gate,
            "observer_gate": observer_gate,
            "same_local_ref_support_strength": same_local_strength,
            "direct_overlap_candidate_count": len(direct_candidates),
            "canonicalizable_token_pair_count": int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),
        },
        "space_entry_ready_families": direct_candidates,
        "space_entry_lead_family": lead_family,
        "space_entry_blocker": policy.space_entry_blocker,
        "space_entry_reason": policy.space_entry_reason,
    }


def _derived_imported_canonicalization_tokens(
    *,
    family: str,
    semantic_roots: Sequence[str],
    imported_hint: bool,
) -> List[str]:
    if not imported_hint:
        return []
    rows: List[str] = []
    normalized_roots = [_normalize_token(value) for value in semantic_roots if _normalize_token(value)]
    if family == "structural":
        for root in normalized_roots[:3]:
            if root in {"graph", "rag", "graph rag"}:
                rows.append(f"{root} 구조")
                rows.append(f"{root} structure")
    elif family == "object":
        for token in ("property", "ontology", "object"):
            rows.append(token)
    elif family == "process":
        for root in normalized_roots[:2]:
            rows.append(f"{root} retrieval")
    deduped: List[str] = []
    seen: Set[str] = set()
    for value in rows:
        norm = _normalize_token(value)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        deduped.append(norm)
    return deduped[:6]


def _derived_live_canonicalization_tokens(
    *,
    family: str,
    semantic_roots: Sequence[str],
    live_hint: bool,
) -> List[str]:
    if not live_hint:
        return []
    rows: List[str] = []
    normalized_roots = [_normalize_token(value) for value in semantic_roots if _normalize_token(value)]
    if family == "structural":
        for root in normalized_roots[:3]:
            if root in {"graph", "rag", "graph rag"}:
                rows.append(f"{root} 구조")
                rows.append(f"{root} structure")
    elif family == "object":
        for token in ("property", "ontology", "object"):
            rows.append(token)
    elif family == "process":
        for root in normalized_roots[:2]:
            rows.append(f"{root} retrieval")
    deduped: List[str] = []
    seen: Set[str] = set()
    for value in rows:
        norm = _normalize_token(value)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        deduped.append(norm)
    return deduped[:6]


def _build_canonicalization_proposals(
    *,
    family: str,
    semantic_roots: Sequence[str],
    live_tokens: Sequence[str],
    imported_tokens: Sequence[str],
    live_hint: bool,
    imported_hint: bool,
) -> List[str]:
    proposals: List[str] = []
    roots = [_normalize_token(value) for value in semantic_roots if _normalize_token(value)]
    if family == "structural":
        for root in roots[:2]:
            proposals.append(f"{root} structure")
        proposals.extend([_normalize_token(value) for value in live_tokens[:2]])
    elif family == "object":
        for token in ("property", "ontology", "object"):
            if token in " ".join(roots + list(live_tokens)).lower() or live_hint:
                proposals.append(token)
        proposals.extend([_normalize_token(value) for value in imported_tokens[:2]])
    elif family == "process":
        for root in roots[:2]:
            proposals.append(f"{root} retrieval")
    deduped: List[str] = []
    seen: Set[str] = set()
    for value in proposals:
        norm = _normalize_token(value)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        deduped.append(norm)
    return deduped[:4]


def _nearby_local_refs(best_local_ref: str, local_refs: Sequence[str]) -> List[str]:
    match = re.search(r"^(.*_)(\d+)$", best_local_ref)
    if not match:
        return []
    prefix = match.group(1)
    current = int(match.group(2))
    rows: List[tuple[int, str]] = []
    for local_ref in local_refs:
        if local_ref == best_local_ref:
            continue
        other = re.search(r"^(.*_)(\d+)$", local_ref)
        if not other or other.group(1) != prefix:
            continue
        distance = abs(int(other.group(2)) - current)
        if 0 < distance <= 2:
            rows.append((distance, local_ref))
    rows.sort(key=lambda row: (row[0], row[1]))
    return [local_ref for _, local_ref in rows[:6]]


def _text_family_hints(text: str) -> Dict[str, Set[str]]:
    lowered = _normalize_token(text)
    hints: Dict[str, Set[str]] = {"structural": set(), "process": set(), "object": set()}
    if any(value in lowered for value in {"구조", "관계", "graph db", "database", "node", "relationship", "relation"}):
        hints["structural"].add("text_cue")
    if any(value in lowered for value in {"검색", "질의", "추론", "generation", "retrieval", "multi hop", "multi-hop", "처리"}):
        hints["process"].add("text_cue")
    if any(value in lowered for value in {"llm", "property", "object", "ontology", "속성", "객체"}):
        hints["object"].add("text_cue")
    return hints


def _build_weak_support_summary(possibility_basis: Dict[str, object]) -> Dict[str, object]:
    observer_affinity = dict(possibility_basis.get("observer_affinity", {}) or {})
    translation_alignment = dict(possibility_basis.get("translation_assisted_alignment", {}) or {})
    interplay = dict(possibility_basis.get("translation_processing_interplay", {}) or {})
    return {
        "partial_anchor_alignment_count": len(list(possibility_basis.get("partial_anchor_alignment", []) or [])),
        "weak_processing_overlap_count": len(list(possibility_basis.get("weak_processing_overlap", []) or [])),
        "structural_echo_count": len(list(possibility_basis.get("structural_echo", []) or [])),
        "observer_affinity_available": bool(observer_affinity.get("available")),
        "shared_scene_or_flow_hint_count": len(list(possibility_basis.get("shared_scene_or_flow_hint", []) or [])),
        "translation_assisted_alignment_available": bool(translation_alignment.get("available")),
        "translation_assisted_local_ref_count": int(translation_alignment.get("matched_local_ref_count", 0) or 0),
        "translation_processing_convergence_level": str(interplay.get("convergence_level", "")).strip(),
    }


def _build_blocked_alignment_evidence(possibility_basis: Dict[str, object]) -> Dict[str, object]:
    translation_alignment = dict(possibility_basis.get("translation_assisted_alignment", {}) or {})
    interplay = dict(possibility_basis.get("translation_processing_interplay", {}) or {})
    return {
        "partial_anchor_alignment": list(possibility_basis.get("partial_anchor_alignment", []) or [])[:3],
        "weak_processing_overlap": list(possibility_basis.get("weak_processing_overlap", []) or [])[:3],
        "partial_handle_overlap": list(possibility_basis.get("partial_handle_overlap", []) or [])[:3],
        "shared_scene_or_flow_hint": list(possibility_basis.get("shared_scene_or_flow_hint", []) or [])[:3],
        "translation_assisted_handles": list(translation_alignment.get("matched_handles", []) or [])[:3],
        "translation_assisted_local_refs": list(translation_alignment.get("matched_local_refs", []) or [])[:3],
        "translation_processing_best_local_ref": str(interplay.get("best_local_ref", "")).strip(),
        "translation_processing_best_score": float(interplay.get("best_score", 0.0) or 0.0),
        "translation_processing_convergence_level": str(interplay.get("convergence_level", "")).strip(),
    }


def _build_translation_assisted_alignment(
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    if {left_kind, right_kind} != {"live", "imported"}:
        return {"available": False, "translation_scope_used": ""}
    live_materials = left_materials if left_kind == "live" else right_materials
    imported_materials = right_materials if left_kind == "live" else left_materials
    live_handles = _collect_live_alignment_handles(live_materials)
    if not live_handles:
        return {"available": False, "translation_scope_used": "local_ref"}
    matched_local_refs: List[str] = []
    matched_handles: List[str] = []
    matched_rows: List[Dict[str, object]] = []
    seen_pairs: Set[tuple[str, str]] = set()
    for material in imported_materials:
        metadata = dict(material.get("metadata", {}) or {})
        local_ref = str(dict(metadata.get("transformable_handles", {}) or {}).get("source_local_ref", "")).strip()
        for row in list(metadata.get("translated_handles", []) or []):
            if str(row.get("translation_scope", "")).strip() != "local_ref":
                continue
            translated_handle = _normalize_token(str(row.get("translated_handle", "")).strip())
            if not translated_handle or translated_handle not in live_handles:
                continue
            scoped_ref = str(row.get("translation_source_local_ref", "")).strip()
            if local_ref and scoped_ref and scoped_ref != local_ref:
                continue
            dedupe = (local_ref or scoped_ref, translated_handle)
            if dedupe in seen_pairs:
                continue
            seen_pairs.add(dedupe)
            if (local_ref or scoped_ref) and (local_ref or scoped_ref) not in matched_local_refs:
                matched_local_refs.append(local_ref or scoped_ref)
            if translated_handle not in matched_handles:
                matched_handles.append(translated_handle)
            matched_rows.append(
                {
                    "source_local_ref": local_ref or scoped_ref,
                    "translated_handle": translated_handle,
                    "translation_basis": str(row.get("translation_basis", "")).strip(),
                    "translation_confidence": float(row.get("translation_confidence", 0.0) or 0.0),
                }
            )
    return {
        "available": bool(matched_rows),
        "translation_scope_used": "local_ref",
        "matched_local_ref_count": len(matched_local_refs),
        "matched_local_refs": matched_local_refs[:4],
        "matched_handles": matched_handles[:4],
        "matched_rows": matched_rows[:8],
    }


def _build_translation_processing_interplay(
    left_materials: Sequence[Dict[str, object]],
    right_materials: Sequence[Dict[str, object]],
) -> Dict[str, object]:
    left_kind = _dominant_path_kind(left_materials)
    right_kind = _dominant_path_kind(right_materials)
    if {left_kind, right_kind} != {"live", "imported"}:
        return {"available": False}
    live_materials = left_materials if left_kind == "live" else right_materials
    imported_materials = right_materials if left_kind == "live" else left_materials
    live_profiles = [_processing_profile(material) for material in live_materials]
    live_profiles = [row for row in live_profiles if row]
    if not live_profiles:
        return {"available": False, "convergence_level": "missing_live_processing"}
    rows: List[Dict[str, object]] = []
    for material in imported_materials:
        metadata = dict(material.get("metadata", {}) or {})
        translated_handles = list(metadata.get("translated_handles", []) or [])
        if not translated_handles:
            continue
        imported_profile = _processing_profile(material)
        if not imported_profile:
            continue
        best = max(_processing_similarity(imported_profile, live_profile) for live_profile in live_profiles)
        local_ref = str(dict(metadata.get("transformable_handles", {}) or {}).get("source_local_ref", "")).strip()
        rows.append(
            {
                "source_local_ref": local_ref,
                "score": best,
                "scene": str(imported_profile.get("scene", "")).strip(),
                "flow": str(imported_profile.get("flow", "")).strip(),
                "translated_handles": [
                    str(row.get("translated_handle", "")).strip()
                    for row in translated_handles
                    if str(row.get("translated_handle", "")).strip()
                ][:4],
            }
        )
    rows.sort(key=lambda row: row["score"], reverse=True)
    best_score = float(rows[0]["score"]) if rows else 0.0
    convergence_level = "none"
    if best_score >= 0.82:
        convergence_level = "strong"
    elif best_score >= 0.64:
        convergence_level = "partial"
    elif rows:
        convergence_level = "weak"
    return {
        "available": bool(rows),
        "best_score": round(best_score, 4),
        "best_local_ref": str(rows[0]["source_local_ref"]).strip() if rows else "",
        "convergence_level": convergence_level,
        "top_rows": rows[:6],
    }


def _collect_live_alignment_handles(materials: Sequence[Dict[str, object]]) -> Set[str]:
    rows: Set[str] = set()
    for material in materials:
        metadata = dict(material.get("metadata", {}) or {})
        bundle = dict(metadata.get("anchor_bundle", {}) or {})
        for item in list(bundle.get("representative_anchors", []) or []):
            for value in (
                str(item.get("canonical_key", "")).strip(),
                str(item.get("display_label", "")).strip(),
            ):
                token = _normalize_token(value)
                if token:
                    rows.add(token)
        for value in list(bundle.get("supporting_anchors", []) or []):
            token = _normalize_token(str(value).strip())
            if token:
                rows.add(token)
    return rows


def _normalize_token(value: str) -> str:
    lowered = value.strip().lower().replace("_", " ").replace("-", " ").replace("/", " ")
    lowered = re.sub(r"\s+", " ", lowered)
    return lowered.strip()


def _processing_profile(material: Dict[str, object]) -> Dict[str, object]:
    metadata = dict(material.get("metadata", {}) or {})
    processing = dict(metadata.get("processing_values", {}) or {})
    if not processing:
        return {}
    return {
        "scene": str(processing.get("scene", metadata.get("scene", ""))).strip(),
        "flow": str(processing.get("flow", metadata.get("flow", ""))).strip(),
        "D": float(processing.get("D", metadata.get("D", 0.5)) or 0.5),
        "I": float(processing.get("I", metadata.get("I", 0.5)) or 0.5),
        "S": float(processing.get("S", metadata.get("S", 0.5)) or 0.5),
    }


def _processing_similarity(left: Dict[str, object], right: Dict[str, object]) -> float:
    score = 1.0
    score -= abs(float(left.get("D", 0.5)) - float(right.get("D", 0.5))) * 0.25
    score -= abs(float(left.get("I", 0.5)) - float(right.get("I", 0.5))) * 0.2
    score -= abs(float(left.get("S", 0.5)) - float(right.get("S", 0.5))) * 0.15
    if str(left.get("scene", "")) and left.get("scene") != right.get("scene"):
        score -= 0.2
    if str(left.get("flow", "")) and left.get("flow") != right.get("flow"):
        score -= 0.2
    return round(max(0.0, min(1.0, score)), 4)


def _material_side_ref(materials: Sequence[Dict[str, object]]) -> str:
    source_labels = sorted(
        {
            str((material.get("metadata", {}) or {}).get("source_label", "")).strip()
            for material in materials
            if str((material.get("metadata", {}) or {}).get("source_label", "")).strip()
        }
    )
    if source_labels:
        return source_labels[0]
    material_ids = sorted(
        {
            str(material.get("id", "")).strip()
            for material in materials
            if str(material.get("id", "")).strip()
        }
    )
    return material_ids[0] if material_ids else ""


def _build_review_timestamp(
    *,
    bridge_mode: str,
    review_state: str,
    trace_temperature: str,
    lifecycle_stage: str,
    space_entry_state: str,
    next_review_blocker: str,
    left_ref: str,
    right_ref: str,
) -> ReviewTimestamp:
    evaluated_at = datetime.now(timezone.utc).isoformat()
    signature_parts = [
        bridge_mode.strip(),
        review_state.strip(),
        trace_temperature.strip(),
        lifecycle_stage.strip(),
        space_entry_state.strip(),
        next_review_blocker.strip(),
        left_ref.strip(),
        right_ref.strip(),
    ]
    return ReviewTimestamp(
        evaluated_at=evaluated_at,
        state_signature="|".join(part for part in signature_parts if part),
    )


def _local_space_label(service: FormationService, local_space_id: str) -> str:
    local_space = service.local_spaces.get(local_space_id) or {}
    source_label = str(local_space.get("source_label", "")).strip()
    if source_label:
        return source_label
    label = str(local_space.get("label", "")).strip()
    return label or local_space_id
