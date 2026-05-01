# Integrated Engine Worker Adapter Prompt Contract Validation v0

## 1. Verdict

PASS_WITH_NOTE

## 2. What Was Implemented

Package 2 added the minimal actual-worker adapter prompt contract.

Implemented behavior:

- prompt asks actual workers for a delimited `WORKER_RETURN_JSON` block
- runtime extracts the block from stdout
- valid block becomes primary `structured_return.worker_return`
- `worker_return_source` records source quality
- fallback normalization remains intact
- notebook projection receives the source label

## 3. Files / Code Path

Main runtime path:

- `app/runtime/vectorfl_integrated_engine_api.py`

Narrow patch points:

- `_cli_session_prompt(...)`
- `_extract_worker_emitted_return(...)`
- `CodexCliAdapter.start_run(...)`
- `_normalize_worker_return(...)`
- `_enrich_run_record(...)`
- `_build_cli_package_notebooks(...)`

UI exposure remains narrow:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- Package Notebook now has a small return source badge.

## 4. Actual Worker Validation

Actual external worker run was executed with Codex CLI.

Successful emitted-block run:

- session: `cli_20260418T223904Z_a8f2ac17`
- status: `done`
- `worker_return_source`: `worker_emitted`
- persisted path: `runtime/cli_sessions/cli_20260418T223904Z_a8f2ac17/structured_return.json`

The persisted `worker_return` contained:

- `answer`
- `findings[]`
- `files_artifacts[]`
- `next_continue_hint`
- `open_questions[]`
- `risks_or_limits[]`
- `source_refs[]`

Notebook projection check:

- package: `pkg_worker_adapter_contract_smoke`
- latest run: `cli_20260418T223904Z_a8f2ac17`
- latest source: `worker_emitted`
- latest answer/findings readable through the package notebook projection

## 5. Fallback Validation

Fallback behavior remains intact.

Observed fallback cases:

- sandbox-blocked actual run: `raw_fallback`
- dry-run/OpenHarness package: `runtime_normalized`
- synthetic raw-only legacy summary: `raw_fallback`

Older sessions without persisted `worker_return` still read through normalization.

## 6. Important Finding

The actual Codex worker did emit the requested JSON block, but the first extractor version failed because it matched `WORKER_RETURN_JSON` mentions inside prose or inside a JSON string.

The extractor was tightened to recognize delimiters only when they appear alone on a line.

This is why the package is `PASS_WITH_NOTE` rather than a stronger operational promotion. The contract works, but delimiter parsing must stay strict.

## 7. Remaining Risks

- Actual workers can still omit the block.
- Actual workers can emit invalid JSON.
- Actual workers can include the block but underfill fields.
- The current validation used Codex only, not Gemini.
- `worker_emitted` proves parseable return shape, not result quality.

## 8. Package 3 Readiness

Package 3 is ready.

Reason:

- actual worker path was exercised
- worker-emitted structured block was extracted
- source label was persisted
- notebook projection read the emitted worker return
- fallback remained intact

Recommended Package 3 focus:

- use the existing continuity package or one adjacent package
- run one real external worker task that does real bounded reading rather than only smoke validation
- verify that the notebook becomes a continuation asset from actual worker content, not merely contract compliance
