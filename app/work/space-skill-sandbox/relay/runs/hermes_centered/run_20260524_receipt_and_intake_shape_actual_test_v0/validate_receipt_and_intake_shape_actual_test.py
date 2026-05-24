#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys, time, re
RUN=Path(__file__).resolve().parent
SHAPE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_scenario_1_receipt_and_intake_function_shape_extraction_v0')
load=lambda p: json.loads(Path(p).read_text())
intake_shape=load(SHAPE/'vectorfl_original_intake_packet_shape_candidate_v0.json')
receipt_shape=load(SHAPE/'vectorfl_receipt_writer_shape_candidate_v0.json')
cases=load(RUN/'actual_test_cases_v0.json')
results=[]

def build_intake(case):
    return {
      'packet_id': case['case_id'].lower()+'_packet',
      'classification':'candidate_packet_input_layer_no_authority_mutation',
      'source_layer':'input_layer',
      'raw_user_original':case.get('raw_user_original',''),
      'interpreted_constraints':['space reading required','do not rely on model only'],
      'watch_notes':['actual shape test fixture'],
      'guard_status':'PASS_WITH_HOLD',
      'authority_effect':case.get('authority_effect','NO_AUTHORITY_MUTATION'),
      'promotion_status':'HOLD'
    }

def validate_intake(pkt, declared_original=None):
    req=list(intake_shape['required_fields'].keys())
    for f in req:
      if f not in pkt: return False,'MISSING_'+f
    if pkt['source_layer']!='input_layer': return False,'BAD_SOURCE_LAYER'
    if pkt['authority_effect']!='NO_AUTHORITY_MUTATION': return False,'AUTHORITY_DRIFT'
    if pkt['promotion_status']!='HOLD': return False,'PROMOTION_DRIFT'
    if declared_original is not None and pkt['raw_user_original']!=declared_original: return False,'RAW_MUTATION_DETECTED'
    if not pkt['raw_user_original']: return False,'EMPTY_ORIGINAL'
    return True,'PASS'

def build_receipt(case):
    validators=[{'path':'/local/no_call_validator.py','rc':case.get('validator_rc',0),'seconds':0.001,'stdout':'PASS' if case.get('validator_rc',0)==0 else 'FAIL','stderr':''}]
    receipt={
      'receipt_id':case['case_id'].lower()+'_receipt',
      'classification':'receipt_actual_shape_test_with_hold',
      'source_layer':'tool_reentry_layer',
      'status':case.get('status','PASS'),
      'validators_run':validators,
      'forbidden_scan':{'active_call_hits':[],'active_call_scan_status':case.get('active_call_scan_status','PASS'),'scan_hits':[]},
      'seconds':0.001,
      'guard_status':'PASS_WITH_HOLD',
      'authority_effect':'NO_AUTHORITY_MUTATION',
      'promotion_status':'HOLD',
      'api_call':'NO','api_direct':'NO','local_http_endpoint_replay':'NO','local_server_start':'NO','model_execution':case.get('model_execution','NO_FIXTURE_ONLY'),'codex_cli_execution':'NO','gemini_cli_execution':'NO','registry_mutation':'NO','current_position_apply':'NO'
    }
    if case.get('missing_boundary'):
      receipt.pop(case['missing_boundary'],None)
    return receipt

def validate_receipt(rcpt):
    for f in receipt_shape['required_fields'].keys():
      if f not in rcpt: return False,'MISSING_'+f
    for b in receipt_shape['boundary_fields']:
      if b not in rcpt: return False,'BOUNDARY_FIELD_MISSING_'+b
    if rcpt['authority_effect']!='NO_AUTHORITY_MUTATION': return False,'AUTHORITY_DRIFT'
    if rcpt['promotion_status']!='HOLD': return False,'PROMOTION_DRIFT'
    if rcpt['forbidden_scan']['active_call_scan_status']!='PASS': return False,'ACTIVE_CALL_SCAN_FAIL'
    if any(v.get('rc')!=0 for v in rcpt['validators_run']) and rcpt['status']=='PASS': return False,'HIDDEN_VALIDATOR_FAILURE'
    if not str(rcpt['model_execution']).startswith('NO'): return False,'MODEL_EXECUTION_DRIFT'
    return True,'PASS'

# Run positive cases: must pass.
for c in cases['positive_cases']:
    if c['kind']=='original_intake':
      artifact=build_intake(c); ok, reason=validate_intake(artifact)
    else:
      artifact=build_receipt(c); ok, reason=validate_receipt(artifact)
    (RUN/(c['case_id'].lower()+'.json')).write_text(json.dumps(artifact,ensure_ascii=False,indent=2,sort_keys=True))
    results.append({'case_id':c['case_id'],'expected':c['expected'],'actual':'PASS' if ok else 'FAIL_'+reason,'ok': ok and c['expected']=='PASS'})
# Run negative cases: must fail with expected category.
for c in cases['negative_cases']:
    if c['kind'].startswith('original_intake'):
      artifact=build_intake(c); ok, reason=validate_intake(artifact, c.get('declared_original'))
    else:
      artifact=build_receipt(c); ok, reason=validate_receipt(artifact)
    (RUN/(c['case_id'].lower()+'.json')).write_text(json.dumps(artifact,ensure_ascii=False,indent=2,sort_keys=True))
    actual='PASS' if ok else 'FAIL_'+reason
    expected_prefix=c['expected']
    results.append({'case_id':c['case_id'],'expected':c['expected'],'actual':actual,'ok': (not ok) and actual.startswith(expected_prefix)})
# Active forbidden primitive scan over generated artifacts.
primitive_patterns=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
hits=[]
for p in RUN.glob('*.json'):
  txt=p.read_text(errors='ignore')
  for pat in primitive_patterns:
    if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
summary={'test_id':'receipt_and_intake_shape_actual_test_v0','results':results,'positive_count':len(cases['positive_cases']),'negative_count':len(cases['negative_cases']),'passed_cases':sum(1 for r in results if r['ok']),'failed_cases':[r for r in results if not r['ok']],'active_call_hits':hits,'verdict':'PASS' if all(r['ok'] for r in results) and not hits else 'FAIL','boundaries':{'api_call':'NO','local_http_endpoint_replay':'NO','local_server_start':'NO','model_execution':'NO','authority_mutation':'NO','promotion':'HOLD'}}
(RUN/'actual_test_result_v0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
if summary['verdict']!='PASS':
  print('FAIL_RECEIPT_AND_INTAKE_SHAPE_ACTUAL_TEST')
  print(json.dumps(summary,ensure_ascii=False,indent=2))
  sys.exit(1)
print('PASS_RECEIPT_AND_INTAKE_SHAPE_ACTUAL_TEST_WITH_HOLD')
print('positive=%d negative=%d passed_cases=%d active_call_hits=%d' % (summary['positive_count'], summary['negative_count'], summary['passed_cases'], len(hits)))
