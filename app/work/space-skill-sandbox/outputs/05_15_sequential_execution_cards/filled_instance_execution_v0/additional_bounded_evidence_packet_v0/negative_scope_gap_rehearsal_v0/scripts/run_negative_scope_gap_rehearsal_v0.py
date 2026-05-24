#!/usr/bin/env python3
import os,json,sys,re
NEG='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/negative_scope_gap_rehearsal_v0'
results=[]
def stop_ok(name, reason): results.append({'case':name,'result':'STOP_OK','reason':reason})
# json cases
for name in ['bad_missing_completion.json','bad_wrong_relay_count.json','bad_promotion_implication.json']:
    obj=json.load(open(os.path.join(NEG,'cases',name),encoding='utf-8'))
    reason=None
    if obj.get('completion_signal')!='GEMINI_SCOPE_GAP_LITE_DONE': reason='bad completion_signal'
    elif len(obj.get('observed_relay_inputs',[]))!=5: reason='bad observed_relay_inputs count'
    elif any('APPROVED_PROMOTION: yes' in x or 'promotion' in x.lower() and 'yes' in x.lower() for x in obj.get('candidate_upgrade_implications',[])): reason='forbidden promotion implication'
    if reason: stop_ok(name, reason)
    else: results.append({'case':name,'result':'UNEXPECTED_PASS'})
text=open(os.path.join(NEG,'cases','bad_codex_promotion_claim.md'),encoding='utf-8').read()
if 'promotion_performed: true' in text: stop_ok('bad_codex_promotion_claim.md','forbidden promotion claim')
else: results.append({'case':'bad_codex_promotion_claim.md','result':'UNEXPECTED_PASS'})
all_ok=all(r['result']=='STOP_OK' for r in results)
receipt={'verdict':'NEGATIVE_SCOPE_GAP_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED' if all_ok else 'NEGATIVE_SCOPE_GAP_REHEARSAL_WATCH','results':results,'promotion':False,'vectorfl_authority_mutation':False,'required_final_line':'No promotion was performed. Recovery class remains candidate.'}
json.dump(receipt, open(os.path.join(NEG,'outputs','NEGATIVE_SCOPE_GAP_REHEARSAL_RECEIPT_V0.json'),'w',encoding='utf-8'), indent=2, ensure_ascii=False)
if not all_ok:
    print('verdict: NEGATIVE_SCOPE_GAP_REHEARSAL_WATCH')
    sys.exit(2)
print('verdict: NEGATIVE_SCOPE_GAP_REHEARSAL_PASS_ALL_BAD_FIXTURES_STOPPED')
for r in results: print(r['case']+': '+r['result']+' / '+r['reason'])
print('required_final_line: No promotion was performed. Recovery class remains candidate.')
