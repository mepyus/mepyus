#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_review_or_hold_current_position_proposal_v0'
review=json.loads((RUN/'review_or_hold_current_position_proposal_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL_20260524_V0.json').read_text())
problems=[]
if review.get('decision')!='HOLD_BY_DEFAULT': problems.append('decision drift')
if review.get('review_status')!='REVIEWED_HOLD_NO_AUTO_APPLY': problems.append('review status drift')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','root_pointer_mutation','source_mutation']:
    if review.get(k)!='NO': problems.append('review '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if review.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
assess=review.get('acceptance_assessment',{})
for k in ['lineage_all_pass','safe_entry_points_present','no_call_boundaries_present','root_pointer_mutation_blocked','authority_mutation_blocked','promotion_blocked']:
    if assess.get(k) is not True: problems.append('assessment '+k+' not true')
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL_20260524_V0.md', WORK/'VECTORFL_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','root_pointer_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_REVIEW_OR_HOLD_CURRENT_POSITION_PROPOSAL_WITH_HOLD')
print('decision='+review['decision'])
print('root_pointer_mutation=NO')
print('api_call=NO')
print('promotion=HOLD')
