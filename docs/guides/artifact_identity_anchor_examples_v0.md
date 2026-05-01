# Artifact Identity Anchor Examples v0

## Question Packet

Expected role: `question_packet`.

Useful anchor:

- `run_stem`: `phase1_11_run_01`
- `phase_label`: `phase1_11`
- `artifact_slot`: `run artifact slot`
- `identity_basis`: `path_plus_role`

## Exploration Result

Expected role: `exploration_result`.

Useful anchor:

- `generated_from_ref`: the question packet path.
- `prior_artifact_ref`: the question packet path.
- `comparison_ready`: true.

## Merge Diff Report

Expected role: `merge_diff_report`.

Useful anchor:

- `generated_from_ref`: exploration result path.
- `artifact_slot`: `report family slot`.
- `family_key`: shared normalized run/role family.

## Weak Identity

Older JSON artifacts without embedded identity may still be read through path/stem inference. They should be treated as `plausible_identity` or `weak_identity`, not as fully self-described artifacts.
