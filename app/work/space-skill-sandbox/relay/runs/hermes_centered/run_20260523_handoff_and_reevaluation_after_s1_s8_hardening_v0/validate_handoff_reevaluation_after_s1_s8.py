#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=[
'app/work/VECTORFL_HANDOFF_AFTER_S1_S8_HARDENING_20260523_V0.md',
'app/work/VECTORFL_REEVALUATION_AFTER_S1_S8_HARDENING_20260523_V0.md',
'app/work/VECTORFL_CHATGPT_SELF_CONTAINED_HANDOFF_AFTER_S1_S8_HARDENING_20260523_V0.md',
'app/work/VECTORFL_HANDOFF_REEVALUATION_AFTER_S1_S8_DASHBOARD_20260523_V0.json',
'app/work/VECTORFL_NEXT_WORK_AFTER_HANDOFF_REEVALUATION_20260523_V0.md'
]
problems=[]
texts=[]
for rel in files:
    p=ROOT/rel
    if not p.exists():
        problems.append('missing '+rel)
    else:
        texts.append(p.read_text(encoding='utf-8'))
combined='\n'.join(texts)
for token in ['DIRECTION_MATCHES_PROGRAM_UNIT_INTERNAL_STRUCTURE_BUILDUP_WITH_HOLD','S1 Diagnose','S2 Verify','S3 Test','S4 Reflect','S5 Apply','S6 Surface','S7 Receipt','S8 Decide next','evidence_layer receipt-field schema','YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET','real_gemini_execution: no','promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no']:
    if token not in combined:
        problems.append('missing token '+token)
for layer in ['operator_recovery_layer','surface_layer','review_guard_layer','evidence_layer']:
    if layer not in combined:
        problems.append('missing layer '+layer)
try:
    dash=json.loads((ROOT/'app/work/VECTORFL_HANDOFF_REEVALUATION_AFTER_S1_S8_DASHBOARD_20260523_V0.json').read_text(encoding='utf-8'))
    if dash.get('direction_fit')!='YES_WITH_HOLD': problems.append('dashboard direction not YES_WITH_HOLD')
    if dash.get('bundle_count')!=10: problems.append('dashboard bundle_count not 10')
    if dash.get('next_recommended_layer')!='evidence_layer': problems.append('dashboard next layer not evidence')
    if dash.get('authority_mutation')!='NO': problems.append('dashboard authority mutation not NO')
    if dash.get('promotion_status')!='HOLD': problems.append('dashboard promotion not HOLD')
except Exception as e:
    problems.append('dashboard json error '+repr(e))
for bad in ['promotion_status: PROMOTED','authority_mutation: YES','program_alpha_ready: YES','real_gemini_execution: YES','live_db_intake: ENABLED','schema_mutation: YES','router_runner_claim: YES','M4 module confirmed','Program Alpha ready']:
    if bad in combined:
        problems.append('contamination '+bad)
if problems:
    print('FAIL_HANDOFF_REEVALUATION_AFTER_S1_S8_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_HANDOFF_REEVALUATION_AFTER_S1_S8_WITH_HOLD')
print('direction_fit=YES_WITH_HOLD')
print('bundle_count=10')
print('s1_s8_hardening_layers=operator_recovery_layer,surface_layer,review_guard_layer')
print('next_recommended_layer=evidence_layer')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
