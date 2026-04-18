# Integrated Engine Review-Stage Second Shadow-Fit Candidate Scan v0

## 1. Purpose

This scan selects one second review-stage-adjacent candidate for shadow-fit validation.

This is not rollout.
This is not patching.
This is not camera promotion.

## 2. Candidate Set Considered

| candidate | considered because | decision |
|---|---|---|
| `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md` | Same C0-C6 review-stage zone; contains explicit steps, rollback destinations, partial/missing handling, C3 forcing guard, candidate/canonical boundary, and save report/runlog step. | selected |
| `docs/reports/integrated_engine_provisional_camera_review_bundle_summary_v0.md` | Same bundle; summarizes status, allowed/blocked actions, authoritative documents, and next valid action. | rejected for second test because it is a bundle summary and may shadow-fit by summary wording rather than field-level structure |
| `docs/reports/integrated_engine_lens_slot_compatibility_matrix_v0.md` | Same lens/camera zone; has lens-slot mapping and verification questions. | rejected because it is matrix/spec-like, not review-stage note-like enough for this repeatability test |
| `docs/reports/integrated_engine_camera_verification_rollback_integration_v0.md` | Adjacent rollback discipline document. | not selected because current package needs a second candidate distinct from boundary but still close to usage/review; procedure is closer and more inspectable |

## 3. Selected Candidate

Selected candidate:

- `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md`

## 4. Why It Is The Best Second Test Target

The selected candidate is distinct from the first weak-fit case:

- first candidate was a usage boundary document
- second candidate is a usage procedure document

It is still review-stage adjacent because it keeps:

- `eligible for provisional camera candidate, not promoted`
- review-stage procedure language
- rollback points
- candidate/canonical distinction
- C3 mechanism forcing guard
- save report / note / runlog step

This makes it a meaningful repeatability test for whether the micro-template can fit more than a boundary table.

## 5. Phase 1 Validation

Review-stage adjacency:

- yes, the candidate is in the same C0-C6 provisional camera review-stage zone

Distinctness from first weak-fit case:

- yes, it is procedural rather than boundary-table centered

Rollout implication:

- none; this scan selects a shadow-fit target only

Status remains:

```text
eligible for provisional camera candidate
not promoted
```

