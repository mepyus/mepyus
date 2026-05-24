#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[7]
files=[
'app/work/VECTORFL_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_20260523_V0.json',
'app/work/VECTORFL_TWELVE_CANDIDATE_USER_STATUS_CARD_20260523_V0.md',
'app/work/VECTORFL_TWELVE_CANDIDATE_HOLD_STOP_COVERAGE_MAP_20260523_V0.md',
'app/work/VECTORFL_TWELVE_CANDIDATE_PERSONAL_PROGRAM_COMPLETE_CHAIN_RECEIPT_20260523_V0.md'
]
problems=[]
for rel in files:
    p=ROOT/rel
    if not p.exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
required=['TWELVE_CANDIDATE_PERSONAL_PROGRAM_CORE_CHAIN_WITH_HOLD','promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','real_gemini_execution','real_codex_execution','live_db_intake','write_ui','m4_reusable_module','module_promotion','program_alpha_ready']
for r in required:
    if r not in text: problems.append('missing '+r)
# dashboard exact checks
dash=json.loads((ROOT/'app/work/VECTORFL_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_20260523_V0.json').read_text(encoding='utf-8'))
for k,v in [('candidate_count',12),('pass_with_hold_count',12),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('authority_mutation','NO'),('real_codex_execution','NO'),('real_gemini_execution','NO'),('live_db_intake','HOLD'),('shared_db_mutation','NO'),('write_ui','NO'),('m4_reusable_module','NO'),('module_promotion','NO'),('program_alpha_ready','NO')]:
    if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch: {dash.get(k)}')
if len(dash.get('candidates',[]))!=12: problems.append('dashboard candidates length not 12')
for c in dash.get('candidates',[]):
    if c.get('classification')!='CANDIDATE_EVIDENCE_WITH_HOLD': problems.append('candidate classification drift '+c.get('id','?'))
# check contaminated positive claims absent outside negative phrase context using exact bad tokens
bad_positive=['status: PROGRAM_ALPHA_READY','promotion_status: PROMOTED','authority_mutation: yes','m4_reusable_module: yes','module_promotion: yes','write_ui: yes','real_codex_execution: yes','real_gemini_execution: yes']
for b in bad_positive:
    if b in text: problems.append('contaminated positive claim '+b)
if problems:
    print('FAIL_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_VALIDATOR_WITH_HOLD')
print('candidate_count=12')
print('pass_with_hold_count=12')
print('dashboard_promotion_contamination=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
print('program_alpha_ready=NO')
