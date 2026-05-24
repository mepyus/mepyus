#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_evidence_layer_field_fill_rehearsal_v0'
schema=json.loads((WORK/'VECTORFL_EVIDENCE_LAYER_RECEIPT_FIELD_SCHEMA_20260523_V0.json').read_text())
filled=json.loads((RUN/'phase1_deterministic_stable_cycle_evidence_layer_receipt_filled_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_20260523_V0.json').read_text())
problems=[]
for p in [WORK/'VECTORFL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p))
for field in schema.get('required_fields',[]):
    if field not in filled or filled[field] in (None,'',[]): problems.append('missing required field '+field)
if filled.get('guard_status')!='PASS_WITH_HOLD': problems.append('guard_status not PASS_WITH_HOLD')
if filled.get('classification')!='RUNTIME_EVIDENCE_CANDIDATE_WITH_HOLD': problems.append('classification drift')
for token in ['Program Alpha','authority mutation','schema registry mutation','baseline/snapshot creation','promotion','live DB intake','model execution evidence']:
    if token not in filled.get('not_valid_for',[]): problems.append('not_valid_for missing '+token)
for token in ['promotion_status: HOLD','program_alpha_status: NOT_READY','authority_mutation: NO','schema_registry_mutation: NO','model_execution: NO']:
    if token not in filled.get('hold_boundaries',[]): problems.append('hold boundary missing '+token)
for token in ['treat as Program Alpha evidence','promote module/component/M3/M4','mutate authority','create schema registry','execute model lane from this receipt']:
    if token not in filled.get('forbidden_actions',[]): problems.append('forbidden missing '+token)
if meta.get('promotion')!='HOLD': problems.append('promotion drift')
for k in ['authority_mutation','model_execution','schema_registry_mutation','original_receipt_mutation','shared_db_mutation']:
    if meta.get(k)!='NO': problems.append(k+' drift')
if meta.get('all_required_fields_present') is not True: problems.append('required field completeness false')
combined='\\n'.join(p.read_text() for p in [WORK/'VECTORFL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_20260523_V0.md'] if p.exists())
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','schema_registry_mutation: YES','authority_mutation: YES','model_execution: YES']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL')
    print('\\n'.join(problems))
    sys.exit(1)
print('PASS_NO_MODEL_EVIDENCE_LAYER_FIELD_FILL_REHEARSAL_WITH_HOLD')
print('required_field_count='+str(len(schema.get('required_fields',[]))))
print('guard_status='+filled.get('guard_status'))
print('source_receipt='+filled.get('source_contact'))
print('promotion=HOLD')
print('authority_mutation=NO')
print('model_execution=NO')
print('schema_registry_mutation=NO')
