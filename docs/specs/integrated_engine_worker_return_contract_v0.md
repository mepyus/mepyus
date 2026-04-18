# Integrated Engine Worker Return Contract v0

## 1. Purpose

This contract reduces dependence on post-hoc parsing.

The operating spine already stores CLI sessions, event ledger entries, package notebooks, and enriched RunRecords. The remaining weak point is that RunRecord enrichment has to recover meaning from raw worker text. This note defines the stable worker return shape that the runtime should prefer when available.

## 2. Contract Shape

The bounded worker return payload is:

- `schema_version`
- `worker_id`
- `package_id`
- `run_kind`
- `answer`
- `findings[]`
- `files_artifacts[]`
- `next_continue_hint`
- `open_questions[]`
- `risks_or_limits[]`
- `source_refs[]`
- `raw_fallback_text`

Current schema version:

- `integrated_engine_worker_return_v0`

## 3. Runtime Boundary

Current path:

`worker stdout/stderr -> structured_return.json -> RunRecord enrichment -> package notebook`

Target path:

`worker return payload -> structured_return.worker_return -> RunRecord enrichment -> package notebook`

The parser remains only as compatibility fallback for older or raw-only runs.

## 4. Primary / Fallback Rule

RunRecord projection should read in this order:

1. `structured_return.worker_return`
2. compatible top-level structured return fields if present
3. fallback extraction from `result_summary`
4. raw summary fallback

This keeps old sessions readable while making new sessions less format-sensitive.

## 5. What This Does Not Solve

This contract does not implement:

- multi-agent orchestration
- worker switching UX
- streaming terminal
- artifact viewer
- automatic line / axis detection
- cross-package automation
- universal schema for every future tool

## 6. Validation Standard

PASS requires:

- new worker/session returns include `worker_return`
- package notebook uses `answer/findings/files_artifacts/next_continue_hint`
- old runs without `worker_return` still read through fallback projection

PASS_WITH_NOTE is appropriate if real external worker output still needs normalization before it can emit the contract directly.
