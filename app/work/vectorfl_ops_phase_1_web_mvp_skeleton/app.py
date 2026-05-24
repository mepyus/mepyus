#!/usr/bin/env python3
"""VectorFL Ops Phase 1 Local Web MVP Skeleton.
Local-only stdlib HTTP server. Reads Phase 0.5 SQLite evidence.
No authority mutation. No promotion. No external model/tool/network execution.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from pathlib import Path
import json, sqlite3, html, os, sys
ROOT=Path(__file__).resolve().parent
PHASE0_DB=Path(os.environ.get('VECTORFL_PHASE0_DB','/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite'))
HOST=os.environ.get('VECTORFL_PHASE1_HOST','127.0.0.1')
PORT=int(os.environ.get('VECTORFL_PHASE1_PORT','8765'))
BOUNDARY={
  'classification':'PIPELINE_PHASE1_LOCAL_WEB_MVP_SKELETON_V0',
  'local_only':True,
  'authority_mutation':'NO',
  'promotion':'HOLD',
  'program_alpha_evidence':'NO',
  'external_model_tool_network_execution':'NO',
  'real_company_data':'NO',
  'source_db':str(PHASE0_DB),
}

def connect():
    if not PHASE0_DB.exists():
        raise FileNotFoundError(str(PHASE0_DB))
    con=sqlite3.connect(PHASE0_DB)
    con.row_factory=sqlite3.Row
    return con

def rows(sql, args=()):
    with connect() as con:
        return [dict(r) for r in con.execute(sql,args).fetchall()]

def one(sql, args=()):
    with connect() as con:
        r=con.execute(sql,args).fetchone()
        return dict(r) if r else None

def counts():
    with connect() as con:
        cur=con.cursor()
        return {
          'requests':cur.execute('SELECT COUNT(*) c FROM requests').fetchone()['c'],
          'executions':cur.execute('SELECT COUNT(*) c FROM executions').fetchone()['c'],
          'receipts':cur.execute('SELECT COUNT(*) c FROM receipts').fetchone()['c'],
          'reviews':cur.execute('SELECT COUNT(*) c FROM reviews').fetchone()['c'],
          'maturation_entries':cur.execute('SELECT COUNT(*) c FROM maturation_entries').fetchone()['c'],
          'guardrail_events':cur.execute('SELECT COUNT(*) c FROM guardrail_events').fetchone()['c'],
          'fail_events':cur.execute("SELECT COUNT(*) c FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()['c'],
          'authority_mutations':cur.execute("SELECT COUNT(*) c FROM maturation_entries WHERE authority_mutation!='NO'").fetchone()['c'],
          'non_hold_reviews':cur.execute("SELECT COUNT(*) c FROM reviews WHERE promotion_status!='HOLD' OR authority_status!='NO'").fetchone()['c'],
          'probe_requests':cur.execute("SELECT COUNT(*) c FROM requests WHERE title LIKE 'Probe %'").fetchone()['c'],
          'receipts_without_reviews':cur.execute('SELECT COUNT(*) c FROM receipts rc LEFT JOIN reviews rv ON rc.request_id=rv.request_id WHERE rv.id IS NULL').fetchone()['c'],
        }

def request_detail(rid):
    data={'request':one('SELECT * FROM requests WHERE id=?',(rid,))}
    if not data['request']: return None
    data['assets']=rows('SELECT a.*, ra.role FROM request_assets ra JOIN assets a ON a.id=ra.asset_id WHERE ra.request_id=? ORDER BY a.id',(rid,))
    data['decisions']=rows('SELECT * FROM decisions WHERE request_id=? ORDER BY id',(rid,))
    data['executions']=rows('SELECT * FROM executions WHERE request_id=? ORDER BY id',(rid,))
    data['receipts']=rows('SELECT * FROM receipts WHERE request_id=? ORDER BY id',(rid,))
    data['reviews']=rows('SELECT * FROM reviews WHERE request_id=? ORDER BY id',(rid,))
    data['maturation']=rows('SELECT * FROM maturation_entries WHERE request_id=? ORDER BY id',(rid,))
    data['next_actions']=rows('SELECT * FROM next_actions WHERE request_id=? ORDER BY id',(rid,))
    data['guardrail_events']=rows('SELECT * FROM guardrail_events WHERE request_id=? ORDER BY id',(rid,))
    return data

def json_bytes(obj, status=200):
    return status, 'application/json; charset=utf-8', json.dumps(obj, ensure_ascii=False, indent=2).encode('utf-8')

def ui_surface():
    c=counts()
    return {
      'boundary_banner':['local-only','promotion HOLD','authority mutation NO','Program Alpha NO','external execution NO','write UI NO'],
      'source_note_watch':{'missing_notes':[10,19,57],'duplicate_notes':['54.md == 53.md']},
      'intentional_residue':{
        'probe_requests':c.get('probe_requests'),
        'receipts_without_reviews':c.get('receipts_without_reviews'),
        'interpretation':'G1/G6/G8 intentional negative-probe residue; not failure'
      },
      'minimum_sections':['boundary banner','runtime counts','request table','guardrail summary','intentional residue','source-note WATCH','HOLD boundary','API links'],
      'hold':{'promotion':'HOLD','authority_mutation':'NO','program_alpha':'NO','external_model_tool_network_execution':'NO','real_company_data':'NO','production_deployment':'NO','write_ui':'NO'}
    }

def html_page():
    c=counts()
    surface=ui_surface()
    reqs=rows('SELECT id,title,depth,state,promotion_status,authority_status FROM requests ORDER BY id')
    guards=rows('SELECT guardrail,result,COUNT(*) count FROM guardrail_events GROUP BY guardrail,result ORDER BY guardrail,result')
    items=''.join(f"<tr><td><a href='/request/{r['id']}'>{r['id']}</a></td><td>{html.escape(str(r['title']))}</td><td>{r['depth']}</td><td>{r['state']}</td><td>{r['promotion_status']}</td><td>{r['authority_status']}</td></tr>" for r in reqs)
    guard_items=''.join(f"<tr><td>{html.escape(str(g['guardrail']))}</td><td>{html.escape(str(g['result']))}</td><td>{g['count']}</td></tr>" for g in guards)
    cards=''.join(f"<div class='card'><b>{k}</b><span>{v}</span></div>" for k,v in c.items())
    missing=', '.join(str(x) for x in surface['source_note_watch']['missing_notes'])
    duplicates=', '.join(surface['source_note_watch']['duplicate_notes'])
    residue=surface['intentional_residue']
    return f"""<!doctype html><html><head><meta charset='utf-8'><title>VectorFL Phase 1 Local MVP</title><style>body{{font-family:ui-sans-serif,system-ui;margin:24px;background:#0b1020;color:#e9edf7}}a{{color:#8fd3ff}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px}}.card,.panel{{background:#151b2f;border:1px solid #2c365c;border-radius:10px;padding:12px;margin:12px 0}}.card span{{display:block;font-size:24px;margin-top:6px}}table{{border-collapse:collapse;width:100%;margin:16px 0;background:#11172a}}td,th{{border:1px solid #2c365c;padding:8px;text-align:left}}.hold{{color:#ffd166}}.watch{{color:#ffb4a2}}.ok{{color:#9be7c1}}</style></head><body><h1>VectorFL Phase 1 Local Web MVP Skeleton</h1><section id='boundary-banner' class='panel'><h2>Boundary banner</h2><p class='hold'>local-only · promotion HOLD · authority mutation NO · Program Alpha NO · external execution NO · write UI NO</p></section><h2>Runtime counts</h2><div class='grid'>{cards}</div><section id='intentional-residue' class='panel'><h2>Intentional residue</h2><p>probe_requests: {residue['probe_requests']} · receipts_without_reviews: {residue['receipts_without_reviews']}</p><p class='watch'>{html.escape(residue['interpretation'])}</p></section><section id='source-note-watch' class='panel'><h2>Source-note WATCH</h2><p>missing notes: [{missing}]</p><p>duplicate notes: {html.escape(duplicates)}</p></section><h2>Requests</h2><table><tr><th>id</th><th>title</th><th>depth</th><th>state</th><th>promotion</th><th>authority</th></tr>{items}</table><h2>Guardrail summary</h2><table><tr><th>guardrail</th><th>result</th><th>count</th></tr>{guard_items}</table><section id='api-links' class='panel'><h2>API links</h2><p><a href='/api/summary'>/api/summary</a> · <a href='/api/requests'>/api/requests</a> · <a href='/api/guardrails'>/api/guardrails</a> · <a href='/api/ui-surface'>/api/ui-surface</a></p></section></body></html>""".encode('utf-8')

def detail_page(rid):
    d=request_detail(rid)
    if not d: return None
    title=html.escape(str(d['request'].get('title')))
    sections=[]
    for key,val in d.items():
        sections.append(f"<h2>{key}</h2><pre>{html.escape(json.dumps(val, ensure_ascii=False, indent=2))}</pre>")
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>body{{font-family:ui-sans-serif,system-ui;margin:24px;background:#0b1020;color:#e9edf7}}a{{color:#8fd3ff}}pre{{background:#11172a;border:1px solid #2c365c;padding:12px;overflow:auto}}</style></head><body><a href='/'>← dashboard</a><h1>{title}</h1>{''.join(sections)}</body></html>".encode('utf-8')

class Handler(BaseHTTPRequestHandler):
    server_version='VectorFLLocalPhase1/0.1'
    def log_message(self, fmt, *args):
        sys.stderr.write('%s - - [%s] %s\n' % (self.address_string(), self.log_date_time_string(), fmt%args))
    def send_body(self, status, ctype, body):
        self.send_response(status); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(body))); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        try:
            path=urlparse(self.path).path
            if path=='/': self.send_body(200,'text/html; charset=utf-8',html_page()); return
            if path=='/health': self.send_body(*json_bytes({'ok':True, **BOUNDARY})); return
            if path=='/api/summary': self.send_body(*json_bytes({'boundary':BOUNDARY,'counts':counts()})); return
            if path=='/api/ui-surface': self.send_body(*json_bytes(ui_surface())); return
            if path=='/api/requests': self.send_body(*json_bytes({'requests':rows('SELECT id,title,body,depth,state,promotion_status,authority_status,created_at FROM requests ORDER BY id')})); return
            if path=='/api/guardrails': self.send_body(*json_bytes({'guardrails':rows('SELECT * FROM guardrail_events ORDER BY id')})); return
            if path.startswith('/api/request/'):
                rid=int(path.rsplit('/',1)[-1]); d=request_detail(rid)
                if not d: self.send_body(*json_bytes({'error':'not found'},404)); return
                self.send_body(*json_bytes(d)); return
            if path.startswith('/request/'):
                rid=int(path.rsplit('/',1)[-1]); page=detail_page(rid)
                if not page: self.send_body(404,'text/plain; charset=utf-8',b'not found'); return
                self.send_body(200,'text/html; charset=utf-8',page); return
            self.send_body(404,'text/plain; charset=utf-8',b'not found')
        except Exception as e:
            self.send_body(*json_bytes({'error':type(e).__name__,'detail':str(e)},500))

def run(host=HOST, port=PORT):
    print(f'VECTORFL_PHASE1_LOCAL_SERVER_READY http://{host}:{port}', flush=True)
    ThreadingHTTPServer((host, port), Handler).serve_forever()
if __name__=='__main__': run()
