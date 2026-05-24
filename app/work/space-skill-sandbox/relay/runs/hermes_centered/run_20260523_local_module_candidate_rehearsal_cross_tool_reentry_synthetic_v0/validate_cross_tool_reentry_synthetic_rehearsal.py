#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
cases=['XTR-POS-001','XTR-POS-002','XTR-NEG-STOP-001','XTR-NEG-STOP-002','XTR-NEG-HOLD-001']
required=['README.md','module_candidate_contract.md','cross_tool_reentry_dashboard.json','user_surface_cards/cross_tool_reentry_status.md','rehearsal_closeout.md']
for cid in cases:
 required += [f'fixtures/{cid}_fixture.json',f'raw/{cid}_raw.md',f'lite/{cid}_lite.md',f'receipts/{cid}_receipt.md',f'reentry/{cid}_compressed_reentry.md',f'guard_reviews/{cid}_guard_review.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','synthetic_tool_output: yes','approval_applied: no','hidden_transport: no','authority_inheritance: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
expect={}
for cid in cases:
 o=json.loads((ROOT/f'fixtures/{cid}_fixture.json').read_text(encoding='utf-8'))
 expect[cid]=o['expected_recovery']
 for lane in ['raw','lite','receipts','reentry','guard_reviews']:
  rel={'raw':f'raw/{cid}_raw.md','lite':f'lite/{cid}_lite.md','receipts':f'receipts/{cid}_receipt.md','reentry':f'reentry/{cid}_compressed_reentry.md','guard_reviews':f'guard_reviews/{cid}_guard_review.md'}[lane]
  txt=(ROOT/rel).read_text(encoding='utf-8')
  if lane != 'raw' and expect[cid] not in txt: problems.append(f'{cid} expected {expect[cid]} missing in {rel}')
for cid in ['XTR-NEG-STOP-001','XTR-NEG-STOP-002']:
 if 'classification: STOP' not in (ROOT/f'reentry/{cid}_compressed_reentry.md').read_text(encoding='utf-8'):
  problems.append(f'{cid} reentry not STOP')
if 'classification: HOLD_STOP_REVIEW' not in (ROOT/'reentry/XTR-NEG-HOLD-001_compressed_reentry.md').read_text(encoding='utf-8'):
 problems.append('role blur reentry not HOLD_STOP_REVIEW')
dash=json.loads((ROOT/'cross_tool_reentry_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('real_codex_execution','no'),('real_gemini_execution','no'),('synthetic_tool_output','yes'),('model_execution','no'),('hidden_transport','no'),('authority_inheritance','no'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('approval_applied','no'),('m4_reusable_module','no'),('module_promotion','no'),('program_alpha_ready','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_CROSS_TOOL_REENTRY_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_CROSS_TOOL_REENTRY_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=5')
print('positive_gemini_like_raw_lite_receipt=CANDIDATE_MATERIAL_WITH_HOLD')
print('positive_codex_like_review_reentry=CANDIDATE_MATERIAL_WITH_HOLD')
print('negative_hidden_transport=STOP')
print('negative_authority_inheritance=STOP')
print('negative_role_blur=HOLD_STOP_REVIEW')
print('real_gemini_execution=NO')
print('real_codex_execution=NO')
print('synthetic_tool_output=YES')
print('authority_mutation=NO')
print('promotion=HOLD')
