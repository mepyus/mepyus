# folder_status / app/work/processor_compare

## 1. Folder Identity
- path: `app/work/processor_compare`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `7`
- immediate_child_files: `2`
- file_types: `.md` x 2

## 3. Child Folders
- `anchor_engine`
- `inputs`
- `observer_engine`
- `processor_outputs`
- `reports`
- `scripts`
- `standards`

## 4. Markdown Files
- `README.md`
  title: Processor Compare Pipeline
  summary: 이 작업 폴더는 동일 원문 입력에 대한 `codex / chatgpt / gemini` 출력값을 저장하고 비교하기 위한 sidecar 파이프라인이다.
- `root_retention_note_v1.md`
  title: processor_compare root retention note v1
  summary: `app/work/processor_compare` 는 support cluster이지만 현재는 root `app/work` 에 남긴다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `app.work.processor_compare`
- inventory_manifest: `runtime/manifests/folder_inventory/app.work.processor_compare.json`
- parent_folder: `app/work`
- related_status_files: `app/work/processor_compare/folder_status.md`
- last_updated: `2026-04-05T10:19:03+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
