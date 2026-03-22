from __future__ import annotations

from typing import Sequence

from app.core.runtime.approval_policies import evaluate_approval_grammar_policy
from app.core.runtime.approval_policy_types import ApprovalGrammarContext
from app.core.runtime.review_policy_types import (
    CanonicalizationPolicyContext,
    CanonicalizationPolicyResult,
    CrossPathPolicyContext,
    CrossPathPolicyResult,
    DirectOverlapAggregatePolicyContext,
    DirectOverlapAggregatePolicyResult,
    DirectOverlapFamilyPolicyContext,
    DirectOverlapFamilyPolicyResult,
    PromotionPolicyContext,
    PromotionPolicyResult,
    LifecyclePolicyContext,
    LifecyclePolicyResult,
    SpaceEntryPolicyContext,
    SpaceEntryPolicyResult,
)


def evaluate_promotion_review_policy(context: PromotionPolicyContext) -> PromotionPolicyResult:
    if context.cross_path_type != "live-imported":
        return PromotionPolicyResult(
            available=False,
            review_state="not_applicable",
            review_kind="",
            recommendation="",
            translation_coverage_class="missing",
            processing_residual_class="missing",
            next_review_blocker="",
            gate_vector={},
            promotion_readiness_class="",
            promotion_decision="",
        )
    if not context.translation_available:
        return PromotionPolicyResult(
            available=False,
            review_state="translation_missing",
            review_kind="",
            recommendation="",
            translation_coverage_class="missing",
            processing_residual_class="missing",
            next_review_blocker="translation_convergence_missing",
            gate_vector={},
            promotion_readiness_class="",
            promotion_decision="",
        )

    translation_coverage_class = _translation_coverage_class(context.matched_local_ref_count)
    processing_residual_class = _processing_residual_class(
        context.best_processing_score,
        context.processing_convergence_level,
    )
    review_kind = "translation_assisted_local_candidate"
    review_state = "candidate"
    recommendation = "review_for_possibility_promotion"
    if context.processing_convergence_level in {"none", "weak"}:
        review_kind = "translation_led_processing_weak"
        recommendation = "keep_in_possibility_review_lane"
    if not context.best_local_ref:
        review_state = "blocked"
        recommendation = "processing_residual_missing"
    next_review_blocker = _next_review_blocker(
        context.promotion_blockers,
        translation_coverage_class,
        processing_residual_class,
    )
    approval_result = evaluate_approval_grammar_policy(
        ApprovalGrammarContext(
            translation_coverage_class=translation_coverage_class,
            processing_residual_class=processing_residual_class,
            observer_available=context.observer_available,
            canonical_anchor_alignment_count=context.partial_anchor_alignment_count,
            next_review_blocker=next_review_blocker,
        )
    )
    return PromotionPolicyResult(
        available=True,
        review_state=review_state,
        review_kind=review_kind,
        recommendation=recommendation,
        translation_coverage_class=translation_coverage_class,
        processing_residual_class=processing_residual_class,
        next_review_blocker=next_review_blocker,
        gate_vector=approval_result.gate_vector,
        promotion_readiness_class=approval_result.readiness_class,
        promotion_decision=approval_result.decision,
    )


def evaluate_cross_path_overlap_policy(context: CrossPathPolicyContext) -> CrossPathPolicyResult:
    canonicalization_candidate_class = ""
    canonicalization_gap_class = ""
    if context.canonicalization_candidate_families:
        if len(context.canonicalization_candidate_families) >= 2:
            canonicalization_candidate_class = "multi_family_canonicalization_candidate"
        else:
            canonicalization_candidate_class = f"{context.canonicalization_candidate_families[0]}_canonicalization_candidate"
        canonicalization_gap_class = "cross_path_family_present_needs_canonicalization"

    quality_class = "none"
    corroboration_state = "none"
    threshold_gap_class = ""
    if context.family_count == 1 and list(context.overlap_families) == ["semantic"]:
        quality_class = "semantic_only"
        corroboration_state = "semantic_only_cross_path"
        threshold_gap_class = (
            "live_side_family_present_but_not_canonicalized"
            if context.uncorroborated_live_families
            else "cross_path_family_diversity_below_threshold"
        )
    elif context.family_count >= 2:
        quality_class = "multi_family_direct"
        corroboration_state = "cross_family_corroborated"
        threshold_gap_class = ""
    elif context.translation_assisted_overlap_count and context.canonicalizable_overlap_count == 0:
        quality_class = "translated_only"
        corroboration_state = "translated_hits_but_not_canonicalized"
        threshold_gap_class = "translated_overlap_not_canonicalized"
    elif context.canonicalizable_overlap_count <= 1:
        quality_class = "thin_direct_overlap"
        corroboration_state = "cross_path_thin"
        threshold_gap_class = "cross_path_overlap_count_below_threshold"

    return CrossPathPolicyResult(
        cross_path_overlap_quality_class=quality_class,
        cross_path_corroboration_state=corroboration_state,
        cross_path_threshold_gap_class=threshold_gap_class,
        cross_path_canonicalization_candidate_class=canonicalization_candidate_class,
        cross_path_canonicalization_gap_class=canonicalization_gap_class,
    )


def evaluate_direct_overlap_family_policy(
    context: DirectOverlapFamilyPolicyContext,
) -> DirectOverlapFamilyPolicyResult:
    ready = context.family_overlap_count > 0
    blocker = ""
    if ready:
        blocker = ""
    elif context.pair_overlap_count > 0:
        blocker = "token_pair_exists_but_alignment_rule_not_satisfied"
    elif not context.has_live_tokens:
        blocker = "live_side_anchor_form_missing"
    else:
        blocker = "canonicalizable_token_pair_missing"

    if context.pair_overlap_count > 0 and context.live_token_source == "direct" and context.imported_token_source == "direct":
        rule_state = "direct_token_pair_present_but_unpromoted"
    elif context.pair_overlap_count > 0 and {context.live_token_source, context.imported_token_source} == {"direct", "derived"}:
        rule_state = "one_side_direct_one_side_derived"
    elif context.pair_overlap_count > 0 and context.live_token_source == "derived" and context.imported_token_source == "derived":
        rule_state = "both_sides_derived_pair"
    elif context.live_token_source == "missing":
        rule_state = "live_anchor_form_missing"
    else:
        rule_state = "pair_missing"

    return DirectOverlapFamilyPolicyResult(
        ready=ready,
        blocker=blocker,
        rule_state=rule_state,
    )


def evaluate_direct_overlap_aggregate_policy(
    context: DirectOverlapAggregatePolicyContext,
) -> DirectOverlapAggregatePolicyResult:
    gap_class = ""
    token_pair_alignment_state = "missing"
    if context.candidate_families:
        if context.any_alignment_rule_missing:
            gap_class = "token_pair_exists_but_alignment_rule_not_satisfied"
            token_pair_alignment_state = "candidate_pairs_present_but_noncanonical"
        elif context.any_live_form_missing:
            gap_class = "live_side_anchor_form_missing"
            token_pair_alignment_state = "live_form_missing"
        else:
            gap_class = "canonicalizable_token_pair_missing"
            token_pair_alignment_state = "missing"

    live_anchor_form_state = "present" if context.has_live_anchor_form else "missing"
    family_mapping_state = "missing"
    if context.candidate_families:
        family_mapping_state = "family_candidates_present"
        if context.canonicalizable_token_pair_count > 0:
            family_mapping_state = "canonicalizable_pairs_present"

    lead_family = ""
    for family in context.candidate_families:
        if context.family_rule_states.get(family) == "one_side_direct_one_side_derived":
            lead_family = family
            break
    if not lead_family:
        for family in context.candidate_families:
            if context.family_rule_states.get(family) == "direct_token_pair_present_but_unpromoted":
                lead_family = family
                break
    if not lead_family and context.candidate_families:
        lead_family = context.candidate_families[0]

    return DirectOverlapAggregatePolicyResult(
        direct_overlap_gap_class=gap_class,
        token_pair_alignment_state=token_pair_alignment_state,
        live_anchor_form_state=live_anchor_form_state,
        family_mapping_state=family_mapping_state,
        direct_overlap_candidate_lead_family=lead_family,
    )


def evaluate_canonicalization_family_policy(
    context: CanonicalizationPolicyContext,
) -> CanonicalizationPolicyResult:
    strength = "missing"
    if context.has_live_tokens and context.has_imported_tokens:
        strength = "token_supported"
    elif context.live_hint and context.imported_hint:
        strength = "text_hint_supported"
    elif context.has_live_tokens or context.has_imported_tokens or context.live_hint or context.imported_hint:
        strength = "one_sided_hint"

    proposal_blocker = "family_not_ready"
    if strength == "token_supported":
        proposal_blocker = ""
    elif context.live_hint and context.imported_hint and not context.has_live_tokens and not context.has_imported_tokens:
        proposal_blocker = "hint_only_needs_tokenization"
    elif context.has_live_tokens and not context.has_imported_tokens:
        proposal_blocker = "imported_side_token_missing"
    elif context.has_imported_tokens and not context.has_live_tokens:
        proposal_blocker = "live_side_token_missing"
    elif context.live_hint or context.imported_hint:
        proposal_blocker = "one_sided_or_hint_only_support"

    live_token_source = "direct" if context.raw_live_token_source == "direct" else "derived" if context.has_live_tokens else "missing"
    imported_token_source = "direct" if context.raw_imported_token_source == "direct" else "derived" if context.has_imported_tokens else "missing"
    return CanonicalizationPolicyResult(
        strength=strength,
        proposal_blocker=proposal_blocker,
        live_token_source=live_token_source,
        imported_token_source=imported_token_source,
    )


def evaluate_space_entry_policy(context: SpaceEntryPolicyContext) -> SpaceEntryPolicyResult:
    state = "not_ready"
    blocker = ""
    reason = ""
    if (
        context.translation_gate
        and context.processing_gate
        and context.observer_gate
        and context.same_local_ref_support_strength >= 3
        and context.direct_overlap_candidate_count > 0
    ):
        state = "space_pre_entry_candidate"
        blocker = context.direct_overlap_gap_class
        reason = "dense_internal_support_with_family_level_direct_overlap_candidates"
        if context.direct_overlap_candidate_lead_family:
            state = f"{context.direct_overlap_candidate_lead_family}_led_space_pre_entry"
            reason = "lead_family_is_closest_to_direct_canonical_overlap"
    if context.canonical_anchor_gate:
        state = "canonical_space_ready"
        blocker = ""
        reason = "canonical_anchor_gate_passed"
    return SpaceEntryPolicyResult(
        space_entry_state=state,
        space_entry_blocker=blocker,
        space_entry_reason=reason,
    )


def evaluate_review_lifecycle_policy(context: LifecyclePolicyContext) -> LifecyclePolicyResult:
    if context.bridge_mode == "canonical":
        return LifecyclePolicyResult(
            trace_temperature="hot",
            lifecycle_stage="approved_active",
            lifecycle_reason="canonical_connection_remains_hot",
        )
    if context.review_state == "candidate" and context.space_entry_state:
        return LifecyclePolicyResult(
            trace_temperature="hot",
            lifecycle_stage="review_active",
            lifecycle_reason="space_pre_entry_review_candidate",
        )
    if context.bridge_mode == "possibility_candidate":
        return LifecyclePolicyResult(
            trace_temperature="hot",
            lifecycle_stage="possibility_active",
            lifecycle_reason="active_possibility_candidate",
        )
    if context.review_state == "translation_missing":
        return LifecyclePolicyResult(
            trace_temperature="warm",
            lifecycle_stage="blocked_waiting_revisit",
            lifecycle_reason="translation_missing_should_be_preserved_but_not_hot",
        )
    if context.best_local_ref or context.direct_overlap_candidate_count or context.canonicalizable_token_pair_count:
        return LifecyclePolicyResult(
            trace_temperature="warm",
            lifecycle_stage="deferred_review_asset",
            lifecycle_reason="candidate_has_structured_review_evidence",
        )
    return LifecyclePolicyResult(
        trace_temperature="cold",
        lifecycle_stage="thin_trace_archive_candidate",
        lifecycle_reason="no_active_review_signal",
    )


def _translation_coverage_class(matched_local_ref_count: int) -> str:
    if matched_local_ref_count >= 12:
        return "broad_local_ref_hit"
    if matched_local_ref_count >= 3:
        return "narrow_local_ref_hit"
    if matched_local_ref_count >= 1:
        return "single_local_ref_hit"
    return "missing"


def _processing_residual_class(best_score: float, convergence_level: str) -> str:
    if convergence_level == "strong" or best_score >= 0.82:
        return "strong"
    if convergence_level == "partial" or best_score >= 0.64:
        return "partial"
    if convergence_level == "weak" or best_score > 0.0:
        return "weak"
    return "missing"


def _next_review_blocker(
    promotion_blockers: Sequence[str],
    translation_coverage_class: str,
    processing_residual_class: str,
) -> str:
    if translation_coverage_class == "missing":
        return "translation_convergence_missing"
    if processing_residual_class in {"missing", "weak"}:
        return "processing_residual_too_weak"
    for blocker in promotion_blockers:
        if blocker:
            return str(blocker)
    return "reviewable"
