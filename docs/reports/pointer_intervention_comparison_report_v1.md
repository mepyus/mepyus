[[A]] [[OBJ:pointer_intervention_comparison_report_v1]] [[SEM:before_after_comparison_for_minimal_pointer_stabilization_probe]]

# pointer intervention comparison report v1

## 1. experiment purpose

- 이번 비교의 목적은 segmentation support 이후에도 남아 있던 grounding/ref 계열 문제를 `pointer stabilization` 최소 개입만으로 얼마나 줄일 수 있는지 보는 것이다.
- 즉 이 문서는 pointer가 왜 2순위인지 실제 비교 근거로 남기는 문서다.

## 2. baseline after segmentation support

- input_asset: `inputs/external_cases/claude_code_index.txt`
- baseline state:
  - context units: `3`
  - empty-ref context units: `3`
  - question-inducing candidates: `0`
  - naming survives but support structure weak
  - pivot / compression remain ungrounded

## 3. pointer intervention

- mode: `nearest_top_window`
- support:
  - direct candidate ref가 없을 때, `purpose_synthesis top_windows`에서 object-overlap이 있는 window를 fallback evidence pointer로 연결
- unchanged:
  - segmentation output
  - heading logic
  - object naming logic

## 4. after pointer stabilization

- context units: `3`
- empty-ref context units:
  - before: `3`
  - after: `0`
- grounding_status:
  - `fallback_grounded`: `3`
  - `direct_grounded`: `0`
- pointer_support_source:
  - `purpose_top_windows`: `3`
- question-inducing candidates:
  - before: `0`
  - after: `0`

## 5. comparison reading

### A. what actually recovered

- `empty-ref context unit` 문제는 줄었다
- context unit마다 최소 2개 수준의 evidence pointer가 붙었다
- `naming-without-support`는 `naming-with-fallback-support` 수준으로는 완화됐다

### B. what did not recover

- stable question-inducing candidate는 여전히 `0`
- pivot / compression은 이름은 유지되지만 여전히 direct evidence 기반이라고 보기 어렵다
- relation movement와 question opening 태도는 살아 있으나, grounding의 질은 아직 fallback 수준이다

### C. why this still matters

- segmentation만으로는 `이름은 있는데 ref가 없음` 문제가 남았고
- pointer stabilization은 그 문제를 줄이는 데 실제로 도움이 됐다
- 따라서 pointer는 2순위가 아니라, segmentation 다음의 직접적인 grounding 축이라는 점이 더 선명해졌다

## 6. verdict

- pointer stabilization only recovered:
  - empty-ref reduction
  - evidence pointer coverage
  - better-supported hold
- pointer stabilization did not recover:
  - direct grounding
  - stable question seed generation
  - robust pivot / compression support
- why heading is still 3rd:
  - role interpretation failure는 남아 있지만, reusable attitude의 생존과 grounding에는 pointer가 더 직접적으로 영향을 줬다
- why object lift remains hold:
  - grounding은 조금 회복됐지만 전부 fallback이다
  - direct candidate support와 cross-domain stability는 여전히 부족하다

## 7. one-line summary

> pointer stabilization은 `claude_code_index`에서 empty-ref context unit을 실제로 줄였고 grounding coverage를 늘렸지만, direct question-seed / pivot / compression support까지 회복시키진 못했기 때문에 object lift hold는 그대로 유지된다.
