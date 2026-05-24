#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_s6_operator_surface_source_index_v0.json').read_text())
packet=json.loads((RUN/'02_s6_operator_receipt_reentry_surface_function_test_v0.json').read_text())
surface=packet['operator_receipt_reentry_surface']
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and packet['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'attached_to_s6','pass':packet['attached_phase1_stage']=='S6_OPERATOR_RECEIPT_REENTRY'})
checks.append({'check':'space_refs_exist','pass':len(packet['space_references_used'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in packet['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in packet['space_references_used'])==set(d['ref_id'] for d in packet['space_reference_delta'])})
checks.append({'check':'minimal_space_delta_present','pass':'Space changed' in surface['minimal_space_delta'] and 'S6 operator receipt/reentry' in surface['minimal_space_delta']})
checks.append({'check':'hold_boundary_complete','pass':all(x in surface['hold_boundary'] for x in ['NO authority mutation','NO registry mutation','NO current-position apply','NO promotion','NO API/direct/server/replay'])})
checks.append({'check':'reentry_handles_present','pass':len(surface['what_to_use_for_reentry'])>=4 and 'root report json' in surface['what_to_use_for_reentry']})
checks.append({'check':'carry_forward_observations_s1_s5','pass':len(surface['carry_forward_observations'])==4 and all(s in ' '.join(surface['carry_forward_observations']) for s in ['S1','S2','S3','S4/S5'])})
checks.append({'check':'mind_sized_operator_surface','pass':surface['format']=='mind_sized_operator_card' and len(surface['carry_forward_observations'])<=5})
checks.append({'check':'function_results_pass','pass':all(v=='PASS' for v in packet['function_test_result'].values())})
checks.append({'check':'observed_gap_phase3_backlog','pass':packet['observed_gap']['single_observation'] is True and packet['phase3_backlog_delta']['status']=='ACCUMULATE_NOT_FIX_NOW'})
checks.append({'check':'next_is_s7_budget_rollup','pass':packet['next_test_candidate'].startswith('S7_BUDGET_GATE_SESSION_LOG')})
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
out={'verdict':'PASS_S6_OPERATOR_RECEIPT_REENTRY_HOLD_SURFACE_FUNCTION_TEST_WITH_HOLD' if ok else 'FAIL_S6_OPERATOR_RECEIPT_REENTRY_HOLD_SURFACE_FUNCTION_TEST','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'observed_gap':packet['observed_gap'],'phase3_backlog_delta':packet['phase3_backlog_delta'],'next_safe_lane':packet['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
