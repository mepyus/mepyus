# Space Utilization Map v0

verdict:
  SPACE_UTILIZATION_MAP_PREPARED_WITH_EXECUTION_HOLD

## 1. What the space currently contains

execution candidate packet:
  ../FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md

Gemini prompt contract:
  ../GEMINI_PROMPT_EXECUTION_V0.md

Codex recovery prompt contract:
  ../CODEX_RECOVERY_PROMPT_EXECUTION_V0.md

receipt/report contracts:
  ../HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
  ../HERMES_EXECUTION_REPORT_CONTRACT_V0.md

review-only lane:
  ../review_only_contract_shape_v0/CODEX_CONTRACT_SHAPE_REVIEW_ONLY_PROMPT_V0.md
  ../review_only_contract_shape_v0/HERMES_LOCAL_CONTRACT_SHAPE_PREFLIGHT_V0.md

execution harness:
  ../scripts/validate_execution_contract_v0.py
  ../scripts/materialize_gemini_lite_v0.py
  ../scripts/run_execution_v0.sh

approval gate:
  ../EXECUTION_APPROVAL_GATE_V0.md

runbook:
  ../HERMES_EXECUTION_READINESS_RUNBOOK_V0.md

future model outputs:
  ../outputs/gemini_raw_output.txt
  ../outputs/gemini_lite_output.json
  ../outputs/codex_combined_bridge_recovery_return.md

## 2. How the space will be used after approval

Gemini will not be used as free chat.
Gemini will be used as a bounded stage:
  input: GEMINI_PROMPT_EXECUTION_V0.md + declared reference files
  raw output: outputs/gemini_raw_output.txt
  lite output: outputs/gemini_lite_output.json
  completion: GEMINI_LITE_OUTPUT_DONE

Codex will not be used as free chat.
Codex will be used as a recovery stage:
  input 1: FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md
  input 2: outputs/gemini_lite_output.json
  input 3: outputs/gemini_raw_output.txt
  input 4: HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
  output: outputs/codex_combined_bridge_recovery_return.md
  completion: CODEX_RECOVERY_DONE

Hermes will not treat success as authority.
Hermes will close with:
  HERMES_EXECUTION_RECEIPT_V0.json
  HERMES_EXECUTION_REPORT_V0.md

VectorFL will not be mutated by execution.
VectorFL receives only:
  receipt / residue / candidate / STOP classification

## 3. Current non-action confirmation

The space is being used as:
  artifact surface
  contract surface
  validation surface
  future execution lane

The space is not yet being used as:
  Gemini execution lane
  Codex recovery lane
  VectorFL authority lane
  promotion lane

required_final_line:
  No execution was performed. No promotion was performed. Recovery class remains candidate.
