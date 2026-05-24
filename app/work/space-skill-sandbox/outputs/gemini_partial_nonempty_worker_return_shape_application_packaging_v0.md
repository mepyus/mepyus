# Gemini Partial Non-Empty Worker Return Shape Application Packaging v0

## Status

```yaml
status: gemini_return_packaging
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
source_return: user_pasted_gemini_result
verdict: PASS_WITH_WATCH_AS_PARTIAL_RETURN_RECOVERY_MATERIAL
```

## Source

Gemini applied the candidate worker-return shape to:

```text
app/work/space-skill-sandbox/relay/outbox/plan_from_space_compact_crosscheck_20260506_v0_gemini_outbox_20260506_190215.md
```

Codex checked file presence only in this recovery pass:

```text
target_result: present
raw_result_pointer: present
```

## Accepted Values

Accepted as candidate material:

```text
Partial non-empty returns can be recoverable with WATCH when they contain useful candidate Return-to-Space material.
The weakest fields in partial returns are often how_anchors_changed_behavior and not_inspected_scope.
Thin anchor references should not become HOLD by default when usable content and candidate return value are present.
The 10-field shape can classify the gaps without creating micro-runs.
```

## Downshift Corrections

Gemini wording:

```text
Validation Signal / confirms sufficiency
```

Downshift:

```text
candidate signal / suggests usefulness for that target
```

Gemini wording:

```text
clear technical judgment that aligns with space principles
```

Downshift:

```text
usable candidate judgment with thin grounding trace
```

Gemini wording:

```text
recover into space memory
```

Downshift:

```text
recover as candidate material after Codex downshift and gap disclosure
```

## WATCH Classification

```yaml
classification: WATCH
watch_reason:
  - result body exists
  - candidate Return-to-Space value exists
  - anchor mentions are thin but present
  - not_inspected_scope is missing and must be disclosed by recovery
  - over-strong confirmations can be downshifted
not_hold_reason:
  - no unavoidable authority claim
  - no schema/automation/baseline implementation demand
  - not empty
  - usable candidate material exists
```

## Raw Trace Boundary

Remain raw trace:

```text
worker Q&A prose
tool invocation metadata
model "Yes" confirmations
unstated source coverage
raw result body until Codex recovery
```

## Candidate Setting Update

The worker-return candidate setting now has three observed application modes:

```text
success_case:
  fields present -> recover candidate material with watch.

empty_failure_case:
  empty result / missing anchors_used / missing Return-to-Space -> HOLD.

partial_nonempty_case:
  useful content + thin trace + candidate Return-to-Space -> WATCH with downshift and gap disclosure.
```

This remains candidate operating-setting material only.

## Return-to-Space Value

Recoverable material:

```text
The worker-return shape can classify partial non-empty returns as WATCH when useful candidate material exists but grounding trace is thin.
```

Reusable judgment:

```text
Do not force HOLD just because anchor usage is thin. HOLD is for missing recoverable value, hidden critical gaps, authority/schema/baseline claims, or empty returns.
```

Operational correction:

```text
Codex should downshift over-strong confirmations and explicitly add missing not-inspected scope during recovery.
```

Future reuse note:

```text
Use success / empty-HOLD / partial-WATCH as the package-level intake modes for future external worker returns.
```

## Do Not

```text
do not promote to baseline
do not update current position
do not create schema/parser/automation
do not treat thin returns as memory without recovery
do not create micro-runs to fill every missing field
```

`STATUS: GEMINI_PARTIAL_NONEMPTY_WORKER_RETURN_SHAPE_APPLICATION_PACKAGED_WITH_WATCH`
