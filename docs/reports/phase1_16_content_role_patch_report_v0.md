# Phase 1.16 Content-Role Patch Report v0

## Verdict

`PASS_WITH_NOTE`

Lower-side now emits bounded content-role support without changing readiness or packet schema.

## Files Created or Updated

- `app/core/runtime/lower_support_layers.py`
- `app/work/observer_ingest_min/run_observer_ingest_min.py`
- `app/core/runtime/external_input_comparison.py`
- `scripts/run_transcript_preprocess_comparison.py`
- `scripts/build_lower_support_layers.py`
- `scripts/process_structured_doc_with_routing.py`
- `docs/reports/phase1_16_content_role_patch_report_v0.md`

## What Was Actually Patched

### Observer Ingest Path

Each observer run now writes:

- `content_role_tags_<run_id>.json`

The tagging is derived from current split outputs and keeps:

- `content_role`
- `secondary_role`
- `role_confidence`
- `role_status`
- `role_basis_note`
- `why_this_role`

### Transcript Preprocess Path

Each preprocess comparison now carries:

- `support_layers.content_role_tags`

The transcript comparison runner also writes a companion role-tag file beside the comparison JSON.

## Role Handling

The patch keeps role inference narrow and honest:

- uses a bounded keyword-based taxonomy;
- allows `secondary_role`;
- leaves `unknown` when no bounded signal is strong enough;
- leaves `low` confidence on weak readings;
- does not force every chunk into a strong role.

## Why This Is Bounded

This patch does not:

- rewrite split units;
- expand taxonomy broadly;
- treat role as packet-worthiness;
- turn role into axis or camera judgment.

It only gives lower material a first-pass function signal so upper reading has less blind inference work.

## Validation

- Provenance remains visible beside role tags: `PASS`.
- Role tagging does not change readiness labels: `PASS`.
- Role tagging does not imply upper packet admission: `PASS`.
- Weak/unknown roles remain visible: `PASS_WITH_NOTE`.

## Thin Areas

- heading-only units often remain `unknown`;
- some report titles still over-index toward `transition`;
- directive-style material can be too compact to produce rich role diversity.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: listed above.
3. What was actually patched: lower content-role support emission.
4. What remains unresolved: richer role quality for title-only or dense heading blocks.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: use these role tags as the input layer for line seed bundling.
