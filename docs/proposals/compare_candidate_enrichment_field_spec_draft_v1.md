# compare candidate enrichment field-spec draft v1

## 1. verdict

이 문서는 `compare candidate enrichment`에 대한
**field-spec draft v1** 이다.

중요:
- concrete schema 변경안이 아니다
- implementation design이 아니다
- UI behavior spec이 아니다

이번 draft의 목적은
compare model 중심 / payload shaping 보조라는 전제 아래,
어떤 **종류의 field layer**가 최소한으로 필요할 수 있는지
아주 좁게 적는 것이다.

## 2. draft purpose

이 draft가 다루는 문제는 아래다.

- current compare candidate surface는
  candidate 존재는 말하지만 relation thickness는 충분히 못 준다
- 따라서 compare model이 relation hint를 설명 가능한 층으로 가질 수 있는지
  field layer 수준에서 아주 얇게 옮겨볼 필요가 있다

즉 이 draft는
field를 많이 만드는 것이 아니라,
**relation hint를 담는 최소 층이 어떤 종류여야 하는가**
를 적는 데 목적이 있다.

## 3. field layer outline

### layer 1. relation cue core

역할:
- compare candidate가 selected asset와 왜 연결되는지에 대한
  가장 작은 관계 단서 층

성격:
- flat reason only보다는 한 단계 두껍다
- 하지만 recommendation처럼 방향성을 주지 않는다

### layer 2. comparison context qualifier

역할:
- relation cue를 과장 없이 조금 더 읽게 해주는
  얇은 맥락 층

성격:
- context를 주지만
  evidence나 workflow로 넘어가지는 않는다

### layer 3. low-claim fallback / absence layer

역할:
- compare candidate relation이 얇거나 부재할 때
  과장된 의미를 만들지 않게 하는 low-claim 층

성격:
- “없음”이나 “얇음” 자체도
  recommendation이 아닌 상태로 유지시킨다

## 4. field layer qualities

이번 draft에서 허용하는 qualities:

- small
- relation-thickening only
- non-recommendation
- non-evidence-bearing
- low-claim

즉 field layer는
candidate를 richer relation surface로 키우는 것이 아니라,
current thinness를 아주 조금만 완화하는 방향이어야 한다.

## 5. compare model vs payload shaping rule

### compare model 중심

- field layer의 origin은 compare model 쪽에 있어야 한다
- relation hint의 종류와 성격을 먼저 정의하는 주체는 compare model이다

### payload shaping 보조

- payload shaping은
  compare model에서 형성된 relation thickness가
  flatten되지 않도록 전달하는 보조 역할만 맡는다

### adapter mediation 비중심

- adapter는 field layer origin이 아니다
- 이번 draft에서도 adapter는 mediation layer로만 본다

## 6. disallowed in this draft

이번 draft에서도 계속 금지되는 것은 아래다.

- ranking-like signal
- recommendation-like phrasing
- evidence-bearing layer
- workflow/action-driving layer
- UI-structuring layer

이유:
- 이 성질이 들어오는 순간
  field layer는 relation hint가 아니라
  새로운 compare interpretation surface가 된다

## 7. boundary

이 draft가 다루는 것:

- 어떤 종류의 field layer가 필요한지
- 각 layer가 담아야 하는 정보의 성격
- compare model 중심 / payload shaping 보조 원칙

이 draft가 다루지 않는 것:

- concrete field names
- schema shape
- payload branch 설계
- implementation logic
- UI consumer behavior

경계:

- **layer 성격까지가 이 draft**
- **구체 키와 구조를 정하기 시작하면 다음 단계**다

## 8. one-line lock

- compare candidate enrichment field-spec draft v1은
  compare model 중심에서 `small, low-claim, non-recommendation` relation hint layer를 상정하는
  가장 좁은 field-spec entry 문서다.
