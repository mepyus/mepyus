#!/usr/bin/env python3
from pathlib import Path
import sqlite3, sys
root = Path(__file__).resolve().parents[1]
review = Path(__file__).resolve().parent
required = [
    review/'00_REVIEW_BOUNDARY.md',
    review/'01_EXECUTED_RESULT_COMPRESSION.md',
    review/'02_GAP_AND_FIX_BACKLOG.md',
    review/'03_PHASE1_BOUNDARY_CARD.md',
    review/'04_USER_SURFACE_SUMMARY.md',
]
problems=[]
for p in required:
    if not p.exists(): problems.append(f'missing {p}')
texts='\n'.join(p.read_text(encoding='utf-8') for p in required if p.exists())
for token in ['promotion: HOLD','authority_mutation: NO','not authority','Phase 1', 'WATCH']:
    if token not in texts:
        problems.append(f'missing boundary token: {token}')
for bad in ['Program Alpha evidence: YES','authority_mutation: YES','promotion: APPROVED','PHASE_1_WEB_MVP_READY']:
    if bad in texts:
        problems.append(f'forbidden claim: {bad}')
db=root/'data'/'vectorfl_ops_phase_0_5.sqlite'
if not db.exists():
    problems.append('missing sqlite db')
else:
    con=sqlite3.connect(db)
    cur=con.cursor()
    if cur.execute('SELECT COUNT(*) FROM requests').fetchone()[0] != 4: problems.append('expected 4 requests')
    if cur.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()[0] != 0: problems.append('guardrail fail events found')
    if cur.execute("SELECT COUNT(*) FROM maturation_entries WHERE authority_mutation!='NO'").fetchone()[0] != 0: problems.append('authority mutation found')
    if cur.execute("SELECT COUNT(*) FROM reviews WHERE promotion_status!='HOLD' OR authority_status!='NO'").fetchone()[0] != 0: problems.append('non-HOLD/NO review found')
if problems:
    print('VALIDATION_FAIL')
    for p in problems: print('- '+p)
    sys.exit(1)
print('VALIDATION_PASS')
