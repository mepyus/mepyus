# compare candidate enrichment proposal draft v1

## 1. verdict

이 문서는 `compare candidate enrichment`를
future engine-side proposal 초안 수준으로 정리한 것이다.

중요:
- 아직 field spec이 아니다
- contract change proposal이 아니다
- implementation design도 아니다

이번 draft의 목적은
proposal의 **문제 정의 / 범위 / 비범위 / entry constraint**를
더 이상 흔들리지 않게 잠그는 데 있다.

## 2. proposal purpose

이 proposal이 다루려는 핵심 문제는 아래다.

- current compare panel은
  compare candidate가 존재한다는 사실은 말한다
- 하지만 `assetId/title fallback + 얇은 reason` 수준이라
  relation thickness를 충분히 주지 못한다

이 문제의 성격은:
- UI를 더 크게 만드는 문제라기보다
- **current compare model richness가 얇은 문제**에 더 가깝다

즉 proposal purpose는
- compare candidate를 recommendation surface로 키우는 것이 아니라
- selected asset 옆의 read-only comparison aid가
  최소한의 relation hint를 조금 더 읽게 할 수 있는지
  engine-side 후보 관점에서 검토하는 것이다

## 3. proposal scope

이 proposal이 다루는 최소 범위는 아래까지다.

- `relation label/meta 수준의 작은 engine-side enrichment 후보`

더 구체적으로는:
- compare candidate가 왜 붙어 있는지에 대한
  아주 작은 relation hint
- selected asset와 candidate 사이의 관계를
  recommendation처럼 밀지 않는 최소 context

이 scope는 의도적으로 작다.

- richer compare structure를 전제하지 않는다
- panel expansion을 전제하지 않는다
- ranking/recommendation 방향으로 나아가지 않는다

## 4. non-goals

아래 항목은 이 proposal의 비범위다.

- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation

왜 비범위인가:

- 이 다섯 가지 중 하나라도 proposal 안으로 들어오면
  compare candidate enrichment는
  작은 relation hint proposal이 아니라
  새로운 비교/추천 surface proposal로 바뀌게 된다

즉 non-goals는
proposal의 안전장치가 아니라
proposal identity 자체를 지키는 핵심 경계다.

## 5. proposal boundary

이 proposal 범위 안에 있는 것:

- compare candidate thin relation 문제를
  future engine-side candidate로 다룰 수 있는지
- 어디까지를 minimal enrichment 후보로 볼지
- 왜 current compare model flatness가 주요 origin으로 읽히는지
- proposal 단계에서 반드시 유지해야 할 제한은 무엇인지

이 proposal 범위 밖에 있는 것:

- field spec
- adapter/payload contract 변경안
- implementation design
- component/UI behavior change
- route/query/state axis/vocabulary 변경

경계 규정:

- **문제 정의와 후보 범위까지가 이 draft**
- **필드, 계약, 구현을 말하기 시작하면 다음 단계**다

## 6. rationale

지금 proposal 초안 단계로 올릴 수 있는 이유는 아래와 같다.

1. natural live observation과 watchpoint observation에서
   compare candidate thin relation이 반복적으로 관찰됐다

2. engine-origin mapping은
   이 얇음이 UI polish보다 current compare model flatness와 더 강하게 연결된다고 봤다

3. counter-read에서도
   baseline restraint 설명은 가능했지만
   future engine-side candidate 해석이 더 우세했다

4. readiness memo에서는
   candidate validity, non-goal stability, minimal envelope clarity가
   proposal 초안 준비 가능 수준으로 잠겼다

즉:
- 지금은 proposal 본안까진 아니지만
- proposal draft를 세워도 될 만큼 candidate legitimacy는 충분히 확보됐다

## 7. risks and controls

### risk 1. inflation risk

위험:
- relation hint를 말하는 순간
  proposal이 richer compare structure로 비대해질 수 있다

통제:
- minimal envelope를 계속 `relation label/meta 수준`으로 고정한다
- richer structure는 proposal boundary 밖으로 둔다

### risk 2. recommendation-like misread risk

위험:
- compare candidate enrichment가 추천면처럼 읽힐 수 있다

통제:
- ranking, recommendation wording, workflow affordance를 계속 non-goal로 둔다
- read-only comparison aid라는 정체성을 반복해서 고정한다

### risk 3. evidence thinness risk

위험:
- 현재 근거가 아직 too-thin 해석에 머물 수 있다

통제:
- proposal 본안 전에
  field-spec pre-note 또는 contract discussion pre-note 같은
  더 좁은 준비 단계를 두어 과잉 해석을 막는다

## 8. separation note

### why board grounding stays separate

- board grounding absence는 중요한 watchpoint이지만
  existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- compare candidate thin relation은
  current compare model flatness와 더 직접적으로 연결된다
- 따라서 이번 proposal은 compare candidate 트랙에만 집중한다

### why adapter/payload contract discussion stays restrained

- proposal draft 단계에서 contract discussion까지 열면
  문제 정의와 후보 범위보다 구현 방향이 앞서게 된다
- 지금 필요한 것은 “무엇을 논의할 수 있는가”의 경계이지
  “어떻게 바꿀 것인가”의 설계가 아니다

## 9. next-step gate

이 proposal draft 다음에 바로 구현으로 가면 안 된다.

다음 가능한 단계는 아래 같은 준비 단계다.

- `field-spec pre-note`
- `contract discussion pre-note`

즉 proposal draft 이후에도
한 번 더 좁은 준비 단계가 필요하다.

한 줄로:
- 다음은 implementation이 아니라,
  **proposal 안에서 실제로 무엇을 필드/계약 수준으로 논의할 수 있는지 더 좁게 자르는 준비 메모**다.

## 10. codex alignment note

- 감독관의 “이제는 readiness memo가 아니라 proposal draft v1 단계다” 판단에 동의한다.
- 지금은 candidate legitimacy와 readiness가 충분히 쌓여서 proposal 초안으로는 올라갈 수 있다.
- 다만 가장 위험한 inflation 지점은 compare candidate enrichment가 recommendation/workflow 성격으로 읽히기 시작하는 순간이다.
- resolution:
  - 이번 draft에서는 purpose, scope, non-goals, boundary만 잠그고
  - field spec, contract change, implementation discussion은 계속 열지 않았다.
