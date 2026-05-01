# Question Interpretation Contract v0

## Purpose

사용자 질문을 바로 검색하지 않고 탐색 가능한 작업 packet으로 번역한다.

## Execution

Every question interpretation packet must include:

- `user_request_raw`
- `interpreted_goal`
- `task_mode`
- `scope`
- `constraints`
- `expected_output_shape`
- `search_targets`
- `external_reasoning_needed`
- `merge_mode_candidate`
- `ambiguity_notes`
- `hold_reason_if_any`

Allowed `task_mode` values:

- `exploration`
- `extraction`
- `comparison`
- `merge`
- `verification`
- `reflection_support`

Ambiguity handling:

- `provisional`: 진행 가능한 약한 해석. packet에 note를 남기고 탐색한다.
- `hard_hold`: 사용자 고유 판단, authority conflict, destructive action 등으로 진행 불가.
- `none`: 해석상 큰 모호성이 없음.

## Interpretation

retrieval 전에 interpretation이 먼저여야 하는 이유는 검색어가 곧 질문의 의미가 아니기 때문이다. 사용자의 질문은 흔히 대상, 권위층, 기대 산출물, 보류 조건, merge 방식이 섞여 있다. 이를 packet으로 바꾸면 탐색은 "관련 파일 찾기"가 아니라 "이 목표에 필요한 근거 회수"가 된다.

질문을 하나의 답 매칭으로 처리하면 공간 숙성 기반과 어긋난다. Phase 1에서 중요한 것은 답 하나가 아니라 다음 질문에서 재사용 가능한 판단 구조다.

ambiguous한 질문을 즉시 되묻지 않고 provisional/hard hold로 나누는 이유는 대부분의 모호성은 진행하면서 좁힐 수 있기 때문이다. 사용자 결정이 필요한 경우만 멈추고, 나머지는 `PROVISIONAL`로 흔적을 남긴다.

## Validation

- 한 질문을 안정적으로 packet으로 바꿀 수 있다.
- 탐색형/비교형/병합형/검증형이 구분된다.
- packet의 `search_targets`는 Stage 3 exploration contract로 바로 전달된다.
- hard hold는 stop condition에 한정된다.

## Stage 2 Closeout

- Verdict: `PASS`
- Files created: `docs/specs/question_interpretation_contract_v0.md`, `runtime/contracts/question_interpretation_packet_v0.json`, `docs/guides/question_mode_examples_for_codex_v0.md`
- Example packets: `docs/guides/question_mode_examples_for_codex_v0.md` 참조
- Open ambiguities: naming lock은 아직 v0 provisional이다.
- Entry condition for next stage: packet을 기준으로 evidence bundle을 만들 수 있다.
