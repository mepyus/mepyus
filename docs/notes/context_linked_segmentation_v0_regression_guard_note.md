# context linked segmentation v0 regression guard note

## verdict

- regression guard is locked as a documentation asset
- this turn does not change code
- current fully passing fixture state is fixed as the reference baseline

## baseline checkpoint

- 고정 기준 시점은 `reason priority patch -> termination patch -> termination exception patch` 이후다
- 이 기준 시점의 상태는 아래와 같다
  - 4개 fixture 전체 `match_rate = 1.00`
  - `overall_false_positive = []`
  - `overall_miss = []`
- 앞으로의 patch는 이 상태를 깨지 않는지 먼저 확인해야 한다

## fixture list

- `dialogue_continuation`
- `explanatory_mechanism`
- `argument_contrast`
- `mixed_document`

## expected links

### dialogue_continuation

- `dlg_001 -> dlg_002` / `speaker_continuation`

### explanatory_mechanism

- `exp_001 -> exp_002` / `setup_to_mechanism`
- `exp_002 -> exp_003` / `causal_chain`

### argument_contrast

- `arg_001 -> arg_002` / `unfinished_claim`
- `arg_002 -> arg_003` / `contrast_pair`

### mixed_document

- `mix_001 -> mix_002` / `answer_completion`
- `mix_002 -> mix_003` / `causal_chain`
- `mix_003 -> mix_004` / `contrast_pair`
- `mix_004 -> mix_005` / `causal_chain`

## regression criteria

아래 중 하나라도 발생하면 regression으로 본다.

- 어떤 fixture든 `match_rate`가 `1.00` 아래로 떨어질 때
- 기존 expected link가 `miss`로 재등장할 때
- 이전에 제거된 false positive가 다시 등장할 때
- `overall_false_positive`가 비어 있지 않을 때
- `overall_miss`가 비어 있지 않을 때

## execution path

- regression 기준 스크립트는 [scripts/run_context_linked_segmentation_exception_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_context_linked_segmentation_exception_validation.py) 로 고정한다
- 이 스크립트는 전체 fixture를 재실행하고
  - recovered target
  - false positive regression
  - all false positive
  - all miss
  를 함께 확인한다

## fixture addition rules

- 새 fixture는 기존 4개 fixture로 잡히지 않는 새 failure class가 생겼을 때만 추가한다
- 새 fixture는 기존 baseline을 설명하지 못하는 새 구조적 패턴을 다룰 때만 추가한다
- 기존 fixture는 wording 유지가 우선이다
- 기존 fixture를 수정하는 것은 아래 경우가 아니면 금지한다
  - fixture 자체가 현재 spec과 모순되는 경우
  - segment id 또는 expected link가 명백한 문서 오기인 경우
- 단순히 새 heuristic에 맞추기 위해 기존 fixture를 바꾸면 안 된다

## TBD items

- fixture를 파일 기반으로 외부 분리할지 여부
- regression 결과를 CI 성격으로 고정할지 여부
- fixture category tagging 표면 추가 여부

