# COMPACT_POSITION_ANCHOR_20260506_ROUTE_INPUT_EVIDENCE_BUILDOUT_V0

## Status

```yaml
status: active_compact_position_anchor
date: 2026-05-06
baseline_lock: false
automation: false
purpose: ground_route_seed_in_input_materials
```

## Current Purpose

Use the May 6 input materials and current space records to ground the anchor route seed with evidence.

This pass should make route/PV selection more operational without claiming a completed map.

## Position IDs

- `PV_PLAN_BASIS_GATE`
- `PV_BOUNDED_REREAD_UNIT`
- `PV_LINE_MATURITY_CAUTION`
- `PV_RETURN_TO_SPACE_CLOSEOUT`

## What These Positions Mean Now

- `PV_PLAN_BASIS_GATE`: evidence buildout must state its LACL basis before adding route rows.
- `PV_BOUNDED_REREAD_UNIT`: the nine documents are sampled for route evidence, not converted into a whole-space inventory.
- `PV_LINE_MATURITY_CAUTION`: route evidence can mature a candidate, but cannot promote a registry or ontology.
- `PV_RETURN_TO_SPACE_CLOSEOUT`: the buildout must leave reusable route evidence and next Gemini validation targets.

## Required Gate

- Use canonical PV IDs.
- Preserve file/line evidence pointers.
- Mark candidate vs keep vs hold.

## Watch Signals

- `evidence_overclaim_watch`
- `axis_ontology_watch`
- `route_sprawl_watch`
- `done_without_memory_watch`

## Do Not Infer

- no completed map
- no baseline
- no registry
- no schema
- no automation
- no full-space coverage claim

## Return Shape

- Plan Basis
- route input evidence matrix
- plan-mode gate sequence candidate
- route seed update
- Movement Record update
