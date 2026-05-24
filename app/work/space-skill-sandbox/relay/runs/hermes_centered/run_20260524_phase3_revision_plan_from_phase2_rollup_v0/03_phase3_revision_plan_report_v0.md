# PHASE3_REVISION_PLAN_FROM_ACCUMULATED_PHASE2_FUNCTION_TESTS_V0

status: HOLD_PLAN_ONLY

basis: Phase3 modifies whole content based on accumulated Phase2 observations, not one-by-one convergence patches.

## MUST_FIX
- R1_MINIMAL_SPACE_DELTA_ACROSS_REENTRY_SURFACES
  stages: S3_HERMES_MERGE_EXECUTION, S4_CODEX_EVALUATION, S6_OPERATOR_RECEIPT_REENTRY
  change: Define one compact minimal_space_delta line for merge outputs, role reviews, and operator surfaces so future reentry does not lose packet-level evidence.
  test: A future output/card must be understandable from the surface and still point to deeper packet evidence.
- R2_CONTINUATION_INTAKE_NEXT_LANE_LOOKUP
  stages: S1_INTAKE, S7_BUDGET_GATE
  change: For continuation-only user inputs, require latest next-lane lookup before intent classification.
  test: A short continuation is classified by actual latest next-lane card, not guessed from model memory.

## SHOULD_FIX
- R3_SOURCE_SELECTION_REJECTED_REF_LOG
  stages: S2_SPACE_SELECTION
  change: Add rejected refs with reason to source-selection surfaces when rejected refs materially prevent archaeology/decorative citation.
  test: Selected refs include changed_judgment; rejected refs include reason and are not silently reintroduced.
- R4_ROLE_HANDOFF_UNIQUE_DELTA_METRIC
  stages: S4_CODEX_EVALUATION, S5_GEMINI_LAYER_JUDGMENT
  change: Record each agent’s unique delta and classify overlap as productive/duplicative.
  test: Codex and Gemini outputs can be compared without forcing artificial separation or accepting pure duplication.

## WATCH_ONLY
- R5_VALIDATOR_WORDING_SCOPE_GUARD
  stages: S1_INTAKE, S3_HERMES_MERGE_EXECUTION, S7_BUDGET_GATE
  change: Keep as watch unless validator false positives recur in Phase3 plan tests; then distinguish exclusion wording from target classification.
  test: Explicit exclusion phrases such as not validator/checklist hardening do not fail unless target actually is validator hardening.

## non_convergence_guard
Do not apply any single revision directly from one observation. Apply only after grouped plan review; keep each change tied to whole-flow stage and acceptance test.

## observed_gap
PHASE3_PLAN_GAP_READY_BUT_NOT_AUTHORIZED_TO_APPLY: The Phase3 plan is now structured, but applying it would be a separate authorization lane. This plan must stay HOLD evidence until the user approves implementation/revision application.

NEXT: PHASE3_REVISION_PLAN_REVIEW_AND_APPLY_DECISION_HOLD_OR_APPROVE_V0

HOLD: no authority/registry/current-position/promotion/source/schema apply.
