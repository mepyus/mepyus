#!/usr/bin/env python3
import json, os, sys
BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0'
REH='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/no_model_scope_gap_rehearsal_v0'
manifest=json.load(open(os.path.join(BASE,'PRIMARY_INPUT_RELAY_MANIFEST_V0.json'),encoding='utf-8'))
lite_path=os.path.join(REH,'outputs','synthetic_gemini_scope_gap_lite_output.json')
codex_path=os.path.join(REH,'outputs','synthetic_codex_scope_gap_recovery_return.md')
errors=[]
for item in manifest.get('inputs',[]):
    if not os.path.exists(item['relay_path']): errors.append('missing relay '+item['relay_path'])
lite=json.load(open(lite_path,encoding='utf-8'))
required=['observed_relay_inputs','confirmed_patterns','contradictions_with_prior_s8','remaining_uncertainties','candidate_upgrade_implications','do_not_promote','questions_for_codex','completion_signal']
for k in required:
    if k not in lite: errors.append('missing lite key '+k)
if lite.get('completion_signal')!='GEMINI_SCOPE_GAP_LITE_DONE': errors.append('bad lite completion')
if len(lite.get('observed_relay_inputs',[]))!=5: errors.append('synthetic observed relay count not 5')
codex=open(codex_path,encoding='utf-8').read()
for token in ['CODEX_SCOPE_GAP_RECOVERY_DONE','candidate_with_promotion_hold','No promotion was performed. Recovery class remains candidate.']:
    if token not in codex: errors.append('codex missing '+token)
for bad in ['promotion_performed: true','authority_mutation: true','APPROVED_PROMOTION: yes']:
    if bad in codex: errors.append('forbidden claim '+bad)
if errors:
    print('verdict: NO_MODEL_SCOPE_GAP_REHEARSAL_STOP')
    for e in errors: print('STOP:',e)
    sys.exit(2)
receipt={'verdict':'NO_MODEL_SCOPE_GAP_REHEARSAL_PASS_WITH_EXECUTION_HOLD','relay_input_count':len(manifest.get('inputs',[])),'synthetic_only':True,'gemini_execution':False,'codex_execution':False,'promotion':False,'vectorfl_authority_mutation':False,'required_final_line':'No promotion was performed. Recovery class remains candidate.'}
json.dump(receipt, open(os.path.join(REH,'outputs','NO_MODEL_SCOPE_GAP_REHEARSAL_RECEIPT_V0.json'),'w',encoding='utf-8'), indent=2, ensure_ascii=False)
print('verdict: NO_MODEL_SCOPE_GAP_REHEARSAL_PASS_WITH_EXECUTION_HOLD')
print('relay_input_count:', len(manifest.get('inputs',[])))
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
