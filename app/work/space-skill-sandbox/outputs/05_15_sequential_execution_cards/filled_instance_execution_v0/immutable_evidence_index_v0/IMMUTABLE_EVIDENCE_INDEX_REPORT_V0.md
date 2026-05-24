# Immutable Evidence Index v0

verdict:
  IMMUTABLE_EVIDENCE_INDEX_PRE_APPROVAL_LOCKED_WITH_EXECUTION_HOLD

base_dir:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0

file_count:
  87

packet_state:
  approval_no_count: 1
  approval_yes_count: 0
  promotion_no_count: 1

real_outputs_expected_absent:
  outputs/gemini_raw_output.txt: True
  outputs/gemini_lite_output.json: True
  outputs/codex_combined_bridge_recovery_return.md: True
  HERMES_EXECUTION_RECEIPT_V0.json: True
  HERMES_EXECUTION_REPORT_V0.md: True

purpose:
  Pre-approval checksum lockfile for all current execution_v0 artifacts.
  Use this to diff what changed after any future approval transition.

WATCH:
  checksum index mistaken as approval
  evidence lock mistaken as VectorFL authority

HOLD:
  real Gemini execution
  real Codex execution
  Hermes dispatch
  VectorFL authority mutation
  promotion

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
