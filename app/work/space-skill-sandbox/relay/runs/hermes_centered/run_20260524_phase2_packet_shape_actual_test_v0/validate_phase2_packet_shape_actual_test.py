#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
packet=json.loads((RUN/'02_positive_phase2_packet_shape_actual_v0.json').read_text())
neg=json.loads((RUN/'03_phase2_packet_shape_negative_cases_v0.json').read_text())
result=json.loads((RUN/'04_phase2_packet_shape_actual_test_result_v0.json').read_text())
required=['user_intent_verbatim_or_digest','space_references_used','space_reference_delta','hermes_merge_or_execution_result','codex_assessment','gemini_layer_questions','gemini_layer_assessment','lens_card_results','HOLD_receipt','next_safe_lane']
checks=[]
checks.append({'check':'required_fields_present','pass':all(k in packet for k in required)})
checks.append({'check':'space_refs_exist','pass':all(Path(r['path']).exists() for r in packet['space_references_used'])})
checks.append({'check':'space_reference_delta_non_decorative','pass':len(packet['space_reference_delta'])>=3 and all(d.get('changed_judgment') and len(d['changed_judgment'])>30 for d in packet['space_reference_delta'])})
checks.append({'check':'not_model_only','pass':'space references' in packet['hermes_merge_or_execution_result']['why_not_model_only'].lower() or 'prior space' in packet['hermes_merge_or_execution_result']['why_not_model_only'].lower()})
checks.append({'check':'codex_and_gemini_fields_present_without_new_calls','pass':packet['codex_assessment']['mode'].startswith('NO_NEW_CALL') and packet['gemini_layer_assessment']['mode'].startswith('NO_NEW_CALL') and result['new_codex_gemini_calls']=='NO_SKIPPED_BY_BUDGET_GATE'})
checks.append({'check':'lens_results_cover_5','pass':len(packet['lens_card_results'])==5})
checks.append({'check':'negative_cases_cover_6','pass':len(neg)==6 and set(n['expected'] for n in neg)=={'FAIL_NO_SPACE_REFERENCE','FAIL_MODEL_ONLY_DRIFT','FAIL_SPACE_REFERENCE_DECORATION_ONLY','FAIL_INWARD_COLLAPSE','FAIL_AUTHORITY_OVERPROMOTION','FAIL_OPERATOR_OVERLOAD'}})
checks.append({'check':'hold_no_authority','pass':packet['HOLD_receipt']['authority_effect']=='NO_AUTHORITY_MUTATION' and packet['HOLD_receipt']['promotion_status']=='HOLD' and packet['HOLD_receipt']['registry_mutation']=='NO' and packet['HOLD_receipt']['current_position_apply']=='NO'})
checks.append({'check':'mind_sized_pass','pass':packet['lens_card_results']['mind_sized_bite'].startswith('PASS')})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='05_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
out={'verdict':'PASS_PHASE2_PACKET_SHAPE_ACTUAL_TEST_WITH_HOLD' if ok else 'FAIL_PHASE2_PACKET_SHAPE_ACTUAL_TEST','checks':checks,'active_hits':hits}
(RUN/'05_validation_result_v0.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
print(out['verdict'])
print('checks=%d negative_cases=%d active_hits=%d elapsed=%ss' % (len(checks),len(neg),len(hits),result['elapsed_seconds']))
sys.exit(0 if ok else 1)
