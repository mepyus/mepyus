# ACTUAL_MULTI_AGENT_SPACE_EXPLORATION_LOOP_DESIGN_V0

status: HERMES_EXECUTED_WITH_HOLD

## 목적

사용자 지시를 VectorFL의 대상(content)으로만 처리하지 않고, Hermes 자신의 처리 절차를 VectorFL처럼 구성한다.

## 실제 참여

- Hermes: 원본 해석, 비교, merge, 실행 산출물 생성
- Codex: 실제 CLI로 공간 evidence 탐색
- Gemini: 실제 CLI로 공간 층위/압력/해석 수준 읽기

## 설계 루프

1. raw user original 보존
2. Hermes 1차 intent/boundary 해석
3. Codex read-only spatial exploration
4. Gemini layer reading
5. Hermes comparison: original vs Codex space vs Gemini layer
6. Hermes merge: original+space+model/layer interpretation
7. Hermes execution: this design/receipt/trace
8. Codex reinsertion review: 이 산출물이 공간에 들어가면 무엇이 바뀌는지
9. Gemini post-merge layer reading: 재투입 후 층위/압력 변화 읽기

## 방향

fixture 최소루프에서 actual multi-agent processing loop로 전환.
목표는 "VectorFL을 설명하는 산출물"이 아니라 "VectorFL 방식으로 처리된 산출물"을 공간에 되돌리는 것.

## HOLD

이 파일은 evidence/reentry material이다. authority, registry, current-position apply, Program Alpha promotion이 아니다.
