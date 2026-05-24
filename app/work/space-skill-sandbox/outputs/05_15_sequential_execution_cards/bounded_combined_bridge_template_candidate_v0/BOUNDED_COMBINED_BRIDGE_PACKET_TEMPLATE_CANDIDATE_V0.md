# Bounded Combined Bridge Packet Template Candidate v0

## 1. Verdict

```text
BOUNDED_COMBINED_BRIDGE_PACKET_TEMPLATE_CANDIDATE_V0_PREPARED_NO_PROMOTION
```

## 2. Status

```text
status: reusable_packet_template_candidate
derived_from: Option 3A bounded combined bridge rehearsal
recovery_class_hint: candidate
promotion_status: no promotion
authority_status: not authority
component_status: not component
workflow_status: not workflow
schema_registry_ontology_baseline_status: none
```

This file is a reusable candidate packet form only.
It does not approve execution by itself.
It does not promote any artifact.
It does not mutate VectorFL authority.

## 3. Purpose

Use this template when a bounded combined bridge lane is needed:

```text
Hermes main workbench
  -> real Gemini CLI/script lens produces raw+lite evidence
    -> real Codex CLI recovers over Gemini lite output
      -> Hermes writes receipt/report
        -> VectorFL recovery gate only
```

Core rule:

```text
The packet prepares a lane. It is not dispatch approval.
Dispatch approval is not transitive.
Gemini output is evidence, not truth.
Codex recovery is classification evidence, not promotion.
Hermes success is receipt evidence, not VectorFL authority.
```

## 4. Required Approval Block

A real run requires this block filled exactly:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes | no
APPROVED_PACKET_PATH: [absolute path to filled packet instance]
APPROVED_OUTPUT_DIR: [absolute output directory]
APPROVED_GEMINI_COMMAND: [exact Gemini CLI command or wrapper command]
APPROVED_CODEX_COMMAND: [exact Codex CLI command]
APPROVED_NETWORK_SCOPE: model_api_transport_only
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no
APPROVED_EXTERNAL_CONNECTOR: no
APPROVED_BROWSER_MCP: no
APPROVED_MEMORY_SKILL_CRON_CONFIG_MUTATION: no
APPROVED_VECTORFL_AUTHORITY_MUTATION: no
APPROVED_PROMOTION: no
```

Default if missing:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

## 5. Lane Type

```text
LANE_TYPE: HERMES_RUN_GEMINI_THEN_CODEX_RECOVERY_BOUNDED
EXECUTION_TOPOLOGY:
  Hermes main workbench
  -> Gemini lite-output lens
  -> Codex recovery worker
  -> Hermes receipt/report
  -> VectorFL recovery gate
```

## 6. Roles

```text
Hermes:
  prepare bounded prompt/request
  run approved local commands
  capture raw/lite/return outputs
  write receipt/report
  no authority mutation
  no promotion

Gemini:
  read declared files only
  produce raw output and lite JSON
  include negative_evidence
  include receipt_conflict_check
  include raw_audit_trigger
  no truth claim
  no promotion claim

Codex:
  read declared files only
  recover over Gemini lite output
  verify output shape and permission boundary
  restore WATCH/HOLD
  classify recovery hint
  no Gemini rerun
  no source/authority mutation
  no promotion

VectorFL:
  recovery gate only
  promotion gate separate

User:
  dispatch approval
  model transport approval
  side-effect approval
  promotion approval if ever requested separately
```

## 7. Declared Inputs Section

A filled packet must list exact files.

```text
DECLARED_GEMINI_INPUT_FILES:
  - [absolute path]

DECLARED_CODEX_INPUT_FILES:
  - [absolute path to filled packet]
  - [absolute path to gemini_lite_output.json]
  - [absolute path to gemini_raw_output.txt or omit unless raw audit needed]
  - [absolute path to GEMINI_LITE_OUTPUT_CONTRACT]
  - [absolute path to prior recovery/check evidence if any]
```

Rules:

```text
No broad repo scan by default.
No live web/source lookup.
No external source fetch.
No browser/MCP.
No authority files unless explicitly declared as read-only evidence and not mutated.
```

## 8. Expected Outputs Section

A filled packet must bind exact output paths.

```text
OUTPUT_DIR: [absolute path]
EXPECTED_OUTPUTS:
  - [OUTPUT_DIR]/gemini_raw_output.txt
  - [OUTPUT_DIR]/gemini_lite_output.json
  - [OUTPUT_DIR]/codex_combined_bridge_recovery_return.md
  - [packet directory]/HERMES_COMBINED_BRIDGE_RECEIPT.json
  - [packet directory]/HERMES_COMBINED_BRIDGE_REPORT.md
```

## 9. Gemini Lite Output Requirements

Gemini must produce one JSON object with:

```text
format: GEMINI_BULK_REVIEW_LITE_V0
status: returned_with_watch | stopped
observed_files
repeated_patterns
candidate_items
uncertainties
possible_risks
questions_for_codex
do_not_promote
negative_evidence
receipt_conflict_check
raw_audit_trigger
raw_limits
stop_flags
```

Required negative evidence:

```json
{
  "promotion_claimed": false,
  "component_approval_claimed": false,
  "workflow_schema_registry_ontology_baseline_claimed": false,
  "truth_claimed": false,
  "live_web_source_lookup_used": false,
  "external_connector_used": false,
  "memory_skill_cron_config_instruction_present": false
}
```

## 10. Codex Recovery Requirements

Codex must return:

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

Codex must explicitly check:

```text
declared_input_scope_respected_by_recovery
gemini_execution_rerun_by_codex
browser_or_live_web_used
external_connector_used
mcp_used
memory_skill_cron_config_mutation
source_or_authority_files_modified
write_scope
promotion_status
```

## 11. STOP Conditions

Stop and return receipt/report only if:

```text
approval block missing or says no
Gemini command not exact
Codex command not exact
output directory not exact
Gemini lite JSON invalid
Gemini stop_flags non-empty
negative_evidence missing or internally inconsistent
receipt conflict requires Codex resolution and cannot be resolved
Codex attempts source/authority mutation
Codex reruns Gemini without explicit approval
live web/source lookup occurs without approval
external connector occurs without approval
memory/skill/cron/config mutation requested or performed
promotion/component/baseline/schema/registry/ontology claim appears
```

## 12. WATCH

```text
packet mistaken for dispatch approval
model API transport mistaken for live web/source lookup
Gemini confidence mistaken for truth
Codex recovery mistaken for promotion
Hermes receipt mistaken for VectorFL authority
candidate template mistaken for component
permission inheritance during combined model transport
raw output never audited when needed
```

## 13. HOLD

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

## 14. Recovery Class

Default recovery class for successful bounded runs:

```text
candidate
```

Never auto-promote from this template.
