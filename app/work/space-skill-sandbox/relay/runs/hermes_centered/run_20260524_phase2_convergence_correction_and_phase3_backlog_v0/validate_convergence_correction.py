#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_convergence_correction_source_index_v0.json').read_text())
backlog=json.loads((RUN/'02_phase3_backlog_deferred_validator_checklist_work_v0.json').read_text())
refocus=json.loads((RUN/'03_phase2_refocus_work_evaluation_list_v0.json').read_text())
report=(RUN/'04_convergence_correction_report_v0.md').read_text()
checks=[]
checks.append({'check':'user_correction_preserved','pass':(RUN/'00_user_correction_verbatim.md').exists() and '3차 테스트' in (RUN/'00_user_correction_verbatim.md').read_text()})
checks.append({'check':'too_convergent_accepted','pass':refocus['corrected_verdict']=='USER_CORRECTION_ACCEPTED_TOO_CONVERGENT' and '너무 수렴' in report})
checks.append({'check':'phase3_backlog_created','pass':backlog['classification']=='PHASE3_BACKLOG_HOLD' and len(backlog['deferred_items'])>=3})
checks.append({'check':'checklist_negative_cases_deferred','pass':any('CHECKLIST_NEGATIVE' in x['item'] for x in backlog['deferred_items'])})
checks.append({'check':'phase2_refocus_has_work_lanes','pass':refocus['classification']=='PHASE2_REFOCUS_HOLD' and len(refocus['work_lanes'])>=4})
checks.append({'check':'next_is_work_selection_not_validator','pass':refocus['next_safe_lane']=='PHASE2_WORK_SELECTION_BOARD_SPACE_REFERENCED_NO_AUTHORITY_MUTATION_V0'})
checks.append({'check':'budget_gate_fast_no_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'hold_no_authority','pass':source['boundary']['authority_mutation']=='NO' and source['boundary']['promotion']=='HOLD'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_CONVERGENCE_CORRECTION_PHASE3_BACKLOG_WITH_HOLD' if ok else 'FAIL_PHASE2_CONVERGENCE_CORRECTION_PHASE3_BACKLOG','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','next_safe_lane':refocus['next_safe_lane']}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
