# Approval Transition Instructions v0

verdict:
  APPROVAL_TRANSITION_INSTRUCTIONS_PREPARED_WITH_EXECUTION_HOLD

purpose:
  Define the exact final step that changes structure-ready into space-mediated model execution-ready.
  This file is not approval.

current packet:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md

current required line:
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no

only after explicit user packet-scoped execution approval, change exactly one approval field to:
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes

must remain unchanged:
  APPROVED_PROMOTION: no
  APPROVED_LIVE_WEB_SOURCE_LOOKUP: no
  APPROVED_EXTERNAL_CONNECTOR: no
  APPROVED_BROWSER_MCP: no
  APPROVED_MEMORY_SKILL_CRON_CONFIG_MUTATION: no
  APPROVED_VECTORFL_AUTHORITY_MUTATION: no

post-change first command:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh validate-static

then Gemini stage:
  I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh run-gemini-after-approval

then validate/materialize Gemini lite:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh materialize-lite

then Codex recovery stage:
  I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/run_execution_v0.sh run-codex-after-approval

then validate Codex return:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/validate_codex_recovery_return_v0.py

then close Hermes receipt/report:
  /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/scripts/write_hermes_execution_closeout_v0.py

critical distinction:
  This transition enables S5/S6 space-mediated model execution.
  It still does not approve promotion.
  It still does not mutate VectorFL authority.

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
