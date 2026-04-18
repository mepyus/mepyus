# folder_status / input_layer

## 1. Folder Identity
- path: `input_layer`
- role_guess: Input-layer root for segmentation, labeling, anchoring, and source location logic.
- one_line_definition: `app/input_layer` is the intake and fragmentization front layer.
- engine_position: body_input_front
- current_priority: high

## 2. Snapshot
- immediate_child_dirs: `4`
- immediate_child_files: `1`
- file_types: `<no_ext>` x 1

## 3. Child Folders
- `anchorizer`
- `labeler`
- `segmenter`
- `source_locator`

## 4. Markdown Files
- none

## 5. Code / Data Files
- other: `.DS_Store`

## 6. Quick Reading
- 이 폴더는 immediate child folder 중심으로 읽는 것이 맞다.

## 7. Folder-Level Summary
- 이 폴더는 입력을 fragmentizable material 로 바꾸는 앞단이다.
- `segmenter`, `labeler`, `anchorizer`, `source_locator` 가 각자 다른 책임을 가진다.
- `app/fragment` 와 직접 이어지고, `app/measurement` 및 `app/runtime` 의 downstream 이 된다.
- 범용화 가능성이 비교적 높은 레이어다.

## 8. Important Areas Now

### first priority
- `segmenter`
- `labeler`
- `anchorizer`
- `source_locator`

### second priority
- none

### later priority
- 루트 자체보다는 하위 폴더가 더 중요하다

## 9. Current Reading
- 지금은 `input_layer` 를 입력기 코어 front door 로 읽는 것이 맞다.
- 절단, 라벨, 앵커, 위치를 한 덩어리로 보지 말고 하위 책임별로 분리해서 봐야 한다.

## 10. Current Use Hint
- 이 문서는 input layer root index 이다.
- 다음 탐색에서는 `segmenter -> labeler -> anchorizer -> source_locator` 순으로 내려가면 구조가 가장 빨리 잡힌다.

## 11. Caution
- 현재 루트에는 직접 파일이 거의 없고, 의미는 하위 폴더에 있다.
- 다음 보강은 하위 폴더별 per-file block 확장으로 가야 한다.
