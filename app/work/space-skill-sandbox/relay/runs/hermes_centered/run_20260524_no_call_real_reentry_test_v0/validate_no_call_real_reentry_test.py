#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_real_reentry_test_v0'
summary=json.loads((RUN/'no_call_real_reentry_test_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_REAL_REENTRY_TEST_20260524_V0.json').read_text())
problems=[]
if not summary.get('all_validators_pass'): problems.append('validators not pass')
if not summary.get('forbidden_scan_pass'): problems.append('forbidden scan not pass')
if summary.get('validator_pass_count')!=summary.get('validator_count'): problems.append('pass count mismatch')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if summary.get(k)!='NO': problems.append('summary '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if summary.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
for r in summary.get('results',[]):
    if r.get('rc')!=0: problems.append('validator failed '+r.get('validator','?'))
for s in summary.get('forbidden_scan',[]):
    if s.get('forbidden_active_matches'): problems.append('forbidden match '+s.get('path','?'))
if problems:
    print('FAIL_NO_CALL_REAL_REENTRY_TEST')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_REAL_REENTRY_TEST_WITH_HOLD')
print(f"validators={summary['validator_pass_count']}/{summary['validator_count']}")
print('forbidden_scan=PASS')
print('api_call=NO')
print('promotion=HOLD')
