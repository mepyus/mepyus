# Paperclip Extractable Structure v0

## 목적

이 문서는
Paperclip를 아직 VectorFL로 번역하지 않고,
`그 자체의 구조 안에서 밖으로 드러나는 생성물`
이 무엇인지 정리한다.

즉 질문은 이것이다.

- Paperclip 안에서 무엇을 추출 가능한가
- 그 생성물은 어떤 층으로 나뉘는가

## 1. 가장 중요한 판단

Paperclip는 단순 task 앱이 아니라
생성물이 여러 층으로 분리된 control plane이다.

최소한 아래 여섯 층은 뚜렷하다.

- work unit surface
- run trace surface
- event/log surface
- governance surface
- cost/control surface
- output artifact surface

즉 이 프로그램은
“밖으로 뽑아낼 수 있는 구조적 면”이 꽤 많다.

## 2. work unit surface

기준:

- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issues.ts)
- [issue_comments.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issue_comments.ts)

이 층에서 추출 가능한 것:

- issue id / identifier / number
- title / description
- status / priority
- assignee
- parent / goal / project linkage
- request depth / origin
- issue comment thread
- comment author / createdByRunId

즉 Paperclip는
일의 “무엇”과 “왜”와 “누가 맡았는가”를
issue surface에서 드러낸다.

## 3. run trace surface

기준:

- [heartbeat_runs.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/heartbeat_runs.ts)
- [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)

이 층에서 추출 가능한 것:

- run id
- company / agent
- invocationSource / triggerDetail
- status / error / exitCode
- startedAt / finishedAt
- sessionIdBefore / sessionIdAfter
- resultJson / usageJson
- contextSnapshot
- log refs / excerpts

즉 Paperclip는
“실행이 실제로 어떻게 돌았는가”를
heartbeat run surface에서 드러낸다.

## 4. event/log surface

기준:

- [heartbeat_run_events.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/heartbeat_run_events.ts)
- [activity_log.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/activity_log.ts)

이 층에서 추출 가능한 것:

- run event seq
- event_type / stream / level
- message / payload
- actor_type / actor_id
- action / entity_type / entity_id
- run-linked activity trail

즉 Paperclip는
단순 final result만 아니라
실행 도중의 세부 이벤트와
시스템 활동 로그를 따로 남긴다.

## 5. governance surface

기준:

- [approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/approvals.ts)
- [issue_approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issue_approvals.ts)
- [approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/approvals.ts)

이 층에서 추출 가능한 것:

- approval type
- requested_by / decided_by
- status
- payload
- decision note
- issue-linked approval relation

즉 Paperclip는
업무와 별도로
“무엇이 승인/거절/수정요청 되었는가”를
뚜렷한 객체로 남긴다.

## 6. cost/control surface

기준:

- [budget_policies.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/budget_policies.ts)
- [cost_events.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/cost_events.ts)
- [budgets.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/budgets.ts)

이 층에서 추출 가능한 것:

- scopeType / scopeId
- budget amount / warnPercent / hard stop
- cost event provider / model / tokens / cents
- heartbeatRun-linked cost
- pause reason / incident / enforcement result

즉 Paperclip는
비용을 단순 metric으로 두지 않고
실행을 멈출 수 있는 control surface로 남긴다.

## 7. output artifact surface

기준:

- [issue_work_products.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issue_work_products.ts)
- [assets.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/assets.ts)

이 층에서 추출 가능한 것:

- work product type / provider
- title / url / summary / metadata
- status / reviewState / healthStatus
- primary 여부
- execution workspace linkage
- asset object / contentType / byteSize / sha256

즉 Paperclip는
“무엇이 만들어졌는가”도
issue와 분리된 artifact 층으로 남긴다.

## 8. current reading

지금 기준에서 가장 중요한 건 이거다.

Paperclip는 한 덩어리 앱이 아니라,
이미 내부적으로도 아래처럼 면이 갈라져 있다.

- issue surface
- run surface
- event surface
- governance surface
- cost surface
- output surface

그래서 이후 어떤 overlay를 생각하더라도,
먼저 “이 여섯 면 중 어디를 intake 대상으로 삼을지”가 결정되어야 한다.

## 한 줄 요약

Paperclip는 단순 multi-agent task manager가 아니라, `work unit`, `run trace`, `event/log`, `governance`, `cost/control`, `output artifact` 여섯 추출면을 가진 control plane이며, 이후 어떤 결합 논의든 이 추출면 단위로 봐야 덜 헷갈린다.
