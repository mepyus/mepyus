# context linked segmentation pair local termination spec v0

## verdict

- pair-local termination is locked as a spec asset
- this turn does not change implementation code
- current remaining false positives are fixed as termination-governance gaps first

## problem diagnosis

patch 이후 validation에서 남은 false positive는 두 개다.

- `dialogue_continuation`: `dlg_003 -> dlg_004`가 `answer_completion`
- `explanatory_mechanism`: `exp_003 -> exp_004`가 `causal_chain`

이 두 사례는 reset 규칙이 전혀 없는 문제가 아니라,
특정 reason이 "이 pair에서 종료되어야 한다"는 pair-level termination 기준이
문서로 잠기지 않았다는 문제를 보여준다.

즉 현재 남은 병목은 chain reset의 부재보다,
pair-local reason 종료 시점 정의의 부재에 더 가깝다.

## technical summary

### reason termination classification

이 분류는 v0 termination governance 용도다.

1. `pair_local`
   - `answer_completion`
   - `contrast_pair`

2. `chain_capable`
   - `speaker_continuation`

3. `conditional`
   - `causal_chain`
   - `setup_to_mechanism`
   - `unfinished_claim`

분류 근거:

- `answer_completion`과 `contrast_pair`는 기본적으로 인접 pair 해석에 가깝다
- `speaker_continuation`은 여러 pair에 걸친 연속 가능성이 있다
- `causal_chain`, `setup_to_mechanism`, `unfinished_claim`은 chain 가능성이 있지만
  다음 pair의 구조 신호에 따라 종료될 수 있다

### answer_completion termination criteria

기본 원칙:

- `answer_completion`은 한 질문 pair를 닫는 local reason이다
- 다음 pair가 새 질문-응답 구조를 재확인하지 않으면 이어지지 않는다

termination 조건:

- 질문 segment가 이미 직후 segment에서 답을 얻었을 때
- 다음 pair가 다른 speaker 전환, 다른 discourse move, 다른 설명 단계로 넘어갈 때
- 다음 pair가 질문에 대한 직접 답변이 아니라 메타 설명, 후속 운영 문장, unrelated narration일 때
- 현재 answer pair의 두 번째 segment가 이미 완결 문장으로 닫힐 때

예외적으로 이어질 수 있는 경우:

- 다음 pair도 같은 질문에 대한 직접 답변 확장으로 명시될 때
- 다만 이 예외의 세부 판정 규칙은 `TBD`

현재 남은 false positive 해석:

- `dlg_003 -> dlg_004`는 형식상 질문 뒤 서술이지만,
  `dlg_004`는 직접 답변보다 별도 운영 서술에 가깝다
- 따라서 이 pair는 `answer_completion` 후보이더라도 termination 검토를 먼저 받아야 한다

### causal_chain termination criteria

기본 원칙:

- `causal_chain`은 causal marker 하나만으로 자동 연장되지 않는다
- 다음 pair가 같은 인과 흐름을 계속 증명할 때만 이어질 수 있다

termination 조건:

- 다음 segment가 이전 결과를 더 설명하지 않고 새 단계, 새 절차, 새 주제로 넘어갈 때
- causal marker가 한 pair에서만 인과를 닫고 다음 pair에 인과 단서가 반복되지 않을 때
- 다음 pair가 결과의 귀결이 아니라 단순 후속 문장, 전환 문장, stage handoff일 때
- 이전 pair의 causal relation이 이미 완결 문장으로 닫힐 때

continuation 조건:

- 다음 pair에도 명시적 causal marker 또는 같은 인과 흐름의 직접 확장이 있을 때
- 앞 pair의 결과가 다음 pair의 원인/귀결로 직접 이어질 때

현재 남은 false positive 해석:

- `exp_003 -> exp_004`는 `그래서`가 있었던 이전 pair의 인과를 다시 확장하기보다
  "이후에는 다른 단계로 넘긴다"는 단계 전환에 가깝다
- 따라서 `causal_chain`은 여기서 종료되어야 한다

### scope

이번 spec이 다루는 reason:

- `answer_completion`
- `causal_chain`

이번 spec이 직접 다루지 않는 reason:

- `contrast_pair`
- `speaker_continuation`
- `setup_to_mechanism`
- `unfinished_claim`

이 reason들은 기존 priority / chain boundary spec의 범위에 남긴다.

### TBD items

- `answer_completion` 예외 continuation 세부 규칙
- `causal_chain` continuation 강도 판정 기준
- pair termination을 confidence에 반영하는 방식
- termination이 provenance 표면에 어떻게 기록될지

### what this is not

- this is not a code patch
- this is not a heuristic expansion pass
- this is not a global termination taxonomy for all reasons
- this is not a merge algorithm redesign
- this is not a scoring formula spec

## user-language summary

### problem diagnosis

- 지금 남은 오탐은 "reset이 없다"가 아니라
- "이 reason이 여기서 끝나야 한다"는 종료 기준이 없어서 생긴다

### reason termination classification

- `answer_completion`, `contrast_pair`는 짧게 끝나는 reason이다
- `speaker_continuation`은 여러 pair로 이어질 수 있다
- `causal_chain`은 경우에 따라 이어질 수도, 여기서 끊길 수도 있다

### answer_completion termination criteria

- 질문 뒤 한 번 답이 붙으면 기본적으로 그 pair에서 끝난다
- 다음 문장이 같은 답을 직접 이어 주지 않으면 answer_completion을 끌고 가지 않는다

### causal_chain termination criteria

- 인과 marker가 한 번 나왔다고 다음 pair까지 자동으로 causal이 되지 않는다
- 다음 문장이 새 단계 전환이면 causal은 거기서 끝난다

### user-language restatement

- 이번 턴에서 잠근 핵심은 단순하다
- `answer_completion`과 `causal_chain`은 자동 연장 reason이 아니다
- 한 pair에서 충분히 닫히면 그 자리에서 끝나야 한다
