# Layer Digit Mode Thresholds v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  LAYER_DIGIT_MODE_THRESHOLDS_PREPARED_WITH_WATCH

Purpose:
  Define the minimum mode thresholds that survived negative-control and borderline tests.

Boundary:
  Candidate-only threshold note.
  Not baseline, workflow, schema, registry, ontology, automation, eval infrastructure, AGENTS.md, SKILL.md, current-position, or output_manifest.

## 2. Mode Ladder

```text
0. plain chat
1. simple answer
2. light review
3. full review
4. layer-shift
5. stop
```

This is not a workflow.
It is a mode selector.

## 3. Plain Chat

Use when:

```text
0,1,5 only
no meaningful evidence dispute
no boundary
no authority
no follow-up owner
no promotion pressure
no material layer shift
```

Example:

```text
polite reply
simple wording improvement
neutral title brainstorm
```

Output:

```text
answer:
next: optional
```

## 4. Simple Answer

Use when:

```text
0,1,5 plus trivial 2
```

Trivial 2 means:

```text
path citation
known local file
simple status confirmation
non-disputed factual lookup
```

Example:

```text
Which file contains the current asset map?
```

Output:

```text
answer:
evidence/path: optional
```

## 5. Light Review

Use when:

```text
small 2/3/6 appears
but no authority jump
no auto-fail
no promotion pressure
no full card needed
```

Example:

```text
refund mentioned, but no refund promise requested
support is investigating, but no closure claimed
```

Output:

```text
safe answer:
watch:
hold: optional
```

## 6. Full Review

Use when:

```text
material evidence is missing
boundary risk is real
authority is unclear
follow-up owner matters
customer/legal/HR/finance/account/API/file/memory/publishing risk exists
```

Output:

```text
input/frame:
evidence:
boundary:
authority:
next:
follow-up:
HOLD:
```

## 7. Layer-shift

Use when:

```text
8/9 changes meaning materially
```

Examples:

```text
discussion -> assignment
title -> authority claim
lookup -> modification request
friendly message -> implied commitment
customer complaint -> operational incident signal
```

Output:

```text
arrival layer:
arrival meaning:
shifted lens:
shifted layer:
meaning delta:
lowest safe action:
HOLD:
```

## 8. Stop

Use when:

```text
7_action appears
3 auto-fail appears
action requested without authority
promotion/memory/current-surface pressure appears
```

Examples:

```text
update AGENTS.md
create SKILL.md
update current asset map
promise refund without authority
ask for full card number
close ticket before verification
publish official status claim
```

Output:

```text
stop reason:
digit triggered:
unsafe jump:
needed approval/evidence:
safe lower-layer action:
HOLD:
```

Important distinction:

```text
7_action:
  user/model/request asks to change, promote, install, update, automate, write, dispatch, or place near authority surface
  mode = stop

7_topic:
  user asks whether promotion could be considered later, what conditions would be needed, or why something is not ready
  mode = full review

7_absent:
  use normal mode selection
```

## 9. Key Corrections

```text
keywords alone do not determine mode
same object can have different mode by action
light review exists between plain chat and full review
stop is for authority/promotion/auto-fail, not every risk
7_action stops; 7_topic reviews
layer-shift requires material meaning change
```

## 10. Hard stop confirmation

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
no local core/derived/surface authority change
```

`STATUS: LAYER_DIGIT_MODE_THRESHOLDS_PREPARED_WITH_WATCH`
