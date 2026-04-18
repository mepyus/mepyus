[[A]] [[OBJ:second_order_comparison_domain_preparation_v1]] [[SEM:prepare_one_non_ai_dialogue_domain_for_second_order_comparison]]

# second-order comparison domain preparation v1

## 1. purpose

- 이번 문서의 목적은 비교용 새 도메인을 “잘 읽는 것”이 아니라, 무엇이 유지되고 무엇이 깨지는지 볼 준비를 하는 것이다.

## 2. preferred candidate

- preferred_input_asset: `inputs/external_cases/claude_code_index.txt`

## 3. why this candidate

- 현재 AI/에이전트 대화와 충분히 다른 축을 가진다.
- 그래도 기술 설명형 구조와 작업 흐름이 있어 2차 보정 태도를 시험하기 좋다.
- `question seed`, `pivot`, `context unit`, `role shift` 같은 판독이 완전히 무너지지 않는지 보기 위한 비교 도메인으로 적절하다.

## 4. what to observe

- question seed 유지 여부
- pivot 감각 유지 여부
- context unit 재구성 가능 여부
- role interpretation 변화
- residue 처리 방식 변화
- AI 특화 객체명 붕괴 여부
- 그 아래 판독 태도 유지 여부

## 5. what should stay stable

- 1차는 센서값, 2차는 재독해 결과라는 관점
- 같은 자산을 여러 눈으로 읽는 재독해 루프
- candidate / hold / promote 운영 태도
- role shift / question opening / relation movement를 본다는 보정 태도

## 6. what may change

- 중요한 객체 이름
- 중요한 question opening 유형
- pivot가 발생하는 맥락
- residue가 summary를 흐리는 방식

## 7. one-line summary

> 비교 도메인 1순위는 `claude_code_index.txt`이며, 목표는 잘 읽는 것이 아니라 AI 특화 객체명이 깨져도 2차 보정 태도가 유지되는지 확인하는 것이다.
