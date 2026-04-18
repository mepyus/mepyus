# sentence_connection_based_line_reading_spec_v0

## 1. problem restatement

이번 spec의 목적은 `line_input_to_reading_organ` 문제를
`processing category가 좁다`는 수준으로 축소하지 않고,
line 판독 단위 자체를 `sentence/segment connection flow`로 재정의하는 것이다.

지금까지의 한계는 대체로 아래 순서였다.

- line을 `line_name` literal match에 가깝게 읽었다
- 그다음 line을 category나 의미 패턴으로 읽도록 옮겼다
- 하지만 여전히 실제 판독이 개별 단어, 개별 분절, 개별 category hit에 너무 빨리 고정됐다

그 결과 현재 reader는 아래를 자주 under-read한다.

- 실제 문장 흐름 안에 `input -> 수용 -> 처리 -> 결과`가 있어도
  각 고리가 연결된 흐름으로 복원되지 않으면 line 근거로 충분히 읽지 못한다
- `transition_over_surface`도 `이전 상태 -> 전환 -> 표면/경계 -> 이후 상태`가
  흐름으로 이어져 있어야 하는데,
  개별 token이나 개별 segment 수준에서 판단이 너무 일찍 멈춘다

따라서 이번 spec의 핵심 전환은 category refinement가 아니다.
핵심은 line reading의 판독 기준을
`sentence-connection-based reading`으로 잠그는 것이다.

## 2. why segment-only/category-first reading under-reads line

segment-only/category-first reading은 보통 아래 방식으로 동작한다.

- 먼저 분절 하나를 잡는다
- 그 안에서 token, phrase, category hit를 찾는다
- hit가 약하면 그 자리에서 판단을 멈춘다

이 방식의 문제는 line이 실제로 드러나는 위치를 잘못 잡는 데 있다.

- 분절은 line의 완성본이 아니라 진입점이다
- category는 판독 보조물이지 line 자체가 아니다
- line은 역할 이동이 이어지는 연결 흐름에서 드러난다

즉 under-read의 본질은 `category가 조금 부족하다`가 아니다.
under-read의 본질은 reader가 아직도
`연결된 문장 흐름`을 판독면으로 충분히 올리지 못한다는 데 있다.

## 3. segment as entry point, connection as reading surface

### A. segment as entry point

- 분절은 line 판독의 최종 단위가 아니다
- 분절은 reread를 시작하게 만드는 entry point다
- 분절 하나에서 시작하더라도, 판독은 반드시 인접 문장과 분절로 확장되어야 한다

운영 의미:

- 어떤 분절이 `입력`, `표면`, `결과`, `전환` 같은 단서를 품고 있더라도
  그 분절만으로 line을 닫지 않는다
- 해당 분절이 앞뒤 문장과 어떤 역할 연결을 이루는지 먼저 복원한다

### B. connection as reading surface

- 실제 line 판독은 연결 흐름 위에서 일어난다
- 연결 흐름이란 문장/분절들이 역할 이동을 이루며 이어지는 구조다
- line은 개별 단어, 개별 문장, 개별 category에서 직접 주어지지 않는다
- line은 역할 이동이 연결되며 형성되는 reading surface에서 드러난다

운영 의미:

- token/category hit는 reread 유도 신호일 수는 있다
- 그러나 최종 판독 근거는 `무슨 연결 흐름이 복원되었는가`여야 한다

## 4. per-line flow reconstruction model

이번 spec은 아래 두 stable line에 한해
sentence-connection-based reconstruction 기준을 잠근다.

### line_input_to_reading_organ

#### category-centered reading

이 line을 category 중심으로 읽으면 보통 아래처럼 된다.

- `input` 표현이 있는지 본다
- `processing/interpretation/transform` category에 직접 닿는 표현이 있는지 본다
- `result/output/surface` 표현이 있는지 본다
- 각 slot의 hit 유무로 판독을 정리한다

이 방식은 아래에서 under-read를 만든다.

- 처리 단계가 `routing`, `제작`, `자동으로 관련된 에이전트를 부른`, `검증`처럼
  processing category literal에 직접 안 들어오면 약하게 읽는다
- 수용/기관 연결 단계가 문장 사이에 분산되어 있으면
  개별 segment 안에서 slot이 닫히지 않는다는 이유로 흐름 전체를 놓친다
- 결과가 후행 문장에 드러나도,
  그 이전 문장과의 연결 사슬을 충분히 복원하지 못하면 weak/caution에 머문다

#### sentence-connection-based reading

이 line은 아래 흐름이 복원되는지로 읽는다.

- `input -> 수용/기관 연결 -> 처리/해석/변환 -> 결과/표면`

여기서 중요한 점:

- 모든 고리가 같은 문장 안에 있을 필요는 없다
- 어떤 고리는 분절 A에, 다른 고리는 분절 B나 C에 있을 수 있다
- reader는 각 문장이 역할상 어떻게 이어지는지 복원해야 한다

connection reading이 새로 보게 만드는 것은 아래다.

- `입력된 것`이 어디로 수용되거나 어떤 기관/체계로 연결되는지
- 그 연결 이후 어떤 처리, 해석, 변환, 라우팅, 호출, 검증이 일어나는지
- 그 결과 무엇이 출력되거나 표면화되는지

즉 `processing category hit`가 아니라,
문장들이 실제로 `무언가가 들어오고, 어떤 기관/체계가 그것을 받아 연결하고,
처리한 뒤, 결과를 내보이거나 표면화한다`는 흐름을 이루는지가 핵심이다.

#### bounded stop condition

그렇다고 무제한 확장하면 안 된다.
이 line은 아래 경계 안에서만 읽는다.

- 단순히 `입력`과 `결과`가 따로 존재한다고 해서 strong으로 올리지 않는다
- 처리/수용 고리가 설명 가능하게 연결되지 않으면 caution 또는 absent에 머문다
- 기관 연결 없이 막연한 행위 일반론으로만 이어지는 경우는 과잉 판독하지 않는다
- 문서 전체 서사를 임의로 요약해 보충하지 말고,
  실제 인접 문장/분절 연결에서 복원 가능한 흐름까지만 읽는다

### line_transition_over_surface

#### category-centered reading

이 line을 category 중심으로 읽으면 보통 아래처럼 된다.

- `transition` 계열 표현이 있는지 본다
- `surface/boundary/layer` 계열 표현이 있는지 본다
- 조합 seed가 있으면 강하게, 없으면 약하게 정리한다

이 방식은 아래에서 under-read를 만든다.

- 전환 전 상태와 전환 후 상태가 서로 다른 문장에 흩어져 있으면
  조합 token이 약하다는 이유로 흐름을 놓친다
- `표면`, `경계`, `레이어`가 후행 상태 변화와 연결되어 있는데도
  개별 token 점검에서 판단이 끊긴다
- 표면을 가로지르거나 경계를 넘는 이동이
  단어 조합으로는 딱 닫히지 않아도,
  문장 연결상 분명한 경우를 충분히 못 읽는다

#### sentence-connection-based reading

이 line은 아래 흐름이 복원되는지로 읽는다.

- `이전 상태 -> 전환/이동 -> 표면/경계/레이어 -> 이후 상태`

여기서 핵심은 `transition`과 `surface`가 같은 문장에 직접 붙어 있느냐가 아니라,
문장/분절들이 실제로 아래 구조를 이루느냐이다.

- 무엇이 이전 상태였는가
- 어떤 이동, 넘김, 전환, 건너감이 발생했는가
- 그 전환이 어떤 표면, 경계, 레이어를 통과하거나 걸쳤는가
- 그 후 어떤 상태가 되었는가

connection reading이 새로 보게 만드는 것은 아래다.

- 전환이 표면 위에서만 언급된 것이 아니라
  전후 상태 변화를 매개하는 연결 고리라는 점
- 표면/경계가 단순 배경 명사가 아니라
  상태 이동이 발생하는 actual reading surface라는 점
- 이후 상태가 있어야 전환이 완결된 흐름으로 읽힌다는 점

#### bounded stop condition

이 line도 아래 경계 안에서만 읽는다.

- 단독 `표면`이나 단독 `transition`은 여전히 strong 근거가 아니다
- 이전 상태와 이후 상태가 거의 없으면 과도하게 복원하지 않는다
- 표면/경계가 단순 묘사 배경일 뿐이면 line으로 올리지 않는다
- 연결 흐름이 문장 근거 없이 추정에 의존하면 absent 또는 caution으로 멈춘다

## 5. strong/weak/caution/absent judgment under connection reading

이번 spec에서 판정 기준은 category hit보다 flow reconstruction에 더 의존한다.

### strong

- strong은 연결 흐름의 주요 고리가 충분히 복원될 때만 가능하다
- 개별 token의 강도보다 `역할 이동 사슬`이 설명 가능하게 닫히는지가 우선이다

`line_input_to_reading_organ`에서 strong이 되려면:

- input이 보이고
- 그것이 어떤 수용/기관 연결 또는 처리 체계로 이어지며
- 처리/해석/변환이 뒤따르고
- 결과/표면이 후행 상태로 설명 가능해야 한다

`line_transition_over_surface`에서 strong이 되려면:

- 이전 상태가 보이고
- 전환/이동이 발생하며
- 그 전환이 표면/경계/레이어를 매개로 하고
- 이후 상태가 후행 흐름으로 설명 가능해야 한다

### caution

- caution은 흐름의 일부 고리만 보일 때다
- 중요한 고리가 있으나 연결 사슬이 충분히 닫히지 않을 때다
- category hit는 있으나 flow reconstruction이 부분적일 때다

대표 경우:

- `input`과 `result`는 보이지만 수용/처리 연결이 흐리다
- `transition`과 `surface`는 보이지만 전후 상태가 약하다
- 연결은 느껴지지만 실제 문장 근거가 부족해 일부 고리만 복원된다

### weak

- weak은 entry point는 잡혔지만 연결 흐름이 아직 매우 얇게만 복원될 때다
- weak은 category 반응의 존재 보고가 아니라,
  흐름 재구성이 시작되었으나 주요 연결 고리가 거의 비어 있는 상태다
- weak은 caution보다 더 얇고, absent보다는 약간 더 연결 근거가 있는 상태다

대표 경우:

- `input` 또는 `surface` 같은 entry point만 있고 그 다음 역할 이동이 거의 안 보인다
- 인접 문장 재독을 했지만 실제 연결 사슬은 한두 단계만 희미하게 보인다
- 흐름 전체를 서술하려고 하면 대부분이 추정으로 흘러 아직 basis를 닫기 어렵다

### absent

- absent는 흐름 연결이 거의 복원되지 않을 때다
- token이나 category가 있더라도 연결 사슬을 설명할 수 없으면 absent에 머문다
- 개별 어휘 반응만 있고 역할 이동이 보이지 않으면 absent다

## 6. reading_basis guidance

이번 spec에서 `reading_basis` 기록 방식은 아래로 잠근다.

- token hit log를 쓰지 않는다
- category hit log를 주된 형식으로 쓰지 않는다
- `어떤 연결 흐름이 복원되었는지`를 문장으로 설명해야 한다

### required basis style

`reading_basis`는 아래 질문에 답해야 한다.

- 어떤 분절이 reread entry point가 되었는가
- 그 entry point가 어떤 앞뒤 문장과 연결되었는가
- 실제로 어떤 역할 이동 흐름이 복원되었는가
- 어떤 고리가 충분했고 어떤 고리가 부족했는가

### preferred wording pattern

- entry point를 짚는다
- 연결된 앞뒤 문장을 설명한다
- 복원된 흐름을 한 문장으로 요약한다
- 부족한 고리가 있으면 마지막에 적는다

예시 형식:

- `entry segment의 입력 표현을 시작점으로 reread했을 때, 다음 문장에서 해당 입력이 시스템 수용과 처리로 이어지고 후행 문장에서 결과 표면화가 이어져 input -> organ-link -> processing -> result 흐름이 복원된다.`
- `표면 관련 분절을 시작점으로 reread했지만, 전환 이후 상태는 보이나 이전 상태와 실제 경계 통과 연결이 약해서 이전 상태 -> 전환 -> surface -> 이후 상태 흐름은 부분 복원에 머문다.`

금지 형식:

- `matched token: input, process, result`
- `category hits: transition/surface`
- `seed found therefore strong`

핵심:

- `reading_basis`는 hit report가 아니라 flow reconstruction explanation이어야 한다

## 7. bounded non-goals

이번 spec은 아래를 하지 않는다.

- numeric scoring 도입 없음
- broad heuristic refactor 없음
- candidate line 확장 없음
- ontology식 line 정의 고정 없음
- threshold widening 없음
- broad runtime redesign 없음
- code patch 없음

또한 이번 spec은
`문맥을 더 보자`라는 추상 원칙을 말하는 문서가 아니다.
이 문서는 `분절은 entry point이고 연결 흐름이 판독면`이라는
구체적 reading contract를 잠그는 문서다.

## 8. next-step rule

다음 단계는 이 spec이 잠긴 뒤에만 열린다.

- 이후 patch는 category list 수정 중심이 아니라
  `connection-flow reconstruction`을 더 정확히 읽게 하는 좁은 refinement여야 한다
- `input_to_reading_organ`과 `transition_over_surface` 모두
  개별 token/category를 더 늘리는 방식이 아니라
  이미 존재하는 문장 연결을 더 정확히 복원하는 방향이어야 한다

허용되는 다음 단계:

- flow reconstruction을 더 안정적으로 읽게 하는 narrow patch proposal
- `reading_basis`를 flow explanation 중심으로 바꾸는 narrow patch proposal
- segment entry point에서 adjacent sentence/segment reread를 더 일관되게 여는 좁은 조정

여전히 금지되는 다음 단계:

- category expansion 중심 제안
- threshold widening
- candidate-line expansion
- scoring framework 도입
- broad runtime redesign

결론:

- 분절은 시작점일 뿐이다
- 실제 판독면은 문장/분절 사이의 연결이다
- line은 연결된 흐름 위에서 드러난다
- future patch는 이 reading contract를 구현하는 좁은 refinement로만 열 수 있다
