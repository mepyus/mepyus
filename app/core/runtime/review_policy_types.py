from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Sequence


@dataclass(frozen=True)
class PromotionPolicyContext:
    cross_path_type: str
    translation_available: bool
    translation_scope_used: str
    matched_local_ref_count: int
    matched_handles: Sequence[str]
    best_local_ref: str
    best_processing_score: float
    processing_convergence_level: str
    observer_available: bool
    partial_anchor_alignment_count: int
    promotion_blockers: Sequence[str]


@dataclass(frozen=True)
class PromotionPolicyResult:
    available: bool
    review_state: str
    review_kind: str
    recommendation: str
    translation_coverage_class: str
    processing_residual_class: str
    next_review_blocker: str
    gate_vector: Dict[str, object]
    promotion_readiness_class: str
    promotion_decision: str


@dataclass(frozen=True)
class PromotionReviewAssembly:
    anchor_review: Dict[str, object]
    live_side_review: Dict[str, object]
    threshold_review: Dict[str, object]
    cross_path_review: Dict[str, object]
    canonicalization_review: Dict[str, object]
    direct_overlap_review: Dict[str, object]
    space_entry_review: Dict[str, object]
    residual_blockers: List[str]


@dataclass(frozen=True)
class CrossPathPolicyContext:
    family_count: int
    overlap_families: Sequence[str]
    raw_anchor_overlap_count: int
    translation_assisted_overlap_count: int
    canonicalizable_overlap_count: int
    translated_but_not_canonicalized_count: int
    live_side_families: Sequence[str]
    imported_candidate_families: Sequence[str]
    canonicalization_candidate_families: Sequence[str]
    uncorroborated_live_families: Sequence[str]


@dataclass(frozen=True)
class CrossPathPolicyResult:
    cross_path_overlap_quality_class: str
    cross_path_corroboration_state: str
    cross_path_threshold_gap_class: str
    cross_path_canonicalization_candidate_class: str
    cross_path_canonicalization_gap_class: str


@dataclass(frozen=True)
class DirectOverlapFamilyPolicyContext:
    family: str
    family_overlap_count: int
    pair_overlap_count: int
    live_token_source: str
    imported_token_source: str
    has_live_tokens: bool


@dataclass(frozen=True)
class DirectOverlapFamilyPolicyResult:
    ready: bool
    blocker: str
    rule_state: str


@dataclass(frozen=True)
class DirectOverlapAggregatePolicyContext:
    candidate_families: Sequence[str]
    any_alignment_rule_missing: bool
    any_live_form_missing: bool
    canonicalizable_token_pair_count: int
    family_rule_states: Dict[str, str]
    has_live_anchor_form: bool


@dataclass(frozen=True)
class DirectOverlapAggregatePolicyResult:
    direct_overlap_gap_class: str
    token_pair_alignment_state: str
    live_anchor_form_state: str
    family_mapping_state: str
    direct_overlap_candidate_lead_family: str


@dataclass(frozen=True)
class CanonicalizationPolicyContext:
    family: str
    has_live_tokens: bool
    has_imported_tokens: bool
    live_hint: bool
    imported_hint: bool
    raw_live_token_source: str
    raw_imported_token_source: str


@dataclass(frozen=True)
class CanonicalizationPolicyResult:
    strength: str
    proposal_blocker: str
    live_token_source: str
    imported_token_source: str


@dataclass(frozen=True)
class SpaceEntryPolicyContext:
    translation_gate: bool
    processing_gate: bool
    observer_gate: bool
    canonical_anchor_gate: bool
    same_local_ref_support_strength: int
    direct_overlap_candidate_count: int
    canonicalizable_token_pair_count: int
    direct_overlap_gap_class: str
    direct_overlap_candidate_lead_family: str
    direct_overlap_candidate_families: Sequence[str]


@dataclass(frozen=True)
class SpaceEntryPolicyResult:
    space_entry_state: str
    space_entry_blocker: str
    space_entry_reason: str


@dataclass(frozen=True)
class LifecyclePolicyContext:
    bridge_mode: str
    review_state: str
    translation_gate: bool
    processing_gate: bool
    observer_gate: bool
    best_local_ref: str
    direct_overlap_candidate_count: int
    canonicalizable_token_pair_count: int
    space_entry_state: str
    next_review_blocker: str


@dataclass(frozen=True)
class LifecyclePolicyResult:
    trace_temperature: str
    lifecycle_stage: str
    lifecycle_reason: str


@dataclass(frozen=True)
class ReviewTimestamp:
    evaluated_at: str
    state_signature: str
