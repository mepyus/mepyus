# Integrated Engine Three-Surface Screen Relationship Reset Note v0

## Verdict

PASS_WITH_NOTE

## Purpose

This note re-establishes the relationship between the older mock-derived screen pieces and the new CLI-on-top operating pieces added today.

No implementation changes are opened here. This is a closeout map for tomorrow's real UI validation.

## Current Main Screen Body

The current main UI body is:

```text
app/ui/integrated_engine/VectorFLIntegrationShell.tsx
```

It keeps the fixed 3-surface shell:

- User Surface
- VectorFL Surface
- Engine Surface

The CLI layer is not a fourth surface. It is an on-top operating layer, mainly observed and steered through the VectorFL surface.

## Surface Relationship

| surface | central job | current primary panels | newly added relation |
| --- | --- | --- | --- |
| User Surface | purpose / assignment / decision organization | `CommandHeaderPanel`, `UserCliAssignmentPanel`, `InternalTeamAssignmentPanel`, `ExecutionRoutePanel`, `OperationLogPanel` | CLI turns marked `user_assignment_candidate` can become local assignment candidates for selected team/role |
| VectorFL Surface | reread / mediation / validation / CLI conversation | `FlowSummaryPanel`, `Line Atlas`, `VectorFLValidationQueuePanel`, `CliHostControlPanel`, line inspection card | Codex conversation turns live here; User/Engine handoffs return here for reread/validation |
| Engine Surface | processing return / validation feed / deposit candidate material | `EngineCliReturnPanel`, `VectorFLEngineSurfaceMock` | CLI turns marked `engine_request_candidate` appear as request candidates, and `deposit_candidate` remains candidate-only |

## Existing Mock-Derived Pieces To Keep

These still serve the 3-surface operating body:

- `CommandHeaderPanel.tsx`
  - Keep as User surface goal/scope/material context.
- `FlowSummaryPanel.tsx`
  - Keep as VectorFL surface summary band.
- `vectorfl_engine_surface_mock.tsx`
  - Keep as Engine surface process/return visual body for now.
- `ExecutionRoutePanel.tsx`
  - Keep as User surface route/assignment support.
- `OperationLogPanel.tsx`
  - Keep as User surface log support.
- `ui-components.tsx`
  - Keep as local UI primitive layer.

## Newly Added Pieces To Treat As Active

- `CliHostControlPanel.tsx`
  - Active VectorFL CLI conversation/control layer.
  - Sends Codex turns.
  - Shows latest/recent returns.
  - Marks reread / user assignment / engine request / validation / deposit / hold.

- `UserCliAssignmentPanel`
  - Active User surface bridge from VectorFL CLI return to work organization.
  - Shows only `user_assignment_candidate` turns.

- `InternalTeamAssignmentPanel`
  - Active User surface team/role framework.
  - Currently UI-local.
  - Koreanization loop lives inside the language 담당 role modal.

- `EngineCliReturnPanel`
  - Active Engine surface return/request/deposit candidate view.
  - Shows `engine_request_candidate` without executing.

- `VectorFLValidationQueuePanel`
  - Active VectorFL reread/validation queue.
  - Receives handoffs from User and Engine surfaces.
  - UI-local for now.

## Pieces To Hold / Not Treat As Current Core

The following files exist but should not be treated as the current core operating path unless reopened deliberately:

- `TeamRoutingPanel.tsx`
- `RoleConfigurationPanel.tsx`
- `OperationConsolePanel.tsx`
- `SupervisorQueuePanel.tsx`
- `BridgePanel.tsx`
- `WatchpointRegistryPanel.tsx`
- `AssetInventoryPanel.tsx`
- `AssetInspectorPanel.tsx`
- `EventConsolePanel.tsx`
- `SpaceHealthPanel.tsx`
- `MaterialContextPanel.tsx`
- `FilterBarPanel.tsx`

They may still be useful as visual or design material, but the current main path has absorbed or replaced their immediate role through:

- User surface team/role desk
- VectorFL CLI conversation layer
- Engine request/deposit candidate panels

Do not delete these yet. The safer next move is to label them as proposal/support candidates before pruning.

## What Should Not Be Mixed

- User surface team/role organization must not become VectorFL reread logic.
- VectorFL CLI conversation must not become a fourth surface.
- Engine request candidates must not look like executed engine jobs.
- Deposit candidate must not look like canonical memory.
- Mock line atlas must not become the whole VectorFL center of gravity.
- Old governance/supervisor panels must not re-enter as core authority panels without a promotion gate.

## Tomorrow Work Lock

Tomorrow should start with real UI validation, not more abstract documents.

Recommended validation path:

1. Open the main UI.
2. Send one Codex turn from VectorFL.
3. Mark one turn as `user_assignment_candidate`.
4. Confirm it appears on User surface and can attach to a selected role.
5. Mark one turn as `engine_request_candidate`.
6. Confirm it appears on Engine surface as candidate-only.
7. Send the Engine candidate back to VectorFL.
8. Confirm it appears in VectorFL validation/reread queue.
9. Mark a candidate as `deposit_candidate`.
10. Confirm the deposit artifact says candidate-only / not ingested.

## Current Recommendation

Keep all existing files for now.

Next cleanup should be a read-only pruning audit:

- active core
- active support
- proposal/hold
- removable later

No deletion should happen before the first full real UI validation pass.
