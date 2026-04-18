# engine-side compare candidate enrichment candidate note v1

## 1. verdict

`compare candidate thin relation`은
현재 시점에서 **future proposal 이전 단계의 engine-side candidate**로 정리할 가치가 있다.

다만 아직은 proposal로 승격할 단계가 아니다.
이번 문서는
- 무엇이 얇고
- 왜 얇고
- 어디까지를 최소 candidate 범위로 볼 수 있는지
를 좁히는 note다.

## 2. candidate definition

대상:
- `compare candidate thin relation`

현재 증상:

- compare panel이 `assetId/title fallback` 중심으로 읽힌다
- `reason`도 자연 live path에서는 거의 보조 힌트 수준에 머문다
- 그 결과 compare panel은
  “candidate가 있다”는 사실은 말하지만
  “왜 이 candidate인가”를 충분히 두껍게 말하지 못한다

의미:
- 현재 compare panel은 의도대로 recommendation surface로 커지지는 않지만
- 동시에 `comparison aid`로서의 relation thickness도 제한적이다

즉 candidate의 핵심은:
- **UI panel 확장 문제**라기보다
- **current compare candidate model이 전달하는 relation richness가 얇은 문제**에 가깝다

## 3. likely origin summary

### current compare model flatness

가장 유력한 origin은 여기다.

- process-console 쪽 compare surface가
  현재 `related_assets` 중심의 flat model로 읽힌다
- adapter untouched first pass도 이를 그대로
  `assetId + reason` 수준으로 넘긴다

즉 얇음의 중심은
UI rendering보다 **current compare model 자체의 flatness**에 있다.

### payload richness 부족 여부

- payload에는 compare candidate가 존재한다
- 하지만 candidate를 둘러싼 relation label/meta가 두껍지 않다

즉 “payload가 아예 없다”가 아니라
**payload richness가 hint-level에 머문다** 쪽이 더 정확하다.

### adapter untouched first pass의 한계

- adapter는 first pass에서 의도적으로 untouched를 유지했다
- 이건 baseline 보호 측면에선 맞았지만,
  compare relation thickness를 살리는 데는 한계가 있었다

따라서 current limitation은
- adapter bug가 아니라
- first-pass untouched 원칙이 허용한 thinness로 보는 게 맞다

## 4. candidate boundary

### 아직 하지 말아야 할 것

- ranking
- recommendation wording
- score/priority
- evidence drilldown
- workflow affordance
- compare panel을 새 해석면처럼 키우는 확장
- UI 확장을 전제로 한 candidate inflation

### 최소 candidate 범위

future candidate로 생각할 수 있는 최소 범위는 여기까지다.

- compare candidate를 읽을 때
  `assetId` 외에 붙일 수 있는
  **relation label/meta 수준의 enrichment 가능성**

중요:
- 이건 구현안이 아니다
- panel을 더 크게 만들자는 뜻도 아니다
- recommendation으로 가는 richer compare engine을 제안하는 것도 아니다

즉 현재 note에서 허용하는 범위는:
- **candidate relation을 조금 더 읽히게 하는 최소 engine-side label/meta richness 후보**
까지다.

## 5. minimal future value

이 후보가 살아나면 기대할 수 있는 최소 가치는 아래다.

- compare panel이 여전히 read-only comparison aid로 남으면서도
- 단순 `assetId list`보다 조금 더 관계를 읽게 될 수 있다
- 즉 “candidate가 있다”에서
  “이 candidate는 이런 relation 힌트로 붙어 있다” 정도로
  한 단계만 더 두꺼워질 가능성이 있다

하지만 왜 지금 당장 proposal로 가면 안 되는가:

- 아직 natural live observation이 충분히 길게 쌓인 것은 아니다
- 현재 thinness가 실제 운용 friction으로 얼마나 반복되는지
  더 관찰할 여지가 남아 있다
- candidate를 너무 빨리 proposal로 승격하면
  recommendation/workflow 쪽으로 의미가 불어날 위험이 있다

즉:
- minimal future value는 분명 있지만
- 지금은 그 가치를 구현안으로 풀기보다
  candidate 범위만 좁게 잠그는 편이 더 안전하다

## 6. board grounding separation note

이번 턴에서 compare 쪽만 1차 후보로 다루고,
board grounding absence는 보조 watch로 남기는 이유는 아래와 같다.

- board grounding absence는
  existing engine signal reuse 문제에 더 가깝다
- 반면 compare candidate thin relation은
  current compare model flatness 자체와 더 직접적으로 연결된다
- 즉 이번 턴의 목적이 “engine-side 후보를 하나 좁히는 것”이라면
  compare 쪽이 더 직접적이고 응집된 후보가 된다

board grounding은 여전히 중요하지만,
지금 함께 끌어오면 candidate note의 초점이 흐려진다.

## 7. recommendation

판정:
- **compare candidate enrichment proposal 초안으로 바로 가기엔 아직 이르다**
- **candidate note를 한 단계 더 쌓는 쪽이 맞다**

이유:
- 현재는 origin mapping과 thinness 정의는 충분히 됐지만
- proposal로 들어가기 전,
  candidate 범위와 non-goal을 한 번 더 보수적으로 잠글 여지가 있다

즉 다음 단계가 있다면
- 구현 proposal이 아니라
- `minimal compare relation enrichment boundary note`
같은 더 좁은 candidate 정리가 먼저 맞다

## 8. codex alignment note

- 감독관의 “compare candidate thin relation을 engine-side 1차 후보로 좁힌다”는 판단에 대체로 동의한다.
- board grounding absence를 이번 턴에서 보조 후보로만 남기는 것도 적절하다.
- 남는 리스크는 grounding 쪽이 later-stage에서 다시 커질 수 있다는 점이지만,
  지금 함께 다루면 compare candidate note의 초점이 흐려진다.
- resolution:
  - 이번 note는 compare thin relation만 1차 candidate로 좁히고
  - board grounding은 watchpoint로 계속 분리 유지한다.
