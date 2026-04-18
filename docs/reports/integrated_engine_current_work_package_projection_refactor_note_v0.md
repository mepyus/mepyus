# Integrated Engine Current Work Package Projection Refactor Note v0

## 1. Verdict

PASS.

This round did not add a visible feature. It introduced a shared derived `CurrentWorkPackage` object inside the integrated-engine shell so the shared spine and the three surface-local focus layers read from the same current operating object.

## 2. Why This Was Needed

The UI had started to show the right idea visually:

- shared spine
- User local focus
- VectorFL local focus
- Engine local focus

But the code still recomputed route, state, authority, surface role, next action, and evidence readiness separately inside each component. That is a hidden version of the same problem the user flagged on the screen: the surfaces looked connected, but the common object was not strong enough underneath.

## 3. What Changed

Added local type:

- `CurrentWorkPackage`

Added builder:

- `buildCurrentWorkPackage(turn, packetDraft)`

The object now gathers:

- current turn/session id
- purpose
- route
- packet state
- authority state
- evidence readiness
- evidence note
- surface-specific role readings
- surface-specific next action candidates

The object is derived with `useMemo`:

- `currentWorkPackage = buildCurrentWorkPackage(sharedTurn, workPacketDraft)`

And passed to:

- `SharedOperatingSpine`
- `SurfaceCurrentObjectFocus` for User
- `SurfaceCurrentObjectFocus` for VectorFL
- `SurfaceCurrentObjectFocus` for Engine

## 4. What This Does Not Change

- No backend change.
- No manifest shape change.
- No new persisted object.
- No new panel.
- No new route.
- No runtime binding or ingestion automation.
- No multi-work board.

This is a local shell projection refactor only.

## 5. Why This Matters

The current screen goal is not to list every panel. It is to let one work package be read through different lenses:

- User lens: assignment / decision / hold
- VectorFL lens: evidence / mediation / reread / route
- Engine lens: request / process / return / validation / deposit candidate

By deriving one `CurrentWorkPackage`, the UI code now expresses that principle more directly. The common object is formed once, then projected differently.

## 6. Verification

Passed:

- `npm run build` in `app/ui/integrated_engine`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Remaining Watchpoints

1. `CurrentWorkPackage` is still local UI projection, not canonical runtime state.
2. It should not be promoted into manifest/runtime schema until real use proves the fields.
3. If more panels need the same state, they should consume this projection rather than recompute route/authority differently.

## 8. Next Smallest Step

Continue pruning scattered surface-local interpretations. The next likely candidate is route/mark wording inside User and Engine candidate lists, where internal labels still appear directly but should remain badge/support unless they carry operational meaning.
