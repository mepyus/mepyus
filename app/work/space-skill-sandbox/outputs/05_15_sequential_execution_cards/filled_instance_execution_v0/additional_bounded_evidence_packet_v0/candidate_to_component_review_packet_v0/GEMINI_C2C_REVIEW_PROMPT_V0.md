# Gemini Candidate-to-Component Review Prompt v0

Read only these workspace-local files:
- CANDIDATE_TO_COMPONENT_REVIEW_PACKET_V0.md
- C2C_REVIEW_INPUT_MANIFEST_V0.json
- review_inputs/01_S8_SCOPE_GAP_RECOVERY_GATE_RECEIPT_V0.json
- review_inputs/02_S8_SCOPE_GAP_RECOVERY_GATE_REPORT_V0.md
- review_inputs/03_HERMES_SCOPE_GAP_EVIDENCE_RECEIPT_V0.json
- review_inputs/04_HERMES_SCOPE_GAP_EVIDENCE_REPORT_V0.md
- review_inputs/05_gemini_scope_gap_lite_output.json
- review_inputs/06_codex_scope_gap_recovery_return.md

Task:
Evaluate whether the candidate evidence is ready for a future component proposal.
Return only a JSON object with keys:
- observed_inputs
- blocker_status
- component_proposal_supporting_evidence
- component_proposal_blockers
- watch_items
- hold_items
- recommended_classification_one_of_candidate_locked_candidate_upgrade_review_needed_component_proposal_ready_STOP
- do_not_promote
- questions_for_codex
- completion_signal = GEMINI_C2C_LITE_DONE

Hard boundaries:
- Do not claim promotion.
- Do not mutate files.
- Do not use live web/source lookup.
- Do not use browser/MCP/external connectors.
- Treat output as evidence for Codex recovery only.
- If any input cannot be read, classify STOP.
