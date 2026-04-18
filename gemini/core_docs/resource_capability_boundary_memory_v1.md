# resource_capability_boundary_memory_v1.md

## 1. purpose

이 문서는 `vectorfl_replica` 엔진 운용에서
Codex와 외부 자원(Gemini CLI 및 미래 자원들)의 능력 차이,
위임 한계,
확인/검증 필요성을 기억하기 위한 기준 문서다.

핵심 전제:

**외부 자원을 나와 동일한 처리 주체로 가정하지 않는다.**

위임은 능력 동등성 가정 위에서가 아니라,
능력 차이와 실패 위험을 명시적으로 기록한 뒤에만 허용한다.

---

## 2. top principle

### 2-1. know thyself, know the resource

`나 자신을 알라`는 여기서 두 겹 의미를 가진다.

- Codex가 무엇을 안정적으로 할 수 있는지 안다
- Gemini CLI 같은 외부 자원이 무엇을 안정적으로 못 하는지도 안다

즉 위임 판단의 출발점은
“외부 자원도 대충 되겠지”가 아니라
**처리 능력 차이의 기록**이다.

### 2-2. equivalence assumption is forbidden

금지:

- 나와 같은 수준의 canonical judgment를 할 수 있다고 가정
- 나와 같은 수준의 구조 보존 감각이 있다고 가정
- 나와 같은 수준의 맥락 지속성을 가진다고 가정
- 나와 같은 수준의 보수 판정을 할 수 있다고 가정

---

## 3. codex role memory

Codex는 현재 엔진에서 다음을 맡는다.

- canonical operating state finalization
- core / derived / surface / experimental 경계 관리
- update policy 준수 여부 판단
- compare verdict
- false recovery / false improvement 차단
- external resource output adoption / ignore / partial reflect 결정

즉 Codex는 단순 실행자가 아니라
**메인 운용자 + 경계 판단자 + 최종 반영자**다.

---

## 4. gemini cli role memory

Gemini CLI는 현재 다음 범위에서만 신뢰한다.

- read-only summary
- diff review
- pointer/path consistency check
- discrepancy note
- thin briefing / draft log

즉 Gemini CLI는
**후단 보조 판독기**로만 신뢰한다.

아직 신뢰하지 않는 것:

- canonical enum 선택
- 구조 경계 판정
- 정책/freeze 판단
- promotion 판단
- deletion/merge/compaction 승인
- 강한 구조 개조 제안

---

## 5. failure risk memory

외부 자원에 대해 항상 기억해야 하는 위험:

### 5-1. acceleration / overreach risk

- 갑자기 구조 변경 제안이 커질 수 있다
- 제한하지 않으면 과한 일반화를 할 수 있다

### 5-2. false confidence risk

- 불확실한 것을 확정적으로 말할 수 있다
- 읽은 범위보다 더 강한 판단을 할 수 있다

### 5-3. boundary leakage risk

- read-only review가 canonical recommendation처럼 보일 수 있다
- experimental 관찰을 core truth처럼 다룰 수 있다

### 5-4. context compression risk

- 긴 맥락을 단순화하면서 핵심 경계를 놓칠 수 있다
- 같은 말처럼 보이는 것들을 성급히 합칠 수 있다

---

## 6. delegation rule

외부 자원에게 업무를 넘기기 전에 항상 아래를 먼저 확인한다.

1. 이 작업은 read-only인가?
2. canonical 최종 판단이 필요한가?
3. 경계/freeze/policy를 건드리나?
4. 출력이 summary/check/discrepancy 수준으로 충분한가?
5. 결과를 바로 반영하지 않고 candidate layer로 받을 수 있는가?
6. 실패해도 core가 오염되지 않는가?

하나라도 불안정하면 위임하지 않는다.

---

## 7. trust growth rule

외부 자원에게 더 많은 일을 맡기기 전에
반드시 다음 과정을 거친다.

### stage 1. narrow read-only task

- 요약
- diff review
- pointer check

### stage 2. bounded analytical task

- cohort compare read
- anomaly note
- discrepancy clustering

### stage 3. repeated verification

- 같은 유형 업무를 여러 번 반복
- 급발진/과잉 일반화/경계 침범 여부 기록

### stage 4. limited delegation expansion

- stage 1~3 검증이 누적된 뒤에만
- 조금 더 넓은 분석 업무를 허용

즉 위임은 선언으로 늘리지 않고
**반복 검증으로만 확장**한다.

---

## 8. memory rule

이 문서는 앞으로 Gemini뿐 아니라
다른 외부 자원을 붙일 때도 공통 기준으로 재사용한다.

새 자원을 붙일 때마다 아래를 기록한다.

- 무엇을 잘 하는가
- 무엇을 못 하는가
- 어떤 실패 패턴이 있었는가
- 어디까지 신뢰 가능한가
- 어떤 packet 형태가 안전한가

---

## 9. one-line lock

외부 자원 위임의 출발점은 능력 동등성 가정이 아니라, 능력 차이와 실패 위험을 기록하는 것이다. Codex는 그 기록을 바탕으로만 업무를 분할한다.
