# multi_lens_document_reading_v0 probe note

## probe 동작 여부

- skeleton은 이미 구현되어 있었다.
  - [multi_lens_document_reading.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/multi_lens_document_reading.py)
  - [run_multi_lens_document_reading_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_multi_lens_document_reading_probe.py)
- probe 실행은 정상 완료됐다.
  - 출력 경로: `/tmp/multi_lens_document_reading_probe/probe_result.json`

## probe 결과 요약

- primary lens ids
  - `line_input_to_reading_organ`
  - `line_transition_over_surface`
- secondary lens ids
  - `line_pre_read_eye`
  - `line_raw_return_preservation`
- 실제 probe는 `is_stable_lens_only=true`로 돌아서 secondary/candidate line은 이번 턴에 읽히지 않았다.

## line별 reading_strength 분포

- `line_input_to_reading_organ`
  - `weak`: 8
  - `absent`: 5
  - `strong`: 0
- `line_transition_over_surface`
  - `absent`: 13
  - `strong`: 0
- `line_pre_read_eye`
  - not probed
- `line_raw_return_preservation`
  - not probed

## strength 휴리스틱 판정

stable/thick line 기준:
- `line_input_to_reading_organ`
  - fixture에서 `strong`이 한 번도 나오지 않았다
  - 일부는 `입력`, `읽기` 같은 partial cue만 잡고 `weak`로 내려갔다
- `line_transition_over_surface`
  - fixture에서 전부 `absent`였다
  - current heuristic이 `transition over surface` 조합 seed에 너무 좁게 묶여 있다

candidate/thin line 기준:
- 이번 probe는 stable lens only라 validation 불가
- 따라서 `pre_read_eye`, `raw_return_preservation`의 weak/absent safety는 아직 확인되지 않았다

## match rate

- stable/thick regression guard 기준 match rate:
  - `0 / 2 = 0.0`
- 이유:
  - 두 stable line 모두 fixture에서 `strong`을 만들지 못했다

## 오판 패턴

- `input_to_reading_organ`
  - organ-level evidence보다 단일 token partial match에 머문다
  - low linkage confidence downgrade가 자주 걸린다
- `transition_over_surface`
  - 한국어/문맥적 전환 표현을 거의 못 받는다
  - 단일 token/context로는 모두 `absent` 처리된다
- candidate lines
  - 아예 probe path에 들어오지 않아 오판/과잉 판정 여부를 아직 볼 수 없다

## 다음 구현 방향

- 현재 match rate가 `0.75`보다 훨씬 낮다
- 이번 판정:
  - `strength 휴리스틱 spec`을 별도로 잠그고
  - narrow patch 후 재검증으로 가는 것이 맞다
- 아직 가지 않을 것:
  - document-level variation map
  - document-level aggregation
  - scoring formula 확장

## 이번 턴 결론

- probe는 동작했다
- current strength heuristic은 stable/thick line regression guard를 통과하지 못했다
- 다음 단계는 `strength heuristic refinement spec + patch + revalidation`이다
