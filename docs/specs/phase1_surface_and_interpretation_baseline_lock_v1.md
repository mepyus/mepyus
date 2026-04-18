# phase1 surface and interpretation baseline lock v1

## verdict

lock current phase1 as baseline

## purpose

This document locks the current `phase1` surface and interpretation structure so later refinement cannot silently change its meaning.

The baseline is not a feature expansion plan. It is a meaning lock for current surfaces, state layers, persistence boundaries, and anti-confusion rules.

## 1. phase1 surface purpose

### Operating

- What it is:
  - thin observation surface for current engine state, selected asset, recent activity, and minimal path/sticker hints
- What it is not:
  - not a whole-space UI
  - not an onboarding controller
  - not an interpretation workspace

### Explore

- What it is:
  - path-centered interpretation attempt
  - `object -> lens -> position -> preview -> explicit sticker`
- What it is not:
  - not direct-access search
  - not automatic memory
  - not a giant stepper or wizard

### Search

- What it is:
  - direct access surface for object, lens, position, connection, or memory lookup
- What it is not:
  - not the main onboarding surface
  - not exploration flow reuse

### Memory

- What it is:
  - explicit saved interpretation paths only
- What it is not:
  - not click log storage
  - not residue storage
  - not a large document viewer

### Similar

- What it is:
  - seed-based local re-query from an activated sticker context
- What it is not:
  - not recommendation
  - not ranking semantics
  - not whole-space derivation

## 2. state layer distinctions

### preset

- What it is:
  - quick-start scaffold for object, lens, and position selection
- What it is not:
  - not taxonomy
  - not source of truth
- Stored where:
  - thin helper/constants inside phase1 runtime code
- Visible where:
  - Explore only
- Moves upward by:
  - selecting preset values into current path

### current path

- What it is:
  - the currently active interpretation path in Explore
- What it is not:
  - not Memory
  - not Similar result
- Stored where:
  - in current phase1 shared interaction state
- Visible where:
  - Explore primarily
  - thinly in Operating
- Moves upward by:
  - explicit sticker save only

### residue

- What it is:
  - latest in-progress path snapshot for re-entry convenience
- What it is not:
  - not memory
  - not seed
  - not automatic sticker
- Stored where:
  - latest snapshot JSON runtime file
- Visible where:
  - Explore
  - thinly in Operating
- Moves upward by:
  - it does not auto-promote
  - user must restore it and then explicitly save a sticker

### sticker

- What it is:
  - explicit saved interpretation path with structured reason fields
- What it is not:
  - not residue
  - not click trace
- Stored where:
  - append-only sticker JSONL
- Visible where:
  - Memory
  - Similar seed selection
  - thinly in Operating
- Moves upward by:
  - sticker activation can create an active seed for Similar

### active seed

- What it is:
  - selected sticker context used to drive Similar local re-query
- What it is not:
  - not a new memory layer
  - not recommendation context
- Stored where:
  - current phase1 shared interaction state
- Visible where:
  - Similar
  - thinly in Operating and Memory badges
- Moves upward by:
  - selecting a sticker as seed

### similar result

- What it is:
  - local re-query output around a seed sticker
- What it is not:
  - not recommendation
  - not explicit memory yet
- Stored where:
  - derived at runtime from current seed context
- Visible where:
  - Similar only
- Moves upward by:
  - only through explicit sticker save

## 3. anti-confusion contract

| layer | means | not this |
| --- | --- | --- |
| preset | quick-start scaffold | hidden taxonomy |
| current path | active Explore interpretation path | saved memory |
| residue | in-progress path snapshot | sticker or memory |
| sticker | explicit saved interpretation path | click log |
| active seed | activated sticker context for Similar | recommendation engine state |
| similar result | local re-query output | ranked recommendation |

## 4. interpretation lens principle

- Lens is not a locked field.
- Lens is an interpretation position.
- Many lenses do not produce automatic richness.
- Richness manifests when selected structure is retained and reused through sticker, seed, and later rereading.

## 5. runtime path map

### sticker persistence

- Path:
  - `runtime/manifests/operating_ui_phase1/phase1_memory_stickers.jsonl`
- Storage style:
  - append-only
- Why:
  - sticker is explicit saved interpretation path and should remain durable and separable

### residue persistence

- Path:
  - `runtime/manifests/operating_ui_phase1/phase1_current_path_residue.json`
- Storage style:
  - latest snapshot
- Why:
  - residue is only the latest in-progress trace and must stay below Memory in weight and meaning

## 6. phase1 non-goals

- whole-space UI
- recommendation or workflow semantics
- automatic memory generation
- compare track reactivation
- hidden taxonomy hardening
- residue to memory confusion
- seed to recommendation confusion
- preset to ontology confusion

## 7. allowed refinement direction

Later refinement may improve readability, authoring ergonomics, or trace clarity only if it preserves this baseline:

- Operating stays thin
- Explore stays path-centered
- Search stays direct access
- Memory stays explicit-sticker-only
- Similar stays seed-based local re-query
- preset, residue, sticker, seed, and similar result remain semantically distinct

## 8. drift check

Future changes should be treated as drift if they do any of the following:

- make preset read like taxonomy
- make residue read like memory
- make Similar read like recommendation
- make Memory absorb non-explicit traces
- make Operating expand into whole-space interpretation UI

