# Flow-Network Call Rules Dry Run - Hermes Surface Request v0

## 1. Verdict

```text
FLOW_NETWORK_CALL_RULES_DRY_RUN_HERMES_SURFACE_REQUEST_REQUIRES_PACKET_WITH_HOLD
```

## 2. Test Input

```text
헤르메스에게 이거 시켜봐
```

## 3. Surface Reading

Surface meaning:

```text
Ask Hermes to do a task.
```

Missing payload:

```text
"이거" is unspecified.
```

Immediate judgment:

```text
Hermes lane pressure is present,
but task payload, action permission, side effects, and persistence are unknown.
```

## 4. IIC Mode Selection

Selected mode:

```text
layer-shift + full review pending payload
```

Why:

```text
The surface request is not just conversation.
It asks to route work to an external execution harness.
Because the task payload is unspecified, the request cannot safely proceed to Hermes execution.
```

Mode if payload is harmless local read-only:

```text
light review or full review
```

Mode if payload includes external side effect / mutation / automation:

```text
full review or STOP
```

## 5. SOF Permission Check

Current SOF outcome:

```text
full_review_required
```

Reason:

```text
The request invokes Hermes, but action type is unknown.
Hermes can perform terminal, file, browser, MCP, memory, skill, cron, messaging, and external-app actions.
Therefore permission cannot be inferred from the phrase alone.
```

Questions SOF must answer before execution:

```text
What exactly should Hermes do?
Read or write?
Local or external?
One-shot or recurring?
Any external side effect?
Any persistence inside Hermes?
Any VectorFL recovery/promotion claim?
Any credentials, browser, MCP, memory, skill, cron, config?
```

STOP if payload includes unauthorized:

```text
memory write
skill creation/edit
cron creation/edit
config edit
external send/post/deploy/write
source patch without approval
VectorFL authority update
baseline/workflow/schema/registry/ontology promotion
AGENTS.md / SKILL.md update
current-position / output_manifest update
```

## 6. MOL Lane Selection

Candidate lane:

```text
Hermes lane
```

But:

```text
MOL cannot select execution until SOF clears the action.
```

Current route:

```text
Do not execute Hermes.
Draft or request a packet after payload is specified.
```

## 7. Packet Builder Requirement

Packet required:

```text
yes
```

Minimum packet must include:

```text
purpose
exact input/payload
allowed actions
forbidden actions
external side-effect rule
persistence boundary
output directory or return target
expected report
expected receipt
recovery suggestion
WATCH
HOLD
hard stop confirmation
```

Packet is not execution approval.

Packet enables:

```text
bounded Hermes execution if SOF allows
```

## 8. Execution / Review Lane

Action performed in this dry-run:

```text
No Hermes execution.
No packet dispatch.
Only route classification.
```

Why:

```text
Payload is missing.
Permission is unknown.
Packet does not exist.
```

## 9. RML Recovery

Recovered trace:

```text
Hermes surface request requires SOF and Packet Builder before execution.
```

Evidence:

```text
VECTORFL_FLOW_NETWORK_CALL_RULES_V0.md
VECTORFL_FLOW_NETWORK_ATTACHMENT_MODEL_V0.md
this dry-run report
```

## 10. Recovery Gate

Recovery classification:

```text
receipt:
  dry-run route classification was performed.

residue:
  Hermes invocation phrases create execution pressure even when payload is vague.

candidate:
  call rules correctly require Packet Builder before Hermes execution.

component:
  no.

space_update_proposal:
  no.

STOP:
  not triggered by phrase alone,
  but would trigger if payload includes unauthorized mutation/side effect/promotion.
```

## 11. WATCH

```text
1. "헤르메스에게 시켜" can hide side effects.
2. Hermes capability must not become permission.
3. Packet draft must not become dispatch approval.
4. Vague payload must not be executed.
5. Successful Hermes execution would still be receipt, not VectorFL approval.
```

## 12. HOLD

```text
no Hermes execution from vague payload
no component promotion
no workflow creation
no skill creation
no baseline promotion
no schema/registry/ontology creation
no current-position update
no output_manifest update
no AGENTS.md update
no SKILL.md creation
no automation
no VectorFL authority mutation
```

## 13. Next Smallest Action

If the user provides a concrete Hermes task, classify it before execution:

```text
Input:
  [exact Hermes task]

Mode:
  plain/simple/light/full/layer-shift/stop

SOF:
  action permission
  external side effect permission
  persistence permission
  VectorFL recovery permission

MOL:
  Hermes lane or other lane

Packet:
  required fields

Recovery:
  expected receipt/residue/candidate/STOP
```
