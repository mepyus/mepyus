# Integrated Engine Work Packet Generation Gap And Screen Reread Note v0

## 1. Verdict

PASS_WITH_NOTE

The fixed 3-surface body and CLI on-top interpretation are still intact.

The current gap is not that the UI lacks a context preset. The gap is that the first CLI turn is not yet formed as an integrated-engine work packet by the engine itself. The user is still assembling the initial packet by hand.

## 2. Fixed Body Interpretation

| body part | locked role | current reading |
| --- | --- | --- |
| User Surface | purpose / assignment / decision / internal team operation | holds goal, team, role, assignment candidate, and decision signals |
| VectorFL Surface | interpretation / mediation / internal-search trigger / reread / route sorting | currently holds CLI conversation, handoff queue, line atlas support, marks, latest return |
| Engine Surface | processing / return / validation feed / extraction and deposit candidate | currently shows CLI returns, engine request candidates, validation queue, deposit material, and engine mock body |
| CLI on-top layer | tool / actor layer attached to the 3-surface body | currently runnable through VectorFL; not a fourth surface |

The body is correct. The weak point is before execution: the body does not yet create the first work packet from its own assets.

## 3. Current Structural Gap

The engine cannot yet form the first CLI work packet by itself because its assets are still mostly exposed as references, panels, or previous notes, not as an operating object.

Current asset state:

- 기준문 / lock docs exist.
- line / axis / source pointers exist.
- CLI session artifacts exist.
- route marks exist.
- language loop artifacts exist.
- panel relationship notes exist.

Missing operating object:

- no current packet frame that says: "for this user instruction, these are the governing locks, these are the relevant lines/axes, this is the lens, this is the evidence bundle, this is the expected return shape, and this is the next route candidate."

So the user is forced to do the packet-forming step:

```text
user instruction
-> user manually recalls basis documents
-> user picks context refs
-> user rewrites purpose into task form
-> user chooses task type
-> user implies output contract
-> user predicts route
-> CLI run
```

The intended flow should be:

```text
user instruction
-> VectorFL rereads current locks / lines / axes / pointers
-> VectorFL shapes first work packet
-> CLI executes as on-top tool
-> Engine return candidate
-> VectorFL reread / validation
-> User decision or deposit candidate
```

The root cause is not input friction. The root cause is that "current work packet generation" is not yet a visible or structured responsibility in the VectorFL surface.

## 4. User-As-Packet-Assembler Breakdown

| user is currently doing | actually belongs to | why |
| --- | --- | --- |
| 기준 세트 연결 | VectorFL | the mediation surface should know which locks and current state docs govern this turn |
| 문맥 복구 | VectorFL | reread and memory recovery are VectorFL responsibilities before tool execution |
| 목적을 작업 단위로 번역 | User + VectorFL | User supplies intent; VectorFL should shape it into a bounded packet |
| 요청 유형 결정 | VectorFL | inspect / reread / validate / summarize is a route/lens decision, not raw user burden |
| 출력 기대 형식 설정 | VectorFL + Engine | VectorFL sets return contract; Engine produces material in that contract |
| 다음 route 예상 | VectorFL | route candidate is mediation output, not something the user should infer each time |
| 파일 경로 수동 조립 | VectorFL support | source pointers should become evidence bundle candidates |
| 결과가 어느 면으로 가야 하는지 판단 | VectorFL + User | VectorFL proposes route; User approves decision/promotion when needed |

This is exactly the "packet assembler" role. The current UI proves the CLI path works, but it also shows that the first packet assembler is still the user.

## 5. Screen Reread By Surface

### User Surface

What it shows:

- goal / scope through `CommandHeaderPanel`
- CLI assignment candidates through `UserCliAssignmentPanel`
- internal team and role setup through `InternalTeamAssignmentPanel`
- language loop under the language role
- route support through `ExecutionRoutePanel`
- log support through `OperationLogPanel`

What is structurally clear:

- User Surface is moving toward organization / assignment / decision.
- Internal team / language 담당 framing is correct for work that belongs to user-side operation.

What remains weak:

- It can receive assignment candidates, but the first packet is not visibly born from a user purpose.
- Team/role setup is useful, but it does not yet clarify how a raw user instruction becomes a work packet before CLI execution.

### VectorFL Surface

What it shows:

- `FlowSummaryPanel`
- Line Atlas support
- `VectorFLValidationQueuePanel`
- `CliHostControlPanel`
- selected line inspection card

What is structurally clear:

- CLI is on-top and mainly operated through VectorFL.
- VectorFL can load returns from User/Engine for reread.
- VectorFL can mark latest return as reread, validation, engine request, deposit, user assignment, or hold.

What remains weak:

- The main CLI area still reads as "task type + purpose + context refs + prompt + send" more than "VectorFL forms a work packet from current locks and evidence."
- Current 기준문 / lock / line / axis material is not shown as an evidence bundle selected by VectorFL.
- The surface exposes the execution input fields, but does not yet expose the mediation act that should fill them.

### Engine Surface

What it shows:

- `EngineCliReturnPanel`
- engine request candidates
- validation queue
- extraction / deposit material queue
- `VectorFLEngineSurfaceMock`

What is structurally clear:

- Engine Surface receives processing / return / validation / deposit candidate material.
- It does not currently look like the primary authority; it reads as return/process material.

What remains weak:

- Formal request-packet generation from engine request candidates is not visible.
- Engine output can become material, but sedimentation into memory is still candidate-only.

## 6. Panel Classification

Classification criterion: direct contribution to work packet generation, movement, reread, or sedimentation.

### Active Core

| panel/component | reason |
| --- | --- |
| `VectorFLIntegrationShell` | current 3-surface body and active operating shell |
| `CliHostControlPanel` | on-top CLI turn execution and mark surface |
| `CommandHeaderPanel` | user purpose / task identity source |
| `UserCliAssignmentPanel` | user-side decision / assignment candidate receiver |
| `InternalTeamAssignmentPanel` | user-side team/role operation frame |
| `VectorFLValidationQueuePanel` | return-to-VectorFL reread path |
| `EngineCliReturnPanel` | engine return / validation / deposit candidate path |

### Support

| panel/component | reason |
| --- | --- |
| `FlowSummaryPanel` | lifecycle orientation support, but not packet formation by itself |
| `ExecutionRoutePanel` | route support, but currently secondary to CLI marks |
| `OperationLogPanel` | memory/trace support; not yet a live packet trace |
| `Line Atlas` inside VectorFL shell | line-selection support; should not become VectorFL center |
| `selected line inspection card` | evidence support |
| `VectorFLEngineSurfaceMock` | engine body support / mock-derived processing view |
| `AssetInventoryPanel` | asset evidence support when used through engine mock |
| `AssetInspectorPanel` | asset detail support |
| `BridgePanel` | connection trace support |
| `WatchpointRegistryPanel` | warning/failure evidence support |
| `OperationConsolePanel` | internal process support, not core |

### Hold

| panel/component | reason |
| --- | --- |
| `TeamRoutingPanel` | overlaps with internal team/assignment frame; needs promotion gate before core use |
| `RoleConfigurationPanel` | overlaps with current role setup |
| `SupervisorQueuePanel` | risks governance/control-room drift |
| old mock-derived panels not mounted in the main shell | design material only until proven against packet lifecycle |

### Removable

No immediate deletion target should be named in this round.

The right action is not deletion yet. The older mock panels should remain proposal/support material until the read-only pruning audit decides whether they duplicate active core or still carry useful visual grammar.

## 7. Lifecycle Visibility Check

Target lifecycle:

```text
User purpose
-> VectorFL packet formation
-> Engine candidate
-> VectorFL reread
-> deposit candidate
```

Current visibility:

| lifecycle step | visible now? | note |
| --- | --- | --- |
| User purpose | partial | `CommandHeaderPanel` and CLI purpose field both exist, but their relation is not unified |
| VectorFL packet formation | weak | user manually fills task, context refs, and prompt; packet formation is implicit |
| Engine candidate | partial | `engine_request_candidate` route exists, but formal request packet is not visible |
| VectorFL reread | good after return | handoff queue and continue-from-turn flow exist |
| deposit candidate | partial | candidate state is visible; actual sedimentation remains intentionally closed |

Where the flow breaks:

The break is between User purpose and VectorFL packet formation.

The current screen shows execution inputs and result marks, but it does not show how the current instruction is converted into:

- governing locks
- evidence bundle
- task lens
- do / do-not guard
- expected return shape
- route candidate

Because that conversion is hidden, the user supplies it manually.

## 8. Single Highest-Priority Structural Correction

Add a visible "current work packet formation" layer in the VectorFL surface.

This is not a context preset patch.

It should be treated as the missing operating object between raw user purpose and CLI execution. Its job is to display the first packet before `Send Codex Turn`:

- user purpose being interpreted
- active governing locks
- selected evidence/source pointer bundle
- task lens
- do / do-not guard
- expected return shape
- next route candidate
- whether internal search was used or skipped as a named fast-path exception

The correction is structural because it moves packet assembly back from the user into VectorFL mediation.

## 9. Watchpoints

1. Do not turn this into a simple context preset list. Presets may later support the packet, but they are not the packet.
2. Do not make CLI the packet owner. CLI executes the packet; VectorFL forms and mediates it.
3. Do not promote old mock panels just because they look useful. Classify by contribution to packet lifecycle.
4. Do not make User Surface responsible for evidence assembly. User gives purpose, constraints, assignment, and decision.
5. Do not make Engine Surface responsible for route judgment. Engine processes and returns material.

## 10. What Must NOT Be Done Next

- Do not implement Gemini adapter.
- Do not add async/background run support.
- Do not add session history browsing as the next fix.
- Do not patch only the placeholder text in the CLI input fields.
- Do not add broad context presets as the main correction.
- Do not redesign the 3 surfaces.
- Do not delete old panels in this step.
- Do not start a final glossary or UI copy translation pass.
- Do not treat the current issue as "user needs easier file picking."

The next step should be a bounded design/implementation brief for the VectorFL current work packet formation layer, after one quick UI read confirms the same break from the live screen.
