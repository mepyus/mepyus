# Real Operation Test Gate Packet v0

## 1. Verdict

```text
REAL_OPERATION_TEST_GATE_PACKET_V0_PREPARED_WITH_DEFAULT_EXECUTION_HOLD
```

## 2. Status

```text
status: real_operation_gate_packet_candidate
authority: sandbox-local candidate
scope: minimal real operation test gate for Codex-owned / Hermes-run / Gemini-lite bridge
execution_approval: no
promotion_status: no promotion
```

This packet does not authorize real Codex execution.
This packet does not authorize real Gemini execution.
This packet does not authorize network/model API transport.
This packet does not authorize live web/source lookup.
This packet does not authorize external connectors.
This packet does not authorize promotion.

## 3. Purpose

Define the smallest safe gate for a future real operation test after template preflight.

Selected pattern:

```text
CODEX_OWNED_HERMES_RUN_GEMINI_LITE_BRIDGE_V0
```

Minimal real-test route:

```text
User approval
  -> Hermes reads approved packet/request/templates
    -> Hermes runs exact approved command only if provided
      -> output written under approved output dir
        -> receipt written
          -> Codex recovery check
            -> VectorFL recovery classification
              -> no promotion unless separately approved
```

## 4. Required Inputs Before Any Real Test

```text
CODEX_WORKER_REQUEST_V0.md
GEMINI_LITE_OUTPUT_CONTRACT_V0.md
HERMES_RUNNER_RECEIPT_CONTRACT_V0.md
approved concrete request file
approved output directory
approved exact command or explicit no-command rehearsal
approved network scope
```

## 5. Default Approval State

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

No real test may run while this remains `no`.

## 6. Required Approval Block For Real Test

A real test requires the user to provide this block with exact values:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bridge_real_operation_preflight_v0/REAL_OPERATION_TEST_GATE_PACKET_V0.md
APPROVED_CODEX_WORKER_REQUEST: [exact path]
APPROVED_OUTPUT_DIR: [exact path]
APPROVED_CODEX_COMMAND: [exact command or none]
APPROVED_GEMINI_COMMAND: [exact command or none]
APPROVED_NETWORK_SCOPE: none | model_api_transport_only | separately_declared
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no | separately_declared
APPROVED_EXTERNAL_CONNECTOR: no | separately_declared
APPROVED_PROMOTION: no
```

If Gemini CLI/API is used, `APPROVED_NETWORK_SCOPE` cannot be `none`; it must explicitly be `model_api_transport_only` or more specifically declared.

If live search/browsing/source fetch is used, it must be separately declared and approved.

## 7. Minimal Test Options

### Option 0 — No-command dry approval rehearsal

```text
real_codex: no
real_gemini: no
network: none
purpose: verify approval block and output contracts only
```

Safe default.

### Option 1 — Real Codex Only, No Gemini

```text
real_codex: yes
real_gemini: no
network/model transport: depends on Codex CLI requirements
purpose: test whether Codex can consume CODEX_WORKER_REQUEST_V0 and produce recovery return
```

Requires exact Codex command and model transport approval.

### Option 2 — Real Gemini Script Lens Only, No Codex

```text
real_codex: no
real_gemini: yes
network/model transport: model_api_transport_only if CLI/API requires it
purpose: test Gemini lite output contract only
```

Requires exact Gemini command and model transport approval.

### Option 3 — Real Codex + Real Gemini Bridge

```text
real_codex: yes
real_gemini: yes
network/model transport: explicitly approved
purpose: end-to-end bridge test
```

Not recommended as first real test.

## 8. Recommended First Real Test

Recommended first real operation test:

```text
Option 1 or Option 2, not Option 3.
```

Safer order:

```text
1. Real Codex Only consumes CODEX_WORKER_REQUEST_V0 and produces recovery return.
2. Real Gemini Only produces GEMINI_LITE_OUTPUT_CONTRACT_V0 output from declared files.
3. Only then attempt combined bridge.
```

## 9. Output Contract

Approved output dir must contain:

```text
runner_receipt.json
operation_report.md
codex_return.md if Codex is run
gemini_lite_output.json if Gemini is run
gemini_raw_output.[json|md|txt] if Gemini raw output exists
```

## 10. STOP Conditions

STOP before execution if:

```text
approval block missing
exact command missing for real tool run
network scope ambiguous
model API transport not approved
live web/source lookup ambiguous
output dir not exact
request file not exact
promotion requested
```

STOP during/after execution if:

```text
command reads undeclared files
command writes outside approved output dir
network/model transport exceeds approved scope
live web/source lookup occurs without approval
external connector touched
memory/skill/cron/config modified
VectorFL authority file modified
receipt missing negative evidence
Codex recovery skipped
Gemini output claims truth/promotion
```

## 11. Current HOLD

```text
real Codex run
real Gemini run
model API transport
network/live web/source lookup
external connector
cron / recurring automation
memory / skill / config mutation
VectorFL authority mutation
AGENTS.md / SKILL.md / current-position / output_manifest update
baseline / workflow / schema / registry / ontology / component promotion
```

## 12. Final Gate Line

```text
This packet is ready for user approval review, not execution.
```
