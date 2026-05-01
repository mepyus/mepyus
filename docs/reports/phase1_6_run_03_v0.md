# Phase 1.6 Run 03 v0

## Scenario

diff-heavy case with evidence-depth awareness

## Execution

Command:

```bash
python3 scripts/cli/run_phase1_space_query.py 'Compare pointer-only evidence with grounded evidence and preserve any diff in merge risk.' --mode comparison --stem phase1_6_run_03
```

Artifacts:

- `runtime/query_packets/phase1_6_run_03_question_packet.json`
- `runtime/exploration_results/phase1_6_run_03_exploration_result.json`
- `runtime/merge_diff_reports/phase1_6_run_03_merge_diff_report.json`
- `runtime/reingress_records/phase1_6_run_03_reingress_record.json`

## Interpretation

This run confirms comparison mode still chooses `diff`, but now the diff report includes evidence depth summary, confidence distribution, and strongest support refs. The mode is no longer only task-mode based; it carries grounding context into the report.

## Validation

- chosen_mode: `diff`
- pointer_only evidence: 0
- grounded evidence: 6
- strongest_support_refs: present
- evidence_depth_considered: true
- manual support: still needed to decide whether diff should remain after deeper human reading.

Verdict: `PASS`
