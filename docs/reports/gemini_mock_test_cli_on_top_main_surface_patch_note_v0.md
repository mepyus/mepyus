# Gemini Mock Test CLI On-Top Main Surface Patch Note v0

## Verdict
PASS_WITH_NOTE

`gemini/mock_test` is now treated as the main UI body for the CLI on-top path. The existing `/vectorfl-engine/vectorfl` page remains a functional validation shell, while the mock UI now contains the bounded CLI Host / Control panel inside the VectorFL surface.

The note is that validation used the mock app's proxied API path with `curl`, not automated browser-click testing.

## What Changed

- Added `gemini/mock_test/CliHostControlPanel.tsx`.
- Mounted the panel inside `gemini/mock_test/VectorFLIntegrationShell.tsx` in the VectorFL surface's optional tool/support layer position.
- Added a Vite dev proxy in `gemini/mock_test/vite.config.ts`:
  - `/api` -> `http://127.0.0.1:8421`

## Why This Preserves The Baseline

- The mock UI remains the visible body.
- CLI is still an on-top host/control layer, not a fourth surface.
- The panel is placed inside VectorFL support/tool territory, not in the user surface or engine surface.
- The existing `runtime/cli_sessions` contract and integrated-engine API are reused.
- No package 2 behavior, background registry, Gemini adapter, ingestion automation, or new orchestration concept was added.

## What The Panel Provides

- Codex backend, fixed as package-1 backend.
- Task type selection: `summarize`, `inspect`, `reread`, `validate`.
- Purpose input.
- Bounded context refs input.
- Prompt payload input.
- Run Codex action.
- Refresh latest return action.
- Latest session id / backend / task / status / marks.
- Structured return preview.
- Deposit candidate preview.
- Mark actions:
  - `reread_target`
  - `implementation_return`
  - `validation_target`
  - `deposit_candidate`

## Validation

- `npm run build` passed in `gemini/mock_test`.
- Vite dev server started at `http://127.0.0.1:5173/`.
- Dev proxy returned integrated-engine state through `http://127.0.0.1:5173/api/vectorfl-engine/state`.
- A real Codex read-only run succeeded through the mock app proxy path:
  - session id: `cli_20260416T095505Z_30757cb3`
  - requested by page: `gemini/mock_test`
  - status: `done`
  - exit code: `0`
- Mark action through the same proxy path succeeded with `validation_target`.

## Still Deferred

- Browser-click automation.
- Session browsing/history.
- Background/async runner.
- Gemini adapter.
- Deposit ingestion bridge.
- Promotion automation.

## Current Operating Read

The usable screen should now be `gemini/mock_test`, not the old integrated-engine page. The old page remains useful as a validation/control reference, but the visible working body has moved to the Gemini mock surface.

## Recommended Next Target

Keep using the Gemini mock body and validate the panel by hand in the browser before adding session browsing/history.

## Follow-Up Hardening Round

### Round Goal

Make the Gemini mock body behave more like the real operating entrypoint instead of a reference mock that still requires the user to navigate away or infer mark state from runtime files.

### Files Changed

- `gemini/mock_test/VectorFLIntegrationShell.tsx`
- `gemini/mock_test/CliHostControlPanel.tsx`

### What Changed

- The Gemini mock app now opens on the VectorFL surface by default.
- The CLI Host / Control panel is now placed before the line inspection card in the VectorFL right-side work lane.
- The latest return card now includes a short engine-route reminder.
- The latest return card now shows recent mark history directly in the page.

### Why This Was Changed

- VectorFL is the primary operating and observation surface for the on-top CLI layer.
- The user should not need to first switch surfaces before starting a Codex run.
- The user should not need to open `runtime/cli_sessions/*/session.json` just to confirm whether a result was marked for reread, validation, implementation return, or deposit candidate flow.

### Validation

- `npm run build` passed in `gemini/mock_test`.
- The mock app API proxy remained reachable at `http://127.0.0.1:5173/api/vectorfl-engine/state`.
- A real read-only Codex run succeeded through the mock app proxy path:
  - session id: `cli_20260416T100450Z_9e24bf20`
  - requested by page: `gemini/mock_test`
  - status: `done`
  - exit code: `0`
- Mark action through the mock app proxy path succeeded:
  - session id: `cli_20260416T100450Z_9e24bf20`
  - mark: `validation_target`

### Pass / Fail

PASS_WITH_NOTE.

The usable path now starts in the Gemini mock VectorFL surface, can run Codex through the existing CLI session API, can show the latest structured return and deposit preview, and can show mark history without raw artifact inspection.

The note remains browser-click and user-feel validation. The API path is validated end-to-end, but final usability should still be checked by hand in the browser.

### Watchpoints

- Do not turn the CLI panel into a fourth surface.
- Do not add session browsing/history until repeated use proves latest-return-only is the bottleneck.
- Do not add Gemini adapter before Codex-on-top operation feels stable in the main mock body.

### Next Small Step

Open `http://127.0.0.1:5173/`, use the VectorFL surface CLI panel by hand once, and confirm whether the latest return plus mark history is enough for first-pass operation.
