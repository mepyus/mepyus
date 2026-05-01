# Gemini Runner Preflight Checklist v0

## 0. Status

- status: sandbox candidate
- automation: false
- source_space_rule: false
- baseline: false
- production_workflow: false

## 1. Purpose

manual Gemini runner를 실제 sandbox task에 사용하기 전에 확인해야 할 preflight 항목을 정리한다.

## 2. Preflight Commands

포함:

```bash
bash scripts/sandbox/run_gemini_packet.sh --preflight
```

```bash
gemini -p "Reply with exactly: GEMINI_SMOKE_OK" --output-format json
```

```bash
bash scripts/sandbox/run_gemini_packet.sh --smoke-text --timeout-seconds 60
```

## 3. Pass Conditions

* gemini binary exists
* gemini version is recorded
* output directories writable
* smoke-text returns expected answer
* raw output saved
* outbox output saved

## 4. PASS_WITH_NOTE Conditions

* dry-run works but real call timeout
* auth state unclear
* network state unclear
* JSON parsing uncertain but raw output saved

## 5. FAIL Conditions

* gemini binary missing
* script syntax fail
* output directory not writable
* credential value leaked
* source-space modified
* automation created

## 6. Non-Automation Guardrail

This checklist is for manual-triggered terminal execution only.
It does not create automation, hook, MCP, watch mode, background runner, router, controller, or production workflow.
