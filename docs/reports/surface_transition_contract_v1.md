# surface transition contract v1

## package status

complete for this turn

## files created

- [surface_atlas_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/surface_atlas_v1.md)
- [surface_transition_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/surface_transition_contract_v1.md)

## 1. why this atlas is needed now

Both phase1 and phase2 are frozen.

That means the main remaining risk is no longer local surface ambiguity inside one route. The main risk is cross-surface ambiguity:

- which surface should receive a question
- when the operator should leave phase1
- when phase2 should hand back to phase1
- what is still only a parked candidate

The atlas exists to answer those questions before new work starts to sprawl.

## 2. transition contract summary

### phase1 -> phase2

- use this when current thin observation is not enough and the operator needs time-axis reading
- phase1 does not hand over ownership
- transition is explicit only

### phase2 -> phase1

- use this when a prior state slice should come back only as contextual reread reference
- transition is explicit only
- handoff remains reference-only
- no restore, no load, no overwrite

### parked saved-path curation

- remains outside active routing
- neither phase1 nor phase2 should silently absorb it

## 3. what is reference-only vs what does not move

### reference-only

- asset context
- snapshot / cluster / trace reference
- reread context summary
- source honesty note

### does not move

- phase1 current path ownership
- saved path creation
- memory selection
- seed activation
- phase1/phase2 frozen boundary semantics

## 4. why some jumps are explicit only

Explicit-only is necessary because these surfaces are not interchangeable.

- phase1 owns current authoring and current saved-path/seed semantics
- phase2 owns time-axis rereading
- parked curation owns nothing yet because it is not promoted

If transitions were hidden or automatic, the frozen boundaries would collapse.

## 5. why some jumps are forbidden

Forbidden jumps are the ones that would silently redefine meaning:

- phase2 restoring or loading current phase1 state
- phase2 behaving like replay execution
- phase1 silently becoming history dashboard
- any route acting as though saved-path curation is already active

These are not convenience shortcuts. They are semantic boundary violations.

## 6. current watchpoints

- operators may still ask time-axis questions from inside phase1 because it remains the main entry surface
- phase2 reread context could still be overread as `restore state` if future wording loosens
- parked saved-path curation could be reopened too early if memory accumulation pressure is assumed rather than observed

## 7. next candidates

- one short manual atlas walkthrough to confirm common task questions map cleanly to phase1 or phase2 without ambiguity
- if saved-path accumulation pressure becomes real later, re-open the parked curation candidate under this atlas rather than inside phase1 or phase2
