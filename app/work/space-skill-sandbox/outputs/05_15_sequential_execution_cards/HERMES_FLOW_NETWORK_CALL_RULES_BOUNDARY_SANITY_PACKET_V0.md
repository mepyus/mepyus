# Hermes Flow-Network Call Rules Boundary Sanity Packet v0

Copy this whole prompt into the active Hermes terminal only if the user explicitly chooses to run it.

---

You are Hermes Agent acting as a native local execution workbench candidate for VectorFL.

This is a **read-only Stage 1 boundary sanity check**.

This is not component promotion.
This is not workflow creation.
This is not automation.
This is not a Hermes skill.
This is not a VectorFL authority update.

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. Purpose

Review whether the newly drafted VectorFL Flow-Network Call Rules correctly route Hermes surface requests through:

```text
IIC -> SOF -> MOL -> Packet -> Lane -> RML -> Recovery -> Promotion Gate
```

Specifically check whether Hermes routing is bounded correctly:

```text
"헤르메스에게 이거 시켜봐"
  should not execute if payload is vague
  should require SOF permission check
  should require Packet Builder
  should return report/receipt
  should not become VectorFL authority
```

## 2. Source Materials to Read

Read only:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_FLOW_NETWORK_CALL_RULES_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_CALL_RULES_DRY_RUN_CURRENT_INPUT_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_CALL_RULES_DRY_RUN_HERMES_SURFACE_REQUEST_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_FLOW_NETWORK_ATTACHMENT_MODEL_V0.md
```

Do not read the whole repo.
Do not use git.
Do not inspect source code.
Do not use network.

## 3. Hard Boundary

Do not:

```text
modify source files
modify prior documents
run git
run git add
run git commit
run git reset
run git checkout
install packages
use network
call browser
call MCP
connect to external apps
send messages
create cron
edit Hermes memory
create or edit Hermes skill
change Hermes config
update AGENTS.md
create SKILL.md
update VectorFL authority files
update current-position
update output_manifest
promote anything to component/workflow/schema/registry/ontology/baseline
write outside the declared output directory
```

Allowed:

```text
create one declared sandbox output directory
read only declared source materials
write one markdown report
write one JSON receipt
print a concise terminal summary
```

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_flow_network_call_rules_boundary_sanity_v0/
```

Allowed output files:

```text
flow_network_call_rules_boundary_sanity_report.md
flow_network_call_rules_boundary_sanity_receipt.json
```

## 5. Review Questions

Answer:

```text
1. Do the call rules preserve IIC -> SOF -> MOL -> Packet -> Lane -> RML -> Recovery?
2. Does the Hermes surface dry-run correctly stop before execution when payload is vague?
3. Is Packet Builder required before Hermes execution?
4. Does the packet language avoid treating packet draft as execution approval?
5. Does Hermes capability remain separate from permission?
6. Does Hermes success remain receipt, not VectorFL approval?
7. Are HOLD/STOP boundaries strong enough?
8. What is the single weakest boundary in the call rules?
```

## 6. Expected Report

Write:

```text
flow_network_call_rules_boundary_sanity_report.md
```

Include:

```text
verdict
files read
files created
route consistency judgment
Hermes boundary judgment
Packet Builder judgment
Recovery class judgment
weakest boundary
recommended next smallest action
WATCH
HOLD
```

## 7. Expected Receipt

Write:

```text
flow_network_call_rules_boundary_sanity_receipt.json
```

Include:

```text
verdict
timestamp
input_files
output_files
network_used
git_used
packages_installed
source_files_modified
prior_documents_modified
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_files_modified
current_position_updated
output_manifest_updated
baseline_workflow_schema_registry_ontology_promoted
```

## 8. Recovery Suggestion

Use:

```text
receipt:
  Hermes reviewed call-rule boundary with report/receipt evidence.

residue:
  weakest-boundary notes and routing ambiguity.

candidate:
  call rules become stronger if Hermes confirms boundaries.

component:
  no.

space_update_proposal:
  no.

STOP:
  any attempt to execute vague payload, create workflow/skill/baseline, or update authority files.
```

## 9. Terminal Summary Format

Print:

```text
HERMES_FLOW_NETWORK_CALL_RULES_BOUNDARY_SANITY_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_flow_network_call_rules_boundary_sanity_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_flow_network_call_rules_boundary_sanity_v0/flow_network_call_rules_boundary_sanity_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_flow_network_call_rules_boundary_sanity_v0/flow_network_call_rules_boundary_sanity_receipt.json
    verdict: [HERMES_FLOW_NETWORK_CALL_RULES_BOUNDARY_SANITY_RETURNED_WITH_WATCH]
    watch: Hermes boundary sanity can strengthen call rules but does not authorize execution/promotion
```

## 10. Hard Stop Confirmation

Confirm:

```text
no Hermes execution beyond this read-only review
no source files modified
no prior documents modified
no git used
no package install
no network / browser / MCP
no Hermes memory / skill / cron / config edit
no AGENTS.md / SKILL.md update
no VectorFL authority update
no current-position / output_manifest update
no baseline / workflow / schema / registry / ontology promotion
no declared output directory outside write
```
