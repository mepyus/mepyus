You are CODEX_SPACE_MATURATION_BY_REENTRY_RECORD for VectorFL.

You are being used through local Codex CLI/script bridge, not as a direct API target.
This is the second-pass Codex role: read Hermes reentry and decide space maturation.

Read first:
1. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/16_hermes_execution_trace_and_codex_reentry_record_v0.json
2. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/15_hermes_model_merge_from_codex_retrieval_v0.json
3. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/09_CODEX_REENTRY_AFTER_HERMES_MERGE_AND_EXECUTION.md
4. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/07_CODEX_SPACE_RETRIEVAL_RETURN_PACKET_PLACEHOLDER.json
5. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/03_codex_reference_path_index_v0.json
6. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md

Goal:
Decide what, if anything, should be matured in the VectorFL space after Hermes merged the original + Codex retrieval + model interpretation. This is still HOLD/proposal only.

Important role boundary:
- Hermes remains the original/merge/execute center.
- Codex owns space retrieval and later space maturation judgment.
- Gemini may be used only via Codex-linked script-chain if layer analysis is required, but do not invoke Gemini in this pass unless strictly necessary. If not used, set gemini_via_codex_script_used to NO.

Write exactly one JSON object to this output path:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_hermes_centered_codex_retrieval_maturation_setup_v0/19_CODEX_SPACE_MATURATION_RETURN_PACKET.json

Do not modify any other file.
Do not move folders.
Do not mutate source/authority/current-position/registry.
Do not run API/direct/server/replay/local HTTP.
Promotion status must remain HOLD.

Required JSON fields:
- packet_id
- role
- read_files
- maturation_decision
- space_assets_to_reindex
- gemini_via_codex_script_used
- gemini_findings_ref_or_inline
- changed_judgment
- next_safe_lane
- promotion_status

Recommended additional fields:
- proposed_index_additions
- proposed_task_packet_handle_rule
- proposed_first_pass_vs_optional_refs_rule
- rejected_maturation_actions
- risks
