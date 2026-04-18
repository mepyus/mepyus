# folder_status / docs/reports/space_structure

## 1. Folder Identity
- path: `docs/reports/space_structure`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `4`
- file_types: `.md` x 4

## 3. Child Folders
- none

## 4. Markdown Files
- `folder_inventory_delta_sync_review_v1.md`
  title: folder_inventory_delta_sync_review_v1
  summary: 변화분 기반 폴더 운용 레이어의 최소 구성을 기록한다.
- `folder_structure_recheck_v1.md`
  title: folder_structure_recheck_v1
  summary: 현재 폴더 트리를 다시 점검해서 - 정상 역할 분리 - 실제 수정 대상 - 지금은 그대로 두는 것이 맞는 혼합 상태 를 다시 구분한다.
- `folder_tree_duplicate_review_v1.md`
  title: folder_tree_duplicate_review_v1
  summary: 이 문서는 현재 폴더 트리를 다시 점검한 결과, 무엇이 **정상 분리**이고 무엇이 **실제 정리 대상**인지 정리한 리뷰 문서다.
- `README.md`
  title: space_structure report family
  summary: 이 폴더는 공간 정리, 폴더 역할, 중복/혼합 상태 점검을 다루는 보고서를 하나의 구조 벨트로 모은 공간이다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.reports.space_structure`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.reports.space_structure.json`
- parent_folder: `docs/reports`
- related_status_files: `docs/reports/space_structure/folder_status.md`
- last_updated: `2026-04-05T09:56:49+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
