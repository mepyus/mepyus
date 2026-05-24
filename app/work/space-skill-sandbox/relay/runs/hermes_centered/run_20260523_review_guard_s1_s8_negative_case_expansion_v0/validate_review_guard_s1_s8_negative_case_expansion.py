#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
run=ROOT/'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_review_guard_s1_s8_negative_case_expansion_v0'
files=[
'app/work/VECTORFL_REVIEW_GUARD_LAYER_S1_S8_NEGATIVE_CASE_EXPANSION_20260523_V0.md',
'app/work/VECTORFL_REVIEW_GUARD_NEGATIVE_CASE_RULES_20260523_V0.md',
'app/work/VECTORFL_REVIEW_GUARD_S1_S8_NEGATIVE_CASE_DASHBOARD_20260523_V0.json',
'app/work/VECTORFL_REVIEW_GUARD_S1_S8_NEGATIVE_CASE_USER_STATUS_CARD_20260523_V0.md',
'app/work/VECTORFL_NEXT_WORK_AFTER_REVIEW_GUARD_S1_S8_NEGATIVE_CASE_20260523_V0.md',
'app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_review_guard_s1_s8_negative_case_expansion_v0/fixtures/review_guard_negative_cases.json'
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
for token in ['review_guard_layer','STOP','HOLD_STOP_REVIEW','HOLD_UNTIL_APPROVED_MODEL_OUTPUT','WATCH','PASS_WITH_HOLD','not enforcement engine','promotion_status: HOLD']:
    if token not in combined: problems.append('missing token '+token)
try:
    fixture=json.loads((run/'fixtures/review_guard_negative_cases.json').read_text(encoding='utf-8'))
    if fixture.get('layer')!='review_guard_layer': problems.append('wrong layer')
    cases=fixture.get('cases',[])
    if len(cases)!=8: problems.append('case_count not 8')
    required_ids={'RG-PROMOTION-001','RG-AUTHORITY-STOP-001','RG-LIVE-DB-STOP-001','RG-MODEL-RESULT-HOLD-001','RG-REAL-TEST-DRIFT-001','RG-SURFACE-SOFTEN-001','RG-SECRET-CONNECTOR-STOP-001','RG-RECEIPT-AUTHORITY-001'}
    got_ids={c.get('case_id') for c in cases}
    if got_ids != required_ids: problems.append('case ids mismatch '+repr(got_ids))
    statuses={c.get('expected_guard_status') for c in cases}
    required_status={'STOP','HOLD_STOP_REVIEW','HOLD_UNTIL_APPROVED_MODEL_OUTPUT','WATCH'}
    if not required_status.issubset(statuses): problems.append('missing required statuses '+repr(statuses))
    for c in cases:
        if not c.get('blocked_claims'): problems.append('missing blocked claims '+c.get('case_id','?'))
        if c.get('expected_guard_status')=='STOP' and 'block' not in c.get('expected_action','').lower() and 'redact/block' not in c.get('expected_action','').lower():
            problems.append('STOP case lacks block action '+c.get('case_id','?'))
except Exception as e:
    problems.append('fixture json error '+repr(e))
positive_bad=['promotion_status: PROMOTED','authority_mutation: YES','program_alpha_ready: YES','real_gemini_execution: YES','live_db_intake: ENABLED','schema_mutation: YES','router_runner_claim: YES']
for bad in positive_bad:
    if bad in combined:
        problems.append('positive contamination '+bad)
if problems:
    print('FAIL_REVIEW_GUARD_S1_S8_NEGATIVE_CASE_EXPANSION_VALIDATOR')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_REVIEW_GUARD_S1_S8_NEGATIVE_CASE_EXPANSION_WITH_HOLD')
print('layer=review_guard_layer')
print('case_count=8')
print('guard_statuses=HOLD_STOP_REVIEW,HOLD_UNTIL_APPROVED_MODEL_OUTPUT,STOP,WATCH')
print('negative_classes=promotion,authority,live_db,model_result,real_test_drift,surface_softening,secret_connector,receipt_authority')
print('test_type=local_validator')
print('real_codex_execution=YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
