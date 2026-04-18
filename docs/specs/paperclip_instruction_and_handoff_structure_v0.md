# Paperclip Instruction And Handoff Structure v0

이 문서는 `Paperclip` 내부에서 agent에게 지시가 어떻게 붙고,  
기관 간 전달에 해당하는 handoff 맥락이 어디에 남는지를 native하게 읽는다.

목적은 VectorFL 기관 구조로 번역하기 전에,  
Paperclip가 `instructions / prompt / context / session / result summary`를 어떻게 조합하는지 먼저 보는 것이다.

## 1. Verdict

Paperclip의 지시와 handoff 구조는 대체로 아래처럼 읽힌다.

`agent config`
-> `adapterConfig / runtimeConfig`
-> `instructionsFilePath + promptTemplate`
-> `heartbeat contextSnapshot / wake payload`
-> `run result summary / issue comment`
-> `session carry`

즉 Paperclip는 단순히 agent 이름만 두는 것이 아니라,  
`지시 파일 + 실행 템플릿 + run 맥락 + 결과 요약`의 결합으로 handoff를 만든다.

## 2. Agent As Configured Runtime Node

agent는 단순 persona가 아니라 설정된 runtime node다.

- evidence:
  - [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/agents.ts)
  - [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/agents.ts)
- reading:
  - agent는 `role`, `reportsTo`, `adapterType`, `adapterConfig`, `runtimeConfig`, `metadata`를 가진다
  - 즉 agent는 조직도 항목이면서 동시에 실행 설정 객체다

## 3. Instruction Attachment

agent에는 별도 지시 파일과 프롬프트 템플릿이 붙을 수 있다.

- evidence:
  - [codex-local/src/index.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/adapters/codex-local/src/index.ts)
  - [types.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/adapter-utils/src/types.ts)
- reading:
  - `instructionsFilePath`는 markdown instructions file 경로다
  - `promptTemplate`은 run prompt template이다
  - heartbeat 시 Paperclip는 instructions file contents를 run prompt 앞에 붙인다

즉 지시는 UI에만 있는 게 아니라,
`agent config -> adapter config -> runtime prompt`로 실제 주입된다.

## 4. Run-Time Context Attachment

instructions만으로 실행이 끝나지 않고, run 시점 context가 별도로 붙는다.

- evidence:
  - [issue-assignment-wakeup.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/issue-assignment-wakeup.ts)
  - [heartbeat_runs.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/heartbeat_runs.ts)
  - [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)
- reading:
  - wakeup에는 `payload`와 `contextSnapshot`이 붙는다
  - heartbeat run에도 `contextSnapshot`이 저장된다
  - 즉 동일 agent라도 매 run마다 상황별 handoff 맥락이 다르게 주입된다

이건 중요하다.

- Paperclip의 handoff는 완전히 자유 대화형이 아니다
- `payload/contextSnapshot` 같은 공유 환경 기반 전달 구조가 강하다

## 5. Result Return As Handoff Material

run 결과는 다음 기관/사람이 읽을 수 있는 handoff 재료로 다시 압축된다.

- evidence:
  - [heartbeat-run-summary.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat-run-summary.ts)
- reading:
  - resultJson에서 summary/result/message를 짧게 뽑는다
  - 이것이 issue comment나 surface summary로 다시 남는다

즉 결과 handoff는 raw logs보다
`짧은 요약 + comment surface`에 더 많이 의존한다.

## 6. Session As Continuing Handoff

handoff는 한 run으로 끝나지 않고 세션으로 이어질 수 있다.

- evidence:
  - [agent_task_sessions.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/agent_task_sessions.ts)
  - [types.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/adapter-utils/src/types.ts)
- reading:
  - adapter runtime에는 `taskKey`, `sessionParams`, `sessionDisplayId`가 있다
  - task session table은 `taskKey`별 continuity를 유지한다

즉 Paperclip handoff는 세 가지 층을 가진다.

- static instruction handoff
- per-run context handoff
- session continuity handoff

## 7. Structural Reading

Paperclip의 instruction/handoff 구조는 아래처럼 읽는 것이 가장 정확하다.

### 7-1. static instruction layer

- instructionsFilePath
- promptTemplate
- adapterConfig/runtimeConfig

### 7-2. dynamic run context layer

- wake payload
- contextSnapshot
- invocationSource / triggerDetail

### 7-3. returned summary layer

- resultJson summary
- issue comment
- activity/log summary

### 7-4. continuing session layer

- taskKey
- sessionParams
- lastRunId

## 8. What This Means For Deep Reference Use

나중에 VectorFL 쪽에서 가져와야 하는 건 단순히 `agent가 있다`는 사실이 아니다.

오히려 더 중요한 건 아래다.

- 기관마다 별도 지시 문서를 붙일 수 있는 구조
- handoff를 payload/contextSnapshot으로 남기는 구조
- 결과를 다음 기관이 읽기 좋은 요약으로 남기는 구조
- session continuity를 task key로 유지하는 구조

즉 Paperclip에서 진짜 배워야 하는 건  
`다기관 지시/전달 구조의 실제 결합 방식`이다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Paperclip의 지시와 handoff 구조는 agent별 instructions file과 prompt template 같은 정적 지시층, wake payload와 contextSnapshot 같은 동적 run 맥락층, result summary와 issue comment 같은 반환 요약층, task-keyed session continuity 층이 결합된 구조로 읽는 것이 가장 정확하다.`
