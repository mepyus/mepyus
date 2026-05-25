# Filled Bounded Combined Bridge Packet Execution v0

## 1. Verdict

```text
FILLED_INSTANCE_EXECUTION_V0_PREPARED_WITH_EXECUTION_HOLD
```

## 2. Packet Identity

```text
PACKET_ID: FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0
STATUS: approved_execution_completed_with_promotion_hold
SOURCE_DRY_RUN_REFERENCE: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/template_instance_dry_run_v0/
SOURCE_DRY_RUN_MUTATION_ALLOWED: no
REAL_EXECUTION_STATUS: S5_S6_S7_completed_S8_classification_only
REAL_GEMINI_EXECUTION: yes
REAL_CODEX_EXECUTION: yes
MODEL_API_TRANSPORT_USED: yes
LIVE_WEB_SOURCE_LOOKUP_USED: no
EXTERNAL_CONNECTOR_USED: no
PROMOTION_STATUS: no promotion
AUTHORITY_MUTATION: no
RECOVERY_CLASS_HINT: candidate
```

This packet is a real-execution candidate prep artifact only.
It does not approve execution.
It does not execute Gemini or Codex.
It does not call model APIs.
It does not promote anything.
The validated dry-run directory remains receipt/proof and must not be modified.

## 3. Approval Block

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes
APPROVED_PACKET_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md
APPROVED_OUTPUT_DIR: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs
APPROVED_GEMINI_PROMPT_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/GEMINI_PROMPT_EXECUTION_V0.md
APPROVED_CODEX_PROMPT_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/CODEX_RECOVERY_PROMPT_EXECUTION_V0.md
APPROVED_RECEIPT_CONTRACT_PATH: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
APPROVED_NETWORK_SCOPE: model_api_transport_only_after_explicit_execution_approval
APPROVED_LIVE_WEB_SOURCE_LOOKUP: no
APPROVED_EXTERNAL_CONNECTOR: no
APPROVED_BROWSER_MCP: no
APPROVED_MEMORY_SKILL_CRON_CONFIG_MUTATION: no
APPROVED_VECTORFL_AUTHORITY_MUTATION: no
APPROVED_PROMOTION: no
```

Execution note:

```text
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET is now yes for this packet-scoped run.
This approval covered the bounded Gemini/Codex/Hermes receipt lane only.
Promotion remains no.
VectorFL authority mutation remains no.
```

## 4. Lane Type and Role Boundaries

```text
LANE_TYPE: HERMES_RUN_GEMINI_THEN_CODEX_RECOVERY_BOUNDED
EXECUTION_TOPOLOGY:
  Hermes main workbench
    -> Gemini lite-output lens
    -> Codex recovery worker
    -> Hermes receipt/report
    -> VectorFL recovery gate only

DISPATCH_TARGET: Hermes

GEMINI_ROLE:
  bulk exploration / lite evidence producer
  not final judge
  not promotion authority
  not truth authority

CODEX_ROLE:
  recovery judge
  WATCH/HOLD restorer
  recovery class classifier
  not execution authority
  not promotion authority
  not VectorFL authority mutator

VECTORFL_ROLE:
  recovery gate only

USER_ROLE:
  dispatch approval
  side-effect approval
  promotion approval
```

## 5. Declared Gemini Input Files

Gemini may read only these declared reference files after explicit execution approval:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bounded_combined_bridge_template_candidate_v0/BOUNDED_COMBINED_BRIDGE_PACKET_TEMPLATE_CANDIDATE_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bounded_combined_bridge_template_candidate_v0/BOUNDED_COMBINED_BRIDGE_USAGE_CARD_CANDIDATE_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/bounded_combined_bridge_template_candidate_v0/BOUNDED_COMBINED_BRIDGE_RECEIPT_CONTRACT_CANDIDATE_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/HERMES_OPTION3A_COMBINED_BRIDGE_REPORT_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/real_operation_test_option3a_combined_bridge_v0/HERMES_OPTION3A_COMBINED_BRIDGE_RECEIPT_V0.json
```

## 6. Gemini Output Materialization Contract

```text
Gemini raw stdout must be saved to:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt

Gemini lite JSON must be materialized and validated at:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_lite_output.json
```

Required lite JSON schema shape:

```json
{
  "observed_scope": [],
  "repeated_patterns": [],
  "candidate_items": [],
  "uncertainties": [],
  "possible_risks": [],
  "do_not_promote": [],
  "questions_for_codex": [],
  "completion_signal": "GEMINI_LITE_OUTPUT_DONE"
}
```

Materialization rule:

```text
1. Preserve Gemini stdout exactly as gemini_raw_output.txt.
2. Materialize gemini_lite_output.json as a JSON object with the required keys above.
3. If Gemini raw output is already exactly the required JSON object, the same object may be written to gemini_lite_output.json after validation.
4. If Gemini raw output includes extra prose, preserve the full raw output and extract/materialize only the valid schema-conforming JSON object into gemini_lite_output.json.
5. If no valid schema-conforming JSON object with completion_signal GEMINI_LITE_OUTPUT_DONE can be materialized, STOP before Codex recovery.
```

Proposed Gemini raw capture command for later approval only:

```bash
mkdir -p /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs && gemini --approval-mode plan --sandbox --output-format text -p "$(cat /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/GEMINI_PROMPT_EXECUTION_V0.md)" > /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt
```

This command was enabled for the packet-scoped approved execution lane only.
It remains not a promotion approval.

## 7. Codex 4-Input Recovery Contract

Codex must read exactly these four inputs after explicit execution approval and after valid Gemini output materialization:

```text
1. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md
2. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_lite_output.json
3. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt
4. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
```

Codex must write only:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/codex_combined_bridge_recovery_return.md
```

Codex role:

```text
1. Confirm the actual scope Gemini observed.
2. Remove premature Gemini conclusions.
3. Restore WATCH/HOLD boundaries.
4. Assign recovery_class_hint.
5. Compress to a VectorFL-safe return packet.
```

Proposed Codex recovery command for later approval only:

```bash
codex exec "$(cat /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/CODEX_RECOVERY_PROMPT_EXECUTION_V0.md)"
```

This command was enabled for the packet-scoped approved execution lane only.
It remains not a promotion approval.

## 8. Expected Outputs

Declared future execution outputs:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_lite_output.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/codex_combined_bridge_recovery_return.md
```

Declared Hermes closeout outputs after approved execution:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_REPORT_V0.md
```

Prep-stage contract files:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_REPORT_CONTRACT_V0.md
```

## 9. Mini-Agent Rhythm Rule

```text
one action per stage
explicit completion signal
raw output preserved
lite output for next-stage consumption
no hidden shell state assumption
final report/receipt/return contract
```

Stage completion signals:

```text
Gemini stage: GEMINI_LITE_OUTPUT_DONE
Codex stage: CODEX_RECOVERY_DONE
Hermes stage: HERMES_EXECUTION_RECEIPT_DONE
```

## 10. STOP Conditions

```text
execution approval missing or says no
Gemini command executed before explicit approval
Codex command executed before explicit approval
model API transport used before explicit approval
output directory not exact
Gemini raw stdout not saved to gemini_raw_output.txt
Gemini lite JSON missing or invalid
Gemini lite JSON completion_signal is not GEMINI_LITE_OUTPUT_DONE
Codex prompt does not name all four declared inputs
Codex reads outside the four declared inputs
Codex writes outside the declared recovery return path
Codex reruns Gemini
live web/source lookup occurs
external connector occurs
browser/MCP occurs
memory/skill/cron/config mutation requested/performed
VectorFL authority mutation requested/performed
promotion/component/baseline/workflow/schema/registry/ontology claim appears
AGENTS.md/SKILL.md/current-position/output_manifest mutation requested/performed
dry-run directory modified
execution_v0 prep mistaken as real run
```

## 11. Boundary Distinctions

```text
command exists in packet != execution approval
execution approval != promotion approval
Gemini output != truth
Codex recovery != authority mutation
Hermes success != VectorFL approval
receipt/report != authority
candidate != component
```

## 12. Required Final Line

```text
No execution was performed. No promotion was performed. Recovery class remains candidate.
```
