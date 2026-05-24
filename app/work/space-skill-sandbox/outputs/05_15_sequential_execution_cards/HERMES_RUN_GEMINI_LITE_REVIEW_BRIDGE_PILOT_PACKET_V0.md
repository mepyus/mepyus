# Hermes-Run Gemini Lite Review Bridge Pilot Packet v0

## 1. Verdict

```text
HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_DRAFTED_WITH_DISPATCH_HOLD
```

## 2. Status

```text
status: future_pilot_packet_candidate
scope: Codex-owned, Hermes-run Gemini Lite review bridge
authority: sandbox-local candidate
target_level: Level 1.5 to Level 2 pilot design
```

This is not:

```text
workflow
automation
schema
registry
ontology
baseline
component
AGENTS.md
SKILL.md
current-position
output_manifest
```

This packet is not execution approval.

This packet does not run Hermes.

This packet does not run Gemini.

This packet does not connect tools.

This packet does not promote the bridge pattern.

## 3. Packet Identity

```text
PACKET_ID:
  HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_V0

PACKET_VERSION:
  v0

PURPOSE:
  Test, in a future explicitly approved run, whether Hermes can run a Codex-authored Gemini Lite review request and return bounded output for Codex recovery check.
```

## 4. Execution Topology

```text
EXECUTION_TOPOLOGY:
  User / ChatGPT
    -> VectorFL packet review
      -> Hermes main runtime
        -> Gemini headless / lite review command
          -> Gemini raw lite output
            -> Codex recovery check
              -> Hermes receipt/report
                -> VectorFL recovery classification
                  -> User promotion decision if separately requested
```

```text
LANE_TYPE:
  HERMES_RUN_GEMINI_WITH_CODEX_RECOVERY

DISPATCH_TARGET:
  Hermes
```

Important correction:

```text
Codex owns the question and recovery frame.
Hermes may run the command only after packet-bound dispatch approval and SOF clearance.
Gemini explores; it does not judge final recovery or promotion.
Codex is not a runtime middle-hop in this pilot.
```

## 5. Role Declarations

```text
HERMES_ROLE:
  main runtime
  Gemini command runner if approved
  output manager
  receipt/report collector
  not VectorFL authority

CODEX_ROLE:
  Gemini request author
  scope limiter
  recovery checker
  over-promotion filter
  not unrestricted Hermes delegate

GEMINI_ROLE:
  bulk exploration lens
  pattern collector
  candidate/residue scanner
  not truth source
  not component approver
```

## 6. Dispatch Approval

Default:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

The only line that can signal user dispatch approval is:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Future dispatch approval must be packet-bound:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes

APPROVED_PACKET_PATH:
  app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_PACKET_V0.md

APPROVED_GEMINI_REQUEST_FILE:
  [declared path]

APPROVED_OUTPUT_DIR:
  [declared path]

APPROVED_COMMAND:
  [exact command]

APPROVED_NETWORK_SCOPE:
  model_api_transport_only | none | separately_declared

APPROVED_PROMOTION:
  no
```

Even if the line is present:

```text
packet valid != dispatch approval
dispatch approval != SOF clearance
SOF clearance != VectorFL promotion approval
Hermes command success != VectorFL approval
Gemini output != truth
```

## 7. SOF Risk Family

```text
SOF_RISK_FAMILY:
  technical/local execution
  research/web/source if Gemini uses web
  automation/persistence if repeated or scheduled
  mixed if network, external source, memory, skill, cron, config, or connector pressure appears
```

Initial pilot should prefer:

```text
technical/local execution
```

by using only declared local input files and no live web/source lookup.

## 7.1 Network / API Boundary

Gemini CLI execution may require model API transport.

Separate model transport from live browsing or external source lookup:

```text
MODEL_API_TRANSPORT:
  allowed only if explicitly declared in dispatch approval

LIVE_WEB_SOURCE_LOOKUP:
  no, unless separately approved

EXTERNAL_SOURCE_FETCH:
  no, unless separately approved
```

Receipt must split these fields:

```text
model_api_transport_used: yes/no
live_web_lookup_used: yes/no
external_source_fetch_used: yes/no
network_used_for_other_reason: yes/no
```

If Gemini requires model API transport and dispatch approval says network scope is `none`:

```text
STOP
```

## 8. Allowed Future Actions

Allowed only after explicit dispatch approval and SOF clearance:

```text
read one declared Gemini request file
read only declared local input files listed in the request
run one declared Gemini headless/lite command
write one Gemini raw lite output file
write one Hermes execution receipt
write one Hermes bridge report
write only inside the declared output directory
```

## 9. Forbidden Actions

```text
no recurring automation
no cron
no background watcher
no Hermes memory write
no Hermes skill creation/update
no Hermes config mutation
no MCP call
no browser automation
no external connector use
no live web/source lookup unless separately approved
no model API transport unless explicitly declared in dispatch approval
no email/Slack/Telegram/CRM/DB/Obsidian write
no package install
no git add / commit / reset / checkout
no source patch
no repo-wide search unless separately declared
no VectorFL authority file mutation
no AGENTS.md update
no SKILL.md creation
no current-position update
no output_manifest update
no baseline/workflow/schema/registry/ontology promotion
no component promotion
```

## 10. Input Contract

Future pilot input should be bounded.

```text
GEMINI_REQUEST_FILE:
  [declared path]

LOCAL_INPUT_FILES:
  - [declared path]
  - [declared path]

OUTPUT_DIR:
  [declared path]
```

The request file must include:

```text
task purpose
files allowed to read
files forbidden to read
desired lite output format
do_not_promote instructions
WATCH/HOLD reminders
raw limits
questions for Codex
```

No implicit repo-wide context is allowed.

## 11. Gemini Lite Output Contract

Gemini should return this shape.

```text
GEMINI_BULK_REVIEW_LITE

observed_files:
  - [path or label]

repeated_patterns:
  - [pattern]

candidate_items:
  - [candidate only, not component]

uncertainties:
  - [unknown / evidence gap]

possible_risks:
  - [risk]

do_not_promote:
  - [what must not be promoted]

questions_for_codex:
  - [question]

raw_limits:
  - [scope and limitation]
```

Forbidden output posture:

```text
official structure
component approved
workflow approved
update memory
write SKILL.md
baseline confirmed
policy created
```

## 12. Hermes Receipt Contract

Hermes receipt must include:

```text
packet_id
packet_version
dispatch_approval_present: yes/no
SOF_clearance_claim: clear / conditional / HOLD / STOP
command_run
exit_code
input_files_read
output_files_written
network_used: yes/no
model_api_transport_used: yes/no
live_web_lookup_used: yes/no
external_source_fetch_used: yes/no
network_used_for_other_reason: yes/no
browser_used: yes/no
MCP_used: yes/no
external_connector_used: yes/no
memory_modified: yes/no
skill_modified: yes/no
cron_modified: yes/no
config_modified: yes/no
VectorFL_authority_modified: yes/no
timestamp
```

## 13. Hermes Report Contract

Hermes report must include:

```text
verdict
topology used
Gemini request file
Gemini output file
receipt path
limits
WATCH
HOLD
recommended recovery class
explicit non-promotion statement
```

## 14. Codex Recovery Check Contract

Codex should later check:

```text
1. Did Gemini stay inside declared scope?
2. Did Gemini return Lite output?
3. Did Gemini over-promote?
4. Did Hermes preserve receipt/report boundary?
5. Did any permission inheritance drift occur?
6. What recovery class is appropriate?
7. What is the next smallest action?
```

Recovery classes:

```text
receipt:
  pilot ran with evidence

residue:
  bridge bottleneck / output-shape / boundary observations

candidate:
  bridge pattern may be useful

component:
  HOLD

space_update_proposal:
  HOLD unless user explicitly asks

STOP:
  unauthorized execution, persistence, external side effect, authority mutation, or promotion pressure
```

## 15. Minimal Future Command Shape

This packet does not choose the final command.

Future command must be declared before dispatch.

Permitted command shape examples:

```text
gemini -p [prompt text or request file content]
gemini --prompt [declared request]
gemini [headless/lite equivalent supported in local environment]
```

The actual available Gemini CLI syntax must be verified in the local Hermes environment before any run.

No command is approved by this document.

## 16. Validation Checklist

Before dispatch eligibility:

```text
[ ] exact packet path named
[ ] EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes present and packet-bound
[ ] SOF clearance performed
[ ] Gemini request file declared
[ ] input files declared
[ ] output directory declared
[ ] actual Gemini command declared
[ ] model API transport scope declared
[ ] no live web/source lookup unless separately approved
[ ] no Hermes memory/skill/cron/config mutation
[ ] no external connector side effect
[ ] no VectorFL authority update
[ ] receipt/report contract accepted
[ ] Codex recovery check remains required
[ ] no promotion requested in this run
```

## 17. Expected Future Terminal Summary

If a future run is separately approved and executed, expected summary shape:

```text
HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_run_gemini_lite_review_bridge_pilot_v0/
    gemini_request: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_run_gemini_lite_review_bridge_pilot_v0/gemini_lite_review_request.md
    gemini_output: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_run_gemini_lite_review_bridge_pilot_v0/gemini_lite_review_output.md
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_run_gemini_lite_review_bridge_pilot_v0/hermes_run_gemini_lite_review_bridge_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_run_gemini_lite_review_bridge_pilot_v0/hermes_run_gemini_lite_review_bridge_receipt.json
    verdict: [HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_RETURNED_WITH_WATCH]
    watch: Hermes-run Gemini may reduce Codex runtime burden, but does not authorize automatic bridge or promotion
```

## 18. WATCH

```text
packet draft becoming dispatch approval
Hermes-run Gemini becoming automatic bridge
Gemini output becoming truth
Codex recovery check being skipped
Hermes receipt becoming VectorFL approval
Lite output becoming schema
bridge pilot becoming workflow
network/web use sneaking into local pilot
model API transport being confused with live web/source lookup
permission inheritance drift
```

## 19. HOLD

```text
no Hermes dispatch from this packet alone
no Gemini execution from this packet alone
no Codex worker execution
no bridge connected
no recurring automation
no cron
no external connector use
no web/network unless separately approved in future packet
no memory write
no skill creation/update
no config mutation
no VectorFL authority file mutation
no AGENTS.md update
no SKILL.md creation
no current-position update
no output_manifest update
no baseline/workflow/schema/registry/ontology promotion
no component promotion
```

## 20. Hard Stop Confirmation

```text
No Hermes execution performed.
No Gemini execution performed.
No Codex worker execution performed.
No bridge connected.
No command run performed.
No network/API/browser/MCP call performed.
No external connector used.
No memory/skill/cron/config changed.
No authority file updated.
No promotion performed.
```

## 21. Next Smallest Action

If continuing, perform a packet validity review only:

```text
FLOW_NETWORK_PACKET_VALIDITY_REVIEW_FOR_HERMES_RUN_GEMINI_LITE_REVIEW_BRIDGE_PILOT_V0
```

Do not execute the pilot.
