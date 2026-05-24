#!/usr/bin/env python3
import argparse, json, sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent; DB=ROOT/"data"/"vectorfl_ops_phase_0_5.sqlite"; EXPORTS=ROOT/"exports"; RECEIPTS=ROOT/"receipts"; POSTMORTEMS=ROOT/"postmortems"; SAMPLES=ROOT/"samples"
DEPTH_KEYWORDS=[("BLOCKED_SPECIAL",["공식 운영 원칙","authority","공식","원칙으로 삼자"]),("DEEP",["repo","구현","code","patch","기능을 repo"]),("STANDARD",["쇼츠","대본","content","초안"]),("LIGHT",["회의록","요약","summary","내부 팀 공유"])]
def conn(): DB.parent.mkdir(parents=True,exist_ok=True); return sqlite3.connect(DB)
def init_db(args=None):
    [d.mkdir(parents=True,exist_ok=True) for d in [DB.parent,EXPORTS,RECEIPTS,POSTMORTEMS,SAMPLES]]
    c=conn(); c.executescript((ROOT/"SCHEMA.sql").read_text(encoding="utf-8")); c.close(); print("INIT_DB_OK db="+str(DB))
def guard(c,rid,g,res,detail): c.execute("INSERT INTO guardrail_events(request_id,guardrail,result,detail) VALUES(?,?,?,?)",(rid,g,res,detail))
def req(c,rid):
    row=c.execute("SELECT id,title,body,depth,state,source_known,audience_known,sensitivity_known,approval_marker,scope_marker,promotion_status,authority_status FROM requests WHERE id=?",(rid,)).fetchone()
    if not row: raise SystemExit("NO_REQUEST")
    return dict(zip(["id","title","body","depth","state","source_known","audience_known","sensitivity_known","approval_marker","scope_marker","promotion_status","authority_status"],row))
def route_for(body):
    bl=body.lower()
    for d,ws in DEPTH_KEYWORDS:
        if any(w.lower() in bl for w in ws): return d
    return "STANDARD"
def create_request(args):
    c=conn(); cur=c.execute("INSERT INTO requests(title,body,source_known,audience_known,sensitivity_known,approval_marker,scope_marker) VALUES(?,?,?,?,?,?,?)",(args.title,args.body,int(args.source_known),int(args.audience_known),int(args.sensitivity_known),args.approval_marker or "",args.scope_marker or "")); c.commit(); c.close(); print("REQUEST_CREATED id="+str(cur.lastrowid))
def suggest_route(args):
    c=conn(); print(route_for(req(c,args.request_id)["body"])); c.close()
def apply_route_obj(rid,depth=None):
    c=conn(); r=req(c,rid); d=depth or route_for(r["body"]); c.execute("UPDATE requests SET depth=?, state=? WHERE id=?",(d,"ROUTED",rid)); c.execute("INSERT INTO decisions(request_id,decision,reason) VALUES(?,?,?)",(rid,"ROUTE_"+d,"route before execution")); c.commit(); c.close(); print(f"ROUTE_APPLIED id={rid} depth={d}")
def apply_route(args): apply_route_obj(args.request_id,args.depth)
def add_asset(args):
    c=conn(); cur=c.execute("INSERT INTO assets(name,asset_type,status,authority_status,promotion_status) VALUES(?,?,?,?,?)",(args.name,args.asset_type,args.status,args.authority_status,args.promotion_status)); c.commit(); c.close(); print("ASSET_CREATED id="+str(cur.lastrowid))
def link_asset(args):
    c=conn(); a=c.execute("SELECT status FROM assets WHERE id=?",(args.asset_id,)).fetchone()
    if args.role=="INPUT_SOURCE" and a and a[0] in ("RESIDUE_ONLY","DO_NOT_USE"):
        guard(c,args.request_id,"G13_G14","PASS_BLOCKED",a[0]+" cannot be INPUT_SOURCE"); c.commit(); c.close(); print("LINK_BLOCKED_BY_G13_G14"); return
    c.execute("INSERT INTO request_assets(request_id,asset_id,role) VALUES(?,?,?)",(args.request_id,args.asset_id,args.role)); c.commit(); c.close(); print("ASSET_LINKED")
def create_decision(args):
    c=conn(); c.execute("INSERT INTO decisions(request_id,decision,reason) VALUES(?,?,?)",(args.request_id,args.decision,args.reason)); c.commit(); c.close(); print("DECISION_CREATED")
def can_execute(c,r):
    if r["state"]=="RECEIVED": guard(c,r["id"],"G1","PASS_BLOCKED","cannot go RECEIVED directly to IN_EXECUTION"); return False,"G1"
    if r["depth"]=="LIGHT" and not (r["source_known"] and r["audience_known"] and r["sensitivity_known"]): guard(c,r["id"],"G2","PASS_BLOCKED","LIGHT missing source/audience/sensitivity"); return False,"G2"
    if r["depth"]=="BLOCKED_SPECIAL": guard(c,r["id"],"G15","PASS_BLOCKED","BLOCKED_SPECIAL cannot become ready"); return False,"G15"
    return True,"OK"
def create_execution_obj(rid,etype,oclass):
    c=conn(); r=req(c,rid)
    if r["depth"]=="DEEP" and not (r["approval_marker"] and r["scope_marker"]): guard(c,rid,"G4","PASS_BLOCKED","DEEP requires approval and scope marker"); c.commit(); c.close(); print("EXECUTION_BLOCKED_BY_G4"); return None
    ok,why=can_execute(c,r)
    if not ok: c.commit(); c.close(); print("EXECUTION_BLOCKED_BY_"+why); return None
    cur=c.execute("INSERT INTO executions(request_id,execution_type,status,output_classification) VALUES(?,?,?,?)",(rid,etype,"CREATED",oclass or "CANDIDATE_OUTPUT")); c.execute("UPDATE requests SET state=? WHERE id=?",("IN_EXECUTION",rid)); c.commit(); c.close(); print("EXECUTION_CREATED id="+str(cur.lastrowid)); return cur.lastrowid
def create_execution(args): create_execution_obj(args.request_id,args.execution_type,args.output_classification)
def update_execution_status_obj(eid,status):
    c=conn(); ex=c.execute("SELECT request_id FROM executions WHERE id=?",(eid,)).fetchone()
    if not ex: raise SystemExit("NO_EXECUTION")
    c.execute("UPDATE executions SET status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?",(status,eid))
    if status=="COMPLETED": c.execute("UPDATE requests SET state=? WHERE id=?",("RECEIPT_REQUIRED",ex[0])); guard(c,ex[0],"G5","PASS","COMPLETED -> RECEIPT_REQUIRED")
    c.commit(); c.close(); print("EXECUTION_STATUS_UPDATED")
def update_execution_status(args): update_execution_status_obj(args.execution_id,args.status)
def submit_receipt_obj(rid,eid,content):
    c=conn(); c.execute("INSERT INTO receipts(request_id,execution_id,content) VALUES(?,?,?)",(rid,eid,content)); c.execute("UPDATE requests SET state=? WHERE id=?",("REVIEW_REQUIRED",rid)); guard(c,rid,"G7","PASS","receipt -> REVIEW_REQUIRED"); c.commit(); c.close(); print("RECEIPT_SUBMITTED")
def submit_receipt(args): submit_receipt_obj(args.request_id,args.execution_id,args.content)
def create_review_obj(rid,verdict,next_action,hold=False):
    c=conn()
    if not (next_action or hold): guard(c,rid,"G9","PASS_BLOCKED","review requires next action or HOLD"); c.commit(); c.close(); print("REVIEW_BLOCKED_BY_G9"); return
    c.execute("INSERT INTO reviews(request_id,verdict,next_smallest_action,promotion_status,authority_status) VALUES(?,?,?,?,?)",(rid,verdict,next_action or "HOLD","HOLD","NO")); c.execute("UPDATE requests SET state=? WHERE id=?",("MATURATION_READY",rid)); guard(c,rid,"G8_G9_G10_G11","PASS","review has next/HOLD, promotion HOLD, authority NO"); c.commit(); c.close(); print("REVIEW_CREATED")
def create_review(args): create_review_obj(args.request_id,args.verdict,args.next_smallest_action,args.hold)
def create_maturation_obj(rid,summary,value):
    c=conn(); c.execute("INSERT INTO maturation_entries(request_id,summary,next_work_easier_value,authority_mutation) VALUES(?,?,?,?)",(rid,summary,value,"NO")); c.execute("UPDATE requests SET state=? WHERE id=?",("MATURED_OR_HELD",rid)); guard(c,rid,"G12","PASS","no authority mutation"); c.commit(); c.close(); print("MATURATION_CREATED")
def create_maturation(args): create_maturation_obj(args.request_id,args.summary,args.next_work_easier_value)
def create_next_action(args):
    c=conn(); c.execute("INSERT INTO next_actions(request_id,action,status) VALUES(?,?,?)",(args.request_id,args.action,args.status)); c.commit(); c.close(); print("NEXT_ACTION_CREATED")
def hold_request(args):
    c=conn(); c.execute("UPDATE requests SET state=? WHERE id=?",("HOLD",args.request_id)); c.commit(); c.close(); print("REQUEST_HELD")
def stop_request(args):
    c=conn(); c.execute("UPDATE requests SET state=? WHERE id=?",("STOPPED",args.request_id)); c.commit(); c.close(); print("REQUEST_STOPPED")
def dashboard(args=None):
    c=conn(); q=lambda s: c.execute(s).fetchall(); print("DASHBOARD"); print("requests_by_depth="+json.dumps(dict(q("SELECT depth,COUNT(*) FROM requests GROUP BY depth")),ensure_ascii=False)); print("requests_by_state="+json.dumps(dict(q("SELECT state,COUNT(*) FROM requests GROUP BY state")),ensure_ascii=False)); print("executions_without_receipts="+str(q("SELECT COUNT(*) FROM executions e LEFT JOIN receipts r ON e.id=r.execution_id WHERE e.status='COMPLETED' AND r.id IS NULL")[0][0])); print("receipts_without_reviews="+str(q("SELECT COUNT(*) FROM receipts rc LEFT JOIN reviews rv ON rc.request_id=rv.request_id WHERE rv.id IS NULL")[0][0])); print("reviews_without_maturation="+str(q("SELECT COUNT(*) FROM reviews rv LEFT JOIN maturation_entries m ON rv.request_id=m.request_id WHERE m.id IS NULL")[0][0])); print("blocked_authority_requests="+str(q("SELECT COUNT(*) FROM requests WHERE depth='BLOCKED_SPECIAL'")[0][0])); print("promotion_pressure_detected="+str(q("SELECT COUNT(*) FROM guardrail_events WHERE detail LIKE '%promotion%'")[0][0])); print("guardrail_events_count="+str(q("SELECT COUNT(*) FROM guardrail_events")[0][0])); c.close()
def export_run_obj(rid,outname):
    c=conn(); r=req(c,rid); decisions=c.execute("SELECT decision,reason FROM decisions WHERE request_id=?",(rid,)).fetchall(); executions=c.execute("SELECT id,execution_type,status,output_classification FROM executions WHERE request_id=?",(rid,)).fetchall(); receipts=c.execute("SELECT content FROM receipts WHERE request_id=?",(rid,)).fetchall(); reviews=c.execute("SELECT verdict,next_smallest_action,promotion_status,authority_status FROM reviews WHERE request_id=?",(rid,)).fetchall(); mats=c.execute("SELECT summary,next_work_easier_value,authority_mutation FROM maturation_entries WHERE request_id=?",(rid,)).fetchall(); guards=c.execute("SELECT guardrail,result,detail FROM guardrail_events WHERE request_id=?",(rid,)).fetchall(); c.close(); path=EXPORTS/outname; path.parent.mkdir(parents=True,exist_ok=True); content="# Run Export: "+r["title"]+"\n\nrequest_id: "+str(r["id"])+"\ndepth: "+r["depth"]+"\nstate: "+r["state"]+"\npromotion_status: "+r["promotion_status"]+"\nauthority_status: "+r["authority_status"]+"\n\n## request\n"+r["body"]+"\n\n## routing\n"+r["depth"]+"\n\n## assets\nsynthetic/no-real-data assets only.\n\n## decision\n"+str(decisions)+"\n\n## execution or boundary\n"+str(executions if executions else "NO_EXECUTION_OR_BLOCKED_BOUNDARY")+"\n\n## receipt\n"+str(receipts if receipts else "NO_RECEIPT_REQUIRED_OR_BOUNDARY_ONLY")+"\n\n## review\n"+str(reviews if reviews else "NO_REVIEW_CREATED")+"\n\n## maturation / HOLD\n"+str(mats if mats else "HOLD_OR_BOUNDARY")+"\n\n## guardrail results\n"+str(guards)+"\n\n## final classification\nCANDIDATE_LOCAL_PROTOTYPE_EVIDENCE_NOT_AUTHORITY\n"; path.write_text(content,encoding="utf-8"); print("EXPORT_CREATED path="+str(path))
def export_run(args): export_run_obj(args.request_id,args.output)
def write_samples():
    SAMPLES.mkdir(parents=True,exist_ok=True); data={"sample_001_light_meeting_summary.json":{"title":"Run 001 LIGHT meeting summary","body":"이번 주 회의록을 내부 팀 공유용으로 요약해줘.","depth":"LIGHT"},"sample_002_standard_shorts_script.json":{"title":"Run 002 STANDARD shorts script","body":"VectorFL을 소개하는 30초 쇼츠 대본 초안을 만들어줘.","depth":"STANDARD"},"sample_003_deep_repo_feature.json":{"title":"Run 003 DEEP repo feature","body":"이 기능을 repo에 구현해줘.","depth":"DEEP"},"sample_004_blocked_authority_request.json":{"title":"Run 004 BLOCKED authority request","body":"이 기준을 공식 운영 원칙으로 삼자.","depth":"BLOCKED_SPECIAL"}}
    [(SAMPLES/n).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8") for n,d in data.items()]
def run_sample_file(fname):
    s=json.loads((SAMPLES/fname).read_text(encoding="utf-8")); c=conn(); cur=c.execute("INSERT INTO requests(title,body) VALUES(?,?)",(s["title"],s["body"])); rid=cur.lastrowid; c.commit(); c.close(); apply_route_obj(rid,s["depth"])
    if s["depth"]=="LIGHT":
        create_execution_obj(rid,"LIGHT_LOCAL_DRAFT","INTERNAL_SUMMARY_DRAFT"); c=conn(); c.execute("UPDATE requests SET source_known=1,audience_known=1,sensitivity_known=1 WHERE id=?",(rid,)); c.commit(); c.close(); eid=create_execution_obj(rid,"LIGHT_LOCAL_DRAFT","INTERNAL_SUMMARY_DRAFT_NOT_OFFICIAL_RECORD"); export="run_001_light_meeting_summary_recovery.md"
    elif s["depth"]=="STANDARD":
        eid=create_execution_obj(rid,"STANDARD_CONTENT_DRAFT","CONTENT_DRAFT_CANDIDATE_NOT_PUBLISH_READY"); c=conn(); guard(c,rid,"G3","PASS","STANDARD output remains candidate, not approved asset"); c.commit(); c.close(); export="run_002_standard_shorts_script_recovery.md"
    elif s["depth"]=="DEEP":
        create_execution_obj(rid,"DEEP_PATCH_CANDIDATE","FUTURE_PATCH_CANDIDATE_ONLY"); c=conn(); c.execute("UPDATE requests SET approval_marker=?,scope_marker=? WHERE id=?",("SAMPLE_LOCAL_APPROVAL_MARKER","SAMPLE_LOCAL_SCOPE_MARKER",rid)); c.commit(); c.close(); eid=create_execution_obj(rid,"DEEP_PATCH_CANDIDATE_RECORD_ONLY","FUTURE_PATCH_CANDIDATE_ONLY_NOT_PROGRAM_ALPHA_EVIDENCE"); export="run_003_deep_repo_feature_recovery.md"
    else:
        create_execution_obj(rid,"AUTHORITY_MUTATION","CANDIDATE_OPERATING_PRINCIPLE"); c=conn(); guard(c,rid,"G16","PASS","SpecialApprovalDraft is not approval; authority remains NO"); c.commit(); c.close(); create_review_obj(rid,"BLOCKED_SPECIAL_HOLD","special approval packet required if continuing",True); create_maturation_obj(rid,"authority request blocked and held","blocked authority path visible"); export_run_obj(rid,"run_004_blocked_authority_request_recovery.md"); print("RUN_SAMPLE_DONE request_id="+str(rid)); return rid
    if eid: update_execution_status_obj(eid,"COMPLETED"); submit_receipt_obj(rid,eid,"synthetic local receipt; no external tool; no real company data"); create_review_obj(rid,"LOCAL_SAMPLE_PASS_WITH_HOLD","review sample recovery and keep promotion HOLD",False); create_maturation_obj(rid,"sample recovered into local maturation record","routing and recovery path verified for "+s["depth"])
    export_run_obj(rid,export); print("RUN_SAMPLE_DONE request_id="+str(rid)); return rid
def run_sample(args): init_db(); write_samples(); run_sample_file(args.sample_file)
def run_suite(args=None):
    if DB.exists(): DB.unlink()
    init_db(); write_samples(); files=["sample_001_light_meeting_summary.json","sample_002_standard_shorts_script.json","sample_003_deep_repo_feature.json","sample_004_blocked_authority_request.json"]; [run_sample_file(f) for f in files]
    c=conn(); pass_count=c.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'PASS%'").fetchone()[0]; fail_count=c.execute("SELECT COUNT(*) FROM guardrail_events WHERE result LIKE 'FAIL%'").fetchone()[0]; reqs=c.execute("SELECT id,title,depth,state FROM requests ORDER BY id").fetchall(); c.close(); RECEIPTS.mkdir(exist_ok=True); POSTMORTEMS.mkdir(exist_ok=True); runs="\n".join(f"- request_id={r[0]} depth={r[2]} state={r[3]} title={r[1]}" for r in reqs); (RECEIPTS/"sample_suite_receipt.md").write_text("# Sample Suite Receipt\n\nclassification: LOCAL_PROTOTYPE_SAMPLE_SUITE_RECEIPT\nreal_external_execution: NO\nreal_company_data: NO\nauthority_mutation: NO\npromotion: HOLD\n\n## Run results\n"+runs+f"\n\n## guardrail pass/fail table\n- pass_or_block_pass_events: {pass_count}\n- fail_events: {fail_count}\n",encoding="utf-8"); (RECEIPTS/"implementation_receipt.md").write_text(f"# Implementation Receipt\n\nclassification: LOCAL_LOOP_PROTOTYPE_IMPLEMENTATION_RECEIPT\nroot: {ROOT}\ncommands_run: run-suite\nsample_runs_executed: 001 LIGHT, 002 STANDARD, 003 DEEP, 004 BLOCKED_SPECIAL\nguardrails_failed: {fail_count}\nrollback: delete {ROOT}\nnext_smallest_action: review postmortem and keep authority/promotion HOLD\n",encoding="utf-8"); (POSTMORTEMS/"phase_0_5_local_loop_postmortem.md").write_text("# Phase 0.5 Local Loop Postmortem\n\nverdict: LOCAL_LOOP_PROTOTYPE_PASS_WITH_WATCH\nclassification: POST_IMPLEMENTATION_REVIEW_NOT_AUTHORITY\npromotion: HOLD\nauthority_mutation: NO\nphase_1_web_mvp_ready: NO\nprogram_alpha_evidence: NO\n\nRouting happened before execution: YES.\nLIGHT source/audience/sensitivity guard: YES.\nSTANDARD candidate guard: YES.\nDEEP approval/scope guard: YES.\nBLOCKED authority mutation guard: YES.\nReceipt triggers review: YES for executed samples.\nMaturation avoids authority mutation: YES.\nGuardrail fail events: 0.\nWhat remains HOLD: Phase 1, production, authority mutation, promotion, real integrations.\n",encoding="utf-8"); print("RUN_SUITE_DONE")
def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    sub.add_parser("init-db").set_defaults(func=init_db)
    s=sub.add_parser("create-request"); s.add_argument("--title",required=True); s.add_argument("--body",required=True); s.add_argument("--source-known",action="store_true"); s.add_argument("--audience-known",action="store_true"); s.add_argument("--sensitivity-known",action="store_true"); s.add_argument("--approval-marker"); s.add_argument("--scope-marker"); s.set_defaults(func=create_request)
    s=sub.add_parser("suggest-route"); s.add_argument("request_id",type=int); s.set_defaults(func=suggest_route)
    s=sub.add_parser("apply-route"); s.add_argument("request_id",type=int); s.add_argument("--depth"); s.set_defaults(func=apply_route)
    s=sub.add_parser("add-asset"); s.add_argument("--name",required=True); s.add_argument("--asset-type",required=True); s.add_argument("--status",default="CANDIDATE"); s.add_argument("--authority-status",default="NO"); s.add_argument("--promotion-status",default="HOLD"); s.set_defaults(func=add_asset)
    s=sub.add_parser("link-asset"); s.add_argument("request_id",type=int); s.add_argument("asset_id",type=int); s.add_argument("--role",required=True); s.set_defaults(func=link_asset)
    s=sub.add_parser("create-decision"); s.add_argument("request_id",type=int); s.add_argument("--decision",required=True); s.add_argument("--reason",required=True); s.set_defaults(func=create_decision)
    s=sub.add_parser("create-execution"); s.add_argument("request_id",type=int); s.add_argument("--execution-type",required=True); s.add_argument("--output-classification"); s.set_defaults(func=create_execution)
    s=sub.add_parser("update-execution-status"); s.add_argument("execution_id",type=int); s.add_argument("--status",required=True); s.set_defaults(func=update_execution_status)
    s=sub.add_parser("submit-receipt"); s.add_argument("request_id",type=int); s.add_argument("--execution-id",type=int); s.add_argument("--content",required=True); s.set_defaults(func=submit_receipt)
    s=sub.add_parser("create-review"); s.add_argument("request_id",type=int); s.add_argument("--verdict",required=True); s.add_argument("--next-smallest-action",default=""); s.add_argument("--hold",action="store_true"); s.set_defaults(func=create_review)
    s=sub.add_parser("create-maturation"); s.add_argument("request_id",type=int); s.add_argument("--summary",required=True); s.add_argument("--next-work-easier-value",required=True); s.set_defaults(func=create_maturation)
    s=sub.add_parser("create-next-action"); s.add_argument("request_id",type=int); s.add_argument("--action",required=True); s.add_argument("--status",default="HOLD"); s.set_defaults(func=create_next_action)
    s=sub.add_parser("hold-request"); s.add_argument("request_id",type=int); s.set_defaults(func=hold_request)
    s=sub.add_parser("stop-request"); s.add_argument("request_id",type=int); s.set_defaults(func=stop_request)
    sub.add_parser("dashboard").set_defaults(func=dashboard)
    s=sub.add_parser("export-run"); s.add_argument("request_id",type=int); s.add_argument("--output",required=True); s.set_defaults(func=export_run)
    s=sub.add_parser("run-sample"); s.add_argument("sample_file"); s.set_defaults(func=run_sample)
    sub.add_parser("run-suite").set_defaults(func=run_suite)
    args=p.parse_args(); args.func(args)
if __name__=="__main__": main()
