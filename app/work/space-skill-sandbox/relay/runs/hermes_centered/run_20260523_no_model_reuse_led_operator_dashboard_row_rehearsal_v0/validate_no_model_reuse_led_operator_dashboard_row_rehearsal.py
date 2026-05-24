#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path('/Users/sungsookim/universe/vectorfl_replica')
WORK=ROOT/'app/work'
RUN=WORK/'space-skill-sandbox/relay/runs/hermes_centered/run_20260523_no_model_reuse_led_operator_dashboard_row_rehearsal_v0'
row=json.loads((RUN/'program_spine_phase1_stable_cycle_operator_dashboard_row_v0.json').read_text())
meta=json.loads((WORK/'VECTORFL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_20260523_V0.json').read_text())
problems=[]
required=['row_id','display_label','display_verdict','guard_badge','trace_ref','evidence_receipt_ref','source_receipt_ref','surface_claim','operator_readable_summary','valid_for','not_valid_for','hold_boundaries','forbidden_actions','presentation_guard']
for k in required:
    if k not in row or row[k] in (None,'',[]): problems.append('missing '+k)
if row.get('display_verdict')!='PASS_WITH_HOLD': problems.append('display_verdict drift')
if row.get('guard_badge')!='HOLD': problems.append('guard_badge drift')
for k in ['must_show_hold','must_show_not_valid_for','must_link_trace','must_link_evidence_receipt','must_not_claim_authority','must_not_claim_program_alpha','must_not_hide_watch_or_hold']:
    if row.get('presentation_guard',{}).get(k) is not True: problems.append('presentation_guard missing '+k)
for token in ['Program Alpha','authority mutation','schema registry mutation','baseline/snapshot creation','promotion','live DB intake','model execution evidence']:
    if token not in row.get('not_valid_for',[]): problems.append('not_valid_for missing '+token)
for token in ['promotion_status: HOLD','program_alpha_status: NOT_READY','authority_mutation: NO','schema_registry_mutation: NO','model_execution: NO']:
    if token not in row.get('hold_boundaries',[]): problems.append('hold boundary missing '+token)
for k in ['promotion','authority_mutation','model_execution','schema_registry_mutation','dashboard_registry_mutation','source_surface_mutation','source_trace_mutation']:
    expected='HOLD' if k=='promotion' else 'NO'
    if row.get(k)!=expected: problems.append('row '+k+' drift')
    if meta.get(k)!=expected: problems.append('meta '+k+' drift')
for p in [RUN/'program_spine_phase1_stable_cycle_operator_dashboard_row_v0.md', WORK/'VECTORFL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_20260523_V0.md']:
    if not p.exists(): problems.append('missing '+str(p.relative_to(ROOT)))
combined='\n'.join(p.read_text() for p in [RUN/'program_spine_phase1_stable_cycle_operator_dashboard_row_v0.md', WORK/'VECTORFL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_20260523_V0.md', WORK/'VECTORFL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_USER_STATUS_CARD_20260523_V0.md', WORK/'VECTORFL_NEXT_WORK_AFTER_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_20260523_V0.md'] if p.exists())
for bad in ['promotion_status: PROMOTED','program_alpha_status: READY','authority_mutation: YES','model_execution: YES','dashboard_registry_mutation: YES','automatic enforcement: YES']:
    if bad in combined: problems.append('contamination '+bad)
if problems:
    print('FAIL_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL')
    print('\n'.join(problems))
    sys.exit(1)
print('PASS_NO_MODEL_REUSE_LED_OPERATOR_DASHBOARD_ROW_REHEARSAL_WITH_HOLD')
print('row_id='+row['row_id'])
print('display_verdict='+row['display_verdict'])
print('guard_badge='+row['guard_badge'])
print('dashboard_registry_mutation=NO')
print('authority_mutation=NO')
print('model_execution=NO')
print('promotion=HOLD')
