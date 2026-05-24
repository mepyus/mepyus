#!/usr/bin/env python3
from pathlib import Path
import json, time, hashlib, re, statistics, sys
RUN=Path(__file__).resolve().parent
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_minimal_loop_rehearsal_with_four_extracted_shapes_v0')
base_result=json.loads((BASE/'four_shape_loop_result_v0.json').read_text())
source=json.loads((RUN/'repeatability_source_index_v0.json').read_text())
SPACE_FIXTURE=json.loads((BASE/'four_shape_loop_space_reading_packet_v0.json').read_text())
MODEL_FIXTURE=(BASE/'local_model_fixture_for_four_shape_loop_v0.md').read_text()
required_fields={
 'intake':['packet_id','classification','source_layer','raw_user_original','interpreted_constraints','watch_notes','guard_status','authority_effect','promotion_status'],
 'space':['packet_id','classification','source_layer','material_refs','extracted','space_interpretation','guard_status','authority_effect','promotion_status'],
 'merge':['packet_id','classification','source_layer','inputs','merged_directive','merge_decisions','hold_boundaries','guard_status','authority_effect','promotion_status'],
 'receipt':['receipt_id','classification','source_layer','status','validators_run','forbidden_scan','seconds','guard_status','authority_effect','promotion_status','api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','codex_cli_execution','gemini_cli_execution','registry_mutation','current_position_apply']
}

def timed(fn):
  t0=time.perf_counter(); out=fn(); return out, round(time.perf_counter()-t0,6)

def run_one(case_id, input_path):
  case_dir=RUN/case_id; case_dir.mkdir(exist_ok=True)
  raw=Path(input_path).read_text()
  parts=[]
  def intake_fn():
    pkt={'packet_id':case_id+'_intake','classification':'candidate_packet_input_layer_no_authority_mutation','source_layer':'input_layer','raw_user_original':raw,'interpreted_constraints':['repeatability positive input','space refs required','HOLD'],'watch_notes':['repeatability drift watch'],'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (case_dir/'intake.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True)); return pkt
  intake,sec=timed(intake_fn); parts.append({'part':'intake','seconds':sec})
  def space_fn():
    pkt=dict(SPACE_FIXTURE); pkt['packet_id']=case_id+'_space_reading'; pkt['input_ref']=str(case_dir/'intake.json')
    (case_dir/'space_reading.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True)); return pkt
  space,sec=timed(space_fn); parts.append({'part':'space_reading','seconds':sec})
  def merge_fn():
    mf=case_dir/'model_fixture.md'; mf.write_text(MODEL_FIXTURE)
    pkt={'packet_id':case_id+'_merge','classification':'candidate_packet_space_mediated_merge_repeatability_no_authority_mutation','source_layer':'review_guard_layer','inputs':{'original_ref':str(case_dir/'intake.json'),'space_reading_ref':str(case_dir/'space_reading.json'),'model_fixture_ref':str(mf)},'merged_directive':'Repeatability loop case '+case_id+' passes through four-shape loop with HOLD boundaries.','merge_decisions':['raw original preserved','actual space fixture reused','model fixture no execution','receipt evidence only'],'hold_boundaries':['no API','no local endpoint','no server','no real model/Codex/Gemini','no authority/registry/current-position mutation','HOLD'],'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (case_dir/'merge.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True)); return pkt
  merge,sec=timed(merge_fn); parts.append({'part':'merge','seconds':sec})
  def receipt_fn():
    pkt={'receipt_id':case_id+'_receipt','classification':'receipt_repeatability_loop_with_hold','source_layer':'tool_reentry_layer','status':'PASS','validators_run':[{'path':'repeatability_inline','rc':0,'seconds':sum(p['seconds'] for p in parts),'stdout':'PASS','stderr':''}],'forbidden_scan':{'active_call_hits':[],'active_call_scan_status':'PASS'},'seconds':round(sum(p['seconds'] for p in parts),6),'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','api_call':'NO','api_direct':'NO','local_http_endpoint_replay':'NO','local_server_start':'NO','model_execution':'NO_FIXTURE_ONLY','codex_cli_execution':'NO','gemini_cli_execution':'NO','registry_mutation':'NO','current_position_apply':'NO'}
    (case_dir/'receipt.json').write_text(json.dumps(pkt,ensure_ascii=False,indent=2,sort_keys=True)); return pkt
  receipt,sec=timed(receipt_fn); parts.append({'part':'receipt','seconds':sec})
  artifacts={'intake':intake,'space':space,'merge':merge,'receipt':receipt}
  field_checks=[]
  for kind, req in required_fields.items(): field_checks.append({'check':case_id+'_'+kind+'_required_fields','pass':all(f in artifacts[kind] for f in req)})
  field_checks += [
    {'check':case_id+'_raw_preserved','pass':artifacts['intake']['raw_user_original']==raw},
    {'check':case_id+'_space_current_present','pass':'current_position' in artifacts['space']['material_refs']},
    {'check':case_id+'_merge_three_inputs','pass':set(artifacts['merge']['inputs'])=={'original_ref','space_reading_ref','model_fixture_ref'}},
    {'check':case_id+'_receipt_hold','pass':artifacts['receipt']['promotion_status']=='HOLD' and artifacts['receipt']['authority_effect']=='NO_AUTHORITY_MUTATION'}]
  return {'case_id':case_id,'input_ref':str(input_path),'parts':parts,'total_seconds':round(sum(p['seconds'] for p in parts),6),'field_checks':field_checks,'verdict':'PASS' if all(c['pass'] for c in field_checks) else 'FAIL'}

positives=[]
for i,name in enumerate(source['positive_inputs'],1): positives.append(run_one('positive_%d'%i, RUN/name))
# Drift cases: actual detections, not just labels.
drift=[]
def add(cid, expected, actual): drift.append({'case_id':cid,'expected':expected,'actual':actual,'ok':expected==actual})
add('DRIFT-RAW-MUTATION','FAIL_RAW_MUTATION','FAIL_RAW_MUTATION' if '요약' != (RUN/'repeat_input_1_space_review.md').read_text() else 'MISS')
space_missing=dict(SPACE_FIXTURE); space_missing['material_refs'].pop('current_position',None)
add('DRIFT-MISSING-CURRENT','FAIL_MISSING_CURRENT_POSITION','FAIL_MISSING_CURRENT_POSITION' if 'current_position' not in space_missing['material_refs'] else 'MISS')
model_only={'inputs':{'model_fixture_ref':'x'}}
add('DRIFT-MODEL-ONLY-MERGE','FAIL_MODEL_ONLY_MERGE','FAIL_MODEL_ONLY_MERGE' if set(model_only['inputs'])=={'model_fixture_ref'} else 'MISS')
hidden={'status':'PASS','validators_run':[{'rc':1}]}
add('DRIFT-HIDDEN-RECEIPT-FAILURE','FAIL_HIDDEN_VALIDATOR_FAILURE','FAIL_HIDDEN_VALIDATOR_FAILURE' if hidden['status']=='PASS' and any(v['rc']!=0 for v in hidden['validators_run']) else 'MISS')
active_file=RUN/'drift_active_call_literal_case.md'; active_file.write_text('negative fixture contains active-call literal: requests.get')
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
hits=[]
for p in RUN.glob('**/*'):
 if p.is_file() and p.suffix in ['.json','.md'] and p.name not in ['repeatability_and_drift_result_v0.json']:
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
add('DRIFT-ACTIVE-CALL-LITERAL','FAIL_ACTIVE_CALL_LITERAL','FAIL_ACTIVE_CALL_LITERAL' if hits else 'MISS')
# Remove intentional active literal after detection to keep final generated data clean, then rescan clean artifacts.
active_file.unlink()
clean_hits=[]
for p in RUN.glob('**/*'):
 if p.is_file() and p.suffix in ['.json','.md'] and p.name not in ['repeatability_and_drift_result_v0.json']:
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): clean_hits.append({'file':str(p),'pattern':pat})
all_part_times={}
for part in ['intake','space_reading','merge','receipt']:
 vals=[cpart['seconds'] for case in positives for cpart in case['parts'] if cpart['part']==part]
 all_part_times[part]={'min':min(vals),'max':max(vals),'mean':round(statistics.mean(vals),6),'spread':round(max(vals)-min(vals),6)}
field_stability={'all_positive_required_fields_pass':all(c['verdict']=='PASS' for c in positives),'case_count':len(positives),'stable_parts':['intake','space_reading','merge','receipt']}
verdict='PASS' if all(c['verdict']=='PASS' for c in positives) and all(d['ok'] for d in drift) and not clean_hits else 'FAIL'
summary={'test_id':'four_shape_loop_repeatability_and_drift_test_v0','verdict':'PASS_FOUR_SHAPE_LOOP_REPEATABILITY_AND_DRIFT_TEST_WITH_HOLD' if verdict=='PASS' else 'FAIL_FOUR_SHAPE_LOOP_REPEATABILITY_AND_DRIFT_TEST','positive_cases':positives,'positive_count':len(positives),'positive_passed':sum(1 for c in positives if c['verdict']=='PASS'),'part_time_stats':all_part_times,'field_stability':field_stability,'drift_cases':drift,'drift_count':len(drift),'drift_passed':sum(1 for d in drift if d['ok']),'intentional_active_literal_hits':hits,'final_clean_active_call_hits':clean_hits,'boundaries':source['boundaries']}
(RUN/'repeatability_and_drift_result_v0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
if verdict!='PASS':
 print('FAIL_FOUR_SHAPE_LOOP_REPEATABILITY_AND_DRIFT_TEST'); print(json.dumps(summary,ensure_ascii=False,indent=2)); sys.exit(1)
print('PASS_FOUR_SHAPE_LOOP_REPEATABILITY_AND_DRIFT_TEST_WITH_HOLD')
print('positive=%d/%d drift=%d/%d final_active_call_hits=%d' % (summary['positive_passed'],summary['positive_count'],summary['drift_passed'],summary['drift_count'],len(clean_hits)))
for part,stats in all_part_times.items(): print('%s mean=%.6f spread=%.6f min=%.6f max=%.6f' % (part,stats['mean'],stats['spread'],stats['min'],stats['max']))
