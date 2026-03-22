# mixed reentry probe stage1 spec

## 1. 목적
- 기존 mixed hold corridor가 후속 transcript 또는 반대 round에서 다시 붙어 closure를 강화하는지 read-only로 검증한다.

## 2. 현재 잠긴 계약
- mixed는 버릴 재료가 아니라 hold corridor다
- bridge 없음 -> unreadable 쪽
- bridge 있음 + stable closure 없음 -> mixed
- bridge 있음 + stable closure 도달 -> canonical
- mixed 카드 최소 계약:
  - `transition_from`
  - `transition_to`
  - `hold_reason`
  - `bridge fragments`
  - `closure_gap`
  - `why_not_canonical`

## 3. re-entry candidate 정의
- repeated anchor support 있음
- transition_from / transition_to 분명함
- bridge fragments 명시됨
- closure_gap이 transition-led 중심임
- good_hold 또는 hold 가치가 있는 mixed임

## 4. re-entry match 정의
- 같은 anchor group 또는 강한 semantic overlap
- 같은 transition corridor 유형
- 같은 arrival axis 또는 매우 가까운 arrival axis
- 이전 mixed의 bridge 방향을 보강하는 fragment 존재

## 5. strength 단계 정의
- `none`
- `weak`
- `meaningful`
- `strong`

## 6. closure delta 정의
- `no_change`
- `anchor_only_reinforced`
- `arrival_axis_clearer`
- `closure_partially_strengthened`
- `near_canonical_but_hold`
- `stable_closure_reached`

## 7. 이번 턴 비목표
- 코어 수정
- 판정 규칙 변경
- 억지 승격
- 새 ontology 추가

## 8. 성공 조건
- mixed hold 유닛이 re-entry candidate로 정리된다
- round 간 재등장/재보강 여부가 읽힌다
- hold 가치가 실제로 일부 증명된다
- 강화와 승격을 혼동하지 않는다
