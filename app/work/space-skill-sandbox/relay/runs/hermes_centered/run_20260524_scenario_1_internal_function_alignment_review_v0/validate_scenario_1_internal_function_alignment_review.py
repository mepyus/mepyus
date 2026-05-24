#!/usr/bin/env python3
from pathlib import Path
import json, sys
RUN=Path(__file__).resolve().parent
p=RUN/'scenario_1_internal_function_alignment_matrix_v0.json'
if not p.exists():
 print('FAIL missing alignment matrix'); sys.exit(1)
d=json.loads(p.read_text())
assert d['scenario_1_verdict']=='PASS_VECTORFL_SCENARIO_1_SPACE_MEDIATED_PROGRAM_BEHAVIOR_TEST_WITH_HOLD'
assert d['candidate_count']>=12
assert d['coverage']['stages_with_candidate_support']==d['coverage']['stages_total']
for c in d['candidates']:
 assert c['candidate_id'].startswith('M-CAND-')
 assert c['scenario_stages']
 assert c['alignment'].endswith('HOLD') or 'PASS_WITH_HOLD' in c['alignment'] or 'HOLD' in c['alignment']
 assert c['gap'] and c['next_adjustment']
for k,v in d['boundaries'].items():
 if k=='promotion': assert v=='HOLD'
 else: assert v=='NO'
assert 'phase1_deterministic_stable_cycle.py' in json.dumps(d, ensure_ascii=False)
assert 'SCENARIO_1_RECEIPT_AND_INTAKE_FUNCTION_SHAPE_EXTRACTION_NO_AUTHORITY_MUTATION_V0'==d['next_safe_lane']
print('PASS_SCENARIO_1_INTERNAL_FUNCTION_ALIGNMENT_REVIEW_WITH_HOLD')
print('candidates=%d stages=%d weak_or_blocked=%d' % (d['candidate_count'], d['coverage']['stages_total'], d['coverage']['weak_or_blocked_count']))
