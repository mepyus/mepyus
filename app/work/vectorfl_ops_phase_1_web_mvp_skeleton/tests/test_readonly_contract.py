#!/usr/bin/env python3
"""Read-only contract hardening tests for Phase 1 local Web MVP.
Verifies the local server remains an evidence viewer only: no mutating methods,
known read endpoints stay schema-stable, unknown routes 404, all request detail endpoints load.
"""
import json, os, subprocess, sys, tempfile, time, unittest, urllib.request, urllib.error
from pathlib import Path
from fixture_db import create_fixture_db
ROOT=Path(__file__).resolve().parents[1]
PORT=8877
BASE=f'http://127.0.0.1:{PORT}'
READ_ENDPOINTS=['/health','/api/summary','/api/requests','/api/guardrails','/api/request/1','/']
MUTATING_METHODS=['POST','PUT','PATCH','DELETE']

def request(path, method='GET', data=None):
    body=None if data is None else json.dumps(data).encode('utf-8')
    req=urllib.request.Request(BASE+path, data=body, method=method)
    if body is not None:
        req.add_header('Content-Type','application/json')
    try:
        with urllib.request.urlopen(req, timeout=3) as r:
            return r.status, r.headers.get('Content-Type',''), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get('Content-Type',''), e.read()

class ReadOnlyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmpdir=tempfile.TemporaryDirectory()
        cls.isolated_db=Path(cls.tmpdir.name)/'vectorfl_ops_phase_0_5.sqlite'
        create_fixture_db(cls.isolated_db)
        env=os.environ.copy(); env['VECTORFL_PHASE1_PORT']=str(PORT); env['VECTORFL_PHASE1_HOST']='127.0.0.1'; env['VECTORFL_PHASE0_DB']=str(cls.isolated_db)
        cls.proc=subprocess.Popen([sys.executable, str(ROOT/'app.py')], cwd=str(ROOT), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        deadline=time.time()+8
        while time.time()<deadline:
            try:
                status,_,_=request('/health')
                if status==200: return
            except Exception:
                pass
            time.sleep(0.1)
        out,err=cls.proc.communicate(timeout=1)
        raise RuntimeError('server did not start\nSTDOUT='+out+'\nSTDERR='+err)
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        try: cls.proc.wait(timeout=3)
        except subprocess.TimeoutExpired: cls.proc.kill()
        cls.tmpdir.cleanup()
    def get_json(self,path):
        status,ctype,body=request(path)
        self.assertEqual(status,200,path)
        self.assertIn('application/json',ctype)
        return json.loads(body.decode('utf-8'))
    def test_mutating_methods_are_not_supported(self):
        for method in MUTATING_METHODS:
            for path in ['/api/requests','/api/request/1','/api/summary','/']:
                status,_,_=request(path, method=method, data={'attempt':'mutate'})
                self.assertIn(status, (405,501), f'{method} {path} returned {status}')
    def test_unknown_routes_404(self):
        for path in ['/api/does-not-exist','/request/999999','/not-a-real-page']:
            status,_,_=request(path)
            self.assertEqual(status,404,path)
    def test_api_summary_schema(self):
        data=self.get_json('/api/summary')
        self.assertEqual(set(data.keys()), {'boundary','counts'})
        for key in ['classification','local_only','authority_mutation','promotion','program_alpha_evidence','external_model_tool_network_execution','real_company_data','source_db']:
            self.assertIn(key, data['boundary'])
        for key in ['requests','executions','receipts','reviews','maturation_entries','guardrail_events','fail_events','authority_mutations','non_hold_reviews','probe_requests','receipts_without_reviews']:
            self.assertIn(key, data['counts'])
        self.assertEqual(data['boundary']['authority_mutation'],'NO')
        self.assertEqual(data['boundary']['promotion'],'HOLD')
        self.assertEqual(data['counts']['fail_events'],0)
        self.assertEqual(data['counts']['authority_mutations'],0)
        self.assertEqual(data['counts']['non_hold_reviews'],0)
    def test_requests_schema_and_all_details(self):
        reqs=self.get_json('/api/requests')['requests']
        self.assertGreaterEqual(len(reqs),7)
        for r in reqs:
            for key in ['id','title','body','depth','state','promotion_status','authority_status','created_at']:
                self.assertIn(key,r)
            detail=self.get_json('/api/request/'+str(r['id']))
            self.assertEqual(detail['request']['id'], r['id'])
            for section in ['assets','decisions','executions','receipts','reviews','maturation','next_actions','guardrail_events']:
                self.assertIn(section, detail)
                self.assertIsInstance(detail[section], list)
    def test_guardrail_schema_contains_probe_blocks(self):
        gs=self.get_json('/api/guardrails')['guardrails']
        self.assertGreaterEqual(len(gs),22)
        text='\n'.join(str(g) for g in gs)
        for token in ['G1','G6','G8','PASS_BLOCKED']:
            self.assertIn(token,text)
if __name__=='__main__': unittest.main(verbosity=2)
