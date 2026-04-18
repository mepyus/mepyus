# context linked segmentation validation reading handoff v0

## verdict

- validation reading is locked as handoff note
- no implementation change is included in this turn
- next coding gate stays closed until reason governance is referenced

## technical summary

### what validation really showed

- `dialogue_continuation`은 local pair detection이 살아 있음을 보여줬다
- `explanatory_mechanism`과 `argument_contrast`는 후속 reason 전환이 약했다
- `mixed_document`는 첫 `answer_completion`이 뒤쪽 전 pair를 덮어 contamination이 가장 심했다
- 따라서 핵심 병목은 heuristic absence보다 reason governance absence다

### reason class proposal

- `pair_local`
  - `answer_completion`
  - `contrast_pair`
- `chain_extend`
  - `speaker_continuation`
  - `causal_chain`
  - `setup_to_mechanism`
- `bridge_or_tentative`
  - `unfinished_claim`

이 구분은 구현 taxonomy가 아니라 v0 운영 분류다.

### scope rule

- `answer_completion`은 local pair 기본값으로 본다
- `contrast_pair`는 인접 전환 우선 reason으로 읽는다
- `unfinished_claim`은 후속 강한 marker 앞에서 유지권을 잃는다
- `setup_to_mechanism`은 설명 전환까지만 유효하고 후속 강한 marker 앞에서 재판정 대상이 된다
- `causal_chain`은 causal marker가 명시될 때 새 reason으로 올라올 수 있다

### break / override rule

- contrast marker는 기존 `unfinished_claim` / `setup_to_mechanism` 계열을 끊을 수 있다
- causal marker는 기존 local completion을 끊고 causal 판정을 열 수 있다
- mixed document에서는 첫 reason이 전체 뒤를 덮지 못하도록 reset 조건을 둔다
- same speaker continuation은 내용 전환 marker를 이기지 못한다

### validation reading by fixture

- `dialogue_continuation`
  - local pair detection은 동작했다
  - 다만 질문 뒤 서술이 별도 false positive로 잡혔다

- `explanatory_mechanism`
  - 시작점 `setup_to_mechanism`은 감지됐지만
  - 뒤쪽 `causal_chain`으로 전환하지 못했다

- `argument_contrast`
  - 시작점 `unfinished_claim`은 감지됐지만
  - 뒤쪽 `contrast_pair` 전환이 눌렸다

- `mixed_document`
  - 첫 `answer_completion`이 가장 넓게 contamination을 일으켰다
  - 뒤쪽 `causal_chain`과 `contrast_pair`가 모두 눌렸다

### non-goals

- no code patch
- no heuristic addition
- no scoring formula change
- no merge logic change
- no fixture expansion

### next gate

- 다음 코드 수정은 아래 세 가지가 참조될 때만 연다
- priority table
- break condition
- chain reset rule

## user-language summary

### what validation really showed

- 지금 문제는 reason을 못 찾는 게 아니라
- 먼저 찾은 reason을 언제 멈춰야 하는지 모르는 데 있다

### reason class proposal

- 짧게 쓰는 reason과 길게 이어질 수 있는 reason을 분리해 봐야 한다
- 그리고 `unfinished_claim`은 약한 임시 연결로 취급해야 한다

### break / override rule

- contrast나 causal 같은 더 강한 전환 표지가 나오면 앞 reason을 그대로 끌고 가지 말아야 한다
- 특히 `answer_completion`이 뒤 전체를 덮는 현상은 막아야 한다

### next gate

- 지금은 코드 수정보다 governance를 먼저 잠그는 것이 맞다
- 기준 없이 코드를 손대면 오탐만 다른 모양으로 이동할 가능성이 높다

### user-language restatement

- 이번 턴에서 잠근 핵심은 단순하다
- reason detection보다 reason governance가 먼저다
- 첫 reason contamination을 끊는 기준이 다음 구현 게이트다
