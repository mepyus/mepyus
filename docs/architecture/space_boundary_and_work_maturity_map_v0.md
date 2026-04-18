# space boundary and work maturity map v0

## purpose

이 문서는 현재 저장소를 빠르게 읽기 위한
최소 architecture entrypoint다.

목표는 세 가지다.

1. `app/`과 `runtime/`의 경계를 다시 선명하게 적기
2. `app/work/` 내부를 동일 위상으로 보지 않도록 maturity 구획을 잡기
3. `runtime/observer/exploration/`가 이미 존재하는 sidecar lane인지 확인하고 다음 설계 과제를 잠그기

## 1. current architectural reading

현재 저장소는 기능별 앱이 아니라
`source -> interpretation -> body -> evidence -> calibration`
가 폴더 단위로 나뉜 engine workspace로 읽는 것이 맞다.

현재 강한 분해는 아래다.

- `source_assets/`
  - 기준, 선언, 지시, handoff 같은 source philosophy layer
- `docs/`
  - spec, note, report, review가 쌓이는 interpretation layer
- `app/`
  - 철학이 executable organ으로 번역된 code body
- `runtime/`
  - 실행 결과, 영수증, view, event, memory가 남는 evidence layer
- `references/`
  - 외부 구조를 selective하게 읽는 calibration memory

즉 이 저장소의 핵심 경계는
code와 docs의 단순 분리가 아니라,
`생성원 / 해석층 / 몸체층 / 증거층 / 교정층`
분리다.

## 2. `app/` vs `runtime/` stop-line

가장 중요한 구조 경계는 여전히 여기다.

### `app/`이 맡는 것

`app/`은 실행 가능한 organ을 가진다.

현재 읽기:

- `app/core/`
  - schema, registry, formation, state, ingest 같은 보수적 core
- `app/core/runtime/`
  - runtime execution logic
- `app/runtime/`
  - runtime-facing composition, reporting, source/space/process views
- `app/work/`
  - 승격 전 probe, experiment, bounded helper

한 줄로 잠그면:

`app/`은 엔진이 실제로 작동하기 위해 필요한 body layer다.

### `runtime/`이 맡는 것

`runtime/`은 body가 아니라
body가 남긴 결과와 later return path를 붙잡는 층이다.

현재 읽기:

- `runtime/manifests/`
  - registry-like current artifacts
- `runtime/receipts/`
  - 무엇을 실행했는지 남기는 영수증
- `runtime/logs/`
  - append-only raw traces
- `runtime/views/`
  - 사람이 다시 읽는 latest surface
- `runtime/observer/`
  - reread / observation artifacts

한 줄로 잠그면:

`runtime/`은 엔진 결과 표면이자 evidence return layer다.

### boundary rule

아래 규칙으로 읽어야 경계가 흐려지지 않는다.

1. `app/`은 executable body를 둔다.
2. `runtime/`은 emitted artifact를 둔다.
3. runtime output이 다시 code owner를 먹으면 안 된다.
4. runtime readout이 governance decision을 대신하면 안 된다.
5. view/readout/receipt는 body logic과 다른 책임으로 본다.

즉 `app/runtime/`과 `runtime/views/`가 이름은 비슷해도
역할은 다르다.

- `app/runtime/` = view를 만들어 내는 code side
- `runtime/views/` = 만들어진 결과 side

## 3. `docs/architecture/` current gap

`docs/architecture/`는 그동안 사실상 비어 있었다.

문제가 된 지점:

- architecture 설명이 `docs/notes/`와 `docs/reports/`로 분산됨
- 새 agent가 구조 경계를 잡으려면 500개가 넘는 문서층을 넓게 뒤져야 함
- 폴더 역할표는 있지만 현재 공간의 살아 있는 architecture narrative가 얇았음

현재 판단:

- 이 폴더에는 장대한 설계 문서보다
  `entrypoint architecture note` 몇 장만 두는 편이 맞다
- canonical map은 필요하다
- 하지만 세부 판독 기록은 계속 `docs/notes/`와 `docs/reports/`에 둔다

즉 `docs/architecture/`는
전체 문서층을 대체하는 곳이 아니라
구조 읽기 진입점만 잠그는 곳으로 쓰는 것이 적절하다.

## 4. `app/work/` maturity reading

`app/work/`는 한 덩어리 실험장이 아니다.
현재는 최소 세 층으로 나눠 읽는 것이 맞다.

### A. baseline-memory work

대표:

- `app/work/current_layer_baseline`

성격:

- 일반 probe가 아니다
- 현재 철학, 운영 계약, first reference sheet를 잠그는 work-contract memory다

현재 판단:

- `app/work` 내부지만 사실상 baseline root에 가깝다
- 새 agent가 가장 먼저 읽어야 할 work folder다

### B. staged probe corridor

대표:

- `mixed_reentry_probe_stage1`
- `mixed_reentry_observer_stage2`
- `mixed_corridor_boundary_probe_stage3`
- `mixed_corridor_format_disentangle_stage4`
- `technical_business_corridor_decompose_stage5`

성격:

- stage 번호와 spec 파일이 명시된 연속 실험 레인
- 단일 아이디어를 단계적으로 좁혀 가는 bounded probe memory

현재 판단:

- work 중에서도 비교적 구조가 선명하다
- stage lineage가 있기 때문에 읽기 순서가 비교적 안정적이다

### C. utility / sandbox / sidecar work

대표:

- `observer_ingest_min`
- `operating_ui`
- `processor_compare`
- `archive_review/transition_support/workbench_stage1`
- `archive_review/transition_support/result_value_bundle_stage1`
- `archive_review/probe_support/future_segment_probe`
- `archive_review/probe_support/concept_segment_probe`
- `archive_review/external_case_support/external_case_flowline_sweep`
- `archive_review/external_case_support/external_case_folder_sweep`
- `archive_review/interview_support/middle_layer_experiments`
- `archive_review/transition_support/youtube_transcript_probe_0322*`

성격:

- bounded helper, UI demo, compare sidecar, one-topic probe가 혼재한다

현재 판단:

- 유용하지만 maturity label이 약하다
- `baseline-memory`, `staged-probe`, `utility-sidecar` 표식을 상위에서 더 잘 읽히게 만들 필요가 있다

## 5. `app/work/` structural issue

`app/work/folder_status.md`는 현재 child listing은 잘 하지만,
상위 maturity map은 거의 말하지 못한다.

그래서 생기는 문제:

1. `current_layer_baseline`과 일반 probe 폴더가 같은 높이로 보인다.
2. stage 연쇄 실험과 단발 sidecar utility가 같은 종류처럼 보인다.
3. 새 agent가 어디서부터 읽어야 하는지 즉시 판단하기 어렵다.

현재 권장:

- `app/work` 상위에 최소 분류 문서가 하나 더 있어야 한다.
- 분류 단위는 아래 3개면 충분하다.

  - baseline-memory
  - staged-probe
  - utility-sidecar

## 6. exploration sidecar lane status

이 항목은 "없는 설계"가 아니라
이미 얇게 존재하는 설계다.

확인된 사실:

- `runtime/observer/exploration/json/`
- `runtime/observer/exploration/md/`

가 이미 존재한다.

또한 외부 사례 first-pass source도
아래 산출을 명시하고 있다.

- `runtime/observer/exploration/json/external_case_first_pass_<case_name>_v1.json`
- `runtime/observer/exploration/md/external_case_first_pass_<case_name>_v1.md`

즉 `exploration observation sidecar`는
아이디어가 아니라 이미 살아 있는 lane이다.

현재 빈 부분은 lane 자체가 아니라
그 lane의 canonical contract와 reading index다.

## 7. immediate architecture tasks

현재 구조설계 과제는 새 기능 추가보다 아래 순서가 맞다.

1. `app/` 대 `runtime/` 경계 설명을 architecture entrypoint에서 먼저 고정
2. `app/work/`의 maturity 분류를 상위 문서에서 먼저 정리
3. `runtime/observer/exploration/`의 canonical sidecar contract를 별도 문서로 잠그기
4. 그 다음에야 새 exploration output slot이나 translation map을 더 붙이기

## 8. line extraction

이번 내부 폴더 점검에서 두꺼웠던 line은 아래다.

- executable body와 evidence surface는 이미 분리돼 있다
- 문제는 분리 자체보다 entrypoint readability다
- `app/work`는 실험장이지만 내부적으로 같은 maturity가 아니다
- exploration sidecar는 missing이 아니라 under-indexed 상태다
- architecture narrative는 부족해서가 아니라 너무 넓게 흩어져 있었다

## 9. current judgment

현재 저장소는 구조가 약한 것이 아니라
구조 읽기 진입점이 약하다.

따라서 오늘 내부 점검의 결론은
대수술이 아니라 다음 두 문장을 잠그는 것이다.

1. `app`은 body, `runtime`은 evidence surface다.
2. `app/work`는 하나의 실험장이 아니라 baseline-memory / staged-probe / utility-sidecar의 혼합층이다.
