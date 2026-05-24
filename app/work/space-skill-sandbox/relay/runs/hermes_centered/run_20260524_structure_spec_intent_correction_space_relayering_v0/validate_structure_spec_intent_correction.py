#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_structure_spec_intent_correction_source_index_v0.json').read_text())
correction=json.loads((RUN/'02_structure_spec_intent_correction_v0.json').read_text())
blueprint=json.loads((RUN/'03_space_relayering_blueprint_seed_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and '공간안에 너무 많은 자료가 난잡' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'previous_misread_corrected','pass':'operating-contract apply' in correction['previous_misread'] and 'folder-tree redesign' in correction['corrected_intent']})
checks.append({'check':'obsolete_smoke_lane_replaced','pass':correction['obsolete_next_lane']=='PHASE3_APPLIED_CONTRACT_SMOKE_TEST_NO_AUTHORITY_MUTATION_V0' and correction['corrected_next_lane'].startswith('SPACE_RELAYERING_BLUEPRINT')})
checks.append({'check':'source_refs_exist','pass':len(source['space_refs'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in source['space_refs'])})
checks.append({'check':'budget_fast_no_agent_calls','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'blueprint_hold_no_tree_mutation','pass':blueprint['status']=='BLUEPRINT_SEED_HOLD_NO_TREE_MUTATION' and blueprint['boundary']['folder_tree_mutation']=='NO'})
checks.append({'check':'big_frame_layers_7','pass':len(blueprint['phase1_big_frame_layers'])==7})
checks.append({'check':'function_connection_map_6','pass':len(blueprint['phase2_function_connection_map'])==6})
checks.append({'check':'future_tree_candidate_present','pass':len(blueprint['proposed_future_space_tree_candidate'])>=12 and any('40_agent_space_roles' in x for x in blueprint['proposed_future_space_tree_candidate'])})
checks.append({'check':'codex_gemini_early_attach_candidates','pass':len(blueprint['codex_gemini_early_attach_candidates'])==3 and all('codex_role' in c and 'gemini_role' in c for c in blueprint['codex_gemini_early_attach_candidates'])})
checks.append({'check':'space_roles_before_s4_possible','pass':any(c['stage']=='between S1 and S2' for c in blueprint['codex_gemini_early_attach_candidates']) and any(c['stage']=='after S2 source/rejected refs' for c in blueprint['codex_gemini_early_attach_candidates'])})
checks.append({'check':'asset_relayering_not_program_apply','pass':'future folder-tree/spec organization' in blueprint['purpose'] and 'programization' in blueprint['purpose']})
checks.append({'check':'next_asset_sample_test','pass':blueprint['next_test_candidate'].startswith('SPACE_RELAYERING_BLUEPRINT_ASSET_SAMPLE_TEST')})
checks.append({'check':'hold_boundaries_no_mutation','pass':all(source['boundary'][k]=='NO' for k in ['authority_mutation','registry_mutation','current_position_apply','source_code_mutation','folder_tree_mutation']) and source['boundary']['promotion']=='HOLD'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_api_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_STRUCTURE_SPEC_INTENT_CORRECTION_SPACE_RELAYERING_BLUEPRINT_WITH_HOLD' if ok else 'FAIL_STRUCTURE_SPEC_INTENT_CORRECTION_SPACE_RELAYERING_BLUEPRINT','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'layers':len(blueprint['phase1_big_frame_layers']),'functions':len(blueprint['phase2_function_connection_map']),'early_attach_candidates':len(blueprint['codex_gemini_early_attach_candidates']),'next_safe_lane':blueprint['next_test_candidate'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','folder_tree_mutation':'NO'}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d layers=%d functions=%d early_attach=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['layers'],out['functions'],out['early_attach_candidates'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
