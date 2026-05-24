#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_codex_return_merge_source_index_v0.json').read_text())
shape=json.loads((RUN/'02_codex_return_shape_review_v0.json').read_text())
merge=json.loads((RUN/'03_hermes_merge_from_codex_space_steward_return_v0.json').read_text())
gemini=(RUN/'04_USER_INSTRUCTION_FOR_GEMINI_LAYER_READER_DRY_RUN.md').read_text()
checks=[]
checks.append({'check':'codex_packet_exists','pass':source['space_refs'][0]['exists'] and len(source['space_refs'][0]['sha256'])==64})
checks.append({'check':'script_only_no_live_gemini','pass':source['budget_gate']['selected_mode']=='FAST_NO_CALL_LOCAL_VALIDATION' and source['budget_gate']['gemini_cli_execution']=='NO'})
checks.append({'check':'required_fields_present','pass':shape['required_fields_present'] and not shape['missing_required_fields']})
checks.append({'check':'referenced_material_4','pass':shape['referenced_material_count']==4})
checks.append({'check':'reinserted_material_8','pass':shape['reinserted_material_count']==8})
checks.append({'check':'boundary_all_no_or_hold','pass':shape['boundary_all_no_or_hold']})
checks.append({'check':'codex_read_expansion_recorded','pass':shape['read_files_count']==11 and shape['extra_read_files_count']==5})
checks.append({'check':'observed_gaps_recorded','pass':len(shape['observed_gaps'])==3})
checks.append({'check':'task_packet_gap_detected','pass':any(g['gap_id']=='GAP_EXPLICIT_TASK_PACKET_HANDLE_MISSING' for g in shape['observed_gaps'])})
checks.append({'check':'compact_index_gap_detected','pass':any(g['gap_id']=='GAP_COMPACT_INDEX_MISSING_NEXT_AFTER_ASSET_SAMPLE' for g in shape['observed_gaps'])})
checks.append({'check':'hermes_merge_delta_present','pass':len(merge['space_reference_delta'])==3 and merge['codex_return_ref'].endswith('08_CODEX_SPACE_STEWARD_RETURN_PACKET_DRY_RUN.json')})
checks.append({'check':'gemini_prompt_created','pass':'GEMINI_LAYER_READER' in gemini and 'JSON only' in gemini and 'Codex 질문' in gemini})
checks.append({'check':'gemini_prompt_has_codex_packet','pass':'08_CODEX_SPACE_STEWARD_RETURN_PACKET_DRY_RUN.json' in gemini})
checks.append({'check':'next_gemini_or_hold','pass':merge['next_safe_lane']=='OPTIONAL_BOUNDED_GEMINI_LAYER_READER_DRY_RUN_OR_HOLD_V0'})
checks.append({'check':'no_mutation_boundary','pass':all(source['boundary'][k]=='NO' for k in ['folder_tree_mutation','source_code_mutation','authority_mutation','registry_mutation','current_position_apply','api_direct_server_replay','gemini_live_call']) and source['boundary']['promotion']=='HOLD'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'forbidden_endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_CODEX_SPACE_STEWARD_RETURN_MERGED_FOR_GEMINI_WITH_HOLD' if ok else 'FAIL_CODEX_SPACE_STEWARD_RETURN_MERGE','checks':checks,'checks_count':len(checks),'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'codex_read_files_count':shape['read_files_count'],'referenced_material_count':shape['referenced_material_count'],'reinserted_material_count':shape['reinserted_material_count'],'observed_gaps_count':len(shape['observed_gaps']),'next_safe_lane':merge['next_safe_lane'],'authority_effect':'NO_AUTHORITY_MUTATION','folder_tree_mutation':'NO','promotion_status':'HOLD'}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d read_files=%d referenced=%d reinserted=%d gaps=%d active_hits=%d next=%s elapsed=%ss' % (out['checks_count'],out['codex_read_files_count'],out['referenced_material_count'],out['reinserted_material_count'],out['observed_gaps_count'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
