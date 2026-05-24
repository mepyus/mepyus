#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
result=json.loads((RUN/'02_applied_decision_table_validator_result_v0.json').read_text())
source=json.loads((RUN/'01_applied_validator_source_index_v0.json').read_text())
expected=['FAIL_AUTHORITY_OVERPROMOTION','FAIL_OPERATOR_OVERLOAD','FAIL_HEAVY_ESCALATION_MISSING','FAIL_MODEL_ONLY_DRIFT','FAIL_NO_SPACE_REFERENCE','FAIL_SPACE_REFERENCE_DECORATION_ONLY']
checks=[]
checks.append({'check':'applied_result_pass','pass':result['verdict']=='PASS_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_WITH_HOLD'})
checks.append({'check':'priority_order_exact','pass':result['priority_order']==expected,'observed':result['priority_order']})
checks.append({'check':'six_cases_blocked','pass':result['cases']==6 and result['blocked']==6})
by={r['case_id']:r for r in result['case_results']}
checks.append({'check':'authority_not_masked','pass':by['NEG_AUTHORITY_REF_WRITABLE']['actual_failure']=='FAIL_AUTHORITY_OVERPROMOTION' and 'FAIL_SPACE_REFERENCE_DECORATION_ONLY' in by['NEG_AUTHORITY_REF_WRITABLE']['signals']})
checks.append({'check':'operator_not_masked','pass':by['NEG_TOO_MANY_REFS_NO_HEAVY_ESCALATION']['actual_failure']=='FAIL_OPERATOR_OVERLOAD' and 'FAIL_SPACE_REFERENCE_DECORATION_ONLY' in by['NEG_TOO_MANY_REFS_NO_HEAVY_ESCALATION']['signals']})
checks.append({'check':'conflict_not_masked','pass':by['NEG_CONFLICT_NO_HEAVY_TRIGGER']['actual_failure']=='FAIL_HEAVY_ESCALATION_MISSING'})
checks.append({'check':'budget_gate_fast_no_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'hold_no_authority','pass':source['boundary']['authority_mutation']=='NO' and source['boundary']['promotion']=='HOLD'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 # Scan generated evidence artifacts, not the validator source itself; the source
 # necessarily contains forbidden-pattern literals as test patterns.
 if p.suffix in ['.json','.md'] and p.name!='03_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_META_WITH_HOLD' if ok else 'FAIL_PHASE2_DECISION_TABLE_APPLIED_VALIDATOR_META','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'03_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d active_hits=%d elapsed=%ss' % (len(checks),len(hits),out['elapsed_seconds']))
sys.exit(0 if ok else 1)
