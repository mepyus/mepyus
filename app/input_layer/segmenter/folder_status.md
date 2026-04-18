# folder_status / input_layer/segmenter

## 1. Folder Identity
- path: `input_layer/segmenter`
- role_guess: Focused input-layer module folder.
- one_line_definition: `segmenter` is the split/fragmentization module slice.
- engine_position: body_input_segmenter
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `2`
- file_types: `.py` x 2

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `experimental_segmenter.py`, `experimental_segmenter_v2.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.
- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.

## 7. Folder-Level Summary
- 이 폴더는 입력을 잘라 fragment 후보를 만드는 절단 모듈 레이어다.
- 현재 `experimental_segmenter` 계열이 중심이라 실험 레인 성격도 함께 가진다.

## 8. Key Files

### `experimental_segmenter.py`
- current role: 1차 절단 실험기
- function: 입력 분절 규칙 실험
- engine position: experimental segmenter v1

### `experimental_segmenter_v2.py`
- current role: 보강 절단 실험기
- function: 대체/개선 split 규칙 실험
- engine position: experimental segmenter v2

## 9. Current Reading
- 지금은 production-ready split engine 보다 실험 기반 split layer 로 읽는 것이 맞다.

## 10. Caution
- 실험 파일이므로 현재 코어 절단 truth 로 과대해석하면 안 된다.
