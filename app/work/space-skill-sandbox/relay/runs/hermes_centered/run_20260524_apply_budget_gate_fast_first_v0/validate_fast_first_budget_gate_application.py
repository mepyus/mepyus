#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
required=['00_user_original_verbatim.md','01_fast_first_source_index_v0.json','02_budget_gate_mode_decision_v0.json','03_fast_first_operator_route_card_v0.json','03_fast_first_operator_route_card_v0.md','04_fast_first_budget_gate_application_receipt_v0.json','05_fast_first_budget_gate_application_trace_v0.json']
checks=[]
checks.append({'check':'required_artifacts_exist','pass':all((RUN/p).exists() for p in required)})
decision=json.loads((RUN/'02_budget_gate_mode_decision_v0.json').read_text())
route=json.loads((RUN/'03_fast_first_operator_route_card_v0.json').read_text())
receipt=json.loads((RUN/'04_fast_first_budget_gate_application_receipt_v0.json').read_text())
trace=json.loads((RUN/'05_fast_first_budget_gate_application_trace_v0.json').read_text())
checks.append({'check':'fast_first_selected','pass':decision['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and route['fast_mode_now']['selected'] is True})
checks.append({'check':'no_heavy_cli_execution','pass':decision['codex_cli_execution']=='NO' and decision['gemini_cli_execution']=='NO' and route['boundary']['codex_cli_execution']=='NO' and route['boundary']['gemini_cli_execution']=='NO'})
checks.append({'check':'fast_trigger_hits_present','pass':len(decision['fast_trigger_hits'])>=3 and len(decision['heavy_trigger_hits'])==0})
checks.append({'check':'timing_under_5s','pass':receipt['timings']['total_seconds'] < 5, 'observed':receipt['timings']['total_seconds']})
checks.append({'check':'hold_no_authority','pass':receipt['authority_effect']=='NO_AUTHORITY_MUTATION' and receipt['promotion_status']=='HOLD' and receipt['registry_mutation']=='NO' and receipt['current_position_apply']=='NO'})
checks.append({'check':'trace_rows_present','pass':len(trace['rows'])>=2,'observed':len(trace['rows'])})
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='06_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'active_endpoint_or_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
result={'verdict':'PASS_APPLY_BUDGET_GATE_FAST_FIRST_WITH_HOLD' if ok else 'FAIL_APPLY_BUDGET_GATE_FAST_FIRST','checks':checks,'active_hits':hits}
(RUN/'06_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('checks=%d active_hits=%d total=%.6fs' % (len(checks),len(hits),receipt['timings']['total_seconds']))
sys.exit(0 if ok else 1)
