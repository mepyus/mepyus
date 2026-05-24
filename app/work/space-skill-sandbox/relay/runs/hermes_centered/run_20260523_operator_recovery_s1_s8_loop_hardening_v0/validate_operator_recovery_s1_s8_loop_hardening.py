#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
run=ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_operator_recovery_s1_s8_loop_hardening_v0'
files=[
'app/work/VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0.md',
'app/work/VECTORFL_OPERATOR_RECOVERY_LAYER_S1_S8_HARDENING_20260523_V0.md',
'app/work/VECTORFL_OPERATOR_RECOVERY_S1_S8_HARDENING_DASHBOARD_20260523_V0.json',
'app/work/VECTORFL_OPERATOR_RECOVERY_S1_S8_HARDENING_USER_STATUS_CARD_20260523_V0.md',
'app/work/VECTORFL_NEXT_WORK_AFTER_OPERATOR_RECOVERY_S1_S8_HARDENING_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_operator_recovery_s1_s8_loop_hardening_v0/fixtures/operator_recovery_s1_s8_case.json'
]
problems=[]
texts=[]
for rel in files:
    p=ROOT/rel
    if not p.exists():
        problems.append('missing '+rel)
    else:
        if p.suffix in ['.md','.json']:
            texts.append(p.read_text(encoding='utf-8'))
combined='\n'.join(texts)
for step in ['S1 Diagnose','S2 Verify','S3 Test','S4 Reflect','S5 Apply','S6 Surface','S7 Receipt','S8 Decide next']:
    if step not in combined:
        problems.append('missing step '+step)
for token in ['operator_recovery_layer','PASS_WITH_HOLD','authority_mutation: NO','promotion_status: HOLD','program_alpha_ready: NO']:
    if token not in combined:
        problems.append('missing token '+token)
try:
    fixture=json.loads((run/'fixtures/operator_recovery_s1_s8_case.json').read_text(encoding='utf-8'))
    for key in ['S1_diagnose','S2_verify','S3_test','S4_reflect','S5_apply','S6_surface','S7_receipt','S8_decide_next','HOLD']:
        if key not in fixture: problems.append('fixture missing '+key)
    if fixture.get('layer')!='operator_recovery_layer': problems.append('fixture wrong layer')
    if fixture.get('S3_test',{}).get('test_type')!='local_validator': problems.append('fixture test_type not local_validator')
    if fixture.get('S6_surface',{}).get('guard_status')!='PASS_WITH_HOLD': problems.append('fixture guard not PASS_WITH_HOLD')
except Exception as e:
    problems.append('fixture json error '+repr(e))
# Freshness check: quickstart entry in bundle index still exists/hash-correct
bundle=json.loads((ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.json').read_text(encoding='utf-8'))
b0=next((b for b in bundle['bundles'] if b['bundle_id']=='BUNDLE-00-START-HERE'), None)
q=next((f for f in b0['files'] if f['path']=='app/work/VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md'), None) if b0 else None
if not q or not q.get('exists'):
    problems.append('quickstart freshness regressed')
elif q.get('sha256') != hashlib.sha256((ROOT/q['path']).read_bytes()).hexdigest():
    problems.append('quickstart hash regressed')
for bad in ['promotion_status: PROMOTED','authority_mutation: YES','program_alpha_ready: YES','M4 module confirmation: YES','live DB intake enabled','real_gemini_execution: YES']:
    if bad in combined:
        problems.append('contamination '+bad)
if problems:
    print('FAIL_OPERATOR_RECOVERY_S1_S8_LOOP_HARDENING_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_OPERATOR_RECOVERY_S1_S8_LOOP_HARDENING_WITH_HOLD')
print('layer=operator_recovery_layer')
print('s1_s8_fields=COMPLETE')
print('test_type=local_validator')
print('quickstart_freshness_regression=NO')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
