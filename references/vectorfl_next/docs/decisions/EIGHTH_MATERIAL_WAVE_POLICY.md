# Eighth Material Wave Policy

## Intent

The eighth material wave does not widen space again.
It lets the newly opened reflective terrain accumulate its own continuity.

## Why this step exists

After the seventh wave, the reflective terrain exists but only as a fresh relocation.
This wave lets that terrain hold itself once before any future adjacency is considered.

## Rules

- Reuse the reflective pressure signature from the seventh terrain.
- Keep the family as `seed-seventh-wave`.
- Add a fresh material, trace, pressure profile, and reentry seed.
- Reuse the existing reflective cell when the pressure matches.
- Reactivate that cell with `thickening`.
- Do not create an additional bridge.
- Do not create another terrain component.

## Contract notes

- new terrain should first learn self-continuity before wider adjacency
- bridge count must stay unchanged during this wave
- terrain growth still happens through material reentry, not topology collapse

## Expected reread outcome

- thickening count increases
- bridge count remains one
- terrain component count remains three
- the reflective terrain gains its first internal continuity
