# mixed reentry observer stage2 spec

## 1. 목적

- mixed hold corridor를 더 많은 후속 입력에 대조해, 어떤 corridor가 반복적으로 재강화되는지 observer layer에서 누적 기록한다.

## 2. 현재 잠긴 계약

- mixed hold는 dead-end가 아니라 re-entry 가능한 corridor다.
- re-entry는 hold 가치를 강화할 수 있지만 곧바로 canonical promotion을 뜻하지 않는다.
- `stable_closure_reached` 가 반복 확인되기 전까지 observer evidence는 observer evidence로만 남긴다.

## 3. re-entry observer 입력

- baseline:
  - `app/work/mixed_reentry_probe_stage1/generated/*`
- observer inputs:
  - `references/vectorfl_next_gemini_session/youtube_exam.md`
  - `runtime/logs/work_sessions/session_20260318_180251.md`

## 4. corridor 정의

- corridor_id는 `transition_from -> transition_to :: anchor_group` 으로 묶는다.
- 이번 stage2는 corridor를 다음 세 축에서 본다.
  - `technical -> organization :: harness_agent`
  - `technical -> organization :: ai_business`
  - `technical -> business :: ai_business`

## 5. re-entry match 정의

- 같은 transition corridor가 observer input에서 다시 보이면 re-entry match 후보로 본다.
- 판정 기준:
  - arrival axis overlap
  - bridge support 존재
  - repeated anchor support
  - anchor family overlap

## 6. strength 단계

- `none`
- `weak`
- `meaningful`
- `strong`

이 단계는 설명 가능한 observer 등급이며 점수 모델이 아니다.

## 7. closure delta 단계

- `no_change`
- `anchor_only_reinforced`
- `arrival_axis_clearer`
- `closure_partially_strengthened`
- `near_canonical_but_not_promoted`
- `stable_closure_reached`

이번 stage2의 목적은 승격이 아니라 accumulation 확인이다.

## 8. 이번 턴 비목표

- 코어 로직 수정
- canonical promotion rule 추가
- mixed 자동 승격
- mixed/canonical 경계 규칙 변경

## 9. 성공 조건

- corridor_id 단위 누적 ledger가 생긴다.
- 강화되는 corridor와 정체되는 corridor가 분리된다.
- `technical -> organization` 과 `technical -> business` 의 누적 차이가 읽힌다.
- `stable_closure_reached` 가 여전히 없는지 보수적으로 확인된다.
