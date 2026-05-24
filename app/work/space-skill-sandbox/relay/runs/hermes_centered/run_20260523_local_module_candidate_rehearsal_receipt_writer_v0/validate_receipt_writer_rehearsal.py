#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parent
required = [
    'README.md',
    'module_candidate_contract.md',
    'fixtures/positive_personal_intake_receipt_seed.json',
    'fixtures/negative_fake_promotion_receipt_seed.json',
    'fixtures/negative_authority_language_receipt_seed.json',
    'outputs/RW-POS-001_receipt.md',
    'outputs/RW-NEG-STOP-001_receipt.md',
    'outputs/RW-NEG-HOLD-001_receipt.md',
    'dashboard.json',
    'user_surface_cards/receipt_writer_candidate_status.md',
    'rehearsal_closeout.md',
]
required_tokens = [
    'promotion_status: HOLD',
    'program_alpha_status: NOT_READY',
    'vectorfl_authority_mutation: no',
    'model_execution: no',
    'real_gemini_execution: no',
    'real_codex_execution: no',
    'approval_applied: no',
]
forbidden_phrases = [
    'verdict: M3 confirmed',
    'verdict: M4 reusable internal module confirmed',
    'verdict: Program Alpha ready',
    'verdict: promotion complete',
    'verdict: authority updated',
    'schema mutation complete',
    'registry mutation complete',
    'baseline mutation complete',
]
problems=[]
for rel in required:
    path=ROOT/rel
    if not path.exists():
        problems.append(f'missing file: {rel}')
        continue
    text=path.read_text(encoding='utf-8')
    if path.suffix == '.md':
        for token in required_tokens:
            if token not in text:
                problems.append(f'missing boundary token {token!r} in {rel}')
        for phrase in forbidden_phrases:
            if phrase in text:
                problems.append(f'forbidden phrase {phrase!r} in {rel}')
# Validate fixtures expected recoveries against outputs/dashboard
fixture_expect = {}
for rel in required:
    if rel.startswith('fixtures/'):
        obj=json.loads((ROOT/rel).read_text(encoding='utf-8'))
        fixture_expect[obj['case_id']] = obj['expected_recovery']
expected_outputs = {
    'RW-POS-001':'CANDIDATE_MATERIAL_WITH_HOLD',
    'RW-NEG-STOP-001':'STOP',
    'RW-NEG-HOLD-001':'HOLD_STOP_REVIEW',
}
for cid, expected in expected_outputs.items():
    if fixture_expect.get(cid) != expected:
        problems.append(f'fixture expected recovery mismatch for {cid}')
    out_name = {'RW-POS-001':'RW-POS-001_receipt.md','RW-NEG-STOP-001':'RW-NEG-STOP-001_receipt.md','RW-NEG-HOLD-001':'RW-NEG-HOLD-001_receipt.md'}[cid]
    txt=(ROOT/'outputs'/out_name).read_text(encoding='utf-8')
    if f'recovery_class: {expected}' not in txt and f'classification: {expected}' not in txt:
        problems.append(f'output recovery missing {expected} for {cid}')
dash=json.loads((ROOT/'dashboard.json').read_text(encoding='utf-8'))
if dash.get('summary',{}).get('problem_count') != 0:
    problems.append('dashboard problem_count is not 0')
for k,v in [('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('model_execution','no'),('real_gemini_execution','no'),('real_codex_execution','no'),('approval_applied','no')]:
    if dash.get(k) != v:
        problems.append(f'dashboard boundary {k} expected {v}, got {dash.get(k)!r}')
if problems:
    print('FAIL_RECEIPT_WRITER_MODULE_CANDIDATE_REHEARSAL')
    for p in problems:
        print(p)
    sys.exit(1)
print('PASS_RECEIPT_WRITER_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=3')
print('positive=CANDIDATE_MATERIAL_WITH_HOLD')
print('negative_fake_promotion=STOP')
print('negative_authority_language=HOLD_STOP_REVIEW')
print('authority_mutation=NO')
print('promotion=HOLD')
