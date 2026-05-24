#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
cases=['GGL-POS-001','GGL-POS-002','GGL-NEG-STOP-001','GGL-NEG-STOP-002','GGL-NEG-HOLD-001']
required=['README.md','module_candidate_contract.md','gemini_gap_scan_lens_dashboard.json','user_surface_cards/gemini_gap_scan_lens_status.md','rehearsal_closeout.md']
for cid in cases:
 required += [f'fixtures/{cid}_fixture.json',f'synthetic_gemini_raw/{cid}_raw.md',f'lite/{cid}_lite.md',f'gap_findings/{cid}_finding.md',f'receipts/{cid}_receipt.md',f'guard_reviews/{cid}_guard_review.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','synthetic_gemini_output: yes','approval_applied: no','implementation_truth: no','repo_mutation: no','confidence_overreach: no']
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
 expect[cid]=o['expected_guard']
 for lane in ['lite','gap_findings','receipts','guard_reviews']:
  rel={'lite':f'lite/{cid}_lite.md','gap_findings':f'gap_findings/{cid}_finding.md','receipts':f'receipts/{cid}_receipt.md','guard_reviews':f'guard_reviews/{cid}_guard_review.md'}[lane]
  if expect[cid] not in (ROOT/rel).read_text(encoding='utf-8'):
   problems.append(f'{cid} expected {expect[cid]} missing in {rel}')
for cid in ['GGL-NEG-STOP-001','GGL-NEG-STOP-002']:
 if 'classification: STOP' not in (ROOT/f'guard_reviews/{cid}_guard_review.md').read_text(encoding='utf-8'):
  problems.append(f'{cid} guard not STOP')
if 'classification: HOLD_STOP_REVIEW' not in (ROOT/'guard_reviews/GGL-NEG-HOLD-001_guard_review.md').read_text(encoding='utf-8'):
 problems.append('confidence overreach not HOLD_STOP_REVIEW')
dash=json.loads((ROOT/'gemini_gap_scan_lens_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('real_gemini_execution','no'),('real_codex_execution','no'),('synthetic_gemini_output','yes'),('model_execution','no'),('implementation_truth','no'),('repo_mutation','no'),('confidence_overreach','no'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('approval_applied','no'),('m4_reusable_module','no'),('module_promotion','no'),('program_alpha_ready','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_GEMINI_GAP_SCAN_LENS_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_GEMINI_GAP_SCAN_LENS_SYNTHETIC_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=5')
print('positive_candidate_gap=CANDIDATE_MATERIAL')
print('positive_uncertain_coupling=WATCH')
print('negative_gemini_truth_claim=STOP')
print('negative_repo_mutation_claim=STOP')
print('negative_confidence_overreach=HOLD_STOP_REVIEW')
print('real_gemini_execution=NO')
print('synthetic_gemini_output=YES')
print('authority_mutation=NO')
print('promotion=HOLD')
