#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,time,hashlib
RUN=Path(__file__).resolve().parent
start=time.perf_counter()
source=json.loads((RUN/'01_source_index_v0.json').read_text())
loop=json.loads((RUN/'02_hermes_centered_loop_contract_v0.json').read_text())
ref=json.loads((RUN/'03_codex_reference_path_index_v0.json').read_text())
task=json.loads((RUN/'05_codex_space_retrieval_task_packet_v0.json').read_text())
schema=json.loads((RUN/'06_expected_codex_space_retrieval_return_schema_v0.json').read_text())
merge=json.loads((RUN/'08_hermes_model_merge_packet_template_v0.json').read_text())
read_first=(RUN/'04_CODEX_READ_FIRST_FOR_SPACE_RETRIEVAL.md').read_text()
reentry=(RUN/'09_CODEX_REENTRY_AFTER_HERMES_MERGE_AND_EXECUTION.md').read_text()
cli=(RUN/'10_run_codex_space_retrieval_cli_TEMPLATE.sh').read_text()
checks=[]
checks.append({'check':'user_original_preserved','pass':(RUN/'00_user_original_verbatim.md').exists() and 'Hermes는 사용자 지시' in (RUN/'00_user_original_verbatim.md').read_text()})
checks.append({'check':'hermes_centered_principle','pass':'Hermes remains execution/merge center' in loop['principle'] and 'CODEX_SPACE_RETRIEVAL_BY_ORIGINAL_VIA_CLI_SCRIPT' in loop['flow']})
checks.append({'check':'codex_two_phase_role','pass':'CODEX_SPACE_RETRIEVAL_BY_ORIGINAL' in read_first and 'CODEX_SPACE_MATURATION_BY_REENTRY_RECORD' in reentry})
checks.append({'check':'gemini_only_via_codex_script_chain','pass':'Gemini is used only inside Codex-linked script-chain' in loop['principle'] and 'Hermes does not directly call Gemini' in reentry})
checks.append({'check':'no_direct_agent_api_boundary','pass':source['boundary']['codex_direct_api_invocation']=='NO' and source['boundary']['gemini_direct_api_invocation']=='NO' and source['boundary']['hermes_direct_gemini_invocation']=='NO'})
checks.append({'check':'reference_index_read_first_lte_6','pass':len(ref['read_first'])==6})
checks.append({'check':'task_packet_handle_explicit','pass':task['packet_id']=='05_codex_space_retrieval_task_packet_v0' and task['return_schema_ref'].endswith('06_expected_codex_space_retrieval_return_schema_v0.json')})
checks.append({'check':'codex_return_placeholder_exists','pass':(RUN/'07_CODEX_SPACE_RETRIEVAL_RETURN_PACKET_PLACEHOLDER.json').exists()})
checks.append({'check':'schema_has_required_fields','pass':all(k in schema for k in ['selected_space_material','rejected_space_material','changed_judgment_for_hermes','recommended_hermes_merge_inputs'])})
checks.append({'check':'hermes_merge_template_has_original_space_model','pass':all(k in merge['fields_to_fill_after_retrieval'] for k in ['original_reading','codex_retrieved_material_summary','hermes_model_reinterpretation','changed_judgment','execution_decision'])})
checks.append({'check':'codex_reentry_file_points_to_maturation','pass':'space maturation' in reentry.lower() and 'Return JSON fields' in reentry})
checks.append({'check':'cli_template_only_no_execution','pass':'TEMPLATE ONLY' in cli and 'codex --sandbox read-only' in cli})
checks.append({'check':'no_folder_source_authority_mutation','pass':all(source['boundary'][k]=='NO' for k in ['folder_tree_mutation','source_code_mutation','authority_mutation','registry_mutation','current_position_apply']) and source['boundary']['promotion']=='HOLD'})
# forbid active endpoint/API/replay patterns, allow textual direct_api_invocation boundary labels only
forbidden=[r'https?://',r'localhost',r'127\.0\.0\.1',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py',r'curl\s',r'fetch\(',r'requests\.']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md','.sh','.py'] and p.name!='validate_hermes_centered_codex_bridge_setup.py':
  txt=p.read_text(errors='ignore')
  for pat in forbidden:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'forbidden_api_endpoint_replay_hits_0','pass':len(hits)==0,'observed':len(hits)})
checks.append({'check':'source_refs_exist','pass':all(r['exists'] and r.get('sha256') for r in source['space_refs'])})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_HERMES_CENTERED_CODEX_RETRIEVAL_MATURATION_SETUP_NO_DIRECT_API_WITH_HOLD' if ok else 'FAIL_HERMES_CENTERED_CODEX_RETRIEVAL_MATURATION_SETUP','checks':checks,'checks_count':len(checks),'active_hits':hits,'elapsed_seconds':time.perf_counter()-start,'run_dir':str(RUN),'next_safe_lane':'USER_RUN_CODEX_SPACE_RETRIEVAL_CLI_OR_HOLD_V0','boundary':source['boundary'],'read_first_count':len(ref['read_first']),'promotion_status':'HOLD'}
(RUN/'11_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d read_first=%d active_hits=%d next=%s elapsed=%ss' % (out['checks_count'],out['read_first_count'],len(hits),out['next_safe_lane'],out['elapsed_seconds']))
sys.exit(0 if ok else 1)
