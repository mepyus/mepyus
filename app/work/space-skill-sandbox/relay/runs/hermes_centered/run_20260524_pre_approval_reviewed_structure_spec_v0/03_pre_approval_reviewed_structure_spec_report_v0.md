# VECTORFL_PRE_APPROVAL_REVIEWED_STRUCTURE_SPEC_V0

status: HOLD_SPEC_ONLY_NOT_APPROVAL_NOT_APPLY

## purpose
승인/적용 전에 우리가 검토한 구조를 명세로 고정한다. 이 문서는 적용 승인이 아니다.

## top-level structure
User original + space reading + model reasoning are merged by Hermes; Codex/Gemini re-enter as bounded evaluators; all outputs remain HOLD evidence until explicit approval.

## phase model
- Phase1: whole-flow rehearsal: actual processing loop, not internal validator/card substrate only
- Phase2: function placement/testing against Phase1 whole-flow stages with observed gaps and Phase3 backlog deltas
- Phase3: batched revision based on accumulated Phase2 observations, not one-by-one convergence patches

## whole-flow stages
- S1_INTAKE: User original intake
- S2_SPACE_SELECTION: Space evidence selection
- S3_HERMES_MERGE_EXECUTION: Hermes original + space + model merge execution
- S4_CODEX_EVALUATION: Codex evaluates space refs + Hermes output
- S5_GEMINI_LAYER_JUDGMENT: Gemini evaluates structural/layer pressure
- S6_OPERATOR_RECEIPT_REENTRY: Operator receipt/reentry and HOLD
- S7_BUDGET_GATE: Fast/heavy budget gate

## revision groups
- MUST_FIX R1_MINIMAL_SPACE_DELTA_ACROSS_REENTRY_SURFACES: Define one compact minimal_space_delta line for merge outputs, role reviews, and operator surfaces so future reentry does not lose packet-level evidence.
- MUST_FIX R2_CONTINUATION_INTAKE_NEXT_LANE_LOOKUP: For continuation-only user inputs, require latest next-lane lookup before intent classification.
- SHOULD_FIX R3_SOURCE_SELECTION_REJECTED_REF_LOG: Add rejected refs with reason to source-selection surfaces when rejected refs materially prevent archaeology/decorative citation.
- SHOULD_FIX R4_ROLE_HANDOFF_UNIQUE_DELTA_METRIC: Record each agent’s unique delta and classify overlap as productive/duplicative.
- WATCH_ONLY R5_VALIDATOR_WORDING_SCOPE_GUARD: Keep as watch unless validator false positives recur in Phase3 plan tests; then distinguish exclusion wording from target classification.

## interface contracts
### input_contract
- preserve raw original
- read latest next-lane for continuation-only prompts
- separate user approval from execution permission
### space_reference_contract
- selected refs require exists/sha256/used_for/changed_judgment
- rejected refs should be logged when they materially prevent archaeology/decorative citation
- space_reference_delta must explain how judgment changed
### merge_contract
- show original + selected space refs + model reasoning merge
- include why_not_model_only where model-only drift risk exists
- include minimal_space_delta across reentry surfaces
### agent_role_contract
- Codex: spatial delta/reentry review
- Gemini: layer/big-frame/inward-collapse review
- compare unique delta and productive vs duplicative overlap when heavy mode is justified
### operator_surface_contract
- mind-sized status
- HOLD boundary
- minimal space delta line
- evidence handles
- clear next safe lane
### budget_contract
- FAST_NO_CALL_LOCAL_VALIDATION by default for known safe lanes
- HEAVY_BUDGETED only for explicit agent role test, architecture/principle ambiguity, drift/risk, cross-agent comparison need
- post-review only on disagreement, STOP/HOLD_STOP_REVIEW, or unclear reinsertion effect

## pre-apply checklist
- Confirm this spec matches the reviewed structure
- Choose HOLD / revise spec / approve bounded apply lane
- If approving, name exact apply lane and allowed files/surfaces
- Do not mutate authority/registry/current-position unless separately authorized
- Run validation after any future bounded apply

## out of scope
- implementation changes
- source/schema mutation
- authority/current-position mutation
- registry updates
- API/direct/server/replay
- Codex/Gemini new calls
- promotion

NEXT_SAFE_LANE: PRE_APPROVAL_STRUCTURE_SPEC_REVIEW_HOLD_OR_APPROVE_BOUNDED_APPLY_V0

HOLD: no authority/registry/current-position/source/schema/implementation apply.
