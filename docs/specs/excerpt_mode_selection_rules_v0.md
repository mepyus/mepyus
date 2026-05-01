# Excerpt Mode Selection Rules v0

## Status

- phase: `phase1_7_excerpt_quality_tuning`
- authority: `working_spec`

## Execution

Mode selection remains rule-based:

- Markdown specs/guides/reports: prefer `heading_plus_block`, but widen if the block is title-only.
- Bullet-heavy sections: use `bullet_cluster`, with adjacent siblings when a single bullet is too thin.
- JSON/runtime artifacts: use `line_window`, with strict character clipping.
- Empty, unreadable, missing, or noisy files: use `pointer_only`.

Retry order:

1. initial mode from document shape;
2. quality check;
3. if poor and recoverable, widen within the same section;
4. if still poor, try paragraph or line window;
5. if unsafe/noisy/unreadable, fallback to pointer-only.

## Interpretation

This is bounded tuning, not a parser rewrite. The goal is to avoid obvious bad excerpts while keeping artifacts small and predictable.

## Validation

- Title-only capture should decrease.
- Excerpts should not grow without limits.
- Pointer fallback remains available.
