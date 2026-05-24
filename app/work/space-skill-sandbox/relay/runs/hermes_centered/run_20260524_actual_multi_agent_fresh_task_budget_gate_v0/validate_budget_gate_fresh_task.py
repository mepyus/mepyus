#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
required=['00_fresh_task_original.md','01_hermes_fresh_task_interpretation_v0.json','02_fresh_task_source_index_v0.json','05_codex_budget_gate_output_v0.txt','06_gemini_budget_gate_output_v0.txt','07_budget_gate_codex_gemini_comparison_v0.json','08_vectorfl_heavy_vs_fast_budget_gate_policy_v0.json','08_vectorfl_heavy_vs_fast_budget_gate_policy_v0.md','09_budget_gate_execution_receipt_v0.json']
checks=[]
checks.append({'check':'required_artifacts_exist','pass':all((RUN/p).exists() for p in required)})
policy=json.loads((RUN/'08_vectorfl_heavy_vs_fast_budget_gate_policy_v0.json').read_text())
receipt=json.loads((RUN/'09_budget_gate_execution_receipt_v0.json').read_text())
comparison=json.loads((RUN/'07_budget_gate_codex_gemini_comparison_v0.json').read_text())
checks.append({'check':'codex_gemini_once_each','pass':receipt['codex_cli_execution']=='YES' and receipt['gemini_cli_execution']=='YES' and receipt['post_review_execution']=='SKIPPED_BY_BUDGET_GATE'})
checks.append({'check':'policy_has_heavy_and_fast_triggers','pass':len(policy['heavy_mode_use_when'])>=5 and len(policy['fast_mode_use_when'])>=4})
checks.append({'check':'budget_thresholds_present','pass':all(k in policy['budget_thresholds'] for k in ['fast_target_seconds','budgeted_heavy_target_seconds','full_heavy_expected_seconds','post_review_gate'])})
checks.append({'check':'agreement_true','pass':comparison['agreement'] is True and comparison['post_review_decision']['needed'] is False})
checks.append({'check':'timings_positive','pass':all(v and v>0 for v in policy['timings'].values()),'observed':policy['timings']})
checks.append({'check':'hold_no_authority','pass':policy['authority_effect']=='NO_AUTHORITY_MUTATION' and policy['promotion_status']=='HOLD' and policy['registry_mutation']=='NO' and policy['current_position_apply']=='NO'})
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='10_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'active_endpoint_or_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
result={'verdict':'PASS_ACTUAL_MULTI_AGENT_FRESH_TASK_BUDGET_GATE_WITH_HOLD' if ok else 'FAIL_ACTUAL_MULTI_AGENT_FRESH_TASK_BUDGET_GATE','checks':checks,'active_hits':hits}
(RUN/'10_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('checks=%d active_hits=%d codex=%.2fs gemini=%.2fs' % (len(checks),len(hits),policy['timings']['codex_budget_gate_seconds'],policy['timings']['gemini_budget_gate_seconds']))
sys.exit(0 if ok else 1)
