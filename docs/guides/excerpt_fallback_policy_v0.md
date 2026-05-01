# Excerpt Fallback Policy v0

## Execution

Use `pointer_only` fallback when:

- file does not exist;
- file is binary or unreadable as text;
- file is too large for bounded extraction;
- no non-empty block can be found;
- extraction would produce an overlong or misleading excerpt.

Fallback fields:

- `pointer`: path
- `excerpt_window`: empty string or short failure note
- `excerpt_mode`: `pointer_only`
- `grounding_status`: `pointer_only`
- `local_confidence`: `low`
- `why_it_matters`: keep the selected asset reason

## Interpretation

Fallback is not failure. It is honest evidence depth reporting. The loop can still proceed, but merge/diff/hold should know that the evidence basis is thin.

## Validation

- The usage loop continues.
- The thinness is visible.
- Reingress can record weak grounding areas for the next run.
