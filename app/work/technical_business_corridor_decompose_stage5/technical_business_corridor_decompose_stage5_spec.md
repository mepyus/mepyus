# technical_business_corridor_decompose_stage5 spec

## 1. 목적
- `technical->business::ai_business` 를 observer layer에서 더 좁은 business arrival axis 후보로 분해한다.
- corridor의 흐림이 `format/source-family noise` 때문인지, `business 내부 axis 혼합` 때문인지 구분한다.

## 2. 현재 baseline
- `technical->organization::ai_business` = `mostly_meaning_driven`
- `technical->organization::harness_agent` = `mostly_meaning_driven`
- `technical->business::ai_business` = `format_noisy`
- `stable_closure_reached` = 없음
- promotion rule 논의 금지

## 3. 왜 business corridor 정밀 분해가 필요한가
- business corridor는 same-meaning / cross-family에선 잘 붙지만 same-format / same-family에서도 meaningful echo가 남았다.
- 이 noise가 corridor 전체의 약함이 아니라 내부 arrival axis 혼합일 가능성이 있다.

## 4. positive control
- `technical->organization::ai_business`
- `technical->organization::harness_agent`
- 이번 턴에서는 재정의 대상이 아니라 clean baseline 비교 기준선으로만 사용한다.

## 5. 하위 arrival axis 후보
- `business_leverage`
- `monetization_value_capture`
- `startup_thesis`
- `org_business_boundary`
- `software_value_shift`

## 6. match type
- `axis_specific_reentry`
- `business_corridor_general_echo`
- `bridge_partial_echo`
- `format_resonance_only`
- `family_assisted_echo`
- `no_meaningful_match`

## 7. decomposition judgment
- `single_corridor_plausible`
- `multi_axis_mixed`
- `mostly_axis_specific`
- `format_noisy`
- `family_noisy`
- `unclear`

## 8. 비목표
- 코어 corridor 분할
- canonical promotion
- organization corridor 재정의
- stable closure 해석 확대

## 9. 성공 조건
- business 하위 axis 후보별 반응 차이가 보인다.
- format/family noise와 axis 혼합이 어느 정도 분리된다.
- positive control과의 clean/noisy 차이가 설명된다.
- observer layer split 후보만 남기고 코어 분할은 하지 않는다.
