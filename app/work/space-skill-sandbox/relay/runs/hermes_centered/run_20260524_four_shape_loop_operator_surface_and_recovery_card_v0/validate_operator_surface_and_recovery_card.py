#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
RUN=Path(__file__).resolve().parent
card=json.loads((RUN/'four_shape_loop_operator_recovery_card_v0.json').read_text())
idx=json.loads((RUN/'operator_surface_source_index_v0.json').read_text())
required=['card_id','classification','verdict','current_position_candidate','safe_entrypoints','status_summary','timing_summary','hold_boundaries','authority_effect','promotion_status','registry_mutation','current_position_apply','api_call','local_http_endpoint_replay','local_server_start','model_execution','codex_cli_execution','gemini_cli_execution']
checks=[]
checks.append(('required_fields', all(k in card for k in required)))
checks.append(('safe_entrypoints_exist', all(v.get('exists') and Path(v.get('path','')).exists() for v in card['safe_entrypoints'].values())))
checks.append(('entrypoint_count>=5', len(card['safe_entrypoints'])>=5))
checks.append(('display_only_no_authority', card['authority_effect']=='NO_AUTHORITY_MUTATION' and card['promotion_status']=='HOLD' and card['registry_mutation']=='NO' and card['current_position_apply']=='NO'))
checks.append(('no_call_boundaries', card['api_call']=='NO' and card['local_http_endpoint_replay']=='NO' and card['local_server_start']=='NO' and card['model_execution']=='NO_FIXTURE_ONLY'))
checks.append(('repeatability_summary_present', card['status_summary']['repeatability'].startswith('3/3') and card['status_summary']['drift'].startswith('5/5')))
checks.append(('trace_rows_present', card['status_summary']['trace_rows']>=4))
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
hits=[]
for p in RUN.glob('*'):
    if p.suffix in ['.json','.md']:
        txt=p.read_text(errors='ignore')
        for pat in pats:
            if re.search(pat,txt): hits.append({'file':str(p),'pattern':pat})
checks.append(('active_call_hits==0', len(hits)==0))
ok=all(v for _,v in checks)
result={'verdict':'PASS_OPERATOR_SURFACE_AND_RECOVERY_CARD_WITH_HOLD' if ok else 'FAIL_OPERATOR_SURFACE_AND_RECOVERY_CARD','checks':[{'check':k,'pass':v} for k,v in checks],'active_call_hits':hits,'safe_entrypoints':len(card['safe_entrypoints'])}
(RUN/'operator_surface_validation_result_v0.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
print(result['verdict'])
print('safe_entrypoints=%d active_call_hits=%d checks=%d' % (result['safe_entrypoints'],len(hits),len(checks)))
sys.exit(0 if ok else 1)
