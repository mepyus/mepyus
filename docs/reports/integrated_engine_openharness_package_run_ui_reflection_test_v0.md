# Integrated Engine OpenHarness Package Run UI Reflection Test v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Test Prompt

`references/git_search/openharness-main 폴더를 구조적으로 분해/분석해서 우리 내부의 공간의 재료를 활용해 분석해줘`

## 3. Why This Test Was Needed

The prior UI could show package language, but real execution still looked like one returned output. The event rail mixed previous records, the active package was not clearly reflected, and the control panel did not make the source/context material visible enough.

This test checked whether a real package run now creates inspectable process events and whether the backend can read the referenced folder before CLI handoff.

## 4. What Was Changed Before Testing

- Runtime package events are now recorded in `runtime/events/integrated_engine_package_run_events.jsonl`.
- CLI session state now exposes `cli_host_control.package_run_events`.
- The VectorFL event rail maps runtime events into package process events.
- The front-end filters runtime events by the selected active package id before mixing them with local UI events.
- Context refs are inferred for known package titles:
  - `OpenHarness` -> `references/git_search/openharness-main`
  - external lens material -> `gemini/external_analysis`
  - surface/UI package -> current integrated-engine UI files
- Dry-run execution now profiles context refs instead of returning only a generic contract message.

## 5. Three Run Results

All three runs used the same package id:

`pkg_openharness_structure_probe`

### Run 1

- ok: `true`
- event count: `6`
- event chain:
  - `package_intake`
  - `context_bundle`
  - `source_structure_scan`
  - `cli_handoff`
  - `cli_return`
  - `vectorfl_reread`

### Run 2

- ok: `true`
- event count: `6`
- event chain:
  - `package_intake`
  - `context_bundle`
  - `source_structure_scan`
  - `cli_handoff`
  - `cli_return`
  - `vectorfl_reread`

### Run 3

- ok: `true`
- event count: `6`
- event chain:
  - `package_intake`
  - `context_bundle`
  - `source_structure_scan`
  - `cli_handoff`
  - `cli_return`
  - `vectorfl_reread`

## 6. Source Structure Read Result

The source folder was actually profiled before CLI handoff:

- ref: `references/git_search/openharness-main`
- kind: `directory`
- exists: `true`
- file count: `400`
- directory count: `90`
- top dirs include:
  - `.agents`
  - `.claude`
  - `.github`
  - `assets`
  - `docs`
  - `frontend`
  - `ohmo`
  - `scripts`
- top files include:
  - `.gitignore`
  - `CHANGELOG.md`
  - `CONTRIBUTING.md`
  - `LICENSE`
  - `README.md`
  - `README.zh-CN.md`
  - `pyproject.toml`

## 7. Panel Reflection Judgment

### Package / vessel reflection

Improved. The run now records `package_intake`, so the package is not only a selected UI card; it has a runtime vessel event.

### Context / source reflection

Improved. The run records `context_bundle` and `source_structure_scan`, including the actual OpenHarness folder profile.

### CLI / digestion reflection

Partially improved. The run records `cli_handoff` and `cli_return`, but the test was dry-run, so this validates the package event pipeline and source profiling, not live model analysis quality.

### VectorFL reread reflection

Improved. The run records `vectorfl_reread`, so the output is not treated as final approval.

### Event rail clarity

Improved but still limited. The rail now has runtime events and active-package filtering, but it still needs real browser use to judge whether labels are intuitive enough during manual operation.

## 8. Remaining Limits

- The test used dry-run execution to avoid depending on external model behavior.
- Events appear after the synchronous run returns; they are not streamed live during execution.
- Direct API test packages do not automatically appear in the left package stack unless the UI creates or selects a matching package id.
- The event rail is now less mixed, but older runtime records still exist in the ledger by design.

## 9. Validation Commands

- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py`
- `npm run build`
- Three direct API package-run calls through `run_integrated_engine_cli_session(...)`
- `/api/vectorfl-engine/state` read through the running server

## 10. Next Safe Fix

The next fix should be UI-facing:

- make the event rail show a small active package header
- add a current run/session filter indicator
- show source/profile results in the control panel digest
- keep old ledger events available but visually separate from current active package events

Do not add automation yet. The current gap is still run readability, not model orchestration.
