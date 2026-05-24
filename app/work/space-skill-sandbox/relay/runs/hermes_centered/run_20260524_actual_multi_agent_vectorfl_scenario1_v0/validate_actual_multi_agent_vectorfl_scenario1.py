#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
RUN=Path(__file__).resolve().parent
required=[
 '00_user_original_verbatim.md','01_hermes_original_interpretation_actual_v0.json','02_actual_multi_agent_source_index_v0.json',
 '05_codex_space_exploration_output_v0.txt','06_gemini_layer_reading_output_v0.txt','07_interpretation_comparison_actual_v0.json',
 '08_hermes_space_model_merge_actual_v0.json','09_hermes_executed_loop_design_actual_v0.md','10_hermes_execution_receipt_actual_multi_agent_v0.json',
 '13_codex_reinsertion_effect_output_v0.txt','14_gemini_post_merge_layer_output_v0.txt','15_full_process_comparison_speed_direction_analysis_v0.json','16_actual_multi_agent_trace_rows_v0.json'
]
checks=[]
checks.append({'check':'required_artifacts_exist','pass':all((RUN/p).exists() for p in required)})
analysis=json.loads((RUN/'15_full_process_comparison_speed_direction_analysis_v0.json').read_text())
trace=json.loads((RUN/'16_actual_multi_agent_trace_rows_v0.json').read_text())
receipt=json.loads((RUN/'10_hermes_execution_receipt_actual_multi_agent_v0.json').read_text())
checks.append({'check':'actual_agents_present','pass':set(analysis['actual_agents'])=={'Hermes','Codex','Gemini'}})
checks.append({'check':'codex_and_gemini_cli_marked_yes','pass':receipt['codex_cli_execution']=='YES' and receipt['gemini_cli_execution']=='YES'})
checks.append({'check':'trace_rows>=8','pass':len(trace['rows'])>=8,'observed':len(trace['rows'])})
checks.append({'check':'timings_present','pass':all(v and v>0 for v in analysis['time_speed'].values()),'observed':analysis['time_speed']})
checks.append({'check':'hold_no_authority','pass':receipt['authority_effect']=='NO_AUTHORITY_MUTATION' and receipt['promotion_status']=='HOLD' and receipt['registry_mutation']=='NO' and receipt['current_position_apply']=='NO'})
checks.append({'check':'comparison_includes_merge_improvement','pass':analysis['comparisons']['merged_result_vs_user_intent']['match']=='IMPROVED'})
# generated artifact scan: allow CLI logs, scan data/md/json except prompts/log stderr; no endpoint replay/server/local API primitives
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
    if p.suffix in ['.json','.md'] and p.name != '17_validation_result_v0.json':
        txt=p.read_text(errors='ignore')
        for pat in pats:
            if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'active_endpoint_or_replay_hits==0','pass':len(hits)==0,'observed':len(hits),'hits':hits})
ok=all(c['pass'] for c in checks)
result={'verdict':'PASS_ACTUAL_MULTI_AGENT_VECTORFL_SCENARIO1_WITH_HOLD' if ok else 'FAIL_ACTUAL_MULTI_AGENT_VECTORFL_SCENARIO1','checks':checks,'active_hits':hits}
(RUN/'17_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('checks=%d trace_rows=%d active_hits=%d' % (len(checks),len(trace['rows']),len(hits)))
sys.exit(0 if ok else 1)
