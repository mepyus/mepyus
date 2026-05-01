# Structured Mode Selection Rules v0

## Execution

Structured extraction remains bounded:

- Prefer salient node paths over full object dumps.
- If top-level identity is selected first, inspect child/member fields.
- For contracts, prefer fields named `evidence`, `validation`, `mode`, `status`, `required`, `trigger`, `learning`, `summary`, `chosen`, `decision`, `risk`.
- For generated run artifacts, prefer `chosen_mode`, `evidence_depth_summary`, `excerpt_quality_summary`, `structured_evidence_summary`, validation flags, and artifact refs.
- For arrays, select a representative item and summarize shape.
- For large objects, emit shape summary plus up to five salient child nodes.
- If extraction fails, use `pointer_only` or `shape_only` and explain the fallback.

## Interpretation

Full JSON dumping is not better evidence. It makes artifacts large while hiding the important path. A bounded structured reader should show the path, a compact value, and the implication for the current question.

## Validation

- Avoid identity-only evidence when child fields are available.
- Avoid noisy dumps.
- Preserve fallback.
