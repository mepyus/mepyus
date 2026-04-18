[[A]] [[OBJ:doc_graphrag_enterprise_next_loop_gate_validation_v1_operation_receipt]] [[SEM:operation_receipt_for_graphrag_and_enterprise_gate_validation]]

# doc_graphrag_enterprise_next_loop_gate_validation_v1 operation receipt

- created_at: 2026-03-28
- operator: Codex
- operation_type: bounded multi-asset gate validation
- primary_inputs:
  - `inputs/external_cases/graphrag_neosh.txt`
  - `inputs/external_cases/enterprise.txt`
- supporting_generated:
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_segmentation_probe_v1_w3_s1_20260328T104511Z.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_segmentation_probe_v1_w6_s3_20260328T104511Z.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_engine_purpose_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/question_inducing_block_graphrag_neosh_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_multi_pass_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_context_unit_candidates_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_paragraph_role_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/enterprise_segmentation_probe_v1_w3_s1_20260328T104511Z.json`
  - `app/work/dialogue_loop_test/generated/enterprise_segmentation_probe_v1_w6_s3_20260328T104511Z.json`
  - `app/work/dialogue_loop_test/generated/enterprise_engine_purpose_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/question_inducing_block_enterprise_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/enterprise_multi_pass_validation_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/enterprise_context_unit_candidates_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/enterprise_paragraph_role_validation_v1_20260328.json`
- produced:
  - `docs/reports/graphrag_enterprise_next_loop_gate_validation_v1.md`
- updated:
  - `runtime/views/repo_delta_log_latest_v1.md`
- verdict:
  - `ENTRY_GATE_NOT_PASSED` for both assets
- note:
  - `graphrag_neosh.txt` and `enterprise.txt` both needed segmentation support before second-order validation. After support, reusable attitudes survived, but question-inducing candidates stayed at zero, context units remained fallback-grounded, and role-like readings showed scaffold carryover rather than generalized recovery. These assets reinforce the current object-lift hold rather than reopen the next loop gate.
