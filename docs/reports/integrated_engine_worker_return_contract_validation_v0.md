# Integrated Engine Worker Return Contract Validation v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Tested Package

- package: `pkg_openharness_structure_probe`
- target context: `references/git_search/openharness-main`
- validation run: `cli_20260418T215447Z_e6239bf8`
- legacy fallback run checked: `cli_20260418T214000Z_9d955976`

## 3. Structured Return Presence

The new validation run wrote `runtime/cli_sessions/cli_20260418T215447Z_e6239bf8/structured_return.json` with a `worker_return` payload.

Observed `worker_return` fields:

- `schema_version`
- `worker_id`
- `package_id`
- `run_kind`
- `answer`
- `findings`
- `files_artifacts`
- `next_continue_hint`
- `open_questions`
- `risks_or_limits`
- `source_refs`
- `raw_fallback_text`

The schema version was `integrated_engine_worker_return_v0`.

## 4. Notebook Read Path

The package notebook now reads the latest run from structured return fields before parser inference.

For the OpenHarness package, the latest notebook run exposes:

- answer: source profile for `references/git_search/openharness-main`
- findings: source existence, directory summary, top dirs, top files, marker files
- files/artifacts: session and return artifacts plus extracted refs
- next_continue_hint: reread the latest answer with artifact refs and decide the next package-specific question
- risks/limits: dry-run validates carryover, not worker reasoning quality; reread-target is not approval

This is less dependent on raw output formatting than the previous RunRecord-only parser path.

## 5. Fallback Compatibility

The previous run `cli_20260418T214000Z_9d955976` does not contain `worker_return`.

It still reads through fallback enrichment:

- `result_summary` remains available
- `answer` is extracted
- `findings` are extracted
- artifact refs remain available

This confirms that the new contract did not break older/raw sessions.

## 6. Remaining Weakness

The current dry-run path can emit the contract reliably because it already controls the profile data. Real external CLI runs may still return unstructured prose. In that case, the runtime normalizes the raw output into `worker_return`, but the semantic quality will depend on the raw return.

The exact blockage is not storage or notebook projection. The remaining blockage is worker discipline: real workers should eventually be prompted or wrapped to return the contract fields directly, not merely prose that the runtime normalizes.

## 7. Boundary

This validation did not implement:

- full multi-agent orchestration
- worker switching UI
- new dashboard surface
- advanced artifact viewer
- streaming terminal
- cross-package automation
- automatic line / axis detection

## 8. Final Judgment

The structured worker return contract exists and is threaded through the current runtime path.

Notebook continuity is now less parser-dependent for new runs, while old runs remain readable through fallback parsing. The result is bounded and usable, but real worker output still needs stronger contract discipline before parser dependence disappears completely.
