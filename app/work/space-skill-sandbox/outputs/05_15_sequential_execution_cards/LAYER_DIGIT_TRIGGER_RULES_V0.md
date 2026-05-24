# Layer Digit Trigger Rules v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  LAYER_DIGIT_TRIGGER_RULES_PREPARED_WITH_WATCH

Purpose:
  Consolidate the minimum trigger rules that survived iterative search and multi-case stress tests.

Boundary:
  Candidate-only.
  Not baseline, workflow, schema, registry, ontology, automation, eval infrastructure, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Digit skeleton

```text
0<->1:
  observation/frame loop

2:
  evidence quality / plausibility / ground truth

3:
  boundary / trap / auto-fail

4:
  authority / owner / escalation / role split

5:
  smallest safe action

6:
  effectiveness check / follow-up owner

7:
  promotion / memory / standing structure

8/9:
  lens shift / meaning delta
```

## 3. Plain chat vs card

Use plain chat when:

```text
only 0,1,5 are needed
no evidence dispute
no boundary risk
no authority question
no follow-up owner
no promotion pressure
no material layer shift
```

Use a review card when:

```text
2 appears:
  claim needs evidence, source, metric, attachment, policy, ticket, log, or ground truth

3 appears:
  boundary, privacy, legal, payment, HR, account, file, API, credential, publishing, memory, or compliance risk exists

4 appears:
  approval, owner, escalation, decision rights, or role split is unclear

6 appears:
  result cannot be trusted until checked later

8/9 appears:
  the same input means something materially different when read through another layer
```

## 4. Short-circuit rules

### Rule 1 — Promotion Stop

If `7` appears:

```text
stop before action
name the promotion/memory/process-change risk
require explicit approval before any file/system/policy/automation change
```

Examples:

```text
AGENTS.md
SKILL.md
baseline
workflow
schema
registry
ontology
current-position
output_manifest
official policy
automation
```

### Rule 2 — Auto-fail Before Rewrite

If `3 auto-fail` appears:

```text
block unsafe action first
do not merely improve wording
```

Examples:

```text
full card number request
refund promise without authority
legal advice without legal authority
HR decision implication
credential/API/browser/account action
file write without permission
unsupported public claim
closing ticket before verification
```

### Rule 3 — Authority Before Action

If `4` is unclear:

```text
default to approval-needed or escalation-needed
do not treat action pressure as authority
```

Examples:

```text
manager urgency != refund authority
model suggestion != user approval
meeting summary != assigned owner
draft summary != legal sign-off
```

### Rule 4 — No Owner, No Closure

If `6` needs follow-up and no owner exists:

```text
do not close
do not finalize
do not call it resolved
```

Examples:

```text
payment logs not checked
customer confirmation missing
postmortem action owner absent
test result unverified
source support unconfirmed
```

### Rule 5 — Preserve Arrival Layer

If `8/9` appears:

```text
record input layer first
record shifted layer second
record meaning delta third
```

Do not shift every input.
Shift only when the meaning materially changes.

## 5. Minimal output shapes

### Plain chat shape

```text
answer:
next:
```

### Review shape

```text
input/frame:
evidence:
boundary:
authority:
next:
follow-up:
HOLD:
```

### Layer-shift shape

```text
arrival layer:
arrival meaning:
shifted lens:
shifted layer:
meaning delta:
lowest safe action:
HOLD:
```

### Stop shape

```text
stop reason:
digit triggered:
unsafe jump:
needed approval/evidence:
safe lower-layer action:
HOLD:
```

## 6. Domain skins that can reuse this

```text
Customer Response Safety:
  customer reply, refund, billing, complaint, public review

Operational Exception Triage:
  incident, checkout failure, bug cluster, SLA risk, quality defect

External Tool Pre-use:
  Codex, Gemini, CLI, API, browser, account, credential

Claim/Evidence Review:
  blog, sales copy, product page, report, legal memo

Work Artifact Review:
  email, report, instruction, meeting note, decision memo
```

## 7. Current HOLD

```text
do not turn this into workflow
do not turn this into schema
do not turn this into registry
do not turn this into ontology
do not make it AGENTS.md or SKILL.md behavior
do not automate
do not update current-position
do not update output_manifest
```

## 8. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
no official customer-service policy
no refund/SLA/legal/HR/procurement authority
```

`STATUS: LAYER_DIGIT_TRIGGER_RULES_PREPARED_WITH_WATCH`
