#!/usr/bin/env python3
"""PIPELINE_BASELINE_REPLAY_VALIDATOR_V0
Verify the Phase 0.5 candidate baseline snapshot against current local evidence files.
Local-only. Evidence replay/integrity check only. No authority mutation. No promotion.
"""
import argparse, hashlib, json, sqlite3
from pathlib import Path
from datetime import datetime
ROOT=Path(__file__).resolve().parents[1]
SNAP=ROOT/'snapshots'/'phase0_5_candidate_baseline_v0'
MANIFEST=SNAP/'baseline_manifest.json'
CHECKSUMS=SNAP/'baseline_checksums.tsv'
RECEIPT=ROOT/'receipts'/'pipeline_baseline_replay_validator_receipt.md'
EXPORT=ROOT/'exports'/'pipeline_baseline_replay_validator_export.md'
LIVE_SAFETY_RECEIPT=ROOT/'receipts'/'pipeline_baseline_live_safety_validator_receipt.md'
LIVE_SAFETY_EXPORT=ROOT/'exports'/'pipeline_baseline_live_safety_validator_export.md'
DB=ROOT/'data'/'vectorfl_ops_phase_0_5.sqlite'

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def db_facts():
    con=sqlite3.connect(DB)
    cur=con.cursor()
    facts={
        'requests':cur.execute('SELECT COUNT(*) FROM requests').fetchone()[0],
        'executions':cur.execute('SELECT COUNT(*) FROM executions').fetchone()[0],
        'receipts':cur.execute('SELECT COUNT(*) FROM receipts').fetchone()[0],
        'reviews':cur.execute('SELECT COUNT(*) FROM reviews').fetchone()[0],
        'maturation_entries':cur.execute('SELECT COUNT(*) FROM maturation_entries').fetchone()[0],
        'guardrail_events':cur.execute('SELECT COUNT(*) FROM guardrail_events').fetchone()[0],
        'fail_events':cur.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()[0],
        'authority_mutations':cur.execute("SELECT COUNT(*) FROM maturation_entries WHERE authority_mutation!='NO'").fetchone()[0],
        'non_hold_reviews':cur.execute("SELECT COUNT(*) FROM reviews WHERE promotion_status!='HOLD' OR authority_status!='NO'").fetchone()[0],
        'probe_requests':cur.execute("SELECT COUNT(*) FROM requests WHERE title LIKE 'Probe %'").fetchone()[0],
    }
    con.close()
    return facts

def write_result(result, title, receipt_path=RECEIPT, export_path=EXPORT):
    body=f'# {title}\n\n'
    body+='classification: '+result['classification']+'\n'
    body+='verdict: '+result['verdict']+'\n'
    body+='validated_at: '+result['validated_at']+'\n'
    body+='external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\nprogram_alpha_evidence: NO\nphase1_implementation: NO\n\n'
    if 'checked_files' in result:
        body+=f"## Replay counts\n- checked_files: {result['checked_files']}\n- matched_files: {result['matched_files']}\n- problem_count: {result['problem_count']}\n- watch_count: {result['watch_count']}\n\n"
    body+='## Result\n```json\n'+json.dumps(result, ensure_ascii=False, indent=2)+'\n```\n\n'
    if result['classification']=='PIPELINE_BASELINE_REPLAY_VALIDATOR_V0':
        body+='## Interpretation\nFrozen replay checks exact snapshot byte identity. File checksum mismatches are FAIL. DB count drift after snapshot is WATCH unless safety invariants fail. Promotion remains HOLD and authority remains NO.\n\n'
        body+='## Boundary\nThis frozen replay validator confirms candidate baseline snapshot integrity only. It is not live-safety PASS, not authority, not promotion, not Program Alpha evidence, and not Phase 1 implementation.\n'
    else:
        body+='## Interpretation\nLive-safety mode checks current DB safety invariants only. It does not compare file checksums and does not claim baseline replay PASS. Promotion remains HOLD and authority remains NO.\n\n'
        body+='## Boundary\nThis live-safety validator confirms current local safety invariants only. It is not snapshot replay, not authority, not promotion, not Program Alpha evidence, and not Phase 1 implementation.\n'
    receipt_path.parent.mkdir(parents=True, exist_ok=True); export_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(body, encoding='utf-8')
    export_path.write_text(body.replace(f'# {title}', f'# {title.replace("Receipt", "Export")}'), encoding='utf-8')

def build_frozen_result():
    problems=[]; watches=[]; checked=0; matched=0
    if not MANIFEST.exists():
        problems.append({'code':'MANIFEST_MISSING','detail':str(MANIFEST)})
        manifest={}
    else:
        manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    if not CHECKSUMS.exists():
        problems.append({'code':'CHECKSUMS_MISSING','detail':str(CHECKSUMS)})
    for e in manifest.get('manifest_entries',[]):
        if not e.get('exists'):
            watches.append({'code':'MISSING_ENTRY_WAS_MISSING_AT_SNAPSHOT','relative_path':e.get('relative_path')})
            continue
        p=Path(e['path'])
        if not p.exists():
            problems.append({'code':'SNAPSHOT_FILE_NOW_MISSING','relative_path':e.get('relative_path'),'path':str(p)})
            continue
        current=sha256(p)
        checked+=1
        if current != e.get('sha256'):
            problems.append({'code':'CHECKSUM_MISMATCH','relative_path':e.get('relative_path'),'expected':e.get('sha256'),'actual':current})
        else:
            matched+=1
    current_db=db_facts() if DB.exists() else {'DB_MISSING':True}
    baseline_db=manifest.get('db_facts',{})
    db_drift={k:{'baseline':baseline_db.get(k),'current':current_db.get(k)} for k in sorted(set(baseline_db)|set(current_db)) if baseline_db.get(k)!=current_db.get(k)}
    # DB count drift is WATCH unless safety invariants fail, because new receipts/exports can be added after snapshot.
    if db_drift:
        watches.append({'code':'DB_FACT_DRIFT_AFTER_SNAPSHOT','detail':db_drift})
    if current_db.get('fail_events',0)!=0:
        problems.append({'code':'DB_FAIL_EVENTS_NONZERO','detail':current_db.get('fail_events')})
    if current_db.get('authority_mutations',0)!=0:
        problems.append({'code':'AUTHORITY_MUTATIONS_NONZERO','detail':current_db.get('authority_mutations')})
    if current_db.get('non_hold_reviews',0)!=0:
        problems.append({'code':'NON_HOLD_REVIEWS_NONZERO','detail':current_db.get('non_hold_reviews')})
    return {
        'classification':'PIPELINE_BASELINE_REPLAY_VALIDATOR_V0',
        'verdict':'PASS_REPLAY_MATCH' if not problems else 'FAIL_REPLAY_MISMATCH',
        'validated_at':datetime.utcnow().isoformat(timespec='seconds')+'Z',
        'mode':'frozen',
        'checked_files':checked,
        'matched_files':matched,
        'problem_count':len(problems),
        'watch_count':len(watches),
        'problems':problems,
        'watches':watches,
        'current_db_facts':current_db,
        'baseline_db_facts':baseline_db,
        'manifest':str(MANIFEST),
        'checksums':str(CHECKSUMS),
        'hold':{'promotion':'HOLD','authority_mutation':'NO','phase1_implementation':'NO','external_execution':'NO'}
    }

def build_live_safety_result():
    current_db=db_facts() if DB.exists() else {'DB_MISSING':True}
    problems=[]
    if current_db.get('fail_events',0)!=0:
        problems.append({'code':'DB_FAIL_EVENTS_NONZERO','detail':current_db.get('fail_events')})
    if current_db.get('authority_mutations',0)!=0:
        problems.append({'code':'AUTHORITY_MUTATIONS_NONZERO','detail':current_db.get('authority_mutations')})
    if current_db.get('non_hold_reviews',0)!=0:
        problems.append({'code':'NON_HOLD_REVIEWS_NONZERO','detail':current_db.get('non_hold_reviews')})
    return {
        'classification':'PIPELINE_BASELINE_LIVE_SAFETY_VALIDATOR_V0',
        'verdict':'PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD' if not problems else 'FAIL_LIVE_SAFETY_INVARIANTS',
        'validated_at':datetime.utcnow().isoformat(timespec='seconds')+'Z',
        'mode':'live-safety',
        'problem_count':len(problems),
        'problems':problems,
        'current_db_facts':current_db,
        'checksum_replay_claim':'NO',
        'baseline_replay_pass_claim':'NO',
        'hold':{'promotion':'HOLD','authority_mutation':'NO','phase1_implementation':'NO','external_execution':'NO'}
    }

def main():
    parser=argparse.ArgumentParser(description='Validate Phase 0.5 frozen baseline replay or live safety invariants.')
    parser.add_argument('--mode', choices=['frozen','live-safety'], default='frozen')
    args=parser.parse_args()
    if args.mode=='live-safety':
        result=build_live_safety_result()
        write_result(result, 'Pipeline Baseline Live Safety Validator Receipt', LIVE_SAFETY_RECEIPT, LIVE_SAFETY_EXPORT)
        print('BASELINE_LIVE_SAFETY_'+('PASS' if result['problem_count']==0 else 'FAIL'))
        print('verdict='+result['verdict'])
        print('problem_count='+str(result['problem_count']))
        print('receipt='+str(LIVE_SAFETY_RECEIPT))
        print('export='+str(LIVE_SAFETY_EXPORT))
        raise SystemExit(0 if result['problem_count']==0 else 1)
    result=build_frozen_result()
    write_result(result, 'Pipeline Baseline Replay Validator Receipt')
    print('BASELINE_REPLAY_'+('PASS' if result['problem_count']==0 else 'FAIL'))
    print('checked_files='+str(result['checked_files']))
    print('matched_files='+str(result['matched_files']))
    print('problem_count='+str(result['problem_count']))
    print('watch_count='+str(result['watch_count']))
    print('receipt='+str(RECEIPT))
    print('export='+str(EXPORT))
    raise SystemExit(0 if result['problem_count']==0 else 1)
if __name__=='__main__': main()
