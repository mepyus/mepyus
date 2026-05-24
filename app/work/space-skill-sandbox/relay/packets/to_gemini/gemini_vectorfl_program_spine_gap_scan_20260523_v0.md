# GEMINI_VECTORFL_PROGRAM_SPINE_GAP_SCAN_20260523_V0

## 1. Work Order Status

cycle_id:
  vectorfl_program_spine_stabilization_20260523

work_order_id:
  gemini_vectorfl_program_spine_gap_scan_20260523_v0

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  broad bounded internal exploration / gap detection

authority:
  work order only

not:
  repo modification
  Obsidian modification
  implementation
  workflow
  registry
  schema
  baseline
  automation
  current-position update
  output_manifest update
  final authority

## 2. Purpose

VectorFL now has local implementation evidence:

- Phase 0.5 local SQLite + CLI + Markdown export prototype
- Phase 1 local read-only Web/API MVP skeleton
- 05-21 Obsidian local no-model operating loop and CLI skeleton candidate
- 05-22 Input Localization candidate package

Codex found a concrete program-design defect:

Phase 0.5 guardrail probes append to the shared SQLite DB, which changes live counts and breaks Phase 1 tests that assert fixed baseline counts.

Gemini should perform a bounded broad scan to find related test-isolation, replay-drift, shared-state, receipt-count, and baseline-count risks across the recent VectorFL material.

## 3. Required Read Scope

Read:

- `/Users/sungsookim/universe/vectorfl_replica/app/work/CODEX_GEMINI_HERMES_OPERATING_SPLIT_20260523_V0.md`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/README.md`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/BASELINE_REPLAY_VALIDATOR.md`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/probes/guardrail_probe_runner.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/README.md`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py`
- `/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/62.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/66.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-22/CHATGPT_CODEX_GEMINI_TODAY_HANDOFF_SUMMARY_V0.md`

Optional if needed:

- Obsidian `05-18` final dashboard / structural validation files
- Obsidian `05-19` real S5/S8 receipt and postmortem files
- Obsidian `05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/scripts/`
- Obsidian `05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/outputs/`

## 4. Do Not Read

- entire repo
- entire Obsidian vault
- credential or token material
- unrelated raw logs
- node_modules
- broad runtime cli_sessions unless explicitly needed

## 5. Gemini Task

Answer:

1. Where does VectorFL currently mix baseline evidence and live/probe execution state?
2. Which tests or validators appear brittle because they assert fixed counts instead of invariants?
3. Which recent 05-* assets already describe replay drift, receipt hardening, baseline lock, or test isolation?
4. What are the smallest candidate structural fixes Codex should design?
5. What should Hermes execute only after Codex makes an exact packet?

## 6. Return Format

Verdict:
  GEMINI_PROGRAM_SPINE_GAP_SCAN_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / HOLD

Directly inspected:
  - ...

Not inspected:
  - ...

Main finding:
  ...

Shared-state risks:
  - ...

Fixed-count brittleness:
  - ...

Relevant existing assets:
  - ...

Candidate structural fixes for Codex:
  - ...

Hermes execution candidates:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do Not Promote:
  - no authority mutation
  - no promotion
  - no Program Alpha claim
  - no M3/M4 claim
  - no router/runner claim

## 7. Hard Boundaries

- no repo modification
- no Obsidian modification
- no implementation
- no automation
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no final authority claim
