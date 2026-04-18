# VectorFL Paper Operating Board Sections v0

## purpose

이 문서는 `VectorFL Paper proper`의 첫 화면인
`Operating Board`가 무엇을 먼저 보여줘야 하는지
섹션 단위로 잠근다.

핵심은 overview가 아니라
감독자가 즉시 현재 loop를 판단할 수 있는
`supervisor entrypoint`를 만드는 것이다.

---

## board role

`Operating Board`는 아래 질문에 먼저 답해야 한다.

- 지금 무엇을 증명 중인가
- 어떤 case들이 살아 있는가
- 어디가 막혀 있는가
- 어떤 셀이 움직이고 있는가
- 내가 지금 어떤 판단을 해야 하는가
- 최근 무엇이 다시 내부로 돌아왔는가

즉 첫 화면은
artifact index가 아니라
현재 operating judgment surface여야 한다.

---

## section order

### 1. current proof

가장 위에 와야 한다.

보여줄 것:

- one-line current proof
- why this loop exists now
- current stage
- single remaining gate

왜 필요한가:

사용자가 첫 5초 안에
현재 loop의 의미를 잡아야 하기 때문이다.

### 2. decision queue

보여줄 것:

- go / hold / reopen / redirect 대기 항목
- decision urgency
- why decision is needed
- what changes if approved

왜 필요한가:

이 보드의 핵심은
`무엇이 중요한가`를 먼저 보여주는 것이다.

### 3. active cases

보여줄 것:

- active case list
- current loop stage
- current line pressure
- blocked reason or next move

왜 필요한가:

case 목록이 단순 리스트가 아니라
현재 숙성 루프의 active set으로 읽혀야 한다.

### 4. active cells and cli runs

보여줄 것:

- active cells
- owning cli
- run state
- current handoff direction
- stuck / idle / waiting signals

왜 필요한가:

통합 엔진으로 자라려면
사용자는 어떤 셀과 어떤 CLI가
현재 일을 받고 있는지 즉시 볼 수 있어야 한다.

### 5. latest returns

보여줄 것:

- recent reinjection
- recent reopen
- recent changed line
- recent changed bundle or next probe

왜 필요한가:

이 엔진의 핵심은
실행 결과가 내부로 돌아오는 것이다.
그러므로 보드에서도 최근 return이 보여야 한다.

### 6. remaining gates

보여줄 것:

- realism gate
- reading protection gate
- external comparison gate
- promotion gate

왜 필요한가:

지금 무엇이 아직 닫히지 않았는지 보여주지 않으면
보드는 progress board처럼 보이게 된다.

---

## global board rules

### rule 1

첫 화면은 counts보다 문장으로 시작해야 한다.

### rule 2

각 섹션은 반드시
`why this matters now`
를 짧게 드러내야 한다.

### rule 3

active case, active cell, latest return은
모두 같은 current loop grammar 안에서 읽혀야 한다.

### rule 4

company, team, agent 같은 외부 ontology naming을
보드의 1차 언어로 쓰지 않는다.

### rule 5

artifact file refs는 보조다.
보드의 주언어는 supervisor-readable language여야 한다.

---

## first implementation note

1차에서는 숫자 metric보다
아래 여섯 블록이 먼저 살아야 한다.

- current proof
- decision queue
- active cases
- active cells and cli runs
- latest returns
- remaining gates

이 여섯 블록이 살아 있으면
사용자는 첫 화면에서
`무엇을 하는 중인지 / 어디서 개입해야 하는지`
바로 읽을 수 있다.

---

## one-line lock

`Operating Board`는
현재 loop의 의미, 현재 개입 포인트, 현재 귀속 변화,
그리고 남은 gate를 먼저 보여주는
감독자용 operating surface여야 한다.
