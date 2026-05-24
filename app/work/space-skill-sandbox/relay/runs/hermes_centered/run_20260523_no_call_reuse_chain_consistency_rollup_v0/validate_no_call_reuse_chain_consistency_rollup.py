#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_call_reuse_chain_consistency_rollup_v0'
rollup=json.loads((RUN/'no_call_reuse_chain_consistency_rollup_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_20260523_V0.json').read_text())
problems=[]
if not rollup.get('lineage_all_pass'): problems.append('lineage failed')
if len(rollup.get('layers',[]))!=5: problems.append('layer count drift')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if rollup.get(k)!='NO': problems.append('rollup '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if rollup.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
for item in rollup.get('layers',[]):
    if item.get('authority_mutation')!='NO': problems.append(item['layer']+' authority drift')
    if item.get('model_execution')!='NO': problems.append(item['layer']+' model drift')
for p in [WORK/'VECTORFL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_20260523_V0.md', WORK/'VECTORFL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p.relative_to(ROOT)))
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_20260523_V0.md', WORK/'VECTORFL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_20260523_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_REUSE_CHAIN_CONSISTENCY_ROLLUP_WITH_HOLD')
print('layer_count='+str(len(rollup['layers'])))
print('lineage_all_pass='+str(rollup['lineage_all_pass']).lower())
print('api_call=NO')
print('local_http_endpoint_replay=NO')
print('promotion=HOLD')
