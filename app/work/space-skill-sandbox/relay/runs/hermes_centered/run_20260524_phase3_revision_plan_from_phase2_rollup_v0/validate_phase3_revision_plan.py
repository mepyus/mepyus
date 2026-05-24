#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_phase3_revision_plan_source_index_v0.json').read_text())
plan=json.loads((RUN/'02_phase3_revision_plan_from_phase2_rollup_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and plan['user_original_verbatim']==(RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'plan_only_purpose','pass':'without applying changes yet' in plan['purpose'] and 'not one-by-one' in plan['basis']})
checks.append({'check':'source_refs_exist','pass':len(plan['space_references_used'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in plan['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':set(r['ref_id'] for r in plan['space_references_used'])==set(d['ref_id'] for d in plan['space_reference_delta'])})
checks.append({'check':'budget_fast_no_calls','pass':plan['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and plan['budget_gate']['codex_cli_execution']=='NO' and plan['budget_gate']['gemini_cli_execution']=='NO'})
items=plan['revision_plan_items']
checks.append({'check':'five_grouped_revisions','pass':len(items)==5 and all(i['from_patterns'] for i in items)})
checks.append({'check':'priority_split','pass':len(plan['priority_summary']['MUST_FIX'])==2 and len(plan['priority_summary']['SHOULD_FIX'])==2 and len(plan['priority_summary']['WATCH_ONLY'])==1})
checks.append({'check':'all_not_apply_now','pass':all(i['not_apply_now'] is True for i in items)})
checks.append({'check':'acceptance_tests_present','pass':all(i['acceptance_test'] and i['planned_change'] for i in items)})
checks.append({'check':'whole_flow_stages_present','pass':all(i['affected_stages'] for i in items) and any('S1_INTAKE' in i['affected_stages'] for i in items) and any('S6_OPERATOR_RECEIPT_REENTRY' in i['affected_stages'] for i in items)})
checks.append({'check':'non_convergence_guard','pass':'Do not apply any single revision directly from one observation' in plan['non_convergence_guard']})
checks.append({'check':'hold_boundaries_complete','pass':plan['hold_boundaries']['authority_mutation']=='NO' and plan['hold_boundaries']['implementation_apply']=='NO' and plan['hold_boundaries']['source_schema_change']=='NO' and plan['hold_boundaries']['promotion']=='HOLD'})
checks.append({'check':'observed_gap_requires_approval','pass':plan['observed_gap']['severity']=='HIGH' and 'separate authorization lane' in plan['observed_gap']['description']})
checks.append({'check':'next_is_review_apply_decision','pass':plan['next_test_candidate'].startswith('PHASE3_REVISION_PLAN_REVIEW_AND_APPLY_DECISION')})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE3_REVISION_PLAN_FROM_PHASE2_ROLLUP_WITH_HOLD' if ok else 'FAIL_PHASE3_REVISION_PLAN_FROM_PHASE2_ROLLUP','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'items':len(items),'priority_summary':plan['priority_summary'],'observed_gap':plan['observed_gap'],'next_safe_lane':plan['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','implementation_apply':'NO'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d items=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),len(items),len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
