# context linked segmentation termination exception spec v0

## verdict

- termination exception conditions are locked as a spec asset
- this turn does not change implementation code
- current misses are fixed as missing exception-governance gaps first

## problem diagnosis

termination patch 후 남은 miss는 세 개다.

- `explanatory_mechanism`: `exp_002 -> exp_003` / `causal_chain`
- `mixed_document`: `mix_001 -> mix_002` / `answer_completion`
- `mixed_document`: `mix_002 -> mix_003` / `causal_chain`

공통 원인은 termination 기준 자체가 틀린 것이 아니라,
"이 경우는 종료하지 말아야 한다"는 예외 조건이 문서로 잠기지 않았다는 점이다.

즉 현재 병목은 termination이 과하다는 사실보다,
정상 continuation 예외가 비어 있다는 데 있다.

## technical summary

### answer_completion exception conditions

`answer_completion` termination을 보류할 수 있는 예외는 좁게 정의한다.

예외 조건:

- 현재 pair의 두 번째 segment가 질문에 대한 직접 답변 문장으로 읽히고,
  그 문장 자체가 이유, 정의, 설명을 포함해 질문을 실제로 닫는 경우
- direct answer signal이 아래처럼 동시에 보일 때
  - 질문 직후 위치
  - 응답 문장이 완결형 서술
  - 답변 핵심 술어가 현재 pair 내부에 이미 존재
- 다음 pair가 없어도 현재 pair만으로 question-answer closure가 충분할 때

예외 우선순위:

- direct answer closure 신호가 있으면
  `answer_completion` termination보다 예외 판단을 먼저 검토한다
- 단, 이 예외는 "같은 질문에 대한 현재 pair 내부 closure"에만 적용한다

예외가 아닌 경계:

- 다음 segment가 단순 운영 문장, 메타 설명, stage handoff, unrelated narration이면 예외가 아니다
- 질문 직후 서술이 있어도 실제 답변 closure보다 외부 설명 전환에 가까우면 예외가 아니다
- 질문 뒤에 답변이 아니라 다음 절차 안내가 붙는 경우는 예외가 아니다

남은 miss 해석:

- `mix_001 -> mix_002`는 질문 뒤에 붙은 문장이
  질문에 대한 직접 설명형 답변으로 기능한다
- 따라서 이 pair는 termination보다 answer closure 예외를 먼저 받아야 한다

### causal_chain exception conditions

`causal_chain` termination을 보류할 수 있는 예외도 좁게 정의한다.

예외 조건:

- 현재 pair 또는 다음 pair에 명시적 causal marker가 존재할 때
- 다음 pair가 새 주제 전환이 아니라 직전 결과의 귀결, 설명 확장, 원인-결과 완성으로 읽힐 때
- causal relation이 현재 pair에서 완결되지 않고, 다음 pair가 그 귀결을 직접 이어받을 때

명시적 causal marker 처리:

- `그래서`, `때문에`, `따라서`, `결과적으로` 같은 marker가 현재 pair의 다음 segment에 있으면
  termination보다 continuation 예외를 먼저 검토한다
- marker 하나만으로 무조건 연장하지는 않지만,
  marker 존재는 종료보다 예외 후보를 우선 열어 주는 신호다

예외가 아닌 경계:

- 다음 pair가 단계 전환, 절차 분기, 메타 안내이면 예외가 아니다
- causal marker가 앞 pair에만 있고 다음 pair에는 인과 확장 신호가 없으면 예외가 아니다
- 결과를 다시 설명하지 않는 후속 일반 문장은 예외가 아니다

남은 miss 해석:

- `exp_002 -> exp_003`는 `그래서`가 직접 등장해 인과 귀결을 열고 있다
- `mix_002 -> mix_003`도 `따라서`가 직접 등장해 앞 pair의 의미를 causal continuation으로 잇는다
- 이 두 pair는 termination보다 causal continuation 예외를 먼저 받아야 한다

### exception boundary

예외 조건은 termination을 무력화하지 않도록 아래 경계를 둔다.

- 예외는 현재 reason의 정상 continuation이 좁게 확인될 때만 적용한다
- marker 존재만으로 무조건 예외를 주지 않는다
- stage handoff, 운영 문장, 메타 설명은 예외보다 종료 쪽으로 우선 판단한다
- 예외는 `answer_completion`과 `causal_chain`에만 한정한다

### scope

이번 spec이 다루는 것:

- `answer_completion` termination exception
- `causal_chain` termination exception

이번 spec이 다루지 않는 것:

- 다른 reason의 exception rule
- termination confidence 조정
- provenance 기록 방식
- continuation scoring

### TBD items

- direct answer closure의 세부 lexical rule
- causal continuation 강도 판정 세부 규칙
- exception과 priority 충돌 시 tie-break 세부 규칙
- exception 적용 결과를 confidence에 반영할지 여부

### what this is not

- this is not a code patch
- this is not a global exception system for all reasons
- this is not a scoring formula spec
- this is not a merge algorithm redesign
- this is not a heuristic expansion pass for unrelated reasons

## user-language summary

### problem diagnosis

- 지금 남은 miss는 termination이 틀렸기 때문이 아니라
- "이 경우는 계속 이어야 한다"는 예외 규칙이 없어서 생긴다

### answer_completion exception conditions

- 질문 뒤 문장이 그 질문을 실제로 닫는 직접 답변이면
  그 pair는 끊지 말아야 한다
- 하지만 운영 문장이나 메타 설명이면 예외를 주지 않는다

### causal_chain exception conditions

- `그래서`, `따라서` 같은 인과 표지가 실제 귀결을 여는 경우
  그 pair는 끊지 말아야 한다
- 하지만 단계 전환이나 절차 안내면 예외를 주지 않는다

### exception boundary

- 예외는 좁게만 준다
- 그렇지 않으면 termination이 다시 무력화된다

### user-language restatement

- 이번 턴에서 잠근 핵심은 단순하다
- termination은 유지하되,
  direct answer와 direct causal continuation 같은 좁은 정상 사례만 예외로 살린다
