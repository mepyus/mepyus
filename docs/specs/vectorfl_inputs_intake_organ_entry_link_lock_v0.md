# vectorfl inputs intake organ entry link lock v0

## 1. purpose

`Inputs / Intake` should not remain only a material summary surface.
If VectorFL Paper is supposed to show organ flow, intake must also expose its own
organ entry and a visible bridge back to current-reading.

## 2. lock

The semi-live `Inputs / Intake` surface should expose:

- direct link to `Input Organ Detail`
- direct link back to `Current Reading Center`

## 3. semantic rule

This does not promote intake above current-reading.

- `Inputs / Intake` remains a primary surface for material inspection
- `Input Organ Detail` makes intake responsibility explicit
- `Current Reading` remains canonical semantic center

## 4. why this matters

Without this link, intake stays a passive data screen.

With this link, the operator can see:

- what source material was selected
- what the input organ is responsible for preserving
- how weak/fallback carry is handled
- how intake hands material back toward current-reading flow

## 5. current lockable outcome

At the current stage, `Inputs / Intake` should be read as:

- material surface
- provenance surface
- input-organ drill-in entry
- bridge surface back to current-reading
