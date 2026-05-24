#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
required=['00_user_original_verbatim.md','01_phase2_source_index_v0.json','02_hermes_phase2_interpretation_v0.json','03_t_brain_mind_sized_maintainability_lens_card_v0.json','05_codex_phase2_space_evaluation_output_v0.txt','07_gemini_phase2_structure_output_v0.txt','08_phase2_internal_exploration_structure_merge_v0.json','09_phase2_internal_structure_space_referenced_report_v0.md','10_phase2_internal_structure_space_referenced_receipt_v0.json','11_phase2_internal_structure_space_referenced_trace_v0.json']
checks=[]
checks.append({'check':'required_artifacts_exist','pass':all((RUN/p).exists() for p in required)})
merge=json.loads((RUN/'08_phase2_internal_exploration_structure_merge_v0.json').read_text())
receipt=json.loads((RUN/'10_phase2_internal_structure_space_referenced_receipt_v0.json').read_text())
trace=json.loads((RUN/'11_phase2_internal_structure_space_referenced_trace_v0.json').read_text())
card=json.loads((RUN/'03_t_brain_mind_sized_maintainability_lens_card_v0.json').read_text())
report=(RUN/'09_phase2_internal_structure_space_referenced_report_v0.md').read_text()
checks.append({'check':'space_not_answer_principle_present','pass':'Space is not the answer' in merge['phase2_operating_principle'] and 'primary evidence/reference layer' in merge['phase2_operating_principle']})
checks.append({'check':'five_lenses_present','pass':len(card['lenses'])==5 and all(x in [l['lens'] for l in card['lenses']] for x in ['T_brain_operator_load','mind_sized_bite','maintainability_debt_watch','ai_native_vs_assisted','slow_ai_guard'])})
checks.append({'check':'codex_and_gemini_present','pass':(RUN/'05_codex_phase2_space_evaluation_output_v0.txt').stat().st_size>1000 and (RUN/'07_gemini_phase2_structure_output_v0.txt').stat().st_size>1000})
checks.append({'check':'packet_fields_include_space_delta_and_gemini','pass':'space_reference_delta' in merge['adopted_phase2_packet_fields'] and 'gemini_layer_assessment' in merge['adopted_phase2_packet_fields']})
checks.append({'check':'stop_conditions_include_model_only_and_no_space','pass':any('MODEL_ONLY' in x for x in merge['stop_conditions']) and any('NO_SPACE_REFERENCE' in x for x in merge['stop_conditions'])})
checks.append({'check':'source_selection_rejects_decorative_citation','pass':'decoratively' in merge['source_selection_rule']['reject'] or 'decorative' in merge['source_selection_rule']['reject']})
checks.append({'check':'trace_rows>=4','pass':len(trace['rows'])>=4,'observed':len(trace['rows'])})
checks.append({'check':'hold_no_authority','pass':receipt['authority_effect']=='NO_AUTHORITY_MUTATION' and receipt['promotion_status']=='HOLD' and merge['registry_mutation']=='NO' and merge['current_position_apply']=='NO'})
checks.append({'check':'timings_present','pass':merge['timings']['codex_seconds'] and merge['timings']['gemini_seconds'] and merge['timings']['codex_seconds']>0 and merge['timings']['gemini_seconds']>0,'observed':merge['timings']})
checks.append({'check':'report_mentions_big_frame','pass':'내부로 수렴하지 않는다' in report and '공간자료가 판단을 어떻게 바꿨나' in report})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='12_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
result={'verdict':'PASS_PHASE2_INTERNAL_STRUCTURE_SPACE_REFERENCED_WITH_HOLD' if ok else 'FAIL_PHASE2_INTERNAL_STRUCTURE_SPACE_REFERENCED','checks':checks,'active_hits':hits}
(RUN/'12_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('checks=%d trace_rows=%d endpoint_hits=%d codex=%ss gemini=%ss' % (len(checks),len(trace['rows']),len(hits),merge['timings']['codex_seconds'],merge['timings']['gemini_seconds']))
sys.exit(0 if ok else 1)
