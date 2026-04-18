# folder_status / source_assets/external_case_inputs

## 1. Folder Identity
- path: `source_assets/external_case_inputs`
- role_guess: Folder with mixed project assets; inspect child folders and markdown files for exact role.
- status_mode: `rendered_from_inventory`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `15`
- file_types: `.md` x 15

## 3. Child Folders
- none

## 4. Markdown Files
- `choi_ai_classroom_transformer1_input_v1.md`
  title: choi_ai_classroom_transformer1_input_v1
  summary: [[A]] [[OBJ:external_case_input]] [[SEM:choi_ai_classroom_transformer1_input_v1]]
- `choi_ai_classroom_transformer2_input_v1.md`
  title: choi_ai_classroom_transformer2_input_v1
  summary: [[A]] [[OBJ:external_case_input]] [[SEM:choi_ai_classroom_transformer2_input_v1]]
- `external_case_first_pass_aifrontier_01_28_input_v1.md`
  title: CODEx 지시서 — aifrontier_01_28 canonical first pass v1
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:external_case_first_pass_aifrontier]] [[SEM:aifrontier_repeat_check_with_saltlux]]
- `external_case_first_pass_alexkarp_youtube_input_v1.md`
  title: External Case First Pass — alexkarp_youtube.txt canonical input v1
  summary: - case_name: `alexkarp_youtube_raw_transcript_v1` - source_ref: `inputs/external_cases/alexkarp_youtube.txt` - source_type: `external_case_primary_transcript` - source_origin: `raw_talk_or_conversation_transcript`
- `external_case_first_pass_andrej_karpathy_youtube_input_v1.md`
  title: External Case First Pass — andrej_karpathy_youtube.txt canonical input v1
  summary: - case_name: `andrej_karpathy_youtube_raw_transcript_v1` - source_ref: `inputs/external_cases/andrej_karpathy_youtube.txt` - source_type: `external_case_primary_transcript` - source_origin: `raw_youtube_interview_transcript`
- `external_case_first_pass_andrewng_stanford_input_v1.md`
  title: External Case First Pass — andrewng_stanford.txt canonical input v1
  summary: - case_name: `andrewng_stanford_raw_transcript_v1` - source_ref: `inputs/external_cases/andrewng_stanford.txt` - source_type: `external_case_primary_transcript` - source_origin: `raw_talk_or_keynote_transcript`
- `external_case_first_pass_dario_amodei_youtube_input_v1.md`
  title: External Case First Pass — dario_amodei_youtube.txt canonical input v1
  summary: - case_name: `dario_amodei_youtube_raw_transcript_v1` - source_ref: `inputs/external_cases/dario_amodei_youtube.txt` - source_type: `external_case_primary_transcript` - source_origin: `raw_youtube_interview_transcript`
- `external_case_first_pass_enterprise_input_v1.md`
  title: External Case First Pass — enterprise.txt canonical input v1
  summary: - case_name: `enterprise_ai_adoption_and_ultrathink_raw_transcript_v1` - source_ref: `enterprise.txt` - source_type: `external_case_primary_transcript` - source_origin: `raw_podcast_or_talk_transcript`
- `external_case_first_pass_oh_my_opencode_input_v1.md`
  title: CODEx 지시서 — oh_my_opencode canonical first pass v1
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:external_case_first_pass_oh_my_opencode]] [[SEM:oh_my_opencode_repeat_check_with_prev_cases]]
- `external_case_first_pass_saltlux_ai_input_v1.md`
  title: external_case_first_pass_saltlux_ai_input_v1
  summary: [[A]] [[OBJ:external_case_input]] [[SEM:saltlux_ai_single_case_reality_test_v1]]
- `external_case_first_pass_saltlux_raw_transcript_input_v2.md`
  title: CODEx 입력문 v2 — saltlux.txt canonical first pass
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:external_case_first_pass_raw_transcript]] [[SEM:saltlux_canonical_raw_transcript_first_pass]]
- `external_case_first_pass_saltlux_secondary_summary_input_v1.md`
  title: CODEx 입력문 — Saltlux Secondary Summary First Pass v1
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:external_case_first_pass_secondary_summary]] [[SEM:saltlux_secondary_summary_first_pass]]
- `external_case_first_pass_v1.md`
  title: CODEx 지시서 — External Case First Pass v1
  summary: [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]] [[A]] [[OBJ:external_case_first_pass]] [[SEM:thin_operation_rules_live_validation]]
- `saltlux_ai_summary_pair_validation_input_v1.md`
  title: saltlux_ai_summary_pair_validation_input_v1
  summary: [[A]] [[OBJ:external_case_input]] [[SEM:saltlux_ai_summary_pair_validation_v1]]
- `saltlux_ai_vs_ontology_youtube_compare_input_v1.md`
  title: saltlux_ai_vs_ontology_youtube_compare_input_v1
  summary: [[A]] [[OBJ:external_case_input]] [[SEM:saltlux_ai_vs_ontology_youtube_compare_v1]]

## 5. Code / Data Files
- no immediate code/data files

## 6. Current Use Hint
- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.
- 이 문서는 원장이 아니라 읽기면이다.

## 7. Inventory Link
- folder_key: `source_assets.external_case_inputs`
- inventory_manifest: `runtime/manifests/folder_inventory/source_assets.external_case_inputs.json`
- parent_folder: `source_assets`
- related_status_files: `source_assets/external_case_inputs/folder_status.md`
- last_updated: `2026-03-28T06:51:36+09:00`

## 8. Render Rule
- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.
- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.
- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.
