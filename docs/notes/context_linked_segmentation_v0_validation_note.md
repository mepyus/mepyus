# context linked segmentation v0 validation note

## Purpose

이 note는 `context_linked_segmentation_v0` 휴리스틱이
여러 문서 유형에서 얼마나 일반화되는지 얕게 확인한 결과를 남긴다.

이번 pass의 목적은 휴리스틱 수정이 아니라
오탐과 누락 패턴 관찰이다.

## Fixture types and intent

- 대화형
  - 같은 화자 연속 발화에서 `speaker_continuation`이 붙는지 확인
- 설명형
  - 설명 다음 메커니즘, 그리고 원인-결과 연결이 `setup_to_mechanism`과 `causal_chain`으로 잡히는지 확인
- 논증형
  - 미완 주장과 대비 전환이 `unfinished_claim`과 `contrast_pair`로 잡히는지 확인
- 혼합형
  - 질문-응답, 인과, 대비가 섞일 때 어느 부분이 오탐/누락되는지 확인

## Execution result summary

- validation 스크립트는 `/tmp/context_linked_segmentation_validation/validation_result.json`을 생성한다
- fixture별 expected vs actual linkage를 pair 단위로 비교한다
- match, miss, false_positive를 fixture별로 남긴다
- fixture별 match rate는 아래와 같다
- `dialogue_continuation`: `1.00`
- `explanatory_mechanism`: `0.50`
- `argument_contrast`: `0.50`
- `mixed_document`: `0.25`

## Observed pattern summary

- 현재 휴리스틱은 순차 병합이라 한 번 묶이기 시작하면 같은 그룹 안에서 reason이 고정될 수 있다
- 그 결과 뒤쪽 pair에서 다른 linkage reason이 기대돼도 앞쪽 reason으로 눌릴 수 있다
- 질문-응답과 미완 주장 같은 초반 reason이 후속 contrast나 causal pair를 덮을 가능성이 있다
- `speaker_continuation`은 다른 reason보다 뒤에 평가돼, 앞 규칙이 먼저 잡히면 누락될 수 있다
- 실제 결과에서는 `setup_to_mechanism`, `unfinished_claim`, `answer_completion`이 시작점 reason으로 잡힌 뒤
  같은 그룹 내부의 후속 pair reason을 덮는 오탐이 반복됐다
- `mixed_document`는 첫 질문-응답 pair 이후 전 구간이 `answer_completion`으로 유지돼
  `causal_chain`과 `contrast_pair` 기대 링크를 놓쳤다

## Heuristic limits

- pair별 reason 재평가가 아니라 group 첫 reason 유지에 가깝다
- 복수 linkage reason 우선순위 규칙이 아직 없다
- long chain 안에서 중간 전환이 생겨도 분리되지 않을 수 있다
- 이 한계들은 이번 턴에 수정하지 않는다

## Next step

다음 단계는 validation 결과를 기준으로 reason 우선순위와 chain 분리 기준만 문서로 먼저 좁히는 것이다.
