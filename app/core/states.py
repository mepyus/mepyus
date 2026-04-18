from enum import Enum


class SeedState(str, Enum):
    ISOLATED = "isolated"
    FORMING = "forming"
    REENTERING = "reentering"
    CELL_CANDIDATE = "cell_candidate"
    CELL_BOUND = "cell_bound"


class CellState(str, Enum):
    CANDIDATE = "candidate"
    HELD = "held"
    UNSTABLE = "unstable"
    REENTERING = "reentering"
    DISSOLVED = "dissolved"


class LocalSpaceState(str, Enum):
    FORMING = "forming"
    STABLE_LOCAL = "stable_local"
    SPARSE = "sparse"
    BOUNDARY_HEAVY = "boundary_heavy"
    BRIDGE_EXPOSED = "bridge_exposed"


class BridgeState(str, Enum):
    CANDIDATE = "candidate"
    OBSERVED = "observed"
    HELD = "held"


class PacketTexture(str, Enum):
    MODERATELY_OPEN = "moderately_open"
    STRUCTURED_OPEN_LOW_EMERGENCE = "structured_open_low_emergence"
    OVERCOMPRESSED_CLOSURE_HEAVY = "overcompressed_closure_heavy"
    OVERCOMPRESSED_BREATHING = "overcompressed_breathing"


class GroundingStatus(str, Enum):
    DIRECT_GROUNDED = "direct_grounded"
    PARTIALLY_GROUNDED = "partially_grounded"
    FALLBACK_GROUNDED = "fallback_grounded"
    EMPTY_REF_RISK = "empty_ref_risk"


class EmergenceStatus(str, Enum):
    QUESTION_OPENING_PRESENT = "question_opening_present"
    MINIMAL_EMERGENCE = "minimal_emergence"
    LOW_EMERGENCE = "low_emergence"
    NO_EMERGENCE = "no_emergence"


class CarryoverRisk(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    PREPARED_SCAFFOLD_CARRYOVER = "prepared_scaffold_carryover"


class MaturationState(str, Enum):
    HOLD = "hold"
    RESIDUE = "residue"
    WEAK = "weak"
    FALLBACK = "fallback"
    BLOCKED = "blocked"
    BREATHING = "breathing"


class TraceabilityStatus(str, Enum):
    TRACEABLE = "traceable"
    PARTIALLY_TRACEABLE = "partially_traceable"
    NOT_TRACEABLE = "not_traceable"


class ComparisonMemoryReason(str, Enum):
    SAME_COMPRESSED_FAMILY = "same_compressed_family"
    SAME_FALLBACK_DOMINANCE = "same_fallback_dominance"
    BREATHING_CONTRAST = "breathing_contrast"
    SIMILAR_CARRYOVER_PATTERN = "similar_carryover_pattern"
    SIMILAR_GROUNDING_FAILURE_SURFACE = "similar_grounding_failure_surface"


class GateBlockerSummary(str, Enum):
    QUESTION_INDUCING_CANDIDATE_ABSENCE = "question_inducing_candidate_absence"
    FALLBACK_GROUNDING_DOMINANCE = "fallback_grounding_dominance"
    WEAK_ROLE_LIKE_ONLY = "weak_role_like_only"
    PIVOT_COMPRESSION_NON_RECURRENCE = "pivot_compression_non_recurrence"
    SCAFFOLD_CARRYOVER_RISK = "scaffold_carryover_risk"


class UpdateTriggerType(str, Enum):
    BACKFILL = "backfill"
    RUNTIME_EVIDENCE = "runtime_evidence"
    RECOMPUTE = "recompute"
    MANUAL_CORRECTION = "manual_correction"
