#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_s4_s5_role_handoff_source_index_v0.json').read_text())
packet=json.loads((RUN/'06_s4_s5_role_handoff_function_test_v0.json').read_text())
codex=(RUN/'04_codex_s4_output_v0.txt').read_text(errors='ignore')
gemini=(RUN/'05_gemini_s5_output_v0.txt').read_text(errors='ignore')
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and packet['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'attached_to_s4_s5','pass':packet['attached_phase1_stage']==['S4_CODEX_EVALUATION','S5_GEMINI_LAYER_JUDGMENT']})
checks.append({'check':'budget_gate_heavy','pass':packet['budget_gate']['selected_mode']=='HEAVY_BUDGETED' and source['budget_gate']['codex_cli_execution'].startswith('YES') and source['budget_gate']['gemini_cli_execution'].startswith('YES')})
checks.append({'check':'actual_outputs_exist','pass':(RUN/'04_codex_s4_output_v0.txt').exists() and (RUN/'05_gemini_s5_output_v0.txt').exists() and len(codex)>300 and len(gemini)>300})
checks.append({'check':'codex_sections_present','pass':all(s in codex for s in ['ROLE_VALUE','ADDED_OBSERVATIONS','MISSED_OR_DUPLICATED','PHASE3_BACKLOG_CANDIDATE','HOLD_CONFIRMATION'])})
checks.append({'check':'gemini_sections_present','pass':all(s in gemini for s in ['ROLE_VALUE','ADDED_OBSERVATIONS','MISSED_OR_DUPLICATED','PHASE3_BACKLOG_CANDIDATE','HOLD_CONFIRMATION'])})
checks.append({'check':'codex_spatial_reentry_value','pass':'reentry' in codex.lower() and 'spatial' in codex.lower() and 'S4_REENTRY_SURFACE_MUST_PRESERVE_MINIMAL_SPACE_DELTA' in codex})
checks.append({'check':'gemini_layer_value','pass':'layer' in gemini.lower() and 'inward' in gemini.lower() and 'S3_STRUCTURAL_DELTA_BY_LAYER' in gemini})
checks.append({'check':'comparison_complementary','pass':packet['comparison']['relationship']=='COMPLEMENTARY_WITH_MINOR_OVERLAP' and 'productive' in packet['observed_gap']['description']})
checks.append({'check':'post_review_skipped_with_reason','pass':packet['budget_gate']['post_review_skipped'] is True and 'non-conflicting' in packet['budget_gate']['post_review_skip_reason']})
checks.append({'check':'observed_gap_and_phase3_backlog','pass':packet['observed_gap']['single_observation'] is True and packet['phase3_backlog_delta']['status']=='ACCUMULATE_NOT_FIX_NOW' and len(packet['phase3_backlog_delta']['children'])>=3})
checks.append({'check':'next_is_s6_operator_surface','pass':packet['next_test_candidate'].startswith('S6_OPERATOR_RECEIPT_REENTRY')})
checks.append({'check':'hold_no_authority','pass':packet['HOLD_receipt']['promotion_status']=='HOLD' and packet['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and packet['HOLD_receipt']['current_position_apply']=='NO'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md','.txt'] and p.name!='08_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_S4_S5_CODEX_GEMINI_ROLE_HANDOFF_FUNCTION_TEST_WITH_HOLD' if ok else 'FAIL_S4_S5_CODEX_GEMINI_ROLE_HANDOFF_FUNCTION_TEST','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'codex_seconds':packet['budget_gate']['codex_seconds'],'gemini_seconds':packet['budget_gate']['gemini_seconds'],'observed_gap':packet['observed_gap'],'phase3_backlog_delta':packet['phase3_backlog_delta'],'next_safe_lane':packet['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'08_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d active_hits=%d codex=%s gemini=%s next=%s elapsed=%ss' % (len(checks),len(hits),out['codex_seconds'],out['gemini_seconds'],out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
