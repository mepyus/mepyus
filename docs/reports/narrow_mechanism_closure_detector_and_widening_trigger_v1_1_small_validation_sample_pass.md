# narrow mechanism closure detector + widening trigger v1.1 small validation sample pass

## 1. 선정한 small validation sample과 이유

- sample: `choi_ai_classroom_vlm / carryover_risk`
- 선정 이유:
  - 기존 검증의 중심이었던 `grounding_status`, `traceability_status`, `emergence_status`와 다르게,
    이 사례는 `current + next`가 실제로 같은 설명 흐름을 이어 주는 것처럼 보인다.
  - 동시에 현재 상태는 `binding_closed = no`, `anchor=None`, `anchors=[]`라서,
    v1.1 contract가 local context의 설명력만 보고 detector/widening을 과발동시키지 않는지 보기 좋다.
  - 즉 이 sample은 “widening 유혹은 있지만 detector 전제는 충족하지 않는” 경계 사례다.

## 2. v1.1 적용 결과

### 2-1. current unit

- row family: `carryover_risk`
- asset: `choi_ai_classroom_vlm`
- current paragraph ref:
  - `lines 81-82 @ 4:29`
- current paragraph text:
  - `가지 이유를 드러놨는데 데이터 수집이 훨씬 편하죠.이 이즈 데이터 컬렉션이죠. 예. 우리가 데이터를`
- next sentence / local widening 후보:
  - `lines 83-84 @ 4:36`
  - `수집해서 그걸 일일이 다 사람한테 레이블링을 시키는 거는 되게 힘든 일입니다. 예. 그래서 어 그냥 어`
- fragment state:
  - `anchor=None`
  - `anchors=[]`
  - `scene=comparison`
  - `flow=tension`
- reread state:
  - `match_score=2`
  - `match_confidence=medium`

### 2-2. expected vs actual by v1.1

- `binding_closed`
  - expected reading: `no`
  - actual by sample state: `no`
- `semantic_fidelity`
  - expected reading: `not evaluable as closure`, because canonical closure 자체가 아직 없다
  - actual by sample state: canonical closure 없음
- `output_worthiness`
  - expected reading: `yes`
  - actual: `yes`
- `meaning_context_sufficiency`
  - expected reading: `minimum sufficient`
  - actual: `minimum sufficient`
  - 이유:
    - 문장 자체는 읽힌다
    - 하지만 row 의미 전체를 안정적으로 운반한다기보다, 다음 문장이 붙어야 `왜 이게 carryover risk인지`가 더 분명해진다

### 2-3. detector / widening 판정

- detector should fire?
  - `no`
  - 이유:
    - v1.1 detector의 선결 조건은 `binding_closed = yes`인데, 현재 sample은 여전히 `binding_closed = no`다
- detector did fit by v1.1 wording?
  - `no`
- widening should fire?
  - `no`
  - 이유:
    - widening trigger는 detector가 먼저 켜져 있어야 한다
    - 이 sample은 next sentence가 실제로 설명을 이어 주지만, detector 전제가 성립하지 않는다
- widening did fit by v1.1 wording?
  - `no`

## 3. false positive / false negative / ambiguity 체크

- false positive:
  - 없음
  - 이 sample은 widening 유혹이 있는 사례인데도, v1.1은 `binding_closed = no`를 이유로 detector/widening을 켜지 않았다
- false negative:
  - 없음
  - 이 sample은 현재 설계상 detector가 켜지면 안 되는 사례다
- ambiguity:
  - 있다, 하지만 contract 바깥이 아니라 sample 쪽 ambiguity다
  - `current + next`는 실제로 carryover risk 의미를 보강한다
  - 다만 v1.1은 `closure 이후 local widening` 후보 contract이므로, 이런 pre-closure 사례까지 포괄하려고 하지 않는다
  - 이 점은 broad default rule 금지와도 맞는다

## 4. output-worthiness / meaning-context sufficiency 보조 판정

- output-worthiness:
  - `yes`
  - 현재 문장은 읽기/표시 단위로 최소 성립한다
- meaning-context sufficiency:
  - `minimum sufficient`
  - current unit만으로도 “데이터 수집이 더 편하다”는 비교 포인트는 읽히지만,
    바로 다음 문장이 붙어야 `일일이 레이블링하는 비용/노동`이 드러나면서 row 의미가 더 안정된다
- mechanism 설명 편향 여부:
  - `mechanism-only`라기보다 `risk rationale fragment`에 가깝다
  - 그래서 이 sample은 detector 사례라기보다, detector가 켜지지 않아야 하는 경계 사례로 더 중요했다
- next sentence 성격:
  - `실제 보강`
  - noise가 아니다
  - 그러나 detector 미발동 상태이므로 widening trigger까지 가면 안 된다

## 5. validation verdict

- 판정:
  - `v1.1을 감독 기준 후보로 채택 가능`
- 이유:
  - 이 sample은 widening의 설명력은 있지만 detector 전제가 없는 사례다
  - v1.1은 이 경계 사례에서 broad rule처럼 과발동하지 않았다
  - 즉 wording이 실제 적용 단계에서도 operational하게 버틴다

## 6. 다음 supervisor 지시를 위한 메모

- 이번 sample이 중요한 이유:
  - v1.1이 “next sentence가 의미를 보강하면 무조건 widen” 같은 broad rule로 오작동하지 않는지 확인해 줬다
- v1.1이 잘 버틴 지점:
  - `binding_closed = yes`를 detector의 실제 gate로 유지한 점
  - `output-worthiness / meaning-context sufficiency`와 `closure 여부`를 혼동하지 않은 점
- 아직 애매한 지점:
  - pre-closure reread quality가 충분히 좋고 next sentence도 보강적일 때,
    이것을 별도 watchpoint로 남길 필요가 있는지는 아직 안 잠겼다
- 다음 턴 추천:
  - `감독 기준 후보 채택`
  - 필요하면 구현 전 `pre-closure context-bearing watchpoint`를 별도 note로만 정리

## 7. 한 줄 결론

- `carryover_risk / vlm`은 next sentence가 실제 보강을 주는 경계 사례였지만, v1.1 contract는 `binding_closed = no`라는 전제를 지켜 detector와 widening을 과발동시키지 않았다. 따라서 v1.1은 감독 기준 후보로 채택 가능한 수준의 operational validity를 보인다.
