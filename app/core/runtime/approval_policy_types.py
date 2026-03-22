from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class ApprovalGrammarContext:
    translation_coverage_class: str
    processing_residual_class: str
    observer_available: bool
    canonical_anchor_alignment_count: int
    next_review_blocker: str


@dataclass(frozen=True)
class ApprovalGrammarResult:
    gate_vector: Dict[str, object]
    readiness_class: str
    decision: str


@dataclass(frozen=True)
class CanonicalAnchorApprovalContext:
    semantic_supported: bool
    structural_supported: bool
    process_supported: bool
    object_supported: bool
    translated_handle_count: int
    local_compound_state: str
    local_review_anchor_support_class: str
    local_review_anchor_gap_class: str
    local_next_review_blocker: str
    has_local_compound_candidates: bool


@dataclass(frozen=True)
class CanonicalAnchorApprovalResult:
    canonical_anchor_gate: bool
    canonical_anchor_alignment_count: int
    review_anchor_gap_class: str
    review_anchor_support_class: str
    anchor_alignment_compound_state: str
    next_review_blocker: str
    anchor_alignment_missing_types: list[str]
    anchor_alignment_subcritical_types: list[str]


@dataclass(frozen=True)
class BridgeModeApprovalContext:
    canonical_pair_present: bool
    cross_path_type: str
    possibility_basis_available: bool


@dataclass(frozen=True)
class BridgeModeApprovalResult:
    bridge_mode: str


@dataclass(frozen=True)
class CanonicalReviewDecisionContext:
    promotion_readiness_class: str
    anchor_next_review_blocker: str
    threshold_gap_class: str
    cross_path_threshold_gap_class: str
    direct_overlap_gap_class: str


@dataclass(frozen=True)
class CanonicalReviewDecisionResult:
    next_review_blocker: str
    promotion_decision: str
    canonical_review_focus_class: str


@dataclass(frozen=True)
class CanonicalApprovalStatusContext:
    canonical_anchor_gate: bool
    cross_path_overlap_family_count: int
    direct_overlap_candidate_count: int
    canonicalizable_token_pair_count: int
    space_entry_state: str
    canonical_review_focus_class: str


@dataclass(frozen=True)
class CanonicalApprovalStatusResult:
    canonical_approval_readiness_class: str
    canonical_approval_next_step: str
    canonical_approval_vector: Dict[str, object]
