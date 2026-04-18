# multi_lens strength heuristic spec v0

## verdict

현재 `multi_lens_document_reading_v0`의 strength 휴리스틱은 실패했다.

- probe 결과
  - `line_input_to_reading_organ`: `weak 8 / absent 5 / strong 0`
  - `line_transition_over_surface`: `absent 13 / strong 0`
  - match rate: `0.0`
- 다음 patch는 `line_name` 문자열 매칭이 아니라
  `의미 패턴 기반 판단`으로 좁게 바꿔야 한다.

## failure analysis

현재 휴리스틱의 실패 원인은 단순하다.

- linked text 안에 `input_to_reading_organ`, `transition_over_surface` 같은
  line 이름이 직접 나올 것을 기대했다
- 실제 문서 텍스트는 line 이름이 아니라
  처리 흐름, 전환 행위, 경계 이동 같은 의미 패턴으로 line을 드러낸다
- 그래서 현재 방식은 구조적으로 `strong`을 만들기 어렵다

즉 실패 원인은:

- `line_name literal matching`
- `의미 패턴 부재`
- `reading_basis가 의미 흐름이 아니라 token hit에 묶여 있음`

## line_input_to_reading_organ semantic pattern

이 line은 `인풋이 읽기 기관으로 들어가며 처리/변환/해석되는 흐름`이 보일 때 살아난다.

구체 패턴:

- 인풋이 들어오는 서술
  - `가져온다`
  - `넣는다`
  - `받는다`
  - `들어온다`
  - `feed`
  - `ingest`
- 인풋이 읽히거나 해석되는 서술
  - `읽힌다`
  - `해석된다`
  - `파싱된다`
  - `parse`
  - `interpret`
- 인풋이 처리/변환되는 서술
  - `처리된다`
  - `변환된다`
  - `정리된다`
  - `가공된다`
  - `process`
  - `transform`
- 흐름 표현
  - `입력 -> 처리 -> 결과`
  - `자료 -> 읽기 -> 출력`
  - `source -> parse -> output`
  - `feed -> process -> result`

강도 판단:

- `strong`
  - 인풋 + 처리/해석 + 결과 흐름이 함께 보일 때
  - 또는 처리 경로가 문장 안에서 분명하게 이어질 때
- `weak`
  - 인풋/처리/해석 중 일부만 보일 때
  - 흐름이 암시되지만 전 구간이 보이지 않을 때
- `absent`
  - 위 패턴이 전혀 없을 때
- `caution`
  - 인풋/처리처럼 보이지만
    linkage confidence나 문맥이 불분명해 line 판정으로 밀기 어려울 때

## line_transition_over_surface semantic pattern

이 line은 `한 표면/층위/경계에서 다른 표면/층위/경계로 넘어가는 전환`이 보일 때 살아난다.

구체 패턴:

- 전환/이동 서술
  - `바뀐다`
  - `넘어간다`
  - `전환된다`
  - `이동한다`
  - `shift`
  - `transition`
  - `cross`
  - `move across`
  - `handoff`
- 경계/표면/층위 언급
  - `표면`
  - `경계`
  - `레이어`
  - `층위`
  - `interface`
  - `API`
  - `surface`
  - `layer`
  - `boundary`
- 전환 전후 양쪽이 보이는 표현
  - `A에서 B로 넘어간다`
  - `내부에서 표면으로 올라간다`
  - `runtime에서 handoff로 이동한다`
  - `API boundary를 건넌다`

강도 판단:

- `strong`
  - 전환 전후 양쪽이 함께 보일 때
  - 또는 경계/표면/층위와 전환 행위가 같이 나타날 때
- `weak`
  - 전환 행위는 보이지만
    어느 표면에서 어느 표면으로 가는지 한쪽만 보일 때
- `absent`
  - 전환/경계 패턴이 전혀 없을 때
- `caution`
  - 변화처럼 보이지만
    표면/층위 전환인지 단순 상태 변화인지 불분명할 때

## strength decision structure

### A. 판단 순서

1. `caution` 조건 먼저 본다
   - `linkage_confidence == low`
   - `linkage_reason == contrast_pair`인 경우
   - 변화/처리처럼 보이지만 line 의미 패턴으로는 불분명한 경우
2. `strong` 조건을 본다
   - 의미 패턴이 명확하다
   - 두 개 이상의 신호가 함께 있다
   - 흐름 또는 전환의 양쪽이 확인된다
3. `weak` 조건을 본다
   - 의미 패턴이 하나만 있다
   - 흐름이 약하게만 보인다
4. `absent`
   - 의미 패턴이 전혀 없다

### B. line_input_to_reading_organ 적용 규칙

- strong
  - `인풋/자료` 계열 + `처리/해석` 계열 + `결과/출력` 계열
  - 또는 이 셋 중 둘 이상이 명시적 흐름으로 붙을 때
- weak
  - `인풋`만 있거나 `처리`만 있을 때
  - 또는 흐름이 간접적일 때

### C. line_transition_over_surface 적용 규칙

- strong
  - `전환/이동` 계열 + `표면/경계/레이어` 계열이 함께 있을 때
  - 또는 `A에서 B로` 같은 전후 구조가 보일 때
- weak
  - 전환 행위만 있고 표면/경계 쪽이 약할 때
  - 표면/경계 언급만 있고 실제 이동이 약할 때

## reading_basis recording rule

`reading_basis`는 token hit 설명으로 끝내면 안 된다.

기록 규칙:

- `키워드 X가 있어서`라고만 쓰지 않는다
- `텍스트에서 Y 흐름이 보여서`로 남긴다

예시:

- 좋은 기록
  - `input -> processing -> result 흐름이 문장 안에 명시되어 strong`
  - `표면 전환 행위와 boundary 언급이 함께 보여 strong`
  - `처리 단계만 보이고 결과 흐름이 약해서 weak`
- 나쁜 기록
  - `input 키워드가 있어서`
  - `transition 단어가 있어서`

## caution_reason recording rule

`caution`일 때는 이유를 반드시 남긴다.

허용 이유:

- `low_linkage_confidence`
- `contrast_pair_context`
- `meaning_pattern_ambiguous`
- `state_change_but_not_surface_transition`
- `processing_hint_without_clear_flow`

## TBD items

- `line_pre_read_eye` 의미 패턴
- `line_raw_return_preservation` 의미 패턴
- numeric scoring 방식
- multi-line conflict handling
- pattern dictionary auto-expansion 방식

## what this is not

이 spec은 아래를 하지 않는다.

- 구현 코드 작성
- scoring formula 확정
- document-level aggregation
- line registry 수정
- main runtime 수정
- broad refactor

이 spec은 오직:

- 실패 원인 고정
- 두 stable line의 의미 패턴 고정
- strength 판단 순서 고정
- `reading_basis` / `caution_reason` 기록 기준 고정

만 다룬다.
