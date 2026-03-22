# Sixteenth Material Pulse Policy

## Intent

The sixteenth step uses a single material pulse rather than a larger wave.
It checks whether one small mixed terrain can perturb an existing weak exposure without collapsing either side.

## Why this step exists

After the first observed bridge-facing exposure, the next useful test is not another broad wave.
It is a single pulse that lets us watch local flow change.

## Rules

- Use one fresh material only.
- Open a small mixed pulse terrain with `temporal_pressure`, `reflection_pressure`, and `recurrence_pressure`.
- Keep the pulse terrain distinct from the temporal-project and reflective terrains.
- Derive weak exposures from the pulse terrain toward each mature side.
- Do not merge or collapse any terrain.

## Contract notes

- pulse observation stays space-first
- relation is still exposure, not compression
- the pulse must remain a small passing terrain, not a new dominant field

## Expected reread outcome

- local space count increases by one
- bridge count increases by two
- the pulse terrain sits inside the exposed temporal-reflective component
