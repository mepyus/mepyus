#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_approved_no_call_current_position_entry_apply_v0'
entry=json.loads((WORK/'CURRENT_POSITION_20260524_NO_CALL_REUSE_CHAIN_AFTER_OPERATOR_HANDOFF_V0.json').read_text())
receipt=json.loads((WORK/'VECTORFL_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY_20260524_V0.json').read_text())
old=WORK/'CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md'
backup=RUN/'backup_CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md'
problems=[]
if hashlib.sha256(old.read_bytes()).hexdigest()!=hashlib.sha256(backup.read_bytes()).hexdigest(): problems.append('backup mismatch')
if entry.get('approved_by_user') is not True: problems.append('approval missing')
if entry.get('position')!='NO_CALL_OPERATOR_HANDOFF_ENTRYPOINT_REALIZED_WITH_HOLD': problems.append('position drift')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if entry.get(k)!='NO': problems.append('entry '+k+' drift')
    if receipt.get(k)!='NO': problems.append('receipt '+k+' drift')
if entry.get('promotion')!='HOLD' or receipt.get('promotion')!='HOLD': problems.append('promotion drift')
combined='\n'.join(p.read_text() for p in [WORK/'CURRENT_POSITION_20260524_NO_CALL_REUSE_CHAIN_AFTER_OPERATOR_HANDOFF_V0.md', WORK/'VECTORFL_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY_20260524_V0.md', WORK/'VECTORFL_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_APPROVED_NO_CALL_CURRENT_POSITION_ENTRY_APPLY_WITH_HOLD')
print('new_position_entry=CURRENT_POSITION_20260524_NO_CALL_REUSE_CHAIN_AFTER_OPERATOR_HANDOFF_V0')
print('backup_match=true')
print('api_call=NO')
print('promotion=HOLD')
