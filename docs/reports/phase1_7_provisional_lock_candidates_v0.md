# Phase 1.7 Provisional Lock Candidates v0

## Purpose

Track candidates that are promising but not baseline-ready.

## Promising Candidates

- `excerpt_quality` field.
- `excerpt_retry_count` field.
- `fallback_reason` field.
- `tuning_note` field.
- title-only detection and bounded widening.
- quality summary at exploration/merge/reingress levels.

## Not Ready To Lock

- exact labels `poor`, `usable`, `strong`;
- retry thresholds;
- JSON stress excerpt scoring;
- cross-support scoring combined with excerpt quality.

## Recommendation

Keep Phase 1.7 as working tuning. Reuse it operationally, but do not promote or final-lock the taxonomy.
