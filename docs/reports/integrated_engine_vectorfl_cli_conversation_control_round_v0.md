# Integrated Engine VectorFL CLI Conversation Control Round v0

## Verdict

PASS_WITH_NOTE

The stable integrated-engine UI now supports a first-pass conversation-like Codex operating path inside the VectorFL surface. It also exposes thin 3-surface focus controls without changing the fixed engine body.

The note is that this is still synchronous, latest/recent-session based operation. It is not async background orchestration, a full chat database, a Gemini adapter, or deposit ingestion automation.

## Round Goal

Make the VectorFL surface more like the actual operating place where the user can talk to Codex, reread recent Codex turns, and steer the 3-surface frame without leaving the integrated-engine flow.

## Files Changed

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

## Why These Changes

- The previous panel could run one Codex task, but it did not yet feel like an operating conversation.
- The user needed recent turns visible in the same VectorFL flow instead of mentally reconstructing from raw session artifacts.
- The user also needs to steer User / VectorFL / Engine perspective from the VectorFL operating place without creating a fourth surface.

## What Changed

- Added `recent_readable_returns` to `cli_host_control` state, derived from the existing `runtime/cli_sessions/index.json`.
- Added a recent Codex turns list to the VectorFL CLI panel.
- Added 3-surface focus buttons:
  - user
  - vectorfl
  - engine
- Each focus button switches the visible surface and loads a bounded Codex prompt template for that surface perspective.
- Updated the panel request source to `requested_by_page: app/ui/integrated_engine`.
- Kept marks and mark history inside the same panel flow.

## What Was Verified

- Python API syntax check passed with `py_compile`.
- `npm run build` passed in `app/ui/integrated_engine`.
- Viewer server was restarted so the updated API state is active.
- Stable UI API state now includes:
  - `recent_readable_returns`
  - latest session id
  - latest marks
- A real read-only Codex conversation-mode run succeeded:
  - session id: `cli_20260416T102144Z_d65ce415`
  - requested_by_surface: `vectorfl_surface`
  - requested_by_page: `app/ui/integrated_engine`
  - status: `done`
  - exit code: `0`
- Marking that session as `reread_target` succeeded.
- The latest session became the first recent readable return.

## Pass / Fail

PASS_WITH_NOTE.

The user can now operate Codex from the VectorFL surface as a sequence of visible recent turns, not only as a raw one-off CLI call. The 3-surface controls steer perspective and prompt shape, but do not redesign or replace the engine surfaces.

## Still Deferred

- Browser-click/user-feel validation.
- Async/background run support.
- Session browsing beyond the recent-turn list.
- Gemini adapter.
- Deposit ingestion automation.
- Any new surface or multi-agent orchestration layer.

## Watchpoints

- Recent turns must remain an operating aid, not a full conversation database.
- Surface focus buttons must remain perspective controls, not new routing authority.
- Codex returns must remain on-top tool returns until the user marks or deposits them.
- If repeated use needs older runs, session history is the likely next bounded package.

## Next Small Step

Hand-use the VectorFL CLI panel in the browser and check whether the recent-turn list plus surface focus buttons are enough for actual conversation-style operation.

## Follow-Up Continuation Patch

### Round Goal

Reduce the remaining manual step between reading a recent Codex turn and continuing the conversation from that turn.

### Files Changed

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- Added artifact paths to each `recent_readable_returns` item:
  - `session_path`
  - `structured_return_path`
  - `deposit_candidate_path`
- Added a `Continue latest` action in the VectorFL CLI panel.
- Selecting a recent Codex turn now loads that turn's artifacts into `bounded_context_refs`.
- The prompt/purpose fields are rewritten into a bounded follow-up prompt.
- Added thin `suggested_next_use` inference so Codex returns that say validation/deposit/implementation/reread can set the structured next-use field more accurately.

### Why This Was Changed

- Conversation-like operation should not require the user to open raw files or copy artifact paths manually.
- Recent turns should be reusable as follow-up context from the VectorFL surface.
- The structured return should not always default to `reread_target` when the returned text clearly indicates `validation_target` or another next use.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- `py_compile` passed for `app/runtime/vectorfl_integrated_engine_api.py`.
- Viewer server was restarted so the updated API state is active.
- API state confirmed recent turns now expose artifact paths.
- A real follow-up Codex run succeeded using previous session artifacts as bounded context:
  - session id: `cli_20260416T102612Z_277b5388`
  - status: `done`
  - exit code: `0`
- A suggested-next-use inference smoke test succeeded:
  - session id: `cli_20260416T102720Z_8e045e9b`
  - structured `suggested_next_use`: `validation_target`
- The inference smoke test session was marked as `validation_target`.

### Pass / Fail

PASS_WITH_NOTE.

The VectorFL surface can now continue from a previous Codex turn without raw artifact copying. The note is that this is still a synchronous session-artifact conversation path, not a full chat system or background runner.

### Watchpoints

- Continue-from-turn should remain bounded to explicit session artifacts.
- Do not infer authority from Codex text alone; marks still represent the operator's route decision.
- If users need more than the last few turns, session browsing/history becomes the next bounded package.

### Next Small Step

Hand-use `Continue latest` and one recent-turn click in the browser. If it feels sufficient, continue using this mode before adding session browsing/history.

## Deposit-Ready Queue Patch

### Round Goal

Make deposit-candidate returns visible in the VectorFL operating flow without opening automatic ingestion or promotion.

### Files Changed

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- Added `deposit_ready_returns` to `cli_host_control` state.
- The queue is derived from existing CLI sessions marked with `deposit_candidate` or `deposit_ready`.
- Added a `deposit-ready queue` section to the VectorFL CLI panel.
- Selecting a deposit-ready item loads it as the current return and prepares follow-up context.
- The queue explicitly says it is not automatic ingestion or promotion.

### Why This Was Changed

- Marking a return as `deposit_candidate` should create an operating signal the user can see from the VectorFL surface.
- The user should not need to inspect raw session files to know which returns are ready for possible engine deposition.
- Actual deposit ingestion remains intentionally closed until it becomes the confirmed bottleneck.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- `py_compile` passed for `app/runtime/vectorfl_integrated_engine_api.py`.
- Viewer server was restarted so the updated API state is active.
- API state confirmed `deposit_ready_returns` exists and contains ready items.
- Session `cli_20260416T102720Z_8e045e9b` was marked with `deposit_candidate`.
- API state confirmed that session appears in the deposit-ready queue with marks:
  - `validation_target`
  - `deposit_candidate`

### Pass / Fail

PASS_WITH_NOTE.

Deposit-ready visibility now exists inside the VectorFL surface. The note is that this is still a queue/readiness signal only; it does not ingest, canonicalize, promote, or mutate engine memory.

### Watchpoints

- Deposit-ready must not be confused with completed ingestion.
- Queue selection must remain a reread/follow-up aid, not an automatic engine write.
- If repeated use requires actual deposition, the next package should be a bounded deposit-ingestion bridge with explicit user approval.

### Next Small Step

Hand-check that the deposit-ready queue is visible in the VectorFL panel and that selecting an item loads it as follow-up context.

## Cross-Surface Reflection Patch

### Round Goal

Make CLI sessions generated and mediated in the VectorFL surface visible across all three fixed surfaces:

- User surface: work assignment / user decision signal
- VectorFL surface: operating conversation / mediation signal
- Engine surface: processing return / validation / extraction material signal

### Files Changed

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `app/runtime/vectorfl_integrated_engine_api.py`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- Added `UserCliAssignmentPanel` to the User surface.
- Added `EngineCliReturnPanel` to the Engine surface.
- Added CLI turn and deposit counts to the top orientation band.
- Kept the VectorFL CLI panel as the only direct operating/control panel for CLI.
- User surface now reads latest CLI return as:
  - latest work signal
  - user decision mark state
  - deposit-ready count
- Engine surface now reads latest CLI return as:
  - processing status
  - latest return material
  - validation route label
  - extract/deposit candidate count
  - recent processing returns

### Why This Was Changed

- The final target is not only "Codex runs from VectorFL".
- The final target is that VectorFL-mediated CLI operation can affect the fixed 3-surface engine:
  - User surface can organize work and decision points.
  - VectorFL surface can mediate and reread.
  - Engine surface can show processing, return, validation, and extraction material.
- This patch does not create new authority or automatic ingestion. It only makes current session signals visible across surfaces.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- API state remained readable:
  - latest session present
  - recent turn count present
  - deposit-ready count present
- A real cross-surface reflection Codex run succeeded:
  - session id: `cli_20260416T103857Z_dcf7d364`
  - status: `done`
  - exit code: `0`
- That run confirmed:
  - User surface assignment signal is visible.
  - VectorFL operating signal remains central.
  - Engine return/validation signal is visible.
- The run was marked as `validation_target`.

### Suggested-Next-Use Inference Fix

The cross-surface validation run exposed a small inference bug:

- The body contained `deposit candidate`.
- The explicit tail said `suggested next use: validation target`.
- The first inference logic incorrectly selected `deposit_candidate`.

Fix:

- `suggested_next_use` inference now prefers the explicit tail around `suggested next use` before scanning the whole body.

Validation:

- `py_compile` passed.
- Viewer server was restarted.
- A retest succeeded:
  - session id: `cli_20260416T103956Z_7c38c3cf`
  - structured `suggested_next_use`: `validation_target`
  - mark: `validation_target`

### Pass / Fail

PASS_WITH_NOTE.

The 3-surface reflection path now exists. The note is that current labels are still largely internal/spatial language. The user may need Korean/operator-level interpretation from Codex until a later bounded readability pass is opened.

### Watchpoints

- User surface signal must not become automatic assignment authority.
- Engine surface signal must not be confused with completed ingestion or canonical memory.
- VectorFL remains the place to operate CLI directly.
- Human-readable reporting should be provided in Codex final responses for now, not rushed into UI wording patches.

### Next Small Step

Hand-check User surface and Engine surface after a new VectorFL CLI run:

- User surface should show latest assignment/decision signal.
- Engine surface should show latest processing/return/validation signal.
- VectorFL should remain the only place where CLI is directly operated.

## User/Engine Queue Reflection Patch

### Round Goal

Move beyond "the same CLI session is visible" toward "the same CLI session can be read as work assignment on the User surface and processing/validation/extraction material on the Engine surface."

### Files Changed

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- Expanded `UserCliAssignmentPanel` with a user work queue derived from recent CLI returns.
- The User surface now groups recent CLI turns as:
  - triage
  - reread assignment
  - validation decision
  - implementation return
  - deposit review
- Expanded `EngineCliReturnPanel` with:
  - validation queue
  - extraction / deposit material queue
- The Engine surface now separates validation-like returns from extraction/deposit material.

### Why This Was Changed

- The project target is not just "Codex can run from VectorFL".
- The target is that Codex returns can become operating material for all three fixed surfaces:
  - User surface organizes work and decisions.
  - VectorFL surface mediates and rereads.
  - Engine surface reads processing/return/validation/extraction material.
- This patch still avoids automatic assignment, automatic ingestion, or promotion.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- API state check confirmed:
  - latest CLI session is present.
  - recent turn count: 8
  - validation-like returns: 5
  - deposit-ready returns: 3

### Pass / Fail

PASS_WITH_NOTE.

The User and Engine surfaces now receive differentiated queue signals from VectorFL-mediated CLI returns. The note is that these queues are still internal/spatial-language heavy and should be interpreted for the user in Codex reports until a later readability pass is opened.

### Watchpoints

- User work queue is not automatic assignment authority.
- Engine validation/extraction queues are not completed processing or canonical memory.
- VectorFL remains the only surface that directly operates the CLI.
- UI language is still not human-comfortable enough for final use without Codex explanation.

### Next Small Step

Hand-check:

- User surface: the work queue should show CLI returns as decision/work candidates.
- Engine surface: validation and extraction/deposit queues should be visible.
- VectorFL surface: direct CLI operation remains there only.

## Cross-Surface Handoff-To-VectorFL Patch

### Round Goal

Let User and Engine surface queue items send a selected CLI return back to the VectorFL surface for follow-up, without allowing User or Engine surfaces to directly operate the CLI.

### Files Changed

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- Added `Send to VectorFL` actions on User surface work queue items.
- Added `Send to VectorFL` actions on Engine surface validation queue items.
- Added `Send to VectorFL` actions on Engine surface extraction/deposit material queue items.
- Selecting one of these actions:
  - switches the visible surface to VectorFL
  - loads the selected CLI turn as the current return
  - inserts that turn's artifact paths into `bounded_context_refs`
  - rewrites the prompt as a bounded follow-up

### Why This Was Changed

- User and Engine surfaces now receive useful queue signals, but they still need a way to hand a selected item back to the VectorFL operating surface.
- This preserves the fixed 3-surface role split:
  - User surface organizes/chooses work candidates.
  - Engine surface exposes processing/validation/extraction candidates.
  - VectorFL surface remains the direct CLI operation and mediation place.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- `py_compile` passed for `app/runtime/vectorfl_integrated_engine_api.py`.

### Pass / Fail

PASS_WITH_NOTE.

The handoff route is wired in the UI. The note is that final validation requires browser-click/user-feel confirmation, because the critical behavior is whether the surface switch and context loading feel clear to the user.

### Watchpoints

- `Send to VectorFL` is not direct CLI execution from User or Engine surfaces.
- It is a handoff/control preparation action only.
- CLI execution remains inside the VectorFL panel.
- The user still owns final decision and promotion.

### Next Small Step

Browser-check one item from the User surface queue and one item from the Engine surface queue:

- click `Send to VectorFL`
- confirm the app switches to VectorFL
- confirm `bounded_context_refs` is loaded with the selected session artifacts
- run Codex only from VectorFL if needed

## Execution Route Board CLI Ticket Patch

### Round Goal

Make CLI returns appear in the User surface's existing route board as work-routing candidates, not only in the separate CLI assignment panel.

### Files Changed

- `app/ui/integrated_engine/ExecutionRoutePanel.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- `ExecutionRoutePanel` now accepts `cliReturns`.
- Recent CLI returns are converted into route-board candidate tickets.
- CLI return marks determine placement:
  - unmarked / `reread_target` -> Backlog
  - `implementation_return` -> Handoff
  - `validation_target` / `deposit_candidate` -> Review
- The panel copy now notes that CLI returns are routed as candidates only.

### Why This Was Changed

- The User surface should not only display "there are CLI returns".
- It should be able to read those returns as work-routing candidates inside the user's operating board.
- This still avoids automatic assignment authority; the tickets are candidate signals derived from current marks.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- API state check confirmed current CLI ticket sources:
  - recent CLI tickets: 8
  - review candidates: 5
  - handoff candidates: 1
  - backlog/reread/unmarked candidates: 4

### Pass / Fail

PASS_WITH_NOTE.

The User surface now has CLI-derived work candidates inside the existing route board. The note is that this is still candidate routing, not automatic work assignment or task ownership.

### Watchpoints

- CLI route tickets must remain visually and conceptually candidate material.
- Do not let route-board placement imply completed assignment without user decision.
- If a real assignment action is needed later, it should be a bounded user approval action, not implicit mark conversion.

### Next Small Step

Hand-check User Surface:

- Execution Route Board should contain Codex CLI items in Backlog/Handoff/Review.
- These should read as candidate work items, not completed assignments.

## Engine Pipeline CLI Material Patch

### Round Goal

Reflect CLI returns inside the Engine surface's primary pipeline area, not only in the separate Engine CLI feed.

### Files Changed

- `app/ui/integrated_engine/vectorfl_engine_surface_mock.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_vectorfl_cli_conversation_control_round_v0.md`

### What Changed

- `VectorFLEngineSurfaceMock` now accepts CLI state as a prop.
- Added `EngineCliMaterialStrip` after the validation return panel in the primary engine pipeline.
- The strip displays:
  - latest CLI return status
  - route mark
  - validation count
  - deposit-ready count
  - latest return material
  - extraction/deposit candidate preview

### Why This Was Changed

- The Engine surface should not only have a separate CLI feed.
- CLI returns should also appear as material in the engine processing/validation/return chain.
- This remains a material signal only; it does not perform ingestion, canonicalization, or automatic processing.

### Validation

- `npm run build` passed in `app/ui/integrated_engine`.
- API state check confirmed:
  - latest session exists
  - latest status: `done`
  - latest mark includes `validation_target`
  - deposit-ready count: 3

### Pass / Fail

PASS_WITH_NOTE.

The Engine surface now reflects CLI-derived material in its primary pipeline. The note is that this still remains mock/runtime signal display; actual engine ingestion and processing remain closed.

### Watchpoints

- Engine pipeline reflection must not be interpreted as completed ingestion.
- CLI-derived material is still a return/validation/extraction candidate.
- Actual processing should only open through a bounded engine deposit/ingestion bridge later.

### Next Small Step

Hand-check Engine Surface:

- Primary Control Pipeline should include `CLI-derived engine material`.
- It should show latest route/status and return/extract material.
