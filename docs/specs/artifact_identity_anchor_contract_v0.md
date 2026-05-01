# Artifact Identity Anchor Contract v0

## Purpose

This contract defines a bounded inline identity anchor for generated/runtime/JSON/contract artifacts. It does not create a global provenance graph. It lets an artifact state enough about itself to support future pairing and diff.

## Identity Anchor Fields

- `artifact_id`: local artifact identifier, normally filename stem.
- `artifact_role`: role such as question packet, exploration result, merge diff report, reingress record, runtime contract, generated artifact, or comparison candidate.
- `family_key`: provisional normalized family key.
- `lineage_hint`: compact phase/run/role hint.
- `run_stem`: run-level stem when available.
- `phase_label`: phase marker when available.
- `artifact_slot`: logical slot such as report family slot or run artifact slot.
- `generated_from_ref`: upstream artifact that generated this one.
- `prior_artifact_ref`: direct prior artifact in the local handoff chain when available.
- `comparison_ready`: whether the artifact can reasonably be considered in comparison.
- `identity_confidence`: weak, plausible, or strong identity.
- `identity_basis`: why the identity was assigned.
- `identity_anchor_source`: whether identity was embedded or inferred.

## Provisional Identity Confidence

- `weak_identity`: role/family cannot be inferred safely.
- `plausible_identity`: role or family can be inferred, usually from path/stem.
- `strong_identity`: emitted artifact has role, run, and phase context.

## Interpretation

`family_key` alone is not enough. Role, slot, and lineage hint explain what kind of sameness is being claimed. Two artifacts can share a path family but occupy different logical roles.

`generated_from_ref` and `prior_artifact_ref` matter because they make the local handoff chain visible without requiring a full provenance graph.

Identity confidence is different from pair confidence. Identity confidence describes one artifact. Pair confidence describes a relationship between two artifacts.

## Validation

- The anchor is inline and additive.
- It remains compatible with grounded, structured, diff, and pairing fields.
- Weak identity fallback is preserved.
- No final taxonomy lock is implied.
