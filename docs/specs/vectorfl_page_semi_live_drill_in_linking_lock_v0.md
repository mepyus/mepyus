# vectorfl page semi-live drill-in linking lock v0

## 1. purpose

Semi-live organ detail should not remain a hidden secondary artifact.
If VectorFL Paper is supposed to inherit Paperclip's progression legibility in
VectorFL terms, the current organ and next candidate must be directly reachable
from the primary surfaces.

## 2. lock

The semi-live route set should expose direct drill-in links from:

- `Current Reading / current responsibility`
- `Current Reading / next candidate strip`
- `Cases / Queue / current organ`
- `Cases / Queue / next candidate`
- contextual organ panel titles

## 3. target rule

The first drill-in mapping is locked as:

- `organ_detail:flow_interpretation` -> `semi_live_organ_detail/current.html`
- `organ_detail:governance` -> `semi_live_organ_detail/governance.html`

## 4. semantic rule

These links do not re-center the app around organ detail.

- primary surface remains primary
- organ detail remains drill-in
- drill-in makes responsibility and bounded status legible
- drill-in does not redefine case meaning

## 5. inheritance reason

This is the structural flow inheritance we actually want from Paperclip:

- current responsibility is visible
- next responsibility is visible
- deeper detail can be opened from the live flow

What is inherited is reachability and progression legibility, not Paperclip
ontology.
