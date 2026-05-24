# Hermes Execution Readiness Runbook v0

verdict:
  EXECUTION_V0_HARNESS_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Build the execution candidate up to the point where Gemini and Codex can run after explicit approval, while preserving HOLD now.

current_state:
  execution_prep_only
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no
  APPROVED_PROMOTION: no

safe_now:
  Local/static validation only:
    /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh validate-static

not_safe_until_explicit_approval:
  Gemini execution
  Codex recovery execution
  model API transport for bridge execution
  Hermes dispatch
  promotion

approval_required_before_real_run:
  1. User explicitly approves this packet for execution.
  2. Packet is intentionally updated to:
       EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
  3. APPROVED_PROMOTION remains:
       APPROVED_PROMOTION: no
  4. Operator runs real commands with:
       I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes

execution_sequence_after_approval_only:
  1. Static validation:
       /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh validate-static

  2. Gemini stage:
       I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh run-gemini-after-approval

     expected writes:
       /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt
       /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_lite_output.json

     required completion:
       GEMINI_LITE_OUTPUT_DONE

  3. Codex recovery stage:
       I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh run-codex-after-approval

     expected write:
       /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/codex_combined_bridge_recovery_return.md

     required completion:
       CODEX_RECOVERY_DONE

  4. Hermes closeout:
       write HERMES_EXECUTION_RECEIPT_V0.json
       write HERMES_EXECUTION_REPORT_V0.md
       preserve promotion HOLD

prepared_files:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/validate_execution_contract_v0.py
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/materialize_gemini_lite_v0.py
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/EXECUTION_COMMAND_MANIFEST_V0.json
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/EXECUTION_APPROVAL_GATE_V0.md

WATCH:
  command harness mistaken as current execution approval
  env var mistaken as packet approval
  packet approval mistaken as promotion approval
  Gemini output mistaken as truth
  Codex recovery mistaken as VectorFL authority mutation

HOLD:
  real Gemini execution until approval yes
  real Codex execution until approval yes and Gemini outputs valid
  promotion
  VectorFL authority mutation
  live web/source lookup
  external connector

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
