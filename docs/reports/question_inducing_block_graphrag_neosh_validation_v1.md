[[A]] [[OBJ:question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1]] [[SEM:bounded_refinement_for_question_inducing_dialogue_blocks_and_summary_priority_shift]]

# question-inducing block promotion and summary-stage deprioritization review v1

## 1. input

- input_asset: `inputs/external_cases/graphrag_neosh.txt`
- probe_files:
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_segmentation_probe_v1_w3_s1_20260328T104511Z.json`
  - `app/work/dialogue_loop_test/generated/graphrag_neosh_segmentation_probe_v1_w6_s3_20260328T104511Z.json`

## 2. top-level verdict

- status: `HOLD`
- one-line verdict: high-score window는 있으나 질문 유도 block candidate 경계가 충분히 선명하지 않다.

## 3. question-inducing block candidates


## 4. why these are not just high-score summary blocks

- 이 블록들은 객체가 2개 이상 같이 살아남고, 질문 생성 힌트와 전이/실행 이동 힌트를 같이 갖는다.
- 따라서 단순 요약 density가 아니라 다음 탐색을 여는 응축핵 후보로 읽을 수 있다.
- 특히 `Bundle-Unbundle`, `기존 사업자의 UX 마찰`, `적응 경쟁`, `RLVR/CUA` 계열은 미래 담론을 전략/실행/검증 질문으로 끌어내린다.

## 5. summary-stage deprioritization candidates


## 6. before / after reading


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
