[[A]] [[OBJ:codex_directive_question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1]] [[SEM:promote_question_inducing_blocks_and_deprioritize_interview_residue_after_high_density_dialogue_success]]

# CODEx 지시서 — 질문 유도 문단 승격 + summary-stage 후순위화 검토

## 0. 목적

이번 턴의 목적은 `youtube_03_22.md` 반복 실험 결과를 바탕으로,
다음 bounded refinement를 수행하는 것이다.

핵심은 두 가지다.

1. 질문 유도력이 강한 문단/윈도우를 별도 candidate로 검토한다
2. interview/dialogue residue를 hard suppression 하지 않고 summary-stage에서 뒤로 미룰 후보만 정리한다

즉 이번 턴은
- axis 수정 턴이 아니다
- ontology/general law 승격 턴이 아니다
- residue hard suppression 턴이 아니다
- 사전류/백과사전류 투입 턴이 아니다

오직
**question-inducing block candidate review + summary-stage deprioritization review**
턴이다.

## 1. 작업 원칙

- 질문 유도 candidate는 정답 문단이 아니라 다음 탐색을 여는 응축핵 후보로 본다
- residue는 삭제하지 않고 opening summary / user-facing gloss 선두에서만 후순위 후보로 본다
- broad probe 안정성은 흔들지 않는다
- local success를 바로 일반 구조로 승격하지 않는다

## 2. 최소 산출물

- report:
  - `docs/reports/question_inducing_block_promotion_and_summary_stage_deprioritization_review_v1.md`
- candidate output:
  - `app/work/dialogue_loop_test/generated/question_inducing_block_candidates_*.json`
- runtime evidence:
  - delta latest
  - raw log
  - receipt

## 3. 한 줄 최종 지시

> `youtube_03_22.md` 반복 실험 결과를 바탕으로, 다음 탐색을 여는 question-inducing block candidate를 선별하고, interview/dialogue류 residue를 hard suppression 하지 않은 채 summary-stage 후순위화 후보로 정리하여 user-layer opening을 더 선명하게 만드는 bounded refinement를 수행하라.
