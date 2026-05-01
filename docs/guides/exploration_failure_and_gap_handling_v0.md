# Exploration Failure And Gap Handling v0

## Execution

Use these labels:

- `missing_path`: expected file or folder does not exist.
- `missing_authority`: relevant source exists but no clear authority source was found.
- `missing_example`: contract exists but no scenario/example exists.
- `thin_contract`: fields exist but rules are not operational enough.
- `conflict_unresolved`: two sources disagree and authority ladder cannot resolve safely.
- `phase_boundary`: answer would require UI, automation, ontology redesign, or external deep integration.

Handling:

- Do not treat every gap as failure.
- Put gaps in `missing_gaps`.
- Continue when gap is not a stop condition.
- Use `HOLD` only for authority conflict, destructive action, operating philosophy conflict, or user-only naming/meaning decision.

## Interpretation

공간은 숙성 기반이므로 gap은 다음 탐색의 재료다. 실패와 gap을 섞으면 Codex가 자료 부족을 과도한 결론으로 덮거나 불필요하게 멈춘다.

## Validation

- gap reason is explicit.
- stop condition is narrow.
- unresolved items can re-enter as future probe notes.
