# compare candidate enrichment candidate boundary hardening v2

## 1. verdict

현재 `compare candidate enrichment`는
여전히 **proposal 이전 단계의 candidate**로만 다루는 것이 맞다.

이번 hardening의 목적은
무엇을 enrich 하려는지보다
**무엇은 절대 하지 않을지**와
**최소 어디까지를 후보로 볼지**를 더 분명히 잠그는 것이다.

## 2. hardened non-goals

아래 항목은 이번 candidate 범위 밖으로 다시 명시적으로 잠근다.

### ranking

- compare candidate에 우선순위, 점수, best-match 느낌을 붙이는 순간
  panel이 reading aid를 넘어 recommendation surface처럼 읽힐 수 있다
- 따라서 ranking은 candidate 범위 밖이다

### recommendation wording

- `best`, `suggested`, `recommended`, `top related` 같은 언어는
  compare candidate의 의미를 즉시 바꾼다
- current candidate의 목적은 추천이 아니라
  **얇은 relation hint**다

### evidence drilldown

- compare candidate를 눌러 근거를 추적하거나
  why-chain을 펼치는 순간
  panel이 read-only 보조층이 아니라 drilldown surface가 된다
- 이는 현재 candidate 범위를 넘는다

### workflow / action affordance

- compare candidate를 action trigger, next-step CTA, workflow 진입점으로 쓰는 것은
  현재 주제와 무관하다
- compare candidate는 운영 행동이 아니라
  selected asset 주변 읽기 보조층이어야 한다

### UI inflation 전제

- “UI를 더 크게 만들기 위해” compare candidate를 enrich 하는 건
  현재 candidate의 목적이 아니다
- current question은 panel 확장이 아니라
  **relation thinness 자체를 최소 수준에서 어떻게 이해할지**다

## 3. minimum candidate envelope

future candidate로 볼 수 있는 최소 envelope는 아래까지다.

- compare candidate를 읽을 때
  `assetId/title fallback` 외에 붙을 수 있는
  **아주 작은 relation label/meta 수준의 enrichment 가능성**

이 최소 envelope는 다음 성격까지만 허용한다.

- candidate가 왜 붙어 있는지에 대한
  얇고 조용한 단서
- selected asset와 candidate 사이를
  recommendation처럼 밀지 않는 최소 context

중요:
- 이 envelope는 field 설계가 아니다
- payload contract 확장안도 아니다
- panel redesign 범위도 아니다

경계:
- **이 정도까지가 candidate**
- 이 이상으로
  - richer structure
  - ranking nuance
  - deeper relation explanation
  를 말하기 시작하면
  그건 proposal 단계다

## 4. possible origin layers

이 최소 후보가 나중에 어디서 올 수 있는지는
추상 수준에서만 아래처럼 본다.

### compare model

- 가장 직접적인 origin 후보
- current compare candidate relation thinness는
  compare model flatness와 가장 강하게 연결된다

### payload shaping

- compare model이 있더라도
  payload surface에서 얼마나 압축되어 나오는지에 따라
  relation thinness가 달라질 수 있다

### adapter mediation

- adapter는 first pass에서 untouched를 유지했기 때문에
  current thinness를 거의 그대로 전달한다
- future에도 adapter는 mediation layer일 뿐,
  enrichment의 본 origin이 되어선 안 된다

## 5. why not proposal yet

지금 proposal로 가면 이른 이유는 아래 셋으로 충분하다.

1. natural live observation이 아직 길게 누적된 것은 아니다
2. current compare meaning의 얇음이 실제 friction인지, baseline restraint인지 경계가 더 굳어져야 한다
3. non-goal과 minimal goal 경계가 지금처럼 더 단단히 잠겨 있어야
   proposal이 recommendation/workflow 쪽으로 비대해지지 않는다

## 6. board grounding separation reaffirmed

이번 문서에서도 board grounding을 주제로 올리지 않는 이유는 명확하다.

- board grounding absence는 중요한 watchpoint지만
  existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- 반면 compare candidate thin relation은
  current compare model flatness 자체와 더 직접적으로 연결된다
- 따라서 이번 hardening note는 compare candidate 후보의 범위를 좁히는 데만 집중한다

## 7. recommendation

판정:
- **proposal precondition note 1회 더**

이유:
- 지금은 candidate 경계가 많이 좁혀졌지만,
  바로 proposal 초안으로 가기보다는
  proposal 전에 확인해야 할 precondition을 한 번 더 적는 편이 안전하다

한 줄로:
- compare candidate enrichment는 아직 proposal이 아니라,
  **relation hint 수준을 넘지 않는 최소 후보**로만 더 단단히 잠가야 한다.
