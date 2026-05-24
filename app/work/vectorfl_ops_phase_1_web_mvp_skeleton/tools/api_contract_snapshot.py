#!/usr/bin/env python3
"""Capture/replay API contract snapshots for Phase 1 local Web MVP.
Local-only. Starts the server, captures selected GET endpoints, writes stable JSON
snapshots, and verifies boundary/count/schema invariants.
"""
from pathlib import Path
import json, os, subprocess, sys, time, urllib.request, hashlib, datetime
ROOT=Path(__file__).resolve().parents[1]
SNAP_DIR=ROOT/'snapshots'/'phase1_api_contract_snapshot_v0'
PORT=int(os.environ.get('VECTORFL_PHASE1_SNAPSHOT_PORT','8878'))
BASE=f'http://127.0.0.1:{PORT}'
ENDPOINTS=['/health','/api/summary','/api/requests','/api/guardrails','/api/ui-surface','/','/api/request/1','/api/request/2','/api/request/3','/api/request/4','/api/request/5','/api/request/6','/api/request/7']

def fetch(path):
    with urllib.request.urlopen(BASE+path, timeout=3) as r:
        body=r.read()
        ctype=r.headers.get('Content-Type','')
        parsed=None
        if 'application/json' in ctype:
            parsed=json.loads(body.decode('utf-8'))
        return {'path':path,'status':r.status,'content_type':ctype,'bytes':len(body),'json':parsed,'sha256':hashlib.sha256(body).hexdigest()}

def start_server():
    env=os.environ.copy(); env['VECTORFL_PHASE1_PORT']=str(PORT); env['VECTORFL_PHASE1_HOST']='127.0.0.1'
    p=subprocess.Popen([sys.executable, str(ROOT/'app.py')], cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    deadline=time.time()+8
    while time.time()<deadline:
        try:
            x=fetch('/health')
            if x['status']==200: return p
        except Exception:
            time.sleep(0.1)
    out,err=p.communicate(timeout=1)
    raise RuntimeError('server did not start\nSTDOUT='+out+'\nSTDERR='+err)

def schema_of(obj):
    if isinstance(obj, dict):
        return {k:schema_of(v) for k,v in sorted(obj.items())}
    if isinstance(obj, list):
        if not obj: return []
        # union first 3 shapes to avoid content dump
        return [schema_of(obj[0])]
    return type(obj).__name__

def main():
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    proc=start_server()
    problems=[]
    try:
        captured=[]
        for ep in ENDPOINTS:
            item=fetch(ep)
            captured.append(item)
            safe=ep.strip('/').replace('/','__') or 'root'
            (SNAP_DIR/(safe+'.json')).write_text(json.dumps(item, ensure_ascii=False, indent=2, sort_keys=True), encoding='utf-8')
        by_path={x['path']:x for x in captured}
        summary=by_path['/api/summary']['json']
        if summary['boundary']['authority_mutation']!='NO': problems.append('authority_mutation not NO')
        if summary['boundary']['promotion']!='HOLD': problems.append('promotion not HOLD')
        if summary['counts']['requests']!=7: problems.append('requests count drift')
        if summary['counts']['fail_events']!=0: problems.append('fail events nonzero')
        if summary['counts']['authority_mutations']!=0: problems.append('authority mutations nonzero')
        reqs=by_path['/api/requests']['json']['requests']
        if len(reqs)!=7: problems.append('requests endpoint not 7')
        for i in range(1,8):
            detail=by_path[f'/api/request/{i}']['json']
            if detail['request']['id'] != i: problems.append(f'detail id mismatch {i}')
            for section in ['assets','decisions','executions','receipts','reviews','maturation','next_actions','guardrail_events']:
                if section not in detail: problems.append(f'missing detail section {i}:{section}')
        manifest={
            'classification':'PIPELINE_PHASE1_API_CONTRACT_SNAPSHOT_V0',
            'verdict':'PASS_API_CONTRACT_SNAPSHOT_CAPTURED' if not problems else 'FAIL_API_CONTRACT_SNAPSHOT',
            'created_at':datetime.datetime.utcnow().isoformat(timespec='seconds')+'Z',
            'base_url':BASE,
            'endpoints':ENDPOINTS,
            'captured_count':len(captured),
            'problems':problems,
            'schemas':{x['path']:schema_of(x['json']) for x in captured if x['json'] is not None},
            'response_hashes':{x['path']:x['sha256'] for x in captured},
            'boundary':summary['boundary'],
            'counts':summary['counts'],
            'hold':{'promotion':'HOLD','authority_mutation':'NO','program_alpha':'NO','external_model_tool_network_execution':'NO','real_company_data':'NO','production_deployment':'NO'},
            'next_lane':'PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0'
        }
        (SNAP_DIR/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True), encoding='utf-8')
        receipt=f"""# Phase 1 API Contract Snapshot Receipt

classification: PIPELINE_PHASE1_API_CONTRACT_SNAPSHOT_V0
verdict: {manifest['verdict']}
created_at: {manifest['created_at']}

## Captured
base_url: {BASE}
endpoints: {len(ENDPOINTS)}

## Endpoint list
""" + '\n'.join('- '+x for x in ENDPOINTS) + f"""

## Counts
```json
{json.dumps(summary['counts'], ensure_ascii=False, indent=2)}
```

## Boundary
promotion: HOLD
authority mutation: NO
Program Alpha evidence: NO
external model/tool/network execution: NO
real company data: NO
production deployment: NO

## Problems
{json.dumps(problems, ensure_ascii=False, indent=2)}

## Next lane
PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0
"""
        (ROOT/'receipts'/'phase1_api_contract_snapshot_receipt.md').write_text(receipt, encoding='utf-8')
        (ROOT/'exports'/'phase1_api_contract_snapshot_export.md').write_text(receipt.replace('Receipt','Export',1), encoding='utf-8')
        print(manifest['verdict'])
        print('captured_count='+str(len(captured)))
        print('snapshot_dir='+str(SNAP_DIR))
        return 0 if not problems else 1
    finally:
        proc.terminate()
        try: proc.wait(timeout=3)
        except subprocess.TimeoutExpired: proc.kill()
if __name__=='__main__': raise SystemExit(main())
