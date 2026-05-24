#!/usr/bin/env python3
from pathlib import Path
import json, sys
RUN=Path(__file__).resolve().parent
problems=[]
required_dirs=['synthetic_model_outputs','raw','lite','receipts','reentry','guard_reviews','user_surface_cards']
for d in required_dirs:
    if not (RUN/d).is_dir(): problems.append('missing dir '+d)
case_ids=['COD-POS-001','COD-NEG-001','GEM-POS-001','GEM-NEG-001','MIX-NEG-001']
for cid in case_ids:
    for sub,suffix in [('synthetic_model_outputs','.md'),('raw','_RAW.md'),('lite','_LITE.md'),('receipts','_RECEIPT.md'),('reentry','_REENTRY.md'),('guard_reviews','_GUARD.md')]:
        name=cid+suffix if sub!='synthetic_model_outputs' else cid+'.md'
        if not (RUN/sub/name).exists(): problems.append('missing '+sub+'/'+name)
text='\n'.join(p.read_text(encoding='utf-8') for p in RUN.rglob('*.md'))
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for tok in ['STOP_CODEX_PROMOTION_OR_PATCH_CLAIM','STOP_GEMINI_TRUTH_OR_MUTATION_CLAIM','STOP_ROLE_BLUR_AND_RECEIPT_BYPASS','CANDIDATE_MATERIAL_WITH_HOLD']:
    if tok not in text: problems.append('missing classification '+tok)
data=json.loads((RUN/'model_result_intake_reentry_dashboard.json').read_text(encoding='utf-8'))
if data.get('real_codex_execution')!='NO': problems.append('real_codex_execution drift')
if data.get('real_gemini_execution')!='NO': problems.append('real_gemini_execution drift')
if data.get('case_count')!=5: problems.append('case count mismatch')
classes={c['classification'] for c in data.get('cases',[])}
for required in ['STOP_CODEX_PROMOTION_OR_PATCH_CLAIM','STOP_GEMINI_TRUTH_OR_MUTATION_CLAIM','STOP_ROLE_BLUR_AND_RECEIPT_BYPASS','CANDIDATE_MATERIAL_WITH_HOLD']:
    if required not in classes: problems.append('dashboard missing '+required)
if problems:
    print('FAIL_MODEL_RESULT_INTAKE_REENTRY_DRY_RUN_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_MODEL_RESULT_INTAKE_REENTRY_DRY_RUN_WITH_HOLD')
print('cases_checked=5')
print('real_codex_execution=NO')
print('real_gemini_execution=NO')
print('synthetic_model_outputs=YES')
print('raw_lite_receipt_reentry_contract=PASS')
print('authority_mutation=NO')
print('promotion=HOLD')
