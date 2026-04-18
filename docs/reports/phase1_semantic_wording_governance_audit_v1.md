# phase1 semantic wording governance audit v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_semantic_wording_governance_audit_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_semantic_wording_governance_audit_v1.md)

## 1. wording areas audited

- surface purpose copy
- state-layer labels around:
  - preset
  - current path
  - residue
  - sticker / saved path
  - active seed
  - similar result
  - imported context
- jump action wording
- empty-state helper text

## 2. drift-risk wording and cleanup

### Similar result note

- current risk:
  - `local resonance result` could drift toward soft recommendation or vague relevance rhetoric
- revised wording:
  - `local re-query output / not recommendation / not ranked answer`
- risk level:
  - medium -> lower

### Operating sticker hint

- current risk:
  - `selected sticker` and `active seed status` were close enough to blur Memory selection and Similar seed ownership
- revised wording:
  - `memory selection`
  - `active seed context`
  - title changed to `Path / Saved Path Hint`
- risk level:
  - high -> medium

### imported-from wording

- current risk:
  - `imported from` read slightly like provenance or audit log rather than current state context
- revised wording:
  - `import context=...`
- risk level:
  - medium -> lower

### Search groups and actions

- current risk:
  - `stickers / memory` and `use in Similar` were functional but could read a bit loosely
- revised wording:
  - `saved paths / memory`
  - `seed-related paths`
  - `activate in Similar`
- risk level:
  - medium -> lower

### Memory labels

- current risk:
  - `Stickered Paths` and `activate as Similar seed` were semantically correct but less explicit about saved-path ownership
- revised wording:
  - `Explicit Saved Paths`
  - `activate seed in Similar`
- risk level:
  - medium -> lower

### Similar seed wording

- current risk:
  - `selected sticker or seed_ref` and `Seed` were too implementation-flavored
- revised wording:
  - `active seed context -> thin local re-query`
  - `Seed Context`
  - `explicit saved paths are the only seeds in this turn`
- risk level:
  - high -> lower

## 3. wording kept as-is and why

- `save explicit sticker`
  - kept because `sticker` is still a deliberate phase1 term and the action must remain clearly different from residue or import
- `blank authoring entry`
  - kept because it usefully distinguishes blank start from quick-start scaffold
- `residue`
  - kept because it already names the in-progress trace layer distinctly from Memory

## 4. remaining watchpoints

- `sticker` and `saved path` now coexist; this is intentional but still worth watching so the two terms do not diverge in meaning
- `seed-related paths` in Search is controlled, but future copy polish could still drift toward recommendation language if trace-first wording weakens
- `import context` is clearer than `imported from`, but still needs consistency in future edits across Explore, Memory, and Similar

## 5. next candidates

- run one short manual wording walkthrough after any future Search or Similar copy change
- decide whether `sticker` should remain the primary internal term while `saved path` stays the dominant user-facing term
