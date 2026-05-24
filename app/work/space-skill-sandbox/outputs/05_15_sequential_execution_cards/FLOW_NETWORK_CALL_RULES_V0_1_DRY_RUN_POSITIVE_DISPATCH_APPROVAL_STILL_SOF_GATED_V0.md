# Flow-Network Call Rules v0.1 Dry Run - Positive Dispatch Approval Still SOF-Gated v0

## 1. Verdict

```text
FLOW_NETWORK_CALL_RULES_V0_1_POSITIVE_DISPATCH_APPROVAL_STILL_REQUIRES_SOF_CLEARANCE
```

## 2. Purpose

This dry-run tests the positive side of the post-packet dispatch boundary:

```text
If a named packet and explicit dispatch approval are present,
does Hermes execution become automatically allowed?
```

Answer:

```text
No.
Explicit dispatch approval is necessary but not sufficient.
SOF must still clear action, persistence, side effect, and recovery boundaries.
```

## 3. Hypothetical Input

```text
packet:
  app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_FLOW_NETWORK_CALL_RULES_BOUNDARY_SANITY_PACKET_V0.md

EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

Important:

```text
This is a dry-run only.
The user has not provided this exact packet-bound approval in the current turn.
No Hermes dispatch is authorized by this document.
```

## 4. Applied Rule

```text
VECTORFL_FLOW_NETWORK_CALL_RULES_V0_1.md
```

Applied sequence:

```text
IIC -> SOF -> MOL -> Packet -> Dispatch Approval -> Lane -> RML -> Recovery -> Promotion Gate
```

## 5. IIC Mode Selection

Selected mode:

```text
full review
```

Why:

```text
The request would involve Hermes execution.
Even with explicit dispatch approval, the system must inspect the packet's scope, allowed actions, forbidden actions, output contract, persistence boundary, and STOP conditions.
```

## 6. SOF Permission Check

Dispatch approval status in hypothetical input:

```text
present
```

SOF result:

```text
conditional_clearance_only
```

Meaning:

```text
The request can proceed toward Hermes lane only if the packet itself is bounded and does not authorize prohibited action.
```

SOF must verify:

```text
1. action permission:
   what Hermes may actually do

2. external side effect permission:
   whether any Slack/email/browser/MCP/deploy/send action exists

3. persistence permission:
   what files/state Hermes may create or modify

4. recovery permission:
   what VectorFL can receive from the result

5. promotion boundary:
   whether the packet tries to create workflow/skill/baseline/ontology/current-position/output_manifest
```

If any of these fail:

```text
STOP
```

## 7. Packet Builder Check

The named packet must be checked for:

```text
purpose
input scope
allowed actions
forbidden actions
persistence boundary
expected report
expected receipt
recovery classification
HOLD
STOP
```

Packet presence does not equal packet validity.

Packet validity does not equal promotion approval.

## 8. Post-Packet Dispatch Approval Check

Required line:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
```

If present and packet-bound:

```text
dispatch gate may open
```

If absent, ambiguous, stale, or bound to a different packet:

```text
do not dispatch
```

## 9. MOL Lane Selection

Candidate lane:

```text
Hermes lane
```

Selected lane in this dry-run:

```text
none
```

Reason:

```text
This document is not an execution approval.
It only verifies that positive approval would still remain SOF-gated.
```

## 10. Recovery Classification

```text
receipt:
  v0.1 positive dispatch boundary was dry-run without executing Hermes.

residue:
  dispatch approval is necessary but not sufficient.
  packet-bound approval must not bypass SOF.

candidate:
  call rules v0.1 become more robust by distinguishing:
    packet validity
    dispatch approval
    SOF clearance
    promotion approval

component:
  no.

space_update_proposal:
  no.

STOP:
  actual Hermes dispatch without a current user-provided packet-bound approval and SOF clearance.
```

## 11. Boundary Equations

```text
packet exists != packet valid
packet valid != dispatch approval
dispatch approval != SOF clearance
SOF clearance != VectorFL promotion approval
Hermes success != VectorFL approval
```

## 12. WATCH

```text
1. Positive approval line being reused after packet contents change.
2. Approval bound to one packet being applied to another packet.
3. Dispatch approval bypassing SOF.
4. SOF clearance being mistaken for promotion approval.
5. Hermes run success being treated as component readiness.
```

## 13. HOLD

```text
no Hermes dispatch
no Gemini dispatch
no automation
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

## 14. Recovered Judgment

The new gate should not be interpreted as:

```text
approval line -> run
```

It should be interpreted as:

```text
valid packet + explicit packet-bound dispatch approval + SOF clearance -> eligible for Hermes lane
```

Even after a successful Hermes run:

```text
report/receipt returns first.
Codex recovery classification follows.
Promotion remains separate.
```

