# compare candidate enrichment proposal precondition note v1

## 1. verdict

`compare candidate enrichment`는
아직 proposal 본안으로 넘어가기보다,
그 전에 충족되어야 할 **precondition**을 명시적으로 잠그는 단계가 맞다.

이번 문서의 목적은
구현안이나 field spec을 적는 것이 아니라,
proposal이 recommendation/workflow 쪽으로 비대해지지 않도록
진입 조건을 먼저 좁히는 것이다.

## 2. proposal preconditions

### precondition 1. natural live observation이 한 번 더 누적될 것

의미:
- current compare candidate thinness가
  특정 asset/cohort에 국한된 현상인지,
  current compare model 전체의 패턴인지
  조금 더 안정적으로 볼 필요가 있다

### precondition 2. current thinness가 baseline restraint를 넘는 future candidate로 더 안정적으로 읽힐 것

의미:
- 지금의 얇음이 단순한 baseline 절제인지,
  실제로 future engine-side candidate로 볼 만한 반복 friction인지
  판단이 더 고정돼야 한다

### precondition 3. non-goal과 minimal goal 경계가 계속 유지될 것

의미:
- compare candidate enrichment를 말하는 순간
  ranking/recommendation/workflow 쪽으로 의미가 불어나지 않도록
  현재 경계가 충분히 단단하게 유지돼야 한다

### precondition 4. compare panel이 여전히 read-only comparison aid로 읽힐 것

의미:
- enrichment 후보를 논의하더라도
  compare panel이 새로운 해석면이나 추천면으로 읽히기 시작하면
  proposal 진입은 보류하는 편이 맞다

## 3. readiness check

### precondition 1. natural live observation이 한 번 더 누적될 것

- status: `partially met`

이유:
- natural live observation v1, v2는 있다
- 하지만 compare thin relation이 장기적으로 반복 friction인지 보기엔
  아직 누적 횟수가 많다고 보긴 어렵다

### precondition 2. current thinness가 future candidate로 더 안정적으로 읽힐 것

- status: `partially met`

이유:
- engine-origin mapping과 candidate note까지는 정리됐다
- 다만 아직 “proposal로 가야 할 만큼 충분히 반복된다”는 정도로는 잠기지 않았다

### precondition 3. non-goal과 minimal goal 경계가 계속 유지될 것

- status: `met`

이유:
- boundary hardening v2에서
  non-goal과 minimum candidate envelope가 명시적으로 잠겼다

### precondition 4. compare panel이 여전히 read-only comparison aid로 읽힐 것

- status: `met`

이유:
- 현재 placement, wording, behavior 모두
  recommendation/workflow surface로 번지지 않게 유지되고 있다

## 4. proposal entry rule

proposal 초안으로 넘어갈 수 있는 상태:

- 위 precondition 중
  - `non-goal / minimal goal` 경계가 유지된 채
  - natural live observation이 한 번 더 누적되고
  - compare thin relation이 여전히 engine-side candidate로 읽히는 경우

아직 candidate/precondition 단계에 머물러야 하는 상태:

- thinness가 다시 baseline restraint로 읽히거나
- compare panel이 recommendation/workflow 쪽으로 오해될 소지가 커지거나
- observation 없이 곧바로 richer relation 논의로 넘어가려는 경우

## 5. non-goal retention

proposal 전제 단계에서도 아래 비범위는 계속 유지해야 한다.

- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation

왜 계속 중요한가:
- proposal 전제 단계에서 이 경계가 느슨해지면
  compare candidate enrichment가
  “작은 relation hint”가 아니라
  “새로운 비교/추천 surface”로 읽히기 시작한다
- 따라서 non-goal retention은
  proposal 전제 단계에서도 핵심 보호 장치다

## 6. board grounding separation

board grounding은 여전히 이번 트랙의 주제가 아니다.

- board grounding absence는 중요한 watchpoint이지만
  existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- compare candidate thin relation은
  current compare model flatness와 더 직접적으로 연결된다
- 따라서 proposal precondition도 compare candidate 트랙에만 한정하는 편이 맞다

## 7. recommendation

판정:
- **proposal precondition note v2**

이유:
- 현재 상태는 proposal로 바로 갈 정도로 충분히 안정됐다고 보기보단,
  proposal 진입 조건을 한 번 더 observation 축과 연결해 확인하는 편이 더 안전하다

한 줄로:
- compare candidate enrichment는 지금도 candidate 단계이며,
  proposal로 올라가기 전 **observation 누적과 경계 유지가 한 번 더 확인되어야 한다**.

## 8. codex alignment note

- 감독관의 “다음은 proposal이 아니라 precondition note” 판단에 동의한다.
- 지금은 구현안보다 proposal 진입 조건을 먼저 잠그는 편이 맞다.
- 아직 더 굳혀야 할 전제는
  natural live observation 누적과 future candidate 판단 안정성이다.
- 남는 리스크는 observation이 충분히 쌓이기 전에 proposal로 점프하면
  compare candidate가 recommendation 쪽으로 비대해질 수 있다는 점이다.
- resolution:
  - 이번 문서에서는 proposal 진입 조건만 좁게 잠그고
  - field spec이나 contract discussion은 계속 열지 않았다.
