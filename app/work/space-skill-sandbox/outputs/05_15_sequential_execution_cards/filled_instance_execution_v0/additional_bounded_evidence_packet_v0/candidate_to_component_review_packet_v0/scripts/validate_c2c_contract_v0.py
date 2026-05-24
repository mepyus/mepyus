#!/usr/bin/env python3
from pathlib import Path
import json, sys
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0')
errors=[]
for rel in ['CANDIDATE_TO_COMPONENT_REVIEW_PACKET_V0.md','GEMINI_C2C_REVIEW_PROMPT_V0.md','CODEX_C2C_RECOVERY_PROMPT_V0.md','C2C_REVIEW_RECEIPT_CONTRACT_V0.json','C2C_COMMAND_MANIFEST_V0.json']:
    if not (BASE/rel).exists(): errors.append('missing '+rel)
packet=(BASE/'CANDIDATE_TO_COMPONENT_REVIEW_PACKET_V0.md').read_text()
for token in ['EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes','APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no','No promotion was performed. Recovery class remains candidate.']:
    if token not in packet: errors.append('packet missing '+token)
manifest=json.loads((BASE/'C2C_COMMAND_MANIFEST_V0.json').read_text())
if manifest.get('execution_approval_granted_for_this_packet')!='yes': errors.append('manifest execution approval not yes')
if manifest.get('approved_promotion')!='no': errors.append('manifest promotion not no')
if manifest.get('approved_vectorfl_authority_mutation')!='no': errors.append('manifest authority not no')
if errors:
    print('verdict: C2C_CONTRACT_VALIDATION_STOP')
    [print('STOP:', e) for e in errors]
    sys.exit(2)
print('verdict: C2C_CONTRACT_VALIDATION_PASS')
print('execution_approval_state: yes')
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
