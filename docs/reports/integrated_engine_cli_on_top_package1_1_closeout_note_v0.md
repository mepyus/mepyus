# Integrated Engine CLI On-Top Package 1.1 Closeout Note v0

## Verdict
PASS_WITH_NOTE

Package 1.1 validated the real read-only Codex path and hardened the latest-return readability layer on the VectorFL page. The note is that the real-path validation used the same HTTP endpoint invoked by the VectorFL panel rather than an automated browser click. The UI path is wired to that endpoint, and the endpoint completed a real `codex exec --sandbox read-only` run.

## Real Run Used

- session id: `cli_20260416T094421Z_8b0ef908`
- backend kind: `codex`
- task type: `summarize`
- requested by surface: `vectorfl_surface`
- requested by page: `/vectorfl-engine/vectorfl`
- dry run: `false`
- source file read by Codex: `docs/reports/integrated_engine_cli_on_top_package1_closeout_note_v0.md`
- purpose: Package 1.1 real-path validation by reading the Package 1 closeout note and returning a short summary.

## What Passed

- A real Codex read-only run completed through the CLI session API used by the VectorFL panel.
- Session status moved through the runtime path and ended as `done`.
- `stdout.log` was captured.
- `stderr.log` was captured.
- `structured_return.json` was generated.
- `deposit_candidate.md` was generated.
- Mark action worked after the real run with `validation_target`.
- The latest session is now exposed through `cli_host_control.latest_readable_return`.

## Readability Hardening

The VectorFL CLI Host / Control panel now shows a thin latest-return layer:

- latest session id
- backend kind
- task type
- status
- purpose text
- structured return preview
- deposit candidate preview
- current marks
- recent mark history
- refresh latest return action

This is deliberately not a session explorer or generic log viewer. It only makes the latest return readable enough for first-pass use without opening raw files manually.

## Baseline Protection

- No new surface was added.
- The CLI layer remains an on-top host/control layer.
- VectorFL remains the main observation/steering place for CLI operation.
- No background registry was added.
- No Gemini adapter was added.
- No async runner, polling daemon, ingestion pipeline, promotion automation, or multi-agent orchestration was opened.
- The 3-surface engine interpretation remains intact.

## What Remains Deferred

- Browser-click automation for UI validation.
- Background runner / async polling.
- Interrupt hardening for live subprocesses.
- Gemini or other backend adapters.
- Session explorer or log viewer.
- Structured ingestion of deposit candidates.
- Promotion automation.

## First-Pass Reading Judgment

The VectorFL page now removes the need to manually open raw session artifacts for first-pass understanding of the latest run. Raw artifacts remain available for deeper audit, but the latest return, purpose, mark state, and deposit candidate preview are visible from the VectorFL page itself.

## Review Result

- Fixed 3 surfaces: preserved.
- CLI on-top: preserved.
- Real read-only Codex path: passed.
- Latest result readable from VectorFL page: passed.
- Raw file inspection still useful for audit but no longer required for first-pass reading.

## One-Line Lock

Package 1.1 proves the first real Codex read-only path and makes the latest return readable from the VectorFL surface without opening a new engine surface or package-2 orchestration.
