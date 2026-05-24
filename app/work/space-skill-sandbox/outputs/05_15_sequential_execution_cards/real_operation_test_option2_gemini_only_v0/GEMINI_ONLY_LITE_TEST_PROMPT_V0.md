You are running a bounded Gemini-only lite-output test for VectorFL bridge topology.

STRICT SCOPE:
Read/use only these declared input files:
1. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
2. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_SEARCH_TO_CODEX_GEMINI_REHEARSAL_PACKET_V0.md
3. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_ONLY_BRIDGE_REHEARSAL_RECEIPT_V0.json
4. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs/codex_recovery_return.md
5. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/HERMES_REAL_CODEX_ONLY_EXECUTION_RECEIPT_V0.json

DO NOT:
- run Codex
- use live web/source lookup
- use external connector
- use browser or MCP
- modify files
- modify memory/skill/cron/config
- mutate VectorFL authority files
- promote anything

TASK:
Produce only one JSON object compatible with GEMINI_LITE_OUTPUT_CONTRACT_V0.
No markdown fences. No prose outside JSON.

Required JSON fields:
format, status, request_id, source_scope, observed_files, repeated_patterns, candidate_items, uncertainties, possible_risks, questions_for_codex, do_not_promote, negative_evidence, receipt_conflict_check, raw_audit_trigger, raw_limits, stop_flags.

Set:
format = GEMINI_BULK_REVIEW_LITE_V0
request_id = REAL_GEMINI_ONLY_LITE_TEST_V0
source_scope = declared files only; no live web/source lookup; model_api_transport_only

Important semantics:
- Treat all inputs as candidate evidence, not truth.
- This output is evidence for Codex recovery, not approval.
- Include negative_evidence with false values for promotion_claimed, component_approval_claimed, workflow_schema_registry_ontology_baseline_claimed, truth_claimed, live_web_source_lookup_used, external_connector_used, memory_skill_cron_config_instruction_present unless you actually detect such a problem.
- receipt_conflict_check must compare the Codex-only receipt/report claims against the packet/lite contract at a high level.
- raw_audit_trigger.required should be true only if required fields are missing, over-promotion language appears, receipt conflict appears, or uncertainty requires audit.
- Include do_not_promote entries.
- recovery class should remain candidate if mentioned inside candidate_items or questions.

Output JSON only.