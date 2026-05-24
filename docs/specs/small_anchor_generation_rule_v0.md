# Small Anchor Generation Rule v0

## Status

```yaml
status: rule_candidate
date: 2026-05-06
baseline_lock: false
automation: false
```

## Purpose

Define how to generate a small anchor from position values.

This rule is for human/Codex use. It is not automation.

## Rule

A small anchor should include:

1. current purpose
2. 2-4 position IDs
3. one sentence per position ID
4. required gate
5. watch signals
6. do-not-infer
7. return shape

## Selection Order

Select position IDs in this order:

1. What must happen before planning?
2. What changes package size?
3. What prevents overclaim?
4. What ensures Return-to-Space?
5. What prevents user relay or raw trace promotion?

## Common Sets

### External Tool Planning

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
```

### Bounded Gemini Reread

```text
PV_BOUNDED_REREAD_UNIT
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
```

### Manual Relay / Worker Return Packaging

```text
PV_MANUAL_RELAY_BRIDGE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
```

### Session Recovery

```text
PV_CURRENT_POSITION_ENTRY
PV_RETURN_TO_SPACE_CLOSEOUT
PV_RAW_TRACE_BOUNDARY
```

## Quality Check

The small anchor fails if:

- it includes more than 4 position IDs without reason
- it has no watch signals
- it has no do-not-infer line
- it does not change task behavior
- it repeats broad philosophy instead of position values

