# Integrated Engine CLI On-Top Package 1 Closeout Note v0

## Verdict
PASS_WITH_NOTE

Package 1 now has a first usable CLI host/control path on top of the existing integrated-engine body. The 3-surface interpretation remains fixed: user surface keeps purpose/approval posture, VectorFL surface observes and steers the CLI operation layer, and engine surface receives structured return/deposit material.

The note is that package 1 uses a synchronous Codex adapter path. It records `queued -> running -> done/failed` in the canonical session folder, but it does not yet provide long-running background polling or interruption of an already-running subprocess.

## Implemented

- Added canonical CLI session artifacts under `runtime/cli_sessions/<session_id>/`.
- Added a package-1 Codex adapter boundary with `prepare_run`, `start_run`, `poll_run`, `collect_result`, and `interrupt_run`.
- Added integrated-engine API actions for running a CLI session and marking the latest return.
- Added `cli_host_control` to the integrated-engine state payload.
- Added a bounded CLI Host / Control panel to the existing VectorFL page at `/vectorfl-engine/vectorfl`.
- Added mark actions for:
  - `reread_target`
  - `implementation_return`
  - `validation_target`
  - `deposit_candidate`

## Runtime Artifact Contract

Each session writes:

- `session.json`
- `prompt.md`
- `stdout.log`
- `stderr.log`
- `structured_return.json`
- `deposit_candidate.md`

The session index is stored at:

- `runtime/cli_sessions/index.json`

## Baseline Protection

- No new engine surface was added.
- The CLI layer is explicitly recorded as `on_top_cli_host_control_layer`.
- VectorFL is the primary observation/control surface for the package-1 panel.
- The existing scaffold/read-map contract was not changed.
- Runtime binding remains explicit API action based; no watcher or supervisor automation was introduced.
- Gemini/other backends are extension points only, not package-1 behavior.

## Intentionally Out Of Scope

- Full multi-agent routing.
- Autonomous planning.
- Distributed workers.
- Universal plugin or skill framework.
- Page promotion automation.
- Selected-object behavior.
- Long-running background worker orchestration.

## Extension Points

- Add `GeminiCliAdapter` behind the same adapter contract.
- Replace synchronous execution with a background process registry if repeated real use proves it necessary.
- Promote richer polling only after package-1 session artifacts are stable in real use.
- Add structured output parsing for important findings/diffs after real Codex returns show stable shape.

## Verification

- Python compile passed for:
  - `app/runtime/vectorfl_integrated_engine_api.py`
  - `app/runtime/vectorfl_integrated_engine_shell.py`
  - `app/core/runtime/viewer_server.py`
- Integrated-engine state now exposes `cli_host_control`.
- Dry-run CLI session created the canonical artifact folder successfully.
- Dry-run mark action recorded `reread_target`.
- React dual surface app build passed with `npm run build`.

## Watchpoints

1. Actual Codex invocation depends on a working local `codex` CLI in the viewer-server process environment.
2. Synchronous execution is enough for package 1, but long tasks will block the API request until completion or timeout.
3. The current `deposit_candidate.md` is prepared material only; actual engine ingestion/promotion remains closed.

## One-Line Lock

This is not a new agent system. It is the first bounded CLI host/control path on top of the fixed integrated-engine body, primarily visible through the VectorFL surface.
