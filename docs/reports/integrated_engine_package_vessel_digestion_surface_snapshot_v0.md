# Integrated Engine Package Vessel / Digestion Surface Snapshot v0

## 1. Verdict

PASS_WITH_NOTE

## 2. What This Snapshot Locks

The current integrated-engine UI now reads the active work package as a bounded processing vessel.

This does not change the implementation into automation. It only makes the operating interpretation visible:

- package = vessel for a purpose/object
- line / axis = weak internal structure signals read inside that vessel
- CLI / engine handling = processing / digestion
- return material = output that must be reread before absorption or redeposit
- redeposit = possible later route, not automatic approval

## 3. Where It Appears In The Surface

### Active Package Workbench

The central package summary now explains that the selected package is read as a vessel. The workbench remains one-package centered and does not become a team dashboard.

### Package Setup Modal

The setup modal now distinguishes:

- package vessel
- inner line / axis
- executor candidate
- context refs
- manual line / axis watch
- digestion guard

This keeps setup tied to purpose, boundary, evidence, and guardrails before execution.

### Line / Axis Watch Modal

The watch modal now includes digestion-specific reading:

- line reaction
- axis reaction
- digestion signal
- internal exploration trigger
- redeposit route
- what this is not

The modal explicitly says this is not automation, line promotion, or axis confirmation.

### Structure Reading Slot

The right-side structure slot now shows the current package through:

- vessel
- line hint
- axis hint
- precedent
- boundary
- package state
- digestion

These fields are weak/bounded readings, not claims of completed validation.

### VectorFL Event Rail

The former engine position log is now a VectorFL event rail. It makes recent movement legible as:

- input
- vessel
- digest
- return
- route
- line/axis
- redeposit

Each event may carry confidence, receiver, suggested action, and signal. This turns logs into mediation signals without pretending that the UI can automatically act on them.

## 4. Boundary

This snapshot does not authorize:

- automatic internal exploration
- package automation
- line promotion
- axis promotion
- canonical ingestion
- multi-handler orchestration
- automatic lower-to-upper bridge execution

## 5. Current Usable Reading

The screen can now support this user interpretation:

> I create or select one package as a vessel, give it a purpose, let the engine/CLI process it, then read the returned material as possible internal change, new material, or redeposit candidate.

This is sufficient for current one-handler operating use.

## 6. Remaining Limits

- The line / axis signals are still weak and manually interpreted.
- The event rail records mediation signals but does not yet dispatch packages.
- The watch modal is still a human inspection layer, not a live detector.
- Redeposit remains a later decision, not an automatic result of return.

## 7. Next Safe Action

Use this surface in small real tasks and observe whether the VectorFL event rail makes the current package flow easier to follow. If it still feels too abstract, the next patch should tune event labels and modal wording before adding any new automation.
