#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
files=['app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.md','app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.json','app/work/VECTORFL_TRACE_LEDGER_EXAMPLE_ROW_CANDIDATES_20260523_V0.md','app/work/VECTORFL_NEXT_WORK_AFTER_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.md','app/work/VECTORFL_TRACE_LEDGER_SCHEMA_USER_STATUS_CARD_20260523_V0.md']
problems=[]
for rel in files:
    if not (ROOT/rel).exists(): problems.append('missing '+rel)
text='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in files if (ROOT/rel).exists())
required=['TRACE_LEDGER_SCHEMA_CANDIDATE_WITH_HOLD','TRACE_LEDGER_EXAMPLE_ROWS_CANDIDATE_WITH_HOLD','NEXT_WORK_AFTER_TRACE_LEDGER_SCHEMA_CANDIDATE_WITH_HOLD','TRACE_LEDGER_SCHEMA_USER_STATUS_CARD_WITH_HOLD','trace_id','source_layer','source_artifact','input_ref','output_ref','receipt_ref','guard_status','surface_label','reentry_ref','authority_effect','promotion_status','watch_notes','VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_FIXTURE_REHEARSAL_20260523_V0.md']
for tok in required:
    if tok not in text: problems.append('missing schema token '+tok)
for layer in ['input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer']:
    if layer not in text: problems.append('missing layer '+layer)
for status in ['PASS_WITH_HOLD','WATCH','HOLD_STOP_REVIEW','STOP','HOLD_UNTIL_APPROVED_MODEL_OUTPUT']:
    if status not in text: problems.append('missing guard status '+status)
for tok in ['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','schema_mutation: no','write_ui: no','m4_reusable_module: no','module_promotion: no','program_alpha_ready: no']:
    if tok not in text: problems.append('missing HOLD token '+tok)
data=json.loads((ROOT/'app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.json').read_text(encoding='utf-8'))
if data.get('field_count') != 14: problems.append('field_count mismatch')
if data.get('layer_count') != 6: problems.append('layer_count mismatch')
for k in ['model_execution','real_codex_execution','real_gemini_execution','authority_mutation','schema_mutation','registry_mutation','baseline_mutation']:
    if data.get(k) != 'NO': problems.append(k+' drift')
if data.get('promotion') != 'HOLD': problems.append('promotion drift')
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','authority_effect: AUTHORITY_MUTATION','model_execution: YES','real_codex_execution: YES','real_gemini_execution: YES','schema_mutation: YES']:
    if bad in text: problems.append('contamination '+bad)
if problems:
    print('FAIL_TRACE_LEDGER_SCHEMA_CANDIDATE_VALIDATOR')
    print('\n'.join(problems)); sys.exit(1)
print('PASS_TRACE_LEDGER_SCHEMA_CANDIDATE_WITH_HOLD')
print('field_count=14')
print('layer_count=6')
print('next_work=trace_ledger_fixture_rehearsal_no_model')
print('model_execution=NO')
print('authority_mutation=NO')
print('promotion=HOLD')
