# Real Gemini-Only Lite Test Request v0

## 1. Verdict

```text
REAL_GEMINI_ONLY_LITE_TEST_REQUEST_PREPARED_FOR_OPTION2
```

## 2. Status

```text
status: concrete_gemini_lite_request_candidate
scope: Option 2 real Gemini-only lite output test
real_codex_execution: no
real_gemini_execution: approved by user message "보강할 것 보강하고 제미나이로 넘어가자"
model_api_transport: model_api_transport_only
live_web_source_lookup: no
external_connector: no
promotion_status: no promotion
```

## 3. Purpose

Run a minimal real Gemini-only test to check whether Gemini can consume declared bridge assets and produce a lite output compatible with the strengthened GEMINI_LITE_OUTPUT_CONTRACT_V0.

## 4. Declared Input Files

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/GEMINI_LITE_OUTPUT_CONTRACT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_SEARCH_TO_CODEX_GEMINI_REHEARSAL_PACKET_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/asset_only_bridge_rehearsal_v0/ASSET_ONLY_BRIDGE_REHEARSAL_RECEIPT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/outputs/codex_recovery_return.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option1_codex_only_v0/HERMES_REAL_CODEX_ONLY_EXECUTION_RECEIPT_V0.json
```

## 5. Declared Output Directory

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option2_gemini_only_v0/outputs
```

## 6. Gemini Task

Gemini should:

```text
1. Use only declared input files.
2. Do not run Codex.
3. Do not use live web/source lookup.
4. Do not use external connectors, browser, MCP, memory, skill, cron, config, or VectorFL authority mutation.
5. Treat all inputs as candidate evidence, not authority.
6. Produce only a JSON object compatible with GEMINI_LITE_OUTPUT_CONTRACT_V0.
7. Include negative_evidence, receipt_conflict_check, raw_audit_trigger, WATCH-like risks, and do_not_promote lines.
8. Do not promote anything.
```

## 7. Expected Outputs Written By Hermes Shell Wrapper

```text
gemini_raw_output.txt
gemini_lite_output.json
```

Gemini itself should only emit JSON to stdout. Hermes captures stdout and extracts/validates JSON.

## 8. Exact Command Family

```bash
gemini --approval-mode plan --sandbox --output-format text -p "[prompt from GEMINI_ONLY_LITE_TEST_PROMPT_V0.md]" > gemini_raw_output.txt
```

## 9. HOLD

```text
Codex execution
combined bridge
live web/source lookup
external connector
browser/MCP
memory/skill/cron/config mutation
VectorFL authority mutation
promotion
```
