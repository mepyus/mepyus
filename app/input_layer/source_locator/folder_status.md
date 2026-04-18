# folder_status / input_layer/source_locator

## 1. Folder Identity
- path: `input_layer/source_locator`
- role_guess: Focused input-layer module folder.
- one_line_definition: `source_locator` is the source-link, origin-map, and source-return handle module.
- engine_position: body_input_source_locator
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `3`
- file_types: `.py` x 3

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `__init__.py`, `locator.py`, `origin_map_minimum_v1.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 fragment/source 를 다시 원본과 연결할 수 있게 위치 정보를 부여하는 레이어다.
- provenance 와 역추적 가능성에 직접 연결된다.
- 최근에는 단순 위치 지정에서 더 나아가, 파생 시점에 자동으로 붙는 `origin map` 최소 helper 까지 포함한다.
- 즉 이 폴더는 `locator -> origin map -> source return handle` 흐름의 입력기 하위 provenance ingress 보조층이다.

## 8. Key Files

### `locator.py`
- current role: source location assignment 핵심 파일
- function: source path / line range / location linkage 보조
- engine position: source linkage core
- reuse potential: 높음

### `origin_map_minimum_v1.py`
- current role: origin map 최소 helper
- function: heading path, char span, source preview 를 자동 추출해 source return handle seed 생성
- engine position: provenance return handle preparer
- reuse potential: 높음
- caution: v1 은 lightweight helper 이며 full provenance graph 는 아니다

## 9. Current Reading
- 지금은 `source_locator` 를 provenance 보조가 아니라 엔진 역추적성의 핵심 모듈로 읽는 것이 맞다.
- 최근 기준으로는 locator-only utility 가 아니라, 입력기 하위의 source return / provenance handle 레이어로 읽는 편이 맞다.

## 10. Caution
- location 이 약하면 fragment 신뢰도와 calibration lane 이 같이 약해질 수 있다.
- origin map v1 은 최소 provenance 손잡이이므로, merge provenance 나 version graph 를 대신하지는 않는다.
