# compare candidate enrichment contract proposal readiness note v1

## 1. verdict

현재 `compare candidate enrichment`는
**contract proposal 초안 준비 가능** 단계로 본다.

중요:
- 이 문서는 contract proposal 본안이 아니다
- concrete contract shape를 적지 않는다
- field spec이나 implementation design으로 가지 않는다

이번 note의 역할은
compare model 중심 discussion surface가 이미 잠긴 상태에서,
실제 contract proposal 초안으로 들어갈 준비가 되었는지만 판정하는 것이다.

## 2. codex alignment note

- 감독관의 “이제는 contract proposal readiness note 단계다” 판단에 동의한다.
- discussion surface는 이미 compare model 중심으로 충분히 좁혀졌고, 지금은 그 위에서 proposal readiness만 확인하면 된다.
- compare model 중심 readiness를 볼 때 가장 큰 리스크는
  model-level thinness 논의를 곧바로 concrete field/spec로 번역해버리는 점이다.
- resolution:
  - 이번 note에서는 proposal readiness만 판단하고
  - contract shape, field, implementation discussion은 계속 열지 않는다.

## 3. readiness purpose

왜 이 readiness note가 필요한가:

- contract discussion pre-note에서
  contract 논의의 허용 범위를 잘랐다
- contract discussion memo에서
  primary surface를 `compare model`,
  secondary surface를 `payload shaping`으로 좁혔다

이제 남은 질문은 하나다.

- **이 상태로 concrete contract proposal 초안에 들어갈 준비가 되었는가?**

즉 이번 문서는
discussion surface 판정과 concrete proposal 사이의 마지막 readiness gate다.

## 4. readiness factor check

### 4-1. primary surface clarity

- status: `ready`

이유:
- current compare candidate thin relation의 주요 origin은
  `compare model`이라는 점이 충분히 잠겼다
- discussion surface memo에서도 이 판단이 명확히 정리됐다

### 4-2. secondary surface containment

- status: `ready`

이유:
- `payload shaping`은 보조 surface로만 읽히고 있다
- 현재까지 이 축이 primary처럼 커지거나
  contract 논의의 본체가 되는 방향으로 번지지 않았다

### 4-3. non-goal stability

- status: `ready`

이유:
- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation

이 비범위는 반복적으로 확인되었고,
contract readiness 단계까지도 흔들리지 않았다

### 4-4. minimal information layer stability

- status: `ready`

이유:
- field-spec pre-note에서
  `relation hint / comparison context cue / lightweight reason thickening`
  수준으로 information layer가 충분히 좁혀졌다
- richer structure는 여전히 범위 밖으로 유지된다

### 4-5. inflation control readiness

- status: `nearly ready`

이유:
- inflation risk 자체는 충분히 인식되어 있고
  entry constraints도 이미 보인다
- 다만 contract proposal 단계에서는
  discussion surface를 설계안으로 오해하는 속도가 빨라질 수 있어
  이 항목은 `ready`까지는 올리지 않는다

## 5. blocking risks

### 1. compare model discussion -> concrete field/spec inflation

- compare model 중심 논의를 시작하자마자
  “그럼 어떤 field가 필요하냐”로 급히 번질 위험

### 2. payload shaping drift

- 보조 surface인 `payload shaping`이
  contract proposal 단계에서 primary처럼 커질 위험

### 3. UI-led contract shaping

- compare panel의 현재 thinness를 보완하고 싶다는 UI need가
  contract shape를 선도하는 위험

## 6. readiness judgment

판정:
- **contract proposal 초안 준비 가능**

이유:
- primary/secondary discussion surface가 정리됐다
- non-goal과 minimal information layer도 충분히 안정적이다
- 남은 리스크는 proposal 진입을 막는 수준이 아니라
  proposal 초안 entry constraint로 통제해야 할 종류다

즉:
- 더 이상의 readiness note 반복보다
  이제는 contract proposal 초안 단계로 넘어가는 편이 맞다

## 7. entry constraints

다음 contract proposal 초안에 들어갈 때 반드시 유지해야 할 조건은 아래다.

### 1. compare model 중심 유지

- primary discussion surface는 계속 compare model이다

### 2. payload shaping은 보조로만 취급

- payload shaping이 contract proposal의 주체처럼 커지지 않게 한다

### 3. non-goals 유지

- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation

### 4. minimal information layer 유지

- relation hint / comparison context cue / lightweight reason thickening
  수준을 넘지 않는다

### 5. board grounding 분리

- board grounding 트랙은 이번 contract proposal과 합치지 않는다

### 6. UI inflation 금지

- compare panel을 더 큰 interpretive surface로 만드는 방향을 전제하지 않는다

## 8. board grounding separation

이번 readiness note에서도 board grounding은 compare contract 트랙과 합치지 않는다.

- board grounding absence는 여전히 existing signal reuse와 surface suppression 경계 문제에 가깝다
- compare candidate thin relation은 current compare model flatness와 더 직접적으로 연결된다
- 따라서 contract proposal readiness도 compare candidate 트랙 안에서만 유지하는 편이 맞다
