# Integrated Engine Three Surface Shared Operating Spine Gap Note v0

## 1. Verdict

PASS_WITH_NOTE

VectorFL is no longer just a CLI input surface. The packet layer now makes a single turn more readable inside VectorFL.

The remaining discomfort is not VectorFL-only. The 3 surfaces still do not share one explicit current operating object, authority state, and turn lifecycle spine. The user still has to mentally stitch together the same turn across User / VectorFL / Engine.

## 2. Fixed Body Interpretation

| surface | fixed role | current local object |
| --- | --- | --- |
| User Surface | purpose / assignment / decision / internal team operation | goal, user assignment candidates, team/role desk, route/log support |
| VectorFL Surface | interpretation / mediation / packet formation / reread / route sorting | current work packet layer, CLI turn, marks, validation/reread queue, evidence atlas |
| Engine Surface | processing / return / validation feed / extraction/deposit candidate | engine request candidates, validation queue, extraction/deposit material, engine mock body |
| CLI on-top | tool layer, not fourth surface | Codex turn execution and return artifact creation |

The body is still correct. The problem is that the shared object moving through the body is not explicit enough.

## 3. Why The Discomfort Is Not VectorFL-Only

Symptom:

- VectorFL now shows a packet summary, route candidate, latest return, and marks.
- But switching to User or Engine still feels like reading separate panels rather than the same operating object from another surface.

Cause:

- `cliHostState` is shared as raw state, but the UI does not expose a named shared spine such as "current operating object."
- Each surface derives its own local queue from the latest/recent CLI returns.
- Authority states appear as local labels, badges, or explanatory text, not as one common status line carried through all surfaces.

This means the user must remember:

```text
this latest CLI return
-> was formed from this packet
-> has this route candidate
-> is only a candidate
-> appears in User or Engine only if marked a certain way
-> can return to VectorFL reread
-> may become deposit candidate but is not ingested
```

The UI has the pieces. It does not yet give them a common spine.

## 4. Current Operating Object Gap

The common current operating object should be the active turn/work packet and its return state.

Minimum shared object:

- current purpose
- current packet state
- current governing locks
- current evidence/source bundle
- current route status
- current authority state
- current next action

Current visibility:

| field | visible in VectorFL | visible in User | visible in Engine | gap |
| --- | --- | --- | --- | --- |
| current purpose | yes, in packet layer and latest return | partial, as latest turn or user queue item | partial, as latest return or candidate item | not named as one shared current purpose |
| packet state | yes, in current packet formation | weak | weak | packet state is mostly VectorFL-local |
| governing locks | expandable in VectorFL | not shown | not shown | lock state does not travel across surfaces |
| evidence/source bundle | expandable in VectorFL | not shown | not shown | evidence is not carried as shared object metadata |
| route status | yes, as candidate/mark | partial, as user assignment candidate | partial, as engine request/validation/deposit candidate | route is local queue membership, not one shared spine |
| authority state | partial, candidate text and marks | partial, user decision text | partial, candidate-only / not automatic notes | "candidate / not canonical / not ingested" is repeated locally, not unified |
| next action | partial, send/mark/continue | partial, send back to VectorFL | partial, send back to VectorFL | next action is surface-local, not shared |

The object exists in fragments. It is not yet framed as the same object traveling through the body.

## 5. Authority State Visibility Gap

Authority states currently appear, but unevenly.

Visible authority signals:

- VectorFL: route candidate badge, marks, "candidate only" wording, `still manual / not hidden`
- User: "자동 배정이 아니라 사용자가 다음 작업을 조직하기 위한 신호"
- Engine: "실행 큐가 아니라 실행 전 요청 후보", "자동 기록이 아니라 검증/추출 후보"
- Deposit: `not_ingested` is present in artifact and sometimes preview text

Gap:

- The user must still remember that all of these are the same authority grammar.
- A route label can still look like completion when seen outside its local explanatory text.
- `deposit_candidate` can be visually strong even though it is not canonical memory.
- `engine_request_candidate` can look like an execution request unless the user reads the local note.
- `user_assignment_candidate` can look like assigned work unless the user reads the local note.

The authority state should be carried as one shared status:

```text
candidate only / not executed / not assigned / not ingested / not canonical
```

Right now that message is scattered.

## 6. Turn Lifecycle Visibility Gap

Target lifecycle:

```text
User purpose
-> VectorFL packet formation
-> Codex run
-> route/mark
-> User or Engine candidate
-> VectorFL reread
-> deposit candidate or hold
```

Current visibility:

| lifecycle step | current screen support | break |
| --- | --- | --- |
| User purpose | User `CommandHeaderPanel`, CLI purpose input | these can diverge; no common active turn purpose is shown across all surfaces |
| VectorFL packet formation | strong in VectorFL after latest patch | mostly disappears when user switches surfaces |
| Codex run | visible in VectorFL latest return/session | User/Engine see return candidates, but not the original packet frame |
| route/mark | visible in VectorFL and route-filtered queues | route is not shown as one lifecycle spine |
| User candidate | visible only if marked user assignment | may feel like local user queue, not same turn continuing |
| Engine candidate | visible only if marked engine/validation/deposit | may feel like separate engine feed, not same turn continuing |
| VectorFL reread | handoff queue exists | queue is local and not persistent; lifecycle continuity depends on user memory |
| deposit candidate / hold | visible in marks/preview | not clearly tied back to same turn lifecycle in all surfaces |

The turn is traceable if the user already understands the model. It is not yet self-evident from the screen.

The break is not a missing button. The break is that the lifecycle is not represented as one shared spine across surfaces.

## 7. Surface-Local Vs Shared Reading Breakdown

### User Surface Local Reading

User Surface currently reads:

- latest turn as user-facing decision signal
- user assignment queue from marked CLI returns
- internal team / role assignment
- route/log support

What is local-only:

- user decision text
- assignment candidate queue
- team/role operation

What should be shared but is weak:

- whether the latest item is the same current operating object seen in VectorFL
- authority state across the whole lifecycle
- original packet purpose/evidence/route

### VectorFL Surface Local Reading

VectorFL currently reads:

- current packet summary
- packet details
- send/continue/mark controls
- latest return summary
- validation/reread queue
- support evidence atlas

What is local-only:

- packet formation state
- lock/evidence bundle
- inferred route
- internal search flag

What should be shared but is weak:

- current packet state should still be visible when viewing User or Engine
- authority status should not need to be reread from local notes

### Engine Surface Local Reading

Engine currently reads:

- latest return material
- engine request candidates
- validation queue
- extraction/deposit material queue
- processing mock body

What is local-only:

- processing status
- request candidates
- validation/extraction/deposit queues

What should be shared but is weak:

- the packet that produced the return
- whether candidate means not executed / not ingested / not canonical
- the next route back to VectorFL or User

## 8. Single Highest-Priority Structural Correction

Add one shared operating spine at the shell level.

This is not a new feature queue, not a preset selector, and not another surface.

It should be a thin, always-visible shell-level object that all 3 surfaces read from. Minimum fields:

- active turn/session id
- current purpose
- packet state
- route candidate/current mark
- authority state
- current surface-local role
- next action candidate

The spine should say, in one place:

```text
What is the current operating object?
Where is it in the lifecycle?
What authority state does it have?
What surface is reading it now?
What is the next candidate action?
```

This correction is higher priority than further VectorFL-only refinement because it reduces the user's need to mentally glue the same turn across three surfaces.

## 9. Watchpoints

1. Do not implement this as a large dashboard.
2. Do not create a fourth surface.
3. Do not turn route candidate into completion state.
4. Do not hide authority boundaries such as candidate-only, not ingested, not canonical.
5. Do not make User Surface responsible for packet evidence.
6. Do not make Engine Surface responsible for route judgment.
7. Do not start session history or persistence as the next step.

## 10. What Must NOT Be Done Next

- Do not add Gemini adapter.
- Do not add async/background.
- Do not add session browsing/history.
- Do not add deposit ingestion automation.
- Do not add context presets as the main correction.
- Do not keep refining only VectorFL density.
- Do not redesign the 3 surfaces.
- Do not make a new "spine surface."

The next bounded implementation should be a shell-level shared operating spine that displays the current operating object and authority state across User / VectorFL / Engine without changing the underlying route/mark mechanics.
