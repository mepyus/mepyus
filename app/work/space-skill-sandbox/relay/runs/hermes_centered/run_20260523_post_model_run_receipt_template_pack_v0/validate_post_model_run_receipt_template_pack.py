#!/usr/bin/env python3
from pathlib import Path
import sys
PACK=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/templates/post_model_run_receipt_pack_20260523_v0')
problems=[]
lanes=['codex_review_only','gemini_gap_scan']
templates=['RAW_OUTPUT_TEMPLATE.md','LITE_SUMMARY_TEMPLATE.md','MODEL_RUN_RECEIPT_TEMPLATE.md','HOLD_REVIEW_TEMPLATE.md','REENTRY_COMPRESSION_TEMPLATE.md','USER_SURFACE_CARD_TEMPLATE.md']
for lane in lanes:
    for t in templates:
        p=PACK/lane/t
        if not p.exists(): problems.append('missing '+str(p))
for p in [PACK/'README.md', PACK/'shared/POST_MODEL_RUN_VALIDATION_CHECKLIST.md', PACK/'user_surface_cards/post_model_run_template_pack_status.md']:
    if not p.exists(): problems.append('missing '+str(p))
text='\n'.join(p.read_text(encoding='utf-8') for p in PACK.rglob('*.md'))
for tok in ['Raw output is never authority','Lite summary is never approval','Receipt is never promotion','HOLD review is not permission','Re-entry compression is candidate material only']:
    if tok not in text: problems.append('missing doctrine '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for tok in ['ALLOW_AS_CANDIDATE_WITH_HOLD','HOLD_STOP_REVIEW','STOP','READY_FOR_CONTRACT','CANDIDATE_MATERIAL','WATCH','OUT_OF_SCOPE']:
    if tok not in text: problems.append('missing classification '+tok)
for bad in ['real_codex_execution: yes','real_gemini_execution: yes','promotion_status: PROMOTED','program_alpha_status: READY','vectorfl_authority_mutation: yes']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_POST_MODEL_RUN_RECEIPT_TEMPLATE_PACK_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_POST_MODEL_RUN_RECEIPT_TEMPLATE_PACK_WITH_HOLD')
print('lanes=2')
print('templates_per_lane=6')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
