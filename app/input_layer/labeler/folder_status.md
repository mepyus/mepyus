# folder_status / input_layer/labeler

## 1. Folder Identity
- path: `input_layer/labeler`
- role_guess: Focused input-layer module folder.
- one_line_definition: `labeler` is the core input-layer labeler slot.
- engine_position: body_input_labeler
- current_priority: medium

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `1`
- file_types: `.py` x 1

## 3. Child Folders
- none

## 4. Markdown Files
- none

## 5. Code / Data Files
- python: `labeler.py`

## 6. Quick Reading
- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.

## 7. Folder-Level Summary
- 이 폴더는 repo 전반에 이미 분산되어 존재하는 labeling 을
  `core input-layer labeler` 관점으로 수렴시키기 위한 슬롯이다.
- 현재는 최소 구현 파일이 생겼지만, 여전히 contract-first 성격이 강하다.
- 이 슬롯의 현재 역할은 `external routing labels` 와 `intake/core labels` 사이의 경계를 잠그는 데 있다.
- 즉 이 위치는 labeling 전체를 먹는 만능 모듈이 아니라,
  입력 정규화 중심 코어 슬롯이다.

## 8. Key Files

### `labeler.py`
- current role: core input-layer labeler entrypoint
- function: external routing labels 정규화, core intake labels 조립, structured doc intake label packet 생성
- engine position: input normalization core
- reuse potential: 높음
- caution: operation labels, anchor handles, fragment grouping labels 전체를 다루는 만능 모듈은 아님
- current link note: [input_layer_wrapper_core_link_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/input_layer_wrapper_core_link_note_v1.md)

## 9. Current Reading
- 현재 repo 에는 labeling 이 이미 여러 층에 존재한다.
- 하지만 `app/input_layer/labeler` 는 그 전체를 대체하는 모듈이 아니다.
- 지금은 `segmenter` 와 `anchorizer` 사이에 놓이는 책임 구획이면서,
  external routing label 을 intake/core label 로 수렴시키는 코어 slot 이자 최소 entrypoint 로 읽는 것이 맞다.
- structured doc intake 에서는 wrapper 가 이 모듈을 호출하지만, wrapper 와 이 모듈의 책임은 동일하지 않다.

## 10. Caution
- operation labels 와 meaning-side handles 를 이 슬롯이 직접 소유한다고 읽으면 안 된다.
- fragment/retrieval/grouping label 미래 슬롯을 현재 완성형처럼 읽으면 안 된다.
- 현재는 구현이 시작됐지만, 여전히 분산된 labeling 을 later implementation 으로 더 수렴시켜야 하는 core slot 상태다.
