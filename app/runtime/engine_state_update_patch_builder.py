from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

from app.core.models.entities import EngineStateRecord, SupportRef
from app.core.state_store.engine_state_update_policy import CANONICAL_STATE_FIELDS, FORBIDDEN_CANONICAL_FIELDS
from app.core.states import (
    CarryoverRisk,
    ComparisonMemoryReason,
    EmergenceStatus,
    GateBlockerSummary,
    GroundingStatus,
    MaturationState,
    PacketTexture,
    TraceabilityStatus,
    UpdateTriggerType,
)


PATCH_ALLOWED_FIELDS = set(CANONICAL_STATE_FIELDS) | {"state_notes"}
ARRAY_FIELDS = {"comparison_memory_reason", "gate_blocker_summary"}


def _dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _merge_evidence_refs(previous_refs: List[Dict[str, Any]], incoming_refs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: List[Dict[str, Any]] = []
    seen = set()
    for ref in previous_refs + incoming_refs:
        key = (ref.get("ref_kind"), ref.get("ref_id"), ref.get("note"))
        if key in seen:
            continue
        seen.add(key)
        merged.append(
            {
                "ref_kind": ref.get("ref_kind"),
                "ref_id": ref.get("ref_id"),
                "note": ref.get("note"),
            }
        )
    return merged


def _normalize_patch_value(field: str, value: Any) -> Any:
    if field in ARRAY_FIELDS:
        if value is None:
            return []
        if not isinstance(value, list):
            raise ValueError(f"{field} patch must be a list")
        return _dedupe_preserve_order(str(item) for item in value)
    if hasattr(value, "value"):
        return value.value
    if value is None:
        return None
    return str(value) if isinstance(value, bool) else value


def build_runtime_state_patch_proposal(
    *,
    asset_id: str,
    update_reason: str,
    evidence_type: str,
    evidence_summary: str,
    evidence_refs: List[Dict[str, Any]],
    proposed_changes: Dict[str, Any],
    experimental_namespace: Optional[Dict[str, Any]] = None,
    trigger_type: UpdateTriggerType = UpdateTriggerType.RUNTIME_EVIDENCE,
    replace_array_fields: Optional[List[str]] = None,
) -> Dict[str, Any]:
    if not asset_id:
        raise ValueError("asset_id is required")
    if not update_reason:
        raise ValueError("update_reason is required")
    if not evidence_type:
        raise ValueError("evidence_type is required")
    if not evidence_summary:
        raise ValueError("evidence_summary is required")
    if not evidence_refs:
        raise ValueError("evidence_refs are required")

    canonical_changes: Dict[str, Any] = {}
    experimental = dict(experimental_namespace or {})
    for key, value in proposed_changes.items():
        if key in FORBIDDEN_CANONICAL_FIELDS or key not in PATCH_ALLOWED_FIELDS:
            experimental[key] = value
            continue
        canonical_changes[key] = _normalize_patch_value(key, value)

    replace_fields = [
        field
        for field in (replace_array_fields or [])
        if field in ARRAY_FIELDS
    ]

    return {
        "asset_id": asset_id,
        "update_trigger_type": trigger_type.value,
        "update_reason": update_reason,
        "evidence_type": evidence_type,
        "evidence_summary": evidence_summary,
        "evidence_refs": evidence_refs,
        "proposed_changes": canonical_changes,
        "experimental_namespace": experimental,
        "replace_array_fields": replace_fields,
    }


def build_state_record_payload_from_patch(
    latest_state: Dict[str, Any],
    proposal: Dict[str, Any],
) -> Dict[str, Any]:
    if not latest_state:
        raise ValueError("latest_state is required to build runtime update payload")

    merged = dict(latest_state)
    proposed_changes = proposal.get("proposed_changes", {})
    replace_array_fields = set(proposal.get("replace_array_fields", []))
    for field, value in proposed_changes.items():
        if field in ARRAY_FIELDS:
            previous = list(merged.get(field, []))
            if field in replace_array_fields:
                merged[field] = list(value)
            else:
                merged[field] = _dedupe_preserve_order(previous + list(value))
            continue
        merged[field] = value

    merged["state_notes"] = proposed_changes.get("state_notes", merged.get("state_notes"))
    merged["evidence_refs"] = _merge_evidence_refs(
        list(merged.get("evidence_refs", [])),
        list(proposal["evidence_refs"]),
    )
    experimental = dict(merged.get("experimental_namespace") or {})
    experimental.update(proposal.get("experimental_namespace") or {})
    experimental["runtime_update_context"] = {
        "evidence_type": proposal["evidence_type"],
        "evidence_summary": proposal["evidence_summary"],
    }
    merged["experimental_namespace"] = experimental
    return merged


def to_engine_state_record(payload: Dict[str, Any]) -> EngineStateRecord:
    return EngineStateRecord(
        asset_id=payload["asset_id"],
        asset_name=payload["asset_name"],
        source_type=payload["source_type"],
        packet_texture=PacketTexture(payload["packet_texture"]),
        grounding_status=GroundingStatus(payload["grounding_status"]),
        emergence_status=EmergenceStatus(payload["emergence_status"]),
        carryover_risk=CarryoverRisk(payload["carryover_risk"]),
        maturation_state=MaturationState(payload["maturation_state"]),
        traceability_status=TraceabilityStatus(payload["traceability_status"]),
        comparison_memory_reason=tuple(ComparisonMemoryReason(item) for item in payload.get("comparison_memory_reason", [])),
        gate_blocker_summary=tuple(GateBlockerSummary(item) for item in payload.get("gate_blocker_summary", [])),
        state_notes=payload.get("state_notes"),
        evidence_refs=tuple(
            SupportRef(
                ref_kind=ref["ref_kind"],
                ref_id=ref["ref_id"],
                note=ref.get("note"),
            )
            for ref in payload.get("evidence_refs", [])
        ),
        experimental_namespace=dict(payload.get("experimental_namespace") or {}),
    )
