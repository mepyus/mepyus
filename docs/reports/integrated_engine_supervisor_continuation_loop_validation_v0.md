# Integrated Engine Supervisor Continuation Loop Validation v0

## 1. Verdict

PASS

## 2. Selected Packages

Primary package:

- `pkg_openharness_structure_probe`
- reason: it contains actual continuity work from Package 3, including two `worker_emitted` runs and earlier normalized/parser-derived runs.

Secondary bounded example:

- `pkg_worker_adapter_contract_smoke`
- reason: the primary package does not honestly contain a failed/raw run. The smoke package contains `worker_emitted`, `parser_fallback`, and `raw_fallback failed` states, so it is the thinnest honest way to test rerun/hold/inspect decisions.

No new worker run was performed.

## 3. Supervisor Judgment Inventory

### Primary: `pkg_openharness_structure_probe`

Observed notebook shape:

- run count: `8`
- latest run: `cli_20260418T224608Z_681737e8`
- latest source: `worker_emitted`
- latest status: `done`
- earlier sources include `runtime_normalized` and `parser_fallback`

Latest notebook evidence:

- answer summarizes OpenHarness worker/session boundary lessons for VectorFL
- findings identify CLI entrypoints, `QueryEngine.submit_message`, `run_query`, tool validation, permission checks, and VectorFL `CodexCliAdapter.start_run`
- files/artifacts include Step A structured return, operator report, stdout, and bounded OpenHarness source refs
- risks say this was source inspection only, not behavioral runtime tracing
- next hint points to Package 4 normalization validation

This package supports:

- `continue`
- `close`
- some `inspect`

It does not honestly test:

- failed `hold`
- failed/environment `rerun`

### Secondary: `pkg_worker_adapter_contract_smoke`

Observed notebook shape:

- run count: `3`
- latest run: `cli_20260418T223904Z_a8f2ac17`
- latest source: `worker_emitted`
- earlier run: `parser_fallback`
- failed run: `raw_fallback`, status `failed`, route `hold`

Failure evidence:

- failed session `cli_20260418T223716Z_70343339`
- source: `raw_fallback`
- status: `failed`
- answer preserves permission/thread-start error text
- finding says worker run failed and artifacts should be inspected
- risks include no reliable findings, failed execution status, and exit code `1`

This package supports:

- `hold`
- `rerun`
- `inspect`

## 4. Minimal Supervisor Decision Protocol

The usable minimum read set is:

- package title / id
- run count
- latest status
- `worker_return_source`
- route label
- answer
- findings
- files/artifacts
- next continue hint
- risks/limits
- source refs

These fields are enough to make most decisions without opening raw logs.

Raw logs are only required when:

- status is failed
- source is `raw_fallback`
- parser fallback output is too thin
- artifact quality itself is disputed

## 5. Validation Result By Action

### Continue

Package evidence:

- `pkg_openharness_structure_probe`
- latest run `cli_20260418T224608Z_681737e8`
- source `worker_emitted`
- answer and findings are concrete
- next hint names a bounded Package 4 validation direction

Notebook-only judgment:

- sufficient

Decision:

- continue is justified when the next bounded package is normalization hardening or follow-up validation.

Raw logs required:

- no

### Hold

Package evidence:

- `pkg_worker_adapter_contract_smoke`
- failed run `cli_20260418T223716Z_70343339`
- source `raw_fallback`
- status `failed`
- route `hold`
- risks include failed execution and exit code `1`

Notebook-only judgment:

- sufficient to hold

Decision:

- hold is justified until execution environment or worker launch boundary is understood.

Raw logs required:

- not for the hold decision itself; yes if diagnosing the exact environment failure.

### Rerun

Package evidence:

- `pkg_worker_adapter_contract_smoke`
- failed/raw run followed by later successful `worker_emitted` run
- failed run appears environment/launch related, not package-goal invalidation
- bounded context refs remain available

Notebook-only judgment:

- sufficient to decide rerun is appropriate

Decision:

- rerun is justified when the package goal remains valid and the previous failure is execution/format-related.

Raw logs required:

- optional for diagnosis; not required to decide that a rerun is the right next action.

### Inspect

Package evidence:

- `pkg_worker_adapter_contract_smoke` failed run has `files_artifacts[]` pointing to stdout/stderr/prompt/structured_return/operator report
- risks explicitly say no reliable findings and failed execution
- `pkg_openharness_structure_probe` risks say source-inspection-only and no behavioral trace

Notebook-only judgment:

- sufficient to decide inspection is needed

Decision:

- inspect is justified when the notebook marks raw fallback/failure or when source-inspection limits need artifact verification.

Raw logs required:

- yes, because inspect is the action itself.

### Close

Package evidence:

- `pkg_openharness_structure_probe`
- Step A and Step B real worker runs both landed as `worker_emitted`
- latest answer/findings/source refs are specific
- remaining risks are bounded and already recorded
- next action moved to Package 4 and was completed as a separate hardening package

Notebook-only judgment:

- sufficient

Decision:

- close is justified for Package 3's real-worker-continuity validation scope. It does not mean global worker-spine promotion.

Raw logs required:

- no, unless supervisor wants audit-level confirmation.

## 6. Notebook-Only vs Deep-Inspection Boundary

Notebook-only can support:

- continue when latest `worker_emitted` run has concrete findings and next hint
- hold when source/status/risk clearly mark failure
- rerun when failure is execution/format-related and package goal remains valid
- close when bounded purpose is answered and risks are recorded

Deep inspection is still needed for:

- diagnosing failed worker launch internals
- validating raw stdout/stderr content
- checking whether source-inspection findings match actual runtime behavior
- deciding whether a parser-fallback answer is trustworthy enough for reuse

## 7. What Improved

The notebook now behaves more like a supervisor decision surface than a log archive:

- source quality is visible
- answer/findings are separated
- artifacts are listed without being mixed into findings
- next_continue_hint gives package-specific direction when worker-emitted
- failed/raw runs preserve enough information to hold or inspect

## 8. Remaining Limits

Limits:

- one primary package was not enough to cover all five decisions honestly
- close judgment is bounded to package scope, not promotion
- parser-fallback quality remains uneven
- raw logs remain necessary for diagnosis-level inspection
- Gemini/manual worker variation remains untested

## 9. Package 6 Readiness

Package 6 is ready.

Recommended closeout decision basis:

- actual worker spine is usable for one Codex worker
- notebook continuity supports supervisor decisions in bounded form
- fallback handling is resilient enough for hold/rerun/inspect decisions
- broader promotion should remain bounded because only one worker type and limited packages were tested

