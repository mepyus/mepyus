# Option 3A Bounded Combined Bridge Request v0

## 1. Verdict

```text
OPTION3A_BOUNDED_COMBINED_BRIDGE_REQUEST_PREPARED_FOR_SINGLE_REHEARSAL
```

## 2. Status

```text
status: concrete_combined_bridge_rehearsal_request
scope: one-shot combined Hermes-run Gemini + Codex recovery
real_gemini_execution: approved by user continuation for this bounded lane
real_codex_execution: approved by user continuation for this bounded lane
network_scope: model_api_transport_only for Gemini CLI and Codex CLI
live_web_source_lookup: no
external_connector: no
promotion_status: no promotion
authority_mutation: no
```

## 3. Purpose

Test the smallest combined bridge lane after successful split tests:

```text
Hermes prepares bounded prompt
  -> real Gemini CLI produces raw/lite evidence
    -> real Codex CLI recovers over the new lite output
      -> Hermes writes receipt/report
```

This is still a rehearsal. It is not a promotion, component, registry, baseline, schema, ontology, or workflow update.

## 4. Declared Gemini Input Files

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2r_codex_recovery_over_gemini_v0/outputs/codex_recovery_over_gemini_lite_return.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2r_codex_recovery_over_gemini_v0/HERMES_OPTION2R_CODEX_RECOVERY_RECEIPT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_CURRENT_EXECUTION_TOPOLOGY_STATE_V0.md
```

## 5. Declared Codex Input Files

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/OPTION3A_COMBINED_BRIDGE_REQUEST_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/outputs/gemini_lite_output.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/outputs/gemini_raw_output.txt
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2r_codex_recovery_over_gemini_v0/outputs/codex_recovery_over_gemini_lite_return.md
```

## 6. Declared Output Directory

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/outputs
```

## 7. Expected Outputs

```text
outputs/gemini_raw_output.txt
outputs/gemini_lite_output.json
outputs/codex_combined_bridge_recovery_return.md
HERMES_OPTION3A_COMBINED_BRIDGE_RECEIPT_V0.json
HERMES_OPTION3A_COMBINED_BRIDGE_REPORT_V0.md
```

## 8. Gemini Task

Gemini should produce exactly one JSON object following GEMINI_BULK_REVIEW_LITE_V0. It must treat all source material as candidate evidence only.

Required emphasis:

```text
combined bridge rehearsal only
no truth claims
no component approval
no promotion
negative_evidence required
receipt_conflict_check required
raw_audit_trigger required
stop_flags required
```

## 9. Codex Task

Codex should read the new Gemini lite output and recover it. Codex must return:

```text
verdict
combined_bridge_shape_validity
permission_boundary_check
recovery_class_hint
promotion_status
WATCH
HOLD
next_smallest_action
```

## 10. HOLD

```text
live web/source lookup
external connector
browser/MCP
memory/skill/cron/config mutation
VectorFL authority mutation
AGENTS.md / SKILL.md / current-position / output_manifest update
baseline/workflow/schema/registry/ontology/component promotion
recurring automation
```
