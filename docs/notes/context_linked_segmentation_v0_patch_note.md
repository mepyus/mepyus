# context linked segmentation v0 patch note

## Purpose

이 note는 `reason priority`와 `chain reset`만 반영한 최소 patch 범위를 기록한다.

이번 patch는 segmentation 알고리즘 확장이 아니라,
이미 잠긴 governance spec을 좁게 코드에 내리는 작업이다.

## Patch scope

- `REASON_PRIORITY` 상수를 추가했다
- `_select_reason()`을 추가해 동시 감지 시 우선순위 높은 reason을 고르게 했다
- `_should_reset_chain()`을 추가해 local scope와 reset 조건을 반영했다
- `link()`는 후속 pair 재판정을 위해 overlapping pair 재시작을 허용하는 쪽으로만 최소 수정했다

## REASON_PRIORITY

- `contrast_pair`
- `causal_chain`
- `speaker_continuation`
- `answer_completion`
- `setup_to_mechanism`
- `unfinished_claim`

## Reset conditions

- `answer_completion`은 1 pair 후 reset
- `contrast_pair`는 pair-local로 두고 다음 pair에서 reset
- `unfinished_claim`은 후속 `contrast_pair` 또는 `causal_chain` 앞에서 reset
- `setup_to_mechanism`은 후속 `contrast_pair` 또는 `causal_chain` 앞에서 reset
- `speaker_continuation`은 후속 strong discourse marker를 이기지 못한다

## Validation change summary

- validation 비교는 `/tmp/context_linked_segmentation_patch_validation/comparison_result.json`에 남긴다
- fixture별 before/after match rate를 비교한다
- 남은 false positive와 miss도 그대로 남긴다
- before/after match rate는 아래와 같다
- `dialogue_continuation`: `1.00 -> 1.00`
- `explanatory_mechanism`: `0.50 -> 1.00`
- `argument_contrast`: `0.50 -> 1.00`
- `mixed_document`: `0.25 -> 1.00`
- 현재 남은 false positive는 `dialogue_continuation`의 질문-응답 pair와
  `explanatory_mechanism`의 `exp_003 -> exp_004` causal 확장이다
- 현재 miss는 없다

## TBD left untouched

- max chain length numeric cap
- pair-to-chain escalation exact thresholds
- tie-break 세부 규칙
- low-confidence downgrade 방식

## Next step

다음 단계는 patch 후에도 남는 false positive를 기준으로 pair-local output contract를 더 명확히 좁히는 것이다.
