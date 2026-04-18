# VectorFL Paper Trace Governance Sections v0

## purpose

이 문서는 `Trace / Governance` 면이
실행 흔적과 인간 판단을 함께 닫는 페이지로 작동하려면
무엇을 보여줘야 하는지 섹션 단위로 잠근다.

---

## page role

이 페이지는 아래 질문에 답해야 한다.

- 어떤 run이 실제로 일어났는가
- 무엇이 append-only trace로 남았는가
- 어떤 governance gate가 현재 걸려 있는가
- 왜 reopen이 발생했는가
- 무엇이 reinjection으로 돌아왔는가
- 지금 supervisor는 무엇을 결정해야 하는가

즉 이 페이지는
로그 뷰어가 아니라
`loop closure and decision page`여야 한다.

---

## section order

### 1. run trace

- current packet
- current trace summary
- source packet ref
- trace state

### 2. governance gate

- route gate
- hold trace
- promotion gate
- caution note

### 3. reopen history

- reopen summary
- why reopen now
- reopen questions
- next reread target

### 4. reinjection

- advisory return hint
- changed line or next probe
- target return slot

### 5. supervisor decision

- current decision mode
- what decision is needed now
- what changes if approved

### 6. next loop trigger

- next cell
- trigger condition
- why another loop is justified

---

## global page rules

### rule 1

trace must remain append-only in language and structure.

### rule 2

governance must protect reading quality before promotion.

### rule 3

reopen should read as part of the loop, not as failure noise.

### rule 4

reinjection must explicitly point back into internal memory or next probe.

### rule 5

the page must make the current supervisor decision legible without reading raw manifests.

---

## one-line lock

`Trace / Governance`는
run, gate, reopen, reinjection, supervisor decision,
and next loop trigger가 한 면에서 닫히는
loop-closing page여야 한다.
