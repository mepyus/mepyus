# format disentangle board

## 1. strongest meaning-driven corridor
- `technical->organization::ai_business` / `mostly_meaning_driven`
- `technical->organization::harness_agent` / `mostly_meaning_driven`

## 2. format-assisted로 보이는 corridor

## 3. family bias 경고 사례
- `technical->business::ai_business` / family_bias=`medium`
- `technical->organization::ai_business` / family_bias=`medium`
- `technical->organization::harness_agent` / family_bias=`medium`

## 4. 4개 입력 그룹 비교표
- `same_meaning_different_format`: strong=`3`, meaningful=`0`, weak=`0`, none=`0` / dominant=`corridor_specific_reentry` / `meaning_driven`
- `same_format_different_meaning`: strong=`0`, meaningful=`2`, weak=`4`, none=`0` / dominant=`bridge_partial_echo` / `format_noisy`
- `same_family_shifted_axis`: strong=`0`, meaningful=`2`, weak=`4`, none=`0` / dominant=`bridge_partial_echo` / `family_assisted`
- `cross_family_same_corridor`: strong=`2`, meaningful=`1`, weak=`3`, none=`0` / dominant=`bridge_partial_echo` / `format_assisted`

## 5. technical->organization vs technical->business 비교
- technical->organization: `['mostly_meaning_driven', 'mostly_meaning_driven']`
- technical->business: `['format_noisy']`

## 6. stable_closure_reached 여부
- 이번 stage4에서도 `stable_closure_reached` 는 없음

## 7. 다음 턴 추천
- add more cross-family same-corridor inputs and more same-format different-meaning negatives before any promotion discussion.
