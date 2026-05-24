#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_s3_merge_trace_source_index_v0.json').read_text())
packet=json.loads((RUN/'02_s3_hermes_merge_trace_function_test_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and packet['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'attached_to_s3','pass':packet['attached_phase1_stage']=='S3_HERMES_MERGE_EXECUTION'})
checks.append({'check':'merge_has_original_space_model','pass':all(k in packet['original_plus_space_plus_model_merge'] for k in ['original_component','space_component','model_reasoning_component','merged_decision'])})
checks.append({'check':'selected_refs_count_4','pass':len(packet['selected_space_references_used'])==4 and all(r['exists'] for r in packet['selected_space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in packet['selected_space_references_used'])==set(d['ref_id'] for d in packet['space_reference_delta'])})
checks.append({'check':'why_not_model_only_sufficient','pass':'model-only' in packet['why_not_model_only'].lower() and 'space refs' in packet['why_not_model_only'].lower() and len(packet['why_not_model_only'])>120})
checks.append({'check':'merge_trace_step_effects','pass':len(packet['merge_trace'])>=5 and all(x.get('input') and x.get('effect') for x in packet['merge_trace'])})
# Allow explicit exclusion phrases like "not validator/checklist hardening"; reject only
# outputs whose artifact type or target is validator/checklist hardening.
out_text=' '.join(packet['hermes_merge_or_execution_result']['content']).lower()
checks.append({'check':'small_real_output_not_validator_hardening','pass':packet['hermes_merge_or_execution_result']['type']=='operator_status_card' and 'not validator/checklist hardening' in out_text and packet['tested_function'].startswith('S3_HERMES_MERGE_TRACE')})
checks.append({'check':'function_results_pass','pass':all(v=='PASS' for v in packet['function_test_result'].values())})
checks.append({'check':'observed_gap_and_phase3_backlog','pass':packet['observed_gap']['single_observation'] is True and packet['phase3_backlog_delta']['status']=='ACCUMULATE_NOT_FIX_NOW'})
checks.append({'check':'next_is_s4_s5_role_handoff','pass':packet['next_test_candidate'].startswith('S4_S5_CODEX_GEMINI_ROLE_HANDOFF')})
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
out={'verdict':'PASS_S3_HERMES_MERGE_TRACE_FUNCTION_TEST_WITH_HOLD' if ok else 'FAIL_S3_HERMES_MERGE_TRACE_FUNCTION_TEST','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'observed_gap':packet['observed_gap'],'phase3_backlog_delta':packet['phase3_backlog_delta'],'trace_steps':len(packet['merge_trace']),'next_safe_lane':packet['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d trace_steps=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['trace_steps'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
