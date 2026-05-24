#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
RUN=Path(__file__).resolve().parent
required=[
'scenario_1_space_asset_index_v0.json','scenario_1_original_input_v0.json','scenario_1_space_reading_packet_v0.json','scenario_1_model_result_fixture_packet_v0.json','scenario_1_space_mediated_merge_packet_v0.json','scenario_1_subject_routing_packet_v0.json','scenario_1_hermes_execution_packet_v0.json','scenario_1_hermes_execution_receipt_v0.json','scenario_1_codex_reinsertion_packet_v0.json','scenario_1_gemini_exploration_need_assessment_v0.json','scenario_1_space_effect_observation_v0.json','scenario_1_final_operator_output_v0.json','scenario_1_trace_ledger_rows_v0.json']
missing=[f for f in required if not (RUN/f).exists()]
if missing:
    print('FAIL missing '+str(missing)); sys.exit(1)
load=lambda f: json.loads((RUN/f).read_text())
asset=load('scenario_1_space_asset_index_v0.json')
orig=load('scenario_1_original_input_v0.json')
space=load('scenario_1_space_reading_packet_v0.json')
model=load('scenario_1_model_result_fixture_packet_v0.json')
merge=load('scenario_1_space_mediated_merge_packet_v0.json')
routing=load('scenario_1_subject_routing_packet_v0.json')
hermes=load('scenario_1_hermes_execution_receipt_v0.json')
codex=load('scenario_1_codex_reinsertion_packet_v0.json')
gem=load('scenario_1_gemini_exploration_need_assessment_v0.json')
effect=load('scenario_1_space_effect_observation_v0.json')
final=load('scenario_1_final_operator_output_v0.json')
trace=load('scenario_1_trace_ledger_rows_v0.json')
assert len([a for a in asset['assets'] if a.get('exists')]) >= 10, 'not enough existing asset refs'
assert '너의 모델만 사용하지 말고' in orig['raw_user_original'], 'original not preserved'
assert len(space.get('bundle_coverage',[])) >= 6, 'bundle coverage weak'
assert 'space reading' in ' '.join(space['findings']).lower() or 'space' in space['space_interpretation_for_current_user_request'].lower(), 'space reading missing'
assert set(model['capture_contract']) == {'raw','lite','receipt','guard_review','reentry_compression'}, 'model capture contract wrong'
assert model['model_execution'].startswith('NO'), 'model fixture claims real execution'
for k in ['original_ref','space_reading_ref','model_fixture_ref']:
    assert k in merge['inputs'], 'merge missing '+k
for role in ['Hermes','Codex','Gemini','User']:
    assert role in routing['roles'], 'routing missing '+role
assert hermes['status']=='PASS', 'hermes receipt not pass'
assert hermes['forbidden_scan']['active_call_scan_status']=='PASS', 'active call scan failed'
assert codex['authority_effect']=='NO_AUTHORITY_MUTATION' and 'Re-insert' in codex['codex_role'], 'codex reinsertion missing'
assert gem['real_gemini_execution']=='NO', 'gemini executed'
assert effect['current_position_apply']=='NO', 'current position apply happened'
assert final['answers_user_request']=='YES', 'final output does not answer user'
allowed_layers={'input_layer','evidence_layer','review_guard_layer','surface_layer','tool_reentry_layer','operator_recovery_layer'}
assert trace['row_count'] >= 6, 'trace rows missing'
for r in trace['rows']:
    assert r['source_layer'] in allowed_layers, 'bad layer'
    assert r['authority_effect']=='NO_AUTHORITY_MUTATION', 'authority drift'
    assert r['promotion_status']=='HOLD', 'promotion drift'
for obj in [asset, orig, space, model, merge, routing, hermes, codex, gem, effect, final, trace]:
    txt=json.dumps(obj, ensure_ascii=False)
    assert 'PROGRAM_ALPHA_READY' not in txt and 'AUTHORITY_ACCEPTED' not in txt, 'readiness/authority drift'
print('PASS_VECTORFL_SCENARIO_1_SPACE_MEDIATED_PROGRAM_BEHAVIOR_TEST_WITH_HOLD')
print('assets_existing=%d trace_rows=%d validators_run=%d seconds=%s' % (len([a for a in asset['assets'] if a.get('exists')]), trace['row_count'], len(hermes['validators_run']), hermes['seconds']))
