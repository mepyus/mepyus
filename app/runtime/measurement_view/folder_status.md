# folder_status / runtime/measurement_view

## 1. Folder Identity
- path: `runtime/measurement_view`
- role_guess: Runtime subsystem folder containing a focused execution or view slice.
- one_line_definition: `app/runtime/measurement_view` builds measurement-side readable surface.
- engine_position: body_runtime_measurement_surface
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
- python: `__init__.py`, `builder.py`, `render.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 observer/measurement 결과를 사람이 읽는 표면으로 바꾸는 서브레이어다.
- `scripts/build_measurement_view.py` 와 직접 연결된다.

## 8. Key Files

### `builder.py`
- current role: measurement view 조립기
- function: measurement-side readable representation 구성
- engine position: measurement view builder

### `render.py`
- current role: measurement view 렌더러
- function: 조립된 measurement view 를 표면 산출로 내보냄
- engine position: measurement surface renderer

## 9. Current Reading
- 지금은 source_view 와 짝을 이루는 measurement 표면층으로 읽는 것이 맞다.

## 10. Caution
- observer 계산 자체와 measurement view surface 는 분리해서 읽어야 한다.
