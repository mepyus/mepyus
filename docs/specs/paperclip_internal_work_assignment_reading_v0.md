# Paperclip Internal Work Assignment Reading v0

이 문서는 `Paperclip`를 VectorFL 쪽으로 번역하기 전에,  
Paperclip 자체가 내부에서 일을 어떻게 배정하고 밀어가는지 구조적으로 먼저 읽는다.

목적은 Paperclip의 ontology를 가져오는 것이 아니라,  
`업무 단위가 어떻게 agent에게 놓이고 run으로 이어지며 다시 흔적으로 남는가`를 native하게 파악하는 것이다.

## 1. Verdict

Paperclip의 내부 업무 구조는 대체로 아래 연쇄로 읽힌다.

`issue assignment`
-> `wakeup request`
-> `heartbeat run`
-> `run result / issue comment / activity`
-> `task session carry`

즉 Paperclip는 단순히 issue를 저장하는 시스템이 아니라,  
`배정된 일감을 agent 실행으로 밀어 넣는 assignment-driven operating structure`를 가진다.

## 2. Core Work Unit

현재 Paperclip 내부에서 기본 work unit은 `issue`다.

- evidence:
  - [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/issues.ts)
- reading:
  - issue는 status, assignee, participant, comment, activity, workspace와 연결된다
  - 즉 issue는 단순 카드가 아니라 실행/기록/참여의 중심 단위다

중요한 점:

- Paperclip는 `single-owner issue` 성격이 강하다
- `assigneeAgentId`가 실제 실행 흐름의 핵심 연결점이다

## 3. Assignment To Wakeup

업무 배정은 곧바로 실행 계열 신호로 이어진다.

- evidence:
  - [issue-assignment-wakeup.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/issue-assignment-wakeup.ts)
- reading:
  - issue에 assignee가 있고 backlog가 아니면
  - Paperclip는 해당 agent에 `wakeup(...)`을 건다
  - wakeup payload에는 `issueId`, `mutation`, `contextSnapshot`이 들어간다

즉 `assignment`는 단순 표시가 아니라,
`agent를 실제로 깨우는 구조적 트리거`다.

## 4. Wakeup To Heartbeat Run

wakeup은 heartbeat run으로 이어지는 중간 운영 구조를 가진다.

- evidence:
  - [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)
  - [heartbeat_runs.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/heartbeat_runs.ts)
- reading:
  - heartbeat run은 `invocationSource`, `triggerDetail`, `status`, `wakeupRequestId`, `contextSnapshot`을 가진다
  - 즉 run은 그냥 실행 결과가 아니라, 왜 시작됐고 어떤 맥락으로 시작됐는지를 같이 잡는 구조다

중요한 점:

- Paperclip의 실제 operating loop는 heartbeat run에 있다
- assignment는 run을 여는 계기이고, heartbeat는 그것을 실제 실행으로 만든다

## 5. Run Result To Human-Readable Return

run은 raw execution으로 끝나지 않고, 다시 issue-facing 산출로 정리된다.

- evidence:
  - [heartbeat-run-summary.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat-run-summary.ts)
  - [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)
- reading:
  - `resultJson`에서 summary / result / message / error를 짧게 추린다
  - 그중 일부는 issue comment body로 다시 올라간다
  - 즉 run 결과는 `issue comment`나 summary surface로 재표면화된다

이건 중요하다.

- Paperclip는 run 결과를 run table에만 남기지 않는다
- 다시 issue-facing surface로 번역해 operator와 다른 agent가 읽게 한다

## 6. Session Carry

Paperclip는 run을 매번 완전히 새로 시작하는 구조만은 아니다.

- evidence:
  - [agent_task_sessions.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/agent_task_sessions.ts)
  - [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)
- reading:
  - session은 `agentId + adapterType + taskKey` 단위로 유지된다
  - `sessionParamsJson`, `sessionDisplayId`, `lastRunId`를 가진다
  - 즉 같은 task key에 대해 세션 carry와 handoff 요약이 가능하다

즉 Paperclip의 assignment 흐름은 단발성이 아니라,
`task-keyed session carry`를 가진 반복 구조다.

## 7. What This Means Structurally

Paperclip 내부 흐름은 아래처럼 읽는 것이 가장 정확하다.

### 7-1. work placement

- issue가 agent에게 놓인다

### 7-2. execution trigger

- assignment가 wakeup으로 번역된다

### 7-3. bounded run

- heartbeat run이 실제 실행 단위를 만든다

### 7-4. summarized return

- run result가 다시 comment / summary / activity로 표면화된다

### 7-5. carryable continuity

- session/task key를 통해 다음 run으로 이어진다

## 8. What VectorFL Should Notice Later

이 문서는 아직 VectorFL 번역 문서는 아니지만,  
나중에 연결할 때 주목해야 할 구조는 이미 보인다.

- assignment payload
- contextSnapshot
- run status / trigger detail
- resultJson summary
- issue comment surface
- task session carry

즉 VectorFL이 받아먹기 좋은 면은 이미 Paperclip 안에 있다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Paperclip의 내부 업무 흐름은 issue를 assignee agent에 배치하고, assignment를 wakeup으로 바꾸고, heartbeat run으로 bounded execution을 수행한 뒤, result를 comment/summary/activity로 다시 표면화하고, task-keyed session으로 다음 run continuity를 유지하는 구조로 읽는 것이 가장 정확하다.`
