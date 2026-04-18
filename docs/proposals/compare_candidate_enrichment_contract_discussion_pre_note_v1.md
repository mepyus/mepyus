# compare candidate enrichment contract discussion pre-note v1

## 1. verdict

이 문서는
`compare candidate enrichment`를 위해 contract를 논의하더라도
**어디까지를 논의 가능한 범위로 볼지**를 먼저 잠그는 pre-note다.

중요:
- 아직 concrete field spec이 아니다
- contract change proposal이 아니다
- implementation design도 아니다

이번 단계의 목적은
contract discussion이 작은 relation hint 후보를 넘어서
payload rewrite나 UI inflation으로 번지지 않게
경계를 먼저 자르는 데 있다.

## 2. codex alignment note

- 감독관의 “이제는 contract discussion pre-note 단계다” 판단에 동의한다.
- information layer의 성격은 이미 잠겼으므로, 다음은 contract를 논의하더라도 어디까지가 허용되는지 먼저 자르는 편이 맞다.
- 이 단계에서 가장 위험한 과잉 확장 지점은
  작은 relation hint를 말하다가 concrete field, payload branch, UI dependency를
  사실상 이미 정해진 전제로 끌어오는 순간이다.
- resolution:
  - 이번 문서에서는 contract를 “어디까지 논의할 수 있는가”만 다루고
  - 변경안, 필드, 구현은 계속 열지 않는다.

## 3. pre-note purpose

왜 이 문서가 필요한가:

- proposal draft에서 범위와 비범위를 잠갔다
- field-spec pre-note에서 정보층의 성격도 잠갔다
- 이제 남은 위험은
  contract discussion이 그 범위를 다시 불리는 것이다

즉 이번 문서의 핵심은:
- compare candidate enrichment를 위해 contract를 논의하더라도
- **어떤 표면까지만 추상적으로 논의 가능한지**
- **어디서부터는 이미 contract proposal/implementation인지**
를 분명히 적는 것이다

## 4. discussable contract surface

이번 단계에서 논의 가능한 contract surface는
추상 수준에서 아래까지다.

### compare model 쪽

- current compare model이
  relation hint를 담을 수 있는 성격의 표면인지
- 지금의 flatness가 model limitation으로 읽히는지
- future에 relation hint를 위한 최소 논의 여지가 있는지

중요:
- 여기서도 concrete relation field나 구조를 말하지 않는다

### payload shaping 쪽

- compare candidate 정보가 runtime/process-console payload로 나올 때
  현재처럼 너무 flat하게 눌리는지
- relation hint 수준의 정보를 이야기하더라도
  payload shaping에서 어느 정도 추상 논의가 가능한지

중요:
- payload branch 추가나 rewrite를 말하지 않는다

### adapter mediation 쪽

- adapter가 current compare candidate thinness를 거의 그대로 전달하는 mediation layer인지
- future에 mediation 관점에서 어떤 discussion surface가 있을 수 있는지

중요:
- adapter 변경안을 말하지 않는다
- adapter 역할이 origin이 아니라 mediation이라는 점만 확인한다

## 5. non-discussable areas

이번 단계에서 여전히 논의 금지인 것은 아래다.

### concrete field names

- 이유:
  - 이름을 정하는 순간 이미 spec 단계로 넘어간다

### schema change

- 이유:
  - schema 논의는 proposal scope를 단번에 키운다

### payload contract rewrite

- 이유:
  - 지금 단계는 rewrite 필요성 판단이 아니라
  discussion surface를 자르는 단계다

### UI behavior dependency

- 이유:
  - contract가 UI behavior를 당연한 소비처로 전제하면
  작은 enrichment 후보가 곧바로 UI 확장안으로 바뀐다

### ranking / recommendation semantics

- 이유:
  - compare candidate enrichment의 비범위를 즉시 침범한다

### evidence / workflow payload

- 이유:
  - relation hint를 넘어서 drilldown/action surface로 번지기 쉽다

## 6. contract discussion boundary

허용 가능한 contract discussion:

- compare model / payload shaping / adapter mediation 중
  **어느 표면이 current thinness와 가장 직접적으로 연결되는지**
- relation hint 수준의 정보를 논의한다고 할 때
  어디까지가 추상 discussion surface인지
- current contract가 너무 flat한지, 아니면 baseline restraint인지

허용되지 않는 contract discussion:

- 어떤 field가 필요하다는 말
- 어떤 branch를 추가해야 한다는 말
- 어떤 schema path를 바꿔야 한다는 말
- 어떤 UI가 그것을 소비할 것이라는 말

경계:

- **origin surface를 추상적으로 읽는 것까지가 discussion**
- **필드/형식/흐름을 정하기 시작하면 이미 proposal 본안 또는 implementation 설계**

## 7. inflation risks

### 1. structure inflation

- 작은 relation hint를 논의하다가
  richer compare structure 전체를 전제하게 될 위험

### 2. consumer inflation

- contract discussion을 하면서
  특정 UI surface나 future interaction을 당연한 소비처로 끌어올 위험

### 3. semantics inflation

- contract를 말하는 순간
  compare candidate가 recommendation/workflow 의미를 띠기 시작할 위험

## 8. entry rule for next stage

판정:
- **contract discussion memo v1**

이유:
- information layer와 boundary는 충분히 좁혀졌다
- 따라서 다음 단계는
  concrete contract proposal이 아니라
  compare model / payload shaping / adapter mediation 중
  어느 discussion surface가 가장 핵심인지 좁게 검토하는 memo가 맞다

## 9. board grounding separation

board grounding은 이번 contract discussion pre-note에서도 합치지 않는다.

- board grounding은 existing signal reuse와 surface suppression 경계 문제에 더 가깝다
- compare candidate thin relation은 current compare model flatness와 더 직접적으로 연결된다
- 따라서 contract discussion도 compare candidate 트랙 안에서만 유지하는 편이 맞다
