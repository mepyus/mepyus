# compare candidate enrichment proposal readiness memo v1

## 1. verdict

`compare candidate enrichment`는
이제 **proposal 초안 준비 가능** 단계로 본다.

중요:
- 이 판단은 proposal 본안을 지금 작성한다는 뜻이 아니다
- field spec, contract change, 구현안은 여전히 열지 않는다
- 이번 memo는 proposal 본안에 들어갈 준비가 되었는지만 판정한다

## 2. readiness question

핵심 질문:

- **compare candidate enrichment는 이제 proposal 초안으로 들어갈 준비가 되었는가?**

이번 memo는 그 질문을
candidate validity, 경계 안정성, 관찰 충분성, inflation risk 기준으로 판단한다.

## 3. readiness factor check

### 3-1. candidate validity

- status: `ready`

이유:
- counter-read 이후에도
  compare candidate thin relation은 단순 baseline restraint로만 환원되지 않았다
- natural live observation과 engine-origin mapping을 함께 읽으면
  current compare model flatness와 연결된 future engine-side candidate 해석이 더 우세하다

### 3-2. non-goal boundary stability

- status: `ready`

이유:
- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation

이 비범위가 반복적으로 재확인되었고,
candidate hardening 단계에서도 흔들리지 않았다.

### 3-3. minimal candidate envelope clarity

- status: `ready`

이유:
- current candidate는
  `relation label/meta 수준의 최소 enrichment 가능성`
  으로 충분히 좁혀졌다
- richer structure나 proposal-level field discussion은 아직 의도적으로 열지 않았다

### 3-4. natural observation sufficiency

- status: `nearly ready`

이유:
- natural live observation v1
- watchpoint observation v2
- counter-read
까지 누적되어, 단발 관찰 수준은 넘었다
- 다만 장기적/다회차 운용 증거라고 보긴 아직 이르다

### 3-5. risk of inflation into recommendation/workflow surface

- status: `nearly ready`

이유:
- 현재까지는 non-goal 경계가 잘 유지됐다
- 하지만 proposal 본안으로 들어가는 순간
  compare candidate 의미가 쉽게 inflation될 수 있으므로
  readiness는 충분하되 완전히 안심할 단계는 아니다

## 4. blocking risks

아직 proposal 본안 진입을 막거나 강하게 제한해야 하는 리스크는 아래 셋이다.

### 1. candidate envelope inflation risk

- proposal 단계에서 relation hint를 넘어서
  richer compare explanation이나 recommendation-like framing으로 불어날 위험

### 2. recommendation-like surface misread risk

- compare candidate enrichment가
  selected asset reading aid가 아니라
  추천면/우선순위면처럼 읽히기 시작할 위험

### 3. evidence still reads thin risk

- 현재 증거가 future candidate 쪽으로 기울긴 했지만,
  natural live 관찰의 두께 자체는 아직 아주 깊지 않다

## 5. readiness judgment

판정:
- **proposal 초안 준비 가능**

이유:
- candidate validity는 충분히 확인됐다
- non-goal boundary와 minimal envelope도 충분히 잠겼다
- 남은 리스크는 proposal 불가 사유라기보다
  proposal entry constraint로 관리해야 할 종류다

즉:
- 더 이상 precondition/counter-read 단계에 머물 필요는 없고
- 다음 단계는 proposal 초안 준비로 넘어갈 수 있다

## 6. entry constraints

proposal 본안에 들어갈 때 반드시 유지해야 할 entry constraints는 아래다.

### 1. non-goals 유지

- ranking 금지
- recommendation wording 금지
- evidence drilldown 금지
- workflow/action affordance 금지

### 2. minimal envelope 유지

- compare candidate enrichment는
  relation label/meta 수준의 최소 후보로만 다룬다
- richer compare structure를 당연한 전제로 두지 않는다

### 3. board grounding과 분리

- board grounding absence는 별도 watchpoint로 유지한다
- compare candidate 트랙과 합치지 않는다

### 4. UI inflation 금지

- proposal 본안은 UI 확장안을 전제로 하지 않는다
- selected asset reading aid의 얇은 성격을 계속 유지해야 한다

### 5. adapter/payload contract discussion 절제

- proposal readiness가 곧바로 contract 변경안을 정당화하지 않는다
- proposal 본안도 first pass에서는 candidate 범위와 origin 후보에 집중해야 한다

## 7. recommendation

다음 단계 추천:
- **compare candidate enrichment proposal 초안**

단,
- 이번 memo에서 잠근 entry constraints를 선행 조건으로 붙인 상태에서만
  proposal 본안으로 넘어가는 것이 맞다

## 8. codex alignment note

- 감독관의 “candidate validity는 충분하고, 다음은 readiness memo다” 판단에 대체로 동의한다.
- counter-read 이후에는 더 이상 같은 precondition 반복보다 readiness 판정으로 넘어가는 편이 맞다.
- 다만 가장 주의해야 할 리스크는 proposal 단계에서 minimal candidate envelope가 inflation되는 점이다.
- resolution:
  - 이번 memo에서는 proposal 진입 가능 판정을 내리되
  - non-goal, minimal envelope, board grounding separation을 entry constraint로 다시 잠갔다.
