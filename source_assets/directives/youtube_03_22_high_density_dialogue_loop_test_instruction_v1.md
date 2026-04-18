[[A]] [[OBJ:codex_directive_youtube_03_22_high_density_dialogue_loop_test_v1]] [[SEM:loop_test_for_object_layer_relation_question_intent_on_high_density_dialogue_asset]]

# CODEx 지시서 — youtube_03_22 기반 고밀도 대화 자산 반복 테스트

## 0. 목적

이번 턴의 목적은
`inputs/external_cases/youtube_03_22.md`
를 대상으로

- 분절
- 의미 파악
- 층위 파악
- 관계 라인 체크
- 질문 의도 적합 문단 탐색
- residue 간섭 확인

을 반복 테스트할 수 있는
**bash loop 기반 실험 구조**를 만드는 것이다.

중요:
이 작업은 한 번의 분석으로 끝나는 probe가 아니다.

이번 작업은 앞으로 유사한 대화 자산에도 반복 적용될 수 있도록
**반복 가능한 테스트 파이프라인**으로 설계해야 한다.

---

## 1. 한 줄 최종 지시

> **`youtube_03_22.md`를 대상으로 bash loop 기반 반복 실험 구조를 만들고, 우리 엔진이 대화 속 객체·층위·관계·질문 의도를 실제로 읽어낼 수 있는지 검증하는 고밀도 테스트 자산 파이프라인으로 실행하라.**
