#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_s7_budget_rollup_source_index_v0.json').read_text())
roll=json.loads((RUN/'02_s7_budget_gate_phase2_rollup_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and roll['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'attached_to_s7','pass':roll['attached_phase1_stage']=='S7_BUDGET_GATE'})
checks.append({'check':'source_refs_exist','pass':len(roll['space_references_used'])==7 and all(r['exists'] and len(r['sha256'])==64 for r in roll['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in roll['space_references_used'])==set(d['ref_id'] for d in roll['space_reference_delta'])})
log=roll['budget_session_log']
checks.append({'check':'fast_heavy_distribution','pass':set(log['FAST_NO_CALL_LOCAL_VALIDATION'])==set(['S1','S2','S3','S6','S7']) and log['HEAVY_BUDGETED']==['S4/S5']})
checks.append({'check':'external_runs_count','pass':log['codex_actual_runs']==1 and log['gemini_actual_runs']==1 and log['post_review_runs']==0})
checks.append({'check':'rollup_contains_s1_s6','pass':len(roll['phase2_function_test_rollup'])==5 and set(x['stage'] for x in roll['phase2_function_test_rollup'])==set(['S1','S2','S3','S4/S5','S6'])})
checks.append({'check':'all_prior_pass_hold','pass':all(x['verdict'].startswith('PASS_') and x.get('active_hits')==0 for x in roll['phase2_function_test_rollup'])})
patterns=roll['repeated_patterns_and_phase3_basis']
checks.append({'check':'patterns_present','pass':len(patterns)>=5 and all(p['pattern_id'].startswith('P') and p['phase3_revision_basis'] for p in patterns)})
checks.append({'check':'phase3_ready_not_applied','pass':roll['phase3_backlog_delta']['status']=='READY_FOR_PHASE3_PLANNING_HOLD_NOT_APPLIED' and len(roll['phase3_backlog_delta']['pattern_ids'])==len(patterns)})
checks.append({'check':'no_phase3_fix_applied','pass':roll['function_test_result']['no_phase3_fix_applied']=='PASS' and 'not patched immediately' in roll['phase3_backlog_delta']['reason']})
checks.append({'check':'observed_gap_high_rollup_warning','pass':roll['observed_gap']['severity']=='HIGH' and 'one-by-one convergence' in roll['observed_gap']['description']})
checks.append({'check':'next_phase3_plan_hold','pass':roll['next_test_candidate'].startswith('PHASE2_TO_PHASE3_REVISION_PLAN') and 'NO_AUTHORITY_MUTATION' in roll['next_test_candidate']})
checks.append({'check':'hold_no_authority','pass':roll['HOLD_receipt']['promotion_status']=='HOLD' and roll['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and roll['HOLD_receipt']['current_position_apply']=='NO'})
checks.append({'check':'budget_source_fast_no_call','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_S7_BUDGET_GATE_PHASE2_FUNCTION_TEST_ROLLUP_WITH_HOLD' if ok else 'FAIL_S7_BUDGET_GATE_PHASE2_FUNCTION_TEST_ROLLUP','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'patterns_count':len(patterns),'fast_stages':log['FAST_NO_CALL_LOCAL_VALIDATION'],'heavy_stages':log['HEAVY_BUDGETED'],'phase3_backlog_delta':roll['phase3_backlog_delta'],'observed_gap':roll['observed_gap'],'next_safe_lane':roll['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d patterns=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),len(patterns),len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
