# External Material Microspace Feature Candidate Survey v0

## 1. status

```yaml
status: feature_candidate_survey
scope: external_material_microspace
verdict: PASS_WITH_NOTE
purpose: inspect whether external material clusters suggest useful feature candidates for the space
attach_decision: not_yet
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
validator_or_script: false
```

## 2. user question

```text
그럼 지금 우리 외부자료공간에서 우리 공간에 필요하거나 붙일만한 기능이 있을지 한번 살펴보자! 넣자는 게 아니야. 일단 살펴보자는 이야기야
```

## 3. reading stance

This is an inspection, not an attachment.

The question is not:

```text
무엇을 바로 구현할 것인가?
```

The question is:

```text
외부자료공간이 반복해서 보여주는 기능적 결핍이나 보강 후보가 무엇인가?
```

## 4. current microspace clusters

| Cluster | Current state | What it may contribute |
| --- | --- | --- |
| governance-architecture cluster | framing_candidate | boundary, role discipline, quality gates |
| Codex workflow/runtime cluster | framing_candidate | role elevation, stage transition, artifact passing, verification return |
| formation-to-movement cycle cluster | framing_candidate | durable intermediate artifacts, constrained execution, keep/discard loops |
| data extraction pipeline cluster | framing_candidate | staged external ingest, return/export surface, source-to-record movement |
| AI architecture hype / verification-path cluster | framing_candidate | narrative / mechanism / operational path separation, README-vs-code-path verification |

## 5. feature candidate scan

### 5.1 external material intake cockpit

Candidate:

```text
외부자료가 들어오면 source, lens, cluster, safe state, next move를 한 화면/한 카드로 잡는 intake cockpit.
```

Suggested by:

- external material microspace index
- GoScrapy staged source-to-record reading
- OpenMythos narrative/mechanism/operational-path reading

Why it may be useful:

```text
사용자가 "자료를 넣었다"는 느낌을 받으려면 저장/요약보다 현재 위치와 다음 이동이 즉시 보여야 함.
```

Possible output:

```text
source:
cluster:
selected_lenses:
state:
next_move:
do_not:
re_emergence_trigger:
```

Do not attach yet:

- do not turn this into mandatory schema
- do not require the user to fill it
- do not automate index updates yet

Provisional judgment:

```yaml
candidate_strength: strong
state: feature_direction_candidate
safe_next_move: prototype_as_manual_card_only
```

### 5.2 narrative / mechanism / operational path check

Candidate:

```text
AI repo, tool, architecture claim, or README-heavy material을 읽을 때 서사/메커니즘/운영경로를 분리하는 검증 카드.
```

Suggested by:

- OpenMythos sheepwave
- weak-signal direct evidence vs comparison frame work
- Codex interpreter/output mode caution

Why it may be useful:

```text
Codex가 잘 읽고 잘 요약할수록, 그 출력이 검증처럼 보이는 위험이 커짐.
```

Possible check:

```text
narrative claim:
implemented mechanism:
operational path:
missing evidence:
safe state:
```

Do not attach yet:

- do not make every external material use this table
- do not treat Codex repo summary as audit
- do not promote this to default rule until more cases repeat

Provisional judgment:

```yaml
candidate_strength: strong_for_AI_repo_material
state: lens_candidate
safe_next_move: reuse_on_next_README_heavy_repo_case
```

### 5.3 stage-bound return/export surface

Candidate:

```text
외부자료가 분석된 뒤 어디로 돌아가는지 명시하는 return/export surface.
```

Suggested by:

- GoScrapy pipeline export
- OMX stage/artifact/verification return
- formation-to-movement lifecycle

Why it may be useful:

```text
자료가 들어온 뒤 report는 생기지만, 사용자가 나중에 "이 자료가 어디 갔는지" 찾기 어려움.
```

Possible distinction:

```text
raw source record
analysis report
microspace card
re-emergence trigger
future comparison target
```

Do not attach yet:

- do not build runtime manifest
- do not implement script-based routing
- do not make this a full provenance system

Provisional judgment:

```yaml
candidate_strength: medium_strong
state: workflow_habit_candidate
safe_next_move: use_as_closeout_section_in_live_intake_reports
```

### 5.4 bounded comparer trigger

Candidate:

```text
외부자료가 compare_only를 넘어 실제 비교 작업으로 갈 수 있는 조건을 명확히 하는 trigger.
```

Suggested by:

- agent-skills / Flutist governance cluster
- OMX workflow/runtime cluster
- external material state policy

Why it may be useful:

```text
외부자료가 계속 쌓이면 "이제 뭘 비교해야 하는지"가 흐려짐.
```

Healthy trigger:

```text
concrete internal target exists
comparison question exists
boundary exists
expected return exists
promotion barrier exists
```

Do not attach yet:

- do not elevate Codex automatically
- do not convert compare_only into execution
- do not make this a validator

Provisional judgment:

```yaml
candidate_strength: medium
state: trigger_candidate
safe_next_move: test_on_next_two_material_merge_cases
```

### 5.5 external material re-emergence reminder

Candidate:

```text
새 질문이 들어오면 외부자료공간에서 관련 cluster를 먼저 떠올리는 reminder.
```

Suggested by:

- user's friction: recent materials were not findable
- re-emergence reread merge note
- external material microspace index

Why it may be useful:

```text
자료는 있는데 자연스럽게 다시 떠오르지 않으면 공간이 아니라 문서 창고가 됨.
```

Possible habit:

```text
If user asks about repo / external tool / workflow / architecture claim / ingest,
check external material microspace before answering from scratch.
```

Do not attach yet:

- do not search the whole repo every time
- do not force a package for simple questions
- do not expose full microspace to user unless needed

Provisional judgment:

```yaml
candidate_strength: strong
state: usage_habit_candidate
safe_next_move: adopt_as_Codex_operating_habit_without_schema
```

## 6. candidate ranking

| Rank | Candidate | Strength | Why |
| --- | --- | --- | --- |
| 1 | external material re-emergence reminder | strong | directly fixes findability and natural re-use problem |
| 2 | external material intake cockpit | strong | makes "space insertion" visible without heavy package |
| 3 | narrative / mechanism / operational path check | strong for AI repo material | prevents README/AI summary from becoming fake validation |
| 4 | stage-bound return/export surface | medium_strong | helps preserve source/analysis/microspace/return separation |
| 5 | bounded comparer trigger | medium | useful, but needs more merge cases before tightening |

## 7. what should not be attached now

- Do not implement an automated ingest pipeline.
- Do not create a runtime manifest.
- Do not turn microspace cards into mandatory schema.
- Do not add new object families.
- Do not baseline-lock the narrative/mechanism/operational-path check.
- Do not make Codex a default auditor or executor.
- Do not treat external material clusters as doctrine.

## 8. recommended next move

The safest next move is not implementation.

Recommended next move:

```text
Run one manual "external material intake cockpit" trial on the next incoming material.
```

The cockpit should be only a compact output format, not a new package:

```text
source:
cluster:
selected_lenses:
state:
next_move:
do_not:
re_emergence_trigger:
```

This would test whether the external material space can become usable without becoming heavy.

## 9. current judgment

```yaml
verdict: PASS_WITH_NOTE
best_candidate_now: external_material_re_emergence_reminder + lightweight_intake_cockpit
not_ready_for: implementation / automation / schema / baseline
main_reason: "The user friction is findability and natural flow, not lack of theory."
```

## 10. unresolved questions

- Should the intake cockpit be a user-facing card or an internal Codex habit?
- Should narrative / mechanism / operational path be shown only for AI architecture claims, or for all technical repos?
- How many external materials are enough before bounded comparer trigger becomes stable?
- Can re-emergence reminder remain a habit without becoming another manual checklist?

