#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[7]
PACKET=ROOT/'app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_twelve_candidate_dashboard_20260523_v0'
required=['PACKET.md','PROMPT.txt','COMMAND_TEMPLATE_NOT_EXECUTED.md','expected_return_shape/RETURN_SHAPE.md']
problems=[]
for rel in required:
    p=PACKET/rel
    if not p.exists(): problems.append('missing '+rel); continue
    text=p.read_text(encoding='utf-8')
    for tok in ['real_codex_execution: NO','approval_applied','HOLD']:
        if tok not in text and rel!='PROMPT.txt': problems.append(f'missing {tok} in {rel}')
all_text='\n'.join((PACKET/r).read_text(encoding='utf-8') for r in required if (PACKET/r).exists())
for section in ['verdict:','read_before_work:','files_touched:','commands_run:','receipts_created_or_updated:','state_mutations_observed:','WATCH:','HOLD:','overclaim_findings:','missing_evidence:','next_smallest_action:']:
    if section not in all_text: problems.append('missing return section '+section)
for tok in ['do not edit files','do not patch files','read-only review only','do not claim approval/promotion/authority']:
    if tok not in all_text: problems.append('missing constraint '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_codex_execution: no','real_gemini_execution: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in all_text: problems.append('missing HOLD token '+tok)
# Assert there is no run output file that would imply actual Codex execution.
for bad in ['RAW_CODEX_OUTPUT.md','codex_review_output.md','CODEX_RESULT.md']:
    if (PACKET/bad).exists(): problems.append('unexpected Codex output exists '+bad)
if 'COMMAND_TEMPLATE_ONLY_NOT_EXECUTED' not in all_text: problems.append('command template not marked not executed')
if problems:
    print('FAIL_CODEX_REVIEW_ONLY_PACKET_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_CODEX_REVIEW_ONLY_PACKET_PREPARED_WITH_HOLD')
print('real_codex_execution=NO')
print('command_template_only=YES')
print('approval_applied=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
