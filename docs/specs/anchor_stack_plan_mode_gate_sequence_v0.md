# Anchor Stack Plan Mode Gate Sequence v0

## Status

```yaml
status: gate_sequence_candidate
date: 2026-05-06
baseline_lock: false
automation: false
workflow: false
registry: false
schema: false
scope: external_tool_plan_mode_anchor_operation
```

## Purpose

Define the operating gate sequence that makes the Anchor Stack act during external tool planning.

This is not an automated workflow. It is a human/Codex operating sequence for deciding when to reread anchors and which PVs to transmit.

## Gate 1. Pre-Plan Gate

Use before any plan is drafted.

Required checks:

- What is the user input asking for?
- Which line does the input activate?
- Which past space assets are relevant?
- What hard boundary or watch signal is already visible?
- What Plan Basis must be returned before plan?

Primary PVs:

```text
PV_PLAN_BASIS_GATE
PV_CURRENT_POSITION_ENTRY
PV_NON_INSPECTED_DISCLOSURE
```

Route link:

```text
ROUTE_INPUT_CLASSIFICATION
ROUTE_EXTERNAL_TOOL_PLANNING
```

## Gate 2. Plan Sizing Gate

Use when the tool starts decomposing the work.

Required checks:

- Is a small session split justified by a blocking reason?
- Can execution, self-check, issue log, and return value fit inside one broad-but-bounded package?
- Is user approval needed before implementation or file modification?
- Is the current line clear enough to continue?

Primary PVs:

```text
PV_BROAD_BOUNDED_PACKAGE
PV_PLAN_BASIS_GATE
PV_RETURN_TO_SPACE_CLOSEOUT
```

Route link:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
```

## Gate 3. Runtime Re-Entry Gate

Use during work, not only at the beginning.

Trigger moments:

- before splitting into detailed tasks
- before creating a separate validation/review session
- when deciding hard boundary vs watch item
- before final/ready/complete language
- before asking the user to relay output between tools

Primary PVs:

```text
PV_CURRENT_POSITION_ENTRY
PV_LINE_MATURITY_CAUTION
PV_MANUAL_RELAY_BRIDGE
PV_RAW_TRACE_BOUNDARY
```

Route link:

```text
ROUTE_SESSION_REENTRY
ROUTE_MANUAL_WORKER_RETURN_INTAKE
ROUTE_AUTHORITY_DOWNSHIFT
```

## Gate 4. Closeout / Return-to-Space Gate

Use before ending the work.

Required checks:

- What recoverable material was produced?
- What reusable judgment should remain?
- What issue/watch should be carried forward?
- What should not be promoted?
- Which next route or PV set should a future small anchor use?

Primary PVs:

```text
PV_RETURN_TO_SPACE_CLOSEOUT
PV_RAW_TRACE_BOUNDARY
PV_CURRENT_POSITION_ENTRY
```

Route link:

```text
ROUTE_SESSION_REENTRY
ROUTE_MANUAL_WORKER_RETURN_INTAKE
```

## Minimum Plan-Mode Output Shape

External tools should return:

```text
PLAN_BASIS
bounded plan
package sizing judgment
stop / continue rule
return-to-space requirement
```

The plan may be short. The Plan Basis must exist before the plan.

## Do Not

- Do not treat this sequence as an automated workflow.
- Do not create a runner from this file.
- Do not require all gates to become separate sessions.
- Do not use gate names as taxonomy.
- Do not close without Return-to-Space Value.
