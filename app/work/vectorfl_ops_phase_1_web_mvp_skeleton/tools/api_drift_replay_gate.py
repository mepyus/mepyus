#!/usr/bin/env python3
"""Formal API drift replay gate for Phase 1 local Web MVP.
Reads the captured API contract snapshot, starts the local server, compares live
schema/boundary/count invariants, writes a drift report, receipt, and export.
"""
from pathlib import Path
import json, os, subprocess, sys, tempfile, time, urllib.request, urllib.error, datetime, hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tests'))
from fixture_db import create_fixture_db
SNAP_DIR=ROOT/'snapshots'/'phase1_api_contract_snapshot_v0'
REPORT_DIR=ROOT/'reports'
PORT=int(os.environ.get('VECTORFL_PHASE1_DRIFT_PORT','8880'))
BASE=f'http://127.0.0.1:{PORT}'
STRICT_HASH=os.environ.get('VECTORFL_PHASE1_STRICT_HASH','0')=='1'

def fetch(path):
    try:
        with urllib.request.urlopen(BASE+path, timeout=3) as r:
            body=r.read(); ctype=r.headers.get('Content-Type','')
            parsed=json.loads(body.decode('utf-8')) if 'application/json' in ctype else None
            return {'path':path,'status':r.status,'content_type':ctype,'bytes':len(body),'json':parsed,'sha256':hashlib.sha256(body).hexdigest()}
    except urllib.error.HTTPError as e:
        return {'path':path,'status':e.code,'content_type':e.headers.get('Content-Type',''),'bytes':0,'json':None,'sha256':None,'error':e.read().decode('utf-8','replace')}

def start(db_path):
    env=os.environ.copy(); env['VECTORFL_PHASE1_PORT']=str(PORT); env['VECTORFL_PHASE1_HOST']='127.0.0.1'; env['VECTORFL_PHASE0_DB']=str(db_path)
    p=subprocess.Popen([sys.executable, str(ROOT/'app.py')], cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    deadline=time.time()+8
    while time.time()<deadline:
        try:
            if fetch('/health')['status']==200: return p
        except Exception: pass
        time.sleep(0.1)
    out,err=p.communicate(timeout=1)
    raise RuntimeError('server did not start\nSTDOUT='+out+'\nSTDERR='+err)

def shape(obj):
    if isinstance(obj, dict): return {k:shape(v) for k,v in sorted(obj.items())}
    if isinstance(obj, list): return [shape(obj[0])] if obj else []
    return type(obj).__name__

def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path=SNAP_DIR/'manifest.json'
    problems=[]; watches=[]; live=[]
    if not manifest_path.exists():
        problems.append('missing snapshot manifest')
        manifest={}
    else:
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    proc=None
    try:
        if manifest:
            tmpdir=tempfile.TemporaryDirectory()
            proc=start(create_fixture_db(Path(tmpdir.name)/'vectorfl_ops_phase_0_5.sqlite'))
            for ep in manifest.get('endpoints',[]):
                item=fetch(ep); live.append(item)
                if item['status']!=200: problems.append(f'{ep} status drift {item["status"]}')
                if ep.startswith('/api') or ep=='/health':
                    if 'application/json' not in item['content_type']: problems.append(f'{ep} content-type drift')
                    if item['json'] is None: problems.append(f'{ep} missing json')
                old_file=SNAP_DIR/((ep.strip('/').replace('/','__') or 'root')+'.json')
                if old_file.exists():
                    old=json.loads(old_file.read_text(encoding='utf-8'))
                    if item['json'] is not None and old.get('json') is not None and shape(item['json']) != shape(old['json']):
                        problems.append(f'{ep} schema shape drift')
                    if STRICT_HASH and item.get('sha256') != old.get('sha256'):
                        problems.append(f'{ep} strict hash drift')
                    elif item.get('sha256') != old.get('sha256'):
                        watches.append(f'{ep} response hash changed or runtime ordering differs')
                else:
                    problems.append(f'{ep} missing saved snapshot file')
            by={x['path']:x for x in live}
            if '/api/summary' in by and by['/api/summary']['json']:
                s=by['/api/summary']['json']
                expected=manifest.get('counts',{})
                for key in ['requests','fail_events','authority_mutations','non_hold_reviews']:
                    if s['counts'].get(key)!=expected.get(key): problems.append(f'count drift {key}: {s["counts"].get(key)} != {expected.get(key)}')
                if s['boundary'].get('promotion')!='HOLD': problems.append('promotion boundary drift')
                if s['boundary'].get('authority_mutation')!='NO': problems.append('authority boundary drift')
                if s['boundary'].get('external_model_tool_network_execution')!='NO': problems.append('external execution boundary drift')
            req_item=by.get('/api/requests')
            if req_item and req_item['json']:
                ids=[r['id'] for r in req_item['json'].get('requests',[])]
                if ids != [1,2,3,4,5,6,7]: problems.append('request id set drift '+repr(ids))
    finally:
        if proc:
            proc.terminate()
            try: proc.wait(timeout=3)
            except subprocess.TimeoutExpired: proc.kill()
        if 'tmpdir' in locals():
            tmpdir.cleanup()
    verdict='PASS_API_DRIFT_REPLAY_MATCH' if not problems else 'FAIL_API_DRIFT_DETECTED'
    report={
        'classification':'PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0',
        'verdict':verdict,
        'created_at':datetime.datetime.utcnow().isoformat(timespec='seconds')+'Z',
        'snapshot_manifest':str(manifest_path),
        'base_url':BASE,
        'strict_hash':STRICT_HASH,
        'endpoint_count':len(manifest.get('endpoints',[])) if manifest else 0,
        'problems':problems,
        'watches':watches,
        'live_hashes':{x['path']:x.get('sha256') for x in live},
        'hold':{'promotion':'HOLD','authority_mutation':'NO','program_alpha':'NO','external_model_tool_network_execution':'NO','real_company_data':'NO','production_deployment':'NO','write_ui':'NO'},
        'next_lane':'PIPELINE_PHASE1_UI_SURFACE_COMPLETENESS_V0'
    }
    (REPORT_DIR/'phase1_api_drift_replay_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True), encoding='utf-8')
    receipt=f"""# Phase 1 API Drift Replay Validator Receipt

classification: PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0
verdict: {verdict}
created_at: {report['created_at']}

## Snapshot manifest
{manifest_path}

## Replay mode
strict_hash: {STRICT_HASH}

## Checked
endpoints: {report['endpoint_count']}

## Problems
```json
{json.dumps(problems, ensure_ascii=False, indent=2)}
```

## Watches
```json
{json.dumps(watches, ensure_ascii=False, indent=2)}
```

## Boundary
promotion: HOLD
authority mutation: NO
Program Alpha evidence: NO
external model/tool/network execution: NO
real company data: NO
production deployment: NO
write UI: NO

## Next lane
PIPELINE_PHASE1_UI_SURFACE_COMPLETENESS_V0
"""
    (ROOT/'receipts'/'phase1_api_drift_replay_validator_receipt.md').write_text(receipt, encoding='utf-8')
    (ROOT/'exports'/'phase1_api_drift_replay_validator_export.md').write_text(receipt.replace('Receipt','Export',1), encoding='utf-8')
    print(verdict)
    print('endpoint_count='+str(report['endpoint_count']))
    print('problem_count='+str(len(problems)))
    print('watch_count='+str(len(watches)))
    return 0 if not problems else 1
if __name__=='__main__': raise SystemExit(main())
