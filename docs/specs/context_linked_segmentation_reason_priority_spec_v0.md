# context linked segmentation reason priority spec v0

## verdict

- reason governance is locked as a spec asset
- this turn does not change implementation code
- current failure is fixed as a governance problem first, not a taxonomy expansion problem first

## technical summary

### what validation really showed

- validation 결과는 local pair detection 자체가 완전히 비어 있지는 않음을 보여줬다
- `dialogue_continuation`은 `1.00` match rate로 local pair detection이 동작했다
- 반면 `explanatory_mechanism`, `argument_contrast`, `mixed_document`는 각각 `0.50`, `0.50`, `0.25`로 낮았다
- 공통 병목은 첫 reason이 chain 전체를 오염시키는 contamination이다
- 따라서 현재 문제는 reason taxonomy 부족보다 reason priority, scope, break, chain boundary 부재에 더 가깝다

### reason class proposal

이 분류는 구현 taxonomy가 아니라 governance용 운영 분류 v0다.

1. `pair_local`
   - `answer_completion`
   - `contrast_pair`

2. `chain_extend`
   - `speaker_continuation`
   - `causal_chain`
   - `setup_to_mechanism`

3. `bridge_or_tentative`
   - `unfinished_claim`

### reason priority order

동시 감지 시 기본 우선순위는 아래 순서를 따른다.

1. `contrast_pair`
2. `causal_chain`
3. `speaker_continuation`
4. `answer_completion`
5. `setup_to_mechanism`
6. `unfinished_claim`

우선순위 근거:

- `contrast_pair`는 전환 marker가 명시될 때 구조적으로 강하다
- `causal_chain`은 인과 marker가 명시될 때 `answer_completion`보다 더 구체적이다
- `speaker_continuation`은 화자 연속이라는 강한 표면 단서가 있지만 내용 전환 marker를 이기지는 못한다
- `answer_completion`은 자주 과도 확장되므로 local scope로 묶어야 한다
- `setup_to_mechanism`은 설명 흐름에는 유용하지만 후속 강한 marker가 나오면 유지권을 잃어야 한다
- `unfinished_claim`은 bridge 성격이 강하므로 가장 약한 유지권을 가진다

### simultaneous detection rule

- 같은 pair에서 여러 reason이 동시에 감지되면 더 높은 우선순위 reason을 선택한다
- `pair_local`과 `chain_extend`가 충돌하면 우선 현재 pair에 더 구체적으로 표지된 reason을 택한다
- `bridge_or_tentative`는 더 강한 marker reason이 없을 때만 선택한다
- `unfinished_claim`은 임시 연결 권한만 가지며, 후속 pair에서 더 강한 reason이 감지되면 override될 수 있다
- `answer_completion`은 질문-응답 pair에서는 유효하지만 다음 pair까지 자동 유지되지 않는다

### scope rule

- `answer_completion`은 기본값 `1 pair local`로 잠근다
- `contrast_pair`는 인접 전환 우선 reason으로 본다
- `unfinished_claim`은 후속 강한 marker가 나오면 유지권을 잃는다
- `setup_to_mechanism`은 설명 전환까지만 유효하고, `contrast_pair` 또는 `causal_chain` marker가 나오면 재판정 대상이 된다
- `causal_chain`은 causal marker가 명시될 때 새 reason으로 승격될 수 있다
- `speaker_continuation`은 내용 전환 marker가 없는 경우에만 chain_extend 권한을 가진다

### chain separation conditions

- `contrast_pair` marker가 나오면 기존 `unfinished_claim` 또는 `setup_to_mechanism` chain을 끊을 수 있다
- `causal_chain` marker가 나오면 기존 `answer_completion` local scope를 끊고 새 chain 판단이 가능하다
- 첫 reason이 `pair_local`인데 다음 pair가 다른 strong marker를 보이면 chain을 reset한다
- 같은 speaker라도 `contrast` 또는 `causal` marker가 나타나면 continuation chain을 유지하지 않는다
- chain 내부에서 기대 reason class가 `pair_local -> chain_extend` 또는 `chain_extend -> pair_local`로 바뀌면 분리 후보로 본다
- mixed document에서는 첫 reason이 뒤쪽 전체 pair를 덮지 못하도록 reset 조건을 기본으로 둔다

### chain continuation conditions

- 같은 reason class가 연속 pair에서 반복되고 override marker가 없을 때
- `speaker_continuation`이 유지되며 내용 전환 marker가 없을 때
- `causal_chain`이 연속 causal marker로 이어질 때
- `setup_to_mechanism` 뒤에 mechanism 설명이 이어지고 contrast/causal override가 없을 때
- continuation은 기본적으로 reset 가능 상태이며, 영구 유지권을 갖지 않는다

### max chain length

- max chain length hard cap is `TBD`
- v0 governance 원칙은 길이 상한보다 break condition 우선이다

### scope of change

- 이 spec은 `context_linked_segmentation_v0`의 reason governance 기준만 잠근다
- 다음 구현 변경이 열릴 범위는 아래에 한정한다
- priority table
- simultaneous detection selection rule
- break condition
- chain reset rule
- 이 spec은 heuristic 추가, scoring tuning, merge algorithm 확장을 바로 승인하지 않는다

### TBD items

- max chain length numeric cap
- pair-to-chain escalation exact thresholds
- 동일 pair에서 marker가 중복될 때의 tie-break 세부 규칙
- low-confidence downgrade 방식
- pair-level vs chain-level provenance expansion 방식

### what this is not

- this is not a code patch
- this is not a heuristic expansion pass
- this is not a scoring formula spec
- this is not a merge algorithm redesign
- this is not a multi-lens reading spec

## user-language summary

### what validation really showed

- 지금 문제는 reason 종류가 너무 적어서가 아니다
- 오히려 처음 잡힌 reason이 뒤쪽까지 너무 오래 남는 것이 핵심 병목이다
- 즉, detection보다 governance가 먼저 비어 있다

### reason class proposal

- `answer_completion`, `contrast_pair`는 짧게 쓰는 pair-local reason이다
- `speaker_continuation`, `causal_chain`, `setup_to_mechanism`은 chain을 조금 더 이어갈 수 있는 reason이다
- `unfinished_claim`은 임시 다리 역할만 하는 약한 reason이다

### scope rule

- `answer_completion`은 한 pair까지만 기본 유효하다
- `unfinished_claim`은 더 강한 marker가 나오면 바로 유지권을 잃는다
- `setup_to_mechanism`도 후속 contrast/causal marker가 나오면 다시 판단해야 한다

### break / override rule

- contrast가 나오면 이전 setup/unfinished 흐름을 끊을 수 있다
- causal marker가 나오면 이전 local completion을 끊고 causal 판정이 올라올 수 있다
- mixed 문서에서는 첫 reason이 뒤 전체를 덮지 못하도록 reset 기준을 둔다

### next gate

- 다음 코드 변경은 이 spec에 잠긴 priority table, break condition, chain reset rule을 먼저 참조할 때만 연다

### user-language restatement

- 지금 잠근 핵심은 "reason을 더 늘리자"가 아니다
- 먼저 "어떤 reason이 얼마나 오래 유효한가"를 잠갔다
- 초기 reason contamination을 막는 기준이 먼저다

