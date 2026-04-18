# VectorFL Current Reading Mock Fixture Set v0

이 문서는 `VectorFL Current Reading` 첫 mock shell에 사용할  
권장 fixture 시나리오와 fixture 묶음 구성을 잠근다.  
실제 JSON 파일을 만드는 문서가 아니라, 어떤 사례를 first mock의 기준 시나리오로 쓸지 정하는 문서다.

## 1. 목적

현재 단계에서 필요한 것은

- 첫 mock shell이 어떤 성격의 case를 읽어야 하는지
- 어떤 fixture 조합이 VectorFL다운 current-reading을 가장 잘 드러내는지

를 먼저 고정하는 것이다.

즉 이 문서는 mock contract 위에서 `first scenario selection`을 잠근다.

## 2. First Fixture Scenario Verdict

첫 mock fixture는 아래 성격으로 잡는 것이 가장 적절하다.

- `case 1개`
- `lane 1개`
- `mixed hold` 또는 `observer-only` 성격의 governance
- readable current-reading surface 1개
- residue / reentry 단서가 보이는 trace 1~2개
- optional intake weakness/fallback note

즉 `happy path completed case`보다
`해석은 생겼지만 governance와 caution이 아직 살아 있는 case`가 first mock에 더 적합하다.

## 3. Why This Scenario

이 시나리오를 first mock으로 쓰는 이유는 아래다.

### 3-1. VectorFL다움을 보여준다

VectorFL의 강점은 단순 결과 표시가 아니라

- current-reading
- governance
- residue
- reentry hint

가 같이 보이는 데 있다.

### 3-2. shell 역할을 과장하지 않게 한다

문제가 없는 완료 상태만 보여주면
shell이 그냥 dashboard처럼 읽힐 수 있다.

반대로 mixed/observer-only 사례를 쓰면
shell이 `판정 재정의`가 아니라 `판정 가시화` 역할이라는 점이 더 분명해진다.

### 3-3. caution visibility를 시험할 수 있다

hold, restriction, residue, weakness 같은 것이
adapter 과정에서 숨겨지지 않는지 확인할 수 있다.

## 4. Fixture Set Composition

첫 fixture set은 아래 여섯 묶음으로 읽는다.

### 4-1. Case Fixture

- 역할: case identity와 linked program, current anchor를 제공
- 성격:
  - active but not closed
  - current lane이 있고, current surface가 존재

### 4-2. Lane Fixture

- 역할: 현재 lane 상태와 next hop 후보를 제공
- 성격:
  - 진행 중 또는 hold 상태
  - next hop이 canonical 확정이 아니라 candidate 성격

### 4-3. Governance Fixture

- 역할: mixed hold / observer-only / release pending 같은 보호 조건을 제공
- 성격:
  - 완전 해제 상태보다 제한이 남아 있는 상태

### 4-4. Surface Fixture

- 역할: 현재 reading body와 supporting unit anchor를 제공
- 성격:
  - headline이 있고
  - operator가 지금 무엇을 읽어야 하는지 보이는 상태

### 4-5. Trace Preview Fixture

- 역할: residue note와 reentry hint를 제공
- 성격:
  - 1~2개만 있어도 충분
  - current issue와 연결된 trace여야 함

### 4-6. Optional Intake Caution Fixture

- 역할: intake 단계 약함이 current-reading에 다시 보이는지 시험
- 성격:
  - fallback used
  - weak intake
  - re-read needed
  중 하나 이상이 살아 있는 상태

## 5. First Mock Reading Target

이 fixture set으로 mock shell이 보여줘야 하는 핵심 질문은 아래다.

- 지금 이 case는 무엇을 읽고 있는가
- 지금 어느 lane에 있는가
- 왜 아직 멈춰 있거나 조심해야 하는가
- 다음에 무엇을 다시 봐야 하는가
- 어떤 residue / reentry가 남아 있는가

즉 first mock은
`결과를 보여주는 화면`보다
`현재 읽기와 보류 조건을 같이 보여주는 화면`이어야 한다.

## 6. Avoid Fixture Types For First Mock

첫 mock에는 아래 유형을 쓰지 않는 편이 맞다.

### 6-1. fully resolved happy path

- 이유:
  - governance와 caution이 잘 안 드러난다

### 6-2. trace-only case

- 이유:
  - current-reading body와 lane strip이 약해진다

### 6-3. intake-only raw case

- 이유:
  - current-reading shell보다 intake detail shell에 더 적합하다

## 7. Good Enough Mock Condition

아래가 보이면 first mock은 충분하다.

- case header가 보임
- current reading body가 보임
- lane strip이 보임
- governance card가 보임
- trace strip이 보임
- hold / restriction / residue / reentry / weakness 중 일부가 실제로 visible함

즉 상세 styling보다
`VectorFL다운 current-reading contract가 살아 있는가`
가 기준이다.

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Current Reading first mock fixture는 mixed hold 또는 observer-only 성격을 가진 active case 하나를 중심으로 Case/Lane/Governance/Surface/Trace를 묶고, current-reading과 caution이 함께 보이는 시나리오를 우선 기준으로 삼는다.`
