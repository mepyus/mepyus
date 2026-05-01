# Phase 1.11 Identity Anchor Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Phase 1.10 improved pairing quality, but most identity evidence still came from path, stem, phase, and version heuristics. The next bottleneck is artifact self-description: artifacts should state their role, family, lineage, and run context so future pairing and diff can rely less on external guessing.

## Gap Categories

- `family_inferred_only_from_path`: family is usually normalized from path/stem.
- `lineage_not_declared`: phase/version order is visible in filenames, not embedded in artifacts.
- `run_context_missing`: older runtime artifacts do not always state run stem or phase label internally.
- `role_missing`: artifact role can be inferred from filename, but is not always declared.
- `before_after_marker_missing`: prior/next relation is not explicit in artifact body.
- `same_family_but_weak_self_description`: pairing can be strong by path while identity remains inferred.
- `pairing_needs_external_guess`: comparison still needs helper-side reasoning to justify family.

## Interpretation

Pairing quality depends on identity quality. If artifacts say who they are, pairing can verify family and role from the artifact itself instead of treating filenames as the main source of truth.

This is not a provenance graph. It is a bounded identity anchor: enough role, family, run, and generation-chain context to make generated/runtime comparison more honest.

Identity anchors matter most for same-family comparison, generated artifact lineage questions, hold-trigger comparisons, and ambiguous runtime JSON sets.

## Validation

- Identity gap is separated from pairing heuristic gap: PASS.
- Existing Phase 1.5~1.10 spine can be preserved: PASS.
- No canonical path migration is required: PASS.
- Next contract target is clear: `artifact_identity` plus identity-aware pairing fields.

## Entry Condition For Next Stage

Proceed with inline artifact identity anchors as draft v5 fields. Do not create sidecar metadata as canonical storage and do not final-lock naming.
