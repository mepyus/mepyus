# Hermes Runner Receipt Contract v0

## 1. Verdict

```text
HERMES_RUNNER_RECEIPT_CONTRACT_V0_DRAFTED_AS_TEMPLATE_ONLY_WITH_EXECUTION_HOLD
```

## 2. Status

```text
status: receipt_contract_candidate
authority: sandbox-local candidate
scope: Hermes runner receipt for bounded bridge tests
execution_status: template only
promotion_status: no promotion
```

This contract is not execution approval.
A receipt is evidence, not authority.

## 3. Purpose

Define the receipt shape Hermes must write after any bounded runner action so Codex and VectorFL can see what happened and what did not happen.

Core rule:

```text
Hermes command success != VectorFL approval.
Receipt existence != recovery approval.
```

## 4. Required JSON Shape

```json
{
  "verdict": "[RETURNED_WITH_WATCH | STOPPED | FAILED]",
  "status": "[structural_rehearsal_complete | execution_complete | stopped | failed]",
  "packet_path": "[exact path]",
  "request_path": "[exact path]",
  "output_dir": "[exact path]",
  "command_executed": "[exact command or none]",
  "exit_code": null,
  "files_read": ["[exact path]"],
  "files_written": ["[exact path]"],
  "real_codex_executed": false,
  "real_gemini_executed": false,
  "simulated_codex_only": false,
  "simulated_gemini_only": false,
  "network_used": false,
  "model_api_transport_used": false,
  "live_web_lookup_used": false,
  "external_source_fetch_used": false,
  "browser_used": false,
  "mcp_used": false,
  "external_connector_used": false,
  "memory_modified": false,
  "skill_modified": false,
  "cron_modified": false,
  "config_modified": false,
  "vectorfl_authority_modified": false,
  "promotion_performed": false,
  "recovery_required_by_codex": true,
  "recovery_completed_by_codex": false,
  "recovery_class_hint": "none | receipt | residue | candidate | component | proposal | STOP",
  "watch": ["[watch item]"],
  "hold": ["[hold item]"],
  "timestamp": "[ISO-8601]"
}
```

## 5. Required Negative Evidence

Receipt must explicitly state whether these were used or modified:

```text
real_codex_executed
real_gemini_executed
network_used
model_api_transport_used
live_web_lookup_used
external_source_fetch_used
browser_used
mcp_used
external_connector_used
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_modified
promotion_performed
```

Missing negative fields should be treated as WATCH or STOP depending on risk.

## 6. STOP Conditions

STOP if:

```text
runner reads undeclared files
runner writes outside approved output dir
command differs from approved command
network/model API transport appears without approval
live web/source lookup appears without approval
external connector is touched
memory/skill/cron/config is modified
VectorFL authority file is modified
receipt claims approval or promotion
Codex recovery is required but skipped
```

## 7. WATCH

```text
receipt treated as authority
command success treated as recovery approval
negative evidence omitted
output dir too broad
real model transport hidden under generic network field
```

## 8. HOLD

```text
execution without packet-bound approval
network/model transport without explicit scope
external connector
persistence mutation
promotion
```
