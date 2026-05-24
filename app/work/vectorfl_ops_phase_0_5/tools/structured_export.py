#!/usr/bin/env python3
"""PIPELINE_EXPORT_COMPLETENESS_PATCH_V0
Structured local exporter for Phase 0.5 runtime requests.
No external execution. No authority mutation. No promotion.
"""
import sqlite3, json, re
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'data'/'vectorfl_ops_phase_0_5.sqlite'
OUT=ROOT/'exports'/'structured'
RECEIPT=ROOT/'receipts'/'pipeline_export_completeness_patch_receipt.md'
INDEX=ROOT/'exports'/'pipeline_export_completeness_index.md'

TABLES={
    'request':'SELECT id,title,body,depth,state,source_known,audience_known,sensitivity_known,approval_marker,scope_marker,promotion_status,authority_status,created_at FROM requests WHERE id=?',
    'assets':'SELECT a.id,a.name,a.asset_type,a.status,a.authority_status,a.promotion_status,ra.role FROM request_assets ra JOIN assets a ON a.id=ra.asset_id WHERE ra.request_id=? ORDER BY a.id',
    'decisions':'SELECT id,decision,reason,created_at FROM decisions WHERE request_id=? ORDER BY id',
    'executions':'SELECT id,execution_type,status,output_classification,created_at,updated_at FROM executions WHERE request_id=? ORDER BY id',
    'receipts':'SELECT id,execution_id,content,created_at FROM receipts WHERE request_id=? ORDER BY id',
    'reviews':'SELECT id,verdict,next_smallest_action,promotion_status,authority_status,created_at FROM reviews WHERE request_id=? ORDER BY id',
    'maturation':'SELECT id,summary,next_work_easier_value,authority_mutation,created_at FROM maturation_entries WHERE request_id=? ORDER BY id',
    'next_actions':'SELECT id,action,status FROM next_actions WHERE request_id=? ORDER BY id',
    'guardrail_events':'SELECT id,guardrail,result,detail,created_at FROM guardrail_events WHERE request_id=? ORDER BY id',
}
HEADERS={
    'request':['id','title','body','depth','state','source_known','audience_known','sensitivity_known','approval_marker','scope_marker','promotion_status','authority_status','created_at'],
    'assets':['id','name','asset_type','status','authority_status','promotion_status','role'],
    'decisions':['id','decision','reason','created_at'],
    'executions':['id','execution_type','status','output_classification','created_at','updated_at'],
    'receipts':['id','execution_id','content','created_at'],
    'reviews':['id','verdict','next_smallest_action','promotion_status','authority_status','created_at'],
    'maturation':['id','summary','next_work_easier_value','authority_mutation','created_at'],
    'next_actions':['id','action','status'],
    'guardrail_events':['id','guardrail','result','detail','created_at'],
}

def slug(s):
    s=re.sub(r'[^A-Za-z0-9가-힣_-]+','_',s).strip('_')[:60]
    return s or 'request'

def md_table(headers, rows):
    if not rows:
        return '_none_\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for row in rows:
        vals=[]
        for v in row:
            text='' if v is None else str(v)
            text=text.replace('\n','<br>').replace('|','\\|')
            vals.append(text)
        out.append('| '+' | '.join(vals)+' |')
    return '\n'.join(out)+'\n'

def export_request(cur, rid):
    row=cur.execute(TABLES['request'],(rid,)).fetchone()
    if not row:
        raise ValueError(f'NO_REQUEST {rid}')
    title=row[1]
    data={}
    for name,sql in TABLES.items():
        rows=cur.execute(sql,(rid,)).fetchall()
        data[name]=[dict(zip(HEADERS[name], r)) for r in rows]
    boundary_ok=(row[10]=='HOLD' and row[11]=='NO')
    path=OUT/f'request_{rid:03d}_{slug(title)}_structured_export.md'
    body=[]
    body.append(f'# Structured Run Export: {title}\n\n')
    body.append('classification: STRUCTURED_LOCAL_RUN_EXPORT\n')
    body.append(f'request_id: {rid}\n')
    body.append(f'exported_at: {datetime.utcnow().isoformat(timespec="seconds")}Z\n')
    body.append('external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\nprogram_alpha_evidence: NO\n\n')
    for name in ['request','assets','decisions','executions','receipts','reviews','maturation','next_actions','guardrail_events']:
        rows=[tuple(d[h] for h in HEADERS[name]) for d in data[name]]
        body.append(f'## {name}\n')
        body.append(md_table(HEADERS[name], rows))
        body.append('\n')
    body.append('## completeness checklist\n')
    for name in ['request','assets','decisions','executions','receipts','reviews','maturation','next_actions','guardrail_events']:
        count=len(data[name])
        if name=='request': status='PASS' if count==1 else 'FAIL'
        elif name=='assets': status='PASS_EMPTY_OK'
        elif name=='next_actions': status='PASS_EMPTY_OK'
        else: status='PASS' if count>0 else 'WATCH_EMPTY'
        body.append(f'- {name}: {status} count={count}\n')
    body.append(f'- boundary_hold_no: {"PASS" if boundary_ok else "FAIL"}\n')
    body.append('\n## final classification\nLOCAL_STRUCTURED_EXPORT_EVIDENCE_NOT_AUTHORITY\n')
    path.write_text(''.join(body), encoding='utf-8')
    json_path=OUT/f'request_{rid:03d}_{slug(title)}_structured_export.json'
    json_path.write_text(json.dumps({'request_id':rid,'title':title,'classification':'STRUCTURED_LOCAL_RUN_EXPORT','data':data,'boundary_ok':boundary_ok}, ensure_ascii=False, indent=2), encoding='utf-8')
    return {'request_id':rid,'title':title,'markdown':str(path),'json':str(json_path),'boundary_ok':boundary_ok,'counts':{k:len(v) for k,v in data.items()}}

def main():
    if not DB.exists(): raise SystemExit('DB_MISSING')
    OUT.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as con:
        cur=con.cursor()
        ids=[r[0] for r in cur.execute('SELECT id FROM requests ORDER BY id').fetchall()]
        exports=[export_request(cur,rid) for rid in ids]
    fail_count=sum(1 for e in exports if not e['boundary_ok'])
    receipt='# Pipeline Export Completeness Patch Receipt\n\n'
    receipt+='classification: PIPELINE_EXPORT_COMPLETENESS_PATCH_V0\n'
    receipt+='verdict: '+('PASS_STRUCTURED_EXPORTS_CREATED' if fail_count==0 else 'FAIL')+'\n'
    receipt+='external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\nprogram_alpha_evidence: NO\n'
    receipt+=f'exported_requests: {len(exports)}\nfail_count: {fail_count}\n\n'
    receipt+='## Export index\n'
    for e in exports:
        receipt+=f"- request_id={e['request_id']} boundary_ok={e['boundary_ok']} markdown={e['markdown']} json={e['json']}\n"
    receipt+='\n## Boundary\nStructured exports are evidence only, not authority, not promotion, not Phase 1 implementation.\n'
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(receipt, encoding='utf-8')
    INDEX.write_text(receipt.replace('# Pipeline Export Completeness Patch Receipt','# Pipeline Export Completeness Index'), encoding='utf-8')
    print('STRUCTURED_EXPORT_PASS' if fail_count==0 else 'STRUCTURED_EXPORT_FAIL')
    print('exported_requests='+str(len(exports)))
    print('fail_count='+str(fail_count))
    print('receipt='+str(RECEIPT))
    print('index='+str(INDEX))
    raise SystemExit(0 if fail_count==0 else 1)
if __name__=='__main__': main()
