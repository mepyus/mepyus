#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
md=ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md'
js=ROOT/'app/work/VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.json'
quick=ROOT/'app/work/VECTORFL_S1_S8_HARDENING_BUNDLE_QUICKSTART_20260523_V0.md'
problems=[]
for p in [md, js, quick]:
    if not p.exists(): problems.append('missing '+str(p))
idx=json.loads(js.read_text(encoding='utf-8'))
text=md.read_text(encoding='utf-8') if md.exists() else ''
if idx.get('bundle_count') != len(idx.get('bundles', [])):
    problems.append('bundle_count mismatch json')
if idx.get('bundle_count') != 10:
    problems.append('bundle_count not 10')
ids=[b.get('bundle_id') for b in idx.get('bundles', [])]
if 'BUNDLE-09-S1-S8-LAYER-HARDENING' not in ids:
    problems.append('missing BUNDLE-09')
if 'BUNDLE-09-S1-S8-LAYER-HARDENING' not in text:
    problems.append('md missing BUNDLE-09')
required_paths={
'app/work/VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0.md',
'app/work/VECTORFL_OPERATOR_RECOVERY_LAYER_S1_S8_HARDENING_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_operator_recovery_s1_s8_loop_hardening_v0/receipt.md',
'app/work/VECTORFL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_HARDENING_20260523_V0.md',
'app/work/VECTORFL_SURFACE_LABEL_PRESSURE_RULES_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_layer_s1_s8_label_pressure_hardening_v0/receipt.md',
'app/work/VECTORFL_REVIEW_GUARD_LAYER_S1_S8_NEGATIVE_CASE_EXPANSION_20260523_V0.md',
'app/work/VECTORFL_REVIEW_GUARD_NEGATIVE_CASE_RULES_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_review_guard_s1_s8_negative_case_expansion_v0/receipt.md'
}
b9=next((b for b in idx.get('bundles', []) if b.get('bundle_id')=='BUNDLE-09-S1-S8-LAYER-HARDENING'), None)
if not b9:
    problems.append('json missing b9')
else:
    got={f.get('path') for f in b9.get('files', [])}
    if got != required_paths:
        problems.append('b9 paths mismatch '+repr(got ^ required_paths))
    for f in b9.get('files', []):
        p=ROOT/f['path']
        if not p.exists() or not f.get('exists'):
            problems.append('b9 missing file '+f['path'])
        else:
            h=hashlib.sha256(p.read_bytes()).hexdigest()
            if h != f.get('sha256'):
                problems.append('hash mismatch '+f['path'])
    if 'not enforcement engine' not in b9.get('boundary_note',''):
        problems.append('b9 boundary lacks not enforcement engine')
for token in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','real_codex_execution: YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET','real_gemini_execution: no','live_db_intake: HOLD','schema_mutation: no','program_alpha_ready: no']:
    if token not in text:
        problems.append('md missing HOLD token '+token)
for bad in ['promotion_status: PROMOTED','authority_mutation: YES','program_alpha_ready: YES','real_gemini_execution: YES','schema_mutation: YES','router_runner_claim: YES','live_db_intake: ENABLED']:
    if bad in text:
        problems.append('contamination '+bad)
if problems:
    print('FAIL_S1_S8_HARDENING_BUNDLE_INDEX_UPDATE_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_S1_S8_HARDENING_BUNDLE_INDEX_UPDATE_WITH_HOLD')
print('bundle_count=10')
print('bundle_09=S1_S8_LAYER_HARDENING_INDEXED')
print('indexed_layers=operator_recovery_layer,surface_layer,review_guard_layer')
print('checksums_verified=YES')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
