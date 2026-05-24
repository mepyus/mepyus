# VECTORFL_PHASE3_APPLIED_OPERATING_STRUCTURE_CONTRACT_20260524_V0

status: APPLIED_TO_HOLD_SPEC_ARTIFACTS_ONLY

approval: YES_BOUNDED

not authority / not registry / not current-position / not promotion.

## applied rules
- R2_CONTINUATION_INTAKE_NEXT_LANE_LOOKUP: APPLIED_TO_CONTRACT
  rule: For continuation-only user inputs, preserve raw original, read latest next-lane card, then classify intent/budget. Do not infer next lane from model memory alone.
  acceptance: Short continuation must cite latest next-lane evidence in space_reference_delta.
- R1_MINIMAL_SPACE_DELTA_ACROSS_REENTRY_SURFACES: APPLIED_TO_CONTRACT
  rule: Merge outputs, role reviews, and operator surfaces must include one compact minimal_space_delta line plus evidence handles when reentry could lose packet-level context.
  acceptance: Surface is mind-sized but includes a delta line and deeper evidence handle.
- R3_SOURCE_SELECTION_REJECTED_REF_LOG: APPLIED_TO_CONTRACT
  rule: Source-selection surfaces must record rejected refs with reasons when rejection prevents archaeology, overload, or decorative citation.
  acceptance: Selected refs have changed_judgment; rejected refs have reason; rejected refs are not silently reintroduced.
- R4_ROLE_HANDOFF_UNIQUE_DELTA_METRIC: APPLIED_TO_CONTRACT
  rule: When Codex/Gemini heavy mode is used, record each agent unique_delta and classify overlap as productive, duplicative, or conflicting.
  acceptance: Comparison explains why both agents were useful or why one should be skipped/reviewed.
- R5_VALIDATOR_WORDING_SCOPE_GUARD: WATCH_ONLY_NOT_APPLIED
  rule: If wording false positives recur, distinguish exclusion wording from target classification.
  acceptance: Watch future validators; do not harden now without recurrence.

## boundaries
- approval_granted: YES_FOR_BOUNDED_APP_WORK_SPEC_ARTIFACTS
- implementation_apply: YES_BOUNDED_SPEC_ARTIFACTS_ONLY
- authority_mutation: NO
- registry_mutation: NO
- current_position_apply: NO
- source_code_mutation: NO
- source_schema_change: NO
- promotion: HOLD

NEXT_SAFE_LANE: PHASE3_APPLIED_CONTRACT_SMOKE_TEST_NO_AUTHORITY_MUTATION_V0
