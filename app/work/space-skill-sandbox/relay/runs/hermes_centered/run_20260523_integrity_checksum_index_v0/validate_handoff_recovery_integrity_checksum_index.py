#!/usr/bin/env python3
from pathlib import Path
import json, sys, subprocess
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
index=ROOT/'app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_20260523_V0.md'
jfile=ROOT/'app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_20260523_V0.json'
quick=ROOT/'app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_QUICK_VERIFY_20260523_V0.md'
problems=[]
for p in [index,jfile,quick]:
    if not p.exists(): problems.append('missing '+str(p))
text='\n'.join(p.read_text(encoding='utf-8') for p in [index,jfile,quick] if p.exists())
for tok in ['HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_WITH_HOLD','INTEGRITY_QUICK_VERIFY_CARD_WITH_HOLD','sha256sum','promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','v1_snapshot_creation: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing token '+tok)
data=json.loads(jfile.read_text(encoding='utf-8')) if jfile.exists() else {}
if data.get('file_count') != 16: problems.append('file_count mismatch')
if data.get('expected_file_count') != 16: problems.append('expected_file_count mismatch')
if data.get('promotion') != 'HOLD': problems.append('promotion drift')
if data.get('authority_mutation') != 'NO': problems.append('authority drift')
if data.get('model_execution') != 'NO': problems.append('model execution drift')
entries=data.get('entries',[])
if len(entries)!=16: problems.append('entry length mismatch')
for e in entries:
    p=ROOT/e.get('path','')
    if not p.exists(): problems.append('indexed file missing '+str(p))
# Recompute via local sha256sum and compare exact hashes.
if entries:
    proc=subprocess.run(['sha256sum']+[e['path'] for e in entries], cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0: problems.append('sha256sum rerun failed '+proc.stderr)
    current={line.split(maxsplit=1)[1]:line.split(maxsplit=1)[0] for line in proc.stdout.splitlines() if len(line.split(maxsplit=1))==2}
    for e in entries:
        if current.get(e['path']) != e['sha256']: problems.append('checksum mismatch '+e['path'])
for bad in ['real_codex_execution: YES','real_gemini_execution: YES','approval_applied: YES','promotion_status: PROMOTED','program_alpha_status: READY']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_WITH_HOLD')
print('file_count=16')
print('checksums_verified=YES')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
