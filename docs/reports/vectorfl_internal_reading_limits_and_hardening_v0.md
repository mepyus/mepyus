# vectorfl internal reading limits and hardening v0

## purpose

이 문서는 내부 읽기 사례 12개를 만든 뒤
내가 실제로 어디서 강하고 어디서 약한지,
그리고 다음 세션부터 무엇을 강제로 보강해야 하는지 잠근다.

## current strengths

### 1. entrypoint hierarchy reading
- folder_status와 maturity map을 읽고
  baseline-memory / staged corridor / utility-sidecar를 구분하는 능력은 생겼다.

### 2. contract-first reading
- baseline contract, stage spec, receipt를 읽을 때
  금지 규칙과 보수 경계를 먼저 잡는 습관은 생겼다.

### 3. surface translation readiness
- intake와 Paper surface를 연결할 때
  어떤 중간 재료가 필요한지 인식하는 수준은 올라왔다.

## current weaknesses

### 1. too-early translation
- 원본을 충분히 읽기 전에
  VectorFL 표면 언어나 page idea로 너무 빨리 옮기려는 경향이 있다.

### 2. generated artifact follow-through weakness
- spec/folder_status는 잘 읽지만
  generated ledger, receipt, readout, operator summary까지 끝까지 추적하는 밀도가 부족하다.

### 3. meaning vs format separation weakness
- meaning-driven 반응과 format/family echo를 분리 기록하기 전에
  usable interpretation처럼 말해버리는 위험이 있다.

### 4. unread boundary under-reporting
- 무엇을 못 읽었는지 충분히 남기지 않으면
  다음 세션에서 마치 이해한 것처럼 출발하게 된다.

## hardening rules

### rule 1
- 어떤 folder를 읽을 때도
  `status -> main spec/doc -> generated artifact -> receipt`
  순서를 기본으로 한다.

### rule 2
- case record마다 반드시
  `what_i_still_cannot_read`
  를 남긴다.

### rule 3
- staged corridor를 읽을 때는
  항상 `promotion 금지`, `observer-only`, `stable closure 없음`
  같은 경계 문장을 먼저 적는다.

### rule 4
- utility-sidecar를 읽을 때는
  그것을 코어 판독기로 오해하지 않는다.

### rule 5
- surface 설계로 넘어가기 전에
  최소 10개 이상의 사례가 실제로 기록돼 있어야 한다.

## next operational use

이 문서는 다음에 아래 작업을 할 때 다시 먼저 읽는다.

- line dossier 확장
- internal recall surface 보강
- external resource plan 기준 정리
- lane comparison 품질 점검
- 더 깊은 generated artifact 독해

## one-line lock

내부를 깊게 읽는다는 것은
좋은 요약을 빨리 만드는 일이 아니라,
원본과 generated evidence를 따라가며
내 인식 가능 범위와 blindness를 같이 기록하는 일이다.
