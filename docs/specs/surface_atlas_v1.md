# surface atlas v1

## verdict

lock current surface atlas as the upper map for frozen phase1, frozen phase2, and parked adjacent candidate

## purpose

This document maps the current operator-facing surface system above individual surface internals.

The goal is not to add functionality. The goal is to clarify which surface answers which kind of question, where each route lives, what transitions are explicit only, and what remains parked rather than active.

## 1. current atlas

### phase1

- role
  - current operating surface family
  - thin observation, path authoring, direct access, explicit saved path selection, seeded local re-query
- current route
  - `/operating-ui-phase1`
- internal surfaces
  - `Operating`
  - `Explore`
  - `Search`
  - `Memory`
  - `Similar`

### phase2

- role
  - adjacent time-axis reading companion
  - history, reread, and translated trace reading outside phase1
- current route
  - `/operating-ui-history`
- minimum sections
  - `Recent Runs / Snapshots`
  - `Activity Cluster List`
  - `Trace Reading Panel`
  - `Rereadable State Preview`
  - `Return / Open in phase1`

### parked candidate

- name
  - `saved-path curation surface`
- role
  - possible later adjacent surface for rereading and lightly curating explicit saved paths
- current status
  - parked
  - not active
  - not implemented

## 2. question-to-surface map

### questions for phase1

- what is happening now
  - go to `phase1 / Operating`
- how do I try one interpretation path from an object
  - go to `phase1 / Explore`
- how do I directly find an object, lens, position, saved path, or seed-related item
  - go to `phase1 / Search`
- which explicit saved paths do I already have
  - go to `phase1 / Memory`
- what local similar structure can I reread from one activated seed
  - go to `phase1 / Similar`

### questions for phase2

- how did the current operating state form over time
  - go to `phase2 / history`
- what recent or prior read checkpoint should I reread
  - go to `phase2 / recent runs / snapshots`
- what grouped activity flow belongs to this checkpoint
  - go to `phase2 / activity cluster list`
- what translated trace unit explains this slice
  - go to `phase2 / trace reading panel`
- which prior state slice should I reopen as reread context
  - go to `phase2 / rereadable state preview`

### questions not yet assigned to an active surface

- how should many saved paths be reread, lightly grouped, or curated over time
  - parked candidate only
  - not phase1
  - not phase2

## 3. route / entry map

- `/operating-ui-live`
  - current live operating surface outside this atlas lock
- `/operating-ui-phase1`
  - frozen phase1 shell
- `/operating-ui-history`
  - frozen phase2 history / reread / trace shell

The parked saved-path curation candidate has no active route.

## 4. transition atlas

### phase1 -> phase2

- why
  - when current thin observation is no longer enough and the operator needs time-axis reading
  - when recent activity hint needs lineage rereading
  - when current state needs prior state slice rereading
- allowed transition
  - explicit link or jump only
- state stance
  - phase1 does not hand over ownership
  - phase2 receives reading pressure, not control state

### phase2 -> phase1

- why
  - when a prior state slice should be carried back only as contextual reread reference
  - when the operator wants to return to current authoring/direct-access/saved-path work
- allowed transition
  - explicit `open in phase1 with reread context`
- state stance
  - reference only
  - not restore
  - not load
  - not overwrite

### phase1 -> parked candidate

- current status
  - not allowed
- reason
  - saved-path curation remains parked and unpromoted

### phase2 -> parked candidate

- current status
  - not allowed
- reason
  - time-axis reading and saved-path curation are still separate concerns

## 5. explicit-only jumps

- `phase1 Search -> Explore`
  - explicit import only
- `phase1 Search -> Memory`
  - explicit saved path selection only
- `phase1 Search -> Similar`
  - explicit seed activation only
- `phase1 Memory -> Similar`
  - explicit seed activation only
- `phase1 -> phase2`
  - explicit route/link only
- `phase2 -> phase1`
  - explicit reread-context link only

## 6. forbidden jumps

- `phase1 -> phase2` by hidden automatic mutation
- `phase2 -> phase1` by restore/load/rerun semantics
- `phase2 -> phase1` by current path overwrite
- `phase2 -> phase1` by automatic saved path creation
- `phase2 -> phase1` by automatic memory selection
- `phase2 -> phase1` by automatic seed activation
- any route into parked saved-path curation as if it were active

## 7. transition payload rules

### phase1 -> phase2

- allowed
  - current asset or current reading anchor by explicit link
- not allowed
  - changing phase2 into a control dashboard

### phase2 -> phase1

- allowed
  - `asset_id`
  - snapshot/cluster/trace reference
  - reread context summary
  - source honesty note
- not allowed
  - saved path creation
  - memory selection
  - active seed activation
  - current path overwrite

## 8. upper anti-drift rules

- phase1 must remain the current operating family, not a time-axis dashboard
- phase2 must remain the time-axis reading companion, not a command center
- parked saved-path curation must remain parked until separately promoted
- explicit transition is required whenever moving meaning across frozen boundaries
- contextual reference is lighter than ownership and must stay lighter

## 9. atlas reading rule

Any future surface work should first answer:

- is this question about current reading or time-axis reading
- does this belong to frozen phase1, frozen phase2, or a parked/new candidate
- is the transition explicit only
- does the handoff transfer ownership or only reference

If the answer is unclear, treat the proposal as atlas-level drift until clarified.
