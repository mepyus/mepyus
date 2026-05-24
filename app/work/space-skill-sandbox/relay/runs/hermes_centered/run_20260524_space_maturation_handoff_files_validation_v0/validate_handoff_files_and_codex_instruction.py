#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_handoff_files_validation_source_index_v0.json').read_text())
validation=json.loads((RUN/'02_handoff_files_readability_validation_v0.json').read_text())
codex=(RUN/'03_USER_INSTRUCTION_FOR_CODEX_SPACE_STEWARD_DRY_RUN.md').read_text()
gemini=(RUN/'04_USER_INSTRUCTION_FOR_GEMINI_LAYER_READER_AFTER_CODEX.md').read_text()
checks=[]
checks.append({'check':'raw_original_saved','pass':(RUN/'00_user_original_verbatim.md').exists() and '코덱스에 어떻게 지시' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'script_only_no_live_agent','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_SCRIPT_ONLY_VALIDATION' and source['budget_gate']['codex_cli_execution']=='NO' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'draft_files_exist_and_hashed','pass':len(source['draft_files'])==7 and all(f['exists'] and len(f['sha256'])==64 and f['bytes']>0 for f in source['draft_files'])})
checks.append({'check':'codex_minimum_lte_7','pass':validation['codex_minimum_pass'] and validation['codex_input_minimum_count']==6})
checks.append({'check':'gemini_minimum_lte_5','pass':validation['gemini_minimum_pass'] and validation['gemini_input_minimum_count']==4})
checks.append({'check':'readability_pass','pass':validation['readability_pass']})
checks.append({'check':'asset_index_has_12_items','pass':validation['asset_index_items']==12})
checks.append({'check':'schema_codex_gemini_present','pass':validation['schema_has_codex_return'] and validation['schema_has_gemini_return']})
checks.append({'check':'codex_instruction_has_boundaries','pass':all(x in codex for x in ['폴더 이동 금지','파일 수정 금지','API/direct/server/replay 실행 금지','JSON 형태로만'])})
checks.append({'check':'codex_instruction_has_read_order','pass':all(str(i)+'.' in codex for i in range(1,7)) and '읽을 파일, 순서 고정' in codex})
checks.append({'check':'codex_instruction_has_packet_fields','pass':all(x in codex for x in ['referenced_material_findings','reinserted_material_findings','primary_layer_assignments_review','gemini_questions'])})
checks.append({'check':'gemini_instruction_present','pass':'Gemini layer-reader' in gemini and 'layer flattening' in gemini and 'Codex return packet' in gemini})
checks.append({'check':'no_mutation_boundary','pass':all(source['boundary'][k]=='NO' for k in ['folder_tree_mutation','source_code_mutation','authority_mutation','registry_mutation','current_position_apply','api_direct_server_replay','codex_live_call','gemini_live_call']) and source['boundary']['promotion']=='HOLD'})
checks.append({'check':'next_optional_codex_or_hold','pass':validation['next_safe_lane']=='OPTIONAL_BOUNDED_CODEX_SPACE_STEWARD_DRY_RUN_OR_HOLD_V0'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'forbidden_endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_SPACE_MATURATION_HANDOFF_FILES_VALIDATION_WITH_CODEX_INSTRUCTIONS_HOLD' if ok else 'FAIL_SPACE_MATURATION_HANDOFF_FILES_VALIDATION','checks':checks,'checks_count':len(checks),'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'codex_input_minimum_count':validation['codex_input_minimum_count'],'gemini_input_minimum_count':validation['gemini_input_minimum_count'],'asset_index_items':validation['asset_index_items'],'next_safe_lane':validation['next_safe_lane'],'authority_effect':'NO_AUTHORITY_MUTATION','folder_tree_mutation':'NO','promotion_status':'HOLD'}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d codex_files=%d gemini_files=%d active_hits=%d next=%s elapsed=%ss' % (out['checks_count'],out['codex_input_minimum_count'],out['gemini_input_minimum_count'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
