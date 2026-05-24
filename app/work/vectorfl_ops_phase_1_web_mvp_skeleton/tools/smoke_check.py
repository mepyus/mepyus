#!/usr/bin/env python3
import json, urllib.request, sys
base=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:8765'
checks=[]
def get(path):
    with urllib.request.urlopen(base+path, timeout=3) as r:
        data=r.read()
        return r.status, r.headers.get('Content-Type',''), data
for path in ['/health','/api/summary','/api/requests','/api/guardrails','/api/request/1','/']:
    status,ctype,data=get(path)
    checks.append({'path':path,'status':status,'content_type':ctype,'bytes':len(data)})
    if status!=200: raise SystemExit('BAD_STATUS '+path)
summary=json.loads(get('/api/summary')[2].decode('utf-8'))
if summary['counts']['requests'] != 7: raise SystemExit('BAD_REQUEST_COUNT')
if summary['counts']['fail_events'] != 0: raise SystemExit('FAIL_EVENTS_NONZERO')
if summary['counts']['authority_mutations'] != 0: raise SystemExit('AUTHORITY_MUTATION_NONZERO')
if summary['boundary']['promotion'] != 'HOLD': raise SystemExit('PROMOTION_NOT_HOLD')
print('PHASE1_SERVER_SMOKE_PASS')
print(json.dumps(checks, ensure_ascii=False, indent=2))
