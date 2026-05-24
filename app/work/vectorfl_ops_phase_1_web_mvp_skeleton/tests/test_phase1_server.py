#!/usr/bin/env python3
import json, unittest, urllib.request, subprocess, sys, time, os, tempfile
from pathlib import Path
from fixture_db import create_fixture_db
ROOT=Path(__file__).resolve().parents[1]
PORT=8876
BASE=f'http://127.0.0.1:{PORT}'
class Phase1ServerTests(unittest.TestCase):
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
                with urllib.request.urlopen(BASE+'/health', timeout=0.5) as r:
                    if r.status==200: return
            except Exception:
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
        with urllib.request.urlopen(BASE+path, timeout=3) as r:
            self.assertEqual(r.status,200)
            return json.loads(r.read().decode('utf-8'))
    def test_health_boundaries(self):
        h=self.get_json('/health')
        self.assertTrue(h['ok'])
        self.assertEqual(h['authority_mutation'],'NO')
        self.assertEqual(h['promotion'],'HOLD')
        self.assertEqual(h['external_model_tool_network_execution'],'NO')
    def test_summary_counts_and_safety(self):
        s=self.get_json('/api/summary')
        self.assertEqual(s['counts']['requests'],7)
        self.assertEqual(s['counts']['fail_events'],0)
        self.assertEqual(s['counts']['authority_mutations'],0)
        self.assertEqual(s['counts']['non_hold_reviews'],0)
    def test_requests_and_detail(self):
        req=self.get_json('/api/requests')['requests']
        self.assertEqual(len(req),7)
        detail=self.get_json('/api/request/1')
        for key in ['request','decisions','executions','receipts','reviews','maturation','guardrail_events']:
            self.assertIn(key, detail)
    def test_guardrail_probe_presence(self):
        gs=self.get_json('/api/guardrails')['guardrails']
        text='\n'.join(g['guardrail']+':'+g['result'] for g in gs)
        self.assertIn('G1', text)
        self.assertIn('G6', text)
        self.assertIn('G8', text)
        self.assertIn('PASS_BLOCKED', text)
    def test_html_dashboard(self):
        with urllib.request.urlopen(BASE+'/', timeout=3) as r:
            body=r.read().decode('utf-8')
        self.assertIn('VectorFL Phase 1 Local Web MVP Skeleton', body)
        self.assertIn('promotion HOLD', body)
        self.assertIn('/api/summary', body)
if __name__=='__main__': unittest.main(verbosity=2)
