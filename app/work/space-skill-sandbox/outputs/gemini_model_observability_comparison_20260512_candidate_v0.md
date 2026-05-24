# Gemini Model Observability Comparison 2026-05-12 Candidate v0

## 1. Status

```text
Document = model observability comparison
Status = CANDIDATE_SETUP_SUPPORT
Authority = observed smoke-test evidence only
Not baseline
Not official workflow
Not model policy
Not automation
Not current-position update
```

## 2. Smoke Tests Compared

### gemini-2.5-flash

```text
Outbox:
  app/work/space-skill-sandbox/relay/outbox/smoke_model_observability_20260512_gemini_outbox_20260512_222811.md

requested_model:
  gemini-2.5-flash

duration_seconds:
  21

likely_state:
  model_capacity_or_quota

stderr:
  429 / MODEL_CAPACITY_EXHAUSTED retry traces

result:
  GEMINI_SMOKE_OK
```

### gemini-3-flash-preview

```text
Outbox:
  app/work/space-skill-sandbox/relay/outbox/smoke_model_observability_gemini_3_flash_preview_20260512_gemini_outbox_20260512_223140.md

requested_model:
  gemini-3-flash-preview

duration_seconds:
  10

likely_state:
  no_known_issue

stderr:
  Ripgrep is not available. Falling back to GrepTool.

result:
  GEMINI_SMOKE_OK
```

## 3. Observed Judgment

```text
gemini-3-flash-preview looked faster and cleaner in this smoke test.
```

Candidate operational preference:

```text
Use --model gemini-3-flash-preview for the next Gemini worker packet unless there is a specific reason not to.
```

## 4. What This Does Not Prove

```text
It does not prove gemini-3-flash-preview is better for all tasks.
It does not prove quality is higher.
It does not remove the need to inspect stderr, duration, completion condition, and evidence depth.
It does not create a model-selection policy.
```

## 5. Watch

```text
single smoke test becomes global model rule
speed is mistaken for depth
clean stderr is mistaken for quality
preview model behavior changes without notice
```

`STATUS: GEMINI_MODEL_OBSERVABILITY_COMPARISON_PREPARED_WITH_WATCH`
