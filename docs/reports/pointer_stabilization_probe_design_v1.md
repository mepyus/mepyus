[[A]] [[OBJ:pointer_stabilization_probe_design_v1]] [[SEM:minimal_pointer_support_design_after_segmentation_probe]]

# pointer stabilization probe design v1

## 1. purpose

- 이번 설계의 목적은 `claude_code_index.txt`에서 segmentation support 이후에도 남아 있던 grounding/ref 계열 문제를 pointer 축에서 최소 개입으로 검증하는 것이다.
- 즉 이 문서는 새 anchor system 설계가 아니라, `empty-ref / weak grounding / naming-without-support`를 줄일 수 있는지 보는 얇은 support 설계 문서다.

## 2. remaining baseline problems after segmentation support

- `present_window_refs` remained empty across all context units
- `question_inducing_candidates` remained `0`
- `pivot / compression` stayed effectively ungrounded
- naming survived, but support structure still weak

## 3. minimal intervention

- intervention_name: `nearest_top_window pointer stitching`
- source:
  - already generated `purpose_synthesis top_windows`
- target:
  - context unit candidates in multi-pass rereading
- rule:
  - direct question-inducing candidate ref가 있으면 그대로 사용
  - direct ref가 없으면, context unit의 center objects와 가장 많이 겹치는 `purpose top_windows`를 fallback evidence pointer로 연결

## 4. why this is minimal

- splitter를 다시 건드리지 않는다
- heading 규칙을 새로 늘리지 않는다
- object naming을 새로 만들지 않는다
- 이미 살아난 window diversity와 existing top windows만 재활용한다

## 5. why this is not evidence fabrication

- pointer는 새로 발명하지 않는다
- 이미 생성된 segmentation-support probe의 top windows 중 object overlap이 있는 window만 evidence fallback으로 쓴다
- 따라서 이번 개입은 `없는 ref를 만드는 것`이 아니라 `이미 살아 있는 window surface를 context unit과 다시 연결하는 것`이다

## 6. expected read

- expected_recovery:
  - empty-ref context unit 감소
  - evidence pointer coverage 증가
  - naming-with-support 약간 회복
- not_expected:
  - question-inducing candidate 자체의 대폭 회복
  - pivot / compression의 direct grounding 완성
  - object lift hold 해제

## 7. one-line summary

> pointer probe는 segmentation support로 회복된 window diversity를 context unit grounding에 다시 묶는 최소 stitching 실험이며, evidence fabrication 없이 empty-ref를 줄일 수 있는지 검증하는 단계다.
