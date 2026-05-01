# Integrated Engine Terminal Mirror Dashboard Reuse Note v0

## 1. status

```yaml
report_status: implementation_note
verdict: PASS_WITH_NOTE
scope: reuse_existing_integrated_engine_ui
new_dashboard_created: false
baseline_lock: false
schema_enforcement: false
runtime_manifest_created: false
```

## 2. purpose

This note records the first practical reuse of the existing integrated engine screen as a dashboard for terminal/Codex conversation flow.

The goal is not to turn the UI into the primary work surface.

The goal is to let the terminal conversation remain the main operating surface while the integrated engine screen mirrors:

- current package vessel
- latest Codex/CLI return
- route label
- package run events
- return-to-space candidates
- manual refresh / live poll status

## 3. current finding

The existing integrated engine UI is reusable.

It already has the right attachment points:

- `CliHostControlPanel` reads `/api/vectorfl-engine/state`.
- `build_cli_host_control_state()` reads `runtime/cli_sessions`.
- package run events are already exposed through `runtime/events/integrated_engine_package_run_events.jsonl`.
- latest return, recent returns, deposit candidates, and package notebooks are already available in the API state.

The missing piece was not a new screen.

The missing piece was a lighter default live refresh behavior and clearer framing that this screen is a terminal conversation mirror.

## 4. implemented change

Updated:

```text
app/ui/integrated_engine/VectorFLIntegrationShell.tsx
```

Added:

- `DashboardRefreshState`
- `refreshDashboardState()`
- automatic 5-second polling of `/api/vectorfl-engine/state`
- manual `refresh now` button
- header label: `terminal conversation mirror / runtime poll`
- visible live source note explaining that the dashboard reflects:
  - `runtime/cli_sessions`
  - package run events
  - latest return

This keeps the UI as observer/dashboard, not as the source of truth.

## 5. verification

Command:

```text
npm run build
```

Result:

```yaml
status: passed
typescript: passed
vite_build: passed
```

## 6. interpretation

This is the right first reuse direction.

The integrated engine screen should not become another heavy control panel that the user must operate.

It should become a live cockpit that shows what the terminal conversation is already doing:

```text
terminal/Codex conversation
-> runtime/cli_sessions + package events
-> /api/vectorfl-engine/state
-> integrated engine dashboard mirror
```

## 7. remaining gap

This is still not full "conversation reflection."

The dashboard currently mirrors only persisted runtime state:

- CLI sessions
- package run events
- latest return
- package notebooks

It does not yet mirror the current live chat turn unless that turn is written into runtime or a session artifact.

Therefore, the next actual gap is a small conversation event capture layer, not more UI.

## 8. next candidate

Recommended next bounded action:

```text
create a small terminal conversation event writer
```

Possible shape:

```text
scripts/cli/record_terminal_turn_event.py
```

It should write a tiny JSONL event such as:

```yaml
source: terminal_conversation
role: user|codex
summary: short text
route_hint: optional
lens_hint: optional
return_to_space_state: optional
```

Then `/api/vectorfl-engine/state` can expose these events and the dashboard can show them beside CLI returns.

## 9. guardrails

- Do not make the dashboard the source of truth.
- Do not require the user to fill UI forms.
- Do not add a second workflow.
- Do not treat polling as ingestion.
- Do not auto-promote terminal turns into space records.
- Keep Codex responsible for judgment.
- Keep scripts responsible only for capture, lookup, and display support.

## 10. verdict

```yaml
verdict: PASS_WITH_NOTE
why: existing integrated engine UI can be reused as a terminal conversation mirror with minimal changes
main_limit: current live chat is visible only after it becomes runtime/session/event material
next_move: add bounded terminal-turn event capture if live reflection remains useful
```
