#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
table=json.loads((RUN/'02_guard_priority_mini_decision_table_v0.json').read_text())
matrix=json.loads((RUN/'03_guard_priority_masking_matrix_v0.json').read_text())
rows=table['decision_table']
order=[r['class'] for r in rows]
expected=['FAIL_AUTHORITY_OVERPROMOTION','FAIL_OPERATOR_OVERLOAD','FAIL_HEAVY_ESCALATION_MISSING','FAIL_MODEL_ONLY_DRIFT','FAIL_NO_SPACE_REFERENCE','FAIL_SPACE_REFERENCE_DECORATION_ONLY']
checks=[]
checks.append({'check':'six_rows_present','pass':len(rows)==6,'observed':len(rows)})
checks.append({'check':'priority_order_expected','pass':order==expected,'observed':order})
checks.append({'check':'authority_first','pass':rows[0]['class']=='FAIL_AUTHORITY_OVERPROMOTION' and any('promotion_status' in x for x in rows[0]['detect_when'])})
checks.append({'check':'decorative_last','pass':rows[-1]['class']=='FAIL_SPACE_REFERENCE_DECORATION_ONLY' and rows[-1]['masks']==[]})
checks.append({'check':'operator_before_decorative','pass':order.index('FAIL_OPERATOR_OVERLOAD') < order.index('FAIL_SPACE_REFERENCE_DECORATION_ONLY')})
checks.append({'check':'conflict_before_no_space','pass':order.index('FAIL_HEAVY_ESCALATION_MISSING') < order.index('FAIL_NO_SPACE_REFERENCE')})
checks.append({'check':'model_only_before_no_space','pass':order.index('FAIL_MODEL_ONLY_DRIFT') < order.index('FAIL_NO_SPACE_REFERENCE')})
checks.append({'check':'masking_repair_recorded','pass':'masked by decorative-citation' in matrix['known_masking_repair']['before'] and 'before citation-shape' in matrix['known_masking_repair']['after']})
checks.append({'check':'hold_candidate_not_authority','pass':'not schema' in table['not_authority'] and 'not router' in table['not_authority'] and 'not promotion' in table['not_authority']})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_GUARD_PRIORITY_DECISION_TABLE_WITH_HOLD' if ok else 'FAIL_PHASE2_GUARD_PRIORITY_DECISION_TABLE','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d rows=%d active_hits=%d elapsed=%ss' % (len(checks),len(rows),len(hits),out['elapsed_seconds']))
sys.exit(0 if ok else 1)
