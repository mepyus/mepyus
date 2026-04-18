# Integrated Engine Process Recovery Checklist v0

## Status

PASS_WITH_NOTE

This checklist records the reusable reading-frame experiment as a recoverable operating sequence.
It does not promote the frame to a camera, axis, glossary, or canonical record.

## Current Baseline Pointer

- Current frame status: `camera-candidate review eligible, not promoted`
- Current hold frame: `provisional reusable reading-frame hold`
- Current template: `docs/reports/integrated_engine_reusable_reading_frame_probe_result_template_v0.md`
- Current target-shape rule: content-bearing assets only; intake-note-only assets are support objects or rollback-only metadata.

## Recovery Checklist

| step | purpose | input | output | failure signal | rollback method | next-step condition |
|---|---|---|---|---|---|---|
| 1. baseline status lock | Start from the correct current state before opening any work. | Latest status verdict, hold frame, target-shape gate. | Explicit status line: hold / review eligible / promoted. | Work starts from memory or assumes promotion. | Return to status note and mark current frame as `not promoted`. | Status is named before any probe/review starts. |
| 2. target-shape gate 확인 | Prevent applying the frame to assets that cannot test F1-F6. | Candidate target asset. | valid / invalid / rollback-only target decision. | Intake-note-only or metadata-only asset is treated as full probe target. | Reclassify as support object or asset-specific metadata. | Target is content-bearing and can test at least 4 of F1-F6. |
| 3. probe target selection | Choose one bounded target without broad scan. | Narrow candidate list, max 3. | One selected target with reason. | Too many targets, broad scan, or target chosen for convenience only. | Reduce to one content-bearing candidate and document why others were not selected. | One valid target is selected. |
| 4. probe execution using fixed template | Keep probes comparable and repeatable. | Selected target + probe result template. | Filled probe result. | Free-form analysis replaces template fields. | Re-run the same target through the fixed template. | F0-F6, content variation, anchor split, support rule, gate update are filled. |
| 5. frame/content separation 판정 | Separate reusable role from asset-specific content. | Probe result. | Frame-level match vs content-level variation table. | Content difference is treated as frame failure, or frame role is forced over content. | Split role and content again; mark partial/missing where needed. | Mismatch can be named without forcing. |
| 6. rollback signal 확인 | Detect drift before promotion pressure starts. | Probe result + rollback signal list. | rollback signal table. | Frame forcing, support inflation, axis/glossary/canonical drift. | Mark target as rollback-only or keep hold. | No unhandled rollback signal remains. |
| 7. promotion gate update | Update evidence status without promoting automatically. | Probe result + gate table. | Gate status: open / partial / pass. | Gate pass is read as immediate promotion. | Re-state: gate pass allows review, not promotion. | Gate status is explicit and promotion remains closed. |
| 8. current status verdict | Name the exact current phase. | Gate update + rollback signal check. | hold / review eligible / promoted / rollback verdict. | Vague “looks good” verdict. | Re-run status distinction: hold vs review vs promotion. | Exact status is stated in one line. |
| 9. next valid action 결정 | Select the next smallest safe step. | Current verdict. | Next action: hold / probe / review / rollback. | Opening implementation, UI, axis, or glossary too early. | Return to the nearest prior gate. | Next action does not exceed current status. |
| 10. runlog / report / note 저장 | Make the run recoverable later. | Final decision and evidence. | Report/note path and summary. | Work remains only in chat memory. | Create or update a bounded report. | Next reader can restart from the note. |

## Recovery Routes

| if this happens | return to |
|---|---|
| target is metadata-only | Step 2. target-shape gate |
| template fields cannot be filled | Step 4. probe execution using fixed template |
| frame/content distinction collapses | Step 5. frame/content separation |
| support becomes a center | Step 6. rollback signal check |
| gate pass is mistaken for promotion | Step 7. promotion gate update |
| next action opens implementation | Step 9. next valid action |

## Current Locked Reading

The current experiment is not a camera promotion.
It is a recoverable review path for deciding whether the held F0-F6 frame can become a camera candidate later.

## Pointers

- Camera big frame draft: `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md`
- Lens draft: `docs/reports/integrated_engine_lens_structure_draft_v0.md`
- Test pool matrix: `docs/reports/integrated_engine_internal_external_test_pool_matrix_v0.md`
- Verification and rollback: `docs/reports/integrated_engine_verification_and_rollback_discipline_v0.md`
- Review entry summary: `docs/reports/integrated_engine_review_entry_summary_v0.md`
