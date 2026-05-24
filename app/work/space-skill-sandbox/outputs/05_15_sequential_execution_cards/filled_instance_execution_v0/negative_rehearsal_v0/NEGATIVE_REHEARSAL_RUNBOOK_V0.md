# Negative Rehearsal v0

verdict:
  NEGATIVE_REHEARSAL_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Prove bad synthetic outputs STOP before Codex/closeout/promotion paths.

this is:
  no-model bad fixture rehearsal
  validation failure-path test

this is not:
  Gemini execution
  Codex execution
  model API transport
  Hermes dispatch
  VectorFL authority mutation
  promotion

command:
  scripts/run_negative_rehearsal_v0.py

expected verdict:
  NEGATIVE_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
