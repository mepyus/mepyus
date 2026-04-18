# compare candidate enrichment field-spec pre-note v1

## 1. verdict

이 문서는
`compare candidate enrichment proposal draft v1` 다음 단계로서의
**field-spec pre-note**다.

중요:
- 아직 field spec이 아니다
- field name을 정하지 않는다
- payload/adapter contract discussion으로도 가지 않는다

이번 pre-note의 역할은
proposal draft에서 잠근 `relation label/meta 수준의 작은 enrichment 후보`가
정확히 어떤 **정보층의 성격**을 뜻하는지,
필드 설계 직전 단계에서 더 명확히 적는 것이다.

## 2. pre-note purpose

왜 이 문서가 필요한가:

- proposal draft는 범위와 비범위를 잠갔다
- 하지만 `relation label/meta`라는 표현만으로는
  아직 무엇이 허용되는 정보층인지 충분히 선명하지 않다
- field spec으로 바로 가면
  문제 정의보다 설계가 앞서기 쉽다

즉 이 pre-note의 목적은
- 계약이나 구현을 열기 전에
- **candidate information layer의 성격을 더 정확히 좁히는 것**이다

## 3. candidate information layer

이번 트랙에서 말하는 `relation label/meta`는
아래 같은 성격의 정보층으로만 본다.

### relation hint

- candidate가 왜 붙는지에 대한
  짧고 조용한 관계 단서

### comparison context cue

- selected asset와 compare candidate 사이를
  아주 얇게 위치시키는 맥락 단서

### lightweight reason thickening

- 현재 거의 비어 있거나 너무 얇게 읽히는 compare reason을
  recommendation으로 가지 않으면서
  한 단계만 두껍게 만드는 정보층

중요:
- 이건 아직 field가 아니다
- 구조가 아니다
- UI 문구 세트도 아니다

즉 여기서 말하는 것은
`무슨 종류의 정보가 후보가 될 수 있는가`에 대한 성격 규정이다.

## 4. allowed vs disallowed information

### allowed information

허용되는 정보층은 아래까지다.

- compare candidate가 붙는 관계에 대한 작은 힌트
- selected asset와 candidate 사이를
  과장 없이 조금 더 읽게 하는 얇은 맥락 cue
- 현재 너무 flat하게 느껴지는 compare reason의
  최소 thickening

### disallowed information

아래 정보층은 이번 단계에서도 계속 허용되지 않는다.

#### ranking-like signal

- 우선순위
- 점수
- best-match 느낌

#### recommendation-like phrasing

- suggested
- recommended
- top related
- should compare

#### evidence payload

- why-chain
- source excerpt
- trace packet
- evidence drilldown 요소

#### workflow / action cue

- next step
- open compare flow
- operator action hint

#### UI-driving rich structure

- panel 확장을 전제로 한 richer compare block
- deep relationship tree
- compare cluster presentation

즉 허용되는 것은
작은 relation hint이고,
허용되지 않는 것은
recommendation, evidence, workflow, UI inflation이다.

## 5. thickness boundary

현재 thin relation에서
허용 가능한 enrichment 후보 두께는 아래까지다.

- compare candidate가 단순 `assetId/title fallback` 이상으로
  “왜 붙어 있는지”를 아주 얇게 읽게 해주는 정도
- relation을 더 잘 보이게 하지만
  compare candidate의 해석 권위를 올리지 않는 정도

어디부터 inflation인가:

- candidate 간 우선순위를 암시하기 시작할 때
- selected asset에 대해 “이 candidate를 보는 것이 더 맞다”는 식의 방향성을 띨 때
- compare 이유가 evidence-like payload나 workflow cue를 포함하기 시작할 때
- relation hint가 작은 cue가 아니라
  compare interpretation surface처럼 커질 때

즉:
- **한 단계 thicker한 hint까지는 후보**
- **의미를 안내하거나 유도하기 시작하면 이미 inflation**

## 6. why not contract yet

아직 adapter/payload contract discussion으로 가면 안 되는 이유는 아래다.

### 1. information layer의 성격이 먼저 잠겨야 한다

- 지금 바로 contract를 논의하면
  어떤 종류의 정보를 허용할지보다
  어떤 구조로 실을지가 먼저 논의된다

### 2. contract discussion은 쉽게 scope를 넓힌다

- 작은 relation hint를 말하려던 것이
  richer compare structure나 new payload branch 이야기로 번질 수 있다

### 3. field/contract는 proposal inflation을 가속한다

- 현재 단계에서 가장 큰 리스크는
  compare candidate enrichment가 recommendation/workflow 쪽으로 비대해지는 것이다
- contract 이야기는 그 비대화를 빠르게 정당화할 위험이 있다

## 7. next-step gate

판정:
- **contract discussion pre-note**

이유:
- information layer의 성격은 지금 단계에서 충분히 좁혀졌다
- 따라서 다음은 field spec 본안이 아니라,
  contract를 논의하더라도 어디까지를 논의 가능한지 먼저 자르는
  `contract discussion pre-note`가 맞다

## 8. codex alignment note

- 감독관의 “다음은 contract discussion이 아니라 field-spec pre-note다” 판단에 동의한다.
- proposal draft 다음 단계에서 가장 위험한 과잉 구체화는
  relation hint를 곧바로 field name, contract, UI behavior 전제로 번역해버리는 순간이다.
- resolution:
  - 이번 문서에서는 field나 schema를 쓰지 않고
  - information layer의 성격만 좁게 잠갔다.
