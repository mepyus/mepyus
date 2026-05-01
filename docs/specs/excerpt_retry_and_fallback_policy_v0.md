# Excerpt Retry And Fallback Policy v0

## Status

- phase: `phase1_7_excerpt_quality_tuning`
- authority: `working_spec`

## Execution

Policy:

- `poor` + recoverable shape -> retry or widen.
- `poor` + noisy/unsafe/unreadable shape -> `pointer_only` fallback.
- `usable` -> keep.
- `strong` -> prefer in evidence summaries.

Additional fields:

- `excerpt_quality`
- `excerpt_retry_count`
- `fallback_reason`
- `tuning_note`

Retry limit:

- maximum 2 bounded retries.

## Interpretation

Retry and fallback mean different things. Retry says the source is readable but the first extraction was low quality. Fallback says the loop should not pretend to have grounded evidence. A poor excerpt can be worse than pointer-only when it gives false confidence.

If `why_it_matters` says the source defines a rule but the excerpt is title-only, the quality label should be `poor` or the extractor should retry. If a bounded retry finds the rule block, the excerpt can become usable or strong.

## Validation

- Retry is capped.
- Fallback reason is visible.
- Evidence artifact becomes more honest.
