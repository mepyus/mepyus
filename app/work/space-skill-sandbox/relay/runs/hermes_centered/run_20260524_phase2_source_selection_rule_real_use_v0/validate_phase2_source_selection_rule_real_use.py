#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
packet=json.loads((RUN/'02_phase2_source_selection_rule_packet_v0.json').read_text())
neg=json.loads((RUN/'04_source_selection_rule_negative_cases_v0.json').read_text())
result=json.loads((RUN/'05_source_selection_rule_real_use_result_v0.json').read_text())
rule=packet['hermes_merge_or_execution_result']['rule']
checks=[]
required=['user_intent_verbatim_or_digest','space_references_used','space_reference_delta','hermes_merge_or_execution_result','codex_assessment','gemini_layer_questions','gemini_layer_assessment','lens_card_results','HOLD_receipt','next_safe_lane']
checks.append({'check':'phase2_packet_fields_present','pass':all(k in packet for k in required)})
checks.append({'check':'space_refs_exist','pass':all(Path(r['path']).exists() for r in packet['space_references_used'])})
checks.append({'check':'delta_for_each_ref','pass':len(packet['space_references_used'])==len(packet['space_reference_delta']) and all(len(d.get('changed_judgment',''))>40 for d in packet['space_reference_delta'])})
checks.append({'check':'rule_requires_changed_judgment','pass':'changed_judgment' in rule['required_for_each_ref'] and 'no changed_judgment' in rule['reject_ref_when']})
checks.append({'check':'rule_limits_default_refs','pass':rule['max_default_refs']<=4 and 'reference increases operator load without changing decision' in rule['reject_ref_when']})
checks.append({'check':'rule_has_heavy_escalation','pass':all(x in rule['escalate_to_heavy_when'] for x in ['source refs conflict','space_reference_delta unclear','architecture/principle pressure appears'])})
checks.append({'check':'not_model_only','pass':'prior Phase2' in packet['hermes_merge_or_execution_result']['why_not_model_only'] or 'space reports' in packet['hermes_merge_or_execution_result']['why_not_model_only']})
checks.append({'check':'codex_gemini_no_new_call_recorded','pass':packet['codex_assessment']['mode']=='NO_NEW_CALL_BUDGET_GATE' and packet['gemini_layer_assessment']['mode']=='NO_NEW_CALL_BUDGET_GATE' and result['new_codex_gemini_calls']=='NO_SKIPPED_BY_BUDGET_GATE'})
checks.append({'check':'negative_cases_cover_required','pass':set(n['expected'] for n in neg)=={'FAIL_SPACE_REFERENCE_DECORATION_ONLY','FAIL_OPERATOR_OVERLOAD','FAIL_AUTHORITY_OVERPROMOTION','FAIL_MODEL_ONLY_DRIFT','FAIL_NO_SPACE_REFERENCE'}})
checks.append({'check':'hold_no_authority','pass':packet['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and packet['HOLD_receipt']['promotion_status']=='HOLD' and packet['HOLD_receipt']['registry_mutation']=='NO' and packet['HOLD_receipt']['current_position_apply']=='NO'})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='06_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_SOURCE_SELECTION_RULE_REAL_USE_WITH_HOLD' if ok else 'FAIL_PHASE2_SOURCE_SELECTION_RULE_REAL_USE','checks':checks,'active_hits':hits}
(RUN/'06_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d negative_cases=%d active_hits=%d elapsed=%ss' % (len(checks),len(neg),len(hits),result['elapsed_seconds']))
sys.exit(0 if ok else 1)
