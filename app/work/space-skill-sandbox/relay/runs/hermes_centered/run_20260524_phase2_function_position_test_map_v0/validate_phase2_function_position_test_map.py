#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_phase2_function_position_source_index_v0.json').read_text())
matrix=json.loads((RUN/'02_phase2_function_position_matrix_v0.json').read_text())
obs=json.loads((RUN/'03_phase2_session_observation_and_phase3_revision_backlog_v0.json').read_text())
board=json.loads((RUN/'04_phase2_work_selection_board_v0.json').read_text())
checks=[]
checks.append({'check':'user_original_preserved','pass':(RUN/'00_user_original_verbatim.md').exists() and '1차는 전체' in (RUN/'00_user_original_verbatim.md').read_text() and '3차' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'space_refs_read','pass':len(source['space_refs'])>=4 and all(r['exists'] for r in source['space_refs'])})
checks.append({'check':'phase_principle_correct','pass':'Phase1 = whole-flow' in matrix['principle'] and 'Phase2 = function placement' in matrix['principle'] and 'Phase3 = revise' in matrix['principle']})
checks.append({'check':'whole_flow_stages_covered','pass':len(matrix['whole_flow_stages'])>=7})
checks.append({'check':'each_stage_has_phase2_and_phase3','pass':all(s.get('phase2_function_tests') and s.get('phase3_revision_basis') for s in matrix['whole_flow_stages'])})
checks.append({'check':'session_observation_log_fields_present','pass':len(obs['observation_fields'])>=10 and len(obs['initial_observations'])>=3})
checks.append({'check':'phase3_not_one_by_one_rule_present','pass':'Do not modify globally from a single Phase2 observation' in obs['phase3_rule']})
checks.append({'check':'work_selection_board_present','pass':board['classification']=='PHASE2_WORK_SELECTION_BOARD_HOLD' and len(board['rows'])>=5})
checks.append({'check':'phase2_now_and_phase3_backlog_separated','pass':any(r['phase']=='Phase2 now' for r in board['rows']) and any(r['phase']=='Phase3 backlog' for r in board['rows'])})
checks.append({'check':'next_recommended_is_function_test_not_validator','pass':board['next_recommended'].startswith('S1_INTAKE') and 'VALIDATOR' not in board['next_recommended']})
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
out={'verdict':'PASS_PHASE2_FUNCTION_POSITION_TEST_MAP_WITH_HOLD' if ok else 'FAIL_PHASE2_FUNCTION_POSITION_TEST_MAP','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'next_safe_lane':board['next_recommended'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD'}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d stages=%d board_rows=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),len(matrix['whole_flow_stages']),len(board['rows']),len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
