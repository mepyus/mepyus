# PHASE2_GUARD_PRIORITY_MINI_DECISION_TABLE_V0

classification: HOLD_CANDIDATE_DECISION_TABLE

## 1. FAIL_AUTHORITY_OVERPROMOTION
- detect_when: promotion_status != HOLD, current_position_apply != NO, authority_effect != NO_AUTHORITY_MUTATION, authority/current-position/registry used as writable authority
- masks: FAIL_SPACE_REFERENCE_DECORATION_ONLY, FAIL_OPERATOR_OVERLOAD, FAIL_NO_SPACE_REFERENCE
- reason: Authority drift changes governance boundary and must be seen first.

## 2. FAIL_OPERATOR_OVERLOAD
- detect_when: len(space_references_used) > max_default_refs and heavy_escalation_triggered != true, T_brain_operator_load starts with FAIL
- masks: FAIL_SPACE_REFERENCE_DECORATION_ONLY
- reason: Too much space archaeology can hide as citation-shape failure but is primarily human-load drift.

## 3. FAIL_HEAVY_ESCALATION_MISSING
- detect_when: source refs conflict and heavy_escalation_triggered != true, space_reference_delta unclear but mode remains fast
- masks: FAIL_SPACE_REFERENCE_DECORATION_ONLY, FAIL_NO_SPACE_REFERENCE
- reason: Conflict means the budget gate, not just citation shape, failed.

## 4. FAIL_MODEL_ONLY_DRIFT
- detect_when: space_references_used empty and why_not_model_only claims model reasoning only, space_reference_delta empty and output asserts model-only rule
- masks: FAIL_NO_SPACE_REFERENCE
- reason: No-space can be mere missing context, but model-only claim is stronger drift.

## 5. FAIL_NO_SPACE_REFERENCE
- detect_when: space_references_used empty, immediate predecessor/latest next-work ref missing
- masks: FAIL_SPACE_REFERENCE_DECORATION_ONLY
- reason: Missing space layer blocks Phase2 packet before per-ref citation quality.

## 6. FAIL_SPACE_REFERENCE_DECORATION_ONLY
- detect_when: ref lacks matching delta, changed_judgment blank/too short, used_for exists but does not alter judgment
- masks: none
- reason: Citation-quality failure is real, but lower priority than governance/load/conflict failures.

HOLD: not schema/router/registry/current-position/promotion.
