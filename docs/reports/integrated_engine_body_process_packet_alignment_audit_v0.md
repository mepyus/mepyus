# Integrated Engine Body Process Packet Alignment Audit v0

## 1. Verdict

PASS_WITH_NOTE

The current UI now has a fixed 3-surface body, a shared operating spine, surface-local focus layers, and a VectorFL current packet layer. These are useful structural advances.

However, the UI still does not fully embody the integrated-engine process physiology from the 04-17 source notes. It is strongest at frame / mediation / candidate visibility, and weakest at internal search, evidence bundle formation, Engine process concretization, and sedimentation.

## 2. Fixed Body Interpretation

The fixed body remains valid:

| surface | body role | current implementation reading |
| --- | --- | --- |
| User Surface | organization / assignment / approval / decision | goal header, assignment candidates, internal team desk, route board, log |
| VectorFL Surface | interpretation / mediation / internal search trigger / packet formation / reread | shared spine, local focus, current packet layer, CLI operator, validation queue, evidence atlas |
| Engine Surface | process / input / generation / translation / extraction / flow / return material | engine return panel, engine request candidates, validation/extraction queues, mock ingest/pipeline/body |
| CLI on-top | operator/tool layer | Codex run path and return artifacts |

The problem is not the surface split. The problem is whether each work packet actually passes through the body physiology:

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

## 3. Why Multi-Work Board Is Not The Immediate Next Step

A multi-work board is necessary later, but it should not be implemented next.

Reason:

- The current UI can only weakly prove that one work package carries the full process physiology.
- If multiple work items are added now, they will likely become a larger list of shallow latest-turn/session/candidate cards.
- The 04-17 source notes place internal search, evidence bundle formation, Engine process concretization, asset state classification, learning-event classification, and surface language before a multi-work overview.

The immediate gap is not "we cannot list many works." The immediate gap is:

```text
each work package does not yet visibly carry purpose / memory / process / decision / sedimentation through the 8-step process.
```

So a multi-work board now would multiply the gap instead of solving it.

## 4. Current Work Package Reading

### Purpose

Current coverage: medium.

Visible in:

- `CommandHeaderPanel` goal field
- `CliHostControlPanel` turn purpose
- `SharedOperatingSpine` current purpose
- `SurfaceCurrentObjectFocus` local focus text

Gap:

- User goal and CLI purpose can diverge.
- Purpose is visible, but not yet normalized as one work package purpose.

### Memory

Current coverage: weak.

Visible in:

- bounded context refs in VectorFL packet detail
- Evidence Line Atlas support
- OperationLogPanel as older log/support
- latest session artifacts and return previews

Gap:

- memory is still file refs, mock line atlas, or logs.
- memory is not yet a forced prior input that changes the current task.
- there is no explicit "internal memory/evidence was searched and selected" state.

### Process

Current coverage: weak to medium.

Visible in:

- CLI run status
- EngineCliReturnPanel processing status
- `vectorfl_engine_surface_mock.tsx` ingest/pipeline panels
- route/mark movement

Gap:

- Engine process still reads partly as return/candidate feed or mock status.
- input / generation / translation / extraction / flow are not yet tied to the active work package.
- internal search process and main processing process are not clearly separated.

### Decision

Current coverage: medium.

Visible in:

- route marks
- UserCliAssignmentPanel decision signal
- authority state in shared spine and local focus
- hold / validation / deposit candidate marks

Gap:

- decision state is now more visible, but it is still derived from marks and local panel wording.
- user approval / assignment / hold / deposit decisions are not yet a formal decision material layer.

### Sedimentation

Current coverage: weak to medium.

Visible in:

- deposit candidate count
- deposit candidate preview
- `not_ingested / not canonical` authority state
- OperationLogPanel / route history

Gap:

- sedimentation is candidate-only.
- there is no visible asset-state classification for whether a result becomes body asset / operating asset / space asset / hold asset / external reference asset.
- deposit candidate does not yet feed memory.

## 5. Four-Layer Packet Audit

| packet layer | current coverage | current panels | gap |
| --- | --- | --- | --- |
| frame / outer layer | strong | shared spine, surface-local focus, CommandHeaderPanel, FlowSummaryPanel | purpose/status/location are visible, but active work package identity is still latest-turn based |
| internal evidence layer | weak | bounded context refs, Evidence Line Atlas, Inspection, AssetInventory inside engine mock | evidence is not selected by an internal search gate; it is still refs/support |
| mediation / guard layer | medium-strong | VectorFL current packet layer, authority state, marks, validation/reread queue | route/guard is visible, but internal search result is not the basis yet |
| trace / record layer | medium | latest return summary, conversation turns, OperationLogPanel, mark history, deposit preview | trace exists, but not yet classified as reusable memory/sedimentation |

Main finding:

The UI now expresses the packet frame and mediation/guard layers better than before. It does not yet give the internal evidence and trace/sedimentation layers enough operating force.

## 6. Eight-Step Process Audit

| process step | current UI coverage | concrete location | audit note |
| --- | --- | --- | --- |
| 1. instruction intake | medium | User goal, CLI purpose/message | intake exists, but User goal and CLI turn purpose are not unified |
| 2. internal search | weak | context refs, Evidence Line Atlas, engine mock asset inventory | no explicit gate says internal search was run, skipped, or returned evidence |
| 3. evidence bundle | weak | bounded context refs, line selection, selected line inspection | still a file/ref/line support bundle, not a formed evidence bundle |
| 4. VectorFL mediation / packetization | medium-strong | current work packet formation, shared spine, local VectorFL focus | visible, but based on provided/inferred fields rather than internal search output |
| 5. User organization | medium | User focus, UserCliAssignmentPanel, InternalTeamAssignmentPanel | team/role structure exists; attachment is still UI-local and not a formal work package decision |
| 6. Engine main processing | weak-medium | Engine focus, EngineCliReturnPanel, engine mock ingest/pipeline | Engine sees candidates/returns; actual input/generation/translation/extraction/flow is not active-package concrete |
| 7. VectorFL reflux | medium | VectorFLValidationQueuePanel, Send to VectorFL buttons | return-to-VectorFL exists, but queue is local and not a full reflux record |
| 8. record / sedimentation | weak | deposit candidate, mark history, OperationLogPanel | deposit is not ingested; asset-state classification is absent |

The first missing structural gate is step 2: internal search.

Without step 2, steps 3 and 4 become user-provided refs plus VectorFL formatting. That is better than raw CLI, but not yet the integrated-engine physiology.

## 7. Surface Audit

### User Surface

Strength:

- Now has a first local focus layer saying the current object is assignment / decision candidate.
- `UserCliAssignmentPanel` correctly frames candidate as not automatic assignment.
- `InternalTeamAssignmentPanel` establishes team/role assignment as user-side operation.

Weakness:

- User organization does not yet receive a work package with confirmed evidence bundle and internal search result.
- `CommandHeaderPanel` still says `Goal & Scope` and not yet `현재 작업`.
- `ExecutionRoutePanel` remains a ticket lifecycle board with internal English labels such as Backlog / Active / Handoff / Review.

Verdict:

User Surface is structurally close to organization/decision, but it still reads a mix of goal input, candidate queue, and team desk rather than a formal work package organization stage.

### VectorFL Surface

Strength:

- strongest current surface.
- current packet layer, shared spine, local focus, route candidate, authority state, and reread queue exist.
- Line Atlas has been demoted to support.

Weakness:

- internal search is only `refs-based reread` or context refs.
- evidence bundle is still user-provided or support-selected.
- VectorFL mediation is visible, but the evidence it mediates is not yet produced by the integrated-engine body.

Verdict:

VectorFL now shows packetization and mediation. It does not yet show the preceding internal search gate and evidence bundle formation as a real process.

### Engine Surface

Strength:

- local focus clarifies current object as request / validation / deposit material.
- EngineCliReturnPanel separates request candidates, validation queue, extraction/deposit candidates.
- engine mock includes ingest/pipeline material.

Weakness:

- Engine is still closer to return feed / candidate feed than concrete process surface.
- input / generation / translation / extraction / flow are not visible as active work-package process stages.
- internal search process vs main processing process is not distinguished.

Verdict:

Engine Surface needs the most structural clarification after internal search. It must show what process the active work package requires, not only what candidate or return exists.

## 8. Shared Spine / Local Focus / Packet Layer Location Re-Judgment

### Shared Spine

Covers:

- frame layer
- some decision/authority state
- current object continuity

Does not cover:

- internal evidence
- process execution details
- sedimentation classification

Judgment:

Valid as a shell-level current-object reader. It should not become a multi-work board.

### Surface-Local Focus

Covers:

- local surface interpretation of the same current object
- authority reminder
- next candidate action

Does not cover:

- the full process stage evidence
- actual work-package transition record

Judgment:

Valid hierarchy correction. It should remain thin.

### VectorFL Current Work Packet Formation Layer

Covers:

- current purpose
- task lens
- inferred route
- expected return
- visible manual/provided/missing fields

Does not cover:

- actual internal search
- evidence bundle returned from Engine
- confirmed governing locks

Judgment:

It is currently an input summary + mediation frame. It is not yet a full internal-search-backed packet.

## 9. Surface Language Audit

Current status: weak to medium.

The 04-17 language rule is:

```text
human-readable phrase first; internal label as badge
```

Where it works:

- User local focus has Korean titles.
- VectorFL/Engine local focus has Korean titles.
- several explanatory texts clarify candidate-only boundaries.

Where it is still weak:

- `shared operating spine`
- `current work packet formation`
- `packet input details`
- `route / mark`
- `latest return summary`
- `Execution Route Board`
- `Report / Log Center`
- `VectorFL CLI Conversation Layer`
- `Send Codex Turn`

Judgment:

Language cleanup is needed, but it should not be the next structural correction. If done before internal search/evidence gate, it may polish the wrong physiology.

## 10. Single Highest-Priority Next Correction

Implement an internal search / evidence bundle gate as the next bounded structural correction.

This is the highest priority because:

- it is step 2 in the common process
- without it, evidence bundle formation stays manual
- without it, VectorFL packetization is only input formatting
- without it, Engine process cannot distinguish internal search from main processing
- without it, memory is not the past that changes the current task

The correction should be small:

```text
current work package
-> internal search requested / skipped / completed
-> evidence bundle returned
-> VectorFL packet formation uses that bundle
```

It should not be:

- multi-work board
- session history
- broad asset browser
- automatic ingestion
- Gemini adapter

## 11. Watchpoints

1. Do not implement multi-work board before one work package can carry internal search and evidence bundle.
2. Do not confuse context refs with internal search.
3. Do not let Engine remain only return/candidate feed.
4. Do not polish language so much that structural gaps become harder to see.
5. Do not make internal search automatic truth; it should show requested / skipped / completed and evidence limitations.
6. Do not promote deposit candidate into sedimented memory.

## 12. What Must NOT Be Done Next

- no multi-work board implementation
- no preset selector
- no Gemini adapter
- no async/background
- no deposit ingestion / promotion automation
- no new surface
- no giant dashboard
- no broad UI language pass as the immediate next correction
- no session history expansion

The next bounded implementation should be the internal search / evidence bundle gate, because it is the missing process step that lets the current work packet become a true integrated-engine work package rather than a well-framed CLI turn.
