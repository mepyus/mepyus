from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

from app.core.states import (
    BridgeState,
    CarryoverRisk,
    CellState,
    ComparisonMemoryReason,
    EmergenceStatus,
    GateBlockerSummary,
    GroundingStatus,
    LocalSpaceState,
    MaturationState,
    PacketTexture,
    SeedState,
    TraceabilityStatus,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def frozen_dict() -> Dict[str, Any]:
    return {}


@dataclass(frozen=True)
class SupportRef:
    ref_kind: str
    ref_id: str
    note: Optional[str] = None


@dataclass(frozen=True)
class PressureAxis:
    axis: str
    strength_hint: float
    support_refs: Tuple[SupportRef, ...] = ()


@dataclass(frozen=True)
class Material:
    material_id: str
    raw_payload: str
    created_at: str
    actor_id: str
    session_id: str
    project_id: str
    source_type: str
    source_ref: str
    lineage_refs: Tuple[str, ...] = ()
    family_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=frozen_dict)


@dataclass(frozen=True)
class Trace:
    trace_id: str
    material_refs: Tuple[str, ...]
    evidence_kind: str
    support_refs: Tuple[SupportRef, ...]
    note: Optional[str] = None
    created_at: str = field(default_factory=utc_now_iso)


@dataclass(frozen=True)
class PointSeed:
    seed_id: str
    material_refs: Tuple[str, ...]
    trace_refs: Tuple[str, ...]
    pressure_profile_id: str
    state: SeedState
    created_at: str
    lineage_refs: Tuple[str, ...] = ()


@dataclass(frozen=True)
class PressureProfile:
    profile_id: str
    axes: Tuple[PressureAxis, ...]
    created_at: str
    support_refs: Tuple[SupportRef, ...] = ()


@dataclass(frozen=True)
class SpaceBoundary:
    interior_refs: Tuple[str, ...]
    exterior_refs: Tuple[str, ...]
    permeability_hint: float


@dataclass(frozen=True)
class SpaceCell:
    cell_id: str
    material_refs: Tuple[str, ...]
    trace_refs: Tuple[str, ...]
    seed_refs: Tuple[str, ...]
    pressure_profile_id: str
    boundary: SpaceBoundary
    state: CellState
    cohesion_note: Optional[str]
    created_at: str


@dataclass(frozen=True)
class LocalSpace:
    local_space_id: str
    cell_refs: Tuple[str, ...]
    pressure_profile_id: Optional[str]
    state: LocalSpaceState
    created_at: str
    bridge_trace_refs: Tuple[str, ...] = ()


@dataclass(frozen=True)
class BridgeTrace:
    bridge_id: str
    from_local_space_id: str
    to_local_space_id: str
    trace_refs: Tuple[str, ...]
    state: BridgeState
    created_at: str
    note: Optional[str] = None


@dataclass(frozen=True)
class EngineStateRecord:
    asset_id: str
    asset_name: str
    source_type: str
    packet_texture: PacketTexture
    grounding_status: GroundingStatus
    emergence_status: EmergenceStatus
    carryover_risk: CarryoverRisk
    maturation_state: MaturationState
    traceability_status: TraceabilityStatus
    comparison_memory_reason: Tuple[ComparisonMemoryReason, ...] = ()
    gate_blocker_summary: Tuple[GateBlockerSummary, ...] = ()
    state_notes: Optional[str] = None
    evidence_refs: Tuple[SupportRef, ...] = ()
    updated_at: str = field(default_factory=utc_now_iso)
    experimental_namespace: Dict[str, Any] = field(default_factory=frozen_dict)


def to_record(entity: Any) -> Dict[str, Any]:
    return asdict(entity)
