# Integrated Engine Verification and Rollback Discipline v0

## Status

PASS_WITH_NOTE

This document defines verification and rollback discipline for reusable reading-frame review.
It does not promote a camera, axis, glossary, or canonical record.

## Core Rule

Rollback is not failure disposal.
Rollback is the way to preserve evidence while preventing over-promotion.

## Rollback Signal Table

| signal | what it means | where it appears | immediate action | rollback destination | counts toward promotion evidence? |
|---|---|---|---|---|---|
| frame forcing | The frame is being applied where the target cannot support it. | Intake-note-only assets, missing C1-C6 body, forced segment fill. | Stop probe expansion and mark target as invalid/rollback-only. | target-shape gate; asset-specific metadata record. | no |
| scope collapse | Scope anchor frame-role and content-role are mixed. | Scope content treated as universal frame content. | Split anchor into frame-role and content-role. | C0 scope anchor check. | only if corrected and evidence-bearing |
| support inflation | Contrast, guard, limitation, or support note becomes the center. | Must-not list, limitation note, generation strategy, support panel. | Reattach support to the core segment it protects. | C6 support placement check. | yes if corrected; no if unresolved |
| content overgeneralization | Asset-specific content is treated as general frame rule. | Encoder content applied to decoder, transformer content applied to engine report. | Separate frame-level match from content-level variation. | frame/content separation step. | yes if separation remains visible |
| axis drift | Repeated segment fit is treated as an axis promotion. | Strong reusable pattern appears across assets. | Mark axis promotion closed and retain as review evidence only. | promotion gate update. | yes as frame evidence, not axis evidence |
| glossary drift | Segment names become final terms or user-facing copy. | Lens/camera names used as final glossary. | Mark terms provisional and non-final. | lens draft / camera frame draft. | yes if not used as glossary |
| canonical drift | Hold/review material is treated as official camera/canonical record. | Gate pass read as promotion; report used as canonical. | Restate exact status: review eligible, not promoted. | status distinction / review entry summary. | yes if status is corrected |
| low reuse value | Frame application does not make reading faster or clearer. | Probe creates more confusion than asset-specific reading. | Keep asset-specific structure or hold frame. | target-specific rollback. | no, unless it clarifies invalid shape rule |
| mismatch opacity | It is unclear which segment failed or why. | Vague "partially fits" without segment table. | Re-run using fixed probe template. | probe result template. | no until clarified |

## Verification Sequence

1. Confirm target shape.
2. Apply C0-C6 only if target is content-bearing.
3. Fill frame-level match table.
4. Fill content-variation table.
5. Run scope anchor split check.
6. Run support placement check.
7. Check rollback signals.
8. Update promotion gate without promoting.
9. State exact current status.

## Evidence Count Rule

Include a probe in promotion evidence only when:

- target is content-bearing
- C0-C6 can be tested by evidence
- mismatches are visible
- support placement can be checked
- rollback signals are absent or handled

Exclude a probe when:

- target is intake-note-only
- segment fill would be invented
- only C0 scope anchor can be tested
- support placement cannot be tested
- frame forcing is unresolved

## Rollback Destinations

| destination | use when |
|---|---|
| target-shape gate | asset is not content-bearing |
| asset-specific metadata | intake note / pointer-only / metadata-only asset |
| frame/content separation | content differs but role may still match |
| support placement check | support becomes too central |
| status distinction | review eligibility is mistaken for promotion |
| lens draft | lens confusion causes wrong reading |
| process recovery checklist | work opens too many steps or loses sequence |

## Current Safe Status

Current reusable reading-frame state:

`camera-candidate review eligible, not promoted`

This means:

- review can open
- promotion cannot happen yet
- camera use procedure is not yet locked
- rollback discipline remains active

## Pointers

- Recovery checklist: `docs/reports/integrated_engine_process_recovery_checklist_v0.md`
- Provisional camera frame: `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md`
- Probe template: `docs/reports/integrated_engine_reusable_reading_frame_probe_result_template_v0.md`
- Test pool matrix: `docs/reports/integrated_engine_internal_external_test_pool_matrix_v0.md`
