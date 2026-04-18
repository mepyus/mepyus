# VectorFL Paper Proper Page Tree v0

## purpose

이 문서는 `VectorFL Paper proper`가
어떤 페이지 구조로 자라야 하는지,
그리고 그 구조가 왜 통합 엔진 성장 방향과 맞는지
문장으로 잠근다.

핵심은 단순 페이지 나열이 아니다.
핵심은 아래 루프가 한 공간 안에서 닫히도록
페이지 클래스를 잡는 것이다.

`scenario-bearing input -> internal read -> selective external comparison -> cell / worker execution -> governance decision -> trace / return -> next loop`

---

## top direction

`VectorFL Paper`는 멀티에이전트 UI가 아니다.
또한 Paperclip의 회사 ontology를 옮겨놓는 제품도 아니다.

`VectorFL Paper proper`는
내부 재독해와 line 숙성을 중심으로,
CLI가 관리하는 운영 셀을 붙이고,
그 실행 결과를 감독자 판단 언어로 올린 뒤,
다시 내부 기억으로 귀속시키는
숙성형 통합 엔진이어야 한다.

따라서 페이지 구조도
예쁜 대시보드가 아니라
이 숙성 루프를 닫는 순서로 잡혀야 한다.

---

## page tree

### 1. Home / Operating Board

이 페이지는 첫 진입면이다.
사용자는 여기서 바로
지금 무엇을 증명 중인지,
어디가 막혔는지,
어떤 셀이 움직이고 있는지,
내가 어떤 판단을 해야 하는지
읽을 수 있어야 한다.

이 페이지의 역할은
`overview`가 아니라
`supervisor entrypoint`다.

핵심 섹션:

- current proof
- active cases
- decision queue
- active cells and cli runs
- latest returns
- remaining gates

### 2. Intake

이 페이지는 입력을 TODO로 납작하게 만들지 않기 위해 존재한다.
여기서는 scenario-bearing material을
실제 loop seed로 바꾸는 판단이 일어난다.

핵심 섹션:

- scenario entry
- material bundle review
- scenario-bearing check
- bundle preview
- intake route
- launch / hold / preview

### 3. Cases

이 페이지는 현재 숙성 중인 case들을 다룬다.
`VectorFL Paper`의 reading-first 성격은
이 페이지군에서 가장 강하게 드러나야 한다.

하위 페이지:

- case list
- case detail
- inspector
- internal recall
- evidence bundles
- loop history

`case detail`은 본체에 가깝다.
여기서는 source, line seed, stable / unclear, evidence bundle,
human translation, unread boundary, next action이
한 흐름으로 보여야 한다.

`inspector`는 단순 속성 패널이 아니라
선택된 line이나 bundle 뒤의 declaration, directive, judgment history,
family linkage, uncertainty를 여는 내부 기억 기관이어야 한다.

### 4. Cells

이 페이지군은 팀과 역할을
실제 operating cell로 다루는 층이다.
통합 엔진으로 성장하려면
셀이 늘어나도 전체 handoff 구조와 관리 상태가
한눈에 보여야 한다.

하위 페이지:

- cell registry
- cell detail
- cell editor
- cell relation map
- cell health

각 셀은 최소한
lens, managed internal functions, managing cli, md contract,
outputs, handoff targets, external pair cell을 드러내야 한다.

### 5. Workers / CLI

이 페이지군은 CLI 도구 연결이 실제로 일어나는 면이다.
Codex나 Gemini가 단순 외부 툴이 아니라
`cell manager`로 작동하려면
이 페이지군이 필요하다.

하위 페이지:

- worker registry
- worker detail
- adapter config
- launch panel
- run console
- payload preview

여기서 보여야 하는 것은
누가 어떤 셀을 관리하는지,
어떤 contract를 읽는지,
어떤 payload로 실행되는지,
결과가 어디로 귀속되는지다.

### 6. Governance

이 페이지군은 통합 엔진의 stop layer다.
여기서 인간 감독자는
go / hold / reopen / redirect를 판단한다.

하위 페이지:

- supervisor board
- decision queue
- governance gate
- approval history
- protection rules

VectorFL의 governance는
Paperclip의 회사 운영 governance와 다르다.
여기서는 approval 그 자체보다
reading protection, premature closure 방지,
promotion 금지, hold 이유 보존이 더 중요하다.

### 7. Trace

이 페이지군은 실행과 귀속을 연결한다.
로그만 모아두는 곳이 아니라
이번 loop가 어떻게 다시 내부로 들어왔는지 보이는 면이어야 한다.

하위 페이지:

- activity audit
- run trace
- reopen history
- return / reinjection
- residue / unresolved

핵심은 `append-only trace`가
다음 internal read와 next probe로 이어져야 한다는 점이다.

### 8. External Comparison

이 페이지군은 internal-first, external-ready 원칙을
표면으로 보여주는 곳이다.
외부 자료는 여기서 broad search가 아니라
내부 gap을 더 정밀하게 다루기 위한 비교 대상으로 다뤄진다.

하위 페이지:

- comparison targets
- reference candidates
- injection review
- overlay mapping
- external pair cells

### 9. Teams / Expansion

이 페이지군은 셀이 늘어나고 팀이 커질 때를 대비한 확장면이다.
처음부터 모든 기능이 필요하진 않지만,
구조는 처음부터 통합 엔진 방향을 품고 있어야 한다.

하위 페이지:

- team overview
- team selection
- role assignment
- multi-team board
- growth path

이 페이지군의 목적은
팀을 보기 좋게 나열하는 것이 아니라,
여러 셀이 같은 loop grammar 아래서
어떻게 병렬로 움직이는지 보이게 하는 것이다.

### 10. Memory / Contracts

이 페이지군은 철학과 계약이
실행에서 분리되지 않게 만드는 기억층이다.

하위 페이지:

- contracts
- line registry
- conversation-to-line
- internal return memory
- operating principles

이 페이지군이 있어야
지금까지 만든 내부 자료와 계약 문서가
죽은 메모가 아니라
다음 loop의 operating basis로 계속 재사용된다.

---

## first implementation cut

1차에서는 모든 페이지를 다 만들 필요는 없다.
하지만 통합 엔진으로 자라기 위한 최소 5페이지는 먼저 살아야 한다.

- operating board
- intake
- case detail
- cell / worker panel
- trace / governance

이 다섯 페이지가 살아 있으면
입력, 읽기, 실행, 감독, 귀속이
한 바퀴 닫힌다.

---

## page-flow rule

중요한 것은 트리보다 흐름이다.
최소 연결은 아래처럼 닫혀야 한다.

`Operating Board -> Case Detail -> Inspector -> Cell / Worker Panel -> Trace / Governance -> Return -> next Case loop`

즉 페이지는 각각 독립된 화면이 아니라
한 루프의 다른 단면이어야 한다.

---

## paperclip translation rule

이 구조는 Paperclip를 그대로 복제한 것이 아니다.
다만 Paperclip의 operable page class와 control-plane flow를
VectorFL 목적에 맞게 번역한 것이다.

번역의 기준은 아래와 같다.

- dashboard -> supervisor board
- issue -> current case or line-guided work packet
- issue detail -> case detail
- issue properties -> inspector / governance fields
- agent detail -> cell / worker operating panel
- activity -> trace audit
- approval -> supervisor gate
- heartbeat run -> execution pass / run trace

---

## one-line lock

`VectorFL Paper proper`는
읽기 엔진, CLI 운영면, 감독 보드, trace 귀속면,
그리고 팀 확장면이 하나의 loop grammar 아래서 이어지는
숙성형 통합 엔진의 페이지 구조를 가져야 한다.
