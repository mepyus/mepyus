#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_current_position_reentry_smoke_check_v0'
smoke=json.loads((RUN/'no_call_current_position_reentry_smoke_check_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_20260524_V0.json').read_text())
problems=[]
if smoke.get('smoke_status')!='PASS_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_WITH_HOLD': problems.append('smoke status drift')
if smoke.get('safe_entry_count')!=2: problems.append('safe entry count drift')
if not smoke.get('lineage_all_pass'): problems.append('lineage not pass')
if not smoke.get('reentry_does_not_point_to_endpoint_replay_as_action'): problems.append('reentry points to replay action')
for r in smoke.get('safe_entry_reads',[]):
    if not r.get('exists'): problems.append('missing safe entry '+r.get('path','?'))
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if smoke.get(k)!='NO': problems.append('smoke '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if smoke.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_20260524_V0.md', WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_CURRENT_POSITION_REENTRY_SMOKE_CHECK_WITH_HOLD')
print('safe_entry_count=2')
print('lineage_all_pass=true')
print('api_call=NO')
print('promotion=HOLD')
