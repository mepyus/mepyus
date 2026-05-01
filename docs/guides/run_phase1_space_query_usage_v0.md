# Run Phase 1 Space Query Usage v0

## Purpose

`scripts/cli/run_phase1_space_query.py` is the Phase 1.5 entrypoint for repeated Codex CLI usage-loop runs. It binds the Phase 1 contracts into one command without promoting any document to baseline.

## Execution

Basic positional question:

```bash
python3 scripts/cli/run_phase1_space_query.py "Where should Codex start reading this space?" --stem phase1_5_example_01
```

Input file question:

```bash
python3 scripts/cli/run_phase1_space_query.py --input-file /path/to/question.txt --stem phase1_5_example_file_01
```

Optional explicit task mode:

```bash
python3 scripts/cli/run_phase1_space_query.py "Verify the Phase 1.5 usage loop" --mode verification --stem phase1_5_verify_01
```

Generated artifact set:

- `runtime/query_packets/<stem>_question_packet.json`
- `runtime/exploration_results/<stem>_exploration_result.json`
- `runtime/merge_diff_reports/<stem>_merge_diff_report.json`
- `runtime/reingress_records/<stem>_reingress_record.json`

The command prints a JSON summary with the chosen mode and paths.

## What The Entrypoint Does

1. Builds a question interpretation packet.
2. Proposes search targets from Phase 1/1.5 contracts.
3. Creates an exploration result with selected assets, discarded assets, evidence pointers, gaps, and tension markers.
4. Creates a merge/diff/hold report.
5. Creates a reingress record that links back to the previous three artifacts.

## What It Does Not Do

- It does not read every selected source and produce deep excerpts.
- It does not promote v0 documents to baseline.
- It does not move canonical paths.
- It does not perform UI work.
- It does not make final naming locks.

## Interpretation

A single entrypoint matters now because Phase 1 created compatible pieces but left the operator to remember the sequence. Phase 1.5 makes the sequence executable and repeatable while keeping each artifact small enough to inspect and refine.

The entrypoint is not meant to hide judgment. It creates a bounded draft set so Codex or a human can see where the question was interpreted, what was searched, what mode was chosen, and what returned to the space.

## Validation

A valid run must produce all four artifacts. A useful run should also:

- set `task_mode`;
- set `merge_mode_candidate`;
- list `search_targets`;
- preserve stop conditions;
- link artifact refs in the reingress record.
