# Paperclip Core Structure Map v0

## 목적

이 문서는
VectorFL 번역을 잠시 내려놓고,
`paperclip-master`를 그 자체의 제품/구조로 읽기 위한
기준면을 만든다.

핵심 질문은 단순하다.

- Paperclip의 중심 객체는 무엇인가
- 그 객체들은 어떻게 연결되는가
- 실제 operating loop는 어디서 닫히는가

## 1. 한 줄 정의

Paperclip은
`회사(company)를 경계로 두고, agent 조직도와 single-owner issue를 heartbeat loop로 운용하며, approval과 budget으로 제동을 거는 control plane`
이다.

즉 중심은 chat이 아니라

- company
- agent
- issue
- heartbeat run
- approval
- budget

이 여섯 객체다.

## 2. 중심 객체

### 2-1. company

기준 파일:

- [companies.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/companies.ts)
- [SPEC.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/doc/SPEC.md)
- [PRODUCT.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/doc/PRODUCT.md)

Paperclip에서 company는 first-order object다.

company가 들고 있는 것:

- 경계
- issue prefix / numbering
- top-level budget 상태
- 신규 agent 승인 정책

즉 company는 단순 폴더가 아니라
모든 business entity가 속하는 tenancy boundary다.

### 2-2. agent

기준 파일:

- [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/agents.ts)
- [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/agents.ts)

agent는 employee다.

agent가 들고 있는 것:

- role / title
- reportsTo
- adapterType / adapterConfig
- runtimeConfig
- budgetMonthlyCents
- status

즉 agent는 단순 실행기 인스턴스가 아니라
조직도 안의 직무 노드다.

### 2-3. goal / project

기준 파일:

- [goals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/goals.ts)
- [projects.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/projects.ts)

goal과 project는
회사의 방향과 중간 단위 work grouping이다.

goal은 “왜 이 일을 하는가”를 유지하고,
project는 그 안의 실행 묶음을 만든다.

즉 Paperclip은 task manager이지만,
task를 goal chain 위에 묶으려는 의도가 강하다.

### 2-4. issue

기준 파일:

- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issues.ts)
- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/issues.ts)

issue는 core task entity다.

issue가 들고 있는 것:

- company / project / goal / parent linkage
- single assignee
- checkout run / execution run
- status / priority
- request depth / origin
- optional workspace linkage

즉 issue는 단순 카드가 아니라
`업무 atom + 추적 anchor`
다.

### 2-5. heartbeat run

기준 파일:

- [heartbeat_runs.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/heartbeat_runs.ts)
- [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)

heartbeat run은 실제 operating loop 단위다.

heartbeat run이 들고 있는 것:

- 어떤 agent가 돌았는가
- 왜 호출됐는가
- 언제 시작/종료됐는가
- resultJson / usageJson
- session before/after
- logs / excerpts
- context snapshot

즉 Paperclip에서 “실행 흔적”의 중심은 heartbeat run이다.

### 2-6. approval

기준 파일:

- [approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/approvals.ts)
- [approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/approvals.ts)

approval은 board governance surface다.

중심 역할:

- high-impact action 잠금
- approve / reject / revision requested
- payload 기반 승인/거절 결과 적용

즉 approval은 “사람이 개입하는 표면”이다.

### 2-7. budget policy / cost event

기준 파일:

- [budget_policies.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/budget_policies.ts)
- [cost_events.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/cost_events.ts)
- [budgets.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/budgets.ts)

budget는 accounting보다
execution stop layer에 가깝다.

핵심은:

- observed spend를 cost event로 남기고
- policy threshold와 비교해서
- agent / project / company를 pause할 수 있다는 점이다.

즉 budget은 dashboard metric이 아니라
control surface다.

## 3. 객체 연결

구조를 가장 간단히 그리면 이렇다.

### 3-1. top boundary

`company`
-> 모든 핵심 객체가 여기에 묶인다

### 3-2. company 내부 조직

`company`
-> `agents`
-> strict org tree via `reportsTo`

### 3-3. direction chain

`company`
-> `goals`
-> `projects`
-> `issues`

즉 일은 그냥 생성되는 게 아니라
goal ancestry 위에 놓이도록 설계돼 있다.

### 3-4. execution chain

`issue`
-> assigned agent
-> heartbeat run
-> result / logs / session state

즉 issue가 일의 기준점이고,
heartbeat run이 실행의 기준점이다.

### 3-5. governance chain

`approval`
-> can create / activate / reject significant changes

`budget policy`
-> reads `cost_events`
-> can pause agent / project / company

즉 governance는 실행 뒤의 보고가 아니라
실행 가능/불가능을 바꾸는 층이다.

## 4. 실제 operating loop

Paperclip의 실제 operating loop는 아래처럼 읽힌다.

1. board/operator가 company와 goals를 잡는다
2. agents를 org tree로 배치한다
3. issues를 만든다
4. assignee agent가 heartbeat로 깨어난다
5. issue를 checkout/execution 한다
6. result / usage / log / session이 heartbeat run에 남는다
7. cost event와 budget policy가 계속 실행 가능성을 점검한다
8. approval이 필요한 변화는 board가 잠그거나 푼다

즉 Paperclip의 핵심 루프는
`task routing + governed execution`
이다.

## 5. 무엇이 중심이 아닌가

Paperclip를 제대로 읽으려면
무엇이 중심이 아닌지도 알아야 한다.

- line
- semantic memory
- residue
- reread
- projection
- route family

이건 Paperclip의 본래 ontology가 아니다.

또 public docs가 분명히 선을 긋는 것도 있다.

- chatbot이 아님
- prompt manager가 아님
- single-agent tool이 아님
- code review tool이 아님

즉 Paperclip의 중심은
해석 엔진이 아니라 운영 질서다.

## 6. 현재 기준에서 가장 중요한 이해

Paperclip를 이해할 때 가장 중요한 건 이 두 문장이다.

1. `company is first-order`
2. `issue + heartbeat + governance`가 실제 control loop를 만든다

이걸 놓치면
겉으로 task manager처럼 보이거나,
반대로 단순 multi-agent runner처럼 보이는데,
둘 다 절반만 본 것이다.

## 한 줄 요약

Paperclip는 `company boundary` 안에서 `agent org tree`와 `single-owner issue`를 `heartbeat run`으로 운용하고, `approval`과 `budget`으로 제동을 거는 회사 운영용 control plane이다.
