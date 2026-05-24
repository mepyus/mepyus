# VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0

status: S1_S8_LOOP_CHECKLIST_TEMPLATE_WITH_HOLD
created_at: 2026-05-23 11:13:11 KST

## Purpose

Reusable checklist for every bounded VectorFL/Hermes continuation.

## Required template

```yaml
loop_id: S1S8-YYYYMMDD-LAYER-NNNN
layer: <input_layer|evidence_layer|review_guard_layer|surface_layer|tool_reentry_layer|operator_recovery_layer>
claim_under_test: <what might be true>
S1_diagnose:
  observed_risk:
  expected_contract:
  drift_pressure:
S2_verify:
  files_checked:
  checksums_checked:
  declared_scope:
S3_test:
  test_type: <local_validator|fixture_rehearsal|real_codex_review_only|real_gemini_gap_scan>
  command_or_fixture:
  expected_result:
S4_reflect:
  actual_result:
  contract_drift_found:
  lesson:
S5_apply:
  applied_change:
  not_applied:
S6_surface:
  user_label:
  guard_status:
  forbidden_interpretation:
S7_receipt:
  receipt_path:
  state_mutations_observed:
S8_decide_next:
  next_smallest_action:
  stop_or_continue:
HOLD:
  authority_mutation: NO
  promotion_status: HOLD
  program_alpha_ready: NO
```

## Minimum pass criteria

```text
all S1-S8 fields present
one concrete test listed
one reflection listed
one applied or intentionally-not-applied change listed
HOLD/WATCH/STOP surface label preserved
no promotion/authority/readiness claim
```
