# compare candidate enrichment contract proposal draft v1

## 1. verdict

이 문서는 `compare candidate enrichment`에 대한
**contract proposal 초안**이다.

중요:
- 아직 concrete contract shape를 적지 않는다
- field name을 정하지 않는다
- schema 변경안을 쓰지 않는다
- implementation design이나 UI behavior change로도 가지 않는다

이번 draft의 목적은
compare candidate thin relation을
`compare model` 중심 / `payload shaping` 보조라는 전제 아래
**어떤 contract discussion 범위로 올릴 수 있는지**를 잠그는 데 있다.

## 2. codex alignment note

- 감독관의 “이제는 contract proposal draft v1 단계다” 판단에 동의한다.
- readiness note까지 왔기 때문에, 이제는 compare model 중심 contract proposal 초안을 세울 수 있다.
- 이 단계에서 가장 위험한 inflation 지점은
  compare model origin reading을 곧바로 concrete field/schema 설계로 번역하면서
  payload shaping과 UI 소비 요구까지 한 번에 끌어들이는 순간이다.
- resolution:
  - 이번 draft에서는 compare model 중심성과 보조 surface 원칙만 잠그고
  - 구체 필드, 스키마, 구현은 계속 열지 않는다.

## 3. proposal purpose

이 contract proposal 초안이 다루려는 핵심 문제는 아래다.

- current compare model flatness 때문에
  compare candidate relation thickness가 충분히 전달되지 않는다
- 그 결과 current compare panel은
  candidate 존재는 말하지만
  relation hint는 충분히 두껍게 말하지 못한다

이 문제는:
- UI 확장 문제라기보다
- **compare model이 relation thickness를 어떻게 설명 가능한 층으로 담을 수 있는가**
  의 문제에 더 가깝다

즉 이 초안의 목적은
- compare candidate enrichment를 recommendation surface로 키우는 것이 아니라
- compare model 중심에서 relation hint를 더 잘 설명 가능한 contract discussion 대상으로
  올릴 수 있는지 잠그는 것이다

## 4. proposal scope

이 proposal 초안이 다루는 최소 범위는 아래와 같다.

### compare model 중심

- compare candidate thin relation의 주요 origin을
  compare model flatness로 본다
- 따라서 contract discussion의 중심도 compare model이다

### payload shaping은 보조 surface

- compare model에서 생성되는 relation thickness가
  payload로 나올 때 얼마나 눌리거나 평평해지는지 보는 보조 축까지만 둔다
- payload shaping이 proposal의 주체가 되지 않게 한다

### adapter mediation은 중심 범위 밖

- adapter는 current thinness를 전달하는 mediation layer지만
  origin surface는 아니다
- 따라서 이번 proposal 중심 범위에는 넣지 않는다

## 5. proposal non-goals

아래 항목은 이 proposal에서도 계속 비범위다.

- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation
- board grounding merge

왜 여전히 비범위인가:

- 이 항목들이 proposal 안으로 들어오는 순간
  compare candidate enrichment는
  작은 relation hint contract discussion이 아니라
  추천/행동/확장 surface proposal로 바뀐다

즉 non-goals는 여전히
proposal identity를 지키는 핵심 경계다.

## 6. contract proposal boundary

이 초안 안에서 다루는 것:

- compare model 중심 origin reading
- minimal information layer를 contract discussion 대상으로 올릴 수 있는지 여부
- payload shaping을 secondary surface로만 다루는 원칙

이 초안 밖에 두는 것:

- concrete field names
- schema change
- payload contract rewrite
- implementation design
- UI consumer behavior design

경계 규정:

- **origin과 discussion scope를 잠그는 것까지가 이 draft**
- **구체 형식과 소비 행위를 정하기 시작하면 다음 단계**다

## 7. rationale

지금 contract proposal 초안 단계로 올릴 수 있는 이유는 아래와 같다.

1. natural live observation에서 compare candidate thin relation이 반복적으로 관찰됐다
2. counter-read 이후에도 baseline restraint보다 future candidate 해석이 더 우세했다
3. discussion surface memo에서
   `compare model`이 primary,
   `payload shaping`이 secondary라는 점이 잠겼다
4. contract proposal readiness note에서
   proposal entry constraints가 충분히 정리됐다

즉:
- 지금은 아직 구체 설계 단계는 아니지만
- contract proposal 초안을 세울 만큼 중심축과 경계는 충분히 확보됐다

## 8. risks and controls

### risk 1. compare model -> concrete field inflation

위험:
- compare model 중심 논의가
  곧바로 field name/spec/schema 이야기로 번질 수 있다

통제:
- 이번 초안에서는
  compare model을 origin surface로만 다루고
  구체 형식은 다음 단계로 넘긴다

### risk 2. payload shaping centralization

위험:
- 보조 surface인 payload shaping이
  proposal의 주체처럼 커질 수 있다

통제:
- payload shaping은 secondary supporting surface로만 명시한다
- proposal scope에서 compare model 중심성을 반복 고정한다

### risk 3. UI-need-led contract risk

위험:
- 현재 compare panel의 얇음을 보완하고 싶다는 UI need가
  contract shape를 선도할 수 있다

통제:
- UI behavior design은 이 초안의 범위 밖으로 둔다
- relation hint 문제를 UI 소비 문제가 아니라
  compare model origin 문제로 먼저 읽는다

## 9. next-step gate

이 contract proposal draft 다음 단계는
바로 implementation이 아니다.

다음 가능한 단계:

- `contract shape memo`
- 또는 `field spec draft`

현재 판단:
- 먼저 `contract shape memo`가 더 적절하다

이유:
- 아직 concrete field spec보다
  contract shape를 어떤 추상 단위에서 논의할지 한 번 더 자르는 편이 안전하다

## 10. board grounding separation

board grounding은 이번 contract proposal draft에서도 계속 별도 트랙으로 둔다.

- board grounding absence는 existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- compare candidate thin relation은 compare model flatness와 더 직접적으로 연결된다
- 따라서 이번 proposal 초안도 compare candidate 트랙만 다루는 편이 맞다
