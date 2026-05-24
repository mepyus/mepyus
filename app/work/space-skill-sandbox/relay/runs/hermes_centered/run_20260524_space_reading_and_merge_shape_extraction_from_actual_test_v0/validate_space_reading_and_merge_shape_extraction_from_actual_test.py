#!/usr/bin/env python3
from pathlib import Path
import json, sys, re
RUN=Path(__file__).resolve().parent
load=lambda f: json.loads((RUN/f).read_text())
space=load('vectorfl_space_reading_packet_shape_candidate_from_actual_test_v0.json')
merge=load('vectorfl_space_mediated_merge_packet_shape_candidate_from_actual_test_v0.json')
trace=load('space_reading_and_merge_shape_extraction_trace_rows_v0.json')
for f in ['packet_id','classification','source_layer','material_refs','extracted','space_interpretation','guard_status','authority_effect','promotion_status']:
    assert f in space['required_fields'], 'space shape missing required field '+f
    assert f in space['minimal_fixture'], 'space fixture missing '+f
ex=space['minimal_fixture']['extracted']
assert space['minimal_fixture']['source_layer']=='evidence_layer'
assert 'current_position' in space['minimal_fixture']['material_refs']
assert len(space['minimal_fixture']['material_refs'])>=7
assert ex['safe_entry_points_count']>=2
assert ex['guard_status_count']>=5 and ex['guard_layer_count']>=6
assert ex['space_wide_frame_detected'] is True
assert ex['merge_doc_boundary_detected'] is True
assert space['minimal_fixture']['authority_effect']=='NO_AUTHORITY_MUTATION'
assert space['minimal_fixture']['promotion_status']=='HOLD'
for f in ['packet_id','classification','source_layer','inputs','merged_directive','merge_decisions','hold_boundaries','guard_status','authority_effect','promotion_status']:
    assert f in merge['required_fields'], 'merge shape missing required field '+f
    assert f in merge['minimal_fixture'], 'merge fixture missing '+f
inputs=merge['minimal_fixture']['inputs']
assert set(['original_ref','space_reading_ref','model_fixture_ref']).issubset(inputs.keys())
assert len(inputs)==3, 'merge must use original+space+model fixture'
assert 'model fixture remains NO_FIXTURE_ONLY' in merge['minimal_fixture']['merge_decisions']
assert merge['minimal_fixture']['authority_effect']=='NO_AUTHORITY_MUTATION'
assert merge['minimal_fixture']['promotion_status']=='HOLD'
assert len(trace['rows'])==2
for row in trace['rows']:
    assert row['authority_effect']=='NO_AUTHORITY_MUTATION'
    assert row['promotion_status']=='HOLD'
# Ensure negative case inventory preserved from actual test.
for need in ['FAIL_MISSING_CURRENT_POSITION','FAIL_INSUFFICIENT_SPACE_REFS','FAIL_MISSING_ORIGINAL_REF','FAIL_MODEL_ONLY_MERGE','FAIL_AUTHORITY_OR_PROMOTION_DRIFT']:
    assert need in space.get('negative_cases',[])+merge.get('negative_cases',[]), 'missing negative case '+need
# scan data artifacts, excluding validator control script.
pats=[r'urllib\.request\.urlopen',r'requests\.(get|post|put|delete)',r'httpx\.',r'aiohttp',r'fetch\(',r'curl\s',r'127\.0\.0\.1:8879',r'localhost:8879']
hits=[]
for p in RUN.glob('*'):
    if p.suffix in ['.json','.md']:
        txt=p.read_text(errors='ignore')
        for pat in pats:
            if re.search(pat, txt): hits.append((p.name,pat))
assert not hits, 'active call hits '+repr(hits)
print('PASS_SPACE_READING_AND_MERGE_SHAPE_EXTRACTION_FROM_ACTUAL_TEST_WITH_HOLD')
print('shapes=2 trace_rows=2 negative_cases=5')
