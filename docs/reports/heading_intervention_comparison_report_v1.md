[[A]] [[OBJ:heading_intervention_comparison_report_v1]] [[SEM:before_after_comparison_for_minimal_heading_independent_role_probe]]

# heading intervention comparison report v1

## 1. experiment purpose

- 이번 비교의 목적은 pointer probe 이후에도 남아 있던 heading dependency가 role 계열 읽힘을 얼마나 막고 있었는지 확인하는 것이다.
- 즉 이 문서는 heading이 3순위인 이유와, heading-independent role probe가 실제로 무엇을 살리고 무엇을 못 살리는지 남기는 문서다.

## 2. baseline after pointer probe

- input_asset: `inputs/external_cases/claude_code_index.txt`
- baseline state:
  - explicit heading 기반 paragraph role 실행은 여전히 부적합
  - context unit ref는 붙었지만 paragraph role 해석 기관은 사실상 hold
  - role 계열은 `heading mismatch / rigid mapping / unsupported role generalization` 위험이 남아 있었다

## 3. heading-independent probe

- mode: `functional_cue`
- support:
  - explicit heading 대신 `context_unit`, `page_role`, `relation_movement`, `evidence_pointers`를 이용해 약한 role-like hint를 남김
- unchanged:
  - segmentation
  - pointer stitching
  - object naming logic

## 4. after heading probe

- role-like analyses generated: `3`
- role_probe_status:
  - `role_like_reading_observed`: `3`
- role_hint_strength:
  - `weak_medium`: `3`
- grounding_status:
  - `fallback_grounded`: `3`
- unsupported_role_naming_risk:
  - `low`: `3`

## 5. comparison reading

### A. what actually recovered

- hard heading mismatch failure는 줄었다
- evidence-linked role-like reading은 최소 수준으로 살아났다
- unsupported role naming을 크게 늘리지 않고 `transition_or_strategy`, `question_or_role_shift`, `compression_or_evaluation` 같은 약한 기능 힌트를 남길 수 있었다

### B. what did not recover

- paragraph role 자체가 generalized system처럼 살아난 것은 아니다
- 모든 grounding은 여전히 `fallback_grounded`다
- local / page / comparison의 정교한 역할 분화는 아직 부족하다
- question-inducing candidate가 비어 있는 문제는 그대로라 role probe가 그 공백을 대체하진 못한다

### C. why this still matters

- heading은 3순위가 맞다
- segmentation과 pointer가 먼저 없으면 role probe 자체가 설 자리가 없다
- 그러나 heading-independent cue를 통해 role 계열이 완전히 zero가 아니고, 최소한 `evidence-linked role-like reading` 수준까지는 관찰 가능하다는 점이 확인됐다

## 6. verdict

- heading probe recovered:
  - hard heading mismatch 완화
  - evidence-linked role-like hint 생성
  - unsupported role naming 통제
- heading probe did not recover:
  - generalized paragraph role reading
  - direct grounding
  - robust local/page/comparison role shift
- why object lift remains hold:
  - role 계열이 살아나도 전부 weak/fallback 수준이며 reusable attitude보다 still scaffold-bound institution에 더 가깝다

## 7. one-line summary

> heading-independent role probe는 `claude_code_index`에서 hard heading mismatch를 약한 evidence-linked role-like reading으로 바꾸는 데는 성공했지만, 아직 generalized paragraph-role system이나 direct grounded role support를 만들 수준은 아니므로 object lift hold는 그대로 유지된다.
