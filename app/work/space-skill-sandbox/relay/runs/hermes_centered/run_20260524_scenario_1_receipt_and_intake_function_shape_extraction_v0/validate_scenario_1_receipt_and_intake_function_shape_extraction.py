#!/usr/bin/env python3
from pathlib import Path
import json, sys
RUN=Path(__file__).resolve().parent
req=['vectorfl_original_intake_packet_shape_candidate_v0.json','vectorfl_receipt_writer_shape_candidate_v0.json','fixture_original_intake_packet_v0.json','fixture_receipt_writer_receipt_v0.json','scenario_1_receipt_and_intake_function_shape_trace_rows_v0.json','scenario_1_receipt_and_intake_function_shape_extraction_v0.json']
for f in req:
    if not (RUN/f).exists(): print('FAIL missing '+f); sys.exit(1)
load=lambda f: json.loads((RUN/f).read_text())
intake=load('vectorfl_original_intake_packet_shape_candidate_v0.json')
receipt=load('vectorfl_receipt_writer_shape_candidate_v0.json')
ifx=load('fixture_original_intake_packet_v0.json')
rfx=load('fixture_receipt_writer_receipt_v0.json')
trace=load('scenario_1_receipt_and_intake_function_shape_trace_rows_v0.json')
review=load('scenario_1_receipt_and_intake_function_shape_extraction_v0.json')
for field in ['packet_id','classification','source_layer','raw_user_original','interpreted_constraints','watch_notes','guard_status','authority_effect','promotion_status']:
    assert field in intake['required_fields'], 'intake shape missing '+field
    assert field in ifx, 'intake fixture missing '+field
assert '자! 이제 실행' in ifx['raw_user_original'], 'raw original not preserved'
assert ifx['source_layer']=='input_layer'
for field in ['receipt_id','classification','source_layer','status','validators_run','forbidden_scan','seconds','guard_status','authority_effect','promotion_status']:
    assert field in receipt['required_fields'], 'receipt shape missing '+field
    assert field in rfx, 'receipt fixture missing '+field
for b in receipt['boundary_fields']:
    assert b in rfx, 'receipt fixture missing boundary '+b
assert rfx['status']=='PASS'
assert rfx['forbidden_scan']['active_call_scan_status']=='PASS'
assert rfx['authority_effect']=='NO_AUTHORITY_MUTATION' and rfx['promotion_status']=='HOLD'
assert len(trace['rows'])==2
for row in trace['rows']:
    assert row['authority_effect']=='NO_AUTHORITY_MUTATION'
    assert row['promotion_status']=='HOLD'
for k,v in review['boundaries'].items():
    if k=='promotion': assert v=='HOLD'
    else: assert v=='NO'
print('PASS_SCENARIO_1_RECEIPT_AND_INTAKE_FUNCTION_SHAPE_EXTRACTION_WITH_HOLD')
print('shapes=2 fixtures=2 trace_rows=2')
