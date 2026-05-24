# Flow-Network Current Execution Topology State v0

## 1. Verdict

```text
FLOW_NETWORK_CURRENT_EXECUTION_TOPOLOGY_STATE_PREPARED_AS_SANDBOX_LOCAL_CANDIDATE_WITH_LEVEL_2_EXECUTION_HOLD
```

## 2. Status

```text
status: current_execution_topology_state_candidate
scope: Hermes / Codex / Gemini operating topology for VectorFL recovery
authority: sandbox-local candidate
current_level: Level 1.5 ready, cautious Level 2 design ready
execution_status: no real bridge execution authorized
promotion_status: no promotion
```

This is not:

```text
workflow
schema
registry
ontology
baseline
component
AGENTS.md
SKILL.md
current-position
output_manifest
automation
recurring bridge
execution approval
promotion approval
```

This document only closes the current topology state as candidate material.
It does not authorize Hermes, Codex, Gemini, browser, network, MCP, connector, cron, memory, skill, config, or VectorFL authority mutation.

## 3. Purpose

The purpose of this state document is to consolidate the current operating topology discovered through the 05-15 sequential execution cards and the later Hermes / Codex / Gemini bridge checks.

The goal is not to create tool automation.

The goal is:

```text
reduce user transfer burden
preserve user approval points
preserve VectorFL recovery and promotion gates
prevent permission inheritance
make external tool outputs recoverable through packet / receipt / return contracts
```

Short line:

```text
Hermes runs.
Codex frames and recovers.
Gemini explores.
VectorFL gates.
User approves.
```

## 4. Source Asset Anchors

This state closes over the following candidate assets:

```text
INDEX.md
OPERATING_MAP.md
CURRENT_CANDIDATE_STATE_V0.md
FLOW_NETWORK_PROGRAM_TOPOLOGY_CHECK_V0.md
FLOW_PACKET_TOPOLOGY_FIELDS_V0.md
FLOW_NETWORK_GEMINI_BRIDGE_BOTTLENECK_CHECK_V0.md
HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_V0.md
gemini_script_runner_boundary_sandbox_v0/outputs/sandbox_feasibility_report.md
gemini_script_runner_boundary_sandbox_v0/outputs/runner_receipt.json
gemini_script_runner_boundary_sandbox_v0/outputs/gemini_lite_output_simulated.json
```

These are candidate operating materials only.
They do not form a registry, baseline, workflow, schema, or component.

## 5. Current Asset Map By Layer

### 5.1 State / Navigation Layer

```text
INDEX.md
OPERATING_MAP.md
CURRENT_CANDIDATE_STATE_V0.md
```

Role:

```text
show what exists
show how to choose which artifact to read
prevent candidate pile from mimicking registry or baseline
compress current candidate state
```

Current state from the candidate note:

```text
promising: yes
validated: no
promotable: no
local integration ready: no
usable in chat/sandbox: yes
```

### 5.2 Flow / Topology Layer

```text
FLOW_NETWORK_PROGRAM_TOPOLOGY_CHECK_V0.md
```

Role:

```text
insert real program-use topology into the Flow-Network lane stage
preserve the existing Flow-Network anchor
```

Base flow:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

Program topology insertion point:

```text
MOL -> Packet -> Dispatch Approval -> Lane
```

### 5.3 Packet Contract Layer

```text
FLOW_PACKET_TOPOLOGY_FIELDS_V0.md
HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_V0.md
```

Role:

```text
standardize transfer fields
reduce repeated user explanation
separate packet validity from dispatch approval
separate dispatch approval from SOF clearance
separate execution success from recovery/promotion approval
```

### 5.4 Bottleneck / Execution Split Layer

```text
FLOW_NETWORK_GEMINI_BRIDGE_BOTTLENECK_CHECK_V0.md
```

Role:

```text
identify Codex runtime burden as the current Gemini bridge bottleneck
separate question framing from process execution
preserve Codex as space steward and recovery judge
```

### 5.5 Sandbox / Feasibility Layer

```text
gemini_script_runner_boundary_sandbox_v0/outputs/sandbox_feasibility_report.md
gemini_script_runner_boundary_sandbox_v0/outputs/runner_receipt.json
gemini_script_runner_boundary_sandbox_v0/outputs/gemini_lite_output_simulated.json
```

Role:

```text
show that Codex-authored request -> bounded local runner -> raw/lite output + receipt/report is structurally feasible
confirm local simulation only
confirm no real Codex, Gemini, network, connector, memory, skill, cron, config, authority mutation, or promotion occurred
```

Sandbox verdict:

```text
GEMINI_SCRIPT_RUNNER_BOUNDARY_SANDBOX_SIMULATION_RETURNED_WITH_WATCH
```

## 6. Selected Operating Pattern

Selected current pattern:

```text
CODEX_OWNED_HERMES_RUN_GEMINI_LITE_BRIDGE_V0
```

Meaning:

```text
Codex owns the question, scope, and recovery frame.
Hermes acts as the execution workbench and possible runner host.
Gemini acts as a bounded bulk exploration lens.
VectorFL receives recovered evidence through report / receipt / return path.
User keeps dispatch, side-effect, and promotion approval.
```

Preferred execution topology:

```text
User / ChatGPT
  -> VectorFL packet review
    -> Codex-authored request
      -> Hermes-hosted bounded runner if explicitly approved
        -> Gemini script lens or simulated lens
          -> raw output + lite output
            -> Codex recovery check
              -> Hermes receipt/report
                -> VectorFL recovery classification
                  -> User promotion decision only if separately requested
```

The selected pattern is not pure `Hermes -> Codex -> Gemini`.

It is more precise to describe the preferred pattern as:

```text
Codex-owned request
Hermes-run execution
Gemini-lite output
Codex recovery
VectorFL gate
```

## 7. Non-Selected Patterns

### 7.1 Full Automation Bridge

```text
Hermes automatically calls Codex and Gemini repeatedly or recursively.
```

Status:

```text
HOLD
```

Reason:

```text
risks permission inheritance, persistence drift, memory/skill/cron pollution, external side effects, and promotion confusion
```

### 7.2 Hermes-Directed Gemini Without Codex Framing

```text
Hermes writes or decides the Gemini prompt, runs Gemini, summarizes, and sends directly to VectorFL.
```

Status:

```text
not selected as default
```

Reason:

```text
skips Codex as space steward and recovery checker
increases risk that Hermes summary becomes de facto recovery judgment
```

### 7.3 Codex-Run Gemini As Default

```text
Codex writes prompt, runs Gemini script, waits, parses full output, and writes recovery.
```

Status:

```text
available but not preferred for repeated broad checks
```

Reason:

```text
simple authority chain but high Codex token/runtime/process burden
```

### 7.4 Gemini-As-Judge Pattern

```text
Gemini reads broad context and directly decides truth, component status, or promotion.
```

Status:

```text
rejected
```

Reason:

```text
Gemini is an exploration lens, not truth source or VectorFL authority
```

## 8. Permission Boundary

Core rule:

```text
Dispatch approval is not transitive.
Capability is not permission.
```

### 8.1 Hermes Boundary

Hermes may, if packet-approved:

```text
read declared input files
run exact approved local command
write declared output files
collect receipt/report
host a bounded script runner
```

Hermes may not infer permission to:

```text
mutate VectorFL authority files
promote artifacts
write AGENTS.md or SKILL.md
modify current-position or output_manifest
create or edit memory
create or edit skill
create or edit cron
modify config
use browser/network/MCP/external connector without separate approval
treat command success as VectorFL approval
```

### 8.2 Codex Boundary

Codex may:

```text
author request
limit scope
review lite output
inspect raw output only if needed
perform recovery check
package return packet
```

Codex may not:

```text
inherit unrestricted Hermes permissions
mutate outside declared repo-side scope
skip recovery because Hermes succeeded
promote without user approval
treat Gemini output as truth
```

### 8.3 Gemini Boundary

Gemini may:

```text
compare
cluster
summarize
surface repeated patterns
produce raw/lite candidate evidence
support residue/candidate maturation
```

Gemini may not:

```text
approve truth
approve component
approve promotion
replace Codex recovery
replace VectorFL gate
become registry or baseline source
```

### 8.4 User / ChatGPT Boundary

User / ChatGPT retain:

```text
direction setting
WATCH/HOLD judgment
dispatch approval
model API transport approval
external side-effect approval
promotion approval
STOP decision
```

## 9. Return Path

Required return path for the selected pattern:

```text
Gemini raw output
  -> Gemini lite output
    -> Codex recovery check
      -> Codex return packet or recovery summary
        -> Hermes receipt/report
          -> VectorFL recovery classification
            -> User promotion decision if separately requested
```

Do not collapse this into:

```text
Gemini output -> truth
Hermes report -> approval
Codex request -> dispatch
receipt -> authority
recovery classification -> promotion
```

## 10. Raw / Lite / Receipt / Report Contract

### 10.1 raw_output

Role:

```text
full model/script output or broad evidence dump
kept for audit or exception review
not default Codex input if too large
```

Authority:

```text
evidence only
not truth
not recovery approval
not promotion basis by itself
```

### 10.2 lite_output

Role:

```text
bounded structured reduction for Codex recovery check
captures observed files, repeated patterns, candidate items, uncertainties, risks, and questions
```

Authority:

```text
candidate evidence only
Codex must still recover
VectorFL must still classify
```

### 10.3 receipt

Role:

```text
factual execution record
records files read/written and forbidden surfaces not used
```

Required negative fields for runner-style work:

```text
codex_executed
gemini_executed
simulated_gemini_only
network_used
model_api_transport_used
live_web_lookup_used
external_connector_used
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_modified
promotion_performed
```

Authority:

```text
receipt is evidence, not authority
```

### 10.4 report

Role:

```text
Hermes-side human-readable summary of what happened
```

Authority:

```text
report is not recovery approval
report is not promotion
```

### 10.5 return_packet

Role:

```text
Codex-side recovered summary for VectorFL recovery classification
```

Authority:

```text
may suggest discard / receipt / residue / candidate / component / proposal / STOP
but does not self-promote
```

## 11. Current Approval Points

Approval points that must remain with User / ChatGPT:

```text
1. Dispatch approval for a specific packet
2. SOF clearance when risk family requires it
3. Model API transport approval
4. Live web/source lookup approval
5. External connector or side-effect approval
6. Persistence approval if any output is meant to outlive sandbox
7. Promotion approval
```

Packet-bound approval must include at minimum:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: [exact path]
APPROVED_REQUEST_FILE: [exact path]
APPROVED_OUTPUT_DIR: [exact path]
APPROVED_COMMAND: [exact command]
APPROVED_NETWORK_SCOPE: none | model_api_transport_only | separately_declared
APPROVED_PROMOTION: no
```

Even then:

```text
dispatch approval != SOF clearance
SOF clearance != promotion approval
```

## 12. Current WATCH

```text
1. Hermes main runtime may be mistaken for VectorFL authority.
2. Codex-authored request may be mistaken for dispatch approval.
3. Gemini lite output may be mistaken for truth.
4. Hermes receipt/report may be mistaken for recovery approval.
5. Codex recovery check may be skipped after successful runner execution.
6. Script runner may drift into recurring automation.
7. Candidate artifact pile may mimic registry, baseline, or workflow.
8. Model API transport may be confused with live web/source lookup.
9. Raw output may overload Codex again if lite contract is not strict.
10. A successful sandbox simulation may be misread as real Gemini runtime validation.
```

## 13. Current HOLD

```text
real Codex run
real Gemini run
live Hermes-Codex-Gemini bridge connection
Level 3 tool-linked bridge
Level 4 recurring / automated bridge
cron or scheduled runner
external connector
browser / web / MCP / API use unless explicitly packet-approved
Hermes memory mutation
Hermes skill mutation
Hermes config mutation
VectorFL authority mutation
AGENTS.md update
SKILL.md update
current-position update
output_manifest update
baseline promotion
workflow promotion
schema promotion
registry promotion
ontology promotion
component promotion
```

## 14. Current Allowed Use

Allowed now without further promotion:

```text
manual reasoning
structured manual bridge design
Level 1.5 packet/receipt/return drafting
bounded local simulation only if explicitly requested and scoped
reading existing sandbox-local candidate assets
writing new sandbox-local candidate notes under the declared output directory
```

Not allowed by this document:

```text
real model/API execution
real Codex worker execution
real Gemini execution
network/source lookup
external app side effects
persistent automation
authority mutation
promotion
```

## 15. Next Template-Only Assets

Recommended next assets, in order:

```text
1. CODEX_WORKER_REQUEST_V0
2. GEMINI_SCRIPT_RUNNER_BOUNDARY_MODEL_V0
3. GEMINI_LITE_OUTPUT_CONTRACT_V0
4. HERMES_RUNNER_RECEIPT_CONTRACT_V0
```

These should be template-only unless separately approved.

### 15.1 CODEX_WORKER_REQUEST_V0

Purpose:

```text
define how Codex authors a bounded request for Hermes-hosted runner execution
```

Must include:

```text
request_id
owner
purpose
scope
input_files
output_dir
allowed_actions
forbidden_actions
model_api_transport_scope
live_web_lookup_scope
expected_outputs
recovery_required_by_codex
promotion_status
```

### 15.2 GEMINI_SCRIPT_RUNNER_BOUNDARY_MODEL_V0

Purpose:

```text
define runner role as tool/lens executor, not judge
```

Must include:

```text
read boundary
write boundary
network boundary
model API transport boundary
raw/lite output split
receipt requirements
STOP conditions
```

### 15.3 GEMINI_LITE_OUTPUT_CONTRACT_V0

Purpose:

```text
define compact output fields so Codex can recover without rereading all raw material by default
```

Must include:

```text
observed_files
repeated_patterns
candidate_items
uncertainties
possible_risks
questions_for_codex
do_not_promote
raw_limits
```

### 15.4 HERMES_RUNNER_RECEIPT_CONTRACT_V0

Purpose:

```text
define negative evidence fields proving what was not touched
```

Must include:

```text
files_read
files_written
network_used
model_api_transport_used
live_web_lookup_used
external_connector_used
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_modified
promotion_performed
```

## 16. Stop Conditions

Stop before execution if any of the following appear without explicit approval:

```text
request to run real Gemini
request to run real Codex
missing exact command
missing approved packet path
missing approved request file
missing approved output directory
network/API ambiguity
live web/source lookup ambiguity
external connector pressure
memory/skill/cron/config mutation pressure
VectorFL authority file mutation pressure
promotion language
AGENTS.md or SKILL.md mutation
current-position or output_manifest mutation
```

Stop after execution if any of the following occur:

```text
runner reads undeclared files
runner writes outside declared output dir
network is used unexpectedly
model API transport is used when not approved
live web/source lookup occurs unexpectedly
external connector is touched unexpectedly
memory/skill/cron/config is modified
VectorFL authority files are modified
output claims truth or promotion authority
receipt is missing negative evidence fields
Codex recovery step is skipped
```

## 17. Final State Line

```text
CURRENT_STATE:
  The operating topology is structurally usable as a Level 1.5 bridge and cautiously design-ready for Level 2.

SELECTED_PATTERN:
  CODEX_OWNED_HERMES_RUN_GEMINI_LITE_BRIDGE_V0

CURRENT_ACTION:
  use as sandbox-local candidate topology state only

DO_NOT_PROMOTE:
  do not promote to workflow, schema, registry, ontology, baseline, component, AGENTS.md, SKILL.md, current-position, or output_manifest

NEXT_STEP:
  draft template-only CODEX_WORKER_REQUEST_V0 or GEMINI_SCRIPT_RUNNER_BOUNDARY_MODEL_V0
```
