# Integrated Engine Current Slot Component Inventory v0

## 1. Verdict

PASS_WITH_NOTE

This inventory describes what currently lives in center / support / inspector by surface. It is not a redesign proposal.

## 2. User Surface

### Center slot

Current components/content:

- `SingleHandlerPackagePanel` projected as User
- fields shown: purpose, scope, current target, current status, next action

First question visible:

```text
What am I trying to do, where am I, and what is the next valid action?
```

Already feels right:

- purpose-first reading
- next action visible
- package identity present without full trace

Still too dense:

- none in center slot after slot restructuring

Verification-mode-like residue:

- route/authority terms can appear indirectly through support if expanded

### Support slot

Current components/content:

- `SurfaceCurrentObjectFocus`
- `CommandHeaderPanel`
- `UserCliAssignmentPanel`

Role:

- current object focus
- material context
- decision signal / assignment candidate

Already feels right:

- support helps decision without becoming full team console

Still too dense:

- assignment candidate cards can carry route labels that feel technical

### Inspector slot

Current components/content:

- `InternalTeamAssignmentPanel`
- `ExecutionRoutePanel`
- `OperationLogPanel`

Role:

- team/role x-ray
- route/log x-ray

Still too dense:

- full team/role configuration remains large when opened

## 3. VectorFL Surface

### Center slot

Current components/content:

- `SurfaceCurrentObjectFocus`
- `SingleHandlerPackagePanel` projected as VectorFL
- `VectorFLMediationProcessMap`

First question visible:

```text
What is the currently interpreted package/object, in what state, with what evidence/blocker, and where can it route next?
```

Already feels right:

- selected package/object is central
- evidence summary and blocker appear before raw detail
- mediation process is visible without full packet internals

Still too dense:

- center has multiple substantial blocks, but they share one current-object reading

Verification-mode-like residue:

- mediation process map still uses internal process language

### Support slot

Current components/content:

- `CliHostControlPanel`
- `VectorFLValidationQueuePanel`
- `FlowSummaryPanel`

Role:

- compact session strip
- latest result/session support
- return/handoff queue
- lens/intervention summary

Already feels right:

- CliHost is no longer conceptual center
- session controls remain usable

Still too dense:

- CliHost support details are large when opened
- evidence gate / packet formation support can still feel like verification mode

### Inspector slot

Current components/content:

- evidence line atlas
- selected line inspection

Role:

- x-ray line/evidence inspection

Still too dense:

- atlas can be visually heavy
- selected line inspection remains mock-like

## 4. Engine Surface

### Center slot

Current components/content:

- `SingleHandlerPackagePanel` projected as Engine
- `EngineCliReturnPanel`

First question visible:

```text
What has the engine received, how far has processing gone, and what is being returned or redeposited?
```

Already feels right:

- process/return is front
- return and redeposit boundary are visible

Still too dense:

- `EngineCliReturnPanel` can include multiple return queues when runtime state is rich

### Support slot

Current components/content:

- `SurfaceCurrentObjectFocus`

Role:

- authority state and processing boundary support

Already feels right:

- helps avoid completion/canonical overread

### Inspector slot

Current components/content:

- `VectorFLEngineSurfaceMock`
- internal legacy mock sections, including asset/watch/trace support

Still too dense:

- legacy engine mock remains large even when placed in inspector

Verification-mode-like residue:

- asset/watch/trace material reads like a support dashboard when expanded

## 5. Validation

- Current structure accuracy: grounded in `VectorFLIntegrationShell.tsx`.
- First questions visible: yes for all three surfaces.
- Density problems captured without proposed fixes: yes.

