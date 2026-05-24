#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
HANDOFF=ROOT/'app/work/CHATGPT_CODEX_GEMINI_SAME_DAY_FINAL_HANDOFF_UPDATE_20260523_V0.md'
problems=[]
if not HANDOFF.exists(): problems.append('missing handoff')
text=HANDOFF.read_text(encoding='utf-8') if HANDOFF.exists() else ''
for tok in ['self-contained for ChatGPT','TWELVE_CANDIDATE_PERSONAL_PROGRAM_CORE_CHAIN_WITH_MODEL_SAFE_REENTRY_PREPARED_AND_HOLD','M-CAND-01 Input Localization','M-CAND-12 Module Extraction Gate','PASS_CODEX_REVIEW_ONLY_PACKET_PREPARED_WITH_HOLD','PASS_GEMINI_GAP_SCAN_PACKET_TEMPLATE_PREPARED_WITH_HOLD','Raw output is never authority','Lite summary is never approval','Receipt is never promotion','HOLD review is not permission','Re-entry compression is candidate material only']:
    if tok not in text: problems.append('missing token '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
for path in ['VECTORFL_TWELVE_CANDIDATE_PERSONAL_PROGRAM_COMPLETE_CHAIN_RECEIPT_20260523_V0.md','VECTORFL_MODEL_EXECUTION_DECISION_CARD_20260523_V0.md','codex_review_only_twelve_candidate_dashboard_20260523_v0','gemini_gap_scan_twelve_candidate_dashboard_20260523_v0','post_model_run_receipt_pack_20260523_v0']:
    if path not in text: problems.append('missing path ref '+path)
# bad phrases may appear only in does-not-mean section, so require the section and no positive claims.
if 'It does not mean:' not in text: problems.append('missing does-not-mean section')
for bad in ['real_codex_execution: YES','real_gemini_execution: YES','approval_applied: YES','promotion_status: PROMOTED','program_alpha_status: READY']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_SAME_DAY_FINAL_HANDOFF_UPDATE_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_SAME_DAY_FINAL_HANDOFF_UPDATE_WITH_HOLD')
print('chatgpt_self_contained=YES')
print('twelve_candidate_chain_included=YES')
print('codex_packet_prepared_not_executed=YES')
print('gemini_packet_prepared_not_executed=YES')
print('post_model_template_pack_included=YES')
print('real_codex_execution=NO')
print('real_gemini_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
