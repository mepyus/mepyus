# folder_status / docs/reports/multi_lens

## 1. Folder Identity
- path: `docs/reports/multi_lens`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `3`
- file_types: `.md` x 3

## 3. Child Folders
- none

## 4. Markdown Files
- `multi_lens_document_reading_v0_integrated_flow_cohort_observation_report.md`
  title: multi_lens_document_reading_v0 integrated flow cohort observation report
  summary: - integrated `multi_lens_document_reading_v0` flow was observed across a small structured-doc cohort - current artifacts showed stable shape and stable handoff semantics - this report records observational behavior only and does not introdu
- `multi_lens_input_to_reading_organ_basis_quality_post_patch_cohort_report.md`
  title: multi_lens_input_to_reading_organ_basis_quality_post_patch_cohort_report
  summary: - post-patch cohort validation was completed for the bounded `input_to_reading_organ` basis-quality branch - current evidence shows wording clarity improved while strength distribution, operating state, and handoff behavior remained stable
- `README.md`
  title: multi_lens report family
  summary: 이 폴더는 `docs/reports/` 아래에 흩어져 있던 multi-lens 계열 보고서를 하나의 emergent line belt로 읽기 쉽게 모은 공간이다.

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.reports.multi_lens`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.reports.multi_lens.json`
- parent_folder: `docs/reports`
- related_status_files: `docs/reports/multi_lens/folder_status.md`
- last_updated: `2026-04-05T09:56:49+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
