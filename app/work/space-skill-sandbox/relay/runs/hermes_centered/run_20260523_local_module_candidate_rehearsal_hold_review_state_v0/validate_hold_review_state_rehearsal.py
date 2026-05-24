#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/positive_candidate_review_seed.json','fixtures/negative_fake_approval_review_seed.json','fixtures/negative_soft_approval_review_seed.json','outputs/HRS-POS-001_review.md','outputs/HRS-NEG-STOP-001_review.md','outputs/HRS-NEG-HOLD-001_review.md','dashboard.json','user_surface_cards/hold_review_state_candidate_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
expect={}
for rel in required:
 if rel.startswith('fixtures/'):
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); expect[o['case_id']]=o['expected_recovery']
outs={'HRS-POS-001':'outputs/HRS-POS-001_review.md','HRS-NEG-STOP-001':'outputs/HRS-NEG-STOP-001_review.md','HRS-NEG-HOLD-001':'outputs/HRS-NEG-HOLD-001_review.md'}
for cid, rel in outs.items():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if expect[cid] not in txt: problems.append(f'expected recovery missing for {cid}')
dash=json.loads((ROOT/'dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_HOLD_REVIEW_STATE_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_HOLD_REVIEW_STATE_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=3')
print('positive=CANDIDATE_MATERIAL_WITH_HOLD')
print('negative_fake_promotion_review=STOP')
print('negative_soft_approval_language=HOLD_STOP_REVIEW')
print('authority_mutation=NO')
print('promotion=HOLD')
