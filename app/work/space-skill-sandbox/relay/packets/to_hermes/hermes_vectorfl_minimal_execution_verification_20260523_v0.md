# HERMES_VECTORFL_MINIMAL_EXECUTION_VERIFICATION_20260523_V0

## 1. Packet Status

packet_id:
  hermes_vectorfl_minimal_execution_verification_20260523_v0

status:
  READY_FOR_HERMES_WHEN_NEEDED

target:
  Hermes

role:
  minimal local execution / validator rerun / receipt materialization only

authority:
  execution packet only

not:
  broad exploration
  structure design
  promotion
  authority mutation
  schema/registry/baseline mutation
  router/runner implementation
  external model/tool/network expansion

## 2. Purpose

Use Hermes only for necessary execution, because Hermes also consumes GPT-5.5-level resources.

Hermes should not redo Codex structural reasoning or Gemini broad exploration.

Hermes should run only exact validators/tests requested by Codex after a packet is prepared.

## 3. Current Known Verification Commands

Safe local checks already used:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tests/transition_table_validator.py
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_phase1_server.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-19/116_S4_REAL_EXECUTION_GATE_DRAFT_V0/validate_real_s5_s8_outputs.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/scripts/validate_cli_skeleton.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/scripts/validate_local_operating_outputs.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/scripts/validate_receipt_manifest_hardened.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-21/VECTORFL_LOCAL_OPERATING_SETUP_V0/scripts/replay_decision_surface_consistency.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-22/INPUT_LOCALIZATION_HERMES_LOCALIZATION_V0/validate_input_localization_minimal_profile_instance_set_v0.py'
python3 '/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-22/CODEX_RE_ENTRY_RECOGNITION_PACKET_V0/validate_codex_re_entry_recognition_packet_v0.py'
```

## 4. WATCH Before Running

Do not rerun mutable probes against the shared Phase 0.5 SQLite DB unless Codex explicitly asks for live mutation evidence.

Known mutable command:

```bash
python3 app/work/vectorfl_ops_phase_0_5/probes/guardrail_probe_runner.py
```

This appends probe requests and guardrail events to:

```text
app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite
```

## 5. Required Hermes Return

Return:

```text
verdict:
commands_run:
pass:
fail:
state_mutations_observed:
files_written:
receipts_created_or_updated:
WATCH:
HOLD:
next_smallest_action:
```

## 6. HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- baseline/schema/registry mutation: NO unless separately approved
