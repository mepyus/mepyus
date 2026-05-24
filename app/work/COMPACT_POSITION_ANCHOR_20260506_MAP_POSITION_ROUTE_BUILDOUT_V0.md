# COMPACT_POSITION_ANCHOR_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0

## Status

```yaml
status: active_compact_position_anchor
date: 2026-05-06
baseline_lock: false
automation: false
purpose: build_anchor_map_position_routes
```

## Current Purpose

Build the first route seed for "where to draw our map" so future small anchors can carry effective position values without replaying the whole Anchor Stack.

Also create a Gemini packet that asks for deeper evidence on map-position routes, not another broad space summary.

## Position IDs

- `PV_PLAN_BASIS_GATE`
- `PV_BROAD_BOUNDED_PACKAGE`
- `PV_LINE_MATURITY_CAUTION`
- `PV_RETURN_TO_SPACE_CLOSEOUT`

## What These Positions Mean Now

- `PV_PLAN_BASIS_GATE`: this buildout must state why route mapping is the next setup move.
- `PV_BROAD_BOUNDED_PACKAGE`: keep route seed, Gemini packet, and movement update in one bounded package.
- `PV_LINE_MATURITY_CAUTION`: map routes must not become line registry, ontology, or baseline.
- `PV_RETURN_TO_SPACE_CLOSEOUT`: leave reusable route rows and a next Gemini read target.

## Required Gate

- Plan Basis before route seed.
- Canonical PV IDs only in route rows.
- Gemini output must be packaged before any map update.

## Watch Signals

- `axis_ontology_watch`
- `session_convergence_watch`
- `raw_trace_promotion_watch`
- `done_without_memory_watch`

## Do Not Infer

- no baseline
- no ontology
- no registry
- no schema
- no automation
- no completed map

## Return Shape

- Plan Basis
- anchor map position route seed
- Gemini map-position discovery packet
- Movement Record update
