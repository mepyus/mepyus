from __future__ import annotations

from app.core.runtime.review_policy_types import (
    CrossPathPolicyContext,
    CrossPathPolicyResult,
    LifecyclePolicyResult,
    PromotionPolicyContext,
    PromotionPolicyResult,
    PromotionReviewAssembly,
    ReviewTimestamp,
)


def assemble_promotion_review_surface(
    *,
    context: PromotionPolicyContext,
    policy: PromotionPolicyResult,
    assembly: PromotionReviewAssembly,
    lifecycle: LifecyclePolicyResult | None = None,
    timestamp: ReviewTimestamp | None = None,
) -> dict[str, object]:
    if not policy.available:
        return {
            "available": False,
            "review_state": policy.review_state,
        }
    payload = {
        "available": True,
        "review_state": policy.review_state,
        "review_kind": policy.review_kind,
        "recommendation": policy.recommendation,
        "translation_scope_used": context.translation_scope_used,
        "translation_coverage_class": policy.translation_coverage_class,
        "matched_local_ref_count": context.matched_local_ref_count,
        "matched_handles": list(context.matched_handles[:4]),
        "best_local_ref": context.best_local_ref,
        "best_processing_score": round(context.best_processing_score, 4),
        "processing_convergence_level": context.processing_convergence_level,
        "processing_residual_class": policy.processing_residual_class,
        "next_review_blocker": policy.next_review_blocker,
        "translation_gate": bool(policy.gate_vector.get("translation_gate")),
        "processing_gate": bool(policy.gate_vector.get("processing_gate")),
        "observer_gate": bool(policy.gate_vector.get("observer_gate")),
        "canonical_anchor_gate": bool(policy.gate_vector.get("canonical_anchor_gate")),
        "gate_vector": dict(policy.gate_vector),
        "promotion_readiness_class": policy.promotion_readiness_class,
        "promotion_decision": policy.promotion_decision,
        "residual_blockers": list(assembly.residual_blockers[:6]),
    }
    if lifecycle is not None:
        payload.update(
            {
                "trace_temperature": lifecycle.trace_temperature,
                "lifecycle_stage": lifecycle.lifecycle_stage,
                "lifecycle_reason": lifecycle.lifecycle_reason,
            }
        )
    if timestamp is not None:
        payload.update(
            {
                "evaluated_at": timestamp.evaluated_at,
                "state_signature": timestamp.state_signature,
            }
        )
    payload.update(_assemble_anchor_review_surface(assembly.anchor_review))
    payload.update(_assemble_threshold_review_surface(assembly.threshold_review))
    payload.update(_assemble_live_side_review_surface(assembly.live_side_review))
    payload.update(_assemble_cross_path_review_payload(assembly.cross_path_review))
    payload.update(_assemble_canonicalization_review_surface(assembly.canonicalization_review))
    payload.update(_assemble_direct_overlap_review_surface(assembly.direct_overlap_review))
    payload.update(_assemble_space_entry_review_surface(assembly.space_entry_review))
    return payload


def assemble_cross_path_review_surface(
    *,
    context: CrossPathPolicyContext,
    policy: CrossPathPolicyResult,
    overlap_evidence: dict[str, object],
) -> dict[str, object]:
    missing_families = [
        family
        for family in ("semantic", "structural", "process", "object")
        if family not in context.overlap_families
    ]
    subcritical_families = list(context.overlap_families) if context.family_count == 1 else []
    return {
        "cross_path_overlap_family_count": context.family_count,
        "cross_path_overlap_quality_class": policy.cross_path_overlap_quality_class,
        "cross_path_corroboration_state": policy.cross_path_corroboration_state,
        "cross_path_threshold_gap_class": policy.cross_path_threshold_gap_class,
        "cross_path_overlap_families": list(context.overlap_families),
        "cross_path_missing_families": missing_families,
        "cross_path_subcritical_families": subcritical_families,
        "cross_path_uncorroborated_live_families": list(context.uncorroborated_live_families),
        "cross_path_canonicalization_candidate_families": list(context.canonicalization_candidate_families),
        "cross_path_canonicalization_candidate_class": policy.cross_path_canonicalization_candidate_class,
        "cross_path_canonicalization_gap_class": policy.cross_path_canonicalization_gap_class,
        "cross_path_overlap_evidence": overlap_evidence,
    }


def _assemble_anchor_review_surface(anchor_review: dict[str, object]) -> dict[str, object]:
    return {
        "review_anchor_gap_class": str(anchor_review.get("review_anchor_gap_class", "")).strip(),
        "review_anchor_support_class": str(anchor_review.get("review_anchor_support_class", "")).strip(),
        "anchor_alignment_evidence": dict(anchor_review.get("anchor_alignment_evidence", {}) or {}),
        "anchor_alignment_missing_types": list(anchor_review.get("anchor_alignment_missing_types", []) or []),
        "anchor_alignment_subcritical_types": list(anchor_review.get("anchor_alignment_subcritical_types", []) or []),
        "anchor_alignment_compound_state": str(anchor_review.get("anchor_alignment_compound_state", "")).strip(),
        "anchor_support_scope": str(anchor_review.get("anchor_support_scope", "")).strip(),
        "anchor_family_additions": dict(anchor_review.get("anchor_family_additions", {}) or {}),
        "anchor_family_support_strength": dict(anchor_review.get("anchor_family_support_strength", {}) or {}),
        "compound_candidate_families": list(anchor_review.get("compound_candidate_families", []) or []),
        "compound_support_scope": str(anchor_review.get("compound_support_scope", "")).strip(),
    }


def _assemble_threshold_review_surface(threshold_review: dict[str, object]) -> dict[str, object]:
    return {
        "support_density_class": str(threshold_review.get("support_density_class", "")).strip(),
        "corroboration_scope_class": str(threshold_review.get("corroboration_scope_class", "")).strip(),
        "threshold_gap_class": str(threshold_review.get("threshold_gap_class", "")).strip(),
        "threshold_review_vector": dict(threshold_review.get("threshold_review_vector", {}) or {}),
    }


def _assemble_live_side_review_surface(live_side_review: dict[str, object]) -> dict[str, object]:
    return {
        "live_side_support_class": str(live_side_review.get("live_side_support_class", "")).strip(),
        "live_side_support_families": list(live_side_review.get("live_side_support_families", []) or []),
        "live_side_missing_families": list(live_side_review.get("live_side_missing_families", []) or []),
        "live_side_anchor_evidence": dict(live_side_review.get("live_side_anchor_evidence", {}) or {}),
    }


def _assemble_cross_path_review_payload(cross_path_review: dict[str, object]) -> dict[str, object]:
    return {
        "cross_path_overlap_family_count": int(cross_path_review.get("cross_path_overlap_family_count", 0) or 0),
        "cross_path_overlap_quality_class": str(cross_path_review.get("cross_path_overlap_quality_class", "")).strip(),
        "cross_path_corroboration_state": str(cross_path_review.get("cross_path_corroboration_state", "")).strip(),
        "cross_path_threshold_gap_class": str(cross_path_review.get("cross_path_threshold_gap_class", "")).strip(),
        "cross_path_overlap_families": list(cross_path_review.get("cross_path_overlap_families", []) or []),
        "cross_path_missing_families": list(cross_path_review.get("cross_path_missing_families", []) or []),
        "cross_path_subcritical_families": list(cross_path_review.get("cross_path_subcritical_families", []) or []),
        "cross_path_uncorroborated_live_families": list(cross_path_review.get("cross_path_uncorroborated_live_families", []) or []),
        "cross_path_canonicalization_candidate_families": list(cross_path_review.get("cross_path_canonicalization_candidate_families", []) or []),
        "cross_path_canonicalization_candidate_class": str(cross_path_review.get("cross_path_canonicalization_candidate_class", "")).strip(),
        "cross_path_canonicalization_gap_class": str(cross_path_review.get("cross_path_canonicalization_gap_class", "")).strip(),
        "cross_path_overlap_evidence": dict(cross_path_review.get("cross_path_overlap_evidence", {}) or {}),
    }


def _assemble_canonicalization_review_surface(canonicalization_review: dict[str, object]) -> dict[str, object]:
    return {
        "cross_path_canonicalization_scope": str(canonicalization_review.get("cross_path_canonicalization_scope", "")).strip(),
        "cross_path_canonicalization_strengths": dict(canonicalization_review.get("cross_path_canonicalization_strengths", {}) or {}),
        "cross_path_canonicalization_evidence": dict(canonicalization_review.get("cross_path_canonicalization_evidence", {}) or {}),
        "cross_path_canonicalization_ready_families": list(canonicalization_review.get("cross_path_canonicalization_ready_families", []) or []),
        "cross_path_canonicalization_hint_only_families": list(canonicalization_review.get("cross_path_canonicalization_hint_only_families", []) or []),
        "cross_path_canonicalization_proposal_state": str(canonicalization_review.get("cross_path_canonicalization_proposal_state", "")).strip(),
        "cross_path_canonicalization_proposals": dict(canonicalization_review.get("cross_path_canonicalization_proposals", {}) or {}),
        "cross_path_canonicalization_proposal_blockers": dict(canonicalization_review.get("cross_path_canonicalization_proposal_blockers", {}) or {}),
    }


def _assemble_direct_overlap_review_surface(direct_overlap_review: dict[str, object]) -> dict[str, object]:
    return {
        "direct_overlap_candidate_families": list(direct_overlap_review.get("direct_overlap_candidate_families", []) or []),
        "direct_overlap_gap_class": str(direct_overlap_review.get("direct_overlap_gap_class", "")).strip(),
        "direct_overlap_evidence": dict(direct_overlap_review.get("direct_overlap_evidence", {}) or {}),
        "family_canonicalization_strengths": dict(direct_overlap_review.get("family_canonicalization_strengths", {}) or {}),
        "family_direct_overlap_ready": dict(direct_overlap_review.get("family_direct_overlap_ready", {}) or {}),
        "family_direct_overlap_blockers": dict(direct_overlap_review.get("family_direct_overlap_blockers", {}) or {}),
        "family_rule_refinement_state": dict(direct_overlap_review.get("family_rule_refinement_state", {}) or {}),
        "direct_overlap_candidate_lead_family": str(direct_overlap_review.get("direct_overlap_candidate_lead_family", "")).strip(),
        "token_pair_alignment_state": str(direct_overlap_review.get("token_pair_alignment_state", "")).strip(),
        "live_anchor_form_state": str(direct_overlap_review.get("live_anchor_form_state", "")).strip(),
        "canonicalizable_token_pair_count": int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),
        "noncanonical_token_pair_count": int(direct_overlap_review.get("noncanonical_token_pair_count", 0) or 0),
        "family_mapping_state": str(direct_overlap_review.get("family_mapping_state", "")).strip(),
    }


def _assemble_space_entry_review_surface(space_entry_review: dict[str, object]) -> dict[str, object]:
    return {
        "space_entry_state": str(space_entry_review.get("space_entry_state", "")).strip(),
        "space_entry_vector": dict(space_entry_review.get("space_entry_vector", {}) or {}),
        "space_entry_ready_families": list(space_entry_review.get("space_entry_ready_families", []) or []),
        "space_entry_lead_family": str(space_entry_review.get("space_entry_lead_family", "")).strip(),
        "space_entry_blocker": str(space_entry_review.get("space_entry_blocker", "")).strip(),
        "space_entry_reason": str(space_entry_review.get("space_entry_reason", "")).strip(),
    }
