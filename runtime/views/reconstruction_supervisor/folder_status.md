# folder_status / runtime/views/reconstruction_supervisor

## 1. Folder Identity
- path: `runtime/views/reconstruction_supervisor`
- role_guess: Supervisor-facing bounded reconstruction packet surfaces and their lightweight navigation aids.
- status_mode: `builder_generated_surface_summary`

## 2. Snapshot
- immediate_child_dirs: `0`
- immediate_child_files: `9`
- file_types: `.json` x 4, `.md` x 5

## 3. Child Folders
- none

## 4. Core Files
- `index.json`
  summary: machine-readable navigation index for current reconstruction packet set
- `index.md`
  summary: human-readable navigation index and read order note
- `reconstruction_openai_02_11_f338ace89474ee93.json`
  summary: reconstruction packet for `openai_02_11`
- `reconstruction_openai_02_11_f338ace89474ee93.md`
  summary: human-readable companion for `openai_02_11`
- `reconstruction_openai_02_11_run_20260403_184903_920534_18de5b4f_1ea134.json`
  summary: reconstruction packet for `openai_02_11`
- `reconstruction_openai_02_11_run_20260403_184903_920534_18de5b4f_1ea134.md`
  summary: human-readable companion for `openai_02_11`
- `reconstruction_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_run_20260403_184903_920534_18de5b4f_1ea134.json`
  summary: reconstruction packet for `tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`
- `reconstruction_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_run_20260403_184903_920534_18de5b4f_1ea134.md`
  summary: human-readable companion for `tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`

## 5. Current Use Hint
- `runtime/views/reconstruction_supervisor_latest.*` 는 latest surfaced pointer다.
- `index.*` 는 navigation surface다.
- per-reconstruction `json`이 authoritative reconstruction artifact다.
- `md`는 operator/supervisor reread companion이다.
- 이 폴더는 decision surface가 아니라 read-only reconstruction surface다.

## 6. Read Order
- 먼저 `runtime/views/reconstruction_supervisor_latest.json` 또는 `.md`를 본다.
- 필요하면 `runtime/views/reconstruction_supervisor/index.json` 또는 `.md`로 이동한다.
- 다음으로 target reconstruction packet `json`을 본다.
- 사람이 다시 읽을 때만 companion `md`를 본다.

## 7. Guard Note
- no decision logic
- no governing behavior
- no state mutation
- latest is not authoritative
- sidecar / receipt / views role separation must remain visible

## 8. Updated At
- updated_at: `2026-04-05T08:55:26+09:00`
