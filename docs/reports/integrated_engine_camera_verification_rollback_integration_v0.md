# Integrated Engine Camera Verification / Rollback Integration v0

## Status

PASS_WITH_NOTE

This document integrates verification and rollback into the provisional camera candidate usage flow.
It does not promote the camera.

## Signal Table

| signal | signal meaning | where likely appears | detection question | immediate action | rollback destination | counts toward promotion evidence? | note format to save |
|---|---|---|---|---|---|---|---|
| frame forcing | C0-C6 is applied where target cannot support it. | intake-note-only, metadata-only, missing C1-C6. | Am I inventing a slot? | stop slot fill | target-shape gate / asset-specific metadata | no | `frame_forcing: target lacks content-bearing body` |
| scope collapse | C0 frame-role and content-role are mixed. | scope treated as universal content. | Did anchor content become the frame? | split scope frame/content | C0 scope anchor check | only if corrected | `scope_split: frame-role / content-role` |
| support inflation | support/guard/limitation becomes center. | must-not, conflicts, limitations. | Is support replacing core reading? | reattach support | C6 support placement | yes if corrected | `support_attached_to: C?` |
| content overgeneralization | asset-specific content becomes general camera rule. | encoder/decoder/report differences flattened. | Did content become frame? | separate frame/content | frame/content separation | yes if visible | `variation: acceptable / breaks frame` |
| axis drift | repeated fit treated as axis. | strong reusable pattern appears. | Did we promote a theme? | close axis route | promotion gate update | frame evidence only | `axis_closed: true` |
| glossary drift | names become final vocabulary. | C-slot/lens names polished as terms. | Did wording become glossary? | mark provisional | lens draft / candidate boundary | yes if corrected | `glossary_closed: true` |
| canonical drift | review material treated as official camera. | gate pass read as promotion. | Did review become promoted? | restate status | status distinction | yes if corrected | `not_promoted: true` |
| low reuse value | frame creates more confusion than asset-specific reading. | probe feels heavier than target. | Did camera help? | keep asset-specific | target-specific rollback | no | `reuse_value: low` |
| mismatch opacity | unclear which slot failed. | vague partial verdict. | Can I name the failed slot? | re-run template | probe result template | no | `rerun_template_required: true` |

## Stop Immediately Conditions

Stop if:

- target is not content-bearing
- C1-C6 would be mostly invented
- C3 mechanism has to be forced
- support becomes the center
- output is being treated as canonical
- axis/glossary/canonical route opens

## Continue With Partial Conditions

Continue with partial if:

- target is content-bearing
- C0 is clear
- at least four of C1-C6 can be judged
- mismatch is visible
- C3 can be marked partial without forcing
- support can be attached to a core slot

## Rollback But Keep Evidence Conditions

Rollback but keep evidence if:

- intake-note-only target revealed scope/source usefulness
- cross-shape target exposes a naming weakness
- C3 partial shows selection/mechanism is too broad
- support inflation appears but is diagnosable
- low reuse value is clear and useful for target-shape boundary

## Procedure Integration

Run this check at usage procedure steps:

- Step 2 target-shape gate: frame forcing, content-bearing failure
- Step 5 apply C0-C6: scope collapse, content overgeneralization, C3 forcing
- Step 7 detect rollback signals: all signals
- Step 8 result type: canonical, axis, glossary drift
- Step 10 save note: note format must capture signal and rollback destination

## Required Verification

- signal explanations concrete? yes
- linked to usage procedure? yes
- rollback destination explicit? yes

## Pointers

- Usage procedure: `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md`
- Review bundle summary: `docs/reports/integrated_engine_provisional_camera_review_bundle_summary_v0.md`
