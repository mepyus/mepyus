# Integrated Engine UI Stable Folder Migration Note v0

## Verdict

PASS_WITH_NOTE

The integrated-engine main operating UI has been promoted from `gemini/mock_test` into `app/ui/integrated_engine`.

The note is that `gemini/mock_test` remains as Gemini proposal/reference clay, while `app/ui/integrated_engine` is now the stable source folder for the actual main UI path. Some old report wording still says `gemini/mock_test`; that wording should be reread as historical context, not the current source location.

## Round Goal

Move the currently usable Gemini mock UI into a stable project folder before further CLI-on-top work makes the source location ambiguous.

## Files Changed

- `.gitignore`
- `app/ui/integrated_engine/*`
- `docs/reports/integrated_engine_ui_stable_folder_migration_note_v0.md`

## What Changed

- Created `app/ui/integrated_engine` as the stable source folder for the current integrated-engine UI.
- Copied the existing working UI from `gemini/mock_test` into the stable folder.
- Kept `gemini/mock_test` in place as reference/proposal material.
- Updated the stable app package name to `vectorfl-integrated-engine-ui`.
- Updated the stable app browser title to `VectorFL Integrated Engine`.
- Updated the stable app shell label from `VECTORFL Shell` to `Integrated Engine`.
- Added broad ignores for `node_modules/` and `dist/` so local dependency/build artifacts do not become the project signal.

## Why This Was Done

- `gemini/mock_test` should not remain the long-term source of the real operating UI.
- Gemini material is design/proposal clay; the actual integrated-engine UI needs a stable source location.
- `runtime` should remain for session artifacts, manifests, state, and execution returns, not React/Vite source.
- The 3-surface engine structure remains fixed; this migration only changes source placement.

## Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- The stable app dev server is running at `http://127.0.0.1:5173/`.
- The served HTML title is `VectorFL Integrated Engine`, confirming the new source is active.
- The API proxy from the stable app to `http://127.0.0.1:8421` works.
- A real read-only Codex session succeeded through the stable app proxy path:
  - session id: `cli_20260416T101531Z_ba21f03e`
  - requested_by_surface: `vectorfl_surface`
  - requested_by_page: `app/ui/integrated_engine`
  - status: `done`
  - exit code: `0`
- Marking the same session as `validation_target` succeeded.

## Pass / Fail

PASS_WITH_NOTE.

The stable folder now runs and can operate the existing CLI on-top path. The only note is that browser-click/user-feel validation still needs the user, and some prior documentation still refers to `gemini/mock_test` because it was written before the stable-folder promotion.

## Watchpoints

- Do not continue feature work against `gemini/mock_test` unless intentionally modifying the reference mock.
- Do not move React/Vite source into `runtime`.
- Do not treat this migration as package 2 or as a new surface.
- Do not add Gemini adapter, background runner, or session browsing until the stable Codex path is hand-used.

## Next Small Step

Use `http://127.0.0.1:5173/` from the stable app and hand-check one VectorFL CLI run from the browser.
