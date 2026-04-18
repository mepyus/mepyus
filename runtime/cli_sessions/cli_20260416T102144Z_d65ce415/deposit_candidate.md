# Integrated Engine CLI Deposit Candidate

- source_session_id: `cli_20260416T102144Z_d65ce415`
- backend_kind: `codex`
- task_type: `reread`
- requested_by_surface: `vectorfl_surface`
- requested_by_page: `app/ui/integrated_engine`
- status: `done`

## Task Purpose
Conversation-mode smoke test: read the stable UI migration note and tell the VectorFL operator what should remain true before the next change.

## Used Context Refs
- `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md`

## Result Summary
- result summary

1. Fixed 3-surface body remains true: the integrated-engine UI is now sourced from `app/ui/integrated_engine`; `gemini/mock_test` remains reference/proposal clay; `runtime` remains for artifacts, manifests, state, and execution returns. This migration does not create package 2, a new surface, or a new engine shape.

2. CLI on-top layer may now operate through the stable app path. The note records a successful read-only Codex session through the stable app proxy, plus successful marking as `validation_target`.

3. Next smallest safe action: hand-check one VectorFL CLI run from the browser at `http://127.0.0.1:5173/`.

- important findings / diffs / outputs

Stable source folder: `app/ui/integrated_engine`.

Important invariants:
- Do not continue feature work in `gemini/mock_test` unless intentionally editing reference material.
- Do not move React/Vite source into `runtime`.
- Do not add Gemini adapter, background runner, or session browsing before the stable Codex path is hand-used.

Validation already noted:
- `npm run build` passed in `app/ui/integrated_engine`.
- served title confirmed as `VectorFL Integrated Engine`.
- stable app proxy to `127.0.0.1:8421` worked.
- real read-only Codex session completed with exit code `0`.

- uncertainty or failure notes

No files were modified. I only reread `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md`.

Remaining uncertainty from the note: browser-click/user-feel validation still needs a human hand-check.

- suggested next use

validation target: run one browser-based VectorFL CLI smoke test from `app/ui/integrated_engine` at `http://127.0.0.1:5173/`.


## Important Diffs / Findings / Outputs
- not separated in package 1 return


## Uncertainty / Failure Notes
- none recorded


## Suggested Next Use
reread_target
