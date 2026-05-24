#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[7]
PACKET=ROOT/'app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_gap_scan_twelve_candidate_dashboard_20260523_v0'
required=['PACKET.md','PROMPT.txt','COMMAND_TEMPLATE_NOT_EXECUTED.md','expected_return_shape/RETURN_SHAPE.md','raw_lite_receipt_contract/RAW_LITE_RECEIPT_CONTRACT.md']
problems=[]
for rel in required:
    p=PACKET/rel
    if not p.exists(): problems.append('missing '+rel); continue
    text=p.read_text(encoding='utf-8')
    if rel!='PROMPT.txt':
        for tok in ['real_gemini_execution: NO','approval_applied','HOLD']:
            if tok not in text: problems.append(f'missing {tok} in {rel}')
all_text='\n'.join((PACKET/r).read_text(encoding='utf-8') for r in required if (PACKET/r).exists())
for section in ['verdict:','assets_read:','finding_table:','best_mappings:','missing_guards:','weak_boundaries:','user_surface_suggestions:','candidate_only_material:','STOP:','WATCH:','HOLD:','recommended_next_smallest_action:']:
    if section not in all_text: problems.append('missing return section '+section)
for klass in ['READY_FOR_CONTRACT','CANDIDATE_MATERIAL','WATCH','STOP','OUT_OF_SCOPE']:
    if klass not in all_text: problems.append('missing classification '+klass)
for tok in ['do not edit files','do not patch files','do not mutate repo or Obsidian','do not claim truth/approval/promotion/authority','broad gap scan only']:
    if tok not in all_text: problems.append('missing constraint '+tok)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','live_db_intake: HOLD','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in all_text: problems.append('missing HOLD token '+tok)
for artifact in ['raw/GEMINI_RAW_OUTPUT.md','lite/GEMINI_LITE_SUMMARY.md','receipts/GEMINI_GAP_SCAN_RECEIPT.md']:
    if artifact not in all_text: problems.append('missing raw/lite/receipt artifact '+artifact)
for bad in ['GEMINI_RAW_OUTPUT.md','GEMINI_RESULT.md','gemini_gap_scan_output.md']:
    if (PACKET/bad).exists(): problems.append('unexpected Gemini output exists '+bad)
if 'COMMAND_TEMPLATE_ONLY_NOT_EXECUTED' not in all_text: problems.append('command template not marked not executed')
if problems:
    print('FAIL_GEMINI_GAP_SCAN_PACKET_TEMPLATE_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_GEMINI_GAP_SCAN_PACKET_TEMPLATE_PREPARED_WITH_HOLD')
print('real_gemini_execution=NO')
print('command_template_only=YES')
print('approval_applied=NO')
print('raw_lite_receipt_contract=READY')
print('authority_mutation=NO')
print('promotion=HOLD')
