# Phase 1.5 Usage Loop Binding Validation Report v0

## Final Verdict

`PASS_WITH_NOTE`

Phase 1.5 successfully binds the Phase 1 documents, contracts, and CLI skeletons into a repeatable Codex CLI usage loop. One command can now produce the four required artifacts for a bounded user question:

- question packet
- exploration result
- merge/diff/hold report
- reingress record

The note is that the loop is operational binding, not deep automation. It proposes paths and evidence pointers, but does not yet perform full source reading, excerpt extraction, or semantic confidence scoring.

## Execution

Implemented/updated:

- `scripts/cli/run_phase1_space_query.py`
  - now the central entrypoint;
  - accepts positional question or `--input-file`;
  - creates all artifact directories if needed;
  - runs packet -> exploration -> merge/diff/hold -> reingress;
  - prints machine-readable JSON summary.
- `scripts/cli/build_question_packet.py`
  - infers task mode unless explicitly supplied;
  - fills interpreted goal, non-goals, search targets, merge candidate, and stop conditions;
  - records hard hold/provisional ambiguity.
- `scripts/cli/explore_space.py`
  - turns packet search targets into selected assets and evidence pointers;
  - records discarded assets and gaps;
  - marks stop candidates as tension/conflict assets.
- `scripts/cli/merge_or_diff.py`
  - reads packet and exploration result;
  - applies merge/diff/hold candidate;
  - sets decision-required flags for hold cases.
- `scripts/cli/write_reingress_record.py`
  - links generated artifact refs;
  - preserves chosen mode and unresolved tensions;
  - creates a reusable reingress trace.

New docs/reports:

- `docs/reports/phase1_5_asset_audit_and_gap_report_v0.md`
- `docs/guides/run_phase1_space_query_usage_v0.md`
- `docs/specs/phase1_5_decision_gate_rules_v0.md`
- `docs/reports/phase1_5_run_01_v0.md`
- `docs/reports/phase1_5_run_02_v0.md`
- `docs/reports/phase1_5_run_03_v0.md`
- `docs/reports/phase1_5_run_04_v0.md`
- `docs/reports/phase1_5_run_05_v0.md`

Runtime runs:

- `phase1_5_run_01`: space-first exploration, chosen mode `merge`
- `phase1_5_run_02`: mixed Codex + space reflection, chosen mode `merge`
- `phase1_5_run_03`: diff-heavy comparison, chosen mode `diff`
- `phase1_5_run_04`: authority/naming hold trigger, chosen mode `hold`
- `phase1_5_run_05`: reingress-valuable run, chosen mode `merge`

Each run generated:

- `runtime/query_packets/<stem>_question_packet.json`
- `runtime/exploration_results/<stem>_exploration_result.json`
- `runtime/merge_diff_reports/<stem>_merge_diff_report.json`
- `runtime/reingress_records/<stem>_reingress_record.json`

## Interpretation

## Now Repeatedly Usable

- A user question can enter through one CLI command.
- The command creates all four artifacts in stable runtime lanes.
- Question mode and merge/diff/hold candidate are populated.
- Stop candidates are represented in packet, merge report, and reingress.
- Reingress records link back to the three prior artifacts.
- The loop can be run repeatedly without UI, baseline promotion, or path migration.

## Still Needs Manual Support

- Evidence units are pointer-level, not deep excerpt-level.
- The code does not inspect the full content of selected sources.
- Confidence is coarse and rule-based.
- Stop condition detection is keyword-assisted, not full semantic review.
- Run reports are still written manually after the runtime artifacts are produced.

## Needs More Runs Before Baseline Promotion

- Whether the v0 artifact lane names are stable enough.
- Whether `task_mode` inference needs more modes or fewer modes.
- Whether stop keyword detection is too broad or too narrow.
- Whether reingress records need an index/latest view.
- Whether evidence pointer generation should become excerpt extraction.

## Validation

Validation commands/checks performed:

- Python compile check for all five CLI scripts: PASS.
- JSON parse check for all Phase 1.5 run artifacts: PASS.
- Artifact chain check for runs 01-05: PASS.
- Mode check:
  - run 01: `exploration -> merge`
  - run 02: `reflection_support -> merge`
  - run 03: `comparison -> diff`
  - run 04: `verification + stop terms -> hold`
  - run 05: `merge -> merge`
- Reingress artifact refs present for all five runs: PASS.

## Risks / Thin Areas

- The loop may produce plausible-looking drafts even when selected assets need deeper reading.
- Keyword stop detection can miss implicit authority conflicts.
- `--force-merge-mode` can override behavior if misused, so normal usage should omit it.
- No JSON Schema validation exists yet; parse validity is not contract completeness.
- The runtime folders can accumulate drafts without an index policy.

## User Decision Required

No immediate user decision is required.

No baseline meaning was changed. No canonical path was moved. No final naming lock was made. No large structural alternative was selected.

## Recommended Next Step

Continue using `scripts/cli/run_phase1_space_query.py` for real bounded questions and review the generated artifacts. After enough repeated runs, decide whether to add:

- a runtime index for Phase 1.5 runs;
- content excerpt extraction;
- stricter JSON Schema validation;
- a promotion checklist for any contract that repeatedly proves stable.
