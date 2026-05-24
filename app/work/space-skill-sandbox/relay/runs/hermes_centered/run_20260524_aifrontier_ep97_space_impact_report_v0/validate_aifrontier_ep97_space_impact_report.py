#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
required=['00_user_original_verbatim.md','01_budget_gate_and_task_interpretation_v0.json','03_source_page_raw.html','04_article_text_extracted_v0.txt','04_article_extraction_meta_v0.json','07_codex_space_impact_output_v0.txt','08_gemini_layer_impact_output_v0.txt','09_hermes_article_space_impact_merge_v0.json','10_aifrontier_ep97_vectorfl_space_impact_report_v0.md','11_aifrontier_ep97_space_impact_report_receipt_v0.json','12_aifrontier_ep97_space_impact_trace_v0.json']
checks=[]
checks.append({'check':'required_artifacts_exist','pass':all((RUN/p).exists() for p in required)})
meta=json.loads((RUN/'04_article_extraction_meta_v0.json').read_text())
merge=json.loads((RUN/'09_hermes_article_space_impact_merge_v0.json').read_text())
receipt=json.loads((RUN/'11_aifrontier_ep97_space_impact_report_receipt_v0.json').read_text())
trace=json.loads((RUN/'12_aifrontier_ep97_space_impact_trace_v0.json').read_text())
report=(RUN/'10_aifrontier_ep97_vectorfl_space_impact_report_v0.md').read_text()
checks.append({'check':'article_extracted_substantial_text','pass':meta['char_count']>10000,'observed':meta['char_count']})
checks.append({'check':'codex_gemini_outputs_present','pass':(RUN/'07_codex_space_impact_output_v0.txt').stat().st_size>1000 and (RUN/'08_gemini_layer_impact_output_v0.txt').stat().st_size>1000})
checks.append({'check':'space_impact_classification_present','pass':merge['hermes_merged_space_impact']['classification']=='PRESSURE_AND_EXTENSION'})
checks.append({'check':'new_lenses_present','pass':all(x in merge['hermes_merged_space_impact']['primary_new_lens'] for x in ['T_brain/operator-load','mind-sized bite check','maintainability debt watch'])})
checks.append({'check':'report_mentions_core_article_terms','pass':all(term in report for term in ['AI-native','T_brain','slow AI','mind-sized','AI psychosis','컨트롤 레이어'])})
checks.append({'check':'trace_rows>=4','pass':len(trace['rows'])>=4,'observed':len(trace['rows'])})
checks.append({'check':'hold_no_authority','pass':receipt['authority_effect']=='NO_AUTHORITY_MUTATION' and receipt['promotion_status']=='HOLD' and receipt['registry_mutation']=='NO' and receipt['current_position_apply']=='NO'})
checks.append({'check':'timings_present','pass':all(v is not None and v>0 for v in receipt['timings'].values()),'observed':receipt['timings']})
pats=[r'127\.0\.0\.1:8879',r'localhost:8879',r'api_contract_replay\.py',r'api_drift_replay_gate\.py',r'phase1_deterministic_stable_cycle\.py']
hits=[]
for p in RUN.glob('*'):
 if p.suffix in ['.json','.md'] and p.name!='13_validation_result_v0.json':
  txt=p.read_text(errors='ignore')
  for pat in pats:
   if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append({'check':'endpoint_replay_hits==0','pass':len(hits)==0,'observed':len(hits)})
ok=all(c['pass'] for c in checks)
result={'verdict':'PASS_AIFRONTIER_EP97_SPACE_IMPACT_REPORT_WITH_HOLD' if ok else 'FAIL_AIFRONTIER_EP97_SPACE_IMPACT_REPORT','checks':checks,'active_hits':hits}
(RUN/'13_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('checks=%d trace_rows=%d endpoint_hits=%d article_chars=%d' % (len(checks),len(trace['rows']),len(hits),meta['char_count']))
sys.exit(0 if ok else 1)
