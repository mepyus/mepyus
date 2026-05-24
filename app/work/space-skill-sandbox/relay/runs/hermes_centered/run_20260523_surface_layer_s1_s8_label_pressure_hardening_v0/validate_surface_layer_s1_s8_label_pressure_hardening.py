#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
run=ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_layer_s1_s8_label_pressure_hardening_v0'
files=[
'app/work/VECTORFL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_HARDENING_20260523_V0.md',
'app/work/VECTORFL_SURFACE_LABEL_PRESSURE_RULES_20260523_V0.md',
'app/work/VECTORFL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_DASHBOARD_20260523_V0.json',
'app/work/VECTORFL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_USER_STATUS_CARD_20260523_V0.md',
'app/work/VECTORFL_NEXT_WORK_AFTER_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_layer_s1_s8_label_pressure_hardening_v0/fixtures/surface_label_pressure_cases.json'
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
for step in ['S1 Diagnose','S2 Verify','S3 Test','S4 Reflect','S5 Apply','S6 Surface','S7 Receipt','S8 Decide next']:
    if step not in combined: problems.append('missing step '+step)
for token in ['surface_layer','PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT','not approval','not authority','promotion_status: HOLD']:
    if token not in combined: problems.append('missing token '+token)
try:
    fixture=json.loads((run/'fixtures/surface_label_pressure_cases.json').read_text(encoding='utf-8'))
    if fixture.get('layer')!='surface_layer': problems.append('wrong layer')
    cases=fixture.get('cases',[])
    if len(cases)!=5: problems.append('case_count not 5')
    required={'PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT'}
    got={c.get('guard_status') for c in cases}
    if got != required: problems.append('guard statuses mismatch '+repr(got))
    for c in cases:
        label=c.get('expected_surface_label','')
        guard=c.get('guard_status','')
        if guard not in label:
            problems.append('label does not preserve guard '+c.get('case_id','?'))
        if not c.get('forbidden_outputs'):
            problems.append('missing forbidden outputs '+c.get('case_id','?'))
        if c.get('expected_result') in ['ALLOW_WITH_HOLD','ALLOW_WITH_WATCH'] and 'not' not in label.lower():
            problems.append('allow label lacks negative interpretation '+c.get('case_id','?'))
except Exception as e:
    problems.append('fixture json error '+repr(e))
# Ensure exact dangerous softened claims are not emitted as positive claims outside forbidden list context.
positive_bad=['promotion_status: PROMOTED','authority_mutation: YES','program_alpha_ready: YES','real_gemini_execution: YES','live DB intake enabled','READY:','APPROVED:','PROMOTED:']
for bad in positive_bad:
    if bad in combined:
        problems.append('positive contamination '+bad)
if problems:
    print('FAIL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_HARDENING_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_HARDENING_WITH_HOLD')
print('layer=surface_layer')
print('case_count=5')
print('guard_statuses=HOLD_STOP_REVIEW,HOLD_UNTIL_APPROVED_MODEL_OUTPUT,PASS_WITH_HOLD,STOP,WATCH')
print('label_softening_blocked=YES')
print('test_type=local_validator')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
