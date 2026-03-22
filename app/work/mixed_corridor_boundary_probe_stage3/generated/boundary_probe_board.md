# boundary probe board

## 1. 현재 strongest corridor family
- `technical->business::ai_business` / `specific`
- `technical->organization::ai_business` / `specific`
- `technical->organization::harness_agent` / `specific`

## 2. reinforcing / adjacent / off-axis 그룹 비교표
- `reinforcing`: strong=`3`, meaningful=`0`, weak=`2`, none=`1` / dominant=`corridor_specific_reentry`
- `adjacent`: strong=`0`, meaningful=`2`, weak=`4`, none=`0` / dominant=`bridge_partial_echo`
- `off_axis`: strong=`0`, meaningful=`0`, weak=`3`, none=`3` / dominant=`no_meaningful_match`

## 3. technical->organization vs technical->business specificity 비교
- technical->organization corridors: `2` / readings=`['specific', 'specific']`
- technical->business corridors: `1` / readings=`['specific']`

## 4. false positive risk 요약
- specificity counts: `{'specific': 3}`

## 5. stable_closure_reached 여부
- 이번 stage3에서도 `stable_closure_reached` 는 없음

## 6. promotion rule을 아직 만들면 안 되는 이유
- boundary challenge passes still measure observer specificity, not stable closure.
- off-axis resonance remains possible on topic-heavy technical text.

## 7. 다음 턴 추천
- add more off-axis negative controls or a second reinforcing business transcript before any promotion discussion.
