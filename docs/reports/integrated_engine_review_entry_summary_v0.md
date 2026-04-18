# Integrated Engine Review Entry Summary v0

## Status Verdict

PASS_WITH_NOTE

Current reusable reading-frame state:

```text
camera-candidate review eligible, not promoted
```

This package prepares the review entry.
It does not promote a camera, axis, glossary, or canonical record.

## Why This Package Exists

The reusable reading-frame experiment produced useful evidence:

- transformer1 content-bearing transcript supported the frame.
- transformer2 content-bearing transcript supported a decoder-side variation.
- transformer2 intake note showed rollback is required for intake-note-only assets.
- body/camera/lens internal report showed the frame can transfer to a content-bearing cross-shape internal document.

The next risk is over-promotion.
This package creates recovery, camera-frame, lens, test-pool, and rollback documents so review can proceed without losing boundaries.

## Deliverable Map

| document | role |
|---|---|
| `docs/reports/integrated_engine_process_recovery_checklist_v0.md` | Recoverable execution checklist for probe/review/promotion work. |
| `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md` | Content-neutral C0-C6 provisional camera big frame, not promoted. |
| `docs/reports/integrated_engine_lens_structure_draft_v0.md` | Operational lens draft for what to read and what not to read. |
| `docs/reports/integrated_engine_internal_external_test_pool_matrix_v0.md` | Narrow test pool split into external content-bearing, internal content-bearing, and rollback-only shapes. |
| `docs/reports/integrated_engine_verification_and_rollback_discipline_v0.md` | Rollback signal and evidence-count discipline. |
| `docs/reports/integrated_engine_review_entry_summary_v0.md` | Entry point for the next camera-candidate review. |

## Provisional Camera Big Frame Summary

| slot | role |
|---|---|
| C0. Scope Anchor | Lock the reading range. |
| C1. Processing Tension / Problem Shift | Name the pressure or mismatch that moves the object. |
| C2. Input / State Preparation | Read what must be prepared before the mechanism acts. |
| C3. Selection / Mechanism | Read how information is selected, routed, filtered, weighed, or foregrounded. |
| C4. Output / Representation Result | Read what the process produces as candidate/result/projection. |
| C5. Support / Stability | Read what keeps the process repeatable or stable. |
| C6. Contrast / Limitation / Guard | Attach support, non-goal, limitation, or rollback guard to core segments. |

Current frame name remains provisional.
Do not call it a promoted camera yet.

## Lens Structure Summary

Working lens candidates:

- `scope-reading`
- `processing-tension`
- `preparation-structure`
- `selection-mechanism`
- `output-result`
- `support-placement`
- `rollback-detection`
- `correction-reading`
- `grammar-classification`
- `screen-projection`

Lens rule:

```text
object scope first -> primary lens -> optional secondary lens -> candidate return -> rollback check
```

## Internal / External Test Pool Summary

External content-bearing:

- `inputs/external_cases/choi_ai_classroom_transformer1.txt`
- `inputs/external_cases/choi_ai_classroom_transformer2.txt`

Internal content-bearing:

- `docs/reports/integrated_engine_body_camera_lens_reread_correction_v0.md`
- `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md`
- `docs/reports/gemini_mock_test_structural_analysis_v0.md`

Rollback-only:

- intake-note-only files
- metadata-only files
- pointer-only manifests
- index-only documents

## Verification / Rollback Summary

Always check:

- frame forcing
- scope collapse
- support inflation
- content overgeneralization
- axis drift
- glossary drift
- canonical drift
- low reuse value
- mismatch opacity

If any appears, do not promote.
Rollback to the nearest gate and preserve the failed attempt as data.

## Current Review Boundary

Allowed next:

- camera-candidate review note
- one optional confidence probe using internal content-bearing target
- status lock update

Not allowed next:

- camera promotion
- axis promotion
- glossary
- canonical ingestion
- UI implementation
- broad test pool expansion

## Next Valid Action

Recommended next action:

```text
Open camera-candidate review note for C0-C6 provisional camera big frame.
```

Review scope:

- whether C0-C6 should remain a hold frame
- whether it can become a camera candidate
- what naming changes are needed
- what target-shape boundaries are mandatory
- what rollback rules must be part of the camera if later promoted

Review must end with one of:

- keep hold
- one more probe needed
- eligible for provisional camera candidate

It must not end with direct camera promotion.

## Restart Pointers

Start here, then read in this order:

1. `docs/reports/integrated_engine_review_entry_summary_v0.md`
2. `docs/reports/integrated_engine_process_recovery_checklist_v0.md`
3. `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md`
4. `docs/reports/integrated_engine_lens_structure_draft_v0.md`
5. `docs/reports/integrated_engine_verification_and_rollback_discipline_v0.md`
6. `docs/reports/integrated_engine_internal_external_test_pool_matrix_v0.md`
