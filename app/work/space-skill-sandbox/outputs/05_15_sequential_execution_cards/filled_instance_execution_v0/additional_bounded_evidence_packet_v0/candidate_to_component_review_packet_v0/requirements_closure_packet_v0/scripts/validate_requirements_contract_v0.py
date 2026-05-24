#!/usr/bin/env python3
from pathlib import Path
import json, sys
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0/requirements_closure_packet_v0')
errors=[]
for rel in ['REQUIREMENTS_CLOSURE_PACKET_V0.md','GEMINI_REQUIREMENTS_REVIEW_PROMPT_V0.md','CODEX_REQUIREMENTS_RECOVERY_PROMPT_V0.md','REQUIREMENTS_CLOSURE_RECEIPT_CONTRACT_V0.json','REQUIREMENTS_COMMAND_MANIFEST_V0.json','REQ_REVIEW_INPUT_MANIFEST_V0.json']:
 if not (BASE/rel).exists(): errors.append('missing '+rel)
packet=(BASE/'REQUIREMENTS_CLOSURE_PACKET_V0.md').read_text()
for token in ['EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes','APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no']:
 if token not in packet: errors.append('packet missing '+token)
manifest=json.loads((BASE/'REQUIREMENTS_COMMAND_MANIFEST_V0.json').read_text())
if manifest.get('approved_promotion')!='no': errors.append('promotion not no')
if manifest.get('approved_vectorfl_authority_mutation')!='no': errors.append('authority not no')
if errors:
 print('verdict: REQUIREMENTS_CONTRACT_VALIDATION_STOP')
 [print('STOP:', e) for e in errors]
 sys.exit(2)
print('verdict: REQUIREMENTS_CONTRACT_VALIDATION_PASS')
print('execution_approval_state: yes')
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
