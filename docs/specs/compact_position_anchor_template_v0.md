# Compact Position Anchor Template v0

## Status

```yaml
status: template_candidate
date: 2026-05-06
baseline_lock: false
automation: false
```

## Purpose

This is the small-anchor form that uses Position Value IDs.

Use it when a full Session Space Anchor would be too heavy.

```markdown
# COMPACT_POSITION_ANCHOR

## Current Purpose

[one to two sentences]

## Position IDs

- [PV_*]
- [PV_*]
- [PV_*]

## What These Positions Mean Now

- [PV_*]: [one sentence current meaning]
- [PV_*]: [one sentence current meaning]

## Required Gate

- [Plan Basis / package sizing / return-to-space / evidence disclosure / user decision]

## Watch Signals

- [watch_signal]
- [watch_signal]

## Do Not Infer

- [no baseline / no automation / no workflow / no tool authority]

## Return Shape

- [Movement Record / worker return packaging / user-facing card / issue log]
```

## Example

```markdown
# COMPACT_POSITION_ANCHOR

## Current Purpose

Ask an external tool to draft the next package plan without falling into model-default session splitting.

## Position IDs

- PV_PLAN_BASIS_GATE
- PV_BROAD_BOUNDED_PACKAGE
- PV_RETURN_TO_SPACE_CLOSEOUT

## What These Positions Mean Now

- PV_PLAN_BASIS_GATE: the worker must return Plan Basis before plan.
- PV_BROAD_BOUNDED_PACKAGE: do not split into many sessions unless a blocking reason exists.
- PV_RETURN_TO_SPACE_CLOSEOUT: closeout must leave reusable judgment.

## Required Gate

- Plan Basis first
- package sizing reason
- Return-to-Space Value

## Watch Signals

- session_convergence_watch
- done_without_memory_watch

## Do Not Infer

- no baseline
- no automation
- no universal workflow

## Return Shape

- Plan Basis
- bounded plan
- issue/watch
- future reuse note
```

