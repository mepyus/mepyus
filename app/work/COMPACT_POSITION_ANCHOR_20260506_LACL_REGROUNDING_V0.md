# COMPACT_POSITION_ANCHOR_20260506_LACL_REGROUNDING_V0

## Status

```yaml
status: active_compact_position_anchor
date: 2026-05-06
baseline_lock: false
automation: false
purpose: apply_position_anchor_to_current_setup_turn
```

## Current Purpose

Use the Anchor Stack during this setup turn, not only document it.

Create a Gemini instruction packet for deep/wide exploration data needed to re-ground line / axis / camera / lens for future small anchors.

## Position IDs

- `PV_PLAN_BASIS_GATE`
- `PV_BOUNDED_REREAD_UNIT`
- `PV_NON_INSPECTED_DISCLOSURE`
- `PV_RETURN_TO_SPACE_CLOSEOUT`

## What These Positions Mean Now

- `PV_PLAN_BASIS_GATE`: Codex must state the basis for this setup before adding more files.
- `PV_BOUNDED_REREAD_UNIT`: Gemini should read deeply, but through a packeted purpose and retrieval boundary, not as a generic whole-space summary.
- `PV_NON_INSPECTED_DISCLOSURE`: Codex and Gemini must say what was not inspected or only weakly inferred.
- `PV_RETURN_TO_SPACE_CLOSEOUT`: this turn must leave reusable setup artifacts and a movement record update.

## Required Gate

- Plan Basis first.
- Gemini packet must ask for evidence-backed line / axis / camera / lens re-grounding data.
- No baseline, ontology, schema, registry, workflow, runner, or automation.

## Watch Signals

- `broad_scan_watch`
- `evidence_overclaim_watch`
- `axis_ontology_watch`
- `done_without_memory_watch`

## Do Not Infer

- no baseline
- no automation
- no line registry promotion
- no current-position update
- no Gemini verified-truth authority

## Return Shape

- Plan Basis
- Gemini deep exploration packet
- self-application trial note
- Movement Record update

