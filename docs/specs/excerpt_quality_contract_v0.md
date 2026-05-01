# Excerpt Quality Contract v0

## Status

- phase: `phase1_7_excerpt_quality_tuning`
- authority: `working_spec`
- compatibility: additive to Phase 1.6 evidence fields

## Execution

Quality criteria:

- `relevance`: excerpt contains text related to the evidence reason, not only the file title.
- `sufficiency`: excerpt includes enough local context to support `why_it_matters`.
- `non_triviality`: excerpt is not only a heading, metadata pair, or isolated label.
- `boundedness`: excerpt remains short enough for artifact review.
- `fidelity`: excerpt preserves source wording without synthetic paraphrase.

Excerpt quality labels:

- `poor`: title-only, metadata-only, empty, noisy, or too short to support the reason.
- `usable`: bounded excerpt has relevant local context, but may need human review.
- `strong`: bounded excerpt directly includes the operative rule, list, or definition needed by the reason.

## Interpretation

Excerpt quality is not a length contest. A strong excerpt can be short when it contains a direct rule. A long excerpt can still be poor if it is generated noise or misses the relevant block.

`title_only` should not be `usable` because it proves only that the file exists and has a title. It does not show the evidence relation. Strong excerpts are those that make `why_it_matters` inspectable without forcing the reader to open the source immediately.

## Validation

- Quality labels are simple enough for runtime artifacts.
- Labels do not replace `grounding_status`.
- Current grounded contract remains compatible.
