# vectorfl history trace detail drill-in lock v0

## 1. purpose

`History / Trace` should not remain only a short recap list.
If trace, residue, and reentry are first-class in VectorFL, the operator should be
able to drill into a trace item and inspect its carry logic directly.

## 2. lock

The semi-live route set should expose direct detail links from each visible trace row
to a dedicated trace detail page.

## 3. required reading on trace detail

The trace detail surface should make the following visible:

- trace id
- trace kind
- summary
- residue note
- reentry hint
- residue emphasis
- reentry cues

## 4. semantic rule

Trace detail does not replace `History / Trace` as a primary surface.

- `History / Trace` remains the list and carry surface
- trace detail remains drill-in
- trace detail deepens retrospective reading without re-centering the app

## 5. inheritance reason

This continues the same structural inheritance rule used for organ detail:

- a visible surface
- a drill-in target
- deeper bounded inspection

What is inherited is progression legibility and inspectability, not external ontology.
