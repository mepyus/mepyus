# Eleventh Material Wave Policy

## Intent

The eleventh material wave introduces a genuinely different component band.
It opens a fatigue-constraint-conflict terrain that should stand independently from the already formed terrains.

## Why this step exists

Repeated same-family returns were useful for fast-forwarding maturation.
But space also has to prove that it can receive a different component band without collapsing the existing terrains.

## Rules

- Open a new family `seed-eleventh-wave`.
- Use a new pressure band built from `fatigue_pressure`, `constraint_pressure`, and `conflict_pressure`.
- Keep only weak reference to prior terrain.
- Create a fresh seed, candidate cell, relocation reaction, and local space.
- Do not create a bridge during this wave.
- Let the new terrain stand independently first.

## Contract notes

- heterogeneity must widen space before it is allowed to compress into relation
- the new component band should participate without forced adjacency
- bridge count must stay unchanged during this wave

## Expected reread outcome

- local space count increases
- terrain component count increases
- bridge count remains one
- the new terrain appears as another independent single-local climate
