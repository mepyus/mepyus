# phase1 freeze and handoff contract v1

## verdict

freeze phase1 as current baseline and handoff-ready surface contract

## purpose

This document freezes `phase1` after surface semantics, state ownership, jump contract, runtime adapter binding, and provenance visibility have been aligned.

The goal is not more phase1 expansion. The goal is to lock what is now stable, identify what remains watch-only, and prevent later work from silently changing phase1 meaning.

## 1. frozen

### surface roles

- `Operating`
  - thin observation only
- `Explore`
  - path-centered interpretation authoring
- `Search`
  - direct access only
- `Memory`
  - explicit saved interpretation paths only
- `Similar`
  - activated-seed local re-query only

### state ownership

- `Explore` owns current path authoring
- `Memory` owns explicit saved path selection
- `Similar` owns active seed context and local re-query view
- `Search` offers explicit jump/import only
- `Operating` observes and does not author interpretation state

### jump contract

- `Search -> Explore`
  - imports current path fields only
- `Search -> Memory`
  - selects saved path only
- `Search -> Similar`
  - activates seed context only
- `Memory selection`
  - does not auto-activate Similar seed
- `Similar clear seed`
  - detaches seed context without mutating Memory selection

### baseline wording principles

- use `saved path`, `seed context`, `import context`, `local re-query`
- do not use recommendation-like language
- do not let provenance wording override phase1 semantics
- keep `resume`, `restore`, `import`, `activate`, `save` distinct

### runtime adapter boundary

- raw runtime names stay behind the phase1 adapter
- phase1 surfaces read translated view-model summaries, not raw payload keys
- sparse or missing runtime data must degrade gracefully without semantic drift

### provenance / availability categories

- `live`
- `fallback`
- `stored`
- `degraded`
- `unavailable`

These categories are frozen as thin source-reading aids, not authority markers.

## 2. forbidden drift

- `preset -> taxonomy`
- `residue -> memory`
- `sticker -> auto seed`
- `Similar -> recommendation`
- `Search -> exploration stepper`
- `Operating -> dashboard bloat`
- raw runtime naming -> phase1 semantic wording

## 3. open but not promoted

These stay watch-only. They are not promotion grounds by themselves.

- wording drift risk
  - provenance and helper text can still slowly reintroduce ambiguity
- runtime source sparsity
  - live source can be partial or unavailable; degraded mode must stay honest
- Similar heuristic weakness
  - current local re-query remains intentionally thin and non-claiming
- scaffold overgrowth risk
  - presets must remain handholds, not hidden structure

## 4. trim note

Current trim intent is also frozen:

- remove provenance badges that only restate the same state
- keep helper text only where absence would create confusion
- avoid thick debug-note accumulation inside the main surfaces

This means phase1 can stay legible without losing its boundary language.

## 5. handoff contract

Later work on phase1 is allowed only in these categories:

- bugfix
- wording governance cleanup
- source-binding maintenance
- degraded/fallback honesty improvements
- small readability trims that do not change ownership or surface role

Later work on phase1 is not allowed in these categories without an explicit baseline re-open judgment:

- new phase1 feature expansion
- changing state ownership
- changing jump semantics
- changing Memory/seed/sticker boundaries
- changing Search into an exploration surface
- changing Similar into recommendation-style output
- expanding preset scaffolds toward hidden taxonomy

New ideas should be evaluated as phase2 or adjacent-surface work first, not as default phase1 extension.

## 6. runtime path reminders

- saved paths
  - `runtime/manifests/operating_ui_phase1/phase1_memory_stickers.jsonl`
  - append-only explicit saved path store
- residue
  - `runtime/manifests/operating_ui_phase1/phase1_current_path_residue.json`
  - latest-snapshot in-progress trace only

The two stores remain different in meaning, weight, and allowed UI treatment.

## 7. handoff reading rule

Anyone modifying phase1 after this freeze should read these documents first:

- [phase1_surface_and_interpretation_baseline_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/phase1_surface_and_interpretation_baseline_lock_v1.md)
- [phase1_freeze_and_handoff_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/phase1_freeze_and_handoff_contract_v1.md)

If a proposed change conflicts with either document, treat it as baseline drift until explicitly re-opened.
