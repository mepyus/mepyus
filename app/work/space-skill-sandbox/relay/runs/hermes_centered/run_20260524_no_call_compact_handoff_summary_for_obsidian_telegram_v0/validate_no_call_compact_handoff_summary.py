#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260524_no_call_compact_handoff_summary_for_obsidian_telegram_v0'
summary=json.loads((RUN/'no_call_compact_handoff_summary_for_obsidian_telegram_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_CALL_COMPACT_HANDOFF_SUMMARY_FOR_OBSIDIAN_TELEGRAM_20260524_V0.json').read_text())
problems=[]
if summary.get('summary_status')!='PASS_NO_CALL_COMPACT_HANDOFF_SUMMARY_WITH_HOLD': problems.append('summary status drift')
if len(summary.get('safe_entry_points',[]))!=2: problems.append('safe entry count drift')
if 'scrubbed card' not in summary.get('telegram_direction_memo',''): problems.append('telegram memo missing scrubbed card')
if 'rollup' not in summary.get('telegram_direction_memo',''): problems.append('telegram memo missing rollup')
for k in ['api_call','api_direct','local_http_endpoint_replay','local_server_start','model_execution','authority_mutation','registry_mutation','source_mutation']:
    if summary.get(k)!='NO': problems.append('summary '+k+' drift')
    if meta.get(k)!='NO': problems.append('meta '+k+' drift')
if summary.get('promotion')!='HOLD' or meta.get('promotion')!='HOLD': problems.append('promotion drift')
combined='\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_CALL_COMPACT_HANDOFF_SUMMARY_FOR_OBSIDIAN_TELEGRAM_20260524_V0.md', WORK/'VECTORFL_NO_CALL_COMPACT_HANDOFF_SUMMARY_USER_STATUS_CARD_20260524_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_CALL_COMPACT_HANDOFF_SUMMARY_20260524_V0.md'] if p.exists())
for bad in ['urllib.request.urlopen(','requests.get(','httpx.','fetch(','subprocess.run(','subprocess.Popen(','api_call: YES','api_direct: YES','local_http_endpoint_replay: YES','local_server_start: YES','authority_mutation: YES','promotion_status: PROMOTED']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_CALL_COMPACT_HANDOFF_SUMMARY')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_CALL_COMPACT_HANDOFF_SUMMARY_WITH_HOLD')
print('safe_entry_count=2')
print('api_call=NO')
print('promotion=HOLD')
