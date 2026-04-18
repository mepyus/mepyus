# Integrated Engine Generated UI Component Reuse Classification v0

## 1. Verdict

PASS_WITH_NOTE

The current generated UI components are not trash. They are data-bearing artifacts.

The problem is not their existence. The problem is that too many of them are currently visible as equal panels instead of being composed as projections of the same work package.

## 2. Classification Rule

Each generated component should be classified as one of:

- `projection logic`
- `surface front view`
- `surface support view`
- `process evidence`
- `hold / design clay`

Do not classify by whether the component was "right" or "wrong."

Classify by how it contributes to:

```text
same work package
-> body / camera frame / lens
-> surface-specific projection
```

## 3. Current Component Classification

| component | current value | current risk | next classification |
| --- | --- | --- | --- |
| `SharedOperatingSpine` | thin common orientation | can become dashboard | `projection logic` + minimal shell view |
| `SurfaceCurrentObjectFocus` | correct surface questions | can become three extra explanation cards | move toward `projection logic`, keep only minimal visible cue |
| `VectorFLMediationProcessMap` | shows camera frame order | can become another process card row | keep as `surface support view` or reduce into VectorFL section ordering |
| `CliHostControlPanel` | carries packet fields, evidence refs, CLI run | can look like CLI console body | `surface front view` for VectorFL only |
| `InternalTeamAssignmentPanel` | carries team/role assignment and language loop | can look like generic team console | `surface front view` for User only when tied to current work package |
| `UserCliAssignmentPanel` | receives user decision candidates | can become separate candidate feed | `surface front view` for User, but fed by current package projection |
| `EngineCliReturnPanel` | carries return/process candidate material | can become broad return feed | `surface front view` for Engine, tied to process stage |
| `FlowSummaryPanel` | useful line/flow context | can replace VectorFL center | `surface support view` |
| Evidence Line Atlas | useful evidence selector | can turn VectorFL into line browser | `surface support view` |
| selected line inspection card | useful detail | can imply selected-object behavior | `surface support view` |
| `ExecutionRoutePanel` | route/log visual grammar | can make User look like workflow board | `surface support view` |
| `OperationLogPanel` | memory/trace seed | can become dump log | `process evidence` / support |
| `VectorFLEngineSurfaceMock` | engine process visual clay | can imply control room | `hold / design clay` except process fragments |
| `AssetInventoryPanel` | material inventory support | can become engine center | `surface support view` only if tied to current package |
| `SupervisorQueuePanel` | recommendation visual clay | governance drift | `hold / design clay` |
| `BridgePanel` | connection visual clay | bridge authority drift | `surface support view` only as trace, not authority |

## 4. What This Means For Next Patch

Do not delete components.

Do not add components.

Recompose:

```text
current package projection
-> User front components
-> VectorFL front components
-> Engine front components
-> support/hold components collapsed
```

## 5. First Recomposition Target

The first recomposition target should be:

```text
SurfaceCurrentObjectFocus
```

Reason:

- It contains the right questions.
- It is currently visible as another large panel.
- It should become the source of each surface's projection summary, not another card competing for attention.

Possible safe move:

- keep its derived text
- reduce its visible footprint
- let it feed the section titles / first rows of existing panels
- avoid adding a new focus block

## 6. Second Recomposition Target

The second recomposition target should be:

```text
InternalTeamAssignmentPanel
```

Reason:

- It is not wrong.
- It is the right place for User-side assignment.
- But it must foreground "current work package assignment" before generic team setup.

Possible safe move:

- show current package assignment summary first
- keep team add/edit as secondary
- keep language 담당 loop as a role modal / assigned task

## 7. Third Recomposition Target

The third recomposition target should be:

```text
EngineCliReturnPanel
```

Reason:

- It carries useful return material.
- It needs stronger process-stage framing.
- It should not absorb User or VectorFL reasoning.

Possible safe move:

- foreground current process material
- collapse recent return feed
- keep validation/deposit candidate as candidate-only

## 8. Guardrails

- No new panel.
- No deletion as cleanup.
- No final glossary.
- No multi-work board.
- No Gemini adapter.
- No full engine process expansion.
- No "everything visible everywhere."

## 9. Locked Reuse Sentence

```text
Generated UI components are not waste.
They are evidence of attempted projection.
The next job is to make them read as surface projections of the same work package,
not as a pile of equally central panels.
```
