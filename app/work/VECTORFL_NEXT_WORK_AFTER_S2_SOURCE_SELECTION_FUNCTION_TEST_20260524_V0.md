# VECTORFL_NEXT_WORK_AFTER_S2_SOURCE_SELECTION_FUNCTION_TEST_20260524_V0

NEXT_SAFE_LANE: S3_HERMES_MERGE_TRACE_SMALL_REAL_OUTPUT_SPACE_REFERENCED_NO_AUTHORITY_MUTATION_V0

purpose:
Continue Phase2 function tests with S3 Hermes merge trace on a small real output.

Rules:
- attach to Phase1 whole-flow stage S3_HERMES_MERGE_EXECUTION
- use selected refs from S2 unless a new conflict appears
- produce a small real output, not validator/checklist hardening
- show original + selected space refs + model merge result
- record why_not_model_only and space_reference_delta
- record observed_gap and phase3_revision_candidate
- do not globally modify merge contract from one observation
- keep HOLD

Carry forward S1 observation:
continuation-only input requires latest next-lane lookup before intent classification.

Carry forward S2 observation:
source selection should log rejected refs with reasons; accumulate for Phase3, do not globally revise yet.
