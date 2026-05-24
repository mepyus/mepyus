# UI Contract Clarification — VectorFLIntegrationShell <-> CliHostControlPanel

## 0. Status

- contract clarification only
- file-grounded observation only
- not implementation
- not final UI spec
- not API contract authority
- requires GPT/Supervisor review

## 1. Source / Provenance Note

Files inspected:

- `app/work/space-skill-sandbox/outputs/implementation_unit_001_operating_ui_component_spec_20260509_v0.md`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/core/runtime/viewer_server.py`
- `app/runtime/vectorfl_integrated_engine_api.py`

Directly observed:

- `VectorFLIntegrationShell` owns the main workbench shell state, selected package state, modal state, `cliHostState`, `workPacketDraft`, and an `externalFollowupTurn`.
- `VectorFLIntegrationShell` polls `GET /api/vectorfl-engine/state` every 5 seconds and stores `result.cli_host_control` in parent state.
- `VectorFLIntegrationShell` passes `activeSurface`, `onSurfaceChange`, `onCliStateChange`, `onPacketDraftChange`, `externalFollowupTurn`, and `activePackage` into `CliHostControlPanel`.
- `CliHostControlPanel` owns the session draft, prompt/context state, latest/recent returns, package notebooks, conversation turns, session events, runtime events, run status, and running state.
- `CliHostControlPanel` reads `GET /api/vectorfl-engine/state`, posts to `/api/vectorfl-engine/actions/cli-session/run`, and posts to `/api/vectorfl-engine/actions/cli-session/mark`.
- `viewer_server.py` maps those API routes to `build_vectorfl_integrated_engine_state`, `run_integrated_engine_cli_session`, and `mark_integrated_engine_cli_session`.
- `build_vectorfl_integrated_engine_state` returns `cli_host_control` from `build_cli_host_control_state`.

Inference:

- The current boundary is mixed: Shell is the layout/package container, while ControlPanel is both a setup/display surface and an action surface.
- The safest first UI micro-change boundary is contract clarity around shared types/callbacks and action ownership, not dashboard redesign or runtime API mutation.

Missing evidence:

- No build/test/run was performed.
- The endpoint was not called live.
- The full runtime response contract was not exhaustively mapped.
- Browser behavior, visual layout, and user workflow friction were not inspected.

Needs GPT/Supervisor review:

- Whether the next UI micro-change should improve user-visible clarity, type sharing, or action-boundary labeling.
- Whether `CliHostControlPanel` should remain a mixed display/control surface or be split later.

## 2. One-Paragraph Summary

`VectorFLIntegrationShell` currently acts as the parent workbench and package container. It owns selected package, package stack, modal, latest CLI state copy, packet draft copy, and runtime refresh status, and it polls `/api/vectorfl-engine/state` every 5 seconds. `CliHostControlPanel` receives the selected package and parent callbacks, but it also owns its own session draft and directly performs runtime reads plus run/mark POST actions. The clear contract is that Shell frames package/workbench context and receives summarized CLI state/draft updates; the unclear contract is duplicated state polling and mixed ownership of runtime/session action state. The first safe micro-change boundary is to clarify this Shell-to-ControlPanel contract before changing behavior.

## 3. Responsibility Split

| Surface | Owns | Receives | Produces / Renders | Fetches? | Mutates? | Evidence |
| ------- | ---- | -------- | ------------------ | -------- | -------- | -------- |
| `VectorFLIntegrationShell` | package stack, selected package, modal, `cliHostState`, `workPacketDraft`, `externalFollowupTurn`, `dashboardRefresh` | static package/translation JSON imports; child callbacks | 3-column workbench, `PackageStack`, `CliHostControlPanel`, `EnginePositionSidebar`, `PackageModal` | Yes: `GET /api/vectorfl-engine/state` every 5s | React state and localStorage package/selection state | OBSERVED_FILE_EVIDENCE |
| `CliHostControlPanel` | task type, purpose, context refs, prompt payload, latest/recent returns, deposit returns, package notebooks, conversation turns, session events, runtime events, run status | `activeSurface`, `onSurfaceChange`, `onCliStateChange`, `onPacketDraftChange`, `externalFollowupTurn`, `activePackage` | CLI/session setup, package notebook panel, latest return panel, packet digest, activity rail, support controls | Yes: `GET /api/vectorfl-engine/state` | React state, sessionStorage draft, backend CLI session run/mark via POST | OBSERVED_FILE_EVIDENCE |
| Runtime viewer API | state assembly and action route dispatch | HTTP GET/POST requests | JSON state/action responses | No client fetch observed inside route handler | POST routes call session run/mark helpers that update runtime/session artifacts | OBSERVED_FILE_EVIDENCE |

## 4. Props / Data Contract

| Prop / Data Field | Source | Consumer | Required? | Observed Use | Risk |
| ----------------- | ------ | -------- | --------- | ------------ | ---- |
| `activeSurface` | Shell literal `"vectorfl"` | ControlPanel | optional; default `"vectorfl"` | selects surface template context | Shell passes a fixed surface while also passing a no-op surface change handler |
| `onSurfaceChange` | Shell `() => {}` | ControlPanel | optional | called by `focusSurface(surface)` | UI may imply surface switching while parent ignores it |
| `onCliStateChange` | Shell `setCliHostState` | ControlPanel | optional | called after `refreshLatest()` reads `cli_host_control` | parent and child both refresh state, so freshness ownership is duplicated |
| `onPacketDraftChange` | Shell `setWorkPacketDraft` | ControlPanel | optional | emits derived packet draft from current prompt/context/task type | draft is inferred from UI state, not a final packet authority |
| `externalFollowupTurn` | Shell `latestTurn` via sidebar action | ControlPanel | optional | loads selected turn into follow-up context | effect depends on session id / handoff reason; repeated same-session handoff behavior may be subtle |
| `activePackage` | Shell selected package | ControlPanel | optional | seeds purpose/prompt/context refs; filters runtime events/notebooks | changing selected package mutates ControlPanel draft state |
| `cli_host_control.latest_readable_return` | API state | Shell and ControlPanel | optional by shape | latest return display and follow-up source | absent or stale value leaves UI in fallback state |
| `cli_host_control.recent_readable_returns` | API state | Shell and ControlPanel | optional by shape | recent/latest fallback and turn count | parent type is narrower than ControlPanel type |
| `cli_host_control.deposit_ready_returns` | API state | ControlPanel, parent state copy | optional by shape | deposit-ready listing/state | semantics are route/mark-dependent, not final user judgment |
| `cli_host_control.package_run_events` | API state | ControlPanel | optional by shape | runtime activity rail and source profile signal | event mapping may hide raw sequence detail |
| `cli_host_control.package_notebooks` | API state | ControlPanel | optional by shape | package notebook panel | notebook display depends on matching `activePackage.id` |
| `WorkPacketDraft` | ControlPanel derived `currentPacket` | Shell sidebar/modal | optional callback output | shows purpose, lens, evidence, route, expected return shape | derived summary could be mistaken for a submitted packet |

## 5. API / Polling Dependency

Endpoint used:

```text
GET /api/vectorfl-engine/state
```

Action endpoints used by `CliHostControlPanel`:

```text
POST /api/vectorfl-engine/actions/cli-session/run
POST /api/vectorfl-engine/actions/cli-session/mark
```

Observed routing:

- `viewer_server.py` maps `GET /api/vectorfl-engine/state` to `build_vectorfl_integrated_engine_state(runtime_root)`.
- `build_vectorfl_integrated_engine_state` includes `"cli_host_control": build_cli_host_control_state(runtime_root)`.
- `build_cli_host_control_state` returns `latest_readable_return`, `recent_readable_returns`, `deposit_ready_returns`, `package_run_events`, `package_notebooks`, and `spine_contracts`.

Polling / refresh location:

- Shell polls `/api/vectorfl-engine/state` every 5 seconds and updates parent `cliHostState`.
- ControlPanel calls `refreshLatest()` on mount and after `runSession()`, and it can refresh manually from its button.
- ControlPanel does not show an observed interval in the inspected section; its refresh is action/mount/manual based.

Fallback / error handling:

- Shell catches refresh errors and records `dashboardRefresh.status = "error"`.
- ControlPanel catches refresh/run/mark errors and records local status plus session events.

Missing evidence:

- Live endpoint response was not tested.
- Current build health was not checked.
- Full behavior under simultaneous Shell polling and ControlPanel refresh was not verified.

## 6. Safe Micro-change Candidates

| Candidate | Why Safe | Files Involved | Expected Useful Result | Risk | Pre-change Check |
| --------- | -------- | -------------- | ---------------------- | ---- | ---------------- |
| Clarify fixed surface behavior | Shell currently passes `activeSurface="vectorfl"` and `onSurfaceChange={() => {}}`; a small UI/code clarification could reduce false surface-switch expectations | `VectorFLIntegrationShell.tsx`, `CliHostControlPanel.tsx` | Users/workers can see that this panel is locked to the VectorFL surface in the parent shell | Could touch visible UI text or surface template behavior | Confirm desired wording with Supervisor/User; then run build after patch |
| Extract or align shared contract types | Shell and ControlPanel define overlapping `CliReadableReturn`, `CliHostState`, and `WorkPacketDraft` shapes | `VectorFLIntegrationShell.tsx`, `CliHostControlPanel.tsx`, possibly a new/nearby type file later | Reduces type drift before behavior changes | Creating a shared type file is a broader change than a text/UI micro-change | Run focused build/type check after choosing this path |
| Add a small refresh ownership note/status | Both Shell and ControlPanel read the same state endpoint through different timing rules | `VectorFLIntegrationShell.tsx`, `CliHostControlPanel.tsx` | Makes polling/manual refresh distinction visible without changing API | Could add UI noise if not carefully placed | Ask whether the next micro-change should be user-visible or code-structure-only |

## 7. What Not To Do Yet

- redesign whole workbench
- mutate runtime API
- change polling architecture
- refactor state globally
- implement new control actions
- change dashboard route
- styling overhaul
- split `CliHostControlPanel` into multiple components
- treat derived packet draft as final mission-packet authority

## 8. GPT / Supervisor Review Hooks

```text
overstated:
Do not say the Shell/ControlPanel contract is stable or final.

understated:
ControlPanel is not just a child display panel; it has direct run/mark action authority.

needs downshift:
Shared type extraction may be useful, but it is still a candidate micro-change, not required architecture.

needs user priority:
Choose whether the first micro-change should be UI clarity, type contract cleanup, or refresh/status clarity.

needs Codex follow-up:
After one micro-change is selected, run a focused build/type check path or patch the chosen narrow file set only.
```

## 9. Recommended Immediate Next Step

```text
SELECT_ONE_UI_MICRO_CHANGE
```

Reason:

The contract is now narrow enough to choose a micro-change, but not enough to justify implementation without selection. The safest choices are fixed-surface clarity, shared type alignment, or refresh ownership visibility. After selection, run a focused build/type check around `app/ui/integrated_engine` before or after the patch depending on user preference.

## 10. Final Verdict

```text
UI_CONTRACT_CLARIFIED_WITH_WATCH
```

Confidence level:

Medium-high for the observed component contract; medium for runtime/API stability because no endpoint/build/test was executed.

Strongest observed contract:

Shell owns package/workbench framing and receives `cliHostState` / `workPacketDraft` from ControlPanel callbacks, while ControlPanel owns CLI session setup and run/mark actions.

Weakest missing evidence:

Current build/runtime behavior and live response compatibility were not verified.

One next recommended action:

Select exactly one UI micro-change, then verify it with a focused build/type check before treating it as implementation-ready.
