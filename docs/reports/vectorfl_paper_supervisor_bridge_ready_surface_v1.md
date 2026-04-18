# VectorFL Paper Supervisor Bridge-Ready Surface v1

## purpose

- turn VectorFL Paper from a read-only viewer into a supervisor bridge-ready surface
- keep the read-only truth visible until Codex/Gemini connection is actually attached
- organize one operating line:
  - current context
  - worker handoff
  - result intake
  - supervisor decision

## supervisor bridge surface

- primary surface:
  - [run_vectorfl_paper_proper_mock.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_vectorfl_paper_proper_mock.py)
  - [index.html](/Users/sungsookim/universe/vectorfl_replica/runtime/views/vectorfl_paper_proper/index.html)

- four core zones:
  - current context
  - worker handoff slot
  - result intake slot
  - supervisor decision slot

## shortlist

### current context sources

- [vectorfl_paper_weekend_pilot_active_task_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_pilot_active_task_v0.json)
- [vectorfl_paper_proper_selection_state_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_proper_selection_state_v0.json)
- [vectorfl_paper_supervisor_current_board_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_supervisor_current_board_v0.json)
- [vectorfl_paper_pilot_current_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_pilot_current_v0.json)

### handoff sources

- [vectorfl_paper_weekend_pilot_cell_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_pilot_cell_registry_v0.json)
- [vectorfl_paper_proper_selection_presets_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_proper_selection_presets_v0.json)
- [vectorfl_paper_weekend_live_internal_read_output_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_internal_read_output_v1.json)
- [vectorfl_paper_weekend_live_external_resource_output_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_external_resource_output_v1.json)

### result intake sources

- [vectorfl_paper_weekend_live_translated_work_packet_v3.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_translated_work_packet_v3.json)
- [vectorfl_paper_weekend_live_append_only_trace_row_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_append_only_trace_row_v0.json)
- [vectorfl_paper_weekend_live_runtime_write_back_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_weekend_live_runtime_write_back_v0.json)
- [vectorfl_paper_weekend_live_reopen_case_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/vectorfl_paper_weekend_live_reopen_case_v0.json)

### supervisor decision sources

- [vectorfl_paper_weekend_live_synthesis_output_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_live_synthesis_output_v1.json)
- [vectorfl_paper_weekend_pilot_status_board_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/vectorfl_paper_weekend_pilot_status_board_v0.json)
- [vectorfl_paper_weekend_live_supervisor_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_paper_weekend_live_supervisor_report_v1.md)

## future connection memo

- where handoff will be emitted:
  - current worker handoff slot on the proper page

- where result will be ingested:
  - result intake slot on the proper page

- where supervisor action will be recorded:
  - supervisor decision slot on the proper page

- codex placeholder role:
  - deep reading
  - file inspection
  - patch / implementation
  - line tracing

- gemini placeholder role:
  - cross-check
  - review
  - bias / omission check
  - lightweight alternative reading

## alive operating line

- input/context observed
- handoff prepared
- external worker result placeholder
- supervisor decision prepared
- return path reserved

## note

- this surface is bridge-ready, not execution-ready
- no fake control should imply that Codex/Gemini is already attached
