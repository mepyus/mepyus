# context linked segmentation v0 exception patch note

## Purpose

이 note는 `answer_completion`과 `causal_chain`의 termination exception만 반영한
최소 patch 범위를 기록한다.

## Patch scope

- `_should_terminate_pair()`에 exception 분기를 추가했다
- `answer_completion`은 pair 내부 question-answer closure가 직접 보이면 termination하지 않는다
- `causal_chain`은 현재 pair에 명시적 causal marker가 있고 stage handoff가 아니면 termination하지 않는다
- 다른 reason exception은 이번 patch 범위 밖에 둔다

## Exception logic summary

- `answer_completion`
  - 현재 pair가 질문 + 직접 답변 closure로 읽히면 termination보다 exception을 먼저 적용
  - 운영 문장, 메타 설명, stage handoff는 exception을 무효화

- `causal_chain`
  - 현재 pair에 causal marker가 있으면 continuation exception을 먼저 검토
  - stage handoff나 메타 안내는 exception을 무효화

## Validation result

- 이전 miss target
  - `explanatory_mechanism`: `exp_002 -> exp_003` / `causal_chain`
  - `mixed_document`: `mix_001 -> mix_002` / `answer_completion`
  - `mixed_document`: `mix_002 -> mix_003` / `causal_chain`
- 기존 false positive guard
  - `dialogue_continuation`: `dlg_003 -> dlg_004` / `answer_completion`
  - `explanatory_mechanism`: `exp_003 -> exp_004` / `causal_chain`
- 결과는 `/tmp/context_linked_segmentation_exception_validation/exception_result.json`에 기록한다
- 실행 결과 target miss 세 개는 모두 회복됐다
- 기존 false positive guard 두 개도 재발하지 않았다
- 현재 validation fixture 기준 miss와 false positive는 모두 없다

## TBD left untouched

- direct answer closure 세부 lexical rule
- causal continuation 강도 판정 세부 규칙
- exception과 priority 충돌 tie-break
- exception 결과의 confidence 반영

## Next step

다음 단계는 남은 miss나 false positive가 있으면 exception boundary를 다시 좁게 읽는 것이다.
