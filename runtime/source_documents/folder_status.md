# folder_status / runtime/source_documents

## 1. Folder Identity
- path: `runtime/source_documents`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `1`
- file_types: `.md` x 1

## 3. Child Folders
- none

## 4. Markdown Files
- `youtube_exam_excerpt.md`
  title: youtube_exam_excerpt
  summary: 최승준 참 또 하나 흥미로운 게 있었는데, 37수이 건물이 됐더라고요. AlphaGo의 그 놀라운 수라고. 인간인 이세돌 9단의 놀라운 수가 몇 수였죠? 78수였네요. 78수고 AlphaGo의 37수인데, 그 37수의 이름을 따라서 저 Google DeepMind 신사옥이 생기나 봅니다. 여름부터 입주를 한다고 하는데요.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `runtime.source_documents`
- inventory_manifest: `runtime/manifests/folder_inventory/runtime.source_documents.json`
- parent_folder: `runtime`
- related_status_files: `runtime/source_documents/folder_status.md`
- last_updated: `2026-04-05T16:50:15+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
