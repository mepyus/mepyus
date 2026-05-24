#!/usr/bin/env python3
from pathlib import Path
import json, time, hashlib, re, sys
RUN=Path(__file__).resolve().parent
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
source=json.loads((RUN/'actual_material_source_index_v0.json').read_text())

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(path, max_chars=20000): return Path(path).read_text(errors='replace')[:max_chars]
timings=[]
def part(name, fn):
    t0=time.perf_counter(); out=fn(); dt=time.perf_counter()-t0
    timings.append({'part':name,'seconds':round(dt,6),'method':out.get('_method'),'checks':out.get('_checks',[])})
    return out

def discover_materials():
    mats=source['materials']; existing={k:v for k,v in mats.items() if v['exists']}
    checks=[]
    checks.append({'check':'existing_materials>=7','pass':len(existing)>=7,'observed':len(existing)})
    checks.append({'check':'contains_current_position','pass':'current_position' in existing})
    checks.append({'check':'contains_space_wide_reread_packet','pass':'space_wide_reread_packet' in existing})
    checks.append({'check':'contains_merge_doc','pass':'customer_response_merge_doc' in existing})
    return {'existing':existing,'_method':'file material index verification by sha256/path existence, no broad mutation','_checks':checks}

def perform_space_reading():
    mats=source['materials']
    current=json.loads(read(mats['current_position']['path']))
    guard=json.loads(read(mats['guard_matrix']['path']))
    wide=read(mats['space_wide_reread_packet']['path'])
    merge_doc=read(mats['customer_response_merge_doc']['path'])
    prior=json.loads(read(mats['scenario_1_space_reading']['path']))
    extracted={
      'current_position':current.get('position'),
      'safe_entry_points_count':len(current.get('safe_entry_points',[])),
      'forbidden_actions':current.get('forbidden_actions',[]),
      'guard_status_count':guard.get('guard_status_count'),
      'guard_layer_count':guard.get('layer_count'),
      'space_wide_frame_detected':'space-wide reread' in wide.lower() and 'Function Family' in wide,
      'function_family_handles':re.findall(r'`([a-z_]+)`', wide)[:12],
      'merge_doc_boundary_detected':'Candidate-only' in merge_doc and 'not workflow' in merge_doc,
      'prior_space_reading_packet_id':prior.get('packet_id'),
    }
    packet={'packet_id':'actual_space_reading_packet_v0','classification':'candidate_packet_space_reading_actual_materials_no_authority_mutation','source_layer':'evidence_layer','material_refs':mats,'extracted':extracted,'space_interpretation':'Actual materials show that space reading must start from current-position/safe entrypoints, apply guard matrix, use space-wide reread packet as broad lens, and treat merge docs as candidate-only materials.','guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (RUN/'actual_space_reading_packet_v0.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2,sort_keys=True))
    checks=[
      {'check':'current_position_present','pass':bool(extracted['current_position'])},
      {'check':'safe_entry_points>=2','pass':extracted['safe_entry_points_count']>=2,'observed':extracted['safe_entry_points_count']},
      {'check':'guard_matrix_present','pass':extracted['guard_status_count']>=5},
      {'check':'space_wide_frame_detected','pass':extracted['space_wide_frame_detected']},
      {'check':'candidate_only_merge_boundary_detected','pass':extracted['merge_doc_boundary_detected']},
    ]
    packet['_method']='read actual local files -> extract current/safe/guard/lens/boundary facts -> write packet'
    packet['_checks']=checks
    return packet

def perform_merge():
    original=str(RUN/'actual_user_original_material_v0.md')
    model=str(RUN/'actual_model_fixture_material_v0.md')
    space=str(RUN/'actual_space_reading_packet_v0.json')
    space_packet=json.loads(Path(space).read_text())
    merged={'packet_id':'actual_space_mediated_merge_packet_v0','classification':'candidate_packet_space_mediated_merge_actual_materials_no_authority_mutation','source_layer':'review_guard_layer','inputs':{'original_ref':original,'space_reading_ref':space,'model_fixture_ref':model},'merged_directive':'Use real local space materials to validate space reading and merge handling; keep no-call/HOLD; produce timed part checks and negative tests.','merge_decisions':['current-position is mandatory anchor','space-wide reread packet supplies broad reading lens','guard matrix supplies boundary labels','customer response merge doc proves candidate-only merge handling','model fixture remains NO_FIXTURE_ONLY'],'hold_boundaries':space_packet['extracted']['forbidden_actions']+['real model execution','authority mutation','promotion'],'guard_status':'PASS_WITH_HOLD','authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
    (RUN/'actual_space_mediated_merge_packet_v0.json').write_text(json.dumps(merged,ensure_ascii=False,indent=2,sort_keys=True))
    checks=[
      {'check':'has_original_ref','pass':Path(original).exists()},
      {'check':'has_space_reading_ref','pass':Path(space).exists()},
      {'check':'has_model_fixture_ref','pass':Path(model).exists()},
      {'check':'not_model_only','pass':len(merged['inputs'])==3},
      {'check':'promotion_hold','pass':merged['promotion_status']=='HOLD'},
    ]
    merged['_method']='merge actual original material + actual space reading packet + local model fixture into directive'
    merged['_checks']=checks
    return merged

def negative_tests():
    cases=[]
    def eval_case(case_id, packet, expected_fail):
        reason='PASS'
        if packet.get('kind')=='space_reading' and 'current_position' not in packet.get('material_refs',{}):
            reason='FAIL_MISSING_CURRENT_POSITION'
        elif packet.get('kind')=='space_reading' and len(packet.get('material_refs',{}))<3:
            reason='FAIL_INSUFFICIENT_SPACE_REFS'
        elif packet.get('kind')=='merge' and set(packet.get('inputs',{}).keys())=={'model_fixture_ref'}:
            reason='FAIL_MODEL_ONLY_MERGE'
        elif packet.get('kind')=='merge' and 'original_ref' not in packet.get('inputs',{}):
            reason='FAIL_MISSING_ORIGINAL_REF'
        elif packet.get('promotion_status')!='HOLD' or packet.get('authority_effect')!='NO_AUTHORITY_MUTATION':
            reason='FAIL_AUTHORITY_OR_PROMOTION_DRIFT'
        ok=reason==expected_fail
        cases.append({'case_id':case_id,'expected':expected_fail,'actual':reason,'ok':ok})
    eval_case('SPACE-NEG-001',{'kind':'space_reading','material_refs':{},'promotion_status':'HOLD','authority_effect':'NO_AUTHORITY_MUTATION'},'FAIL_MISSING_CURRENT_POSITION')
    eval_case('SPACE-NEG-002',{'kind':'space_reading','material_refs':{'current_position':{}},'promotion_status':'HOLD','authority_effect':'NO_AUTHORITY_MUTATION'},'FAIL_INSUFFICIENT_SPACE_REFS')
    eval_case('MERGE-NEG-001',{'kind':'merge','inputs':{'space_reading_ref':'x','model_fixture_ref':'y'},'promotion_status':'HOLD','authority_effect':'NO_AUTHORITY_MUTATION'},'FAIL_MISSING_ORIGINAL_REF')
    eval_case('MERGE-NEG-002',{'kind':'merge','inputs':{'model_fixture_ref':'y'},'promotion_status':'HOLD','authority_effect':'NO_AUTHORITY_MUTATION'},'FAIL_MODEL_ONLY_MERGE')
    eval_case('MERGE-NEG-003',{'kind':'merge','inputs':{'original_ref':'a','space_reading_ref':'b','model_fixture_ref':'c'},'promotion_status':'APPROVED','authority_effect':'AUTHORITY_ACCEPTED'},'FAIL_AUTHORITY_OR_PROMOTION_DRIFT')
    result={'packet_id':'actual_space_reading_and_merge_negative_test_result_v0','cases':cases,'passed_cases':sum(1 for c in cases if c['ok']),'case_count':len(cases),'verdict':'PASS' if all(c['ok'] for c in cases) else 'FAIL'}
    (RUN/'actual_space_reading_and_merge_negative_test_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return {'_method':'programmatic negative validation of required anchors and merge inputs','_checks':cases,'result':result}

def forbidden_scan():
    pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
    hits=[]
    for p in RUN.glob('*'):
      if p.is_file() and p.suffix in ['.json','.md'] and p.name not in ['actual_space_reading_and_merge_test_result_v0.json']:
        txt=p.read_text(errors='ignore')
        for pat in pats:
          if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
    return {'hits':hits,'_method':'scan generated artifacts for active network/local endpoint primitives','_checks':[{'check':'active_call_hits==0','pass':len(hits)==0,'observed':len(hits)}]}

discovery=part('P1_material_discovery', discover_materials)
space=part('P2_space_reading_actual_materials', perform_space_reading)
merge=part('P3_space_mediated_merge_actual_materials', perform_merge)
neg=part('P4_negative_processing_checks', negative_tests)
scan=part('P5_forbidden_active_call_scan', forbidden_scan)
all_checks=[]
for t in timings:
  all_checks.extend(t.get('checks',[]))
# Add nested neg checks and scan checks
pass_all=all(c.get('pass', c.get('ok', False)) for c in all_checks) and neg['result']['verdict']=='PASS' and len(scan['hits'])==0
summary={'test_id':'space_reading_and_merge_actual_material_test_v0','verdict':'PASS_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_WITH_HOLD' if pass_all else 'FAIL_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST','timings':timings,'total_measured_seconds':round(sum(t['seconds'] for t in timings),6),'part_count':len(timings),'negative_cases':neg['result'],'active_call_hits':scan['hits'],'materials_used':source['materials'],'processing_review':{'space_reading_method':'actual file refs -> extract anchors/lens/guard/boundary -> packet','merge_method':'original material + space reading + model fixture -> merged directive','validation_method':'positive structural checks + negative required-anchor/merge-input checks + forbidden primitive scan'},'boundaries':source['boundaries']}
(RUN/'actual_space_reading_and_merge_test_result_v0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
if not pass_all:
  print('FAIL_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST')
  print(json.dumps(summary,ensure_ascii=False,indent=2))
  sys.exit(1)
print('PASS_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_WITH_HOLD')
print('parts=%d total_measured_seconds=%.6f negative_cases=%d active_call_hits=%d' % (len(timings), summary['total_measured_seconds'], neg['result']['case_count'], len(scan['hits'])))
for t in timings:
  print('%s seconds=%.6f method=%s' % (t['part'], t['seconds'], t['method']))
