# Gemini Component Proposal Review Prompt v0

Read only these workspace-local files:
- COMPONENT_PROPOSAL_PACKET_V0.md
- PROPOSAL_REVIEW_INPUT_MANIFEST_V0.json
- review_inputs/01_REQUIREMENTS_S8_CLASSIFICATION_RECEIPT_V0.json
- review_inputs/02_REQUIREMENTS_S8_CLASSIFICATION_REPORT_V0.md
- review_inputs/03_REQUIREMENTS_CLOSURE_RECEIPT_V0.json
- review_inputs/04_REQUIREMENTS_CLOSURE_REPORT_V0.md
- review_inputs/05_codex_requirements_recovery_return.md
- review_inputs/06_gemini_requirements_lite_output.json

Task:
Assess whether this evidence is ready for a future component proposal review packet, not promotion.
Return only a JSON object with keys:
- observed_inputs
- proposal_candidate_name
- proposal_supporting_evidence
- required_conditions
- unresolved_blockers
- watch_items
- hold_items
- recommended_classification_one_of_proposal_incomplete_proposal_candidate_ready_proposal_review_ready_STOP
- do_not_promote
- next_review_questions
- completion_signal = GEMINI_PROPOSAL_LITE_DONE

Hard boundaries:
- Do not claim promotion.
- Do not claim registry/schema/workflow integration.
- Do not mutate files.
- Treat output as evidence for Codex recovery only.
