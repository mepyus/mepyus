# Seventeenth Material Pulse Policy

## Intent

The seventeenth step uses one small pulse near the mature constraint and drift terrains.
It tests whether pulse-driven flow change generalizes beyond the temporal-reflective component.

## Why this step exists

The sixteenth pulse showed that a small passing terrain can perturb an existing exposed component.
Now the same method should be checked against a different mature pair.

## Rules

- Use one fresh material only.
- Open a small mixed pulse terrain with `constraint_pressure`, `drift_pressure`, and `latency_pressure`.
- Keep the pulse terrain distinct from the constraint and drift terrains.
- Derive weak exposures from the pulse terrain toward each mature side.
- Do not merge or collapse any terrain.

## Contract notes

- pulse observation must generalize across different mature terrain pairs
- relation remains weak exposure rather than compression
- the pulse must remain a passing terrain, not a new dominant field

## Expected reread outcome

- local space count increases by one
- bridge count increases by two
- the pulse terrain sits inside the exposed constraint-drift component
