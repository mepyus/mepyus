# context linked segmentation v0 termination patch note

## Purpose

이 note는 `answer_completion`과 `causal_chain`의 pair-local termination만 반영한
최소 patch 범위를 기록한다.

## Patch scope

- `_should_terminate_pair()`를 추가했다
- `answer_completion`은 direct answer처럼 보이지 않으면 pair 생성 또는 연장을 멈추게 했다
- `causal_chain`은 stage handoff이거나 다음 segment에 causal marker가 없으면 연장을 멈추게 했다
- 다른 reason termination은 이번 patch 범위 밖에 둔다

## _should_terminate_pair summary

- `answer_completion`
  - 현재 segment가 완결 문장이고 direct answer 확장처럼 보이지 않으면 종료
  - 다음 segment가 direct answer 확장처럼 보이지 않으면 종료

- `causal_chain`
  - 현재 segment가 stage handoff처럼 보이면 종료
  - 다음 segment에 causal marker가 없으면 종료

## Validation result

- 이전 target false positive
  - `dialogue_continuation`: `dlg_003 -> dlg_004` / `answer_completion`
  - `explanatory_mechanism`: `exp_003 -> exp_004` / `causal_chain`
- patch 후 target false positive 제거 여부는
  `/tmp/context_linked_segmentation_termination_validation/termination_result.json`에 기록한다
- 실행 결과 두 target false positive는 모두 제거됐다
- 다만 새 miss가 생겼다
  - `explanatory_mechanism`: `exp_002 -> exp_003` / `causal_chain`
  - `mixed_document`: `mix_001 -> mix_002` / `answer_completion`
  - `mixed_document`: `mix_002 -> mix_003` / `causal_chain`
- 즉 termination patch는 target false positive 제거에는 성공했지만,
  일부 정상 pair까지 조기 종료시키는 부작용이 남아 있다

## TBD left untouched

- answer_completion 예외 continuation 세부 규칙
- causal_chain continuation 강도 판정 기준
- termination confidence 반영
- termination provenance 표면 확장

## Next step

다음 단계는 validation fixture를 유지한 채 termination 휴리스틱이 정상 사례를 해치지 않는지만 다시 좁게 보는 것이다.
