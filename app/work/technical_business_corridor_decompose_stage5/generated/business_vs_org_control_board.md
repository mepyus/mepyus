# business vs org control board

## 1. organization corridor를 positive control로 둔 이유
- `technical->organization::ai_business`, `technical->organization::harness_agent` 는 stage4에서 `mostly_meaning_driven` 으로 읽혔다.

## 2. organization corridor와 business corridor의 clean/noisy 차이
- org control `technical->organization::ai_business`: `mostly_meaning_driven` / format_noise=`low` / family_bias=`medium`
- org control `technical->organization::harness_agent`: `mostly_meaning_driven` / format_noise=`low` / family_bias=`medium`
- focus business `technical->business::ai_business`: `multi_axis_business_mix` / format_noise=`medium` / family_noise=`medium`

## 3. business corridor 내부 axis 혼합 가능성
- strongest_axis: `startup_thesis`
- secondary_axes: `['monetization_value_capture', 'org_business_boundary']`

## 4. current strongest business sub-axis 후보
- `monetization_value_capture`: strong=`1`, meaningful=`0` / dominant=`mostly_axis_specific`
- `startup_thesis`: strong=`2`, meaningful=`0` / dominant=`multi_axis_mixed`
- `org_business_boundary`: strong=`1`, meaningful=`0` / dominant=`mostly_axis_specific`

## 5. 아직 promotion이 아닌 이유
- business corridor는 일부 clean sub-axis가 보여도 전체 corridor는 여전히 axis 혼합 + format/family noise를 함께 가진다.

## 6. 다음 단계 추천
- observer layer에서 `startup_thesis` 와 `org_business_boundary` 를 우선 split candidate로 더 관찰한다.
