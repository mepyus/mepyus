# Structured Merge Diff Rules v0

## Status

- phase: `phase1_8_structured_asset_reading_hardening`
- authority: `working_spec`

## Execution

Structured merge/diff guidance:

- identity-only or shape-only evidence cannot justify strong merge by itself.
- salient field/path evidence can strengthen merge when it has `why_it_matters` and no contradiction.
- diff-heavy questions should surface salient changed or compared paths first.
- structured conflict can increase merge risk but does not become authority conflict unless it changes a locked baseline or stop condition.

Merge report fields:

- `structured_evidence_summary`
- `salient_paths`
- `strongest_structured_support_refs`
- `strongest_structured_tension_refs`
- `shape_vs_meaning_note`
- `structured_merge_risk_note`

## Interpretation

JSON shape alignment is not semantic alignment. Two records can have the same fields while saying different things. Conversely, a small scalar field can carry the decisive state. Structured evidence must carry path, value, and salience.

## Validation

- Merge should not rely only on top-level contract identity.
- Diff should expose path-level reasons.
- Hold should remain narrow.
