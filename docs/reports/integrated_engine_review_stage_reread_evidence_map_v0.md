# Integrated Engine Review-Stage Reread Evidence Map v0

## 1. Purpose

This evidence map shows where the current reread support comes from inside:

- `docs/reports/integrated_engine_provisional_camera_candidate_review_note_v0.md`

It is a supervisor inspection aid.
It does not add new validation and does not promote the camera.

## 2. Target Review Note Evidence Map

| support area | target note location / passage | what it supports | bounded result |
|---|---|---|---|
| `base_content_trace` | `## 3A. Minimal Structuring Schema Patch` / `base_content_trace` | Grounds the review in the C0-C6 big frame, recovery checklist, lens draft, internal/external test pool, rollback discipline, review entry summary, two transformer transcripts, decoder-side variation, intake-note-only rollback case, and internal body/camera/lens correction report. | supports review-stage grounding |
| `applied_lens_record` | `## 3A` / `applied_lens_record` | Names camera-candidate review lens plus target-shape boundary, frame/content separation, rollback-detection, and lens-slot compatibility lenses. | supports lens-explicit reread |
| `structural_principle` | `## 3A` / `structural_principle` | States that content-bearing evidence, target-shape boundary, lens compatibility, and rollback discipline must travel together; gate pass is review permission, not promotion. | supports review guideline reread |
| `layer_reapplication_hint` | `## 3A` / `layer_reapplication_hint` | Names bounded future reread hints and explicitly identifies rollback/review layer as a review guideline path for `eligible`, `not promoted`, and `rollback-only`. | supports review-stage reread only |
| `what_this_is_not` | `## 3A` / `what_this_is_not` | Blocks camera promotion, axis promotion, glossary lock, canonical ingestion, UI implementation, automation, and invalid target-shape overuse. | supports authority boundary |
| rollback cue consolidation | `## 3A` / `Bounded Rollback Cue Consolidation` | Groups target-shape rollback, lens rollback, judgment rollback, and authority rollback into one local bounded structure. | supports rollback rule reread directly inside review-stage |
| review guideline support | `structural_principle`, `layer_reapplication_hint`, `what_this_is_not`, `Current Review Verdict`, `Why Immediate Promotion Is Still Blocked` | Keeps review eligibility distinct from promotion and makes review guideline reread directly inspectable. | `directly` |
| rollback rule support | `Bounded Rollback Cue Consolidation`, `what_this_is_not`, `Blockers`, `Why Immediate Promotion Is Still Blocked`, `3-Surface Projection` | Makes rollback cue grouping local enough for direct review-stage rollback reread. | `directly` |

## 3. Specific Grounding Path

Review guideline reread grounding path:

```text
base_content_trace
-> applied_lens_record
-> structural_principle
-> layer_reapplication_hint
-> what_this_is_not
-> current verdict / immediate promotion blocked
```

Rollback rule reread grounding path:

```text
base_content_trace
-> applied_lens_record with rollback-detection
-> structural_principle preserving partial/missing and rollback destinations
-> Bounded Rollback Cue Consolidation
-> what_this_is_not
-> immediate promotion blocked
```

## 4. Phase 1 Validation

Grounding check:

- evidence map is grounded in actual review-note material
- no exact line numbers are required for supervisor inspection because section-level locations and passage names are specific

Scope check:

- the map does not introduce line, axis, camera-slot, rollout, or promotion validation

Status check:

```text
eligible for provisional camera candidate
not promoted
```

