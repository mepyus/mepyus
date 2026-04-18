# Engine Operating Layer Freeze v1 Report

## Why Freeze Now
- The engine already has a stable canonical operating-state core.
- It also has enough derived operating layers that boundary confusion is now a real risk.
- Freezing now prevents derived summaries, UI surfaces, and experimental naming from drifting into authoritative roles.

## Four-Layer Split

### Core
- authoritative
- owns schema, history, latest regeneration, and update policy

### Derived
- non-authoritative
- owns diff, badge, compaction, queue, lifecycle, and memory

### Surface
- non-authoritative
- owns operator-facing reading and navigation
- process console is the main surface here

### Experimental
- non-authoritative
- isolated naming-heavy interpretation and promotion candidates

## Authoritative Hierarchy
- history/schema/policy are highest authority
- latest is derived but still part of core operation
- diff/badge/queue/memory are downstream derived layers
- UI text and display mapping are below those
- experimental naming remains lowest authority

## Process Console Position
- process console is now explicitly fixed as the engine's main operating surface
- it reads latest, lineage, diff, attention, and memory
- it does not replace the core and is not replaced by graph-first views

## Why This Counts As First Operating Layer Completion
- canonical state exists
- append-only history and latest regeneration exist
- update policy exists
- runtime evidence bridge exists
- repeatability fixture exists
- process console reads state/history/diff/attention/memory in one surface

That is enough to call the state-first operating layer complete at v1 freeze level.

## Expansion Boundaries
- derived layer may keep evolving
- surface UX may keep evolving
- experimental layer may keep collecting hypotheses
- core changes are now restricted and require explicit freeze-breaking intent

## Remaining Limits
- this freeze does not promote high-level meaning objects
- this freeze does not remove experimental ambiguity
- this freeze does not make derived summaries authoritative
