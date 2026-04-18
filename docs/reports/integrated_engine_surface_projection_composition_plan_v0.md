# Integrated Engine Surface Projection Composition Plan v0

## 1. Verdict

PASS_WITH_NOTE

This plan narrows the next implementation to composition, not expansion.

The next patch should not create new panels. It should recompose existing panels so each surface receives the same work package through the correct lens.

## 2. Current Mistake To Correct

Current UI tendency:

```text
same data -> many panels -> every surface sees too much
```

Correct UI direction:

```text
same work package -> body/camera/lens -> surface-specific projection
```

## 3. Fixed Terms

### Body

The 3 surfaces:

- User
- VectorFL
- Engine

### Camera Frame

The common process:

```text
instruction intake
-> internal search
-> evidence bundle
-> mediation / packetization
-> organization
-> engine processing
-> reflux
-> sedimentation
```

### Lens

The current task purpose:

- translation / Koreanization
- validation
- implementation
- self-learning
- structure alignment
- external material analysis

### Projection

What each surface should show from the same work package.

## 4. Next Patch Target

Target:

```text
existing panel recomposition for one active work package
```

Not target:

```text
new object registry
new multi-work board
new dashboard
new panel family
```

## 5. Surface Projection Rules

### User Surface Projection

Front:

- current work in human language
- decision needed
- assignment / team / owner
- do / do-not
- approval / hold / return-to-VectorFL candidate

Back / collapsed:

- detailed evidence refs
- raw CLI return
- engine internal logs
- line atlas
- event console

Existing panels to keep front:

- `CommandHeaderPanel`
- `UserCliAssignmentPanel`
- `InternalTeamAssignmentPanel`

Existing panels to keep collapsed:

- `ExecutionRoutePanel`
- `OperationLogPanel`

Composition test:

```text
Can the user decide or assign without learning engine internals?
```

### VectorFL Surface Projection

Front:

- current instruction reading
- internal search state
- evidence bundle
- branch / route reasoning
- guard / do-not
- reread / validation queue
- next movement candidate

Back / collapsed:

- decorative line browser material
- broad flow summaries that do not affect current routing
- raw artifact paths unless needed for evidence

Existing panels to keep front:

- `CliHostControlPanel`
- `VectorFLValidationQueuePanel`

Existing panels to keep support:

- `FlowSummaryPanel`
- Evidence Line Atlas
- selected line inspection

Composition test:

```text
Can VectorFL judge whether the work package is grounded enough to move?
```

### Engine Surface Projection

Front:

- process input
- processing stage
- generated / translated / extracted return
- validation target
- deposit candidate material
- failure / uncertainty

Back / collapsed:

- User assignment details
- VectorFL full mediation reasoning
- supervisor / governance / control-room language
- global asset inventory unless tied to current work package

Existing panels to keep front:

- `EngineCliReturnPanel`
- process chain parts from `vectorfl_engine_surface_mock.tsx` only when tied to current work package

Existing panels to keep collapsed/support:

- `AssetInventoryPanel`
- `AssetInspectorPanel`
- `WatchpointRegistryPanel`
- `EventConsolePanel`
- `BridgePanel`

Hold:

- `SupervisorQueuePanel` as authority
- global control-room framing

Composition test:

```text
Can Engine read what to process and what returned without absorbing User or VectorFL roles?
```

## 6. One Active Lens For First Composition Patch

Use the current active lens:

```text
translation / Koreanization data loop
```

Why:

- it is already present in User Surface as internal language 담당
- it has a real loop path
- it exposes the core problem: user should see assignment, VectorFL should see language evidence/routing, Engine should see process/harvest return

## 7. First Patch Shape

Do only this:

1. derive a small `surfaceProjection` object from the current work package / CLI / language loop state
2. feed it into existing surface sections
3. demote panels that do not match the current surface projection
4. rename only if necessary for human-first reading

Avoid:

- new visible panel
- new surface
- new persistence model
- multi-work list
- broad redesign

## 8. Validation Questions

After the patch:

### User

```text
Do I know what task is assigned and what I must decide?
```

### VectorFL

```text
Do I know what evidence / route / reread judgment is active?
```

### Engine

```text
Do I know what process material exists and what returned?
```

### Whole Body

```text
Do these feel like three lenses over the same work package,
not three dashboards sharing random data?
```

## 9. Stop Conditions

Stop the patch if:

- a new panel feels necessary
- every surface starts showing the same dense object
- User must understand Engine internals
- Engine must understand User assignment reasoning
- VectorFL becomes a generic dashboard
- the work package is still not the common object

## 10. Next Implementation Lock

Next implementation should be:

```text
surfaceProjection composition patch for existing panels
```

It should be judged by:

```text
same body, same camera frame, different surface lens
```

not by:

```text
more visible information
```
