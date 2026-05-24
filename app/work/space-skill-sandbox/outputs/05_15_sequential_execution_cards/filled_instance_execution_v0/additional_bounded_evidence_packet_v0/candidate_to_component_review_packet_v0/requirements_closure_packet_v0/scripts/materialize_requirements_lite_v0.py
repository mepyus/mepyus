#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0/requirements_closure_packet_v0')
raw=(BASE/'outputs/gemini_requirements_raw_output.txt').read_text()
m=re.search(r'```json\s*(\{.*?\})\s*```', raw, re.S) or re.search(r'(\{.*\})', raw, re.S)
if not m:
 print('STOP: no JSON object found')
 raise SystemExit(2)
data=json.loads(m.group(1))
required=['observed_inputs','permission_inheritance_requirement','raw_audit_trigger_requirement','acceptance_tests','remaining_blockers','watch_items','hold_items','recommended_classification_one_of_requirements_incomplete_requirements_candidate_ready_component_proposal_requirements_ready_STOP','do_not_promote','questions_for_codex','completion_signal']
missing=[k for k in required if k not in data]
if missing:
 print('STOP: missing keys '+','.join(missing)); raise SystemExit(2)
if data.get('completion_signal')!='GEMINI_REQUIREMENTS_LITE_DONE':
 print('STOP: bad completion signal'); raise SystemExit(2)
(BASE/'outputs/gemini_requirements_lite_output.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('verdict: REQUIREMENTS_GEMINI_LITE_MATERIALIZED')
print('classification_recommendation:', data.get('recommended_classification_one_of_requirements_incomplete_requirements_candidate_ready_component_proposal_requirements_ready_STOP'))
print('completion_signal: GEMINI_REQUIREMENTS_LITE_DONE')
