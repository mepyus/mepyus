# Runtime Evidence Priority Router v1 Report

## What It Reads
- Adjacent canonical diff
- Interpretation badges
- Trigger type and evidence presence
- Blocker add/remove signals

## Current Routing Outcome
- Representative recent runtime adoption updates route to `background`.
- Reason: they are `provenance_only` and produce no canonical drift.
- This prevents provenance-only flooding from occupying the main attention surface.

## Priority Reading
- `critical` is reserved for traceability, grounding, packet texture, blocker-added, and manual correction.
- `high` is used for emergence, carryover, maturation, blocker-removed, and mixed shifts.
- `medium` covers comparison memory changes, generic canonical changes, and first-anchor reads.

## Suppression
- Repeated provenance-only runtime updates are suppressed from active queue entry creation.
- They remain available as compact background summaries.

## Limits
- Current representative assets do not yet exercise `critical` or `high` paths in recent updates.
- De-dup is currently asset-latest oriented rather than multi-update clustering across many recent records.
