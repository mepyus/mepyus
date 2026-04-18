# multi_lens_document_reading_v0 strength heuristic patch note

## what changed

- `line_input_to_reading_organ`
  - direct `line_name`/seed literal matching 의존을 제거했다
  - `input -> processing -> result` 의미 흐름을 얇게 읽는 방식으로 바꿨다
- `line_transition_over_surface`
  - direct `transition over surface` literal matching 의존을 제거했다
  - `movement/transition + boundary/surface + across/from-to` 의미 패턴으로 바꿨다
- 판단 순서
  - `caution -> strong -> weak -> absent`
  - low linkage / contrast context를 먼저 본다
- `reading_basis`
  - token hit 설명 대신
  - `text hints at input-processing movement`
  - `no surface-transition or boundary-crossing pattern is visible`
  같은 semantic-flow 문구로 바뀌었다

## validation

- compile
  - `python3 -m py_compile app/core/runtime/multi_lens_document_reading.py scripts/run_multi_lens_document_reading_probe.py scripts/run_multi_lens_document_reading_strength_validation.py`
  - passed
- probe
  - `/tmp/multi_lens_document_reading_probe/probe_result.json`
- strength validation
  - `/tmp/multi_lens_document_reading_strength_validation/validation_result.json`

## before / after

### line_input_to_reading_organ

- before
  - `weak 8 / absent 5 / strong 0`
- after
  - `weak 3 / caution 6 / absent 4 / strong 0`

판정:
- weak 남발은 줄었다
- low-confidence / contrast context가 `caution`으로 분리됐다
- 하지만 `strong`은 아직 나오지 않았다

### line_transition_over_surface

- before
  - `absent 13 / strong 0`
- after
  - `absent 9 / caution 4 / strong 0`

판정:
- 전부 absent로 밀어버리던 패턴은 줄었다
- low-confidence segments는 `caution`으로 분리됐다
- 그러나 fixture 안에서 boundary-crossing material 자체가 얇아서 `strong`은 여전히 없다

## reading_basis wording

before:
- `matched seed`
- `partial cue only`
- `no relevant transition-over-surface combination seed`

after:
- `text hints at input-processing movement, but the full flow stays partial`
- `input-processing flow is unclear and linkage confidence is low`
- `no surface-transition or boundary-crossing pattern is visible in the text`

## over-trigger risk

- `line_input_to_reading_organ`
  - 현재 과잉 strong 발화는 없다
  - 대신 `읽기`, `처리` 같은 단일 processing hint가 `weak` 또는 `caution`으로 반응한다
  - 따라서 over-trigger는 낮지만 still conservative bias가 강하다

## remaining weakness

- `line_input_to_reading_organ`
  - fixture에 `결과/출력` 쪽이 약하면 strong까지 못 올라간다
  - 이건 current bounded spec limitation이다
- `line_transition_over_surface`
  - 현재 fixture 텍스트에 boundary/layer/handoff material이 거의 없다
  - 그래서 `absent` 유지가 큰 폭으로 남는다
  - 이건 material scarcity + bounded spec limitation 둘 다 있다

## conclusion

- line reading은 더 이상 line-name literal match 중심이 아니다
- `reading_basis`는 semantic-flow rationale로 더 명확해졌다
- 다만 current fixture material과 bounded spec 때문에 stable line strong 판정은 아직 복구되지 않았다
