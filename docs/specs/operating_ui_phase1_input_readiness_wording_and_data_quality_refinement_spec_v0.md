# operating_ui_phase1 input readiness wording and data quality refinement spec v0

## verdict

- the next legitimate refinement for the first operating-surface panel is a readiness-quality branch, not an engine-expansion branch
- this branch may improve wording clarity and field labeling only
- missing readiness data must remain visibly thin rather than being filled by new runtime behavior

## current weakness summary

### current clear parts

- the panel appears first in the reading path
- selected source and live availability are visible
- provenance wording is visible
- the panel signals whether observation material is broadly available or sparse

### current indirect parts

- split status is not directly attached and is currently represented through thin proxy wording
- linked status is inferred indirectly from multi-lens artifact availability
- observation readiness is readable, but not always through first-order dedicated readiness fields

### current weakness

- the panel still depends on proxy wording more than on cleanly labeled readiness fields
- a supervisor can follow the panel, but the distinction between `ready`, `partially ready`, and `unavailable` is not yet expressed as clearly as it could be

## allowed refinement target

This branch may refine:

- wording clarity
- field labeling clarity
- clearer distinction between:
  - ready
  - partially ready
  - unavailable

Refinement direction:

- make it easier for a supervisor/operator to tell what is directly known
- make it easier to see what is only thin proxy wording
- keep the panel explanation-first and explicitly bounded

## data-source rule

### first rule

- use existing runtime/artifact fields first

### second rule

- if a readiness field is missing, preserve placeholder or empty-state wording

### forbidden shortcut

- do not add new engine behavior
- do not synthesize hidden readiness state
- do not invent deeper linkage or receipt logic just to make the panel look fuller

## prohibited interpretations

- readiness does not mean maturity
- readiness does not mean decision permission
- readiness wording improvement does not mean deeper runtime intelligence
- a clearer first panel does not authorize promotion, reopen, or operating decision logic

## non-goals

- no heuristic/runtime change
- no composition redesign
- no decision behavior
- no promotion behavior
- no maturity interpretation

## reopen condition for actual UI patch

- an actual UI patch for the `Input Readiness` panel may open only after this spec is locked
- the patch must stay inside wording/data-quality refinement scope
- any proposal that requires new runtime state, hidden inference, or engine expansion falls outside this branch

## current conclusion

- a legitimate readiness refinement is a wording/data-quality refinement only
- the correct next move is to make the first panel clearer, not smarter
- this spec exists to separate bounded UI clarity work from hidden engine growth
