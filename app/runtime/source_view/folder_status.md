# folder_status / runtime/source_view

## 1. Folder Identity
- path: `runtime/source_view`
- role_guess: Runtime subsystem folder containing a focused execution or view slice.
- one_line_definition: `app/runtime/source_view` builds source-side readable surface.
- engine_position: body_runtime_source_surface
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
- 이 폴더는 source-side view builder/render 레이어다.
- `scripts/build_source_view.py` 와 직접 이어지고, root `runtime/reports` 및 source 표면과 연결된다.

## 8. Key Files

### `builder.py`
- current role: source view 조립기
- function: source-side readable representation 구성
- engine position: source view builder

### `render.py`
- current role: source view 렌더러
- function: 조립된 source view 를 실제 표면 형식으로 내보냄
- engine position: source surface renderer

## 9. Current Reading
- 지금은 builder 와 render 의 분리를 먼저 보는 것이 맞다.
- source 판독 표면을 만드는 핵심 서브레이어로 취급하면 된다.

## 10. Caution
- 실제 실행 진입점은 `scripts/` 쪽에 있을 수 있으므로 이 폴더만으로 전체 흐름을 닫으려 하면 안 된다.
