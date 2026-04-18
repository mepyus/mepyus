# Integrated Engine Package Notebook MVP Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Problem

The integrated-engine surface had package language, event rails, and CLI execution, but the user still had no clear working unit.

The screen felt like:

- select package
- run CLI once
- inspect scattered process records
- stop

That meant the package was a visual object, not yet a usable workspace.

## 3. Patch

A package notebook layer was added.

The backend now builds `cli_host_control.package_notebooks` by grouping CLI sessions by `active_package.id`.

Each notebook contains:

- package id / title / summary
- latest stage / executor
- run count
- latest run
- prior runs
- result summary
- route label
- event count
- artifact paths
- bounded context refs

The UI now shows a `Package Notebook` panel for the selected package.

## 4. What The Notebook Does

For the selected package, the notebook shows:

- latest package result
- run artifacts
- context refs
- previous package runs
- `Continue this package`

`Continue this package` attaches the selected run's artifacts and context refs into the next prompt setup, so the next instruction can continue from that package history instead of starting as a naked one-shot CLI call.

## 5. Verification

Backend notebook state was checked after existing test runs:

- notebook count: `3`
- `pkg_openharness_structure_probe`: `3` runs
- `pkg_external_lens_pool_003`: `1` run
- `package_1`: `10` recent unassigned/default runs

Build checks:

- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py`
- `npm run build`

Both passed.

## 6. Boundary

This is not full automation.

It does not add:

- multi-handler orchestration
- live streaming runner
- automatic line / axis promotion
- automatic package dispatch
- canonical redeposit

It only creates the first practical working unit: one selected package with accumulated runs and a continuation path.

## 7. Next Safe Check

Use `OpenHarness 구조 분석`, click `Continue this package`, then run a follow-up instruction.

The expected behavior is:

- prior run artifacts move into setup refs
- prompt changes to continue from the selected package run
- the new run is appended to the same package notebook

If this works, the surface has moved from one-shot CLI execution toward a usable package workspace.
