# Integrated Engine Layer Reapplication Guide Draft v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This guide explains how records from camera review can be reread later at other layers.
It does not start those layer tasks now.

## Reapplication Principle

Layer reapplication hint is not promotion.
It is a note that says how a record may be reread later if a matching task appears.

## Layer Guide

| layer | what can be reused from current camera-review records | what cannot be directly reused | most useful schema field | distortion risk | first verification question |
|---|---|---|---|---|---|
| line reading | match/partial/missing decisions, evidence-bound slot notes, base content trace. | C0-C6 as line sequence without reread. | `base_content_trace`, `applied_lens_record` | Camera slots become fake line candidates. | Is there evidence span for each line? |
| axis hint reading | repeated structural principles, rollback patterns, target-shape gate recurrence. | axis promotion from one review bundle. | `structural_principle`, `layer_reapplication_hint` | Review pattern becomes axis too early. | Does this recur across independent content-bearing cases? |
| lens design hint | applied lens records, lens-slot fit/weakness, false-positive risks. | final lens registry or glossary. | `applied_lens_record`, `false_precedent_or_risk` | Good lens name hides weak evidence. | What does the lens read and what does it not read? |
| camera slot refinement | naming drift warnings, C3 forcing risk, support placement behavior. | promoted camera slot change. | `resulting_structure`, `rollback_or_boundary` | Slot renamed because one asset was awkward. | Does the slot role remain stable across target shapes? |
| rollback / pattern learning | failure signal traces, rollback destinations, asset-specific endpoints. | rejection or deletion of failed attempts. | `rollback_or_boundary`, `false_precedent_or_risk` | Failure treated as useless. | What did this failure teach and where should it roll back? |
| review-guideline reuse | process recovery sequence, target-shape gate, decision bridge. | universal governance rule. | `structural_principle`, `next_valid_use` | Review guide becomes heavy mandatory ritual for tiny tasks. | Is this task structurally similar enough to need review discipline? |

## Reapplication Notes

### Line Reading

Use current records to know where candidate evidence may exist.
Do not turn slot labels into line text.
Line work needs evidence spans and line-level normalization.

### Axis Hint Reading

Use repeated principles as hints only.
Axis requires recurrence and stronger evidence than a review bundle.
Keep `axis promotion closed` until a separate axis gate opens.

### Lens Design Hint

Use lens records to see whether a task was read through correction, screen projection, grammar classification, or another lens.
Do not finalize lens names from one use.

### Camera Slot Refinement

Use naming drift warnings to improve neutrality.
Do not change slot names unless multiple records show the same friction.

### Rollback / Pattern Learning

Use failures as training data for rollback.
Do not hide false precedent; it prevents repeated mistakes.

### Review-Guideline Reuse

Use the process only when the task has enough structure.
Do not impose full review process on tiny direct applications.

## Verification

- line/axis/lens/camera collapsed into one layer? no.
- reapplication confused with immediate promotion? no.
- layer_reapplication_hint written as future-use guidance? yes.

## Pointers

- Schema: `docs/reports/integrated_engine_structuring_record_schema_v0.md`
- Archetype note: `docs/reports/integrated_engine_camera_review_as_process_archetype_note_v0.md`
- Patch policy: `docs/reports/integrated_engine_minimal_structuring_patch_policy_v0.md`
