#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_s2_source_selection_source_index_v0.json').read_text())
packet=json.loads((RUN/'02_s2_source_selection_function_test_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and packet['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'attached_to_s2','pass':packet['attached_phase1_stage']=='S2_SPACE_SELECTION'})
checks.append({'check':'non_validator_target','pass':'validator/checklist hardening' in packet['target'].lower() and 'excluded' in packet['space_reference_delta'][1]['changed_judgment'].lower()})
checks.append({'check':'selected_refs_max_4','pass':len(packet['selected_space_references'])<=4 and packet['source_selection_result']['max_default_refs']==4})
checks.append({'check':'selected_refs_exist_and_sha','pass':all(r['exists'] and len(r['sha256'])==64 for r in packet['selected_space_references'])})
checks.append({'check':'delta_for_each_selected_ref','pass':set(r['ref_id'] for r in packet['selected_space_references'])==set(d['ref_id'] for d in packet['space_reference_delta'])})
checks.append({'check':'each_delta_sufficient','pass':all(len(d.get('changed_judgment',''))>=30 for d in packet['space_reference_delta'])})
checks.append({'check':'rejected_refs_logged','pass':len(packet['rejected_space_references'])>=2 and all(r.get('rejected_because') for r in packet['rejected_space_references'])})
checks.append({'check':'conflict_no_heavy_needed','pass':packet['source_selection_result']['conflict_detected'] is False and packet['source_selection_result']['heavy_escalation_triggered'] is False})
checks.append({'check':'observed_gap_and_phase3_backlog','pass':packet['observed_gap']['single_observation'] is True and packet['phase3_backlog_delta']['status']=='ACCUMULATE_NOT_FIX_NOW'})
checks.append({'check':'next_is_s3_merge_not_validator','pass':packet['next_test_candidate'].startswith('S3_HERMES_MERGE_TRACE') and 'VALIDATOR_HARDENING' not in packet['next_test_candidate'] and 'CHECKLIST' not in packet['next_test_candidate']})
checks.append({'check':'budget_gate_fast_no_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'hold_no_authority','pass':packet['HOLD_receipt']['promotion_status']=='HOLD' and packet['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and packet['HOLD_receipt']['current_position_apply']=='NO'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_S2_SOURCE_SELECTION_FUNCTION_TEST_WITH_HOLD' if ok else 'FAIL_S2_SOURCE_SELECTION_FUNCTION_TEST','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'observed_gap':packet['observed_gap'],'phase3_backlog_delta':packet['phase3_backlog_delta'],'selected_count':len(packet['selected_space_references']),'rejected_count':len(packet['rejected_space_references']),'next_safe_lane':packet['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d selected=%d rejected=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['selected_count'],out['rejected_count'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
