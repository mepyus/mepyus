[[A]] [[OBJ:question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1]] [[SEM:bounded_refinement_for_question_inducing_dialogue_blocks_and_summary_priority_shift]]

# question-inducing block promotion and summary-stage deprioritization review v1

## 1. input

- input_asset: `inputs/external_cases/claude_code_index.txt`
- probe_files:
- `app/work/dialogue_loop_test/generated/claude_code_index_dialogue_loop_test_w3_s1_20260328T093821Z.json`
- `app/work/dialogue_loop_test/generated/claude_code_index_dialogue_loop_test_w6_s3_20260328T093821Z.json`

## 2. top-level verdict

- status: `PASS_WITH_NOTE`
- one-line verdict: 질문 유도 block candidate는 선명하게 보였고 summary-stage 후순위화 후보도 정리됐지만, 이 단계는 여전히 local bounded refinement이며 hard suppression이나 일반화 잠금 단계는 아니다.

## 3. question-inducing block candidates

- window `0_0` (`score=11`)
  - objects: 생산성/코딩, 에이전트 애플리케이션, 구현/자동화, 전략/방향성
  - layers: 설명/해석 층, 구현/실행 층, 검증/근거 층, 구조/연결 층
  - relation_hints: reinforcement_hint, contrast_hint, transition_hint, execution_shift_hint, specification_hint, question_generation_hint
  - why: 객체가 함께 살아남음: 생산성/코딩, 에이전트 애플리케이션, 구현/자동화 / 질문 생성 힌트가 직접 동반됨 / 설명에서 전략/실행 쪽으로 이동하는 전이가 보임
  - next_question: 기존 앱의 moat는 agent interface 시대에 무엇으로 남는가?
  - next_question: agent layer는 실제 workflow와 운영 구조를 어디까지 대체하는가?
  - block: `untitled`

## 4. why these are not just high-score summary blocks

- 이 블록들은 객체가 2개 이상 같이 살아남고, 질문 생성 힌트와 전이/실행 이동 힌트를 같이 갖는다.
- 따라서 단순 요약 density가 아니라 다음 탐색을 여는 응축핵 후보로 읽을 수 있다.
- 특히 `Bundle-Unbundle`, `기존 사업자의 UX 마찰`, `적응 경쟁`, `RLVR/CUA` 계열은 미래 담론을 전략/실행/검증 질문으로 끌어내린다.

## 5. summary-stage deprioritization candidates

- `discourse_connective_residue`
  - example_values: 그래서
  - why_not_hard_suppress: 문서 전체의 의미를 없애려는 것이 아니라 opening summary 선두에서만 뒤로 밀기 위한 후보이기 때문
  - why_summary_stage_only: 질문 유도 블록의 핵심 객체와 relation movement는 유지한 채, surface opening만 더 선명하게 하기 위함
- `conversational_filler_residue`
  - example_values: 저희가
  - why_not_hard_suppress: 문서 전체의 의미를 없애려는 것이 아니라 opening summary 선두에서만 뒤로 밀기 위한 후보이기 때문
  - why_summary_stage_only: 질문 유도 블록의 핵심 객체와 relation movement는 유지한 채, surface opening만 더 선명하게 하기 위함

## 6. before / after reading

- window `0_0`
  - existing_opening_summary: 주요 객체 후보: 생산성/코딩, 에이전트 애플리케이션, 구현/자동화 / 주요 층위: 설명/해석 층, 구현/실행 층, 검증/근거 층 / 관계 힌트: reinforcement_hint, contrast_hint, transition_hint
  - anchor_surface_before: 그래서, 이렇게, 있습니다, MCP, 저희가, 보겠습니다
  - anchor_surface_after: 이렇게, 있습니다, MCP, 보겠습니다, 들어서, 작업을
  - deprioritized_values: 그래서, 저희가

## 7. current interpretation

- 지금 필요한 건 residue 삭제가 아니라 summary 선두 우선순위 재배치다.
- 앞으로 올릴 것은 객체 후보, 질문 유도 block, 전략/실행/전이/질문 생성 힌트다.
- 뒤로 미룰 것은 connective, filler, 화자 반복 흔적, 너무 일반적인 추상어다.

## 8. next bounded step

- summary generation 단계에서만 residue-aware deprioritization을 시험하는 얇은 patch를 검토한다.
- broad concept probe 안정성은 유지한 채 dialogue 자산에만 국한된 surface adjustment로 제한한다.
- question-inducing block candidate를 page seed / object growth seed 후보로 다루는 로컬 실험을 이어갈 수 있다.

## 9. one-line summary

> `youtube_03_22.md`에서는 단순 high-score window가 아니라 다음 질문을 여는 question-inducing block candidate가 실제로 보였고, residue 문제는 삭제보다 summary-stage 후순위화로 다루는 것이 맞다는 점이 bounded하게 정리됐다.
