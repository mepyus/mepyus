# Paperclip Structural Fit for VectorFL v0

## 목적

이 문서는
[paperclip-master](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master)
를 기능 / 구조 / 철학 기준으로 다시 읽고,
그 구조를 현재 VectorFL 공간에
`입력기 / 라인생성기 / 라인해석기 / 라인점검기 / 라인추출기`
같은 역할 분담 구조로 붙일 수 있는지 검토한다.

핵심 질문은 아래다.

- Paperclip의 조직/업무 분담 shell을
  VectorFL의 line-centered space 위에 얹을 수 있는가
- 그 경우 무엇을 가져오고 무엇은 그대로 두면 안 되는가

## 1. Paperclip의 기능 요약

Paperclip은 본질적으로
`회사 운영 control plane`
이다.

기능상 중심은 다섯 가지다.

1. `company boundary`
   - 모든 엔티티가 company에 소속된다
   - budget, issue numbering, approval policy가 company 단위로 묶인다

2. `agent org tree`
   - agent는 `reportsTo`로 strict tree를 가진다
   - 각 agent는 adapter / runtime / budget을 가진다

3. `single-owner issue system`
   - 모든 일은 issue로 쪼개지고
   - single assignee와 atomic checkout을 가진다

4. `heartbeat execution loop`
   - agent는 heartbeat로 깨어나 task를 처리한다
   - 세션 / workspace / usage / result / log가 run 단위로 남는다

5. `governance and budget`
   - hire approval
   - budget hard stop
   - board intervention

즉 Paperclip은
agent를 만드는 framework가 아니라
agent 회사의 운영 shell이다.

## 2. Paperclip의 구조 요약

현재 코드 기준으로 가장 중요한 구조는 아래다.

### 2-1. boundary first

- [companies.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/companies.ts)

모든 business entity가 `company_id`에 묶인다.
즉 먼저 company boundary가 있고,
그 안에 나머지 구조가 들어간다.

### 2-2. org tree

- [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/agents.ts)
- [agents.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/agents.ts)

agent는

- `reportsTo`
- `adapterType`
- `adapterConfig`
- `runtimeConfig`
- `budgetMonthlyCents`

를 가진다.

즉 “누가 누구 밑에서 어떤 runtime으로 얼마까지 일할 것인가”가
agent row에 직접 박혀 있다.

### 2-3. issue as work atom

- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/packages/db/src/schema/issues.ts)
- [issues.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/issues.ts)

issue는

- company
- goal / project
- parent issue
- single assignee
- checkout run
- execution run

을 한 곳에 묶는다.

즉 업무 분담은 chat가 아니라 issue atom 기준이다.

### 2-4. heartbeat as operating loop

- [heartbeat.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/heartbeat.ts)

heartbeat는 단순 timer가 아니라

- wake source
- workspace realization
- adapter invocation
- session carryover
- log / usage / result capture

를 한 번에 묶는 execution loop다.

### 2-5. governance as stop layer

- [budgets.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/budgets.ts)
- [approvals.ts](/Users/sungsookim/universe/vectorfl_replica/references/git_search/paperclip-master/server/src/services/approvals.ts)

Paperclip은 자동화만 하는 것이 아니라
어디서 멈추고 누가 승인하는지도 함께 모델링한다.

즉 orchestration은 항상
`work routing + stop conditions`
의 쌍으로 읽혀야 한다.

## 3. Paperclip의 철학

README와 implementation spec를 같이 보면
Paperclip의 철학은 아래에 가깝다.

- agent는 employee다
- company는 first-order object다
- task는 ticket-based로 추적돼야 한다
- context는 task -> project -> company goal chain으로 올라가야 한다
- autonomy는 governance와 예산 아래서만 허용된다

즉 Paperclip은
“많은 agent를 돌리는 기술”
보다
“그 agent들을 회사처럼 운영하는 질서”
를 더 중요하게 본다.

## 4. 이 구조를 VectorFL에 그대로 가져오면 안 되는 이유

현재 VectorFL의 중심은

- bounded functional space
- line family
- projection
- route
- residue
- reentry

다.

Paperclip를 그대로 들여오면
중심 단위가 line이 아니라
company / agent / issue로 바뀔 위험이 있다.

즉 아래 같은 역전이 생길 수 있다.

- line-centered space -> task manager shell로 축소
- family invariant -> generic issue taxonomy로 평탄화
- residue / reentry -> comment / status history 정도로 약화

그래서 Paperclip를
제품 단위로 그대로 이식하면 안 된다.

## 5. VectorFL에 구조적으로 붙일 수 있는 층

붙일 수 있는 것은
제품 전체가 아니라
구조적 shell이다.

### 5-1. company boundary -> bounded operational shell

Paperclip의 company는
VectorFL에선 회사 그 자체보다
`bounded operational shell`
로 번역하는 게 맞다.

즉 예:

- `tank_program`
- `input_ingest_space`
- `transition_validation_space`
- `operating_readout_space`

같은 bounded space를
실제 운영 대상 shell로 둘 수 있다.

### 5-2. agent org tree -> line role tree

이건 가장 직접적으로 붙일 수 있다.

Paperclip의 agent tree를
VectorFL에선 role tree로 번역한다.

예:

- input operator
- line generator
- line interpreter
- line checker
- line extractor

중요한 점은
이걸 사람 같은 캐릭터로 둘 필요는 없고,
`line-facing operating responsibility`
로 둬야 한다는 점이다.

### 5-3. issue system -> line-bound work packet

이건 이미 우리 쪽에 준비된 기반이 있다.

- [line_guided_work_packet_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/line_guided_work_packet_v1.md)
- [line_guided_work_packet_manifest_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/line_guided_work_packet_manifest_v0.md)

즉 Paperclip issue를 그대로 쓰는 대신,
issue를 line-bound work packet으로 번역해
각 역할 노드에 넘기는 방식이 맞다.

### 5-4. heartbeat -> line operating loop

Paperclip heartbeat는 강하게 가져올 수 있다.
다만 내용은 바꿔야 한다.

VectorFL 쪽 heartbeat-like loop는:

- assignment intake
- line translation
- line-guided execution
- residue capture
- reentry bias update

여야 한다.

즉 heartbeat shell은 가져오되,
실행 내부는 line spine이 먹어야 한다.

### 5-5. governance -> promotion / residue / route gate

budget / approval 철학은 가져올 수 있다.
다만 money governance보다 먼저
line governance로 번역하는 편이 맞다.

예:

- route selection gate
- residue promotion gate
- family handoff gate
- future flow-line promotion gate

즉 board approval를
line system의 formalization gate로 바꿔 읽는 것이다.

## 6. 제안하는 역할 구조

현재 VectorFL에 가장 자연스럽게 붙는 최소 구조는 아래다.

### 6-1. line input operator

역할:

- source surface intake
- hint generation
- entry bias update

현재 연결 자산:

- auto hint generation
- source_to_family_hints

### 6-2. line generator

역할:

- source를 line candidate로 번역
- family / projection / route 초기 선택안 생성

현재 연결 자산:

- family invariant
- projection registry
- route registry

### 6-3. line interpreter

역할:

- current hint / reentry prebias / classifier를 조합해
  active line path를 읽는다

현재 연결 자산:

- classifier adapter
- prototype execution spine

### 6-4. line checker

역할:

- residue-backed reentry consistency 확인
- same-family shift vs cross-family handoff 점검
- boundary warning 생성

현재 연결 자산:

- residue_reentry_rules
- reentry_prebias
- classifier priority / selection policy

### 6-5. line extractor

역할:

- execution trace 축적
- repeated pattern detection
- weak flow candidate report 작성

현재 연결 자산:

- execution_trace_log_v0.jsonl
- flow_candidate_detection_v0

## 7. 이 구조를 붙일 때의 가장 좋은 해석

가장 좋은 해석은 이렇다.

Paperclip를
“회사를 돌리는 앱”
으로 가져오는 것이 아니라,

`업무를 나누고 역할을 배정하고 주기적으로 작업을 깨우는 shell`
로만 가져온다.

그 shell 안에서 실제 작업 단위는

- generic task가 아니라 line-bound work packet
- generic status가 아니라 family / projection / route state
- generic result가 아니라 residue / reentry bias / flow candidate trace

가 된다.

즉 Paperclip는
VectorFL를 대체하지 않고,
VectorFL 역할 노드를 조직화하는 외곽 shell로만 쓰인다.

## 8. 구조적으로 가능한가

가능하다.

다만 아래 순서를 지켜야 한다.

1. company shell을 그대로 들이지 않는다
2. line role tree부터 먼저 번역한다
3. issue를 line-bound work packet으로 치환한다
4. heartbeat를 line operating loop로 재해석한다
5. governance를 promotion / residue / route gate로 옮긴다

즉 먼저 가져와야 할 것은
`조직 질서`
이지
`제품 UI`
가 아니다.

## 9. 현재 시점의 판단

지금 시점에서 Paperclip를 VectorFL에 붙이는 가장 좋은 방식은
아래다.

- Paperclip 강점:
  역할 배정 / single-owner work atom / heartbeat / governance
- VectorFL 강점:
  line family / projection / residue / reentry / candidate detection

둘을 합치면:

- Paperclip가 누가 무슨 bounded work를 맡는지 정하고
- VectorFL이 그 bounded work를 어떤 line spine으로 처리할지 정한다

이 구조는 꽤 설득력 있다.

반면 아직 이르거나 위험한 것은 아래다.

- company / board / budget 구조를 그대로 메인 ontolgy로 삼는 것
- line보다 issue/status를 더 앞세우는 것
- weak flow candidate를 바로 orchestration rule로 승격하는 것

## 10. 한 줄 요약

Paperclip는 VectorFL에 제품째로 붙일 대상이 아니라,
`line input operator / line generator / line interpreter / line checker / line extractor`
같은 역할 노드를 배정하고 깨우는
외곽 orchestration shell로 번역해 붙일 수 있으며,
그 경우 실제 일의 본체는 여전히 VectorFL의 line family / projection / residue / reentry spine이 되어야 한다.
