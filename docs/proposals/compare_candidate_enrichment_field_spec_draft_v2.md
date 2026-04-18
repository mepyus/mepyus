# compare candidate enrichment field-spec draft v2

## 1. verdict

이 문서는 `compare candidate enrichment`에 대한
**field-spec draft v2** 이다.

v1 대비 변화:
- field-like layer outline을 더 추상적인 information-band 수준으로 낮췄다
- compare model 중심 / payload shaping 보조 / non-goal 유지 원칙은 유지한다

중요:
- 아직 concrete field spec이 아니다
- schema 변경안이 아니다
- implementation design이 아니다

## 2. draft purpose

이 draft의 목적은
compare candidate thin relation을 완화하기 위해
어떤 **정보 두께의 band**가 최소한으로 필요할 수 있는지 적는 것이다.

즉 이 문서는
구조를 고정하려는 문서가 아니라,
`small, low-claim relation hint`를
어느 정도 성격까지 허용할 수 있는지 적는 문서다.

## 3. information-band outline

### relation-hint band

의미:
- compare candidate가 왜 붙는지에 대한
  가장 작은 관계 단서 수준

성격:
- flat reason only보다는 한 단계 두껍다
- 하지만 recommendation처럼 방향성을 주지 않는다

### context-qualifying band

의미:
- relation hint를 과장 없이 조금 더 읽게 하는
  얇은 comparison context 수준

성격:
- 맥락을 주지만
  evidence나 workflow로 넘어가지 않는다

### low-claim absence / thinness band

의미:
- 관계가 얇거나 거의 없을 때
  과장된 의미를 만들지 않게 하는 low-claim 층

성격:
- “없음”이나 “얇음”도
  recommendation이 아닌 상태로 유지시킨다

## 4. band qualities

이번 draft에서 허용하는 qualities:

- small
- low-claim
- relation-thickening only
- non-recommendation
- non-evidence-bearing

이 band들은
current thinness를 아주 조금만 완화하는 방향이어야 한다.

## 5. compare model vs payload shaping rule

### compare model 중심

- information band의 origin은 compare model 쪽에 있어야 한다
- relation hint의 성격과 두께를 먼저 정의하는 주체는 compare model이다

### payload shaping 보조

- payload shaping은
  compare model에서 형성된 relation thickness가
  지나치게 flatten되지 않도록 전달을 돕는 보조 역할만 맡는다

### adapter mediation 비중심

- adapter는 mediation layer다
- information band의 origin으로 보지 않는다

## 6. disallowed in this draft

이번 draft에서도 계속 금지되는 것은 아래다.

- ranking-like signal
- recommendation-like phrasing
- evidence-bearing content
- workflow/action-driving meaning
- UI-structuring role

이유:
- 이런 성질이 들어오면
  information band는 small relation hint가 아니라
  compare interpretation surface로 바뀐다

## 7. boundary

이 draft가 다루는 것:

- 어떤 종류의 information band가 필요한지
- 각 band가 담아야 하는 정보 두께의 성격
- compare model 중심 / payload shaping 보조 원칙

이 draft가 다루지 않는 것:

- concrete field names
- schema shape
- payload branch 설계
- implementation logic
- UI consumer behavior

경계:

- **information-band 성격까지가 이 draft**
- **구체 형식과 구조를 정하기 시작하면 다음 단계**다

## 8. one-line lock

- compare candidate enrichment field-spec draft v2는
  compare model 중심에서 `small, low-claim, non-recommendation` relation-hint band를 상정하는
  더 조여진 field-spec draft다.
