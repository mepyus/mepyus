#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
BASE=Path('/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0')
raw=(BASE/'outputs/gemini_c2c_raw_output.txt').read_text()
m=re.search(r'```json\s*(\{.*?\})\s*```', raw, re.S) or re.search(r'(\{.*\})', raw, re.S)
if not m:
    print('STOP: no JSON object found in Gemini C2C raw')
    raise SystemExit(2)
data=json.loads(m.group(1))
required=['observed_inputs','blocker_status','component_proposal_supporting_evidence','component_proposal_blockers','watch_items','hold_items','recommended_classification_one_of_candidate_locked_candidate_upgrade_review_needed_component_proposal_ready_STOP','do_not_promote','questions_for_codex','completion_signal']
missing=[k for k in required if k not in data]
if missing:
    print('STOP: missing keys '+','.join(missing))
    raise SystemExit(2)
if data.get('completion_signal')!='GEMINI_C2C_LITE_DONE':
    print('STOP: bad completion signal')
    raise SystemExit(2)
(BASE/'outputs/gemini_c2c_lite_output.json').write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
print('verdict: C2C_GEMINI_LITE_MATERIALIZED')
print('classification_recommendation:', data.get('recommended_classification_one_of_candidate_locked_candidate_upgrade_review_needed_component_proposal_ready_STOP'))
print('completion_signal: GEMINI_C2C_LITE_DONE')
