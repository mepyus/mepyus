# Integrated Engine Structuring Record Schema v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This schema records structuring work so it can be reread later as line, axis, camera, lens, evidence, learning material, or generation guide.
It does not promote any camera, axis, glossary, canonical record, UI implementation, or automation.

## Schema Principle

Do not record only the resulting structure.
Record:

```text
object + action + base content + target shape + lens + result + principle + risk + boundary + reapplication hint
```

The same schema should work when the object changes from camera candidate to lens draft, line set, axis candidate, rollback pattern, or review rule.

## Fields

| field | definition | why it matters | example content | common misuse |
|---|---|---|---|---|
| `object_of_structuring` | The thing being structured now. | Prevents confusing camera, lens, line, axis, and rollback objects. | camera candidate / lens draft / line set / axis candidate / rollback pattern | Treating all structured outputs as camera work. |
| `action_of_structuring` | The current verb being performed. | Distinguishes extract, classify, vary, review, stabilize, hold, and promote-block. | review / classify / hold / vary / stabilize | Calling review a promotion. |
| `base_content_trace` | The actual content, document, failure, or case that produced the structure. | Keeps structure grounded in source material. | transformer transcript, body/camera/lens correction note, failed panel-first implementation | Recording only abstract result and losing evidence. |
| `target_shape_assumption` | The assumed shape of the target being read. | Prevents applying content-bearing procedures to metadata-only assets. | content-bearing report / transcript / intake-note-only / pointer-only | Ignoring shape and forcing C0-C6. |
| `applied_lens_record` | The lens or lens set used to read the object. | Preserves how the result was seen, not just what was produced. | correction-reading + screen-projection | Treating lens as final glossary label. |
| `resulting_structure` | The structure actually produced by the work. | Captures the output without making it canonical. | C0-C6 candidate, normalized line set, rollback signal table | Treating candidate structure as promoted structure. |
| `structural_principle` | The transferable principle revealed by the work. | Makes the result reusable beyond the local case. | content-bearing target must pass target-shape gate before C0-C6 | Replacing principle with a plain summary. |
| `false_precedent_or_risk` | The plausible but dangerous reading. | Prevents repeated misread. | intake note looks like probe target but is support-only | Silently dropping false precedent. |
| `rollback_or_boundary` | Where to stop and where to return. | Keeps expansion recoverable. | rollback to target-shape gate; mark asset-specific | Treating rollback as failure disposal. |
| `layer_reapplication_hint` | How the result may be reread at another layer later. | Turns current work into future line/axis/lens/camera material without immediate promotion. | line reread, axis hint, lens guide, camera slot clue, review rule | Treating hint as immediate promotion. |
| `what_this_is_not` | Boundary statement to prevent overclaim. | Keeps candidate/review/hold status visible. | not a camera promotion, not glossary, not canonical | Omitting boundary because result looks useful. |
| `next_valid_use` | Where this record can safely be used next. | Connects record to future work without broadening scope. | use in camera-candidate review, source for mining, optional stress-test input | Opening UI or automation from a review note. |

## Minimal Record Template

```text
object_of_structuring:
action_of_structuring:
base_content_trace:
target_shape_assumption:
applied_lens_record:
resulting_structure:
structural_principle:
false_precedent_or_risk:
rollback_or_boundary:
layer_reapplication_hint:
what_this_is_not:
next_valid_use:
```

## Verification

- camera-only? no; fields support camera, lens, line, axis, rollback, and review work.
- object/action reusable? yes; object and verb are explicit fields.
- structural_principle reduced to summary? no; it must state a transferable rule.
- layer_reapplication_hint actionable? yes; it must name a future layer and safe use.

## Pointers

- Archetype note: `docs/reports/integrated_engine_camera_review_as_process_archetype_note_v0.md`
- Augmentation plan: `docs/reports/integrated_engine_review_bundle_structuring_schema_augmentation_plan_v0.md`
- Layer guide: `docs/reports/integrated_engine_layer_reapplication_guide_draft_v0.md`
