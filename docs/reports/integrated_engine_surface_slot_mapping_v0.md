# Integrated Engine Surface Slot Mapping v0

## 1. Verdict

PASS_WITH_NOTE

The current screen now maps existing panels into center / support / inspector slots instead of letting panels compete as equal blocks.

## 2. User Surface Mapping

| slot | current implementation | reading |
| --- | --- | --- |
| center | `SingleHandlerPackagePanel` projected as User | purpose, scope, target, status, next action |
| support | `SurfaceCurrentObjectFocus`, `CommandHeaderPanel`, `UserCliAssignmentPanel` | current object focus, material context, decision signal |
| inspector | `InternalTeamAssignmentPanel`, `ExecutionRoutePanel`, `OperationLogPanel` | team/role routing and route/log x-ray |

Demoted from front:

- full team routing
- full role configuration
- packet origin detail
- bridge/lower trace detail

## 3. VectorFL Surface Mapping

| slot | current implementation | reading |
| --- | --- | --- |
| center | `SurfaceCurrentObjectFocus`, `SingleHandlerPackagePanel`, `VectorFLMediationProcessMap` | interpreted object, state, evidence, blocker, route |
| support | `CliHostControlPanel`, `VectorFLValidationQueuePanel`, `FlowSummaryPanel` | compact session, return queue, lens/intervention summary |
| inspector | line atlas, selected line inspection | x-ray evidence / line inspection |

Demoted from front:

- full evidence bundle
- packet formation detail
- recent turn list
- latest return detail
- line atlas
- selected line inspection

## 4. Engine Surface Mapping

| slot | current implementation | reading |
| --- | --- | --- |
| center | `SingleHandlerPackagePanel`, `EngineCliReturnPanel` | ingest/process/validation/return/redeposit |
| support | `SurfaceCurrentObjectFocus` | object authority and processing boundary |
| inspector | `VectorFLEngineSurfaceMock` | legacy asset/watch/trace and generated design clay |

Demoted from front:

- full asset inventory
- watcher recommendations
- runtime artifact tree
- supervisor-like queue behavior
- full bridge contract text

## 5. Same Process / Different Projection

The same `language_handler_loop_pkg_v0` is still the underlying process object.

It is projected differently:

- User reads it as purpose/status/next action.
- VectorFL reads it as mediation material.
- Engine reads it as process/return material.

## 6. Validation

- Cleaner first questions: passed.
- Slot separation: passed with note.
- Same-process/same-projection confusion: reduced.
- Remaining risk: inspector areas can still become visually heavy when opened.

