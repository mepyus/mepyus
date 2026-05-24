#!/usr/bin/env python3
import os,json,sys
BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0'
errors=[]
paths={"cmd_manifest": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/SCOPE_GAP_COMMAND_MANIFEST_V0.json", "receipt_contract": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/HERMES_SCOPE_GAP_EVIDENCE_RECEIPT_CONTRACT_V0.json", "report_contract": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/HERMES_SCOPE_GAP_EVIDENCE_REPORT_CONTRACT_V0.md", "runner": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/scripts/run_scope_gap_execution_v0.sh", "packet": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/GEMINI_SCOPE_GAP_BOUNDED_EVIDENCE_PACKET_V0.md", "prompt": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/GEMINI_SCOPE_GAP_REVIEW_PROMPT_V0.md", "codex_prompt": "/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/CODEX_SCOPE_GAP_RECOVERY_PROMPT_V0.md"}
for name,p in paths.items():
    if not os.path.exists(p): errors.append('missing '+name+': '+p)
cmd=json.load(open(paths['cmd_manifest'],encoding='utf-8'))
if cmd.get('execution_approval_granted_for_this_packet')!='no': errors.append('command manifest approval not no')
for k in ['approved_promotion','approved_vectorfl_authority_mutation','approved_live_web_source_lookup','approved_external_connector','approved_browser_mcp','approved_memory_skill_cron_config_mutation']:
    if cmd.get(k)!='no': errors.append(k+' not no')
contract=json.load(open(paths['receipt_contract'],encoding='utf-8'))
if contract.get('promotion_approved') is not False: errors.append('receipt contract promotion approved')
if contract.get('vectorfl_authority_mutation_approved') is not False: errors.append('receipt contract authority approved')
packet=open(paths['packet'],encoding='utf-8').read()
for token in ['EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: no','APPROVED_PROMOTION: no','APPROVED_VECTORFL_AUTHORITY_MUTATION: no']:
    if token not in packet: errors.append('packet missing '+token)
runner_txt=open(paths['runner'],encoding='utf-8').read()
for token in ['require_approval','scope-gap packet does not grant execution approval: yes','I_UNDERSTAND_THIS_RUNS_SCOPE_GAP_GEMINI_CODEX=yes']:
    if token not in runner_txt: errors.append('runner missing '+token)
if errors:
    print('verdict: SCOPE_GAP_EXECUTION_CONTRACT_VALIDATION_STOP')
    for e in errors: print('STOP:',e)
    sys.exit(2)
print('verdict: SCOPE_GAP_EXECUTION_CONTRACT_VALIDATION_PASS_WITH_EXECUTION_HOLD')
print('execution_approval_state: no')
print('promotion: false')
print('vectorfl_authority_mutation: false')
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
