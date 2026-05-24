# Bridge Real Operation Worklist v0

## 1. Verdict

```text
BRIDGE_REAL_OPERATION_WORKLIST_PREPARED_WITH_REAL_CODEX_GEMINI_EXECUTION_HOLD
```

## 2. Status

```text
status: preflight_worklist_candidate
authority: sandbox-local candidate
scope: move from asset-only rehearsal toward real operation test
execution_status: no real Codex/Gemini run yet
promotion_status: no promotion
```

This worklist does not authorize execution.
It lists the required work before a real operation test.

## 3. Ordered Work

### Step 1 — Close the current topology state

Status:

```text
done
```

Output:

```text
FLOW_NETWORK_CURRENT_EXECUTION_TOPOLOGY_STATE_V0.md
```

### Step 2 — Asset-only structural rehearsal

Status:

```text
done
```

Output:

```text
asset_only_bridge_rehearsal_v0/
```

Result:

```text
ASSET_ONLY_CODEX_GEMINI_RECOVERY_REHEARSAL_RETURNED_WITH_WATCH
```

### Step 3 — Create Codex request template

Status:

```text
in this batch
```

Output:

```text
CODEX_WORKER_REQUEST_V0.md
```

Purpose:

```text
Codex must receive a bounded request object before any Gemini or Hermes-runner work.
```

### Step 4 — Create Gemini lite output contract

Status:

```text
in this batch
```

Output:

```text
GEMINI_LITE_OUTPUT_CONTRACT_V0.md
```

Purpose:

```text
Gemini output must be recoverable without becoming truth or forcing raw reread by default.
```

### Step 5 — Create Hermes runner receipt contract

Status:

```text
in this batch
```

Output:

```text
HERMES_RUNNER_RECEIPT_CONTRACT_V0.md
```

Purpose:

```text
Hermes must prove what happened and what did not happen.
```

### Step 6 — Create real operation test gate packet

Status:

```text
in this batch, HOLD by default
```

Output:

```text
REAL_OPERATION_TEST_GATE_PACKET_V0.md
```

Purpose:

```text
Define the exact approval fields needed before real Codex/Gemini/model transport can run.
```

### Step 7 — Real operation test

Status:

```text
HOLD until explicit packet-bound approval
```

Required before execution:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: [exact path]
APPROVED_CODEX_REQUEST_FILE: [exact path]
APPROVED_GEMINI_REQUEST_FILE: [exact path or none]
APPROVED_OUTPUT_DIR: [exact path]
APPROVED_CODEX_COMMAND: [exact command or none]
APPROVED_GEMINI_COMMAND: [exact command or none]
APPROVED_NETWORK_SCOPE: none | model_api_transport_only | separately_declared
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no | separately_declared
APPROVED_PROMOTION: no
```

## 4. Current HOLD

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

## 5. Next Decision

After this batch, the next decision is not conceptual.
It is whether the user wants to grant packet-bound approval for a minimal real operation test.

Default:

```text
no real execution
```
