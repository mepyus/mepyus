from __future__ import annotations

import hashlib
from typing import Any, Dict, List, Optional

from app.measurement.schema import MeasurementRecord


def _observer_measurement_id(*parts: str) -> str:
    digest = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()
    return f"obs_{digest[:16]}"


def build_revision_judgment(
    *,
    fragment_id: str,
    source_id: str,
    column_key: str,
    previous_value: Dict[str, Any],
    new_value: Dict[str, Any],
    reason: str,
    reason_family: str = "",
    operator: str = "user",
    batch_id: str = "",
    session_id: str = "",
    related_measurement_id: str = "",
    notes: str = "",
    confidence: float = 0.8,
) -> MeasurementRecord:
    measurement_id = _observer_measurement_id(
        "revision_judgment",
        fragment_id,
        column_key,
        reason,
        batch_id,
        session_id,
    )
    return MeasurementRecord(
        measurement_id=measurement_id,
        fragment_id=fragment_id,
        measurement_type="revision_judgment",
        column_key=column_key,
        value={
            "previous_value": previous_value,
            "new_value": new_value,
            "reason": reason,
            "reason_family": reason_family,
            "related_measurement_id": related_measurement_id,
            "notes": notes,
        },
        basis="manual or reviewer revision judgment",
        evidence_text=reason,
        confidence=confidence,
        origin=operator,
        status="active",
        provisional=False,
        metadata={
            "source_id": source_id,
            "operator": operator,
            "ingest_batch_id": batch_id,
            "ingest_session_id": session_id,
            "observer_layer": "history",
            "revision_of": related_measurement_id,
        },
    )


def build_connection_observation(
    *,
    fragment_id: str,
    counterpart_fragment_id: str,
    source_id: str,
    counterpart_source_id: str,
    relation_status: str,
    reason: str,
    reason_family: str = "",
    shared_signals: Optional[List[str]] = None,
    missing_signals: Optional[List[str]] = None,
    operator: str = "system",
    batch_id: str = "",
    session_id: str = "",
    notes: str = "",
    confidence: float = 0.45,
) -> MeasurementRecord:
    measurement_id = _observer_measurement_id(
        "connection_observation",
        fragment_id,
        counterpart_fragment_id,
        relation_status,
        reason,
        batch_id,
        session_id,
    )
    return MeasurementRecord(
        measurement_id=measurement_id,
        fragment_id=fragment_id,
        measurement_type="connection_observation",
        column_key=f"{relation_status}:{counterpart_fragment_id}",
        value={
            "relation_status": relation_status,
            "counterpart_fragment_id": counterpart_fragment_id,
            "counterpart_source_id": counterpart_source_id,
            "reason": reason,
            "reason_family": reason_family,
            "shared_signals": shared_signals or [],
            "missing_signals": missing_signals or [],
            "notes": notes,
        },
        basis="observer-layer connection judgment",
        evidence_text=reason,
        confidence=confidence,
        origin=operator,
        status="active",
        provisional=relation_status != "accepted_connection",
        metadata={
            "source_id": source_id,
            "counterpart_source_id": counterpart_source_id,
            "counterpart_fragment_id": counterpart_fragment_id,
            "operator": operator,
            "ingest_batch_id": batch_id,
            "ingest_session_id": session_id,
            "observer_layer": "observation",
        },
    )
