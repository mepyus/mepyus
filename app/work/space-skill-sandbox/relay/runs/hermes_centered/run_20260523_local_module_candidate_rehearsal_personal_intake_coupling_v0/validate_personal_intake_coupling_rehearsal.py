#!/usr/bin/env python3
from pathlib import Path
import json, sqlite3, subprocess, sys, os, tempfile
ROOT=Path(__file__).resolve().parents[7]
RUN=Path(__file__).resolve().parent
SCRIPT=ROOT/'app/work/vectorfl_ops_phase_0_5/tools/personal_intake_min.py'
SCHEMA=ROOT/'app/work/vectorfl_ops_phase_0_5/SCHEMA.sql'
SHARED=ROOT/'app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite'
required=['README.md','module_candidate_contract.md','personal_intake_coupling_dashboard.json','user_surface_cards/personal_intake_coupling_status.md']
for cid in ['PIC-POS-001','PIC-NEG-STOP-001','PIC-NEG-STOP-002','PIC-NEG-STOP-003','PIC-NEG-HOLD-001']:
 required += [f'fixtures/{cid}_fixture.json',f'guard_reviews/{cid}_guard_review.md']
tokens=['promotion_status: HOLD','program_alpha_status: NOT_READY','vectorfl_authority_mutation: no','model_execution: no','real_gemini_execution: no','real_codex_execution: no','approval_applied: no','live_db_intake: HOLD','shared_db_mutation: no','write_ui: no']
problems=[]
def table_counts(db):
 con=sqlite3.connect(db); cur=con.cursor(); out={}
 for t in ['requests','decisions','executions','receipts','reviews','maturation_entries']:
  out[t]=cur.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
 con.close(); return out
shared_before=table_counts(SHARED) if SHARED.exists() else {}
for rel in required:
 p=RUN/rel
 if not p.exists(): problems.append('missing '+rel); continue
 txt=p.read_text(encoding='utf-8')
 if p.suffix=='.md':
  for tok in tokens:
   if tok not in txt: problems.append(f'missing {tok!r} in {rel}')
# actual fixture CLI run
with tempfile.TemporaryDirectory() as td:
 tmp=Path(td); db=tmp/'fixture.sqlite'; receipt_dir=tmp/'receipts'
 con=sqlite3.connect(db); con.executescript(SCHEMA.read_text(encoding='utf-8')); con.commit(); con.close()
 before=table_counts(db)
 env=os.environ.copy(); env['VECTORFL_PHASE0_DB']=str(db)
 cmd=[sys.executable,str(SCRIPT),'--title','Fixture personal intake coupling','--body','A local-only personal intake coupled to the 11-candidate chain as candidate evidence only.','--source-type','personal_note','--lens','input_localization','--boundary-level','STANDARD','--valid-for','fixture-only candidate chain rehearsal','--not-valid-for','live DB intake; write UI; authority; promotion; Program Alpha','--placement-candidate','personal_program_unit_stage1_candidate','--next-smallest-action','review fixture receipt through HOLD surface','--receipt-dir',str(receipt_dir),'--json']
 r=subprocess.run(cmd,cwd=str(ROOT),env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 (RUN/'cli_outputs/PIC-POS-001_stdout.json').write_text(r.stdout,encoding='utf-8')
 (RUN/'cli_outputs/PIC-POS-001_stderr.txt').write_text(r.stderr,encoding='utf-8')
 if r.returncode!=0: problems.append('personal_intake_min returned nonzero: '+r.stderr)
 else:
  data=json.loads(r.stdout)
  if data.get('verdict')!='PASS_PERSONAL_INTAKE_MIN_WITH_HOLD': problems.append('unexpected CLI verdict')
  hold=data.get('hold',{})
  if hold.get('authority_mutation')!='NO' or hold.get('promotion')!='HOLD': problems.append('CLI HOLD mismatch')
 after=table_counts(db)
 expected={k:before[k]+1 for k in before}
 if after!=expected: problems.append(f'fixture DB counts mismatch before={before} after={after}')
 receipts=list(receipt_dir.glob('personal_intake_request_*.md'))
 if len(receipts)!=1: problems.append('receipt count not 1')
 else:
  txt=receipts[0].read_text(encoding='utf-8')
  for tok in ['authority_status: NO','promotion_status: HOLD','external_execution: NO','router_runner_claim: NO']:
   if tok not in txt: problems.append(f'fixture receipt missing {tok}')
shared_after=table_counts(SHARED) if SHARED.exists() else {}
if shared_before!=shared_after: problems.append(f'shared DB mutated before={shared_before} after={shared_after}')
dash=json.loads((RUN/'personal_intake_coupling_dashboard.json').read_text(encoding='utf-8'))
for k,v in [('live_db_intake','HOLD'),('shared_db_mutation','no'),('write_ui','no'),('promotion_status','HOLD'),('program_alpha_status','NOT_READY'),('vectorfl_authority_mutation','no'),('m4_reusable_module','no')]:
 if dash.get(k)!=v: problems.append(f'dashboard {k} mismatch')
if 'classification: STOP' not in (RUN/'guard_reviews/PIC-NEG-STOP-001_guard_review.md').read_text(encoding='utf-8'): problems.append('live DB claim not STOP')
if 'classification: STOP' not in (RUN/'guard_reviews/PIC-NEG-STOP-002_guard_review.md').read_text(encoding='utf-8'): problems.append('write UI claim not STOP')
if 'classification: HOLD_STOP_REVIEW' not in (RUN/'guard_reviews/PIC-NEG-HOLD-001_guard_review.md').read_text(encoding='utf-8'): problems.append('soft live readiness not HOLD_STOP_REVIEW')
if problems:
 print('FAIL_PERSONAL_INTAKE_COUPLING_MODULE_CANDIDATE_REHEARSAL')
 print('\n'.join(problems)); sys.exit(1)
print('PASS_PERSONAL_INTAKE_COUPLING_MODULE_CANDIDATE_REHEARSAL_WITH_HOLD')
print('cases_checked=5')
print('positive_fixture_intake=INTAKE_CAPTURED_WITH_HOLD')
print('negative_live_db_intake_claim=STOP')
print('negative_write_ui_claim=STOP')
print('negative_authority_promotion_claim=STOP')
print('negative_soft_live_readiness=HOLD_STOP_REVIEW')
print('fixture_db_mutation=YES')
print('shared_db_mutation=NO')
print('live_db_intake=HOLD')
print('authority_mutation=NO')
print('promotion=HOLD')
