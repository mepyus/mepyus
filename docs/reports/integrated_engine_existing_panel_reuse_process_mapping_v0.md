# Integrated Engine Existing Panel Reuse Process Mapping v0

## 1. Verdict

PASS_WITH_NOTE

Existing panels should not be deleted just because they came from the Gemini/mock visual body. They should be reused only when they can be mapped to the integrated-engine process.

Reuse rule:

```text
panel survives if it helps purpose / memory / process / decision / sedimentation
panel stays support if it helps but is not the surface's central question
panel stays hold if it implies governance, supervisor authority, or runtime truth
```

## 2. Process Mapping

The integrated-engine process remains:

```text
instruction intake
-> internal search
-> evidence bundle
-> VectorFL mediation / packetization
-> User organization
-> Engine main processing
-> VectorFL reflux
-> record / sedimentation
```

## 3. Current Panel Reuse Map

| existing panel | process fit | reuse status | note |
| --- | --- | --- | --- |
| `CommandHeaderPanel` | instruction intake / purpose | active core on User | May need purpose-only simplification later. |
| `UserCliAssignmentPanel` | User organization / decision | active core on User | Correct as user decision signal. |
| `InternalTeamAssignmentPanel` | User organization / internal role assignment | active core on User | Correct large frame; persistence still absent. |
| `ExecutionRoutePanel` | route support / decision trace | support on User | Collapsed under support route/log. |
| `OperationLogPanel` | trace support | support on User | Collapsed under support route/log. |
| `CliHostControlPanel` | evidence gate / packetization / CLI tool call | active core on VectorFL | Main VectorFL operating body. |
| `VectorFLValidationQueuePanel` | VectorFL reflux / reread | active support on VectorFL | Return-to-VectorFL queue. |
| `FlowSummaryPanel` | line / intervention summary | support on VectorFL | Reused under support details. |
| `Evidence Line Atlas` | evidence line support | support on VectorFL | Useful selector; not central body. |
| `selected line inspection card` | line detail support | support on VectorFL | Keep subordinate. |
| `EngineCliReturnPanel` | request / process / return / validation / deposit candidate | active core on Engine | Now begins with process chain. |
| `IngestEntryPanel` | Engine input material | support/core candidate on Engine | Useful for future process concretization. |
| `PipelineStatusPanel` | Engine process state | support/core candidate on Engine | Useful if tied to active work package later. |
| `ValidationReturnPanel` | return material / validation target | support/core candidate on Engine | Good fit, but seeded/mock today. |
| `AssetInventoryPanel` | memory/material inventory | support on Engine | Should not become central panel. |
| `AssetInspectorPanel` | asset detail support | support on Engine | Useful after selected-object rules, currently support. |
| `WatchpointRegistryPanel` | risk / boundary support | support on Engine/VectorFL | Good if it stays boundary support. |
| `EventConsolePanel` | trace support | support | Must not become live truth. |
| `BridgePanel` | connection support | support/hold | Useful as connection trace, not bridge authority. |
| `SupervisorQueuePanel` | recommendation/support | hold | Must not read as governance or supervisor authority. |
| `SpaceHealthPanel` | broad status support | hold/support | Should not become global truth or score. |
| `FilterBarPanel` | asset support utility | support | Only useful inside support inventory. |

## 4. Reuse Principle By Surface

### User Surface

Reuse panels that help:

- set purpose
- assign to team / role
- decide / hold / send back

Do not reuse panels that force full evidence, engine process, or trace density into User.

### VectorFL Surface

Reuse panels that help:

- internal reread
- evidence bundle
- packet formation
- route / guard / validation
- line / axis support

VectorFL can be dense, but density must follow process order.

### Engine Surface

Reuse panels that help:

- shaped input
- process state
- return material
- validation/extraction/deposit candidate

Do not reuse panels as control-room or governance authority.

## 5. Immediate Watchpoint

`vectorfl_engine_surface_mock.tsx` still contains control-room and supervisor language from mock origin.

This should be read as design/support material, not final authority. The next small patch should reduce those labels toward:

- process surface
- passive support
- recommendation material
- not runtime truth

## 6. What Must Not Be Done

- Do not delete mock-derived panels without a pruning audit.
- Do not promote supervisor/governance panels to core.
- Do not make asset inventory the Engine center.
- Do not make line atlas the VectorFL center.
- Do not make team/role panels the entire User Surface.
- Do not create multi-work board before this reuse map is stable.
