# phase2 operating history replay trace surface baseline lock v1

## verdict

lock this as current phase2 adjacent-surface baseline

## purpose

This document locks the `operating history / replay / trace` surface as a phase2 adjacent surface outside frozen phase1.

The goal is not to rush implementation. The goal is to define why this surface exists, what it reads, what it does not become, and how it stays separated from phase1.

## 1. why this surface exists

- `phase1 Operating` is already frozen as a thin current observation surface.
- time-axis reading pressure, prior state revisit pressure, and trace inspection pressure should not be absorbed into phase1.
- therefore `history / replay / trace reading` must live in a separate adjacent surface rather than inside phase1.

This surface exists to receive the temporal reading pressure that phase1 must not absorb.

## 2. one-line role

This surface is a read-oriented time-axis companion that lets the operator revisit recent/past operating traces and state formation without replacing the live phase1 operating surface.

## 3. what it is / what it is not

### what it is

- a read-oriented time-axis surface
- a replay / revisit / trace reading surface
- an operating history companion
- a drill-down surface for how current state formed over time

### what it is not

- not the live operating replacement
- not a command center
- not a workflow automation surface
- not a recommendation surface
- not a whole-space timeline
- not a developer debug console

## 4. relationship to phase1

- `phase1 Operating` stays current, thin, and present-tense
- this phase2 surface handles past/recent lineage, replay reading, and trace reading
- phase1 may connect to this surface only by explicit link or jump
- this phase2 surface must not overwrite phase1 shared spine semantics
- this phase2 surface must not turn phase1 into a history dashboard

## 5. minimum surface model

The minimum reading units are locked as:

### run snapshot

- why needed:
  - gives a readable unit for one operating moment or formed state slice
- answers:
  - what did the operator-facing state look like at this point
- different from phase1 current observation because:
  - phase1 reads the current slice only; this surface rereads older or adjacent slices

### activity cluster

- why needed:
  - keeps recent operating movement readable without forcing raw line-by-line history
- answers:
  - what recent set of related changes or activity grouped together
- different from phase1 current observation because:
  - phase1 shows recent hints; this surface groups and revisits them as a time-axis unit

### trace entry

- why needed:
  - gives a translated unit for state change, reason, evidence, or shift marker
- answers:
  - why did this state change happen and what kind of trace is attached to it
- different from phase1 current observation because:
  - phase1 only hints at current and recent context; this surface lets the operator inspect the formed trace unit itself

### replayable state

- why needed:
  - allows a prior operating state to be reopened as a reading target
- answers:
  - what earlier state or configuration should be reread in view form
- different from phase1 current observation because:
  - it is not the current authoritative view; it is a rereadable earlier state projection

These four units are enough for baseline lock. This surface does not need more units at this stage.

## 6. key reading actions

The allowed key actions are:

1. read recent runs or recent snapshots
2. open one run snapshot or activity cluster
3. inspect trace entries around a selected snapshot
4. reopen a replayable state as a view-level reread
5. return to phase1 current context by explicit link

These actions are reading actions, not execution actions.

## 7. replay boundary

- `replay` means view-level reconstruction for rereading a prior state or prior trace context
- `replay` does not mean automatic reenactment
- `replay` does not mean workflow rerun
- `replay` does not mean simulation engine behavior
- `replay` does not mutate current live operating state by default

## 8. trace boundary

- `trace` means a translated reading unit for state change, activity shift, trigger, or evidence-bearing operating movement
- `trace` is for operator-facing reading
- `trace` is not a full audit platform
- `trace` is not a developer debug console
- `trace` should be translated into readable surface units rather than exposed as raw dump

## 9. provenance and source stance

- this surface may read raw runtime history sources underneath, but it does not expose them as a thick raw dump
- provenance should remain visible at a thin reading-layer level
- degraded or sparse source conditions must be shown honestly
- raw source naming must be translated into surface-facing reading units

## 10. non-goals

- full replay engine
- execution controls
- command issuing
- automated recommendation
- saved-path curation expansion
- object deep detail surface
- rich Similar expansion
- whole-system timeline

## 11. anti-drift lock

Future work should be treated as drift if it does any of the following:

- expands phase1 Operating to absorb this surface
- treats replay as rerun or execution
- treats trace as debug dump
- treats history reading as recommendation or workflow direction
- turns this surface into a giant operating dashboard

## 12. open questions

- which repo source mix should become the first translated reading input: history jsonl only, or history plus update events together
- how much compaction should happen before this surface starts to read naturally without becoming raw history scroll
- what the thinnest explicit handoff from phase1 should be: current asset, current run, or selected saved path anchor

## 13. handoff note

This baseline exists so implementation can proceed later without re-opening phase1.

If a future implementation requires:

- phase1 shared spine change
- phase1 Operating expansion
- recommendation-like ranking
- execution or rerun semantics

then treat that as baseline drift and stop for re-judgment first.
