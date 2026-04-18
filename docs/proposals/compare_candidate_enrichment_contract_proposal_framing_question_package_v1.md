# compare candidate enrichment contract proposal framing / question package v1

## 1. verdict

판정:
- **ready for constrained contract proposal draft**

중요:
- 이것은 concrete contract proposal ready를 뜻하지 않는다
- schema proposal ready를 뜻하지 않는다
- implementation design ready를 뜻하지도 않는다

현재 의미는:
- contract proposal entry 안에서
  **어떤 질문을 먼저 잠가야 하는지**가 충분히 정리되었고,
  이제는 그 질문 구조 위에서 constrained contract proposal draft로 들어갈 수 있다는 뜻이다

## 2. package structure choice

이번 패키지는 **1문서 구조**를 택했다.

이유:
- 이번 턴의 핵심은
  framing purpose
  - core question set
  - hierarchy
  - premature-answer risk
  - go/hold decision
  을 하나의 질문 구조로 묶어 잠그는 데 있었다
- 별도 보조 문서를 두면
  질문과 경계와 리스크가 분리되어
  다시 answer-before-question drift가 생길 수 있다

## 3. framing purpose

왜 이 패키지가 필요한가:

- contract proposal entry는 이미 열렸다
- 하지만 아직 contract proposal 초안을 바로 쓰기 전에
  compare model 중심에서
  **무슨 질문을 먼저 붙들어야 하는지**가 정리돼야 한다

즉 이번 패키지의 목적은
- 답을 확정하는 것이 아니라
- 좋은 contract proposal 초안이 되기 전에
  어떤 질문 구조를 먼저 잠가야 하는지 만드는 것이다

## 4. core question set

아래 질문들은
contract proposal 초안 전에 반드시 먼저 잡아야 할 핵심 질문들이다.

### question 1

- **compare model은 compare candidate relation thickness를 어디까지 설명해야 하는가?**

### question 2

- **현재 `flat reason only` 수준을 넘는 최소 relation hint는 어떤 성격까지 허용되는가?**

### question 3

- **relation hint를 두껍게 하더라도 어떤 지점부터 recommendation-like interpretation으로 넘어가는가?**

### question 4

- **payload shaping은 compare model에서 형성된 relation thickness를 어디까지 supporting question으로만 다뤄야 하는가?**

### question 5

- **minimal information layer는 contract discussion 안에서도 어떻게 low-claim 상태를 유지해야 하는가?**

### question 6

- **다음 constrained contract proposal draft에서도 어떤 질문은 계속 바깥에 두어야 하는가?**

## 5. question hierarchy

### primary questions — compare model 중심

- question 1
- question 2
- question 3
- question 5

이유:
- current thin relation의 핵심 origin은 compare model flatness로 읽히기 때문이다

### supporting questions — payload shaping 보조

- question 4

이유:
- payload shaping은 compare model에서 형성된 relation thickness가
  지나치게 flatten되지 않도록 보는 보조 축까지만 맡는다

### out-of-scope questions

- “어떤 concrete field name이 필요한가?”
- “어떤 schema path를 바꿔야 하는가?”
- “UI는 이 정보를 어떻게 보여줄 것인가?”
- “adapter는 무엇을 새로 가져와야 하는가?”

### adapter mediation positioning

- adapter mediation은 **non-central**

이유:
- adapter는 현재 thinness를 전달하는 mediation layer지만
  origin question의 중심은 아니다

## 6. premature-answer risk scan

### risk 1. question이 사실상 답안/shape로 굳는 위험

위험:
- 질문을 적는 순간 이미 minimal layer shape를 정답처럼 고정해버릴 수 있다

early stop:
- 질문이 `무엇이 가능한가`가 아니라
  `무엇이어야 한다`로 바뀌면 멈춘다

### risk 2. question이 concrete field/spec 쪽으로 미끄러지는 위험

위험:
- 질문이 곧바로 key, slot, branch, schema 단위로 내려갈 수 있다

early stop:
- 질문 문장 안에 field-like naming이나 구조 전제가 들어오기 시작하면 멈춘다

### risk 3. question이 UI need 중심으로 재구성되는 위험

위험:
- compare panel의 현재 얇음을 해결하고 싶다는 욕구가
  질문 자체를 UI-consumer 중심으로 바꿀 수 있다

early stop:
- 질문이 `UI에서 더 잘 보이려면`으로 시작되면
  다시 compare model origin question으로 되돌린다

## 7. naming rule carryover

이번 질문 패키지에서도
[compare_candidate_enrichment_field_spec_draft_v2.md](/Users/sungsookim/universe/vectorfl_replica/docs/proposals/compare_candidate_enrichment_field_spec_draft_v2.md)는
계속 아래처럼 읽어야 한다.

- `spec ceiling draft`
- `not concrete field spec`

이유:
- 질문 패키지 단계에서 이 문서를 concrete spec처럼 읽으면
  질문보다 답이 먼저 고정된다

### naming risk가 다시 살아나는 방식

- framing 단계에서
  “이미 spec이 있으니 이제 필드만 정하면 된다”는 식으로 읽히는 순간
  naming risk가 다시 살아난다

따라서:
- 질문 패키지 단계에서도
  explicit reading rule carryover는 계속 필요하다

## 8. contract proposal entry boundary restatement

이번 패키지에서도 여전히 바깥에 두는 것은 아래다.

- concrete field names finalized
- schema shape
- payload rewrite
- UI consumer behavior
- implementation logic
- ranking/recommendation/evidence/workflow semantics

즉 contract proposal entry가 열렸어도,
아직 concrete proposal 본안은 시작되지 않았다.

## 9. go / hold decision

판정:
- **ready for constrained contract proposal draft**

왜 ready인가:

1. core question set가 충분히 정리됐다
2. primary/supporting/out-of-scope hierarchy도 명확하다
3. premature-answer risk에 대한 early stop 기준이 생겼다
4. naming rule carryover와 entry boundary도 유지된다

왜 hold가 아닌가:
- 더 이상 framing 단계에 머물러도
  질문 구조에서 새 핵심 항목이 추가될 가능성은 높지 않다
- 남은 일은 이제 이 질문 구조를 constrained draft로 옮기는 것이다

## 10. if ready: rationale

왜 이제 contract proposal 초안으로 들어갈 수 있는가:

- 질문 구조가 compare model 중심으로 충분히 잠겼다
- payload shaping은 supporting question으로만 정리됐다
- out-of-scope가 분명해졌다
- early stop 기준이 있어 draft가 answer/spec inflation으로 미끄러질 때 제어 가능하다

중요:
- 다음 draft도 여전히 **constrained contract proposal draft** 여야 한다
- concrete contract, schema, implementation으로 점프하면 안 된다

## 11. if hold: rationale

- not applicable

이번 패키지 판정은 hold가 아니다.

## 12. risk and correction record

### 이번 패키지에서 본 리스크

1. naming drift
2. answer-before-question drift
3. overtranslation drift
4. payload/UI re-centralization

### 어떻게 통제했는가

- question hierarchy를 분명히 했다
- early stop 기준을 명시했다
- explicit reading rule을 carry했다
- compare model primary / payload shaping supporting 구도를 다시 고정했다

이 기록은 working memory 차원에서
“entry를 연 다음 단계에선, 좋은 질문 구조를 먼저 잠그는 것이 draft 품질을 좌우한다”
는 원칙으로 남긴다.

## 13. alignment / memory record

- supervisor starting judgment:
  현재는 contract proposal entry가 열려 있으므로, 이제는 어떤 질문을 중심으로 논의를 전개할지 framing 해야 한다고 했다.
- codex own judgment:
  질문 구조를 먼저 잠그지 않으면 contract proposal draft가 곧바로 answer/spec inflation으로 흐를 위험이 크다고 봤다.
- disagreement or risk:
  `field_spec_draft_v2`가 concrete spec처럼 오해되면 질문 패키지 자체가 무력화될 수 있다는 리스크가 남아 있었다.
- resolution:
  explicit reading rule, question hierarchy, early stop 기준을 함께 묶어
  constrained contract proposal draft로 넘어갈 준비를 완료했다고 정리했다.

## 14. recommendation

다음 단계 추천:
- **constrained contract proposal draft**

이유:
- 이제는 무엇을 질문해야 하는지가 충분히 잠겼다
- 다음 단계는 그 질문 구조를 바탕으로
  contract-side proposal 초안을 더 제한적으로 써보는 쪽이 맞다

한 줄로:
- 지금부터는 답을 급히 정하는 것이 아니라, **좋은 질문 구조 위에서 constrained contract proposal draft를 쓰기 시작할 수 있는 상태**다.
