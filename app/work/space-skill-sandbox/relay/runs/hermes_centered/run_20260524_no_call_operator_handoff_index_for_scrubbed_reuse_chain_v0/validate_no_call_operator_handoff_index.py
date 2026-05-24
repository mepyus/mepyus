#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_operator_handoff_index_for_scrubbed_reuse_chain_v0'
idx=json.loads((RUN/'no_call_operator_handoff_index_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_OPERATOR_HANDOFF_INDEX_FOR_SCRUBBED_REUSE_CHAIN_20260524_V0.json').read_text())
problems=[]
if len(idx.get('safe_entry_points',[]))!=2: problems.append('safe entry count drift')
if not idx.get('lineage_all_pass'): problems.append('lineage not pass')
for blocked in ['api_contract_replay.py','api_drift_replay_gate.py','phase1_deterministic_stable_cycle.py']:
    if not any(blocked in p for p in idx.get('do_not_open_as_next_action',[])): problems.append('missing blocked '+blocked)
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if idx.get(k)!='NO': problems.append('index '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if idx.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_OPERATOR_HANDOFF_INDEX_FOR_SCRUBBED_REUSE_CHAIN_20260524_V0.md', WORK/'VECTORFL_NO_CALL_OPERATOR_HANDOFF_INDEX_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_OPERATOR_HANDOFF_INDEX_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_OPERATOR_HANDOFF_INDEX')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_OPERATOR_HANDOFF_INDEX_WITH_HOLD')
print('safe_entry_count='+str(len(idx['safe_entry_points'])))
print('lineage_all_pass='+str(idx['lineage_all_pass']).lower())
print('api_call=NO')
print('local_http_endpoint_replay=NO')
print('promotion=HOLD')
