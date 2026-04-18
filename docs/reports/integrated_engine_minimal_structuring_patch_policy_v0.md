# Integrated Engine Minimal Structuring Patch Policy v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This policy decides whether to patch an existing document, add a companion note, or create a new document when recording structuring fields.

## Purpose

Avoid document explosion while still preserving:

- base content trace
- applied lens record
- structural principle
- rollback / boundary
- layer reapplication hint

## Patch Decision Rules

| situation | action | reason |
|---|---|---|
| existing doc already holds the main decision | append structuring fields | Keeps decision and evidence together. |
| existing doc is too role-specific | add companion note | Avoids blurring the original document role. |
| current step is exploratory and unstable | create note, not canonical report | Keeps uncertainty visible. |
| result is rollback-only | save cautionary note, not promoted structure | Preserves failure without overclaim. |
| multiple docs would repeat the same fields | patch the summary/index only | Prevents duplicate authority. |
| a field changes the meaning of a prior doc | create companion note instead of patch | Protects original record. |

## Minimal Field Patch Set

When patching a document, add only what is needed:

- `base_content_trace` if source grounding is missing
- `applied_lens_record` if the reading angle is unclear
- `structural_principle` if the result may transfer later
- `rollback_or_boundary` if overclaim risk exists
- `layer_reapplication_hint` if future line/axis/lens/camera reread is plausible
- `what_this_is_not` if promotion drift is likely

## New Document vs Patch vs Companion Note

| choose | when |
|---|---|
| patch existing doc | small field addition clarifies an existing decision |
| companion note | new interpretation would clutter or alter the original role |
| new doc | a new reusable schema, protocol, matrix, or cross-document guide is needed |
| cautionary note | result is false precedent, rollback-only, or failure trace |

## Review-Stage Alignment

Because current status is not promoted:

- patches must not imply official camera use
- companion notes must say candidate / review / hold where relevant
- rollback-only notes must not count as promotion evidence
- schema fields must not become canonical ingestion fields

## Verification

- document explosion reduced? yes; patch/companion/new/cautionary paths are separated.
- existing authoritative docs duplicated? no.
- patch decision aligned with review-stage status? yes.
- rollback-only saved without promotion? yes.

## Pointers

- Schema: `docs/reports/integrated_engine_structuring_record_schema_v0.md`
- Augmentation plan: `docs/reports/integrated_engine_review_bundle_structuring_schema_augmentation_plan_v0.md`
- Integration summary: `docs/reports/integrated_engine_structuring_archetype_integration_summary_v0.md`
