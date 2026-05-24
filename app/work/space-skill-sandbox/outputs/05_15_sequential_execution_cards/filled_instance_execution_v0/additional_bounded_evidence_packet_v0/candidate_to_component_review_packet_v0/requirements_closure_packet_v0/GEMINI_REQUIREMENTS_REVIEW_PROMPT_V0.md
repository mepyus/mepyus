# Gemini Requirements Closure Review Prompt v0

Read only these workspace-local files:
- REQUIREMENTS_CLOSURE_PACKET_V0.md
- REQ_REVIEW_INPUT_MANIFEST_V0.json
- review_inputs/01_C2C_S8_CLASSIFICATION_RECEIPT_V0.json
- review_inputs/02_C2C_S8_CLASSIFICATION_REPORT_V0.md
- review_inputs/03_C2C_REVIEW_RECEIPT_V0.json
- review_inputs/04_C2C_REVIEW_REPORT_V0.md
- review_inputs/05_codex_c2c_recovery_return.md
- review_inputs/06_gemini_c2c_lite_output.json

Task:
Turn the two remaining blockers into explicit component-proposal requirements.
Return only a JSON object with keys:
- observed_inputs
- permission_inheritance_requirement
- raw_audit_trigger_requirement
- acceptance_tests
- remaining_blockers
- watch_items
- hold_items
- recommended_classification_one_of_requirements_incomplete_requirements_candidate_ready_component_proposal_requirements_ready_STOP
- do_not_promote
- questions_for_codex
- completion_signal = GEMINI_REQUIREMENTS_LITE_DONE

Hard boundaries:
- Do not claim promotion.
- Do not mutate files.
- Do not use live web/source lookup.
- Treat output as evidence for Codex recovery only.
