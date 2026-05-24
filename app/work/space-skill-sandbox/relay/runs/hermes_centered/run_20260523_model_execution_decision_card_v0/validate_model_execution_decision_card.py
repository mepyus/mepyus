#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[7]
files=['app/work/VECTORFL_MODEL_EXECUTION_DECISION_CARD_20260523_V0.md','app/work/VECTORFL_MODEL_EXECUTION_APPROVAL_BOUNDARY_MAP_20260523_V0.json','app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_model_execution_decision_card_v0/user_surface_cards/model_execution_choice_status.md']
problems=[]
for rel in files:
    p=ROOT/rel
    if not p.exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
for tok in ['MODEL_PACKETS_READY_BUT_MODEL_EXECUTION_REMAINS_HOLD','OPTION A','OPTION B','OPTION C','OPTION D','Codex review-only packet 실행 승인','Gemini gap-scan packet 실행 승인','모델 실행 없이 계속']:
    if tok not in text: problems.append('missing decision token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for bad in ['real_codex_execution: yes','real_gemini_execution: yes','approval_applied: yes','promotion_status: PROMOTED','program_alpha_status: READY','module_promotion: yes','m4_reusable_module: yes']:
    if bad in text: problems.append('contamination '+bad)
data=json.loads((ROOT/'app/work/VECTORFL_MODEL_EXECUTION_APPROVAL_BOUNDARY_MAP_20260523_V0.json').read_text(encoding='utf-8'))
opts=data.get('options',{})
if opts.get('A_no_model_continuation',{}).get('allowed_now')!='yes': problems.append('A not allowed now')
for key in ['B_real_codex_review_only','C_real_gemini_gap_scan']:
    if opts.get(key,{}).get('requires_explicit_approval')!='yes': problems.append(key+' approval mismatch')
if opts.get('D_both_model_run',{}).get('recommendation')!='HOLD_NOT_RECOMMENDED_NOW': problems.append('D recommendation mismatch')
if problems:
    print('FAIL_MODEL_EXECUTION_DECISION_CARD_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_MODEL_EXECUTION_DECISION_CARD_VALIDATOR_WITH_HOLD')
print('no_model_continuation=ALLOWED_NOW')
print('real_codex_review_only=REQUIRES_EXPLICIT_APPROVAL')
print('real_gemini_gap_scan=REQUIRES_EXPLICIT_APPROVAL')
print('both_model_run=HOLD_NOT_RECOMMENDED_NOW')
print('approval_applied=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
