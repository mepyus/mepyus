# Position Value Application Trial Packet v0

## Status

```yaml
status: trial_packet_candidate
date: 2026-05-06
baseline_lock: false
automation: false
purpose: test_position_ids_inside_small_anchor
```

## Purpose

Test whether Position IDs can make a small anchor useful without replaying the whole Anchor Stack.

This is a trial packet, not a workflow.

## Trial Input Shape

Use a realistic external-tool planning request:

```text
Ask an external tool to draft a bounded package plan.
```

## Required Compact Anchor

Use:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_RETURN_TO_SPACE_CLOSEOUT
```

Optional if bounded reading is involved:

```text
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
```

## Expected Worker Behavior

The worker should:

- return Plan Basis before plan
- avoid analysis/design/execution/verification/review split unless blocking reason exists
- include internal evidence check and issue/watch log inside the bounded package
- return Movement Record / Return-to-Space Value

## Gate Check

Review the output with:

- `docs/specs/anchor_stack_gate_checklist_v0.md`

Pass only if:

- position IDs changed plan shape
- package sizing was justified
- hard boundary / watch / continue were separated
- closeout returned reusable judgment

## Stop Conditions

Stop if:

- position IDs are treated as law
- worker asks for broad scan
- plan omits Plan Basis
- plan omits Return-to-Space Value
- worker claims readiness or baseline

## Return-to-Space

Record:

- which position IDs were used
- whether they changed the plan
- which watch signals traveled
- what was still missing

