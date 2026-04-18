[[A]] [[OBJ:codex_directive]] [[SEM:interview_case_renamed_engine_internal_test_v1]]

# CODEx 지시서 — 인터뷰 3건 이름 변형 internal engine test v1

## 0. 목적
이번 턴의 목적은 새 기준을 만드는 것이 아니다.

이미 처리된 인터뷰 3건을
이름 힌트를 줄인 복제본으로 다시 넣어,
Codex의 수동 first-pass 도움 없이
엔진 내부 경로가 자료를 어떻게 나누는지 확인한다.

테스트 원문:
- `inputs/external_cases/dario_amodei_youtube.txt`
- `inputs/external_cases/andrej_karpathy_youtube.txt`
- `inputs/external_cases/alexkarp_youtube.txt`

테스트용 이름 변형본:
- `app/work/middle_layer_experiments/input_variants/interview_case_alpha.txt`
- `app/work/middle_layer_experiments/input_variants/interview_case_beta.txt`
- `app/work/middle_layer_experiments/input_variants/interview_case_gamma.txt`

## 1. 핵심 질문
- 이름 힌트를 줄여도 raw path는 여전히 `review / compare`로 평평해지는가?
- 이름 힌트를 줄여도 middle layer packet은 case-specific dominant role mix를 유지하는가?
- 즉 현재 분화가 파일명 힌트보다 내용 기반 신호에 더 기대는가?

## 2. 실행 원칙
- canonical 원문은 건드리지 않는다
- 테스트용 복제본은 work 영역에서만 다룬다
- 수동 first-pass는 추가하지 않는다
- raw probe와 middle-layer probe만 다시 실행한다
- current asset map은 갱신하지 않는다
- delta는 필요 시 짧게만 남긴다

## 3. 기대 판정
- raw path:
  - 여전히 generic discourse dominance와 flattening이 강할 가능성
- middle layer path:
  - 이름 변형과 무관하게 dominant role mix가 유지되면 내용 기반 분화가 작동하는 것으로 본다

## 4. 한 줄 잠금
> 이름 힌트를 줄인 인터뷰 복제본으로 raw와 middle-layer를 다시 돌려, 현재 분화가 파일명보다 내용 신호에 기대는지 bounded하게 검증한다.
