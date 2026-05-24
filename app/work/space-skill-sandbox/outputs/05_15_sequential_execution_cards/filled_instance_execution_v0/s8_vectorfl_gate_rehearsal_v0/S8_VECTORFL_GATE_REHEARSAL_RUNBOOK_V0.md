# S8 VectorFL Gate Rehearsal v0

verdict:
  S8_VECTORFL_GATE_REHEARSAL_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Rehearse the S8 recovery gate as classification-only, using existing no-model evidence.

this is:
  receipt/residue/candidate/STOP classification rehearsal
  no-authority gate simulation

this is not:
  VectorFL authority mutation
  current-position update
  output_manifest update
  baseline/workflow/schema/registry/ontology/component promotion
  Gemini execution
  Codex execution

command:
  scripts/run_s8_vectorfl_gate_rehearsal_v0.py

expected verdict:
  S8_VECTORFL_GATE_REHEARSAL_CLASSIFIED_CANDIDATE_WITH_PROMOTION_HOLD

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
