# Integrated Engine Surface Projection Reasoning Chain v0

## 1. Verdict

PASS_WITH_NOTE

This is the required reasoning chain before any no-new-panel composition patch.

## 2. Active Lens

Current active lens:

```text
CLI on-top operation + Koreanization / internal-language work support
```

This is not a new body.
It is a task lens attached to the fixed body.

## 3. Current Work Package

Current work package:

```text
User wants to operate Codex from the integrated engine while preserving the body/camera/lens structure and collecting Koreanization / internal-language operating data.
```

Current package is not yet a formal persisted object.
It is currently assembled from:

- User goal / instruction
- CLI latest turn
- VectorFL packet draft
- language-loop state
- user assignment candidate
- engine return / deposit candidate

## 4. Camera Frame Stage

Current primary stage:

```text
VectorFL mediation / packetization
```

Supporting stages present but thin:

- instruction intake: visible through User goal and CLI purpose
- internal search: refs-based and not yet full
- evidence bundle: thin / inferred
- User organization: visible through internal team assignment
- Engine processing: visible as return material, not full process
- VectorFL reflux: visible through handoff queue
- sedimentation: deposit candidate only

## 5. Surface Projection

### User Projection

User should see:

```text
What is the current work package asking me to decide or assign?
Which internal team/role should hold it?
What is only candidate/hold/not canonical?
```

User should not have to see:

- full evidence refs
- full VectorFL mediation chain
- engine internals
- raw artifact paths

### VectorFL Projection

VectorFL should see:

```text
What evidence and guards shape this package?
Is it grounded enough to send to a tool / user / engine / hold?
What needs reread after return?
```

VectorFL can remain dense, but density must be process ordered.

### Engine Projection

Engine should see:

```text
What request/process material exists?
What returned?
What is validation or deposit candidate only?
```

Engine should not absorb:

- User assignment mechanics
- full VectorFL reasoning
- governance/supervisor authority

## 6. Existing Components To Reuse

### Reuse as projection logic

- `SurfaceCurrentObjectFocus`

It contains the right questions, but should stop being a large standalone panel.

### Reuse as User front view

- `UserCliAssignmentPanel`
- `InternalTeamAssignmentPanel`

They should foreground current package assignment/decision, not generic team management.

### Reuse as VectorFL front view

- `CliHostControlPanel`
- `VectorFLValidationQueuePanel`

They should remain the densest operational body.

### Reuse as Engine front view

- `EngineCliReturnPanel`

It should foreground current process material and keep recent returns as support.

## 7. What To Hide / Demote

Demote or keep collapsed:

- large surface-local focus card behavior
- flow summaries that are not current-package decisions
- line atlas as central browser
- broad recent return feeds
- mock supervisor/governance panels

## 8. Patch Permission

Proceed only with a no-new-panel composition patch:

```text
reduce SurfaceCurrentObjectFocus into a compact projection cue
keep existing panels
do not add new panel family
do not add multi-work board
do not add new backend behavior
```

## 9. Success Test

After the patch:

```text
The user should not feel that another panel was added.
The user should feel that each surface now receives the same work package through a different lens.
```
