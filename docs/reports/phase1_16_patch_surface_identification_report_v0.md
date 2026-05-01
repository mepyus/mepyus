# Phase 1.16 Patch Surface Identification Report v0

## Verdict

`PASS`

The safest lower patch surface is the generated/companion layer that already sits after split and preprocess compare:

- observer ingest generated bundle;
- transcript preprocess comparison generated bundle;
- structured-doc routing path only through observer output enumeration.

## Selected Patch Surface

| surface | patch form | why safe |
| --- | --- | --- |
| `app/work/observer_ingest_min/generated/*` | generated companion assets | split/source/trace already exist; support layer can be added without rewriting split outputs |
| `app/work/external_input_preprocess/generated/*` | additive support fields + companion assets | preprocess comparison already acts as an emergent line belt and can carry soft support safely |
| `scripts/process_structured_doc_with_routing.py` | output enumeration update only | structured-doc front door already delegates to observer ingest; no new lower logic needed here |

## Read-Only Inputs

The patch reads from:

- `source_manifest_*.json`
- `split_units_*.json`
- `processing_trace_*.json`
- preprocess comparison JSON components

It does not mutate source text, origin maps, receipts, or readiness labels.

## Companion vs Direct Mutation Decision

Chosen pattern:

- observer ingest: write companion/generated assets
  - `content_role_tags_<run_id>.json`
  - `line_seed_bundles_<run_id>.json`
- transcript preprocess comparison:
  - additive `support_layers` inside the comparison payload
  - companion files for direct lower artifact use

This is safer than patching existing `split_units` rows directly because:

- provenance stays visible;
- consumers of current artifacts are not forced to read new fields;
- support layer can remain clearly separate from readiness.

## Interpretation

This surface is safe because it patches the lower organ after split, not at split. That matches the Phase 1.15 decision: middle-layer patch first, split rewrite later if still needed.

The companion/generated approach also protects the bridge minimum. Support assets can exist and be useful without automatically becoming packet-worthy.

## Validation

- Current lock is preserved: `PASS`.
- Bridge minimum is not redefined: `PASS`.
- Existing lower outputs remain readable on their own: `PASS`.

## Stage Closeout

1. Verdict: `PASS`
2. Files created: `docs/reports/phase1_16_patch_surface_identification_report_v0.md`
3. What was actually patched: safe lower-side patch surfaces were selected.
4. What remains unresolved: whether future support layers should stay companion-only or become inline for some families.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: patch observer/preprocess outputs with role and seed support layers.
