#!/usr/bin/env python3
"""PIPELINE_TRANSITION_TABLE_HARDENING_V0
Local-only state/depth/status transition validator for Phase 0.5 prototype.
No external execution. No authority mutation. No promotion.
"""
import sqlite3, json
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'data'/'vectorfl_ops_phase_0_5.sqlite'
RECEIPT=ROOT/'receipts'/'pipeline_transition_table_hardening_receipt.md'
EXPORT=ROOT/'exports'/'pipeline_transition_table_hardening_export.md'

ALLOWED_REQUEST_STATES={
    'RECEIVED','ROUTED','IN_EXECUTION','RECEIPT_REQUIRED','REVIEW_REQUIRED','MATURATION_READY','MATURED_OR_HELD','HOLD','STOPPED'
}
ALLOWED_DEPTHS={'UNROUTED','LIGHT','STANDARD','DEEP','BLOCKED_SPECIAL'}
ALLOWED_EXECUTION_STATUSES={'CREATED','COMPLETED','FAILED','CANCELLED'}
ALLOWED_GUARDRAIL_RESULTS={'PASS','PASS_BLOCKED','WATCH_INTENTIONAL','FAIL'}
ALLOWED_PROMOTION={'HOLD'}
ALLOWED_AUTHORITY={'NO'}

# Allowed state evidence requirements. Probe residues are allowed only when accompanied by matching probe guardrail event.
PROBE_RESIDUE_RULES={
    'RECEIVED': ('G1','probe:'),
    'RECEIPT_REQUIRED': ('G6','probe:'),
    'REVIEW_REQUIRED': ('G8','probe:'),
}

def q(cur, sql, params=()): return cur.execute(sql, params).fetchall()
def one(cur, sql, params=()): return cur.execute(sql, params).fetchone()[0]

def has_probe(cur, rid, guardrail):
    return one(cur, "SELECT COUNT(*) FROM guardrail_events WHERE request_id=? AND guardrail=? AND detail LIKE 'probe:%'", (rid, guardrail)) > 0

def validate_db():
    if not DB.exists():
        return [{'level':'FAIL','code':'DB_MISSING','detail':str(DB)}]
    con=sqlite3.connect(DB)
    cur=con.cursor()
    issues=[]
    # enum checks
    for rid,state in q(cur, 'SELECT id,state FROM requests'):
        if state not in ALLOWED_REQUEST_STATES:
            issues.append({'level':'FAIL','code':'BAD_REQUEST_STATE','request_id':rid,'detail':state})
    for rid,depth in q(cur, 'SELECT id,depth FROM requests'):
        if depth not in ALLOWED_DEPTHS:
            issues.append({'level':'FAIL','code':'BAD_DEPTH','request_id':rid,'detail':depth})
    for eid,status in q(cur, 'SELECT id,status FROM executions'):
        if status not in ALLOWED_EXECUTION_STATUSES:
            issues.append({'level':'FAIL','code':'BAD_EXECUTION_STATUS','execution_id':eid,'detail':status})
    for gid,result in q(cur, 'SELECT id,result FROM guardrail_events'):
        if result not in ALLOWED_GUARDRAIL_RESULTS:
            issues.append({'level':'FAIL','code':'BAD_GUARDRAIL_RESULT','guardrail_event_id':gid,'detail':result})
    for rid,promo,auth in q(cur, 'SELECT id,promotion_status,authority_status FROM requests'):
        if promo not in ALLOWED_PROMOTION: issues.append({'level':'FAIL','code':'PROMOTION_NOT_HOLD','request_id':rid,'detail':promo})
        if auth not in ALLOWED_AUTHORITY: issues.append({'level':'FAIL','code':'AUTHORITY_NOT_NO','request_id':rid,'detail':auth})
    for rid,promo,auth in q(cur, 'SELECT request_id,promotion_status,authority_status FROM reviews'):
        if promo not in ALLOWED_PROMOTION: issues.append({'level':'FAIL','code':'REVIEW_PROMOTION_NOT_HOLD','request_id':rid,'detail':promo})
        if auth not in ALLOWED_AUTHORITY: issues.append({'level':'FAIL','code':'REVIEW_AUTHORITY_NOT_NO','request_id':rid,'detail':auth})
    if one(cur, "SELECT COUNT(*) FROM maturation_entries WHERE authority_mutation!='NO'"):
        issues.append({'level':'FAIL','code':'MATURATION_AUTHORITY_MUTATION','detail':'non-NO authority mutation exists'})
    # transition/evidence checks
    for rid,title,state,depth in q(cur, 'SELECT id,title,state,depth FROM requests'):
        if state == 'MATURED_OR_HELD':
            rv=one(cur, 'SELECT COUNT(*) FROM reviews WHERE request_id=?', (rid,))
            mt=one(cur, 'SELECT COUNT(*) FROM maturation_entries WHERE request_id=?', (rid,))
            if rv < 1 or mt < 1:
                issues.append({'level':'FAIL','code':'MATURED_WITHOUT_REVIEW_OR_MATURATION','request_id':rid,'detail':f'reviews={rv}, maturation={mt}'})
        if state == 'IN_EXECUTION':
            ex=one(cur, 'SELECT COUNT(*) FROM executions WHERE request_id=?', (rid,))
            if ex < 1:
                issues.append({'level':'FAIL','code':'IN_EXECUTION_WITHOUT_EXECUTION','request_id':rid,'detail':'missing execution'})
        if state in PROBE_RESIDUE_RULES:
            g,prefix=PROBE_RESIDUE_RULES[state]
            if not has_probe(cur,rid,g):
                issues.append({'level':'FAIL','code':'UNEXPLAINED_OPEN_STATE','request_id':rid,'detail':f'{state} without {g} probe residue'})
            else:
                issues.append({'level':'WATCH_INTENTIONAL','code':'INTENTIONAL_PROBE_RESIDUE','request_id':rid,'detail':f'{state} explained by {g}'})
        if depth == 'BLOCKED_SPECIAL':
            bad=one(cur, 'SELECT COUNT(*) FROM executions WHERE request_id=?', (rid,))
            # Original sample creates no execution for blocked special; keep this strict.
            if bad != 0:
                issues.append({'level':'FAIL','code':'BLOCKED_SPECIAL_EXECUTED','request_id':rid,'detail':f'executions={bad}'})
    # receipt/review gap classification
    gaps=q(cur, "SELECT rc.request_id, COUNT(*) FROM receipts rc LEFT JOIN reviews rv ON rc.request_id=rv.request_id WHERE rv.id IS NULL GROUP BY rc.request_id")
    for rid,count in gaps:
        if has_probe(cur,rid,'G8'):
            issues.append({'level':'WATCH_INTENTIONAL','code':'RECEIPT_WITHOUT_REVIEW_G8_RESIDUE','request_id':rid,'detail':f'receipts={count}'})
        else:
            issues.append({'level':'FAIL','code':'RECEIPT_WITHOUT_REVIEW_UNEXPLAINED','request_id':rid,'detail':f'receipts={count}'})
    # summary
    fail_count=sum(1 for x in issues if x['level']=='FAIL')
    watch_count=sum(1 for x in issues if x['level']=='WATCH_INTENTIONAL')
    return issues + [{'level':'SUMMARY','code':'TRANSITION_TABLE_SUMMARY','detail':{'fail_count':fail_count,'watch_intentional_count':watch_count}}]

def main():
    issues=validate_db()
    summary=[x for x in issues if x['level']=='SUMMARY'][0]['detail']
    verdict='PASS_WITH_INTENTIONAL_RESIDUE' if summary['fail_count']==0 else 'FAIL'
    body='# Pipeline Transition Table Hardening Receipt\n\n'
    body+='classification: PIPELINE_TRANSITION_TABLE_HARDENING_V0\n'
    body+='verdict: '+verdict+'\n'
    body+='validated_at: '+datetime.utcnow().isoformat(timespec='seconds')+'Z\n'
    body+='external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\nprogram_alpha_evidence: NO\n\n'
    body+='## Allowed vocabularies\n'
    body+='- request_states: '+', '.join(sorted(ALLOWED_REQUEST_STATES))+'\n'
    body+='- depths: '+', '.join(sorted(ALLOWED_DEPTHS))+'\n'
    body+='- execution_statuses: '+', '.join(sorted(ALLOWED_EXECUTION_STATUSES))+'\n'
    body+='- guardrail_results: '+', '.join(sorted(ALLOWED_GUARDRAIL_RESULTS))+'\n\n'
    body+='## Validation issues\n```json\n'+json.dumps(issues, ensure_ascii=False, indent=2)+'\n```\n\n'
    body+='## Interpretation\nOpen RECEIVED / RECEIPT_REQUIRED / REVIEW_REQUIRED states are acceptable only when explained as G1/G6/G8 intentional probe residues. All promotion and authority fields must remain HOLD/NO.\n\n'
    body+='## Boundary\nThis is local state-transition hardening evidence only; not authority, not promotion, not Phase 1 implementation.\n'
    RECEIPT.parent.mkdir(parents=True, exist_ok=True); EXPORT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(body, encoding='utf-8')
    EXPORT.write_text(body.replace('# Pipeline Transition Table Hardening Receipt','# Pipeline Transition Table Hardening Export'), encoding='utf-8')
    print('TRANSITION_TABLE_VALIDATION_'+('PASS' if summary['fail_count']==0 else 'FAIL'))
    print('fail_count='+str(summary['fail_count']))
    print('watch_intentional_count='+str(summary['watch_intentional_count']))
    print('receipt='+str(RECEIPT))
    print('export='+str(EXPORT))
    raise SystemExit(0 if summary['fail_count']==0 else 1)
if __name__=='__main__': main()
