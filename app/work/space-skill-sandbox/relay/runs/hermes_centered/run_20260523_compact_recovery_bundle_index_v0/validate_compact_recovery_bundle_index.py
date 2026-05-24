#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md','app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.json','app/work/VECTORFL_REUSE_LOOKUP_SPEC_20260523_V0.md','app/work/VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md','app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_USER_STATUS_CARD_20260523_V0.md','app/work/VECTORFL_NEXT_WORK_AFTER_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
data=json.loads((ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.json').read_text(encoding='utf-8'))
if data.get('bundle_count') != 8: problems.append('bundle_count mismatch')
for b in data.get('bundles',[]):
    if b.get('status')!='BUNDLE_INDEXED_WITH_HOLD': problems.append('bundle status drift '+b.get('bundle_id','?'))
    if not b.get('files'): problems.append('empty bundle '+b.get('bundle_id','?'))
    for f in b.get('files',[]):
        p=ROOT/f['path']
        if not p.exists(): problems.append('missing indexed file '+f['path'])
        else:
            h=hashlib.sha256(p.read_bytes()).hexdigest()
            if f.get('sha256') and f.get('sha256')!=h: problems.append('checksum mismatch '+f['path'])
for tok in ['COMPACT_RECOVERY_BUNDLE_INDEX_WITH_HOLD','REUSE_LOOKUP_SPEC_WITH_HOLD','COMPACT_RECOVERY_QUICKSTART_WITH_HOLD','COMPACT_RECOVERY_BUNDLE_USER_STATUS_CARD_WITH_HOLD','NEXT_WORK_AFTER_COMPACT_RECOVERY_BUNDLE_INDEX_WITH_HOLD','DIRECTION_MATCHES_PROGRAM_UNIT_INTERNAL_STRUCTURE_BUILDUP_WITH_HOLD']:
    if tok not in text: problems.append('missing token '+tok)
for bid in ['BUNDLE-00-START-HERE','BUNDLE-01-DIRECTION','BUNDLE-02-STRUCTURE-SPEC','BUNDLE-03-CANDIDATE-CHAIN','BUNDLE-04-TRACE','BUNDLE-05-GUARD','BUNDLE-06-MODEL-REENTRY','BUNDLE-07-OPERATOR-RECOVERY']:
    if bid not in text and bid not in json.dumps(data): problems.append('missing bundle '+bid)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','shared_db_mutation']:
    if data.get(k)!='NO': problems.append(k+' drift')
if data.get('promotion')!='HOLD': problems.append('promotion drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES','authority_mutation: YES','approval_applied: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_COMPACT_RECOVERY_BUNDLE_INDEX_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_COMPACT_RECOVERY_BUNDLE_INDEX_WITH_HOLD')
print('bundle_count=8')
print('checksums_verified=YES')
print('direction_fit=YES_WITH_HOLD')
print('next_default=stop_or_select_one_layer_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
