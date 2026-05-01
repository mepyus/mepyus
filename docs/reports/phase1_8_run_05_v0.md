# Phase 1.8 Run 05 v0

## Scenario

mixed prose + structured case

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Mix prose grounding rules with JSON runtime contracts and show which field paths should re-enter as learning memory.' --mode merge --stem phase1_8_run_05
```

Artifacts:

- `runtime/query_packets/phase1_8_run_05_question_packet.json`
- `runtime/exploration_results/phase1_8_run_05_exploration_result.json`
- `runtime/merge_diff_reports/phase1_8_run_05_merge_diff_report.json`
- `runtime/reingress_records/phase1_8_run_05_reingress_record.json`

## Interpretation

The run checks that prose evidence and structured evidence can coexist. Reingress now records salient paths, reusable structured assets, and generated asset reading notes.

## Validation

- chosen_mode: `merge`
- salient_path evidence: 18
- reingress contract: `space_reingress_record_v2`
- salient_paths_summary: present
- reusable_structured_assets: present

Verdict: `PASS`
