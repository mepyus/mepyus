# Integrated Engine Review-Stage Structuring Micro-Template v0

## 1. Purpose And Boundary

This is a bounded review-stage micro-template.

It is derived from the validated structure in:

- `docs/reports/integrated_engine_provisional_camera_candidate_review_note_v0.md`
- `docs/reports/integrated_engine_structuring_patch_operational_validation_note_v0.md`
- `docs/reports/integrated_engine_rollback_rule_reread_revalidation_note_v0.md`

It is not a global engine template.
It is not a camera promotion path.
It is not a schema rollout instruction.

Allowed use:

- review-stage document inspection
- one bounded review-stage document at a time
- supervisor-readable grounding and boundary check

Forbidden use:

- camera promotion
- broader schema rollout
- automatic reuse across documents
- line / axis / camera-slot validation
- canonical ingestion
- UI implementation
- automation

## 2. Micro-Template Fields

### `object_of_structuring`

What is being structured in this review-stage note?

Required content:

- target review-stage object
- current status
- whether the object is candidate, hold, rollback-only, or not-promoted

Do not use this field to create a new object class.

### `action_of_structuring`

What review-stage action is being performed?

Allowed actions:

- validate
- review
- consolidate
- boundary-check
- shadow-fit
- hold

Do not use this field for promotion, canonicalization, or rollout.

### `base_content_trace`

What material grounds the judgment?

Minimum content:

- source document or source bundle
- prior evidence or probe result if present
- rollback or boundary material if used
- reason the trace is sufficient for review-stage reread

Thin trace is allowed only if it is clearly marked.

### `applied_lens_record`

What reading angle shaped the review?

Minimum content:

- primary lens or review angle
- supporting lens if present
- how the lens shaped the judgment

Do not write only "reviewed."

### `structural_principle`

What rule turned the base content into a review-stage judgment?

Minimum content:

- what must travel together
- what status separation must be preserved
- what does not follow from the judgment

This must be a shaping principle, not a summary.

### `layer_reapplication_hint`

What future reread path is visible, if any?

Allowed content:

- bounded hint
- evidence requirement before use
- explicit statement that hint is not approval

Do not use this field as promotion language.

### `what_this_is_not`

What overreading must be blocked?

Minimum content:

- not promoted
- not canonical
- not rollout
- not broader validation
- not automatic reuse

This field must protect the document's original authority.

## 3. Optional Bounded Block: Rollback Cue Consolidation

Use this only when rollback cues already exist in the note.
Do not invent rollback logic.

### `rollback cue grouping`

Group already-present cues such as:

- target-shape rollback
- lens rollback
- judgment rollback
- authority rollback

### `rollback reread boundary`

State:

- rollback reread is review-stage only
- it does not create an independent rollback protocol
- it does not authorize promotion, rollout, or line / axis / camera-slot validation

## 4. Minimal Fill Skeleton

```text
object_of_structuring:

action_of_structuring:

base_content_trace:

applied_lens_record:

structural_principle:

layer_reapplication_hint:

what_this_is_not:

optional rollback cue consolidation:
  rollback cue grouping:
  rollback reread boundary:
```

## 5. Review-Stage Self-Check

- current status preserved?
- target note authority preserved?
- review guideline reread checked?
- rollback rule reread checked only if cue exists?
- no promotion implied?
- no broader schema rollout implied?
- no automatic reuse implied?

