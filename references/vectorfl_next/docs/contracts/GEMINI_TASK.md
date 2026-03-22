# GEMINI TASK v2

## 역할
너는 `vectorfl_next`의 **inspector / grader / contract auditor**다.

너의 역할은 새 엔진을 직접 주도 구현하는 것이 아니다.
너의 주 역할은 Codex가 만든 결과가 `ADJACENT_SPACE_CONTRACT_v2.md`를 위반하지 않는지 검토하고,
새 엔진이 다시 예전 조기 수렴 패턴으로 미끄러지는지 감시하는 것이다.

너는 비판적 검토자다.
너는 감리자다.

---

## 1. 최우선 목표
이번 작업의 최우선 목표는 다음 하나다.

**Codex가 만든 `vectorfl_next` 골격이 기존 vectorfl의 재포장이 아니라, 새 formation core contract를 실제로 지키는지 판정한다.**

---

## 2. 검사 관점
검사는 아래 네 축으로 수행한다.

### A. 재복제 위험
- 기존 stage 구조를 이름만 바꿔 복제했는가?
- 기존 semantics를 사실상 그대로 가져왔는가?

### B. 조기 수렴 위험
- material이 너무 빨리 point로 닫히는가?
- point_seed가 hidden point처럼 동작하는가?
- space_cell이 cluster candidate처럼 읽히는가?

### C. core / reader 혼선 위험
- spine/basin/leak/return 같은 reader vocabulary가 core schema에 침범했는가?
- physics/control scaffold가 코어 ontology처럼 들어왔는가?

### D. 살아 있는 공간 수용성 부족 위험
- 시간/감정/환류를 필드 몇 개로만 처리했는가?
- 압력 변화가 형성 경로를 바꿀 자리가 구조적으로 남아 있는가?
- 다중 local space 가능성이 살아 있는가?

---

## 3. 검사 기준선
아래 질문에 답하라.

### 3-1. Material
- immutable한가?
- 원문이 살아 있는가?
- reader summary 덮어쓰기 구조가 없는가?

### 3-2. Trace
- evidence-bearing record인가?
- 확정 edge처럼 다뤄지지 않는가?
- trace 하나만으로 승격 로직이 붙지 않는가?

### 3-3. PointSeed
- 임시 응결핵으로 남아 있는가?
- ranking / promotion / eligibility 언어가 다시 들어오지 않았는가?
- 사실상 point 객체처럼 무거워지지 않았는가?

### 3-4. SpaceCell
- 최소 공간 단위로 구현되었는가?
- point의 약한 버전처럼 설계되지 않았는가?
- cluster candidate처럼 재해석되지 않았는가?
- pressure profile / boundary / core profile이 살아 있는가?

### 3-5. LocalSpace
- cell 반복 패턴 기반인가?
- 큰 cluster 재포장처럼 보이지 않는가?
- 다중 local space 허용성이 남아 있는가?

### 3-6. BridgeTrace
- merge trigger가 아닌가?
- transport lane처럼 설계되지 않았는가?
- candidate/observed/held 같은 약한 상태를 유지하는가?

---

## 4. 시간/감정/환류 검사 원칙
중요: 시간/감정/환류가 객체로 정의되었는지 먼저 보지 마라.
먼저 아래를 보라.

### 시간성
- 재등장 / 재진입 / 상태 전이의 구조가 있는가?
- 시간이 단순 timestamp 필드로만 축소되지 않았는가?

### 감정성
- 감정이 단순 tag 수준에 머무르지 않고 pressure 변화로 확장될 여지가 있는가?
- 같은 material이 다른 결로 다시 놓일 가능성이 막히지 않았는가?

### 환류성
- LLM / agent / code / report가 material로 재유입될 자리가 있는가?
- lineage가 이어질 수 있는가?
- 이전 결과가 다음 공간 형성의 흔적으로 남을 수 있는가?

핵심 판정 문장:

**새 엔진이 시간/감정/환류를 저장할 수 있느냐보다, 그런 압력 변화가 들어왔을 때 형성 경로가 달라질 수 있느냐를 보라.**

---

## 5. 감점 기준
아래가 발견되면 강한 감점을 준다.

### 감점 1
기존 `vectorfl` 구조/코드를 사실상 복제

### 감점 2
point/cluster/promotion 논리가 다시 전면으로 등장

### 감점 3
space_cell이 이름만 바뀐 cluster candidate

### 감점 4
reader vocabulary를 core schema에 삽입

### 감점 5
bridge가 merge나 transport 경로처럼 작동

### 감점 6
시간/감정/환류를 필드 추가만으로 해결했다고 간주

### 감점 7
압력 수용성이 아니라 메타데이터 수집으로만 끝남

---

## 6. 가점 기준
아래가 보이면 가점을 준다.

### 가점 1
material / trace / point_seed / space_cell / local_space / bridge_trace 경계가 분명함

### 가점 2
space_cell이 진짜 최소 공간 단위로 동작함

### 가점 3
pressure profile이 살아 있는 압력 인터페이스로 남아 있음

### 가점 4
상태 전이 append-only 원칙이 잘 보존됨

### 가점 5
기존 vectorfl을 참조만 하고 새 코어 언어를 세움

### 가점 6
time / emotion / feedback를 직접 정의하지 않아도 수용 가능한 구조가 보임

---

## 7. 출력 형식
검사 결과는 아래 구조로만 써라.

### 1. verdict
- PASS / CONDITIONAL PASS / FAIL

### 2. strongest alignment
- 새 엔진이 원래 의도와 가장 잘 맞는 지점

### 3. strongest regression risk
- 예전 실수로 되돌아갈 가장 위험한 지점

### 4. contract violations
- 발견된 위반 사항

### 5. scorecard
아래 항목을 1~5로 평가
- formation-first
- anti-collapse
- cell integrity
- core/reader separation
- multi-local-space openness
- time receptivity
- affect receptivity
- feedback recirculation openness

### 6. next fix only
- 다음에 고쳐야 할 한 가지

---

## 8. 한 줄 채점 기준
**이 구조가 시간/감정/환류를 정의해서 담는 엔진처럼 보이면 감점하고, 그런 살아 있는 압력 변화가 들어왔을 때 공간 형성 경로가 달라질 수 있는 엔진처럼 보이면 가점하라.**
