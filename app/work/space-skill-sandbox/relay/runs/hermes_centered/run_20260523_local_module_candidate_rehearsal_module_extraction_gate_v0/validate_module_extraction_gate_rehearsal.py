#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
required=['README.md','module_candidate_contract.md','fixtures/gate_positive_candidate_remains_candidate.json','fixtures/gate_negative_m4_claim.json','fixtures/gate_negative_program_alpha_ready.json','fixtures/gate_negative_soft_reusable_module.json','fixtures/gate_negative_registry_schema_claim.json','gate_reviews/MEG-POS-001_gate_review.md','gate_reviews/MEG-NEG-STOP-001_gate_review.md','gate_reviews/MEG-NEG-STOP-002_gate_review.md','gate_reviews/MEG-NEG-HOLD-001_gate_review.md','gate_reviews/MEG-NEG-STOP-003_gate_review.md','module_extraction_gate_dashboard.json','user_surface_cards/module_extraction_gate_status.md','rehearsal_closeout.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']
problems=[]
for rel in required:
 p=ROOT/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for t in tokens:
   if t not in txt: problems.append(f'missing {t!r} in {rel}')
fixtures={}
for rel in required:
 if rel.startswith('fixtures/'):
  o=json.loads((ROOT/rel).read_text(encoding='utf-8')); fixtures[o['case_id']]=o['expected_recovery']
review_map={'MEG-POS-001':'gate_reviews/MEG-POS-001_gate_review.md','MEG-NEG-STOP-001':'gate_reviews/MEG-NEG-STOP-001_gate_review.md','MEG-NEG-STOP-002':'gate_reviews/MEG-NEG-STOP-002_gate_review.md','MEG-NEG-HOLD-001':'gate_reviews/MEG-NEG-HOLD-001_gate_review.md','MEG-NEG-STOP-003':'gate_reviews/MEG-NEG-STOP-003_gate_review.md'}
for cid, rel in review_map.items():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 if fixtures[cid] not in txt: problems.append(f'{cid} expected {fixtures[cid]} missing')
for rel in review_map.values():
 txt=(ROOT/rel).read_text(encoding='utf-8')
 forbidden=['classification: M4','classification: PROGRAM_ALPHA_READY','promotion_status: COMPLETE','m4_reusable_module: yes','module_promotion: yes','program_alpha_ready: yes']
 for f in forbidden:
  if f in txt: problems.append(f'forbidden {f} in {rel}')
dash=json.loads((ROOT/'module_extraction_gate_dashboard.json').read_text(encoding='utf-8'))
if dash['summary']['problem_count']!=0: problems.append('dashboard problem_count nonzero')
for k,v in [('extraction_decision','HOLD'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no'),('schema_mutation','no'),('snapshot_mutation','no'),('m4_reusable_module','no'),('module_promotion','no'),('program_alpha_ready','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if problems:
 print('FAIL_MODULE_EXTRACTION_GATE_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_MODULE_EXTRACTION_GATE_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=5')
print('positive=ALLOW_AS_CANDIDATE_WITH_HOLD')
print('negative_m4_claim=STOP')
print('negative_program_alpha_ready=STOP')
print('negative_soft_reusable_module=HOLD_STOP_REVIEW')
print('negative_authority_mutation_claim=STOP')
print('m4_reusable_module=NO')
print('module_promotion=NO')
print('program_alpha_ready=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
