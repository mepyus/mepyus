#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_call_source_reference_scrub_proposal_for_reuse_rows_v0'
proposal=json.loads((RUN/'no_call_source_reference_scrub_proposal_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_FOR_REUSE_ROWS_20260523_V0.json').read_text())
problems=[]
if len(proposal.get('scrub_rules',[])) < 6: problems.append('scrub rules too few')
for token in ['api_contract_replay.py','api_drift_replay_gate.py','phase1_deterministic_stable_cycle.py','/api/']:
    if not any(r.get('match')==token for r in proposal.get('scrub_rules',[])): problems.append('missing scrub token '+token)
for k in ['api_call','api_direct','local_http_endpoint_replay','model_execution','authority_mutation','source_mutation','registry_mutation']:
    if proposal.get(k)!='NO': problems.append('proposal '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if proposal.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
for forbidden in ['run stable-cycle wrapper','run endpoint replay scripts','start local server','fetch localhost endpoint','call external API','use API-direct','plan API adapter']:
    if forbidden not in proposal.get('forbidden_operations',[]): problems.append('missing forbidden '+forbidden)
for p in [WORK/'VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_FOR_REUSE_ROWS_20260523_V0.md', WORK/'VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p.relative_to(ROOT)))
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_FOR_REUSE_ROWS_20260523_V0.md', WORK/'VECTORFL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_20260523_V0.md'] if p.exists())
for bad in ['api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','model_execution: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_SOURCE_REFERENCE_SCRUB_PROPOSAL_WITH_HOLD')
print('scrub_rule_count='+str(len(proposal['scrub_rules'])))
print('api_call=NO')
print('api_direct=NO')
print('local_http_endpoint_replay=NO')
print('source_mutation=NO')
print('promotion=HOLD')
