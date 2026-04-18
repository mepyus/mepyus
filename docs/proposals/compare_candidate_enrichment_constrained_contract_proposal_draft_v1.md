# compare candidate enrichment constrained contract proposal draft v1

## 1. verdict

판정:
- **keep as constrained contract proposal draft**

중요:
- 이것은 concrete contract proposal이 아니다
- schema proposal이 아니다
- implementation design이 아니다

현재 의미는 아래까지다.
- compare candidate thin relation에 대해
  compare model 중심 / payload shaping 보조라는 전제 아래
  **아주 제한된 수준의 contract proposal answer draft**를 쓸 수 있다
- 하지만 이 answer draft는
  concrete field, schema, implementation으로 내려가기 전의
  constrained proposal 층에 머물러야 한다

## 2. package structure choice

이번 패키지는 **1문서 구조**를 택했다.

이유:
- 이번 턴의 핵심은
  - proposal purpose
  - constrained answer draft
  - constraint carryover
  - inflation scan
  - keep/stop decision
  을 한 번에 묶어 판단하는 데 있었다
- 별도 review 문서를 두면
  answer와 stop condition이 분리되어
  다시 answer-before-boundary drift가 생길 수 있다

## 3. proposal purpose

이 constrained draft가 해결하려는 문제는 아래다.

- current compare model flatness 때문에
  compare candidate relation thickness가 충분히 설명되지 않는다
- 그 결과 compare panel은
  candidate 존재는 말하지만
  relation이 왜 붙는지에 대한 low-claim reading thickness는 충분히 주지 못한다

하지만 해결 방향은 아래로 제한된다.

- recommendation/workflow로 커지지 않는다
- richer compare interpretation surface를 만들지 않는다
- 오직 **low-claim relation thickening** 수준까지만 다룬다

즉 이번 draft의 목적은
- compare model이 relation thickness를 조금 더 설명할 수 있어야 한다는 방향을 제안하되
- 그 방향이 concrete spec/schema/implementation으로 미끄러지지 않게
  constrained proposal 상태로 잠그는 것이다

## 4. proposal answer draft

이번 draft의 answer는
question package에서 잠근 질문들에 대한
**낮은 해상도의 방향 답안**까지만 허용한다.

### answer 1. compare model은 flat reason only를 넘는 low-claim relation thickness를 설명할 수 있어야 한다

- compare model은
  compare candidate가 왜 붙는지에 대해
  단일 flat reason보다 조금 더 읽히는 relation thickness를 가질 수 있어야 한다
- 다만 그 thickness는
  recommendation이나 evidence처럼 해석 권위를 높이는 방향이 아니라
  **small relation cue** 수준에 머물러야 한다

### answer 2. minimal information layer는 relation hint와 얇은 context를 담되 low-claim 성격을 유지해야 한다

- relation thickness는
  단순 존재 여부를 넘어
  왜 이 candidate가 붙는지에 대한 작은 힌트를 줄 수 있어야 한다
- 동시에 그 힌트는
  selected asset와 candidate 사이의 맥락을
  과장 없이 조금 더 읽게 하는 수준까지만 허용된다
- relation이 약하거나 거의 비어 있는 경우도
  과장된 의미를 만들지 않는 low-claim 상태로 유지되어야 한다

### answer 3. payload shaping은 compare model에서 형성된 relation thickness를 보조적으로만 운반해야 한다

- payload shaping의 역할은
  compare model에서 형성된 low-claim relation thickness가
  지나치게 flatten되지 않도록 돕는 수준까지만 허용된다
- payload shaping이 relation thickness의 주체가 되거나
  contract 논의의 중심이 되어서는 안 된다

### answer 4. adapter mediation은 origin answer를 결정하는 중심이 아니다

- adapter는 current thinness를 전달하는 mediation layer일 수는 있지만
  relation thickness를 정의하는 중심 주체는 아니다
- 따라서 이 draft의 answer는
  adapter 중심 contract answer로 번역되지 않아야 한다

### answer 5. compare candidate enrichment는 compare interpretation이 아니라 comparison aid를 조금 두껍게 하는 방향이어야 한다

- enrichment의 방향은
  selected asset 옆의 read-only comparison aid를
  한 단계만 덜 납작하게 만드는 데 있다
- candidate를 고르거나 추천하거나 행동으로 연결하는 의미는
  계속 이 draft 밖에 둔다

## 5. constraint carryover

이번 draft 안에서도 아래 규칙은 그대로 유지된다.

### spec ceiling draft reading rule

[compare_candidate_enrichment_field_spec_draft_v2.md](/Users/sungsookim/universe/vectorfl_replica/docs/proposals/compare_candidate_enrichment_field_spec_draft_v2.md)는
계속 아래처럼 읽어야 한다.

- concrete field spec이 아니다
- `spec ceiling draft`다
- UI consumer, schema, implementation을 전제하지 않는다

### surface and origin rule

- compare model primary
- payload shaping secondary
- adapter mediation non-central

### non-goal carryover

- ranking 금지
- recommendation wording 금지
- evidence drilldown 금지
- workflow/action affordance 금지
- UI inflation 금지

## 6. non-goals and stop conditions

### 계속 금지되는 것

- ranking
- recommendation wording
- evidence drilldown
- workflow/action affordance
- UI inflation
- concrete field finalized
- schema shape
- implementation logic

### stop conditions

아래 중 하나라도 생기면
이번 constrained draft는 그 자리에서 멈춰야 한다.

1. answer가 concrete field/spec처럼 굳기 시작할 때
2. payload나 UI가 중심처럼 커지기 시작할 때
3. compare model 중심이 흐려질 때

## 7. inflation scan

### answer concretization drift

판정:
- no critical drift

근거:
- answer는 방향과 성격만 말한다
- field names, keys, schema paths, payload branches를 확정하지 않는다

### schema drift

판정:
- no critical drift

근거:
- shape의 구조나 migration을 전제하지 않는다
- contract를 “어떻게 싣는가”보다 “어떤 information thickness를 허용하는가” 수준에 머문다

### payload-centralization drift

판정:
- no critical drift

근거:
- payload shaping은 계속 supporting role로만 적혀 있다
- relation thickness의 중심은 compare model로 유지된다

### UI-led contract drift

판정:
- no critical drift

근거:
- answer는 UI 개선 요구에서 출발하지 않는다
- compare panel은 단지 현재 thinness를 관찰하게 만든 surface일 뿐,
  contract answer의 중심이 아니다

### recommendation/workflow drift

판정:
- no critical drift

근거:
- relation thickness를 높이더라도
  low-claim / non-recommendation / non-workflow 상태를 계속 유지하도록 못박고 있다

## 8. keep / stop decision

판정:
- **keep as constrained contract proposal draft**

왜 keep인가:

1. answer draft가 question hierarchy 안에서만 움직인다
2. compare model primary / payload shaping secondary가 유지된다
3. non-goals와 stop conditions이 계속 살아 있다
4. critical inflation drift가 발견되지 않았다

왜 stop이 아닌가:
- 현재 draft는 아직 concrete contract proposal처럼 굳지 않았다
- spec ceiling을 overtranslate하거나 UI/payload를 중심으로 끌어올리는 징후도 critical 수준은 아니다

## 9. if keep: rationale

현재 draft가 constrained 상태를 유지한다고 보는 이유는 아래다.

- answer가
  “어떤 두께의 relation hint가 허용되는가”
  수준에 머문다
- compare model을 origin 중심으로 유지하고
  payload shaping은 운반 보조로 제한한다
- adapter mediation은 non-central로 고정돼 있다
- concrete field, schema, implementation으로 바로 번역되지 않는다

따라서 이 문서는
contract proposal의 방향을 제안하지만
여전히 **constrained contract proposal draft**로 읽어야 한다.

다음 단계:
- `contract proposal review package`

중요:
- 다음도 concrete contract proposal 본안이 아니라
  constrained draft를 다시 검토하는 패키지여야 한다

## 10. if stop: rationale

- not applicable

이번 패키지 판정은 stop이 아니다.

## 11. risk and correction record

### 이번 패키지에서 본 리스크

1. answer concretization drift
2. overtranslation drift
3. payload/UI re-centralization risk

### 통제 방식

- answer를 direction-level wording으로 제한했다
- `field_spec_draft_v2` reading rule을 다시 carry했다
- compare model primary / payload shaping secondary / adapter non-central 원칙을 반복해서 고정했다
- stop conditions를 문서 안에 직접 다시 적어
  draft가 concrete spec처럼 굳기 시작하면 멈추도록 했다

### working memory note

- constrained draft 단계에서는
  “답을 쓰는 것”보다
  “답이 어떤 해상도까지 허용되는가”를 계속 같이 적어야 한다
- 그렇지 않으면 proposal answer가 바로 shape/spec drift로 이어질 위험이 있다

## 12. alignment / memory record

- supervisor starting judgment:
  - 현재 상태는 ready for constrained contract proposal draft이며,
    concrete contract/schema/implementation 단계와는 분리해서 봐야 한다고 했다
- codex own judgment:
  - 이번 단계에서는 answer를 아주 낮은 해상도로만 쓰고,
    동시에 keep/stop scan을 붙여 constrained 상태를 지키는 것이 핵심이라고 봤다
- disagreement or risk:
  - relation thickness를 설명하려는 순간 answer가 field-like shape로 굳을 위험이 있었다
- resolution:
  - answer를 compare model direction, minimal information character, payload supporting role 수준에만 묶고
    concrete spec/schema/implementation 언어는 계속 밖에 두었다

## 13. recommendation

- 다음 단계는 **contract proposal review package**가 맞다.
- 이유는:
  - constrained draft는 열렸지만
  - 아직 이것을 concrete contract proposal로 오해하지 않도록
    한 번 더 review/tightening 성격의 패키지가 필요하기 때문이다
