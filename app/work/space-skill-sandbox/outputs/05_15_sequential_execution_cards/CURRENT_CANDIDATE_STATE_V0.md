# Current Candidate State v0
# 05-15 Mode-selection Probe

## 1. Status

Status:
  CURRENT_CANDIDATE_STATE_PREPARED_WITH_WATCH

Purpose:
  Compress the current 05-15 candidate state after adapter, layer, local-asset, negative-control, threshold, and middle-layer dry-runs.

Boundary:
  This is a sandbox-local candidate state note.
  It is not current-position, output_manifest, baseline, workflow, schema, registry, ontology, automation, AGENTS.md, or SKILL.md.

## 2. Current Name

Best current label:

```text
05-15 mode-selection probe
```

Avoid stronger labels:

```text
middle layer
operating system
adapter framework
local asset extension
official guidance
workflow
```

## 3. Current Verdict

```text
promising:
  yes

validated:
  no

promotable:
  no

local integration ready:
  no

usable in chat/sandbox:
  yes
```

## 4. What It Does

It helps decide the minimum response mode for an input:

```text
plain chat
simple answer
light review
full review
layer-shift
stop
```

It should prevent:

```text
raw input -> reusable action
candidate -> baseline
summary -> evidence
packet draft -> dispatch
reading guide -> memory
topic discussion -> approval
```

## 5. Current Mode Rule

```text
plain chat:
  only 0,1,5

simple answer:
  0,1,5 + trivial 2

light review:
  small 2/3/6, no authority jump, no auto-fail, no promotion action

full review:
  material 2/3/4/6 with real risk, missing evidence, unclear authority, follow-up owner, or 7_topic

layer-shift:
  8/9 materially changes meaning without requiring stop

stop:
  7_action, 3 auto-fail, or action requested without authority
```

## 6. Most Important Distinctions

```text
7_action:
  stop

7_topic:
  full review

keyword:
  not enough to determine mode

same object:
  can change mode by requested action

layer-shift:
  not a decoration; use only when meaning changes materially

light review:
  prevents jumping from plain chat to full review too early
```

## 7. Strongest Evidence So Far

```text
negative-control:
  simple inputs stayed plain/simple

borderline threshold:
  refund keyword alone did not trigger full card

mixed batch:
  mode selection worked across varied synthetic cases

local authority asset:
  current_asset_map lookup stayed simple; update request stopped

local layer-shift:
  domain-specific name -> reusable reading attitude was detected without stop

raw-to-action:
  raw payment complaints -> support macro was stopped
```

## 8. Weakest Points

```text
tests are still hand-authored
real user messy material is limited
layer-shift can over-interpret
light review / full review boundary needs more real examples
candidate pile can mimic registry
mode thresholds can mimic policy
```

## 9. Use From Now On

For future inputs, do not create a new theory first.

Use:

```text
mode:
why:
minimal answer/action:
WATCH:
HOLD:
```

Expand only when the selected mode requires it.

## 10. Stop Conditions

Stop immediately if the input asks for:

```text
AGENTS.md update
SKILL.md creation/update
current-position update
output_manifest update
baseline promotion
workflow/schema/registry/ontology creation
automation
external dispatch
platform/API/browser/account/credential action
local core/derived/surface authority change
support macro / policy-like reusable customer wording without approval
```

## 11. Next Best Test

Next useful test:

```text
real user-provided messy material
```

Not another conceptual note.

Target output:

```text
mode:
why:
minimal answer/action:
WATCH:
HOLD:
```

## 12. Hard Stop Confirmation

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

`STATUS: CURRENT_CANDIDATE_STATE_PREPARED_WITH_WATCH`
