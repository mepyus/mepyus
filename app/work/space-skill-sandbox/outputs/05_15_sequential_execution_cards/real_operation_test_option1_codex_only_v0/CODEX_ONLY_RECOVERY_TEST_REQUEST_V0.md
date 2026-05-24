# Codex Only Recovery Test Request v0

## 1. Verdict

```text
CODEX_ONLY_RECOVERY_TEST_REQUEST_PREPARED_WITH_EXECUTION_HOLD_PENDING_EXACT_APPROVAL
```

## 2. Status

```text
status: concrete_codex_worker_request_candidate
authority: sandbox-local candidate
scope: Option 1 real Codex-only recovery test
real_codex_execution: HOLD until explicit approval block
real_gemini_execution: no
model_api_transport: HOLD until explicit approval
live_web_source_lookup: no
external_connector: no
promotion_status: no promotion
```

This request does not authorize execution by itself.

## 3. Purpose

Run a minimal real Codex-only test, if approved, to check whether Codex can consume the current bridge preflight assets and produce a bounded recovery return without invoking Gemini.

## 4. Declared Input Files

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/CODEX_WORKER_REQUEST_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/HERMES_RUNNER_RECEIPT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/REAL_OPERATION_TEST_GATE_PACKET_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_SEARCH_TO_CODEX_GEMINI_REHEARSAL_PACKET_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/GEMINI_INTERNAL_EXPLORATION_LITE_SIMULATED_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_ONLY_BRIDGE_REHEARSAL_RECEIPT_V0.json
```

## 5. Declared Output Directory

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs
```

## 6. Codex Task If Approved

Codex should:

```text
1. Read only the declared input files.
2. Do not run Gemini.
3. Do not use browser, live web/source lookup, MCP, external connectors, memory, skill, cron, config, or VectorFL authority mutation.
4. Treat the simulated Gemini lite output as evidence only, not truth.
5. Check whether CODEX_WORKER_REQUEST_V0 is sufficient for real bridge use.
6. Check whether GEMINI_LITE_OUTPUT_CONTRACT_V0 is sufficient for later Gemini output recovery.
7. Check whether HERMES_RUNNER_RECEIPT_CONTRACT_V0 is sufficient negative evidence.
8. Produce one markdown return file under the declared output directory:
   codex_recovery_return.md
9. Include verdict, scope_validity, contract_gaps, WATCH, HOLD, recovery_class_hint, and next_smallest_action.
10. Do not promote anything.
```

## 7. Expected Output

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs/codex_recovery_return.md
```

## 8. Recommended Exact Command If Approved

```bash
codex exec "Read only the declared files in /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/CODEX_ONLY_RECOVERY_TEST_REQUEST_V0.md. Do not modify source or authority files. Do not run Gemini. Do not use browser, web/source lookup, MCP, external connectors, memory, skill, cron, or config. Write only one file: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs/codex_recovery_return.md. Return a bounded Codex recovery check with verdict, scope_validity, contract_gaps, WATCH, HOLD, recovery_class_hint, and next_smallest_action. No promotion."
```

## 9. Approval Required

Real Codex execution requires explicit approval with exact command and model transport scope.

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

## 10. HOLD

```text
real Codex run until explicit approval
real Gemini run
live web/source lookup
external connector
memory/skill/cron/config mutation
VectorFL authority mutation
promotion
```
