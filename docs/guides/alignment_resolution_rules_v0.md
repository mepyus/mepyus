# Alignment Resolution Rules v0

## Execution

Resolution order:

1. Apply `source_authority_ladder_v0.md`.
2. Separate direct conflict from scope difference.
3. Check whether the difference changes Phase 1 goal/non-goal.
4. If not, choose `merge` with notes.
5. If yes but no user-only choice is needed, choose `diff`.
6. If authority, destructive change, operating philosophy, or naming lock requires user choice, choose `hold`.

Do not:

- promote Codex reasoning over locked baseline;
- erase lower-authority tension;
- use hold just because evidence is thin;
- use merge when a high-authority contradiction remains unresolved.

## Interpretation

Alignment is not sameness. Two sources can align while using different language if their operational effect is the same. Diff is useful when the operational effect differs but no immediate decision is required. Hold is reserved for places where continuing would silently change the space.

## Validation

- hold remains narrow.
- difference is preserved.
- authority is explicit.
