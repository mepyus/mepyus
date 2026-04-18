# executable runner index v0

## Purpose

이 문서는 현재 repo 안의 실행 가능한 루프 / 스크립트를
`의도 -> 추천 명령 -> 남는 흔적` 기준으로 묶어 둔 빠른 찾기용 색인이다.

목적은 모든 스크립트를 설명하는 것이 아니라,
나중에 사용자가 정확한 파일명을 말하지 않아도
의도만으로 적절한 runner를 다시 찾을 수 있게 하는 것이다.

## Reading rule

- `plan-first`가 가능한 runner는 먼저 plan-first로 둔다.
- `sandbox-only` runner는 main runtime를 건드리지 않는다.
- `line_thickening` 계열은 해석 보조축 검증용이지 승격 엔진이 아니다.

## 1. external material intake / sweep

### A. 외부문서 전체를 공통 흐름선 기준으로 bounded sweep 한다

- when:
  - 외부자료 폴더 전체에서 `맥락 구조화 -> 에이전트 위임 -> 운영 자동화` 흐름선 접점을 훑고 싶을 때
- runner:
  - [run_external_case_flowline_sweep.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_flowline_sweep.py)
- command:
  - `python3 scripts/run_external_case_flowline_sweep.py`
- leaves:
  - [app/work/archive_review/external_case_support/external_case_flowline_sweep/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/external_case_support/external_case_flowline_sweep/generated)
- note:
  - read-only
  - no line promotion
  - no main runtime mutation

### B. structured markdown input을 실제 입력기로 넣기

- when:
  - 외부자료 `.md`를 정식 입력기로 통과시키고 싶을 때
- runner:
  - [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- command:
  - `python3 scripts/process_structured_doc_with_routing.py --doc inputs/external_cases/<file>.md`
- leaves:
  - receipt
  - label packet
  - origin map
  - observer ingest generated files

### C. raw external file 질감을 빠르게 훑기

- when:
  - 외부자료가 어떤 scene/flow 질감을 갖는지 먼저 보고 싶을 때
- runner:
  - [run_external_case_raw_intake_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_raw_intake_probe.py)
- command:
  - `python3 scripts/run_external_case_raw_intake_probe.py inputs/external_cases/<file>`
- leaves:
  - stdout json only
  - no broad runtime mutation

### D. 입력 전에 바로 넣어도 되는지 / 전처리가 필요한지 판다

- when:
  - 외부자료가 direct ingest 가능한지, transcript-aware 전처리가 먼저 필요한지 판단하고 싶을 때
- runner:
  - [run_external_input_gate.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_input_gate.py)
- command:
  - `python3 scripts/run_external_input_gate.py inputs/external_cases/<file>`
- leaves:
  - stdout json only
  - decision:
    - `direct_ingest_ok`
    - `preprocess_required`
    - `uncertain_needs_probe`
- note:
  - main runtime non-polluting
  - front-door gate only
  - `builder_choi_interview.txt` 같은 transcript-like input을 자막 조각으로 바로 넣지 않기 위한 판단층

### E. transcript-like raw input을 meaning chunk 쪽으로 다시 묶는다

- when:
  - gate가 `preprocess_required`를 반환한 transcript-like input을 바로 ingest하지 않고 정리하고 싶을 때
- runner:
  - [run_transcript_aware_regroup.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_aware_regroup.py)
- command:
  - `python3 scripts/run_transcript_aware_regroup.py inputs/external_cases/<file>`
- leaves:
  - [app/work/external_input_preprocess/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated)
- note:
  - main runtime non-polluting
  - timestamp / chapter marker / short interjection을 약화시키고 bounded chunk로 regroup
  - 전처리 전/후 gate를 같이 비교함

### F. 전처리 전/후를 같은 기준으로 바로 점검한다

- when:
  - transcript-aware regroup가 실제로 shard pressure를 줄였는지 확인하고 싶을 때
- runner:
  - [run_transcript_preprocess_comparison.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transcript_preprocess_comparison.py)
- command:
  - `python3 scripts/run_transcript_preprocess_comparison.py inputs/external_cases/<file>`
- leaves:
  - [app/work/external_input_preprocess/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated)
- note:
  - before/after gate
  - before/after dust split probe
  - ingest readiness read
  - main runtime non-polluting

### G. 전처리된 sidecar 기준으로 first pass를 얇게 본다

- when:
  - regroup 후 입력이 실제로 더 읽히는지, bounded first pass 면에서 확인하고 싶을 때
- runner:
  - [run_post_preprocess_first_pass_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_post_preprocess_first_pass_probe.py)
- command:
  - `python3 scripts/run_post_preprocess_first_pass_probe.py inputs/external_cases/<file>`
- leaves:
  - [app/work/external_input_preprocess/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated)
- note:
  - main runtime non-polluting
  - 전처리 sidecar를 만들고, 그 기준으로 first-pass readability / flatness / caution을 같이 남김

### H. external_cases 폴더 sweep loop 구조 준비 / 실행

- when:
  - 폴더 전체를 파일 단위 루프로 훑고 싶을 때
- runner:
  - [run_external_case_folder_sweep_loop.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_external_case_folder_sweep_loop.py)
- commands:
  - plan only:
    - `python3 scripts/run_external_case_folder_sweep_loop.py runtime`
  - bounded plan:
    - `python3 scripts/run_external_case_folder_sweep_loop.py runtime --limit 5`
  - filtered plan:
    - `python3 scripts/run_external_case_folder_sweep_loop.py runtime --include delta_society --include enterprise`
  - later execute:
    - `python3 scripts/run_external_case_folder_sweep_loop.py runtime --execute --limit 5`
- leaves:
  - [app/work/archive_review/external_case_support/external_case_folder_sweep/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/external_case_support/external_case_folder_sweep/generated)
- note:
  - 기본은 `plan_only`
  - 지금 단계에서는 broad execute보다 plan-first가 기본이다

## 2. grounded line_thickening feeds

### A. fragment grounded observer route

- when:
  - 실제 fragment direct-span 기반 observation을 넣고 싶을 때
- runner:
  - [apply_internal_observer.py](/Users/sungsookim/universe/vectorfl_replica/scripts/apply_internal_observer.py)
- command:
  - `python3 scripts/apply_internal_observer.py runtime <fragment_id> --record-line-thickening`
- bounded recurrence validation:
  - `python3 scripts/apply_internal_observer.py runtime <frag_a> <frag_b> --record-line-thickening --bounded-recurrence-validation`
- strongest lines:
  - `input_to_reading_organ`
  - 일부 fragment에서는 `transition_over_surface`

### B. source_fragment_view primary structured route

- when:
  - stored fragment/source view 기반 primary structured observation을 넣고 싶을 때
- runner:
  - [build_source_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_source_view.py)
- command:
  - `python3 scripts/build_source_view.py runtime --record-line-thickening --fragment-id <fragment_id>`
- strongest line:
  - `transition_over_surface`

### C. preflight summary route

- when:
  - preflight gate에서 summary-level line_thickening sink를 확인하고 싶을 때
- runner:
  - [run_runtime_preflight.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_runtime_preflight.py)
- command:
  - `python3 scripts/run_runtime_preflight.py runtime --mode space_reading --ref inputs/external_cases/<file> --record-line-thickening`
- note:
  - summary echo 계열
  - grounded feed와 같은 무게로 읽으면 안 된다

## 3. transition_over_surface validation chain

### A. targeted primary-material breadth validation

- when:
  - `transition_over_surface`의 primary material breadth를 늘려 볼 때
- runner:
  - [run_transition_over_surface_targeted_breadth_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_targeted_breadth_validation.py)
- command:
  - `python3 scripts/run_transition_over_surface_targeted_breadth_validation.py runtime`

### B. primary material breadth validation summary

- when:
  - representative strong line들의 primary material breadth 상태를 다시 읽고 싶을 때
- runner:
  - [run_primary_material_breadth_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_primary_material_breadth_validation.py)
- command:
  - `python3 scripts/run_primary_material_breadth_validation.py runtime`

### C. forward persistence confirmation

- when:
  - `transition_over_surface`의 `persistent_decay`가 primary-only refresh 뒤에도 유지되는지 볼 때
- runner:
  - [run_transition_over_surface_forward_persistence_confirmation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_forward_persistence_confirmation.py)
- command:
  - `python3 scripts/run_transition_over_surface_forward_persistence_confirmation.py runtime`

### D. residue robustness probe

- when:
  - recent-window 크기를 바꿔도 decaying/persistence 판정이 유지되는지 볼 때
- runner:
  - [run_transition_over_surface_residue_robustness_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_residue_robustness_probe.py)
- command:
  - `python3 scripts/run_transition_over_surface_residue_robustness_probe.py runtime`

### E. reintroduction sentinel refresh-only probe

- when:
  - main runtime current sentinel state만 다시 읽고 싶을 때
- runner:
  - [run_transition_over_surface_reintroduction_sentinel_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_reintroduction_sentinel_probe.py)
- command:
  - `python3 scripts/run_transition_over_surface_reintroduction_sentinel_probe.py runtime`

## 4. sandbox-only sentinel loop checks

### A. sandbox reintroduction trip

- when:
  - derived row를 recent window 안으로 다시 넣었을 때 sentinel이 실제 flip 되는지 보고 싶을 때
- runner:
  - [run_transition_over_surface_sandbox_reintroduction_trip.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_sandbox_reintroduction_trip.py)
- command:
  - `python3 scripts/run_transition_over_surface_sandbox_reintroduction_trip.py runtime`
- expected:
  - before `observed_but_outside_window`
  - after `observed_recently`
- note:
  - sandbox only
  - main runtime non-polluting

### B. sandbox recovery loop close

- when:
  - trip 뒤에 primary-only refresh로 sentinel을 다시 밖으로 밀 수 있는지 볼 때
- runner:
  - [run_transition_over_surface_sandbox_recovery_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_transition_over_surface_sandbox_recovery_check.py)
- command:
  - `python3 scripts/run_transition_over_surface_sandbox_recovery_check.py runtime`
- expected:
  - before `observed_but_outside_window`
  - trip `observed_recently`
  - recovery `observed_but_outside_window`
- note:
  - sandbox only
  - loop proof, not production causality proof

## 5. simple sample / smoke

### A. line_thickening sample

- when:
  - minimal synthetic sample로 registry/log/promotion만 빠르게 확인할 때
- runner:
  - [run_line_thickening_sample.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_line_thickening_sample.py)
- command:
  - `python3 scripts/run_line_thickening_sample.py`

### B. replica smoke check

- when:
  - repo 전반이 크게 깨지지 않았는지 간단 확인할 때
- runner:
  - [run_replica_smoke_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_replica_smoke_check.py)
- command:
  - `python3 scripts/run_replica_smoke_check.py`

## 6. operating screen internal search

### A. capability-aware internal search minimum panel

- when:
  - 운용화면에서 reading candidate 와 capability candidate 를 함께 찾고 싶을 때
- runner:
  - [run_internal_search_operating_panel_demo.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_internal_search_operating_panel_demo.py)
- command:
  - `python3 scripts/run_internal_search_operating_panel_demo.py runtime --query "input observer"`
  - `python3 scripts/run_internal_search_operating_panel_demo.py runtime --query "sandbox trip" --query "validation"`
- leaves:
  - [app/work/operating_ui/generated/](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/generated)
- note:
  - read-only over runtime logs / registry + capability registry
  - main runtime non-polluting
  - result_type distinguishes `reading_result` vs `capability_result`

## 7. intent shortcuts

- “외부자료 하나 정식 입력기로 넣어”
  - `process_structured_doc_with_routing.py`
- “외부자료 질감만 한번 봐”
  - `run_external_case_raw_intake_probe.py`
- “external_cases 폴더 훑는 루프 준비해”
  - `run_external_case_folder_sweep_loop.py`
- “transition_over_surface sentinel 지금 상태만 봐”
  - `run_transition_over_surface_reintroduction_sentinel_probe.py`
- “sentinel sandbox에서 실제 flip 되는지 봐”
  - `run_transition_over_surface_sandbox_reintroduction_trip.py`
- “flip 뒤 recovery까지 닫아봐”
  - `run_transition_over_surface_sandbox_recovery_check.py`
- “fragment grounded로 line_thickening 넣어”
  - `apply_internal_observer.py`
- “source view 기반 primary structured 넣어”
  - `build_source_view.py`
- “운용화면 내부검색 panel 보여줘”
  - `run_internal_search_operating_panel_demo.py`
