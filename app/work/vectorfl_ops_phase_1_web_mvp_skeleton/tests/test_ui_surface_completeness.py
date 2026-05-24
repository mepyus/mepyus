#!/usr/bin/env python3
import json, os, subprocess, sys, tempfile, time, unittest, urllib.request
from pathlib import Path
from fixture_db import create_fixture_db
ROOT=Path(__file__).resolve().parents[1]
PORT=8881
BASE=f'http://127.0.0.1:{PORT}'
class UISurfaceCompletenessTests(unittest.TestCase):
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
            except Exception: time.sleep(0.1)
        out,err=cls.proc.communicate(timeout=1)
        raise RuntimeError('server did not start '+out+err)
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        try: cls.proc.wait(timeout=3)
        except subprocess.TimeoutExpired: cls.proc.kill()
        cls.tmpdir.cleanup()
    def get(self,path):
        with urllib.request.urlopen(BASE+path, timeout=3) as r:
            return r.status, r.headers.get('Content-Type',''), r.read()
    def test_html_surface_contains_required_sections(self):
        status,ctype,body=self.get('/')
        self.assertEqual(status,200)
        html=body.decode('utf-8')
        for token in ['Boundary banner','Runtime counts','Requests','Guardrail summary','Intentional residue','Source-note WATCH','API links']:
            self.assertIn(token, html)
        for token in ['promotion HOLD','authority mutation NO','Program Alpha NO','external execution NO','write UI NO']:
            self.assertIn(token, html)
        for token in ['missing notes: [10, 19, 57]','54.md == 53.md','G1/G6/G8 intentional negative-probe residue']:
            self.assertIn(token, html)
        self.assertIn('/api/ui-surface', html)
    def test_ui_surface_api_contract(self):
        status,ctype,body=self.get('/api/ui-surface')
        self.assertEqual(status,200)
        self.assertIn('application/json',ctype)
        d=json.loads(body.decode('utf-8'))
        self.assertEqual(d['hold']['promotion'],'HOLD')
        self.assertEqual(d['hold']['authority_mutation'],'NO')
        self.assertEqual(d['hold']['write_ui'],'NO')
        self.assertEqual(d['source_note_watch']['missing_notes'],[10,19,57])
        self.assertIn('54.md == 53.md', d['source_note_watch']['duplicate_notes'])
        self.assertGreaterEqual(d['intentional_residue']['probe_requests'],3)
        self.assertGreaterEqual(d['intentional_residue']['receipts_without_reviews'],1)
        for section in ['boundary banner','runtime counts','request table','guardrail summary','intentional residue','source-note WATCH','HOLD boundary','API links']:
            self.assertIn(section, d['minimum_sections'])
if __name__=='__main__': unittest.main(verbosity=2)
