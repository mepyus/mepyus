# Codex Recovery Over Real Gemini Lite Request v0

## 1. Verdict

```text
CODEX_RECOVERY_OVER_REAL_GEMINI_LITE_REQUEST_PREPARED_FOR_OPTION2R
```

## 2. Status

```text
status: concrete_codex_recovery_request
scope: Option 2R real Codex recovery over real Gemini lite output
real_codex_execution: approved by user continuation
real_gemini_execution: no new Gemini run
model_api_transport: model_api_transport_only for Codex CLI
live_web_source_lookup: no
external_connector: no
promotion_status: no promotion
```

## 3. Purpose

Run Codex recovery over the real Gemini-only lite output generated in Option 2. Codex should validate the lite output, normalize WATCH issues, decide whether the separate Option 1 and Option 2 tests justify moving to a bounded combined bridge rehearsal, and avoid promotion.

## 4. Declared Input Files

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2_gemini_only_v0/outputs/gemini_lite_output.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2_gemini_only_v0/HERMES_REAL_GEMINI_ONLY_EXECUTION_RECEIPT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2_gemini_only_v0/HERMES_REAL_GEMINI_ONLY_EXECUTION_REPORT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs/codex_recovery_return.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/HERMES_REAL_CODEX_ONLY_EXECUTION_RECEIPT_V0.json
```

## 5. Declared Output Directory

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2r_codex_recovery_over_gemini_v0/outputs
```

## 6. Codex Task

Codex should:

```text
1. Read only declared input files.
2. Do not run Gemini.
3. Do not use live web/source lookup, browser, MCP, external connectors, memory, skill, cron, config, or VectorFL authority mutation.
4. Treat Gemini lite output as evidence, not truth.
5. Validate the lite output against GEMINI_LITE_OUTPUT_CONTRACT_V0.
6. Normalize these WATCH items:
   - Gemini uncertainty that real Gemini execution remained unverified in observed prior receipts.
   - Gemini raw_limits phrase 'model_api_transport_only for Codex CLI' should be corrected to Gemini CLI for Option 2 context.
7. Decide whether separate Option 1 and Option 2 successes are sufficient to attempt a bounded combined bridge rehearsal.
8. Produce one markdown return file under the declared output directory:
   codex_recovery_over_gemini_lite_return.md
9. Include verdict, output_shape_validity, normalized_watch, bridge_readiness, recovery_class_hint, HOLD, and next_smallest_action.
10. Do not promote anything.
```

## 7. Expected Output

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2r_codex_recovery_over_gemini_v0/outputs/codex_recovery_over_gemini_lite_return.md
```

## 8. HOLD

```text
new Gemini execution
combined bridge execution
live web/source lookup
external connector
memory/skill/cron/config mutation
VectorFL authority mutation
promotion
```
