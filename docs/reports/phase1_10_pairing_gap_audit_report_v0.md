# Phase 1.10 Pairing Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Stage 1 audit found that Phase 1.9 diff salience works, but pair selection is still the next weak layer. The prior helper could compare JSON artifacts by selected order, which is enough for bounded smoke but not enough for generated/runtime lineage questions.

## Gap Categories

- `same_family_not_confirmed`: diff evidence can be produced before the loop proves that two artifacts belong to the same logical family.
- `wrong_order_pairing`: before/after order can follow selected JSON order instead of phase, version, or lineage markers.
- `nearest_file_bias`: nearby runtime artifacts can be compared even when they occupy different logical slots.
- `timestamp_without_lineage`: time order alone is not enough to prove family continuity.
- `stem_match_but_semantic_mismatch`: a shared stem is useful but can still mask different roles.
- `candidate_pair_ambiguous`: multiple candidate pairs can be plausible; rejected candidates must be visible.
- `comparison_done_on_weak_pair`: salient changed paths are less meaningful when pair confidence is weak.

## Interpretation

Diff salience is only as good as the pair underneath it. A changed path can be technically correct while operationally misleading if the two files are not from the same family, run series, contract lineage, or logical artifact slot.

This is different from Phase 1.9. Phase 1.9 asked whether a changed path matters. Phase 1.10 asks whether the two artifacts should have been compared in the first place.

Pairing quality matters most for questions that ask for before/after behavior, generated artifact version shifts, runtime contract evolution, repeated run comparison, or hold decisions based on comparison conflict.

## Validation

- Pairing gap is separated from diff extraction gap: PASS.
- Existing Phase 1.5 spine can be preserved: PASS.
- No baseline meaning change is required: PASS.
- No canonical runtime path migration is required: PASS.
- Next contract target is clear: family key, pairing basis, pair confidence, ordering basis, rejected candidates.

## Most Urgent Weakness

The most urgent weakness is selected-order pairing. It can produce a good-looking diff on the wrong before/after pair.

## Entry Condition For Next Stage

Proceed to artifact family pairing contract and bounded pairing helper. Treat all names as provisional v0/v4 draft surfaces, not final locks.
