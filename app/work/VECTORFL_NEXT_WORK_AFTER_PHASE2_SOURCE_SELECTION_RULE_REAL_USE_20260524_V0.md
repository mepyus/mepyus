# VECTORFL_NEXT_WORK_AFTER_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_20260524_V0

NEXT_SAFE_LANE: PHASE2_SOURCE_SELECTION_RULE_NEGATIVE_DRIFT_TEST_NO_AUTHORITY_MUTATION_V0

purpose:
Negative/drift test the source-selection rule candidate.

Cases:
- decorative ref with no changed_judgment
- too many refs without heavy escalation
- authority/current-position treated as writable authority
- model-only rule with no refs
- missing immediate predecessor
- source refs conflict but heavy gate not triggered

Do not mutate authority/current-position/registry.
