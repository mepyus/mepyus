#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_single_row_static_operator_card_rehearsal_v0'
card=json.loads((RUN/'single_row_static_operator_card_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_20260523_V0.json').read_text())
problems=[]
for k in ['title','verdict','guard_badge','trace_ref','evidence_receipt_ref','not_valid_for','hold_boundaries','render_policy']:
    if k not in card or card[k] in (None,'',[]): problems.append('missing '+k)
if card.get('verdict')!='PASS_WITH_HOLD': problems.append('verdict drift')
if card.get('guard_badge')!='HOLD': problems.append('guard_badge drift')
for k in ['static_only','no_network','no_api_call','no_local_server_start','no_subprocess_runner','show_hold','show_not_valid_for','show_trace_and_evidence_links']:
    if card.get('render_policy',{}).get(k) is not True: problems.append('render_policy missing '+k)
for k in ['api_call','api_direct','live_connector','authority_mutation','model_execution','schema_registry_mutation','dashboard_registry_mutation','source_row_mutation']:
    if card.get(k)!='NO': problems.append('card '+k+' drift')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation']:
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if meta.get('promotion')!='HOLD' or card.get('promotion')!='HOLD': problems.append('promotion drift')
for p in [RUN/'single_row_static_operator_card_v0.md', RUN/'single_row_static_operator_card_v0.html', WORK/'VECTORFL_NO_API_CALL_AUDIT_FOR_STATIC_OPERATOR_CARD_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p.relative_to(ROOT)))
combined='\n'.join(p.read_text() for p in [RUN/'single_row_static_operator_card_v0.md', RUN/'single_row_static_operator_card_v0.html', WORK/'VECTORFL_NO_API_CALL_AUDIT_FOR_STATIC_OPERATOR_CARD_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_20260523_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_server_start: YES','model_execution: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_MODEL_SINGLE_ROW_STATIC_OPERATOR_CARD_REHEARSAL_WITH_HOLD')
print('card_id='+card['card_id'])
print('api_call=NO')
print('api_direct=NO')
print('local_http_endpoint_replay=NO')
print('model_execution=NO')
print('promotion=HOLD')
