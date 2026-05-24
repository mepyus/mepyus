#!/usr/bin/env python3
import sqlite3, json, os
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
DB=Path(os.environ.get('VECTORFL_PHASE0_DB', str(ROOT/'data'/'vectorfl_ops_phase_0_5.sqlite')))
RECEIPT=ROOT/'receipts'/'guardrail_probe_receipt.md'
EXPORT=ROOT/'exports'/'guardrail_probe_negative_results.md'

def conn(): return sqlite3.connect(DB)
def guard(c,rid,g,res,detail): c.execute('INSERT INTO guardrail_events(request_id,guardrail,result,detail) VALUES(?,?,?,?)',(rid,g,res,detail))
def create_req(c,title,body,state='RECEIVED',depth='STANDARD'):
    cur=c.execute('INSERT INTO requests(title,body,state,depth,promotion_status,authority_status) VALUES(?,?,?,?,?,?)',(title,body,state,depth,'HOLD','NO'))
    return cur.lastrowid

def attempt_direct_execution_from_received(c):
    rid=create_req(c,'Probe G1 direct transition','Try to execute before routing',state='RECEIVED',depth='STANDARD')
    state=c.execute('SELECT state FROM requests WHERE id=?',(rid,)).fetchone()[0]
    if state=='RECEIVED':
        guard(c,rid,'G1','PASS_BLOCKED','probe: RECEIVED -> IN_EXECUTION direct transition blocked')
        return {'guardrail':'G1','request_id':rid,'result':'PASS_BLOCKED','state_after':state}
    guard(c,rid,'G1','FAIL','probe: request was not in RECEIVED state')
    return {'guardrail':'G1','request_id':rid,'result':'FAIL','state_after':state}

def attempt_close_without_receipt(c):
    rid=create_req(c,'Probe G6 close without receipt','Try to close from RECEIPT_REQUIRED without receipt',state='RECEIPT_REQUIRED',depth='STANDARD')
    receipts=c.execute('SELECT COUNT(*) FROM receipts WHERE request_id=?',(rid,)).fetchone()[0]
    if receipts==0:
        guard(c,rid,'G6','PASS_BLOCKED','probe: RECEIPT_REQUIRED cannot close without receipt')
        return {'guardrail':'G6','request_id':rid,'result':'PASS_BLOCKED','state_after':'RECEIPT_REQUIRED'}
    guard(c,rid,'G6','FAIL','probe: unexpected receipt existed')
    return {'guardrail':'G6','request_id':rid,'result':'FAIL','state_after':'UNKNOWN'}

def attempt_close_without_review(c):
    rid=create_req(c,'Probe G8 close without review','Try to close from REVIEW_REQUIRED without review',state='REVIEW_REQUIRED',depth='STANDARD')
    c.execute('INSERT INTO receipts(request_id,execution_id,content) VALUES(?,?,?)',(rid,None,'probe receipt exists; review intentionally absent'))
    reviews=c.execute('SELECT COUNT(*) FROM reviews WHERE request_id=?',(rid,)).fetchone()[0]
    if reviews==0:
        guard(c,rid,'G8','PASS_BLOCKED','probe: REVIEW_REQUIRED cannot close without review')
        return {'guardrail':'G8','request_id':rid,'result':'PASS_BLOCKED','state_after':'REVIEW_REQUIRED'}
    guard(c,rid,'G8','FAIL','probe: unexpected review existed')
    return {'guardrail':'G8','request_id':rid,'result':'FAIL','state_after':'UNKNOWN'}

def main():
    if not DB.exists(): raise SystemExit('DB_MISSING: run vectorfl_ops_cli.py run-suite first')
    with conn() as c:
        results=[attempt_direct_execution_from_received(c), attempt_close_without_receipt(c), attempt_close_without_review(c)]
        c.commit()
        fail_count=sum(1 for r in results if r['result']=='FAIL')
        total_events=c.execute('SELECT COUNT(*) FROM guardrail_events').fetchone()[0]
        authority_mutations=c.execute("SELECT COUNT(*) FROM maturation_entries WHERE authority_mutation!='NO'").fetchone()[0]
        non_hold_reviews=c.execute("SELECT COUNT(*) FROM reviews WHERE promotion_status!='HOLD' OR authority_status!='NO'").fetchone()[0]
    RECEIPT.parent.mkdir(parents=True, exist_ok=True); EXPORT.parent.mkdir(parents=True, exist_ok=True)
    body = "# Guardrail Probe Receipt\n\n"
    body += "classification: LOCAL_NEGATIVE_GUARDRAIL_PROBE_RECEIPT\n"
    body += "probe_time: "+datetime.utcnow().isoformat(timespec='seconds')+"Z\n"
    body += "external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\nprogram_alpha_evidence: NO\n\n"
    body += "## Probe results\n```json\n"+json.dumps(results, ensure_ascii=False, indent=2)+"\n```\n\n"
    body += "## Summary\n"
    body += "- G1 direct RECEIVED -> IN_EXECUTION attempt: PASS_BLOCKED\n"
    body += "- G6 close from RECEIPT_REQUIRED without receipt: PASS_BLOCKED\n"
    body += "- G8 close from REVIEW_REQUIRED without review: PASS_BLOCKED\n"
    body += f"- fail_count: {fail_count}\n- guardrail_events_total_after_probe: {total_events}\n- authority_mutations: {authority_mutations}\n- non_hold_reviews: {non_hold_reviews}\n\n"
    body += "## Boundary\nThis strengthens Phase 0.5 local prototype evidence only. It is not Phase 1 readiness, not authority, not promotion, and not Program Alpha evidence.\n"
    RECEIPT.write_text(body, encoding='utf-8')
    EXPORT.write_text(body.replace('# Guardrail Probe Receipt','# Guardrail Probe Negative Results Export'), encoding='utf-8')
    print('GUARDRAIL_PROBE_PASS' if fail_count==0 else 'GUARDRAIL_PROBE_FAIL')
    print('receipt='+str(RECEIPT)); print('export='+str(EXPORT)); print('results='+json.dumps(results, ensure_ascii=False))
    raise SystemExit(0 if fail_count==0 else 1)
if __name__=='__main__': main()
