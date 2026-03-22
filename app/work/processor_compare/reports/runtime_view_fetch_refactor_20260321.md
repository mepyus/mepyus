# Runtime View Fetch Refactor 2026-03-21

## 목적

viewer HTML에 JSON payload를 직접 박아 넣는 방식을 줄여
렌더 무게와 파일 비대화를 낮춘다.

이번 정리는 특히 아래 경로를 대상으로 했다.

- `/source`
- `/measurements`
- `/atlas`
- `/terrain`

원칙:

- viewer route는 `HTML shell + /api fetch`
- 보고서 파일 생성은 기존처럼 inline payload 허용
- 책임 분리와 실제 응답 크기 축소를 동시에 달성

## 구조 변경

### viewer route

- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
  - server route에서 더 이상 큰 JSON을 먼저 build해서 HTML에 주입하지 않음
  - 아래 render 함수들을 `api_path=...` 방식으로 호출

### source view

- [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/source_view/render.py)
  - `render_source_fragment_html(data=None, api_path="/api/source")`
  - embedded payload가 있으면 사용
  - 없으면 `/api/source` fetch

### measurement view

- [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/measurement_view/builder.py)
- [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/measurement_view/render.py)
  - `render_measurement_view_html(data=None, api_path="/api/measurements")`
  - builder/render 분리 유지
  - viewer에서는 fetch 모드 사용

### atlas

- [region_atlas_render.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas_render.py)
  - `render_region_atlas_html(data=None, api_path="/api/atlas")`
  - viewer에서는 fetch 모드 사용

### terrain

- [terrain_map_render.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_render.py)
  - `render_terrain_map_html(data=None, api_path="/api/terrain")`
  - sidebar metric도 fetch 이후 갱신
- [terrain_map_assets.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_assets.py)
  - 기존 즉시실행형 script를 `window.renderTerrainMap(data)` 함수형으로 전환
  - embedded payload가 있으면 그대로 동작
  - fetch 모드에서도 같은 함수로 렌더 가능

## 줄 수 상태

정리 후 주요 파일 줄 수:

- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py): `118`
- [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py): `327`
- [region_atlas.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas.py): `103`
- [region_atlas_render.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/region_atlas_render.py): `160`
- [terrain_map_render.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_render.py): `90`
- [terrain_map_assets.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_assets.py): `188`
- [source_view/builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/source_view/builder.py): `310`
- [source_view/render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/source_view/render.py): `260`
- [measurement_view/builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/measurement_view/builder.py): `76`
- [measurement_view/render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/measurement_view/render.py): `125`
- [terrain_map_builders.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_builders.py): `396`
- [terrain_map_regions.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/terrain_map_regions.py): `183`

## HTML 크기 비교

### fetch shell

- source: `11,842`
- measurements: `4,966`
- atlas: `6,429`
- terrain: `12,215`

### inline payload

- source: `808,805`
- measurements: `579,127`
- atlas: `18,096`
- terrain: `14,452,574`

## 해석

- 가장 큰 병목은 줄 수보다 inline payload였다.
- terrain은 inline 기준으로 약 `14.4MB`까지 커졌고, fetch shell은 약 `12KB`다.
- source/measurement도 shell 기준으로는 충분히 가벼워졌다.
- atlas는 원래 상대적으로 작았지만, fetch 패턴으로 통일해 구조 일관성을 얻었다.

## 검증

- `py_compile` 통과
- fetch shell 렌더 문자열 생성 확인
- inline 렌더도 기존 보고서용으로 유지되는 것 확인

## 남은 정리 포인트

- source/measurement 클라이언트 스크립트 공통화 가능
- terrain/style script asset 추가 분리 여지 있음
- 보고서용 static html도 필요시 `json + shell` 방식으로 더 줄일 수 있음

## 결론

이번 정리로 viewer 레벨의 무거움은 대부분 해소됐다.

이제 남은 문제는

- 렌더 책임 분리의 세부 정리
- 공통 client helper 정리
- 필요 시 보고서 static html 경량화

쪽이다.
