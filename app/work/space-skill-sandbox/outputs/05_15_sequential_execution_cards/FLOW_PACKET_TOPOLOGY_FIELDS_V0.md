# Flow Packet Topology Fields v0

## 1. Verdict

```text
FLOW_PACKET_TOPOLOGY_FIELDS_DRAFTED_AS_CANDIDATE_WITH_EXECUTION_HOLD
```

## 2. Status

```text
status: field_definition_candidate
scope: packet topology fields for Hermes / Codex / Gemini bridge use
authority: sandbox-local candidate
target_level: Level 1.5 to Level 2 design only
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

This document does not authorize execution.

This document does not dispatch Hermes, Codex, or Gemini.

This document does not promote any packet, rule, component, or topology.

## 3. Purpose

Define the minimum fields a future Flow-Network packet should carry when a task may move through:

```text
Hermes main runtime
  -> Codex space worker
    -> Gemini exploration lens if explicitly declared
```

The goal is to reduce repeated user explanation while preserving approval boundaries.

Core rule:

```text
standardized packet fields reduce transfer burden;
they do not create execution approval.
```

## 4. Source Anchors

This field definition is aligned with:

```text
FLOW_NETWORK_PROGRAM_TOPOLOGY_CHECK_V0
FLOW_NETWORK_NEXT_HERMES_PACKET_USAGE_CARD_V0
FLOW_NETWORK_PACKET_VALIDITY_REVIEW_LINE_CLOSEOUT_V0
VECTORFL_FLOW_NETWORK_CALL_RULES_V0_1
```

The anchor chain remains:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

## 5. Core Packet Fields

Future packets should declare these fields before dispatch review.

```text
PACKET_ID:
  stable packet name

PACKET_VERSION:
  v0 / v0.1 / v1 candidate version

PURPOSE:
  what the packet is trying to test, review, execute, or recover

EXECUTION_TOPOLOGY:
  tool route being proposed

LANE_TYPE:
  one of the declared lane values

DISPATCH_TARGET:
  Hermes / Codex / Manual / User / ChatGPT-only

HERMES_ROLE:
  execution runtime / report collector / not used

CODEX_ROLE:
  space worker / repo-side reviewer / recovery formatter / not used

GEMINI_ROLE:
  exploration lens / candidate maturation aid / not used

RETURN_PATH:
  required path by which raw outputs return to VectorFL recovery

PERMISSION_INHERITANCE_BOUNDARY:
  explicit non-transitive permission statement

ALLOWED_ACTIONS:
  closed list of permitted actions

FORBIDDEN_ACTIONS:
  closed list of prohibited actions

TOOL_SURFACE:
  terminal / file read / file write / git / network / browser / MCP / memory / skill / cron / config / external app

EXTERNAL_SIDE_EFFECTS:
  none / declared / requires separate approval

PERSISTENCE_BOUNDARY:
  what may remain after execution

OUTPUT_CONTRACT:
  required output files or return text

RECEIPT_CONTRACT:
  required evidence of what happened

REPORT_CONTRACT:
  required interpretive report

RECOVERY_CLASS_HINT:
  expected recovery class

PROMOTION_STATUS:
  no promotion unless separately approved

DISPATCH_APPROVAL:
  explicit packet-bound approval line

SOF_RISK_FAMILY:
  technical/local execution / semantic/customer/business / automation/persistence / research/web/source / external app/live connector / mixed

SOF_CLEARANCE_REQUIRED:
  yes

WATCH:
  known misread or drift risks

HOLD:
  actions still held

STOP_CONDITIONS:
  conditions that stop the packet before or during dispatch
```

## 6. Lane Values

Use one of these values.

```text
CHATGPT_ONLY:
  explanation, judgment, documentation, scenario
  no execution

CODEX_LOCAL:
  repo-side structure check, packet creation, boundary review

HERMES_NATIVE:
  Hermes direct execution within declared scope

HERMES_TO_CODEX:
  Hermes prepares or invokes Codex worker request
  Codex receives declared scope only

HERMES_TO_CODEX_TO_GEMINI:
  Codex uses Gemini as broad exploration lens
  Gemini output is raw material, not truth

HERMES_EXTERNAL_APP:
  Hermes touches external app or connector
  side-effect approval required

MANUAL_BRIDGE:
  no direct tool connection
  user transfers packet/receipt/return path only
```

Current default:

```text
Design may describe HERMES_TO_CODEX or HERMES_TO_CODEX_TO_GEMINI.
Operation should remain MANUAL_BRIDGE or structured manual bridge unless separately approved.
```

## 7. Dispatch Approval Field

Default state:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
```

Only this exact line may indicate packet-bound dispatch approval:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Even when present:

```text
dispatch approval != SOF clearance
SOF clearance != VectorFL promotion approval
```

Approval is not transitive:

```text
User approves Hermes dispatch
  != User approves Codex unrestricted work

Hermes invokes Codex
  != Codex inherits Hermes tool permissions

Codex invokes Gemini
  != Gemini output becomes accepted knowledge
```

## 8. Return Path Templates

### LANE_3 / HERMES_TO_CODEX

```text
Hermes request
  -> Codex worker request
    -> Codex return packet
      -> Hermes receipt/report
        -> VectorFL recovery classification
          -> User / ChatGPT promotion decision if requested
```

### LANE_4 / HERMES_TO_CODEX_TO_GEMINI

```text
Hermes request
  -> Codex worker request
    -> Gemini exploration request
      -> Gemini raw output
        -> Codex recovery summary
          -> Hermes receipt/report
            -> VectorFL recovery classification
              -> User / ChatGPT promotion decision if requested
```

Forbidden shortcuts:

```text
Gemini raw output -> VectorFL component
Codex summary -> promotion
Hermes receipt -> approval
tool success -> authority mutation
```

## 9. Minimal Packet Skeleton

```text
PACKET_ID:
  [name]

PACKET_VERSION:
  v0

PURPOSE:
  [one bounded purpose]

EXECUTION_TOPOLOGY:
  [Hermes main runtime -> Codex space worker -> Gemini exploration lens if declared]

LANE_TYPE:
  [CHATGPT_ONLY | CODEX_LOCAL | HERMES_NATIVE | HERMES_TO_CODEX | HERMES_TO_CODEX_TO_GEMINI | HERMES_EXTERNAL_APP | MANUAL_BRIDGE]

DISPATCH_TARGET:
  [Hermes | Codex | Manual | User | ChatGPT-only]

HERMES_ROLE:
  [role or not used]

CODEX_ROLE:
  [role or not used]

GEMINI_ROLE:
  [role or not used]

RETURN_PATH:
  [exact expected path]

PERMISSION_INHERITANCE_BOUNDARY:
  Dispatch approval is not transitive.
  Hermes permission does not flow to Codex.
  Codex permission does not flow to Gemini.
  Gemini output does not become truth.
  Hermes orchestration does not become VectorFL approval.

ALLOWED_ACTIONS:
  [closed list]

FORBIDDEN_ACTIONS:
  [closed list]

TOOL_SURFACE:
  [declared surfaces only]

EXTERNAL_SIDE_EFFECTS:
  [none / declared / separate approval required]

PERSISTENCE_BOUNDARY:
  [allowed output paths and state changes]

OUTPUT_CONTRACT:
  [required output]

RECEIPT_CONTRACT:
  [required receipt]

REPORT_CONTRACT:
  [required report]

RECOVERY_CLASS_HINT:
  [discard | receipt | residue | candidate | component | space_update_proposal | STOP]

PROMOTION_STATUS:
  no promotion unless separately approved

DISPATCH_APPROVAL:
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no

SOF_RISK_FAMILY:
  [one risk family]

SOF_CLEARANCE_REQUIRED:
  yes

WATCH:
  [risks]

HOLD:
  [held actions]

STOP_CONDITIONS:
  [stop lines]
```

## 10. Validation Checklist

Before any packet can be considered dispatch-eligible, check:

```text
[ ] packet identity is exact
[ ] packet version is declared
[ ] purpose is bounded
[ ] lane type is one declared value
[ ] dispatch target is explicit
[ ] roles are separated
[ ] return path is explicit
[ ] permission inheritance boundary is present
[ ] allowed actions are closed
[ ] forbidden actions are closed
[ ] tool surface is declared
[ ] external side effects are none or separately approved
[ ] persistence boundary is clear
[ ] output contract is clear
[ ] receipt contract is clear
[ ] report contract is clear
[ ] recovery class hint is non-authoritative
[ ] promotion status says no promotion without separate approval
[ ] dispatch approval line is present only if user granted it for this packet
[ ] SOF risk family is declared
[ ] SOF clearance remains required
[ ] WATCH/HOLD/STOP are present
```

If any required field is missing:

```text
PACKET_INVALID_NEEDS_PATCH
```

If fields pass but approval is missing:

```text
PACKET_VALID_BUT_NO_DISPATCH_APPROVAL
```

If approval is present but SOF risk remains unresolved:

```text
PACKET_VALID_AND_DISPATCH_APPROVAL_PRESENT_BUT_SOF_HOLD
```

## 11. Recovery Classification

This field definition may be recovered as:

```text
receipt:
  topology field definition was drafted

candidate:
  reusable packet field set for future Flow-Network bridge packets
```

It is not:

```text
component
workflow
schema
registry
ontology
baseline
automation
```

## 12. WATCH

```text
field definition becoming schema
packet skeleton becoming workflow
lane value becoming automatic routing
dispatch approval becoming transitive permission
SOF clearance being skipped because packet is well formed
Gemini output becoming truth
Codex return becoming promotion
Hermes receipt becoming VectorFL approval
tool capability becoming permission
return path missing or reversed
```

## 13. HOLD

```text
no Hermes dispatch
no Codex worker invocation
no Gemini request
no tool-linked bridge
no recurring automation
no cron
no external connector execution
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

## 14. Hard Stop Confirmation

```text
No Hermes execution performed.
No Codex worker execution performed.
No Gemini execution performed.
No bridge connected.
No script run performed.
No external connector used.
No file outside this declared document was changed.
No authority file updated.
No promotion performed.
```

## 15. Next Smallest Action

If needed, draft:

```text
CODEX_WORKER_REQUEST_V0
```

as a request/return template only.

Do not execute Codex as a worker.

Do not connect Hermes to Codex.

Do not create automation.
