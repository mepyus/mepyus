# S0-S8 Route Map v0

verdict:
  S0_S8_ROUTE_MAP_PREPARED_WITH_S8_REHEARSED_AND_EXECUTION_HOLD

route_state_table:
  S0_DRY_RUN_PROOF: completed / template_instance_dry_run_v0 preserved
  S1_EXECUTION_STRUCTURE_PREP: completed / packet/prompts/contracts prepared
  S2_REVIEW_ONLY_PREFLIGHT: completed / local preflight + Codex review-only prompt
  S3_EXECUTION_HARNESS_READY: completed / guarded runner/materializer/validators/closeout scripts
  S4_APPROVAL_GATE_WAITING: active / real execution blocked until explicit approval
  S5_GEMINI_SPACE_MEDIATED_RUN: not_entered / requires approval yes; writes real gemini raw/lite
  S6_CODEX_SPACE_MEDIATED_RECOVERY: not_entered / requires valid real Gemini outputs; writes real Codex recovery
  S7_HERMES_RECEIPT_REPORT_CLOSEOUT: not_entered / requires real Gemini+Codex outputs; writes real receipt/report
  S8_VECTORFL_RECOVERY_GATE: rehearsed_no_authority_only / synthetic/no-model classification candidate; no authority mutation

important_current_truth:
  The route has been built and rehearsed through S8 only in no-model/no-authority mode.
  The real lane remains at S4_APPROVAL_GATE_WAITING.
  S5/S6/S7 real model-mediated stages are not entered.

evidence:
  S8 rehearsal verdict: S8_VECTORFL_GATE_REHEARSAL_CLASSIFIED_CANDIDATE_WITH_PROMOTION_HOLD
  positive no-model rehearsal: NO_MODEL_REHEARSAL_PASS_WITH_EXECUTION_HOLD
  negative rehearsal: NEGATIVE_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED
  handoff: OPERATOR_HANDOFF_BUNDLE_PREPARED_WITH_EXECUTION_HOLD
  steward packet: EXTERNAL_STEWARD_REVIEW_PACKET_PREPARED_WITH_EXECUTION_HOLD

remaining_before_real_S5:
  explicit packet-scoped execution approval
  packet approval field changed to yes
  promotion remains no
  static validator pass immediately before run

remaining_before_real_S8_authority:
  real S5/S6/S7 outputs
  separate VectorFL recovery decision
  separate authority mutation approval if any
  separate promotion approval if any

WATCH:
  S8 rehearsal mistaken as real VectorFL gate acceptance
  candidate classification mistaken as component
  no-model route completion mistaken as model execution

HOLD:
  real Gemini execution
  real Codex execution
  real Hermes closeout
  VectorFL authority mutation
  promotion

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
