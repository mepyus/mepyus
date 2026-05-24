#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_asset_sample_test_source_index_v0.json').read_text())
result=json.loads((RUN/'02_space_relayering_asset_sample_classification_v0.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and 'api 호출 보단 스크립트' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'script_only_budget','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_SCRIPT_ONLY_VALIDATION' and source['budget_gate']['api_direct_execution']=='NO' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'source_refs_exist','pass':len(source['space_refs'])==2 and all(r['exists'] and len(r['sha256'])==64 for r in source['space_refs'])})
checks.append({'check':'sample_assets_bounded','pass':8 <= len(source['sample_assets']) <= 14 and result['sample_count']==len(source['sample_assets'])})
checks.append({'check':'all_sample_hashes','pass':all(len(a['sha256'])==64 and a['bytes']>0 for a in source['sample_assets'])})
checks.append({'check':'classification_for_each_asset','pass':len(result['classification_results'])==result['sample_count'] and all(c['assigned_layers'] for c in result['classification_results'])})
checks.append({'check':'all_layers_covered','pass':all(v>=1 for v in result['layer_coverage'].values())})
checks.append({'check':'multi_layer_assets_detected','pass':result['multi_layer_assets_count']>=2})
checks.append({'check':'early_attach_detected','pass':result['early_attach_candidates_detected']>=2})
checks.append({'check':'function_strengthening_links_present','pass':sum(1 for c in result['classification_results'] if c['function_strengthening_links'])>=5})
checks.append({'check':'no_manual_low_confidence','pass':len(result['manual_review_candidates'])==0})
checks.append({'check':'observed_gaps_present','pass':len(result['observed_gaps'])>=2 and any('MULTIPLE_LAYERS' in g['gap_id'] for g in result['observed_gaps'])})
checks.append({'check':'next_crosslink_not_tree_move','pass':result['next_safe_lane']=='SPACE_RELAYERING_INDEX_CROSSLINK_PLAN_NO_TREE_MUTATION_V0' and 'Do not move folders yet' in result['recommendation']})
checks.append({'check':'hold_boundaries_no_mutation','pass':all(source['boundary'][k]=='NO' for k in ['folder_tree_mutation','source_code_mutation','authority_mutation','registry_mutation','current_position_apply','api_direct_server_replay']) and source['boundary']['promotion']=='HOLD'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='04_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_api_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_SPACE_RELAYERING_BLUEPRINT_ASSET_SAMPLE_TEST_WITH_HOLD' if ok else 'FAIL_SPACE_RELAYERING_BLUEPRINT_ASSET_SAMPLE_TEST','checks':checks,'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'sample_count':result['sample_count'],'layer_coverage':result['layer_coverage'],'early_attach_candidates_detected':result['early_attach_candidates_detected'],'multi_layer_assets_count':result['multi_layer_assets_count'],'next_safe_lane':result['next_safe_lane'],'authority_effect':'NO_AUTHORITY_MUTATION','promotion_status':'HOLD','folder_tree_mutation':'NO'}
(RUN/'04_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d sample=%d early_attach=%d active_hits=%d next=%s elapsed=%ss' % (len(checks),out['sample_count'],out['early_attach_candidates_detected'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
