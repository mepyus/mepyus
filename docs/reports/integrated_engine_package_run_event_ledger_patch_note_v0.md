# Integrated Engine Package Run Event Ledger Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Problem Confirmed

The UI could describe a package as a vessel and display a VectorFL event rail, but the actual CLI run still behaved like a single output call:

1. form prompt
2. run Codex CLI
3. receive one text result
4. display one return

That meant package digestion did not visibly run as an internal process. The screen had the language for process, but the runtime did not leave process events behind.

## 3. What Was Added

A minimal runtime event ledger was added:

- `runtime/events/integrated_engine_package_run_events.jsonl`

The CLI session API now records package-run events around the actual CLI call:

- `package_intake`
- `context_bundle`
- `cli_handoff`
- `cli_return`
- `vectorfl_reread`
- `route_mark`

Each event records:

- package id / title
- session id
- stage
- label / detail
- signal
- confidence
- receiver
- suggested action
- boundary

## 4. UI Connection

The integrated-engine UI now reads `cli_host_control.package_run_events` from `/api/vectorfl-engine/state`.

Those runtime events are mapped into the VectorFL event rail, so the rail can show process movement from the backend ledger, not only local front-end events.

## 5. What This Still Is Not

This patch does not create:

- true asynchronous package runner
- automatic internal exploration
- automatic line / axis detection
- external research automation
- multi-handler orchestration
- canonical redeposit

The current run is still synchronous, so the UI sees the full event chain after the request returns. This is enough to stop the run from looking like a naked output, but not enough to show live streaming stages during the CLI call.

## 6. Current Usable Improvement

When a package such as external lens material reading is sent to CLI, the runtime can now leave behind a visible chain:

1. package vessel formed
2. internal context bundle prepared
3. CLI handoff started
4. CLI return received
5. return reread routed

This makes the process inspectable even when the underlying CLI execution remains a single synchronous call.

## 7. Next Safe Action

Use the current ledger-backed rail in real package runs. If the user still needs live progress during long execution, the next implementation should split synchronous CLI execution into a staged runner or polling loop rather than adding more UI-only events.
