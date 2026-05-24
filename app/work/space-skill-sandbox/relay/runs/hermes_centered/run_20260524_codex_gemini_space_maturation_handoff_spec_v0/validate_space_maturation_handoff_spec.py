#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_space_maturation_handoff_source_index_v0.json').read_text())
spec=json.loads((RUN/'02_codex_gemini_space_maturation_handoff_spec_v0.json').read_text())
asset=json.loads((RUN/'05_VECTORFL_ASSET_INDEX_DRAFT.json').read_text())
schema=json.loads((RUN/'08_VECTORFL_SPACE_MATURATION_PACKET_SCHEMA_DRAFT.json').read_text())
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and '작업하자' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'script_only_no_live_agents','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_SCRIPT_ONLY_SPEC_DRAFT' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'source_refs_exist','pass':len(source['space_refs'])==4 and all(r['exists'] and len(r['sha256'])==64 for r in source['space_refs'])})
checks.append({'check':'boundary_no_mutation','pass':all(source['boundary'][k]=='NO' for k in ['folder_tree_mutation','source_code_mutation','authority_mutation','registry_mutation','current_position_apply','api_direct_server_replay','codex_live_call','gemini_live_call']) and source['boundary']['promotion']=='HOLD'})
checks.append({'check':'core_loop_has_hermes_codex_gemini','pass':any('Hermes' in x for x in spec['core_loop']) and any('Codex' in x for x in spec['core_loop']) and any('Gemini' in x for x in spec['core_loop'])})
checks.append({'check':'roles_present','pass':set(spec['roles'])=={'HERMES_EXECUTION_WORKBENCH','CODEX_SPACE_STEWARD','GEMINI_LAYER_READER'}})
checks.append({'check':'handoff_files_7','pass':len(spec['handoff_files_to_generate'])==7})
checks.append({'check':'draft_files_exist','pass':all((RUN/p).exists() for p in ['03_VECTORFL_CURRENT_SPACE_HANDOFF_DRAFT.md','04_VECTORFL_SPACE_LAYER_MAP_DRAFT.json','05_VECTORFL_ASSET_INDEX_DRAFT.json','06_VECTORFL_CODEX_SPACE_STEWARD_GUIDE_DRAFT.md','07_VECTORFL_GEMINI_LAYER_READER_GUIDE_DRAFT.md','08_VECTORFL_SPACE_MATURATION_PACKET_SCHEMA_DRAFT.json','09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md'])})
checks.append({'check':'asset_index_primary_secondary','pass':len(asset['assets'])>=10 and all('primary_layer' in a and 'secondary_links' in a for a in asset['assets'])})
checks.append({'check':'layer_model_7','pass':len(spec['layer_model'])==7})
checks.append({'check':'early_attach_3','pass':len(spec['early_attach_points'])==3})
checks.append({'check':'phase2_patterns_preserved','pass':len(spec['phase2_patterns_to_preserve'])==5})
checks.append({'check':'codex_guide_operational','pass':'referenced_material' in (RUN/'06_VECTORFL_CODEX_SPACE_STEWARD_GUIDE_DRAFT.md').read_text() and 'Do not move files' in (RUN/'06_VECTORFL_CODEX_SPACE_STEWARD_GUIDE_DRAFT.md').read_text()})
checks.append({'check':'gemini_guide_layer_reader','pass':'layer re-interpretation' in (RUN/'07_VECTORFL_GEMINI_LAYER_READER_GUIDE_DRAFT.md').read_text() and 'flattening' in (RUN/'07_VECTORFL_GEMINI_LAYER_READER_GUIDE_DRAFT.md').read_text()})
checks.append({'check':'packet_schema_required_fields','pass':all(k in schema for k in ['codex_return_packet_required','gemini_return_packet_required','hermes_merge_packet_required']) and 'boundary' in schema['codex_return_packet_required'] and 'boundary' in schema['gemini_return_packet_required']})
checks.append({'check':'next_validation_lane','pass':spec['next_safe_lane']=='SPACE_MATURATION_HANDOFF_FILES_DRAFT_VALIDATION_NO_FOLDER_MOVE_V0'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='11_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'forbidden_endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_CODEX_GEMINI_SPACE_MATURATION_HANDOFF_SPEC_WITH_HOLD' if ok else 'FAIL_CODEX_GEMINI_SPACE_MATURATION_HANDOFF_SPEC','checks':checks,'checks_count':len(checks),'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'draft_files':7,'asset_index_items':len(asset['assets']),'early_attach_points':len(spec['early_attach_points']),'next_safe_lane':spec['next_safe_lane'],'authority_effect':'NO_AUTHORITY_MUTATION','folder_tree_mutation':'NO','promotion_status':'HOLD'}
(RUN/'11_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d draft_files=%d assets=%d early_attach=%d active_hits=%d next=%s elapsed=%ss' % (out['checks_count'],out['draft_files'],out['asset_index_items'],out['early_attach_points'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
