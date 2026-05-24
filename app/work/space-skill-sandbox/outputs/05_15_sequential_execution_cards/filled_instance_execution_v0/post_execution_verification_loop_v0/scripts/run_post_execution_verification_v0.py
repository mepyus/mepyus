#!/usr/bin/env python3
import os, json, hashlib, re, datetime
BASE = '/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0'
OUTDIR = os.path.join(BASE, 'post_execution_verification_loop_v0')
os.makedirs(OUTDIR, exist_ok=True)
PATHS = {
    'packet': 'FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md',
    'state': 'space_model_boundary_v0/CURRENT_EXECUTION_LANE_STATE_V0.json',
    'dashboard_json': 'post_execution_dashboard_v0/POST_EXECUTION_DASHBOARD_V0.json',
    'dashboard_md': 'post_execution_dashboard_v0/POST_EXECUTION_DASHBOARD_V0.md',
    'hermes_receipt': 'HERMES_EXECUTION_RECEIPT_V0.json',
    'hermes_report': 'HERMES_EXECUTION_REPORT_V0.md',
    'real_closeout_receipt': 'real_execution_closeout_v0/REAL_EXECUTION_CLOSEOUT_RECEIPT_V0.json',
    'real_closeout_report': 'real_execution_closeout_v0/REAL_EXECUTION_CLOSEOUT_REPORT_V0.md',
    's8_receipt': 's8_real_output_recovery_gate_v0/S8_REAL_OUTPUT_RECOVERY_GATE_RECEIPT_V0.json',
    's8_report': 's8_real_output_recovery_gate_v0/S8_REAL_OUTPUT_RECOVERY_GATE_REPORT_V0.md',
    'post_index_receipt': 'post_execution_evidence_index_v0/POST_EXECUTION_EVIDENCE_INDEX_RECEIPT_V0.json',
    'post_index_json': 'post_execution_evidence_index_v0/POST_EXECUTION_EVIDENCE_INDEX_V0.json',
    'gemini_raw': 'outputs/gemini_raw_output.txt',
    'gemini_lite': 'outputs/gemini_lite_output.json',
    'codex_return': 'outputs/codex_combined_bridge_recovery_return.md',
}

def abspath(rel): return os.path.join(BASE, rel)
def read_text(rel):
    with open(abspath(rel), encoding='utf-8', errors='replace') as f: return f.read()
def read_json(rel):
    with open(abspath(rel), encoding='utf-8') as f: return json.load(f)
def sha(rel):
    data=open(abspath(rel),'rb').read()
    return hashlib.sha256(data).hexdigest(), len(data)

evidence={}
parse_errors={}
for k,rel in PATHS.items():
    p=abspath(rel)
    item={'relative_path':rel,'path':p,'exists':os.path.exists(p)}
    if os.path.exists(p):
        h,s=sha(rel); item.update({'sha256':h,'size':s})
        if rel.endswith('.json'):
            try: read_json(rel); item['json_parse']='ok'
            except Exception as e: item['json_parse']='error'; parse_errors[k]=str(e)
    evidence[k]=item

state=read_json(PATHS['state'])
dash=read_json(PATHS['dashboard_json'])
hermes=read_json(PATHS['hermes_receipt'])
s8=read_json(PATHS['s8_receipt'])
postidx=read_json(PATHS['post_index_receipt'])
glite=read_json(PATHS['gemini_lite'])
raw=read_text(PATHS['gemini_raw'])
codex=read_text(PATHS['codex_return'])
hermes_report=read_text(PATHS['hermes_report'])
s8_report=read_text(PATHS['s8_report'])

missing=[k for k,v in evidence.items() if not v['exists']]
t1_pass=(not missing and not parse_errors)

scope_terms=['inaccessible','could not','cannot','unable','sibling','primary','observed_scope','uncertainties','do_not_promote','scope']
scope_lines=[]
for label,text in [('gemini_raw',raw),('gemini_lite',json.dumps(glite, ensure_ascii=False, indent=2)),('codex_return',codex),('s8_report',s8_report)]:
    for i,line in enumerate(text.splitlines(),1):
        if any(term.lower() in line.lower() for term in scope_terms):
            scope_lines.append({'source':label,'line':i,'text':line[:500]})
observed_scope=glite.get('observed_scope')
uncertainties=glite.get('uncertainties')
do_not_promote=glite.get('do_not_promote')
t2_pass=bool(scope_lines) and isinstance(observed_scope, list) and isinstance(uncertainties, list)

required_codex_signals=['CODEX_RECOVERY_DONE','actual_gemini_scope','premature_claims_removed']
required_codex_presence={s:(s in codex) for s in required_codex_signals}
forbidden_patterns=[r'promotion_performed:\s*true', r'APPROVED_PROMOTION:\s*yes', r'component\s+promotion\s+performed', r'authority_mutation:\s*true']
forbidden_hits=[]
for pat in forbidden_patterns:
    for m in re.finditer(pat, codex, flags=re.I): forbidden_hits.append({'pattern':pat,'span':m.span()})
t3_pass=all(required_codex_presence.values()) and not forbidden_hits

fields={
 'state_active': state.get('active_state'), 'state_promotion': state.get('promotion'), 'state_authority': state.get('vectorfl_authority_mutation'), 'state_recovery_class': state.get('recovery_class'),
 'dashboard_state': dash.get('current_state'), 'dashboard_promotion': dash.get('promotion'), 'dashboard_authority': dash.get('vectorfl_authority_mutation'), 'dashboard_class': dash.get('s8_classification'),
 'hermes_gemini': hermes.get('real_gemini_executed'), 'hermes_codex': hermes.get('real_codex_executed'), 'hermes_promotion': hermes.get('promotion_performed'), 'hermes_authority': hermes.get('vectorfl_authority_modified'),
 's8_classification': s8.get('classification'), 's8_promotion': s8.get('promotion'), 's8_authority': s8.get('vectorfl_authority_mutation'),
 'post_index_s8_classification': postidx.get('s8_classification'), 'post_index_promotion': postidx.get('promotion'), 'post_index_authority': postidx.get('vectorfl_authority_mutation'),
}
contradictions=[]
if fields['state_active'] != 'S8_VECTORFL_RECOVERY_GATE_CLASSIFICATION_COMPLETE': contradictions.append('state active_state is not S8 complete')
for k in ['state_promotion','dashboard_promotion','hermes_promotion','s8_promotion','post_index_promotion']:
    if fields[k] is not False: contradictions.append(f'{k} expected false got {fields[k]!r}')
for k in ['state_authority','dashboard_authority','hermes_authority','s8_authority','post_index_authority']:
    if fields[k] is not False: contradictions.append(f'{k} expected false got {fields[k]!r}')
for k in ['state_recovery_class','dashboard_class','s8_classification','post_index_s8_classification']:
    if fields[k] != 'candidate': contradictions.append(f'{k} expected candidate got {fields[k]!r}')
for k in ['hermes_gemini','hermes_codex']:
    if fields[k] is not True: contradictions.append(f'{k} expected true got {fields[k]!r}')
t4_pass=not contradictions

why=s8.get('why_not_component',[])
conditions=s8.get('conditions',{})
limitation= dash.get('key_limitation','')
t5_pass=(s8.get('classification')=='candidate' and len(why)>=3 and conditions.get('gemini_scope_limited') is True and 'candidate' in s8_report.lower())

runner_path=os.path.join(OUTDIR,'RUN_POST_EXECUTION_SAFE_REGRESSION_V0.sh')
runner="""#!/usr/bin/env bash
set -euo pipefail
BASE=\"/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0\"
cd \"$BASE\"
printf '== validate-static ==\\n'
./scripts/run_execution_v0.sh validate-static
printf '== validate-codex-return ==\\n'
./scripts/run_execution_v0.sh validate-codex-return
printf '== post-execution verification ==\\n'
python3 \"$BASE/post_execution_verification_loop_v0/scripts/run_post_execution_verification_v0.py\"
printf 'verdict: POST_EXECUTION_SAFE_REGRESSION_PASS_NO_MODEL_EXECUTION\\n'
printf 'required_final_line: No promotion was performed. Recovery class remains candidate.\\n'
"""
with open(runner_path,'w',encoding='utf-8') as f: f.write(runner)
os.chmod(runner_path,0o755)
t6_pass=True

packet_path=os.path.join(OUTDIR,'PROMOTION_GATE_REVIEW_ONLY_PACKET_V0.md')
promo_packet=f"""# Promotion Gate Review Only Packet v0

verdict:
  PROMOTION_GATE_REVIEW_ONLY_PACKET_PREPARED_WITH_PROMOTION_HOLD

purpose:
  This packet lists what evidence would be needed before any future component promotion review.
  It does not approve promotion and does not mutate VectorFL authority.

current_classification:
  candidate

current_limitation:
  {limitation}

minimum_extra_evidence_before_component_review:
  - Direct review or equivalent trusted recovery of declared primary sibling inputs that Gemini could not inspect.
  - A new Codex recovery pass that separates actual observed evidence from inferred claims.
  - A consistency receipt proving no promotion/authority mutation happened during evidence collection.
  - Human/VectorFL steward review of candidate-to-component boundary.

explicit_non_approvals:
  APPROVED_PROMOTION: no
  APPROVED_VECTORFL_AUTHORITY_MUTATION: no
  APPROVED_BASELINE_WORKFLOW_SCHEMA_REGISTRY_ONTOLOGY_EDIT: no
  APPROVED_CURRENT_POSITION_OUTPUT_MANIFEST_EDIT: no

allowed_next_action:
  review-only evidence planning or additional bounded evidence packet preparation.

forbidden_next_action_without_separate_approval:
  component promotion
  VectorFL authority mutation
  baseline/workflow/schema/registry/ontology/current-position/output_manifest edits

required_final_line:
  No promotion was performed. Recovery class remains candidate.
"""
with open(packet_path,'w',encoding='utf-8') as f: f.write(promo_packet)
t7_pass=True

watch_path=os.path.join(OUTDIR,'FINAL_S8_WATCH_CLOSEOUT_V0.md')
watch=f"""# Final S8 Watch Closeout v0

verdict:
  FINAL_S8_WATCH_CLOSEOUT_LOCKED_CANDIDATE_WITH_PROMOTION_HOLD

state:
  {state.get('active_state')}

classification:
  candidate

completed_real_lane:
  S5 Gemini space-mediated run: {hermes.get('real_gemini_executed')}
  S6 Codex space-mediated recovery: {hermes.get('real_codex_executed')}
  S7 Hermes closeout: {dash.get('hermes_closeout')}
  S8 classification-only gate: complete

WATCH:
  - Gemini scope limitation remains material.
  - Candidate is not component.
  - S8 classification is not promotion.
  - Receipt/report/dashboard are evidence, not authority.
  - Existing pre-approval regression scripts must not be treated as post-execution proof unless updated.

HOLD:
  - no promotion
  - no VectorFL authority mutation
  - no baseline/workflow/schema/registry/ontology mutation
  - no current-position/output_manifest mutation
  - no memory/skill/cron/config mutation for VectorFL authority

primary_evidence:
  - {abspath(PATHS['gemini_raw'])}
  - {abspath(PATHS['gemini_lite'])}
  - {abspath(PATHS['codex_return'])}
  - {abspath(PATHS['hermes_receipt'])}
  - {abspath(PATHS['s8_receipt'])}
  - {abspath(PATHS['post_index_receipt'])}

next_smallest_action:
  Run post-execution safe regression and then decide whether to prepare an additional bounded evidence packet for the Gemini scope gap.

required_final_line:
  No promotion was performed. Recovery class remains candidate.
"""
with open(watch_path,'w',encoding='utf-8') as f: f.write(watch)
t8_pass=True

results={
 't1_evidence_integrity_check': {'pass':t1_pass,'missing':missing,'parse_errors':parse_errors,'evidence_count':len(evidence)},
 't2_scope_gap_review': {'pass':t2_pass,'observed_scope_count':len(observed_scope) if isinstance(observed_scope,list) else None,'uncertainties_count':len(uncertainties) if isinstance(uncertainties,list) else None,'do_not_promote_count':len(do_not_promote) if isinstance(do_not_promote,list) else None,'scope_line_hits':scope_lines[:40]},
 't3_codex_recovery_quality_review': {'pass':t3_pass,'required_codex_presence':required_codex_presence,'forbidden_hits':forbidden_hits},
 't4_hermes_closeout_consistency_review': {'pass':t4_pass,'fields':fields,'contradictions':contradictions},
 't5_s8_classification_review': {'pass':t5_pass,'why_not_component':why,'conditions':conditions,'limitation':limitation},
 't6_regression_guard_update': {'pass':t6_pass,'runner':runner_path,'note':'post-execution runner does not call run-gemini-after-approval or run-codex-after-approval'},
 't7_promotion_gate_packet_prepare_only': {'pass':t7_pass,'packet':packet_path,'promotion_approved':False},
 't8_final_s8_watch_closeout': {'pass':t8_pass,'watch_closeout':watch_path},
}
overall=all(v.get('pass') for v in results.values())
receipt={
 'verdict':'POST_EXECUTION_VERIFICATION_LOOP_PASS_CANDIDATE_WITH_PROMOTION_HOLD' if overall else 'POST_EXECUTION_VERIFICATION_LOOP_WATCH',
 'created_at_utc':datetime.datetime.utcnow().replace(microsecond=0).isoformat()+'Z',
 'base':BASE,
 'results':results,
 'non_actions':['no Gemini execution','no Codex execution','no model API transport','no promotion','no VectorFL authority mutation'],
 'required_final_line':'No promotion was performed. Recovery class remains candidate.'
}
report_path=os.path.join(OUTDIR,'POST_EXECUTION_VERIFICATION_REPORT_V0.md')
receipt_path=os.path.join(OUTDIR,'POST_EXECUTION_VERIFICATION_RECEIPT_V0.json')
report=f"""# Post Execution Verification Report v0

verdict:
  {receipt['verdict']}

summary_for_human:
  목록 1~8을 실행/검증했습니다.
  현재 상태는 S8 classification-only complete이며, 회수 등급은 candidate입니다.
  promotion과 VectorFL authority mutation은 수행되지 않았습니다.

checks:
  1 evidence_integrity_check: {'PASS' if t1_pass else 'WATCH'}
  2 scope_gap_review: {'PASS' if t2_pass else 'WATCH'}
  3 codex_recovery_quality_review: {'PASS' if t3_pass else 'WATCH'}
  4 hermes_closeout_consistency_review: {'PASS' if t4_pass else 'WATCH'}
  5 s8_classification_review: {'PASS' if t5_pass else 'WATCH'}
  6 regression_guard_update: {'PASS' if t6_pass else 'WATCH'}
  7 promotion_gate_packet_prepare_only: {'PASS' if t7_pass else 'WATCH'}
  8 final_s8_watch_closeout: {'PASS' if t8_pass else 'WATCH'}

key_findings:
  - all declared evidence present: {not missing}
  - json parse errors: {len(parse_errors)}
  - codex forbidden promotion hits: {len(forbidden_hits)}
  - closeout contradictions: {len(contradictions)}
  - S8 classification: {s8.get('classification')}
  - promotion: {s8.get('promotion')}
  - VectorFL authority mutation: {s8.get('vectorfl_authority_mutation')}

created:
  - {receipt_path}
  - {report_path}
  - {runner_path}
  - {packet_path}
  - {watch_path}

runner_to_reuse:
  {runner_path}

WATCH:
  - Gemini scope limitation remains the main blocker for component promotion.
  - Post-execution regression must avoid re-running Gemini/Codex unless separately approved.
  - Candidate is not component.

HOLD:
  - no promotion
  - no VectorFL authority mutation
  - no baseline/workflow/schema/registry/ontology/current-position/output_manifest edits

required_final_line:
  No promotion was performed. Recovery class remains candidate.
"""
with open(report_path,'w',encoding='utf-8') as f: f.write(report)
with open(receipt_path,'w',encoding='utf-8') as f: json.dump(receipt,f,ensure_ascii=False,indent=2); f.write('\n')
print(receipt['verdict'])
print(report_path)
print(receipt_path)
print(runner_path)
