#!/usr/bin/env python3
"""Replay API snapshot invariants without needing a saved live server.
Starts server, reads manifest, rechecks schema/count/boundary and detail coverage.
"""
from pathlib import Path
import json, os, subprocess, sys, tempfile, time, urllib.request
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tests'))
from fixture_db import create_fixture_db
SNAP_DIR=ROOT/'snapshots'/'phase1_api_contract_snapshot_v0'
PORT=8879
BASE=f'http://127.0.0.1:{PORT}'

def fetch(path):
    with urllib.request.urlopen(BASE+path, timeout=3) as r:
        body=r.read()
        return r.status, r.headers.get('Content-Type',''), json.loads(body.decode('utf-8')) if 'application/json' in r.headers.get('Content-Type','') else None

def start(db_path):
    env=os.environ.copy(); env['VECTORFL_PHASE1_PORT']=str(PORT); env['VECTORFL_PHASE1_HOST']='127.0.0.1'; env['VECTORFL_PHASE0_DB']=str(db_path)
    p=subprocess.Popen([sys.executable, str(ROOT/'app.py')], cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    deadline=time.time()+8
    while time.time()<deadline:
        try:
            if fetch('/health')[0]==200: return p
        except Exception: time.sleep(0.1)
    out,err=p.communicate(timeout=1); raise RuntimeError('server did not start '+out+err)

def main():
    problems=[]
    manifest_path=SNAP_DIR/'manifest.json'
    if not manifest_path.exists():
        print('REPLAY_FAIL\n- missing manifest'); return 1
    m=json.loads(manifest_path.read_text(encoding='utf-8'))
    tmpdir=tempfile.TemporaryDirectory()
    p=start(create_fixture_db(Path(tmpdir.name)/'vectorfl_ops_phase_0_5.sqlite'))
    try:
        for ep in m['endpoints']:
            status,ctype,data=fetch(ep)
            if status!=200: problems.append(f'{ep} status {status}')
            if ep.startswith('/api') or ep=='/health':
                if 'application/json' not in ctype: problems.append(f'{ep} not json')
                if data is None: problems.append(f'{ep} no data')
        summary=fetch('/api/summary')[2]
        if summary['boundary']['authority_mutation']!='NO': problems.append('authority drift')
        if summary['boundary']['promotion']!='HOLD': problems.append('promotion drift')
        for key in ['requests','fail_events','authority_mutations','non_hold_reviews']:
            if summary['counts'].get(key) != m['counts'].get(key): problems.append(f'count drift {key}: {summary["counts"].get(key)} != {m["counts"].get(key)}')
        reqs=fetch('/api/requests')[2]['requests']
        if len(reqs) != 7: problems.append('request length drift')
        for r in reqs:
            d=fetch('/api/request/'+str(r['id']))[2]
            for section in ['assets','decisions','executions','receipts','reviews','maturation','next_actions','guardrail_events']:
                if section not in d: problems.append('missing section '+section+' '+str(r['id']))
    finally:
        p.terminate()
        try: p.wait(timeout=3)
        except subprocess.TimeoutExpired: p.kill()
        tmpdir.cleanup()
    if problems:
        print('API_CONTRACT_REPLAY_FAIL')
        for x in problems: print('- '+x)
        return 1
    print('API_CONTRACT_REPLAY_PASS')
    return 0
if __name__=='__main__': raise SystemExit(main())
