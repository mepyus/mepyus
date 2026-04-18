from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, Iterable, Optional

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


CANONICAL_STATE_FIELDS = (
    "packet_texture",
    "grounding_status",
    "emergence_status",
    "carryover_risk",
    "maturation_state",
    "traceability_status",
    "comparison_memory_reason",
    "gate_blocker_summary",
)


FIELD_ALLOWED_VALUES = {
    "packet_texture": {item.value for item in PacketTexture},
    "grounding_status": {item.value for item in GroundingStatus},
    "emergence_status": {item.value for item in EmergenceStatus},
    "carryover_risk": {item.value for item in CarryoverRisk},
    "maturation_state": {item.value for item in MaturationState},
    "traceability_status": {item.value for item in TraceabilityStatus},
    "comparison_memory_reason": {item.value for item in ComparisonMemoryReason},
    "gate_blocker_summary": {item.value for item in GateBlockerSummary},
}


FORBIDDEN_CANONICAL_FIELDS = {
    "context_unit_name",
    "paragraph_role_name",
    "pivot_label",
    "compression_label",
    "business_power_shift",
    "orchestration",
}


def to_record_dict(record: Any) -> Dict[str, Any]:
    if is_dataclass(record):
        return asdict(record)
    return dict(record)


def _normalize_value(value: Any) -> Any:
    if isinstance(value, tuple):
        return [_normalize_value(item) for item in value]
    if isinstance(value, list):
        return [_normalize_value(item) for item in value]
    if hasattr(value, "value"):
        return value.value
    return value


def canonical_state_changed(previous: Optional[Dict[str, Any]], incoming: Dict[str, Any]) -> bool:
    if previous is None:
        return True
    for field in CANONICAL_STATE_FIELDS:
        if previous.get(field) != incoming.get(field):
            return True
    return False


def validate_enums(record: Dict[str, Any]) -> None:
    for field, allowed_values in FIELD_ALLOWED_VALUES.items():
        value = record.get(field)
        if field in {"comparison_memory_reason", "gate_blocker_summary"}:
            if not isinstance(value, list):
                raise ValueError(f"{field} must be a list")
            invalid = [entry for entry in value if entry not in allowed_values]
            if invalid:
                raise ValueError(f"{field} contains invalid values: {invalid}")
            continue
        if value not in allowed_values:
            raise ValueError(f"{field} has invalid value: {value}")


def sanitize_canonical_contamination(record: Dict[str, Any]) -> Dict[str, Any]:
    payload = dict(record)
    experimental = dict(payload.get("experimental_namespace") or {})
    for field in list(payload.keys()):
        if field in FORBIDDEN_CANONICAL_FIELDS:
            experimental[field] = payload.pop(field)
    payload["experimental_namespace"] = experimental
    return payload


def validate_evidence_presence(record: Dict[str, Any], trigger_type: UpdateTriggerType, previous: Optional[Dict[str, Any]]) -> None:
    changed = canonical_state_changed(previous, record)
    if not changed:
        return
    if trigger_type == UpdateTriggerType.MANUAL_CORRECTION and not record.get("update_reason"):
        raise ValueError("manual_correction requires update_reason")
    evidence_refs = record.get("evidence_refs") or []
    if not evidence_refs:
        raise ValueError("state-changing update requires evidence_refs")


def prepare_state_update(
    record: Any,
    *,
    previous_latest: Optional[Dict[str, Any]] = None,
    trigger_type: UpdateTriggerType = UpdateTriggerType.RUNTIME_EVIDENCE,
    update_reason: Optional[str] = None,
    schema_version: str = "engine_state_schema_v1",
) -> Dict[str, Any]:
    payload = {key: _normalize_value(value) for key, value in to_record_dict(record).items()}
    payload = sanitize_canonical_contamination(payload)
    payload["schema_version"] = schema_version
    payload["update_trigger_type"] = trigger_type.value
    payload["update_reason"] = update_reason
    validate_enums(payload)
    validate_evidence_presence(payload, trigger_type, previous_latest)
    return payload
