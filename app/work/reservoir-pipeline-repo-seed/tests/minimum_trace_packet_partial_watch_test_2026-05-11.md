# Minimum Trace Packet Partial WATCH Test - 2026-05-11

## Status

```text
Status = structure power stress test
Input = partial non-empty external worker return recovery
Target = run_257_worker_return_shape_partial_nonempty_application_recovery
Not automation
Not schema
Not promotion
```

## Question

```text
Can the structure preserve a middle state where material is useful enough to watch, but too thin to promote?
```

## Test Object

```text
Run:
  app/work/space-skill-sandbox/runs/run_257_worker_return_shape_partial_nonempty_application_recovery.md

Packaging:
  app/work/space-skill-sandbox/outputs/gemini_partial_nonempty_worker_return_shape_application_packaging_v0.md

Movement record:
  app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_partial_nonempty_application_recovery_v0.md
```

## Packet Applied

```text
purpose
source_refs
thin_plan
what_was_read
what_was_not_read
output_created
feedback_or_mismatch
recovered_judgment
watch
next_condition
return_placement
```

Packet record:

```text
app/work/reservoir-pipeline-repo-seed/records/run_257_minimum_trace_packet.md
```

## Result

```text
PARTIAL_RETURN_WATCH_RECOVERY_PROVEN
```

Reason:

The packet preserved:

```text
usable candidate material
thin grounding trace
missing not_inspected_scope
downshift requirement
WATCH placement
no promotion
no extra micro-runs
```

## Structure Power Judgment

Previous state:

```text
MESSY_EMPTY_RETURN_BOUNDARY_RECOVERY_PROVEN
```

Current state:

```text
THREE_MODE_RETURN_RECOVERY_PROVEN_AS_CANDIDATE_STRUCTURE
```

This matters because:

```text
The structure can now hold three different return states without collapsing them:
  success-like recovery with watch
  empty or weak return HOLD
  partial non-empty return WATCH
```

## What This Adds

```text
The repo seed is gaining a reusable judgment surface:
  extract when evidence supports it
  hold when value is absent
  watch when value exists but trace is thin
```

This is stronger than organization because it preserves different action consequences.

## What Is Still Not Proven

```text
multi-agent disagreement
automatic packet drafting
long-chain compounding across unrelated pipelines
actual user promotion decision
```

## Important Correction

```text
WATCH is not a weaker PASS.
WATCH is a placement that keeps material alive while blocking promotion.
```

## Next Test

```text
Use this three-state packet path as the return-reading layer for the next external worker or sandbox result.
```

`STATUS: MINIMUM_TRACE_PACKET_PARTIAL_WATCH_TEST_PREPARED`
