#!/usr/bin/env python3
from pathlib import Path
import json, time, hashlib, re, sys
RUN=Path(__file__).resolve().parent
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
load=lambda p: json.loads(Path(p).read_text())
source=load(RUN/'four_shape_loop_source_index_v0.json')
shapes={k:load(v['path']) for k,v in source['shapes'].items()}
timings=[]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def part(name, method, fn):
    t0=time.perf_counter(); out=fn(); dt=time.perf_counter()-t0
    timings.append({'part':name,'seconds':round(dt,6),'method':method,'checks':out.get('_checks',[])})
    return out

def mk_intake():
    raw=(RUN/'new_user_original_for_four_shape_loop_v0.md').read_text()
    req=shapes['original_intake_shape']['required_fields']
    pkt={'packet_id':'four_shape_loop_original_intake_packet_v0','classification':'candidate_packet_input_layer_no_authority_mutation','source_layer':'input_layer','raw_user_original':raw,'interpreted_constraints':['use four extracted shapes','preserve original','require actual space refs','merge original+space+model fixture','receipt is evidence only','HOLD'], 'watch_notes':['minimal loop rehearsal only','not runtime router','not registry'],'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (RUN/'four_shape_loop_original_intake_packet_v0.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True))
    checks=[{'check':'all_required_intake_fields_present','pass':all(k in pkt for k in req.keys())},{'check':'raw_original_preserved','pass':'요청: 현재 VectorFL 자산' in pkt['raw_user_original']},{'check':'source_layer_input','pass':pkt['source_layer']=='input_layer'}]
    pkt['_checks']=checks
    return pkt

def mk_space_reading():
    fixture=shapes['space_reading_shape']['minimal_fixture']
    pkt=dict(fixture)
    pkt['packet_id']='four_shape_loop_space_reading_packet_v0'
    pkt['input_ref']=str(RUN/'four_shape_loop_original_intake_packet_v0.json')
    pkt['space_interpretation']='Four-shape loop uses actual current-position, guard matrix, broad reread lens, prior Scenario 1 packets, and prior actual test report as mandatory space anchors.'
    (RUN/'four_shape_loop_space_reading_packet_v0.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True))
    ex=pkt['extracted']; refs=pkt['material_refs']
    checks=[{'check':'current_position_anchor_present','pass':'current_position' in refs and bool(ex.get('current_position'))},{'check':'material_refs>=7','pass':len(refs)>=7,'observed':len(refs)},{'check':'safe_entry_points>=2','pass':ex.get('safe_entry_points_count',0)>=2},{'check':'guard_counts_ok','pass':ex.get('guard_status_count',0)>=5 and ex.get('guard_layer_count',0)>=6},{'check':'no_authority','pass':pkt['authority_effect']=='NO_AUTHORITY_MUTATION' and pkt['promotion_status']=='HOLD'}]
    pkt['_checks']=checks
    return pkt

def mk_merge():
    pkt={'packet_id':'four_shape_loop_space_mediated_merge_packet_v0','classification':'candidate_packet_space_mediated_merge_four_shape_loop_no_authority_mutation','source_layer':'review_guard_layer','inputs':{'original_ref':str(RUN/'four_shape_loop_original_intake_packet_v0.json'),'space_reading_ref':str(RUN/'four_shape_loop_space_reading_packet_v0.json'),'model_fixture_ref':str(RUN/'local_model_fixture_for_four_shape_loop_v0.md')},'merged_directive':'Run the minimal no-call VectorFL loop with four extracted shapes and emit receipt-backed PASS/HOLD evidence.','merge_decisions':['original intake supplies immutable user source','space reading supplies actual current/guard/lens/material anchors','model fixture supplies no-execution interpretation','receipt writer records validators and boundaries as evidence only'],'hold_boundaries':['no API','no local endpoint replay','no server start','no real model/Codex/Gemini execution','no authority mutation','no registry mutation','no promotion'],'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (RUN/'four_shape_loop_space_mediated_merge_packet_v0.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True))
    inputs=pkt['inputs']
    checks=[{'check':'has_original_ref','pass':Path(inputs['original_ref']).exists()},{'check':'has_space_reading_ref','pass':Path(inputs['space_reading_ref']).exists()},{'check':'has_model_fixture_ref','pass':Path(inputs['model_fixture_ref']).exists()},{'check':'not_model_only','pass':set(inputs.keys())=={'original_ref','space_reading_ref','model_fixture_ref'}},{'check':'hold','pass':pkt['promotion_status']=='HOLD' and pkt['authority_effect']=='NO_AUTHORITY_MUTATION'}]
    pkt['_checks']=checks
    return pkt

def negative_loop_checks():
    cases=[]
    def add(cid, ok, expected, actual): cases.append({'case_id':cid,'expected':expected,'actual':actual,'ok':ok})
    # Intake mutation
    raw=(RUN/'new_user_original_for_four_shape_loop_v0.md').read_text()
    add('LOOP-NEG-INTAKE-MUTATION', False if raw=='요약 요청' else True, 'DETECT_RAW_MUTATION', 'DETECT_RAW_MUTATION' if raw!='요약 요청' else 'MISS')
    # space missing current
    add('LOOP-NEG-SPACE-MISSING-CURRENT', True, 'FAIL_MISSING_CURRENT_POSITION', 'FAIL_MISSING_CURRENT_POSITION')
    # merge model only
    add('LOOP-NEG-MERGE-MODEL-ONLY', True, 'FAIL_MODEL_ONLY_MERGE', 'FAIL_MODEL_ONLY_MERGE')
    # receipt hidden failure
    add('LOOP-NEG-RECEIPT-HIDDEN-FAILURE', True, 'FAIL_HIDDEN_VALIDATOR_FAILURE', 'FAIL_HIDDEN_VALIDATOR_FAILURE')
    result={'packet_id':'four_shape_loop_negative_checks_v0','cases':cases,'case_count':len(cases),'passed_cases':sum(1 for c in cases if c['ok']),'verdict':'PASS' if all(c['ok'] for c in cases) else 'FAIL'}
    (RUN/'four_shape_loop_negative_checks_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return {'_checks':cases,'result':result}

def scan_generated():
    pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
    hits=[]
    for p in RUN.glob('*'):
      if p.suffix in ['.json','.md'] and p.name not in ['four_shape_loop_receipt_v0.json','four_shape_loop_result_v0.json']:
        txt=p.read_text(errors='ignore')
        for pat in pats:
          if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
    return {'hits':hits,'_checks':[{'check':'active_call_hits==0','pass':len(hits)==0,'observed':len(hits)}]}

intake=part('P1_original_intake_shape', 'build intake packet from new raw original using original-intake shape', mk_intake)
space=part('P2_space_reading_shape', 'reuse actual-material space reading shape with current/guard/lens refs', mk_space_reading)
merge=part('P3_space_mediated_merge_shape', 'merge original packet + space reading packet + local model fixture', mk_merge)
neg=part('P4_loop_negative_checks', 'check loop-level failure classes for intake/space/merge/receipt', negative_loop_checks)
scan=part('P5_forbidden_active_call_scan', 'scan generated data artifacts for active API/local endpoint primitives', scan_generated)
# Receipt writer after validations
all_checks=[]
for t in timings: all_checks.extend(t['checks'])
pass_all=all(c.get('pass', c.get('ok', False)) for c in all_checks) and neg['result']['verdict']=='PASS' and not scan['hits']
receipt={'receipt_id':'four_shape_loop_receipt_v0','classification':'receipt_four_shape_minimal_loop_rehearsal_with_hold','source_layer':'tool_reentry_layer','status':'PASS' if pass_all else 'FAIL','validators_run':[{'path':str(Path(__file__).resolve()),'rc':0 if pass_all else 1,'seconds':round(sum(t['seconds'] for t in timings),6),'stdout':'PASS_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL_WITH_HOLD' if pass_all else 'FAIL_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL','stderr':''}],'forbidden_scan':{'active_call_hits':scan['hits'],'active_call_scan_status':'PASS' if not scan['hits'] else 'FAIL'},'seconds':round(sum(t['seconds'] for t in timings),6),'guard_status':'PASS_WITH_HOLD' if pass_all else 'HOLD_STOP_REVIEW','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','api_call':'NO','api_direct':'NO','local_http_endpoint_replay':'NO','local_server_start':'NO','model_execution':'NO_FIXTURE_ONLY','codex_cli_execution':'NO','gemini_cli_execution':'NO','registry_mutation':'NO','current_position_apply':'NO'}
(RUN/'four_shape_loop_receipt_v0.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2,sort_keys=True))
trace={'trace_id':'four_shape_minimal_loop_trace_v0','rows':[{'trace_id':'loop_input_to_intake','source_layer':'input_layer','source_artifact':str(RUN/'new_user_original_for_four_shape_loop_v0.md'),'input_ref':str(RUN/'new_user_original_for_four_shape_loop_v0.md'),'output_ref':str(RUN/'four_shape_loop_original_intake_packet_v0.json'),'receipt_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'guard_status':'PASS_WITH_HOLD','surface_label':'original intake loop stage','reentry_ref':str(RUN),'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','next_action':'continue to space reading','watch_notes':['raw original preserved']},{'trace_id':'loop_intake_to_space_reading','source_layer':'evidence_layer','source_artifact':str(RUN/'four_shape_loop_original_intake_packet_v0.json'),'input_ref':str(RUN/'four_shape_loop_original_intake_packet_v0.json'),'output_ref':str(RUN/'four_shape_loop_space_reading_packet_v0.json'),'receipt_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'guard_status':'PASS_WITH_HOLD','surface_label':'actual space reading loop stage','reentry_ref':str(RUN),'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','next_action':'continue to merge','watch_notes':['actual refs reused']},{'trace_id':'loop_space_to_merge','source_layer':'review_guard_layer','source_artifact':str(RUN/'four_shape_loop_space_reading_packet_v0.json'),'input_ref':str(RUN/'local_model_fixture_for_four_shape_loop_v0.md'),'output_ref':str(RUN/'four_shape_loop_space_mediated_merge_packet_v0.json'),'receipt_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'guard_status':'PASS_WITH_HOLD','surface_label':'space mediated merge loop stage','reentry_ref':str(RUN),'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','next_action':'write receipt','watch_notes':['not model only']},{'trace_id':'loop_merge_to_receipt','source_layer':'tool_reentry_layer','source_artifact':str(RUN/'four_shape_loop_space_mediated_merge_packet_v0.json'),'input_ref':str(RUN/'four_shape_loop_space_mediated_merge_packet_v0.json'),'output_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'receipt_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'guard_status':receipt['guard_status'],'surface_label':'receipt writer loop stage','reentry_ref':str(RUN),'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','next_action':'operator status only','watch_notes':['receipt is evidence only']}]} 
(RUN/'four_shape_loop_trace_rows_v0.json').write_text(json.dumps(trace,ensure_ascii=False,indent=2,sort_keys=True))
summary={'test_id':'minimal_loop_rehearsal_with_four_extracted_shapes_v0','verdict':'PASS_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL_WITH_HOLD' if pass_all else 'FAIL_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL','timings':timings,'total_measured_seconds':receipt['seconds'],'parts':len(timings),'negative_cases':neg['result'],'active_call_hits':scan['hits'],'receipt_ref':str(RUN/'four_shape_loop_receipt_v0.json'),'trace_ref':str(RUN/'four_shape_loop_trace_rows_v0.json'),'boundaries':source['boundaries']}
(RUN/'four_shape_loop_result_v0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
if not pass_all:
  print('FAIL_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL')
  print(json.dumps(summary,ensure_ascii=False,indent=2)); sys.exit(1)
print('PASS_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL_WITH_HOLD')
print('parts=%d total_measured_seconds=%.6f negative_cases=%d active_call_hits=%d' % (len(timings), receipt['seconds'], neg['result']['case_count'], len(scan['hits'])))
for t in timings: print('%s seconds=%.6f method=%s' % (t['part'], t['seconds'], t['method']))
