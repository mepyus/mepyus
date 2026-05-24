# Gemini Proposal Diversification Review Prompt v0

Read only these workspace-local files:
- DIVERSIFICATION_GATE_PACKET_V0.md
- DIVERSIFICATION_INPUT_MANIFEST_V0.json
- review_inputs/01_PROPOSAL_S8_CLASSIFICATION_RECEIPT_V0.json
- review_inputs/02_PROPOSAL_S8_CLASSIFICATION_REPORT_V0.md
- review_inputs/03_COMPONENT_PROPOSAL_RECEIPT_V0.json
- review_inputs/04_COMPONENT_PROPOSAL_REPORT_V0.md
- review_inputs/05_codex_proposal_recovery_return.md
- review_inputs/06_gemini_proposal_lite_output.json

Task:
Prevent over-convergence. Generate multiple viable proposal shapes and a reject/defer option.
Do not choose a final architecture.
Return only a JSON object with keys:
- observed_inputs
- current_candidate
- alternative_shapes
- reject_or_defer_option
- anti_convergence_checks
- shared_requirements_preserved
- discriminating_tests
- watch_items
- hold_items
- recommended_classification_one_of_breadth_insufficient_breadth_candidate_ready_diversified_proposal_set_ready_STOP
- do_not_promote
- next_review_questions
- completion_signal = GEMINI_DIVERSIFICATION_LITE_DONE

Hard boundaries:
- Do not claim promotion.
- Do not choose a final structure.
- Do not claim registry/schema/workflow integration.
- Treat output as evidence for Codex recovery only.
