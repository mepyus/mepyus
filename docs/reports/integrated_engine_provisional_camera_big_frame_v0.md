# Integrated Engine Provisional Camera Big Frame v0

## Status

PASS_WITH_NOTE

This document restates the held F0-F6 reusable reading-frame as a content-neutral provisional camera big frame.
It is not a promoted camera.

## Current Phase

- Current status: `camera-candidate review eligible, not promoted`
- Purpose: prepare review, not promotion.
- Promotion blocked until use procedure, target-shape boundary, rollback execution, and naming neutrality are reviewed.

## Naming Shift

The previous F0-F6 frame worked, but some names still carried transformer-specific residue.
This version uses C0-C6 to make the frame more content-neutral.

| previous frame | provisional camera slot |
|---|---|
| F0. Scope Anchor | C0. Scope Anchor |
| F1. Processing Tension / Problem Shift | C1. Processing Tension / Problem Shift |
| F2. Input / State Preparation | C2. Input / State Preparation |
| F3. Attention / Selection Mechanism | C3. Selection / Mechanism |
| F4. Output / Representation Result | C4. Output / Representation Result |
| F5. Block Support / Stability | C5. Support / Stability |
| F6. Support / Contrast / Limitation | C6. Contrast / Limitation / Guard |

## Camera Slot Definitions

### C0. Scope Anchor

- frame role: lock the reading range before interpretation expands.
- what it reads: what this asset is about, what is in scope, what is explicitly not being opened.
- what it does not read: full detail extraction, promotion decision, final categorization.
- acceptable content variation examples:
  - encoder-side self-attention and positional encoding
  - decoder/autoregressive generation
  - body/camera/lens correction
  - handoff grammar classification
- common failure mode: scope content is treated as universal frame content.
- rollback note: if only C0 is available, treat the asset as scope-anchor-only support, not a full probe target.

### C1. Processing Tension / Problem Shift

- frame role: identify what pressure, mismatch, or processing need drives the asset.
- what it reads: problem shift, correction pressure, training/inference tension, misread, route conflict.
- what it does not read: final solution, full implementation, broad theory.
- acceptable content variation examples:
  - RNN sequential limits vs transformer parallel processing
  - autoregressive inference vs parallel training
  - panel-first misread vs camera/lens projection correction
  - proposal-only material vs canonical boundary
- common failure mode: naming a topic as if it were a tension.
- rollback note: if no tension is present, do not force one; mark C1 missing and consider asset-specific reading.

### C2. Input / State Preparation

- frame role: show how the object is prepared before the main mechanism acts.
- what it reads: input representation, source bundle, shifted input, evidence bundle, baseline context, state setup.
- what it does not read: the mechanism itself or the final return.
- acceptable content variation examples:
  - token embedding to Q/K/V preparation
  - shifted decoder input and mask setup
  - common camera frame stages
  - handoff source material and authority setup
- common failure mode: jumping from scope directly to result without preparation state.
- rollback note: if preparation is implicit only, mark C2 partial, not invented.

### C3. Selection / Mechanism

- frame role: identify how the asset chooses, routes, weighs, filters, foregrounds, or mediates information.
- what it reads: attention, masking, cross-reference, route decision, lens selection, validation mechanism, classification mechanism.
- what it does not read: all downstream outputs or broad governance.
- acceptable content variation examples:
  - dot-product attention and softmax weight
  - causal mask and cross-attention
  - lens selection and surface projection
  - authority grammar and validation grammar
- common failure mode: keeping transformer-specific "attention" wording where the target has selection/foregrounding instead.
- rollback note: if no selection mechanism is visible, mark C3 missing; do not rename unrelated content as mechanism.

### C4. Output / Representation Result

- frame role: identify what the mechanism produces as the next usable representation, output, route, or return.
- what it reads: representation result, generation output, surface projection, classified return, candidate state.
- what it does not read: final promotion or canonical ingestion.
- acceptable content variation examples:
  - context-bearing token representation
  - next-token probability distribution
  - surface-specific composition
  - handoff classification result
- common failure mode: treating candidate output as final canonical output.
- rollback note: if output status is unclear, keep candidate/hold labels visible.

### C5. Support / Stability

- frame role: identify what lets the main process remain stable, repeatable, or usable.
- what it reads: residual/norm support, correction path, process guard, ownership boundary, run discipline.
- what it does not read: independent new core concepts.
- acceptable content variation examples:
  - residual path and layer norm
  - composition pass over existing screen
  - workspace ownership and collision boundary
  - recovery checklist
- common failure mode: promoting support into a new center.
- rollback note: if support dominates the asset, check whether the asset is actually a support note rather than a full probe target.

### C6. Contrast / Limitation / Guard

- frame role: attach constraints, non-goals, limitations, negative examples, and rollback brakes to the relevant core segments.
- what it reads: must-not, limitations, contrast cases, support placement, rollback signals.
- what it does not read: new work expansion or promotion approval.
- acceptable content variation examples:
  - simple number append rejected
  - rare-position limitation
  - must-not list
  - final wording / axis / canonical drift guards
- common failure mode: guard list becomes the main reading object.
- rollback note: if C6 becomes central, reattach each guard to the core segment it protects.

## Provisional Use Rule

Use C0-C6 only as a review candidate frame.
Before applying it, run target-shape gate:

1. Is the asset content-bearing?
2. Can at least four of C1-C6 be tested?
3. Is C0 scope anchor separable from content?
4. Can support lines attach to core segments?
5. Can mismatch be marked without forcing?

If no, do not apply the frame as a probe.

## Not Promoted Boundary

This document does not create:

- a canonical camera
- an axis
- a glossary
- a UI structure
- an ingestion rule

## Pointers

- Recovery checklist: `docs/reports/integrated_engine_process_recovery_checklist_v0.md`
- Lens draft: `docs/reports/integrated_engine_lens_structure_draft_v0.md`
- Test pool matrix: `docs/reports/integrated_engine_internal_external_test_pool_matrix_v0.md`
- Verification and rollback: `docs/reports/integrated_engine_verification_and_rollback_discipline_v0.md`
