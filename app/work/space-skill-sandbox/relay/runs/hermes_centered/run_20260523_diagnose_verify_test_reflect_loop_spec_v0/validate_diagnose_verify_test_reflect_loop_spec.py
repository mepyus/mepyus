#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
problems=[]
md=ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md'
js=ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.json'
spec=ROOT/'app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_20260523_V0.md'
quick=ROOT/'app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_QUICKSTART_20260523_V0.md'
dash=ROOT/'app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_DASHBOARD_20260523_V0.json'
for p in [md,js,spec,quick,dash]:
    if not p.exists(): problems.append('missing '+str(p))
text=md.read_text(encoding='utf-8') if md.exists() else ''
spect=spec.read_text(encoding='utf-8') if spec.exists() else ''
for token in ['BUNDLE-08-DIAGNOSE-VERIFY-TEST-REFLECT','diagnosis: real Codex review found quickstart exists/hash stale entry','real_codex_execution: YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET','promotion_status: HOLD','vectorfl_authority_mutation: no']:
    if token not in text: problems.append('bundle md missing '+token)
for token in ['S1 Diagnose','S2 Verify','S3 Test','S4 Reflect','S5 Apply','S6 Surface','S7 Receipt','S8 Decide next','closed rehearsal alone would not have caught these real CLI/index contract issues']:
    if token not in spect: problems.append('spec missing '+token)
if 'exists=FALSE sha256=PENDING_OR_MISSING' in text:
    problems.append('stale pending/missing still present in md')
try:
    data=json.loads(js.read_text(encoding='utf-8'))
    if data.get('bundle_count') != 9: problems.append('bundle_count not 9')
    b0=next((b for b in data['bundles'] if b['bundle_id']=='BUNDLE-00-START-HERE'), None)
    if not b0: problems.append('missing BUNDLE-00')
    else:
        q=next((f for f in b0['files'] if f['path']=='app/work/VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md'), None)
        if not q: problems.append('missing quickstart file entry')
        else:
            actual=hashlib.sha256((ROOT/q['path']).read_bytes()).hexdigest()
            if not q.get('exists'): problems.append('quickstart exists false in json')
            if q.get('sha256') != actual: problems.append('quickstart hash mismatch')
    b8=next((b for b in data['bundles'] if b['bundle_id']=='BUNDLE-08-DIAGNOSE-VERIFY-TEST-REFLECT'), None)
    if not b8: problems.append('missing BUNDLE-08')
    else:
        paths=[f['path'] for f in b8['files']]
        for required in ['app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_20260523_V0.md','app/work/VECTORFL_REAL_CODEX_REVIEW_ONLY_BUNDLE_AUDIT_SUMMARY_20260523_V0.md']:
            if required not in paths: problems.append('BUNDLE-08 missing '+required)
except Exception as e:
    problems.append('json validation error '+repr(e))
for bad in ['promotion_status: PROMOTED','authority_mutation: YES','Program Alpha readiness: YES','M4 module confirmation: YES','real_gemini_execution: YES','live DB intake enabled']:
    if bad in text or bad in spect: problems.append('contamination '+bad)
if problems:
    print('FAIL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_WITH_HOLD')
print('bundle_count=9')
print('s1_s8_loop=REQUIRED')
print('quickstart_freshness_gap=REPAIRED')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
