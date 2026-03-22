from __future__ import annotations

from app.core.runtime.approval_policy_types import (
    ApprovalGrammarContext,
    ApprovalGrammarResult,
    BridgeModeApprovalContext,
    BridgeModeApprovalResult,
    CanonicalApprovalStatusContext,
    CanonicalApprovalStatusResult,
    CanonicalReviewDecisionContext,
    CanonicalReviewDecisionResult,
    CanonicalAnchorApprovalContext,
    CanonicalAnchorApprovalResult,
)


def evaluate_approval_grammar_policy(context: ApprovalGrammarContext) -> ApprovalGrammarResult:
    gate_vector = _build_gate_vector(
        translation_coverage_class=context.translation_coverage_class,
        processing_residual_class=context.processing_residual_class,
        observer_available=context.observer_available,
        canonical_anchor_alignment_count=context.canonical_anchor_alignment_count,
    )
    readiness_class = _approval_readiness_class(gate_vector)
    decision = _approval_decision(gate_vector, context.next_review_blocker)
    return ApprovalGrammarResult(
        gate_vector=gate_vector,
        readiness_class=readiness_class,
        decision=decision,
    )


def evaluate_canonical_anchor_approval_policy(
    context: CanonicalAnchorApprovalContext,
) -> CanonicalAnchorApprovalResult:
    missing_types: list[str] = []
    subcritical_types: list[str] = []
    if not context.semantic_supported:
        missing_types.append("semantic_anchor_alignment_missing")
    elif context.translated_handle_count > 0:
        subcritical_types.append("translation_hit_not_yet_canonical_anchor")
    if not context.structural_supported:
        missing_types.append("structural_anchor_alignment_missing")
    if not context.process_supported:
        missing_types.append("process_anchor_alignment_missing")
    if not context.object_supported:
        missing_types.append("object_anchor_alignment_missing")

    overlap_count = (
        int(context.semantic_supported)
        + int(context.structural_supported)
        + int(context.process_supported)
        + int(context.object_supported)
    )
    compound_state = "insufficient"
    support_class = "missing"
    gap_class = "typed_anchor_missing"
    next_blocker = "missing_canonical_anchor_alignment"
    canonical_anchor_gate = False
    if (
        overlap_count >= 2
        and context.semantic_supported
        and (context.structural_supported or context.process_supported or context.object_supported)
    ):
        compound_state = "cross_anchor_corroborated"
        support_class = "cross_type_anchor_support_present"
        gap_class = "none"
        next_blocker = ""
        canonical_anchor_gate = True
    elif context.semantic_supported:
        compound_state = "single_family_only"
        support_class = "semantic_anchor_present_but_subcritical"
        gap_class = "anchor_alignment_present_but_subcritical"
        next_blocker = "single_anchor_supported_but_not_compounded"
    elif context.translated_handle_count > 0:
        compound_state = "translation_only"
        support_class = "translation_hit_without_anchor_corroboration"
        gap_class = "translation_hit_not_yet_canonical_anchor"
        next_blocker = "translation_hit_not_yet_canonical_anchor"

    if not canonical_anchor_gate and context.has_local_compound_candidates:
        compound_state = context.local_compound_state or compound_state
        support_class = context.local_review_anchor_support_class or support_class
        gap_class = context.local_review_anchor_gap_class or gap_class
        next_blocker = context.local_next_review_blocker or next_blocker

    return CanonicalAnchorApprovalResult(
        canonical_anchor_gate=canonical_anchor_gate,
        canonical_anchor_alignment_count=overlap_count,
        review_anchor_gap_class=gap_class,
        review_anchor_support_class=support_class,
        anchor_alignment_compound_state=compound_state,
        next_review_blocker=next_blocker,
        anchor_alignment_missing_types=missing_types,
        anchor_alignment_subcritical_types=subcritical_types,
    )


def evaluate_bridge_mode_approval_policy(
    context: BridgeModeApprovalContext,
) -> BridgeModeApprovalResult:
    bridge_mode = "none"
    if context.canonical_pair_present:
        bridge_mode = "canonical"
    elif context.cross_path_type in {"live-imported", "live-legacy"} and context.possibility_basis_available:
        bridge_mode = "possibility_candidate"
    return BridgeModeApprovalResult(bridge_mode=bridge_mode)


def evaluate_canonical_review_decision_policy(
    context: CanonicalReviewDecisionContext,
) -> CanonicalReviewDecisionResult:
    next_review_blocker = (
        context.cross_path_threshold_gap_class
        or context.direct_overlap_gap_class
        or context.threshold_gap_class
        or context.anchor_next_review_blocker
    )
    if context.cross_path_threshold_gap_class:
        focus_class = "cross_path_corroboration"
    elif context.direct_overlap_gap_class:
        focus_class = "direct_overlap_alignment"
    elif context.threshold_gap_class:
        focus_class = "threshold_support"
    else:
        focus_class = "anchor_support"

    promotion_decision = _decision_from_readiness_and_blocker(
        context.promotion_readiness_class,
        next_review_blocker,
    )
    return CanonicalReviewDecisionResult(
        next_review_blocker=next_review_blocker,
        promotion_decision=promotion_decision,
        canonical_review_focus_class=focus_class,
    )


def evaluate_canonical_approval_status_policy(
    context: CanonicalApprovalStatusContext,
) -> CanonicalApprovalStatusResult:
    readiness = "canonical_blocked"
    next_step = "hold_canonical_review"
    if context.canonical_anchor_gate:
        readiness = "canonical_ready"
        next_step = "approve_canonical"
    elif context.cross_path_overlap_family_count <= 1:
        readiness = "cross_path_corroboration_pending"
        next_step = "increase_cross_path_family_corroboration"
    elif context.direct_overlap_candidate_count <= 0:
        readiness = "direct_overlap_candidate_missing"
        next_step = "recover_direct_overlap_candidate"
    elif context.canonicalizable_token_pair_count <= 0:
        readiness = "canonicalization_pending"
        next_step = "promote_canonicalizable_token_pairs"
    elif context.space_entry_state:
        readiness = "space_entry_ready_but_unapproved"
        next_step = f"resolve_{context.canonical_review_focus_class or 'canonical_review_focus'}"

    return CanonicalApprovalStatusResult(
        canonical_approval_readiness_class=readiness,
        canonical_approval_next_step=next_step,
        canonical_approval_vector={
            "canonical_anchor_gate": context.canonical_anchor_gate,
            "cross_path_overlap_family_count": context.cross_path_overlap_family_count,
            "direct_overlap_candidate_count": context.direct_overlap_candidate_count,
            "canonicalizable_token_pair_count": context.canonicalizable_token_pair_count,
            "space_entry_state": context.space_entry_state,
            "canonical_review_focus_class": context.canonical_review_focus_class,
        },
    )


def _build_gate_vector(
    *,
    translation_coverage_class: str,
    processing_residual_class: str,
    observer_available: bool,
    canonical_anchor_alignment_count: int,
) -> dict[str, object]:
    translation_gate = translation_coverage_class != "missing"
    processing_gate = processing_residual_class in {"partial", "strong"}
    observer_gate = observer_available
    canonical_anchor_gate = canonical_anchor_alignment_count >= 2
    return {
        "translation_gate": translation_gate,
        "processing_gate": processing_gate,
        "observer_gate": observer_gate,
        "canonical_anchor_gate": canonical_anchor_gate,
        "canonical_anchor_alignment_count": canonical_anchor_alignment_count,
    }


def _approval_readiness_class(gate_vector: dict[str, object]) -> str:
    translation_gate = bool(gate_vector.get("translation_gate"))
    processing_gate = bool(gate_vector.get("processing_gate"))
    observer_gate = bool(gate_vector.get("observer_gate"))
    canonical_anchor_gate = bool(gate_vector.get("canonical_anchor_gate"))
    if translation_gate and processing_gate and observer_gate and canonical_anchor_gate:
        return "canonical_ready"
    if translation_gate and processing_gate and observer_gate and not canonical_anchor_gate:
        return "anchor_alignment_pending"
    if translation_gate and not processing_gate:
        return "processing_pending"
    if not translation_gate:
        return "translation_pending"
    return "review_pending"


def _approval_decision(gate_vector: dict[str, object], next_review_blocker: str) -> str:
    readiness = _approval_readiness_class(gate_vector)
    return _decision_from_readiness_and_blocker(readiness, next_review_blocker)


def _decision_from_readiness_and_blocker(readiness: str, next_review_blocker: str) -> str:
    if readiness == "canonical_ready":
        return "eligible_for_canonical_review"
    if readiness == "anchor_alignment_pending":
        return "review_canonical_anchor_alignment"
    if readiness == "processing_pending":
        return "hold_for_processing_refinement"
    if readiness == "translation_pending":
        return "hold_for_translation_alignment"
    if next_review_blocker:
        return f"hold_for_{next_review_blocker}"
    return "hold_in_possibility_review"
