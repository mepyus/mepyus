# Rubric Two-Agent Gemini Execution Pipeline Candidate v0

## 1. Source Identification

```text
Source = Rubric Labs / Claude한테 짜게 시키고 Codex한테 까게 시키기 / Ch 1
URL = https://rubric.im/curriculum/claude-codex-workflow/01-why-two-agents
Source type = external reference
User-provided = yes
Adoption = not adopted
Use = external comparison / pipeline inspiration
```

Status:

```text
Document = pipeline candidate design
Authority = candidate reference / orientation support
Not workflow
Not automation
Not router
Not registry
Not index
Not ledger
Not permission system
```

## 2. Four-Line Card

### 지금 어디까지 왔나?

Rubric 자료는 사용자 제공 외부자료로 읽혔다.

이 자료는 채택된 것이 아니라, 두 agent를 다른 역할로 붙여 blind spot을 줄이는 방식에 대한 외부 비교 자료다.

### 무엇을 움직일 수 있나?

움직일 수 있는 것은 구현이 아니라 설계 후보다.

우리 적용은 다음 방향으로만 읽는다:

```text
Codex = 설계 / 구조화 / Gemini task packet 생성
Gemini = read-heavy / observation-heavy / repeated evidence 실행
ChatGPT = 방향 검증 / 역할 drift 감지
User = 목적 설정 / 최종 판단
```

### 무엇을 조심해야 하나?

Rubric의 Claude/Codex 구조를 그대로 복사하면 안 된다.

Advisory reviewer가 gate가 되면 안 되고, Gemini 결과가 verified truth가 되면 안 되며, Codex가 Gemini를 자율 routing하면 안 된다.

### 다음 판단은 무엇인가?

단일 채팅 prompt chain이 아니라, 세션이 끊겨도 이어질 수 있는 durable packet / queue / result handoff 후보를 설계한다.

이 설계는 User/ChatGPT 검토 전까지 pipeline candidate일 뿐이다.

## 3. Rubric Source Summary

Rubric Ch 1 explains why using two agents can reduce a single agent's blind spots. The key idea is to attach a different model in a different role, not because one model is inherently smarter, but because another viewpoint can challenge assumptions the first model may miss.

The source frames Claude Code as main writer and Codex as advisory reviewer. The review role is explicitly advisory, not a gate: reviewer failure, timeout, missing install, or even a severe finding should not automatically block the main pipeline. Human judgment remains necessary.

The source also warns that multi-agent use has cost and complexity, so it should be justified by real review burden, domain complexity, or lack of reviewers.

## 4. Translate Rubric Model into Our Roles

| Rubric concept | Our adapted role | Why this fits | What must not be copied directly | Drift risk |
|---|---|---|---|---|
| Claude as main writer | Codex as design/structure packet creator, not autonomous implementer | In our space Codex already structures scope, packets, and review notes | Do not copy "main writer implements everything" into Codex authority | Codex design becoming implementation authority |
| Codex as advisory reviewer | ChatGPT/User review plus Codex packaging of returned evidence | Our review authority is split: ChatGPT checks direction, User decides | Do not make Codex the final gate or truth source | Codex review becoming approval |
| different model / different viewpoint | Codex/Gemini/ChatGPT roles separate blind spots | Separate roles reduce same-context self-confirmation | Do not treat "different model" as inherently correct | model diversity becoming authority |
| advisory not gate | Gemini evidence and Codex packaging are advisory to User/ChatGPT | Matches Roles reference: evidence is not approval | Do not auto-block or auto-promote based on Gemini/Codex result | advisory becoming gate |
| review failure should not block | Missing/blocked Gemini should return blocked state, not hidden failure | Durable packet can preserve skipped/blocked states | Do not hide failure or continue as if evidence exists | skipped result becoming pass |
| human judgment | User decision gate remains final | Matches Roles reference highest orientation | Do not delegate final authority to worker queue | User bypass |
| cost/complexity threshold | Use Gemini packet queue only for read-heavy/repeated evidence tasks | Prevents ceremony for small work | Do not make every task multi-agent | process becoming ceremony |

Important adaptation:

```text
In our space, Codex is not simply the reviewer.
Codex should design the structure and produce Gemini task packets.
Gemini should execute read-heavy / observation-heavy / repeated evidence tasks.
Gemini output remains evidence, not verified truth.
User remains final decision gate.
ChatGPT remains direction / validation / role-drift checker.
```

## 5. Current Manual Pain This Should Solve

The recent operating pattern worked, but it was relay-heavy:

```text
User repeatedly types next.
ChatGPT produces Codex instruction.
User pastes into Codex.
Codex returns report.
User pastes report back.
ChatGPT reviews and creates next instruction.
This worked, but it was manual relay-heavy.
```

Design goal:

```text
Reduce manual relay by making Codex generate persistent Gemini task packets,
so Gemini can execute a sequence of bounded tasks and return structured evidence,
while User/ChatGPT still control approval and direction.
```

## 6. Non-Single-Session Requirement

```text
This design must not depend on one live chat session.
It must use durable files / packets / queue state / result records
so work can continue across sessions.
```

Candidate durable artifacts:

```text
gemini_task_queue_candidate.md
gemini_task_packet_001.md
gemini_task_packet_002.md
gemini_result_template.md
gemini_result_inbox/
gemini_execution_log_candidate.md
handoff_state_candidate.md
```

These names are candidate names only.

No executable automation or folder layout is created in this run.

## 7. Candidate Pipeline Design

| Stage | Owner | Input | Output | Allowed action | Forbidden action | Stop condition | Recovery path |
|---|---|---|---|---|---|---|---|
| Stage 0. User purpose selection | User | purpose / discomfort / direction | selected purpose or stop | choose, reject, stop | hidden worker direction | no explicit purpose | current-position / purpose preflight |
| Stage 1. ChatGPT direction / validation frame | ChatGPT | User purpose, Roles reference | validation frame / guardrails | detect drift, prepare direction | execute, approve movement alone | purpose unclear or overbroad | instruction note / review request |
| Stage 2. Codex design packet | Codex | User purpose + validation frame | bounded design packet | scope, structure, packet fields | implement or self-expand authority | scope touches promotion/automation without approval | run record / design candidate |
| Stage 3. Codex creates Gemini task queue | Codex | approved design packet | queue candidate + task packets | create durable task packets | route Gemini autonomously without selected purpose | missing source or unclear task order | queue file / packet files as candidate |
| Stage 4. Gemini executes task packets | Gemini | one approved packet at a time | evidence + uncertainty | read/observe/repeat bounded checks | approve, promote, implement, rewrite policy | source missing, scope unclear, forbidden action needed | result inbox / blocked result |
| Stage 5. Gemini returns evidence/results | Gemini | completed observation | structured result | report findings, uncertainty, source limits | claim verified truth | evidence insufficient or blocked | result template / inbox |
| Stage 6. Codex packages Gemini results | Codex | Gemini results | review package / synthesis note | organize evidence and watch items | treat evidence as truth or implement | conflicting evidence or authority risk | run record / closeout candidate |
| Stage 7. ChatGPT/User review | ChatGPT + User | packaged results | verdict / hold / next purpose | validate direction, decide | automatic approval | User does not approve | review record / stop |
| Stage 8. Recovery into space | Codex under direction | final verdict | run record / process-memory / watch / current-position if needed | record lightweight recovery | automatic current-position update | no active-direction change | run note only by default |

## 8. Gemini Task Packet Design

Minimum fields:

```text
task_id
source_material
purpose
read_scope
execution_steps
expected_output
evidence_required
uncertainty_required
forbidden_actions
stop_conditions
return_format
recovery_target
next_safe_action
```

Rules:

```text
Gemini must return evidence and uncertainty.
Gemini must not approve, promote, implement, or rewrite source-space policy.
Gemini must not treat its own observations as verified truth.
Gemini must stop if source is missing or scope is unclear.
```

Suggested return format:

```text
task_id
status: COMPLETE | BLOCKED | SCOPE_INSUFFICIENT | SOURCE_MISSING
evidence_summary
source_refs
uncertainty
watch_items
what_must_not_be_inferred
next_safe_action
```

## 9. Codex Design Responsibilities

Codex may:

```text
- read User purpose and Roles reference
- design the Gemini task queue
- create bounded Gemini task packets
- define stop conditions
- package Gemini results after return
- create run records / closeout notes
```

Codex may not:

```text
- self-assign broader authority
- route Gemini without User-selected purpose
- treat Gemini evidence as truth
- implement from Gemini results automatically
- approve package movement
- update current-position unless clearly required or instructed
```

## 10. Gemini Execution Responsibilities

Gemini may:

```text
- execute read-heavy tasks
- inspect provided files/materials
- summarize evidence
- report uncertainty
- mark blocked/missing-source states
- repeat bounded checks across packet list
```

Gemini may not:

```text
- approve or reject packages
- promote candidate references
- create baseline/policy/schema
- decide next purpose
- route work to another worker
- treat observations as verified truth
```

## 11. Semi-Automation Boundary

Principle:

```text
Semi-automation means reducing relay friction,
not hiding decisions from the User.
```

Allowed candidate mechanisms:

```text
manual command to generate Gemini packets
manual command to collect Gemini results
status file showing pending/running/done/blocked
structured return format
one queue file + packet files
```

Forbidden:

```text
background autonomous execution
Gemini broad run without explicit packet
Codex-to-Gemini autonomous routing
automatic package approval
automatic current-position update
automatic baseline/policy/schema creation
hidden worker decisions
```

## 12. Proposed Artifact Layout Candidate

```text
app/work/space-skill-sandbox/worker-handoff-candidate/
  README.md
  queue/gemini_task_queue_candidate.md
  packets/gemini_task_packet_001.md
  results/gemini_result_001_template.md
  logs/gemini_execution_log_candidate.md
  state/handoff_state_candidate.md
```

Status:

```text
LAYOUT_CANDIDATE_ONLY
not implemented
not official workflow
not router
not automation
not registry
not ledger
```

No folder was created in this run.

## 13. First Test Scenario

Scenario:

```text
Gemini reads one external material or one package summary and returns evidence/uncertainty.
```

Recommended first test:

```text
Gemini task packet 001:
Read the Rubric two-agent material summary and compare it against our Roles reference.
Return:
- what fits
- what does not fit
- what must remain watch-only
- whether the material suggests adoption, or only comparison
```

Do not execute it in this run.

## 14. Role Drift Checks

| Risk | Status | Note |
|---|---|---|
| Codex design becoming implementation authority | `WATCH_ONLY` | Codex creates packets, not implementation authority. |
| Gemini execution becoming verified truth | `WATCH_ONLY` | Gemini returns evidence/uncertainty only. |
| task queue becoming workflow | `WATCH_ONLY` | Queue remains candidate and manually reviewed. |
| packet list becoming router | `WATCH_ONLY` | Packet sequence must not auto-route work. |
| execution log becoming ledger | `WATCH_ONLY` | Logs are trace, not official ledger. |
| semi-automation becoming hidden automation | `WATCH_ONLY` | Only manual-triggered mechanisms are allowed. |
| Rubric source becoming adoption plan | `WATCH_ONLY` | Rubric is external comparison/inspiration only. |
| two-agent model overriding our Roles reference | `NO_RISK_FOUND` | Design explicitly uses Roles reference as guardrail. |
| User decision gate being bypassed | `WATCH_ONLY` | Must remain explicit at stage 0 and stage 7. |

## 15. Fit Judgment

```text
FITS_WITH_WATCH
```

Reason:

```text
The source is useful for role-separated multi-agent workflow thinking, but our adaptation must preserve User decision gate, durable handoff, advisory/non-gating review, and evidence return without verified-truth authority.
```

## 16. Current-Position Decision

```text
CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED
```

Reason:

```text
This may become the next active design direction if the User chooses it, but it should not update current-position until User/ChatGPT reviews the candidate pipeline.
```

## 17. Recommendation

```text
HOLD_FOR_USER_REVIEW
```

Reason:

```text
This design affects worker handoff and semi-automation boundaries, so User/ChatGPT should review before creating executable scripts, persistent queue folders, or Gemini packet prototypes.
```

## 18. Boundaries

```text
no Rubric workflow adoption
no Claude/Codex model copied directly
no baseline promotion
no official workflow creation
no architecture finalization
no automation/router/controller
no registry/index/ledger promotion
no formal permission system
no Codex-to-Gemini autonomous routing
no Gemini broad run
no Gemini verified-truth authority
no package movement
no Run 117 approval
no current-position update unless explicitly required
no hidden background execution
```

`STATUS: RUBRIC_TWO_AGENT_GEMINI_PIPELINE_CANDIDATE_PREPARED`
