# Phase 1.6 Run 01 v0

## Scenario

space-first exploration with grounded excerpts

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Find the first reading path and include grounded evidence excerpts for why these sources matter.' --mode exploration --stem phase1_6_run_01
```

Artifacts:

- `runtime/query_packets/phase1_6_run_01_question_packet.json`
- `runtime/exploration_results/phase1_6_run_01_exploration_result.json`
- `runtime/merge_diff_reports/phase1_6_run_01_merge_diff_report.json`
- `runtime/reingress_records/phase1_6_run_01_reingress_record.json`

## Interpretation

Compared with Phase 1.5, this run no longer records only selected paths. It adds excerpt windows, line pointers, excerpt modes, local confidence, cross-support refs, and an evidence depth summary.

## Validation

- chosen_mode: `merge`
- pointer_only evidence: 0
- grounded evidence: 6
- excerpt modes observed: `heading_plus_block`, `bullet_cluster`
- reingress learning fields: present
- manual support: still needed for title-only excerpts that are locally grounded but semantically thin.

Verdict: `PASS_WITH_NOTE`
