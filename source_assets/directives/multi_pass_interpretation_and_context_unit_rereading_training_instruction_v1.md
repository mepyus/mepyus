[[A]] [[OBJ:codex_directive_multi_pass_interpretation_and_context_unit_rereading_training_v1]] [[SEM:train_codex_to_learn_user_thinking_from_same_asset_by_repeated_reinterpretation]]

# CODEx 지시서 — 다중 해석 레이어 반복 판독 + 맥락 단위 재독해 훈련

## 0. 목적

이번 턴의 목적은 `youtube_03_22.md`를 다시 읽되,
단순 분절/요약을 반복하는 것이 아니다.

이번 작업의 목적은 아래다.

1. 같은 자산을 서로 다른 해석 레이어로 2회 이상 다시 읽는다
2. 각 해석 결과를 리포트로 남긴다
3. 그 리포트 차이를 바탕으로, 원래 문단이 아니라 맥락 단위(context unit)를 다시 세운다
4. 그 맥락 단위를 템플릿 기준으로 재해석한다
5. 이 과정을 통해 Codex가 사용자의 의미 층위 감각과 질문 방식을 학습하도록 한다

즉 이번 작업은
- 최종 철학 추출 아님
- 정답 문장 도출 아님
- 일반화 잠금 아님

오직
**해석 감각 학습 훈련**
턴이다.

## 1. 작업 원칙

- 같은 자산을 다른 눈으로 읽는 차이를 남긴다
- 우열 판정보다 시야 차이를 기록한다
- context unit은 문단보다 더 살아 있는 맥락 단위일 수 있다고 가정한다
- 템플릿은 정리 양식이 아니라 읽기 장치로 사용한다
- broad/general 법칙으로 승격하지 않는다

## 2. 최소 산출물

- report:
  - `docs/reports/multi_pass_interpretation_and_context_unit_rereading_training_v1.md`
- generated:
  - `app/work/dialogue_loop_test/generated/multi_pass_interpretation_training_*.json`
  - `app/work/dialogue_loop_test/generated/context_unit_candidates_*.json`
- runtime evidence:
  - delta latest
  - raw log
  - receipt

## 3. 한 줄 최종 지시

> `youtube_03_22.md`를 여러 해석 레이어로 반복 판독하고, 그 결과 차이를 바탕으로 문단이 아닌 맥락 단위를 다시 세운 뒤, 템플릿 기준으로 재해석하여 Codex가 사용자의 의미 층위 감각과 질문 방식을 학습하는 훈련을 수행하라.
