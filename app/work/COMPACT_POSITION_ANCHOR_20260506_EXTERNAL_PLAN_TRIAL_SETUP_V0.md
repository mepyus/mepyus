# COMPACT_POSITION_ANCHOR_20260506_EXTERNAL_PLAN_TRIAL_SETUP_V0

## Status

```yaml
status: active_compact_position_anchor
date: 2026-05-06
baseline_lock: false
automation: false
purpose: setup_external_tool_planning_trial_set_a
```

## Current Purpose

Prepare the first real plan-mode trial packet for an external tool.

The trial should test whether the tool returns `PLAN_BASIS -> bounded plan` instead of model-default session splitting.

## Position IDs

- `PV_PLAN_BASIS_GATE`
- `PV_BROAD_BOUNDED_PACKAGE`
- `PV_NON_INSPECTED_DISCLOSURE`
- `PV_RETURN_TO_SPACE_CLOSEOUT`

## What These Positions Mean Now

- `PV_PLAN_BASIS_GATE`: the worker must return Plan Basis before plan.
- `PV_BROAD_BOUNDED_PACKAGE`: default to one bounded package unless a blocking split reason exists.
- `PV_NON_INSPECTED_DISCLOSURE`: worker must state read scope and non-inspected scope.
- `PV_RETURN_TO_SPACE_CLOSEOUT`: worker output must leave reusable judgment and future reuse note.

## Required Gate

- Use `ROUTE_EXTERNAL_TOOL_PLANNING`.
- Pass Pre-Plan Gate and Plan Sizing Gate.
- Worker must not create files, automation, registry, schema, baseline, or authority claims.

## Watch Signals

- `session_convergence_watch`
- `evidence_overclaim_watch`
- `done_without_memory_watch`
- `worker_authority_drift`

## Do Not Infer

- no implementation permission
- no final route validation
- no full-space coverage
- no automatic runner

## Return Shape

- external planning trial packet
- worker return review template
- Movement Record update
