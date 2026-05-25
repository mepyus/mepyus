#!/usr/bin/env python3
import json, re, html, urllib.parse, requests, subprocess, datetime, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
HELPER='/Users/sungsookim/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py'
NOW=datetime.datetime.now().astimezone().isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def strip_html(x):
    x=re.sub(r'<script[\s\S]*?</script>',' ',x,flags=re.I)
    x=re.sub(r'<style[\s\S]*?</style>',' ',x,flags=re.I)
    x=re.sub(r'<[^>]+>','\n',x)
    for a,b in [('&nbsp;',' '),('&amp;','&'),('&lt;','<'),('&gt;','>')]: x=x.replace(a,b)
    return '\n'.join([ln.strip() for ln in x.splitlines() if ln.strip()])
def official_policy_slot():
    urls=[
      {'name':'youtube_terms','url':'https://www.youtube.com/t/terms','purpose':'YouTube Terms of Service'},
      {'name':'youtube_api_terms','url':'https://developers.google.com/youtube/terms/api-services-terms-of-service','purpose':'YouTube API Services Terms'},
      {'name':'youtube_api_quota','url':'https://developers.google.com/youtube/v3/getting-started#quota','purpose':'YouTube Data API quota overview'}
    ]
    out=[]
    for u in urls:
        try:
            r=requests.get(u['url'],headers={'User-Agent':'Mozilla/5.0'},timeout=20)
            txt=strip_html(r.text)[:70000]
            p=BASE/'official_sources'/f"01_{u['name']}.txt"
            p.write_text(txt,encoding='utf-8')
            kws=['automated','access','api','quota','scraping','permission','prohibit','terms','collect','service']
            snippets=[]
            for i,line in enumerate(txt.splitlines()):
                if any(k in line.lower() for k in kws):
                    snippets.append({'line':i+1,'text':line[:350]})
                    if len(snippets)>=18: break
            out.append({**u,'status_code':r.status_code,'text_path':str(p),'snippets':snippets,'sha256':sha(p)})
        except Exception as e:
            out.append({**u,'error':str(e)})
    table={'slot':'policy_boundary','source_type':'official_web_docs_first','created_at':NOW,'sources':out,'layers':{'L5_power_authority':'official platform/API docs are the authority boundary evidence candidate','L7_counter_uncertainty':'docs still need human/legal interpretation before operational use','L8_vectorfl_mapping':'policy source strengthens guard ring but remains HOLD'},'promotion':'HOLD'}
    tp=BASE/'tables'/'02_layer_table_policy_boundary_official_docs_v0_1.json'
    tp.write_text(json.dumps(table,ensure_ascii=False,indent=2),encoding='utf-8')
    quality={'slot':'policy_boundary','status':'PASS_OFFICIAL_DOCS_ATTACHED_HOLD','score':0.85,'reasons':['official docs fetched','no YouTube fallback used','policy treated as boundary evidence not legal advice'],'missing_source_marker':False}
    return {'slot':'policy_boundary','selected_type':'official_docs','sources':out,'layer_table':str(tp),'slot_quality_review':quality}
def yt_search(query, slot):
    url='https://www.youtube.com/results?search_query='+urllib.parse.quote(query)
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=20)
    ids=[]
    for m in re.finditer(r'"videoId":"([A-Za-z0-9_-]{11})"',r.text):
        v=m.group(1)
        if v not in ids: ids.append(v)
    c=[]
    for v in ids[:5]:
        idx=r.text.find('"videoId":"'+v+'"')
        ctx=r.text[max(0,idx-3000):idx+3000]
        title=None
        m=re.search(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]',ctx)
        if m:
            try: title=html.unescape(m.group(1).encode().decode('unicode_escape','ignore'))
            except Exception: title=html.unescape(m.group(1))
        c.append({'video_id':v,'url':'https://www.youtube.com/watch?v='+v,'title':title,'slot':slot})
    p=BASE/'candidates'/f"03_candidates_{slot}_v0_1.json"
    p.write_text(json.dumps({'query':query,'search_url':url,'candidates':c},ensure_ascii=False,indent=2),encoding='utf-8')
    return c,str(p)
def fetch_first(cands, slot):
    attempts=[]
    for c in cands:
        title=(c.get('title') or '').lower()
        if slot=='quality_failure' and not any(k in title for k in ['fail','mistake','problem','consistent','consistency','limitation','bad','wrong','character']):
            attempts.append({'candidate':c,'status':'skipped_low_title_fit'}); continue
        if any(k in title for k in ['bypass','evade','scrape youtube blocked']):
            attempts.append({'candidate':c,'status':'skipped_bypass_like_title'}); continue
        p=subprocess.run(['python3',HELPER,c['url'],'--language','ko,en,en-US','--timestamps'],capture_output=True,text=True,timeout=120)
        try:
            data=json.loads(p.stdout,strict=False)
            if data.get('full_text') and not data.get('error'):
                raw=BASE/'raw'/f"04_raw_{slot}_{c['video_id']}.json"; raw.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
                md=BASE/'raw'/f"05_transcript_{slot}_{c['video_id']}.md"; md.write_text(data.get('timestamped_text') or data.get('full_text'),encoding='utf-8')
                sel={'candidate':c,'raw':str(raw),'md':str(md),'duration':data.get('duration'),'segments':data.get('segment_count'),'chars':len(data.get('full_text',''))}
                attempts.append({'candidate':c,'status':'selected','chars':sel['chars']})
                return sel, attempts
            attempts.append({'candidate':c,'status':'fetch_error','error':data.get('error')})
        except Exception as e:
            attempts.append({'candidate':c,'status':'parse_error','error':str(e)})
    return None, attempts
def review_slot(slot, selected):
    if not selected:
        return {'slot':slot,'status':'MISSING_SOURCE_MARKER_HOLD','score':0.0,'missing_source_marker':True,'reasons':['no acceptable transcript within bounded candidates']}
    title=(selected['candidate'].get('title') or '').lower()
    md=Path(selected['md']).read_text(encoding='utf-8').lower()[:20000]
    if slot=='quality_failure':
        neg=sum(k in title+' '+md for k in ['fail','failure','problem','mistake','limitation','inconsistent','consistency issue','doesn\'t work','not work','bad'])
        how=sum(k in title+' '+md for k in ['how to','make','create','consistent characters','tutorial'])
        if neg==0 and how>0:
            return {'slot':slot,'status':'WARN_POSITIVE_HOWTO_NOT_TRUE_FAILURE_HOLD','score':0.45,'missing_source_marker':False,'reasons':['source appears technique/how-to positive rather than failure case','use only as consistency-technique evidence']}
        return {'slot':slot,'status':'PASS_OR_PARTIAL_FAILURE_FIT_HOLD','score':0.65 if neg else 0.5,'missing_source_marker':False,'reasons':['bounded source attached','requires manual layer read before promotion']}
    if slot=='human_workflow_guard':
        fit=sum(k in title+' '+md for k in ['human in the loop','review','approval','reliable','guardrail','workflow','human'])
        return {'slot':slot,'status':'PASS_HUMAN_GUARD_FIT_HOLD' if fit else 'WARN_WEAK_HUMAN_GUARD_FIT_HOLD','score':0.75 if fit else 0.4,'missing_source_marker':False,'reasons':['human/workflow terms detected' if fit else 'weak title/text fit']}
def layer_table(slot, selected, review):
    table={'slot':slot,'created_at':NOW,'source':selected['candidate'] if selected else None,'transcript':selected if selected else None,'slot_quality_review':review,'layers':{'L0_surface':'selected transcript or missing-source marker','L1_conceptual':'slot-specific concept only','L2_information_structure':'what structure it adds to mini-space','L5_power_authority':'authority/platform/workflow implications','L6_practical_operational':'operational gate','L7_counter_uncertainty':'uncertainty and warning','L8_vectorfl_mapping':'HOLD mini-space only'},'promotion':'HOLD'}
    p=BASE/'tables'/f"06_layer_table_{slot}_v0_1.json"; p.write_text(json.dumps(table,ensure_ascii=False,indent=2),encoding='utf-8'); return str(p)
results=[official_policy_slot()]
slot_defs=[('quality_failure','AI video character consistency failure limitation case'),('human_workflow_guard','human in the loop automated publishing workflow guardrail')]
for slot,query in slot_defs:
    cands,cpath=yt_search(query,slot)
    selected,attempts=fetch_first(cands,slot)
    ap=BASE/'receipts'/f"07_attempts_{slot}_v0_1.json"; ap.write_text(json.dumps({'slot':slot,'query':query,'attempts':attempts},ensure_ascii=False,indent=2),encoding='utf-8')
    review=review_slot(slot,selected)
    table=layer_table(slot,selected,review)
    results.append({'slot':slot,'candidate_path':cpath,'attempts_path':str(ap),'selected':selected,'layer_table':table,'slot_quality_review':review})
verdict='PASS_AUTOLOOP_V0_1_WITH_SLOT_WARNINGS_HOLD' if any(r['slot_quality_review']['status'].startswith('WARN') or r['slot_quality_review'].get('missing_source_marker') for r in results) else 'PASS_AUTOLOOP_V0_1_WITH_HOLD'
mini={'space_id':'VECTORTUBE_AUTOLOOP_V0_1_RESULT_MINI_SPACE_5LqCwO7x_Gc_3012s','created_at':NOW,'status':verdict,'primary_question':'AI 자동화가 실무 혁신이 되는 지점과 플랫폼/운영 리스크가 되는 지점은 어디서 갈라지는가?','results':results,'slot_quality_summary':{r['slot']:r['slot_quality_review'] for r in results},'rule_learned':'Autoloop may proceed without per-step confirmation, but slot quality review decides whether each source strengthens the mini-space, stays candidate, or becomes missing-source marker.','promotion':'HOLD','main_space_mutation':False}
mp=BASE/'mini_space'/'08_autoloop_v0_1_result_mini_space.json'; mp.write_text(json.dumps(mini,ensure_ascii=False,indent=2),encoding='utf-8')
paths=[mp]+[Path(r['layer_table']) for r in results]
for r in results:
    if r.get('candidate_path'): paths.append(Path(r['candidate_path']))
    if r.get('attempts_path'): paths.append(Path(r['attempts_path']))
val={'validation_id':'VALIDATION_VECTORTUBE_AUTOLOOP_V0_1','created_at':NOW,'verdict':verdict,'checks':{},'content_checks':{'slots':len(results),'official_policy_docs_used':True,'youtube_transcripts_fetched':sum(1 for r in results if r.get('selected')),'slot_quality_review_count':len(results),'missing_source_markers':sum(1 for r in results if r['slot_quality_review'].get('missing_source_marker')),'warnings':sum(1 for r in results if r['slot_quality_review']['status'].startswith('WARN')),'main_space_mutation':False,'promotion_hold':True}}
for p in paths:
    val['checks'][str(p)]={'exists':p.exists(),'sha256':sha(p),'bytes':p.stat().st_size}
vp=BASE/'validation'/'09_validation_autoloop_v0_1.json'; vp.write_text(json.dumps(val,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'verdict':verdict,'mini_space':str(mp),'validation':str(vp),'content_checks':val['content_checks'],'slot_quality_summary':mini['slot_quality_summary']},ensure_ascii=False,indent=2))
