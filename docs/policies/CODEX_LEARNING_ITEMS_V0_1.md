[[A]] [[OBJ:codex_learning_items]] [[ROLE:engine]]

# Codex 추가 학습 항목 v0.1
# 부제: Replica 운영을 위해 Codex가 더 배워야 할 것

## 0. 목적

이 문서는 현재 Replica 구조 위에서
Codex가 앞으로 추가로 배워야 할 운영 감각과 점검 항목을 정리한 것이다.

핵심은 새 기능을 많이 아는 것이 아니다.

지금 더 필요한 학습은:
- 더 많이 구현하는 능력
보다
- 무엇을 남기고
- 무엇을 보류하고
- 무엇을 비교하고
- 왜 수정했는지 기록하는 운영 감각
이다.

즉 Codex는 이제부터
"코드를 만드는 기계"
보다
"흔적을 잃지 않게 누적하는 운영자"
쪽으로 더 학습해야 한다.

## 1. 최상위 판정

현재 Codex가 추가로 배워야 할 것은
새로운 복잡한 이론보다 아래와 같은 실전 운영 감각이다.

1. 분절 기준 학습
2. revision 이유 기록 학습
3. 안 붙은 것 / 보류된 것 기록 학습
4. shadow seed 운용 학습
5. fragment comparison 학습
6. cross-source 읽기 학습
7. 느린 승격 리듬 학습

## 2. 학습 항목 1 — 분절 기준 학습

분절은 단순 전처리가 아니라
Replica 전체 품질의 시작점이다.

Codex가 배워야 하는 것:
- 어디서 끊으면 의미가 살아남는가
- 어디서 끊으면 맥락이 찢어지는가
- 문장 경계와 의미 경계가 다를 때 무엇을 우선할 것인가
- 대화형 source와 문서형 source에서 분절 기준이 어떻게 달라지는가

운영 규칙:
- 기존 fragment를 덮어쓰기보다 alt_fragmentation으로 남긴다
- "더 좋아 보이는 분절"이 나오면 교체보다 비교 대상으로 남긴다
- fragment 경계는 결과가 아니라 실험 가능한 가설로 본다

## 3. 학습 항목 2 — revision 이유 기록 학습

값을 바꾸는 것보다
왜 바꿨는지를 남기는 것이 더 중요하다.

Codex가 배워야 하는 것:
- previous_value
- new_value
- reason
- operator
- revised_at

자주 남겨야 할 이유 유형:
- source.* 과잉
- semantic 과잉 일반화
- structural 부족
- fragment boundary 문제
- context 누락
- external signal 과대반응
- false resonance

## 4. 학습 항목 3 — 안 붙은 것 / 보류된 것 기록 학습

관계를 최소 3종으로 분리해서 본다:
- accepted_connection
- rejected_connection
- deferred_connection

기록해야 할 질문:
- 왜 안 붙였는가
- 무엇이 부족했는가
- 어떤 축에서는 가까웠는가
- 지금은 아니지만 나중에 다시 볼 가치가 있는가

## 5. 학습 항목 4 — shadow seed 운용 학습

seed는 정답 공급원이 아니라
공간이 무엇을 눈치채는지 보는 탐침이다.

Codex가 배워야 하는 것:
- shadow
- soft
- stable

운영 규칙:
- seed는 본문에 넣지 않는다
- ambient probe로만 먼저 붙인다
- 승격보다 보류를 더 잘해야 한다

## 6. 학습 항목 5 — fragment comparison 학습

두 fragment를 비교할 때 아래를 남긴다:
- similarity_reason
- difference_reason
- key divergence
- comparison_note
- operator
- compared_at

비교는 평가용이 아니라 경계 개선용이다.

## 7. 학습 항목 6 — cross-source 읽기 학습

Codex가 배워야 하는 것:
- source type이 달라도 반복되는 object/semantic/structural을 보는 법
- 낮은 연결성 상태를 바로 버리지 않는 법
- 지금은 약하지만 나중에 살아날 수 있는 공통 패턴을 보류하는 법

운영 규칙:
- source type 차이를 이유로 바로 배제하지 않는다
- cross-source relation은 observation으로 먼저 둔다
- 강한 current relation보다 약한 recurrent signal도 함께 본다

## 8. 학습 항목 7 — 느린 승격 리듬 학습

아래 리듬을 버티는 것이 더 중요하다:
- 먼저 받기
- fragment로 남기기
- current/history/observation 분리하기
- 반복 보기
- 나중에 승격하기

운영 규칙:
- fast conclusion보다 slow accumulation 우선
- 승격보다 추적을 먼저
- 안정된 반복 없이는 stable 선언 금지

## 9. 우선순위 잠금

### P0
1. 분절 기준
2. revision 이유 기록
3. 안 붙은 것 / 보류된 것 기록

### P1
4. shadow seed 운용
5. fragment comparison

### P2
6. cross-source 읽기
7. 느린 승격 리듬

## 10. Codex 전용 실천 규칙

- 새 값을 만들기 전에 기존 흔적과 history가 남는지 먼저 본다
- 수정했으면 반드시 이유를 적는다
- 안 붙은 관계도 observation으로 남긴다
- seed는 빨리 올리지 않는다
- 비슷한 fragment를 보면 비교 기록을 남긴다
- source가 다르다고 바로 버리지 않는다
- 반복과 공명이 충분할 때까지 stable을 아낀다

## 11. 하지 말아야 할 것

- 분절 실패를 조용히 덮어쓰기
- reason 없는 revision
- accepted relation만 저장하기
- seed를 본문이나 primary에 바로 섞기
- source_type이 다르다는 이유로 바로 배제하기
- observation을 current처럼 선언하기
- 반복 확인 없이 stable로 승격하기

## 12. 최종 한 줄 정리

Codex가 앞으로 더 배워야 할 것은
새 기능보다
분절 / 수정이유 / 보류 / 그림자 seed / 비교 / cross-source 읽기 / 느린 승격
같은 운영 감각이며,
이 학습이 쌓여야 Replica가 값 저장소가 아니라
사용자 방식에 맞는 흔적 축적 엔진으로 자라난다.
