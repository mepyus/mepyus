# Implementation Unit 001 — Operating UI Component Tree / Props Spec

## 0. Status

- implementation-unit discovery only
- file-grounded observation only
- not implementation
- not final UI spec
- not roadmap authority
- not baseline
- requires GPT/Supervisor review

## 1. Source / Provenance Note

Files inspected:

- `app/work/space-skill-sandbox/outputs/implementation_readiness_discovery_20260509_v0.md`
- `app/ui/integrated_engine/package.json`
- `app/ui/integrated_engine/main.tsx`
- `app/ui/integrated_engine/App.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `app/ui/integrated_engine/EngineStateDashboard.tsx`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/ui/integrated_engine/useEngineSurfaceMockState.ts`
- `app/ui/integrated_engine/engine-surface.types.ts`
- `app/runtime/operating_ui_phase1_adapter.py`
- `app/core/runtime/viewer_server.py`
- `app/runtime/vectorfl_integrated_engine_api.py`

Discovery terms used:

```text
integrated_engine, engine-state-dashboard, dashboard, runtime, viewer,
api, route, component, props, state, panel
```

Directly observed:

- `main.tsx` mounts `App`.
- `App.tsx` routes `/engine-state-dashboard` to `EngineStateDashboard`; all other paths render `VectorFLIntegrationShell`.
- Both `VectorFLIntegrationShell` and `EngineStateDashboard` fetch `/api/vectorfl-engine/state` and poll every 5 seconds.
- `viewer_server.py` exposes `/api/vectorfl-engine/state` via `build_vectorfl_integrated_engine_state(runtime_root)`.
- `CliHostControlPanel` can call `/api/vectorfl-engine/actions/cli-session/run` and `/api/vectorfl-engine/actions/cli-session/mark`.

Inference:

- The first safe implementation unit should clarify UI state/data contracts before changing behavior.
- The route split creates two related but separate UI surfaces: workbench shell and dashboard.

Missing evidence:

- No build/test/run was performed.
- No screenshot or browser usability check was performed.
- The full response shape of `build_vectorfl_integrated_engine_state` was not exhaustively mapped.

Needs GPT/Supervisor review:

- Whether the first implementation unit should target the main workbench shell or `/engine-state-dashboard`.
- Whether current UI text/flow should be preserved or changed.

## 2. One-Paragraph Summary

The operating UI currently has a concrete React/Vite surface. `App.tsx` selects either the main `VectorFLIntegrationShell` or the `/engine-state-dashboard` view. The main shell owns package stack state, selected package state, modal state, packet draft state, latest CLI return state, and a three-column layout around `PackageStack`, `CliHostControlPanel`, and `EnginePositionSidebar`. The dashboard is a separate observation cockpit around `/api/vectorfl-engine/state`. The likely first narrow implementation unit is not visual redesign, but a props/data-flow clarification around `VectorFLIntegrationShell` and `CliHostControlPanel`; runtime API mutation and dashboard overhaul should not be changed yet.

## 3. Component Tree

```text
main.tsx
-> App.tsx
   -> /engine-state-dashboard: EngineStateDashboard.tsx
      -> ShellCard
      -> Metric
      -> FlowStep
      -> LensRail
      -> EventRow
   -> default route: VectorFLIntegrationShell.tsx
      -> PackageStack
      -> CliHostControlPanel.tsx
      -> EnginePositionSidebar
         -> StructureReadingSlot
      -> PackageModal
```

Node notes:

- `main.tsx`: React boot entry. `OBSERVED_FILE_EVIDENCE`.
- `App.tsx`: route/page selector based on `window.location.pathname`. `OBSERVED_FILE_EVIDENCE`.
- `EngineStateDashboard.tsx`: dashboard route, fetches and displays runtime state. `OBSERVED_FILE_EVIDENCE`.
- `VectorFLIntegrationShell.tsx`: main integrated-engine workbench shell. `OBSERVED_FILE_EVIDENCE`.
- `PackageStack`, `PackageModal`, `StructureReadingSlot`, `EnginePositionSidebar`: local components inside `VectorFLIntegrationShell.tsx`. `OBSERVED_FILE_EVIDENCE`.
- `CliHostControlPanel.tsx`: central CLI/session workbench child with callbacks to shell. `OBSERVED_FILE_EVIDENCE`.

## 4. Props / State / Data Flow Table

| Surface | File | Inputs / Props | State | Data Source | Output / UI Role | Evidence |
| ------- | ---- | -------------- | ----- | ----------- | ---------------- | -------- |
| App route selector | `App.tsx` | none | none observed | `window.location.pathname` | chooses dashboard vs shell | OBSERVED_FILE_EVIDENCE |
| React boot | `main.tsx` | `App` | error handler only | DOM root | mounts UI | OBSERVED_FILE_EVIDENCE |
| Main shell | `VectorFLIntegrationShell.tsx` | imported JSON contracts; child callbacks | `cliHostState`, `workPacketDraft`, `externalFollowupTurn`, `packages`, `selectedPackageId`, `modal`, `dashboardRefresh` | `/api/vectorfl-engine/state`; localStorage | 3-column workbench | OBSERVED_FILE_EVIDENCE |
| Package stack | `VectorFLIntegrationShell.tsx` | packages, selected id, select/create/delete/modal callbacks | draft title | local shell state | left package navigation and package creation shell | OBSERVED_FILE_EVIDENCE |
| CLI host control | `CliHostControlPanel.tsx` | active surface, callback props, active package | session draft and conversation/session state | `/api/vectorfl-engine/state`, `/actions/cli-session/run`, `/actions/cli-session/mark` | central CLI/session packet workbench | OBSERVED_FILE_EVIDENCE |
| Engine position sidebar | `VectorFLIntegrationShell.tsx` | latest turn, work packet draft, load latest callback | none observed | parent props | right-side current position / structure reading | OBSERVED_FILE_EVIDENCE |
| Package modal | `VectorFLIntegrationShell.tsx` | modal kind, package, latest turn, work packet draft | none observed | parent props | setup/result/watch modal | OBSERVED_FILE_EVIDENCE |
| Dashboard | `EngineStateDashboard.tsx` | none | `state`, `refresh` | `/api/vectorfl-engine/state`; 5-second polling | observation cockpit for flow, lens rail, events, guardrails | OBSERVED_FILE_EVIDENCE |
| Mock surface state hook | `useEngineSurfaceMockState.ts` | assets, events | selected asset id | passed arrays | derives selected asset/events/stats | OBSERVED_FILE_EVIDENCE |
| Runtime phase1 adapter | `operating_ui_phase1_adapter.py` | `live_data`, memory stickers, path residue | none | runtime live data | maps runtime payload to phase1 view model | OBSERVED_FILE_EVIDENCE |

## 5. Runtime / Viewer API Link

Endpoint:

```text
GET /api/vectorfl-engine/state
```

API files:

- `app/core/runtime/viewer_server.py` maps the endpoint to `build_vectorfl_integrated_engine_state(runtime_root)`.
- `app/runtime/vectorfl_integrated_engine_api.py` defines `build_vectorfl_integrated_engine_state`.

Visible consumer components:

- `VectorFLIntegrationShell.tsx`
- `EngineStateDashboard.tsx`
- `CliHostControlPanel.tsx`

Visible response shape:

- `EngineStateDashboard.tsx` expects `current_posture`, `core_sentence`, `cli_host_control`, `session_worker_policy`, `guard`, and `next_implementation_boundary`.
- `VectorFLIntegrationShell.tsx` reads `result.cli_host_control`.
- `CliHostControlPanel.tsx` reads `cli_host_control` and package notebook/session related structures.

Missing evidence:

- Full API response shape was not exhaustively documented in this pass.
- Runtime endpoint was not called.
- No current browser verification was performed.

Risk:

- UI components duplicate assumptions about `/api/vectorfl-engine/state` shape.
- Runtime API changes could break both shell and dashboard.
- Some shell state is stored in localStorage/sessionStorage, so persistence behavior needs caution.

## 6. First Implementation Unit Candidate

```text
candidate:
Document and tighten the VectorFLIntegrationShell <-> CliHostControlPanel props/data contract.

why this unit:
It is the central handoff between selected package, work packet draft, CLI/session state, and runtime polling. It is narrower than redesigning the dashboard or mutating the runtime API.

files involved:
- app/ui/integrated_engine/VectorFLIntegrationShell.tsx
- app/ui/integrated_engine/CliHostControlPanel.tsx
- app/ui/integrated_engine/engine-surface.types.ts
- app/runtime/vectorfl_integrated_engine_api.py only as read-only response-shape reference

expected useful result:
A small implementation-ready spec that names required props, callback outputs, runtime fields consumed, and which state belongs in parent shell vs CLI panel.

required user decision:
Should the first UI micro-change improve package/workbench clarity, or should it only document and stabilize the existing data contract?

risk:
Changing central props without build/test can break both package workbench and CLI session flow.

pre-change check:
Run `npm run build` in `app/ui/integrated_engine` only after user approval.
```

## 7. What Not To Do Yet

- broad UI redesign
- dashboard overhaul
- runtime API mutation
- styling refactor without behavior clarity
- state architecture change
- automation
- production claim
- changing CLI/session execution behavior
- editing localStorage/sessionStorage persistence behavior without explicit reason

## 8. Gaps / Missing Evidence

```text
gap:
current build/test/run status
why it matters:
file presence and historical reports do not prove current build health
current evidence:
package.json scripts and prior dashboard implementation note
recommended next check:
RUN_BUILD_TEST_CHECK after user approval
```

```text
gap:
full runtime state contract
why it matters:
three UI surfaces consume `/api/vectorfl-engine/state`
current evidence:
consumer-side expected fields and API builder function existence
recommended next check:
read focused return shape in `build_vectorfl_integrated_engine_state` or call endpoint in a later run
```

```text
gap:
visual/user workflow priority
why it matters:
component contract work differs from UX redesign
current evidence:
shell and dashboard are both present
recommended next check:
ASK_USER_UI_PRIORITY
```

```text
gap:
safe edit boundary
why it matters:
central shell and CLI panel are coupled
current evidence:
callbacks and shared state observed
recommended next check:
write a tiny pre-change checklist before code edits
```

## 9. GPT / Supervisor Review Hooks

```text
overstated:
- Do not call this implementation-ready until build/test/run is checked.
- Do not treat this spec as final UI architecture.

understated:
- The UI implementation surface is concrete: route, shell, dashboard, API polling, CLI actions, and type files exist.

needs downshift:
- "data contract" here is observed consumer expectation, not a formal API schema.

needs user priority:
- choose documentation/stabilization vs actual UI micro-change.

needs Codex follow-up:
- focused build check or selected micro-change plan.

needs Gemini audit:
- only if broader UI/flow comparison is needed after a concrete target is selected.
```

## 10. Recommended Immediate Next Step

`GPT_REVIEW_COMPONENT_SPEC`

Reason:

This spec identifies the central UI implementation unit but does not choose the user-facing micro-change. GPT/Supervisor should review whether the first action should be a build check, a contract clarification, or a tiny UI clarity change.

## 11. Final Verdict

`IMPLEMENTATION_UNIT_SPEC_CREATED_WITH_WATCH`

confidence level:
medium-high for component tree and data-flow observation; medium for readiness because no build/run was executed.

strongest observed implementation surface:
`VectorFLIntegrationShell.tsx` and `CliHostControlPanel.tsx` form a concrete central workbench around package selection, CLI/session state, runtime polling, and work packet draft callbacks.

weakest missing evidence:
current build/test/run status and full runtime response contract.

one next recommended action:
GPT/Supervisor should review this spec and choose between `RUN_BUILD_TEST_CHECK`, `SELECT_UI_MICRO_CHANGE`, or contract-only stabilization.
