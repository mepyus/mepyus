# compare candidate enrichment contract shape memo v1

## 1. verdict

이 문서는 `compare candidate enrichment`를 담기 위한
**contract shape의 성격**을 추상 수준에서 잠그는 memo다.

중요:
- 아직 field spec이 아니다
- concrete field names를 적지 않는다
- schema나 branch를 설계하지 않는다
- implementation design으로도 가지 않는다

이번 memo의 목적은
proposal draft에서 잠근 문제 정의와 범위를 바탕으로,
다음 단계에서 field spec으로 가더라도
shape가 recommendation/evidence/workflow 쪽으로 비대해지지 않게
그 **형태적 성격**을 먼저 고정하는 것이다.

## 2. memo purpose

왜 contract shape memo가 필요한가:

- proposal draft는
  목적, 범위, 비범위, discussion surface를 잠갔다
- 하지만 field spec으로 바로 가면
  “어떤 형태의 계약 층을 상상하는가”보다
  “어떤 키를 둘까”가 먼저 튀어나오기 쉽다

즉 이번 memo의 핵심은:
- compare candidate enrichment를 담는 contract가
  **어떤 종류의 shape여야 하는가**
- 그리고 **어떤 종류의 shape여선 안 되는가**
를 추상 수준에서 먼저 정리하는 것이다

## 3. shape concept

현재 이 트랙에서 상상하는 contract shape는
아래 성격에 가깝다.

### not flat reason only

- 지금처럼 거의 비어 있거나 너무 납작한 reason만으로 끝나면
  compare relation은 계속 thin하게 읽힌다

### lightweight relation cue layer

- compare candidate가 왜 붙는지에 대해
  아주 작은 relation cue를 담을 수 있는 층

### minimal relation bundle

- 단일 flat token보다 조금 더 thick하지만
  recommendation이나 evidence bundle로는 가지 않는
  최소 relation 묶음

중요:
- 이건 field 구조가 아니다
- relation cue를 담는 **shape의 성격**만 말한다

즉 현재 shape concept는
- `flat reason only`보다 한 단계 두껍고
- `rich relation structure`보다 훨씬 얇은
  **small relation-hint bearing layer**에 가깝다

## 4. primary vs supporting shape role

### compare model as primary shape role

- compare model은
  relation thickness를 생성/정의하는 중심 표면이어야 한다
- 즉 “어떤 종류의 relation hint가 존재할 수 있는가”라는 shape의 중심은
  compare model 쪽에 있어야 한다

### payload shaping as supporting shape role

- payload shaping은
  compare model에서 형성된 relation thickness가
  지나치게 flatten되지 않도록 보조하는 표면까지만 맡아야 한다
- shape의 주체가 payload shaping이 되면
  origin보다 운반 형식이 먼저 커질 위험이 있다

### adapter mediation is not a shape origin

- adapter는 mediation layer다
- compare candidate enrichment shape를 정의하는 origin이 아니다
- 따라서 shape 논의의 중심을 adapter에 두지 않는다

## 5. allowed shape qualities

이번 후보에서 허용되는 contract shape의 성질은 아래다.

### small

- shape는 작아야 한다
- compare candidate를 richer structure로 키우는 방향이 아니다

### non-recommendation

- shape는 어떤 candidate를 더 보라고 유도하지 않는다
- 방향성/우선순위/선호를 담지 않는다

### non-evidence-bearing

- shape는 evidence payload를 싣지 않는다
- why-chain이나 trace packet처럼 커지지 않는다

### relation-thickening only

- shape의 역할은
  현재 너무 thin한 relation을 한 단계만 두껍게 하는 데 그친다

### low-claim

- shape는 작은 cue를 담되
  해석 권위가 높은 구조처럼 읽히지 않아야 한다

## 6. disallowed shape qualities

아래 성질은 계속 금지된다.

### ranking-like

- compare candidate를 줄 세우는 순간
  shape가 recommendation surface처럼 읽힌다

### recommendation-like

- 특정 candidate를 더 맞는 방향으로 밀기 시작하면
  relation hint를 넘어선다

### evidence-carrying

- evidence를 싣기 시작하면
  compare candidate shape가 drilldown payload처럼 커진다

### workflow-driving

- next step이나 operator action을 암시하면
  shape가 행동 surface를 끌어오게 된다

### UI-structuring

- shape가 특정 UI block이나 richer layout을 전제하기 시작하면
  contract shape가 UI inflation의 원인이 된다

즉 금지되는 것은 모두
shape를 작은 relation cue 층에서
추천/근거/행동/구조 층으로 끌어올리는 성질이다.

## 7. shape boundary

이 memo 안에서 다루는 것:

- compare candidate enrichment를 담을 contract shape의 성격
- 그 shape가 어느 정도 두께까지 허용되는지
- 어떤 qualities는 허용되고 어떤 qualities는 금지되는지

이 memo 밖에 두는 것:

- concrete field spec
- schema discussion
- payload branch 설계
- implementation design
- UI consumer behavior

경계 규정:

- **shape의 질감과 두께를 말하는 것까지가 이 memo**
- **형식, 구조, 위치를 정하기 시작하면 다음 단계**다

## 8. next-step gate

판정:
- **field spec draft v1**

이유:
- contract shape의 성격은 이번 단계에서 충분히 좁혀졌다
- 따라서 다음은 concrete 설계로 바로 뛰기보다,
  이 shape concept를 field spec 수준으로 옮길 수 있는지
  가장 좁은 draft를 써볼 단계다

## 9. board grounding separation

이번 memo에서도 board grounding은 계속 별도 트랙으로 둔다.

- board grounding absence는 existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- compare candidate thin relation은 compare model flatness와 더 직접적으로 연결된다
- 따라서 shape memo도 compare candidate 트랙 안에서만 유지하는 편이 맞다
