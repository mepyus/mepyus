#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_current_position_proposal_for_reuse_chain_v0'
proposal=json.loads((RUN/'no_call_current_position_proposal_for_reuse_chain_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_PROPOSAL_FOR_REUSE_CHAIN_20260524_V0.json').read_text())
problems=[]
if proposal.get('proposal_status')!='PROPOSAL_ONLY_WITH_HOLD': problems.append('not proposal-only')
if not proposal.get('lineage_all_pass'): problems.append('lineage not pass')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','root_pointer_mutation','source_mutation']:
    if proposal.get(k)!='NO': problems.append('proposal '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if proposal.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
forbidden_text=' '.join(proposal.get('forbidden_actions',[])).lower()
if not (('root' in forbidden_text and 'pointer' in forbidden_text) or 'current-position pointer' in forbidden_text): problems.append('missing root pointer forbidden action')
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_PROPOSAL_FOR_REUSE_CHAIN_20260524_V0.md', WORK/'VECTORFL_NO_CALL_CURRENT_POSITION_PROPOSAL_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_CURRENT_POSITION_PROPOSAL_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','root_pointer_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_CURRENT_POSITION_PROPOSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_CURRENT_POSITION_PROPOSAL_WITH_HOLD')
print('proposal_status='+proposal['proposal_status'])
print('lineage_all_pass='+str(proposal['lineage_all_pass']).lower())
print('api_call=NO')
print('root_pointer_mutation=NO')
print('promotion=HOLD')
