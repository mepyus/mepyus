# Phase 1.7 Run 01 v0

## Scenario

space-first exploration with title-only reduction

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Find the first reading path and avoid title-only excerpts when grounding the evidence.' --mode exploration --stem phase1_7_run_01
```

Artifacts:

- `runtime/query_packets/phase1_7_run_01_question_packet.json`
- `runtime/exploration_results/phase1_7_run_01_exploration_result.json`
- `runtime/merge_diff_reports/phase1_7_run_01_merge_diff_report.json`
- `runtime/reingress_records/phase1_7_run_01_reingress_record.json`

## Interpretation

The run tests the main Phase 1.7 target: avoid title-only capture while preserving bounded excerpts. Compared with Phase 1.6 samples, `space_cli_phase1_goal_and_non_goal_v0.md` no longer returns only the title; it widens into the status block.

## Validation

- chosen_mode: `merge`
- title_only / metadata_only issues: 0
- poor excerpts: 0
- usable excerpts: 2
- strong excerpts: 4
- retried excerpts: 2
- pointer fallback: 0

Verdict: `PASS`
