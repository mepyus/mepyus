#!/usr/bin/env python3
import os, json, hashlib, sys
relay='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0'
manifest_path=os.path.join(relay,'PRIMARY_INPUT_RELAY_MANIFEST_V0.json')
packet_path=os.path.join(relay,'GEMINI_SCOPE_GAP_BOUNDED_EVIDENCE_PACKET_V0.md')
prompt_path=os.path.join(relay,'GEMINI_SCOPE_GAP_REVIEW_PROMPT_V0.md')
errors=[]
for p in [manifest_path, packet_path, prompt_path]:
    if not os.path.exists(p): errors.append('missing '+p)
manifest=json.load(open(manifest_path,encoding='utf-8'))
if manifest.get('execution_approval_granted_for_this_packet')!='no': errors.append('execution approval is not no')
if manifest.get('promotion_approved') is not False: errors.append('promotion approved is not false')
if manifest.get('vectorfl_authority_mutation_approved') is not False: errors.append('authority mutation approved is not false')
for item in manifest.get('inputs',[]):
    for key in ['source_path','relay_path','sha256','size']:
        if key not in item: errors.append('manifest input missing '+key)
    if not os.path.exists(item.get('source_path','')): errors.append('missing source '+item.get('source_path',''))
    if not os.path.exists(item.get('relay_path','')): errors.append('missing relay '+item.get('relay_path',''))
    if os.path.exists(item.get('source_path','')) and os.path.exists(item.get('relay_path','')):
        src=open(item['source_path'],'rb').read(); dst=open(item['relay_path'],'rb').read()
        if hashlib.sha256(src).hexdigest()!=item['sha256']: errors.append('source hash drift '+item['source_path'])
        if hashlib.sha256(dst).hexdigest()!=item['sha256']: errors.append('relay hash mismatch '+item['relay_path'])
        if src!=dst: errors.append('relay content mismatch '+item['relay_path'])
packet=open(packet_path,encoding='utf-8').read()
for token in ['EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no','APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no','no Gemini execution','no Codex execution','No promotion was performed. Recovery class remains candidate.']:
    if token not in packet: errors.append('packet missing token '+token)
prompt=open(prompt_path,encoding='utf-8').read()
for token in ['future-only','requires separate explicit execution approval','Do not claim promotion','GEMINI_SCOPE_GAP_LITE_DONE']:
    if token not in prompt: errors.append('prompt missing token '+token)
if errors:
    print('verdict: SCOPE_GAP_PACKET_VALIDATION_STOP')
    for e in errors: print('STOP:', e)
    sys.exit(2)
print('verdict: SCOPE_GAP_PACKET_STATIC_VALIDATION_PASS_WITH_EXECUTION_HOLD')
print('relay_input_count:', len(manifest.get('inputs',[])))
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
