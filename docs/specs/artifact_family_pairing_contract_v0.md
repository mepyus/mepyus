# Artifact Family Pairing Contract v0

## Purpose

This contract defines a thin pairing layer for generated/runtime/JSON/contract comparison. It does not replace structured or diff evidence. It runs before diff evidence and records why two artifacts are a reasonable before/after pair.

## Pairing Unit

Minimum fields:

- `source_ref_before`: earlier artifact path.
- `source_ref_after`: later artifact path.
- `asset_kind`: runtime contract, runtime artifact, generated JSON, config JSON, or structured note.
- `family_key`: provisional normalized family identifier.
- `lineage_hint`: observed phase, run, version, timestamp, or path order clue.
- `pairing_basis`: why the pair was selected.
- `pair_confidence`: weak, plausible, or strong pair confidence.
- `ordering_basis`: how before/after ordering was inferred.
- `why_this_pair`: human-readable explanation.
- `rejected_pair_candidates`: candidates considered but not selected.
- `ambiguity_note`: remaining uncertainty.

## Provisional Pair Confidence

- `weak_pair`: no same-family lineage was confirmed; comparison is fallback-grade.
- `plausible_pair`: same family is plausible from path/stem/context, but lineage marker is weak.
- `strong_pair`: same family and ordering are supported by explicit phase, run, or version markers.

## Provisional Pairing Basis

- `shared_stem`
- `shared_contract_family`
- `shared_run_stem`
- `shared_question_context`
- `timestamp_plus_family`
- `explicit_before_after_marker`
- `selected_order_fallback`

## Interpretation

Changed path detection comes after pair selection. A precise delta is still weak if the compared artifacts do not share a family. `family_key` and `ordering_basis` must travel together because same-family evidence and before/after ordering are different claims.

Rejected candidates are not noise. They show whether the comparison was obvious or ambiguous, and they make later reingress useful for repeated comparison questions.

Pair confidence is separate from diff confidence. A pair can be strong while a particular changed path is trivial; a changed path can be salient while the pair remains weak.

## Validation

- The contract is an additive draft layer over Phase 1.9 diff evidence.
- Weak pair fallback is preserved.
- No final taxonomy lock is made.
- No canonical path changes are required.
