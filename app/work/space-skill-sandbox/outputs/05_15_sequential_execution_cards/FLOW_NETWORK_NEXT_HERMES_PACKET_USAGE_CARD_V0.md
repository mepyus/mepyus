# Flow-Network Next Hermes Packet Usage Card v0

## 1. Verdict

```text
FLOW_NETWORK_NEXT_HERMES_PACKET_USAGE_CARD_CREATED_WITH_DISPATCH_HOLD
```

## 2. Status

```text
status: usage_card_candidate
scope: next Hermes packet pre-dispatch review
authority: sandbox-local candidate
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

This card does not authorize Hermes execution.

This card does not promote packet output.

## 3. Use When

Use this when a future Hermes packet appears and the user asks:

```text
이거 Hermes에 넘겨?
이 packet 실행해?
이거 돌려도 돼?
이걸로 Hermes dispatch 해?
```

Do not dispatch first.

Review first.

## 4. Required Input

Minimum input for a dispatch request:

```text
packet:
  [exact packet path]

EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

If the approval line is missing:

```text
PACKET_VALID_BUT_NO_DISPATCH_APPROVAL
```

## 5. Pre-Dispatch Review

Fill this before any Hermes dispatch:

```text
target packet:
  [exact path]

packet identity:
  exact / ambiguous / changed

packet validity:
  valid / invalid_needs_patch / unclear_needs_review

dispatch approval:
  yes / no / ambiguous / stale / bound_to_different_packet

SOF risk family:
  technical/local execution
  semantic/customer/business
  automation/persistence
  research/web/source
  external app / live connector
  mixed

SOF clearance:
  clearable / conditional_clearance / HOLD / STOP

recovery expectation:
  receipt / residue / candidate / component_candidate_only / STOP

promotion boundary:
  no promotion unless separately approved
```

## 6. Risk Family Quick Lens

```text
technical/local execution:
  script, file write, git, network, package, persistence boundary

semantic/customer/business:
  liability, refund, SLA, account status, company-position boundary

automation/persistence:
  manual dry-run vs real cron, recurring automation, Hermes memory/skill/config

research/web/source:
  source authority, live browsing, output flood, tool capability permission

external app / live connector:
  connector permission, external side effect approval, message/send/write/deploy
```

## 7. Verdict Options

Use one:

```text
PACKET_VALID_BUT_NO_DISPATCH_APPROVAL
PACKET_INVALID_NEEDS_PATCH
PACKET_VALID_AND_DISPATCH_APPROVAL_PRESENT_BUT_SOF_HOLD
PACKET_VALID_AND_SOF_CLEAR_BUT_EXECUTION_NOT_REQUESTED
PACKET_DISPATCH_ELIGIBLE_AFTER_FINAL_USER_CONFIRMATION
PACKET_STOP_TRIGGERED
```

No verdict here means executed.

No verdict here means promoted.

## 8. Dispatch Eligibility

A packet is only dispatch-eligible when all are true:

```text
1. exact packet path is named
2. packet identity/version is unambiguous
3. packet validity review passes
4. EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes is present and packet-bound
5. SOF clearance holds for the packet's risk family
6. no new external side effect is attached
7. no new persistence expansion is attached
8. no promotion/authority mutation is attached
```

Even then:

```text
dispatch-eligible != executed
execution success != VectorFL approval
```

## 9. Never Promote From This Card

```text
packet validity -> dispatch approval
dispatch approval -> SOF clearance
SOF clearance -> VectorFL promotion
Hermes success -> VectorFL approval
receipt/report -> baseline
Hermes memory -> VectorFL memory
Hermes skill -> VectorFL SKILL.md
Hermes cron -> VectorFL workflow
connector ladder -> connector-use permission
```

## 10. HOLD

```text
no Hermes dispatch from this card alone
no Gemini dispatch from this card alone
no packet execution
no script run
no customer draft generation
no message sent
no web browsing
no source lookup
no network / browser / MCP
no live connector use
no email/CRM/database/Slack/Telegram/Obsidian connection
no cron created
no recurring automation
no gateway install
no Hermes memory / skill / cron / config edit
no implementation created
no component promotion
no workflow creation
no skill creation
no baseline promotion
no schema/registry/ontology creation
no current-position update
no output_manifest update
no AGENTS.md update
no SKILL.md creation
no VectorFL authority mutation
```

## 11. Hard Stop Confirmation

```text
No Hermes execution performed.
No Gemini execution performed.
No packet executed.
No script run performed.
No customer draft generated.
No web browsing performed.
No source lookup performed.
No live connector used.
No message sent.
No cron created.
No recurring automation created.
No gateway installed.
No Hermes memory/skill/config edited.
No implementation created.
No component promotion performed.
No workflow/schema/registry/ontology/baseline/automation created.
No AGENTS.md / SKILL.md / current-position / output_manifest update.
No VectorFL authority mutation.
```

