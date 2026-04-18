# VectorFL Paper Cell Worker Panel Sections v0

## purpose

이 문서는 `Cell / Worker Panel`이
통합 엔진의 실제 운영면으로 작동하려면
무엇을 보여줘야 하는지 섹션 단위로 잠근다.

핵심은 셀과 CLI를
이름 목록이 아니라
`contract-driven operating units`로 보이게 하는 것이다.

---

## panel role

이 패널은 아래 질문에 답해야 한다.

- 어떤 셀이 지금 선택되었는가
- 그 셀의 lens와 역할은 무엇인가
- 어떤 CLI가 이 셀을 관리하는가
- 어떤 md 계약을 읽는가
- 어떤 payload로 실행되는가
- 결과는 어디로 돌아오는가

즉 이 패널은
프로필 화면이 아니라
실행과 귀속이 함께 보이는 운용면이어야 한다.

---

## section order

### 1. cell registry

보여줄 것:

- active and available cells
- lens label
- current state
- current owner cli

왜 필요한가:

팀이 늘어나도
사용자가 셀의 존재와 상태를 한눈에 봐야 한다.

### 2. selected cell detail

보여줄 것:

- cell purpose
- lens
- managed internal functions
- outputs
- handoff targets
- external pair cell

왜 필요한가:

셀은 역할 이름이 아니라
입력, 판단, 산출, handoff를 가진 operating cell로 보여야 한다.

### 3. cli ownership

보여줄 것:

- primary cli
- secondary cli
- why this cli owns this cell
- current cli responsibility

왜 필요한가:

CLI가 외부 도구가 아니라
cell manager라는 점이 표면에서 분명해야 한다.

### 4. contract readout

보여줄 것:

- md contract ref
- allowed actions
- disallowed actions
- required evidence
- return slot

왜 필요한가:

이 계약이 보여야
사용자도 왜 이 셀이 이렇게 움직이는지 이해할 수 있다.

### 5. adapter config

보여줄 것:

- provider
- model
- environment policy
- timeout
- budget or run constraints
- enabled flag

왜 필요한가:

CLI 연결이 진짜 운영면이 되려면
실행 조건이 표면에 노출되어야 한다.

### 6. payload preview

보여줄 것:

- current request payload
- selected case
- selected line or bundle
- requested action
- target return slot

왜 필요한가:

실행 전에
무엇을 어떤 맥락으로 보내는지
감독자와 운영자가 같이 읽어야 한다.

### 7. launch controls

보여줄 것:

- dry-run
- launch
- export
- reopen
- cancel or hold

왜 필요한가:

실행은 단순 버튼이 아니라
governance-aware action이어야 한다.

### 8. return slot

보여줄 것:

- where result lands
- how trace is appended
- how reinjection is formed
- what can reopen the case

왜 필요한가:

통합 엔진은 실행보다 귀속이 더 중요하다.
그래서 return structure가 패널 안에 명시돼야 한다.

---

## global panel rules

### rule 1

cell name보다 lens와 role이 먼저 읽혀야 한다.

### rule 2

cli detail은 기술 정보만이 아니라
운영 책임 언어로도 같이 보여야 한다.

### rule 3

payload preview와 return slot은
항상 짝으로 보여야 한다.

### rule 4

launch controls는
trace / governance surface와 끊기면 안 된다.

### rule 5

Paperclip agent/company naming을
canonical language로 쓰지 않는다.

---

## first implementation note

1차에서는 최소 아래 여덟 블록이 살아야 한다.

- cell registry
- selected cell detail
- cli ownership
- contract readout
- adapter config
- payload preview
- launch controls
- return slot

이 여덟 블록이 있으면
팀 선택, 역할 배정, cli 연결, 실행, 귀속이
한 패널 안에서 읽힌다.

---

## one-line lock

`Cell / Worker Panel`은
어떤 셀이 어떤 CLI와 계약 아래서 어떤 payload를 실행하고,
그 결과를 어디로 귀속시키는지 보여주는
통합 엔진의 실제 운용 패널이어야 한다.
