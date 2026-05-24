# Position Anchor Self-Application Trial 20260506 v0

## Status

```yaml
status: self_application_trial
date: 2026-05-06
baseline_lock: false
automation: false
```

## Purpose

Test the user's correction:

```text
Do not only make anchors. Use them while setting up.
```

## Active Compact Anchor

- `app/work/COMPACT_POSITION_ANCHOR_20260506_LACL_REGROUNDING_V0.md`

## Position IDs Used

- `PV_PLAN_BASIS_GATE`
- `PV_BOUNDED_REREAD_UNIT`
- `PV_NON_INSPECTED_DISCLOSURE`
- `PV_RETURN_TO_SPACE_CLOSEOUT`

## How The Anchor Changed This Turn

### 1. Plan Basis before more setup

Codex created:

- `app/work/PLAN_BASIS_20260506_LACL_REGROUNDING_SETUP_V0.md`

This prevents the turn from becoming "just add more documents."

### 2. Gemini packet is bounded by role and output shape

The Gemini instruction is designed for deep/wide reading, but it asks for:

- evidence-backed line / axis / camera / lens re-grounding data
- non-inspected disclosure
- missing / unclear areas
- do-not-promote boundaries

It does not ask for a whole-space summary or ontology.

### 3. Return-to-Space is required

This trial records whether the position IDs changed task shape.

## Early Finding

The compact anchor did change the setup:

- forced a Plan Basis
- made Gemini packet design the main work product
- prevented another abstract layer from being added without a trial note
- preserved non-inspected / no-promotion cautions

## Watch

- This is a single self-application trial, not proof.
- Future turns should keep using compact anchors, otherwise the setup remains decorative.
- If position IDs become mandatory ceremony, they should be reduced or redesigned.

## Return-to-Space Value

- Reusable finding: compact position anchors can guide Codex setup behavior inside the same turn.
- Reusable finding: `PV_BOUNDED_REREAD_UNIT` is the right position for Gemini deep exploration packets.
- Future reuse note: every future external-tool planning/setup turn should start with either a compact anchor or a reason not to use one.

