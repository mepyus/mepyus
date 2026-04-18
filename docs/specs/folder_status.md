# folder_status / docs/specs

## 1. Folder Identity
- path: `docs/specs`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `7`
- file_types: `.md` x 7

## 3. Child Folders
- none

## 4. Markdown Files
- `folder_role_table_v1.md`
  title: folder_role_table_v1
  summary: 이 문서는 프로그램급 작업공간으로 승격하는 과정에서 각 폴더가 무엇을 담당하는지, 무엇을 두면 안 되는지, 새 파일이 생겼을 때 어디로 배치해야 하는지를 빠르게 판단하기 위한 **폴더 역할표 v1** 이다.
- `middle_layer_layered_implementation_note_v1.md`
  title: middle layer layered implementation note v1
  summary: - experimental - read-only - no `inputter.py` patch - no `labeler.py` patch - no promotion logic touch
- `middle_layer_requirement_before_fix_v1.md`
  title: middle layer requirement before fix v1
  summary: - define the missing functions between raw intake and case-level frame extraction. - this is a requirement note, not a patch note.
- `repeated_second_order_pattern_table_draft_v1.md`
  title: repeated second-order pattern table draft v1
  summary: [[A]] [[OBJ:repeated_second_order_pattern_table_draft_v1]] [[SEM:pattern_first_table_before_object_lift]]
- `second_order_next_loop_entry_gate_v1.md`
  title: second-order next loop entry gate v1
  summary: [[A]] [[OBJ:second_order_next_loop_entry_gate_v1]] [[SEM:entry_gate_for_next_validation_loop_after_three_axis_integration]]
- `second_order_readable_condition_table_draft_v1.md`
  title: second-order readable condition table draft v1
  summary: [[A]] [[OBJ:second_order_readable_condition_table_draft_v1]] [[SEM:readability_conditions_for_second_order_outputs_before_object_lift]]
- `second_order_scaffold_reduction_priority_matrix_v1.md`
  title: second-order scaffold reduction priority matrix v1
  summary: [[A]] [[OBJ:second_order_scaffold_reduction_priority_matrix_v1]] [[SEM:priority_matrix_for_reducing_scaffold_dependency_before_object_lift]]

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `docs.specs`
- inventory_manifest: `runtime/manifests/folder_inventory/docs.specs.json`
- parent_folder: `docs`
- related_status_files: `docs/specs/folder_status.md`
- last_updated: `2026-03-28T19:33:43+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
