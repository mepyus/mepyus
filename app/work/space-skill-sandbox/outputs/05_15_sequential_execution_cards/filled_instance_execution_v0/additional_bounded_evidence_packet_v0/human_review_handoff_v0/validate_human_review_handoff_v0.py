#!/usr/bin/env python3
import os,json,sys
H='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/human_review_handoff_v0'
B='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0'
required=['HUMAN_REVIEW_INDEX_V0.json','HUMAN_REVIEW_README_V0.md','OPERATOR_APPROVAL_CHECKLIST_V0.md','EVIDENCE_TO_DECISION_MATRIX_V0.md']
errors=[]
for r in required:
    if not os.path.exists(os.path.join(H,r)): errors.append('missing '+r)
idx=json.load(open(os.path.join(H,'HUMAN_REVIEW_INDEX_V0.json'),encoding='utf-8'))
if any(not item.get('exists') for item in idx.get('items',[])): errors.append('index contains missing items')
texts='\\n'.join(open(os.path.join(H,r),encoding='utf-8').read() for r in required if r.endswith('.md'))
for token in ['APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no','No promotion was performed. Recovery class remains candidate.']:
    if token not in texts: errors.append('missing token '+token)
if 'EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes' not in texts: errors.append('checklist missing future yes approval block')
if 'not_applied_confirmation' not in texts: errors.append('checklist missing not-applied confirmation')
if errors:
    print('verdict: HUMAN_REVIEW_HANDOFF_VALIDATION_STOP')
    for e in errors: print('STOP:',e)
    sys.exit(2)
print('verdict: HUMAN_REVIEW_HANDOFF_VALIDATION_PASS_WITH_EXECUTION_HOLD')
print('indexed_items:', len(idx.get('items',[])))
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
