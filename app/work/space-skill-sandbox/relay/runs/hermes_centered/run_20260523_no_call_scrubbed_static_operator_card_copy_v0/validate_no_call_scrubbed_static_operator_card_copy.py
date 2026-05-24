#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_call_scrubbed_static_operator_card_copy_v0'
card=json.loads((RUN/'single_row_static_operator_card_scrubbed_no_call_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY_20260523_V0.json').read_text())
problems=[]
for k in ['source_reference_policy','legacy_endpoint_replay_labels_visible','local_http_endpoint_replay','local_server_start','subprocess_runner','api_call','api_direct','source_card_mutation']:
    if card.get(k) not in ['NO','SCRUBBED_DISPLAY_ONLY_NOT_ACTIVE_CALL']:
        problems.append('bad '+k+'='+repr(card.get(k)))
if card.get('source_reference_policy')!='SCRUBBED_DISPLAY_ONLY_NOT_ACTIVE_CALL': problems.append('source_reference_policy drift')
if card.get('legacy_endpoint_replay_labels_visible')!='NO': problems.append('legacy labels visible')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','source_card_mutation','registry_mutation']:
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if meta.get('promotion')!='HOLD' or card.get('promotion')!='HOLD': problems.append('promotion drift')
combined='\n'.join(p.read_text() for p in [RUN/'single_row_static_operator_card_scrubbed_no_call_v0.md', RUN/'single_row_static_operator_card_scrubbed_no_call_v0.html', WORK/'VECTORFL_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY_20260523_V0.md', WORK/'VECTORFL_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY_20260523_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_SCRUBBED_STATIC_OPERATOR_CARD_COPY_WITH_HOLD')
print('card_id='+card['card_id'])
print('api_call=NO')
print('local_http_endpoint_replay=NO')
print('source_card_mutation=NO')
print('promotion=HOLD')
