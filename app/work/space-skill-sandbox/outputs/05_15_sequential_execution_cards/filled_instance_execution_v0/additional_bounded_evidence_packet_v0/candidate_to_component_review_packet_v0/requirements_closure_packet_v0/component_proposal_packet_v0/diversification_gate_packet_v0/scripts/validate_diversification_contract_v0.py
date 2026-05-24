#!/usr/bin/env python3
from pathlib import Path
import json, sys
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0/requirements_closure_packet_v0/component_proposal_packet_v0/diversification_gate_packet_v0')
errors=[]
for rel in ['DIVERSIFICATION_GATE_PACKET_V0.md','GEMINI_DIVERSIFICATION_PROMPT_V0.md','CODEX_DIVERSIFICATION_RECOVERY_PROMPT_V0.md','DIVERSIFICATION_RECEIPT_CONTRACT_V0.json','DIVERSIFICATION_COMMAND_MANIFEST_V0.json','DIVERSIFICATION_INPUT_MANIFEST_V0.json']:
 if not (BASE/rel).exists(): errors.append('missing '+rel)
packet=(BASE/'DIVERSIFICATION_GATE_PACKET_V0.md').read_text()
for token in ['EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes','APPROVED_DIVERSIFICATION_REVIEW: yes','APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no','APPROVED_REGISTRY_SCHEMA_WORKFLOW_INTEGRATION: no']:
 if token not in packet: errors.append('packet missing '+token)
manifest=json.loads((BASE/'DIVERSIFICATION_COMMAND_MANIFEST_V0.json').read_text())
for k in ['approved_promotion','approved_vectorfl_authority_mutation','approved_registry_schema_workflow_integration','approved_final_structure_selection']:
 if manifest.get(k)!='no': errors.append(k+' not no')
if errors:
 print('verdict: DIVERSIFICATION_CONTRACT_VALIDATION_STOP')
 [print('STOP:', e) for e in errors]
 sys.exit(2)
print('verdict: DIVERSIFICATION_CONTRACT_VALIDATION_PASS')
print('execution_approval_state: yes')
print('diversification_review: true')
print('final_structure_selection: false')
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('registry_schema_workflow_integration: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
