# folder_status / docs/guides

## 1. Folder Identity
- path: `docs/guides`
- role_guess: Human-facing operation manuals and quick-start guides.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `12`
- file_types: `.md` x 10, `.txt` x 2

## 3. Child Folders
- none

## 4. Markdown Files
- `engine_overview.md`
  title: engine_overview
  summary: 이 문서는 지금 만든 엔진 구조를 사용자가 한눈에 이해할 수 있게 설명하는 개요 문서다.
- `folder_inventory_workflow.md`
  title: folder_inventory_workflow
  summary: 이 문서는 새 폴더나 새 문서가 생겼을 때 전체를 다시 읽지 않고 어떻게 반영하는지 설명한다.
- `gemini_usage.md`
  title: gemini_usage
  summary: 이 문서는 Gemini CLI를 어디까지 쓸 수 있고 어디부터 금지인지 사용자 기준으로 설명하는 문서다.
- `input_dropzones.md`
  title: input_dropzones
  summary: 이 문서는 앞으로 입력 파일을 어디에 둘지 빠르게 확인하는 운영 가이드다.
- `local_delta_update_note.md`
  title: local_delta_update_note
  summary: 이 문서는 inventory가 이미 있는 상태에서 새 문서 하나를 추가했을 때, 해당 폴더와 부모 폴더만 갱신하는지 확인하기 위한 짧은 운영 메모다.
- `operation_workflow.md`
  title: operation_workflow
  summary: 이 문서는 User / Codex / Gemini CLI가 실제로 어떻게 협업하는지 운영 루틴으로 정리한 문서다.
- `prompts_usage.md`
  title: prompts_usage
  summary: 이 문서는 `gemini/prompts/` 아래 프롬프트를 언제 어떻게 쓰는지 빠르게 알려주는 문서다.
- `quick_start.md`
  title: quick_start
  summary: 이 문서는 가장 빨리 다시 시작할 수 있게 만든 짧은 운영 문서다.
- `root_md_reorganization_guide_v1.md`
  title: root_md_reorganization_guide_v1
  summary: 이 문서는 루트에 섞여 있는 md 파일을 어떻게 읽고, 앞으로 어디에 둘지 정리하는 가이드다.
- `source_assets_creation_map_v1.md`
  title: source_assets_creation_map_v1
  summary: 이 문서는 앞으로 Codex가 새 문서를 만들 때 어느 폴더에 둬야 하는지 빠르게 확인하는 **배치 기준표**다.

## 5. Code / Data Files
- other: `aifrontier_01_28.txt`, `oh_my_opencode.txt`

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.guides`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.guides.json`
- parent_folder: `docs`
- related_status_files: `docs/guides/folder_status.md`
- last_updated: `2026-03-27T21:40:26+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
