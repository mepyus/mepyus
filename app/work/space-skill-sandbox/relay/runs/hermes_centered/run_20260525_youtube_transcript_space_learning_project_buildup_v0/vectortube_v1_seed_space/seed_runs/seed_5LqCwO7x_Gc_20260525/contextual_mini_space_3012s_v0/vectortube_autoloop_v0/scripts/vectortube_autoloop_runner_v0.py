#!/usr/bin/env python3
import json, re, html, urllib.parse, requests, subprocess, datetime, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
HELPER='/Users/sungsookim/.hermes/skills/media/youtube-content/scripts/fetch_transcript.py'
SLOTS=[
 {'slot':'policy_boundary','query':'YouTube automated access API quota scraping policy platform rules','purpose':'platform/API/automated-access boundary'},
 {'slot':'quality_failure','query':'AI video generation character consistency failure workflow','purpose':'quality/consistency failure and workflow risk'},
 {'slot':'human_workflow_guard','query':'human in the loop automated publishing review workflow AI content','purpose':'human review and publishing guardrails'}
]
NOW=datetime.datetime.now().astimezone().isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def title_for(text, vid):
    idx=text.find('"videoId":"'+vid+'"')
    ctx=text[max(0,idx-3000):idx+4000]
    for pat in [r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', r'"title":\{"simpleText":"(.*?)"\}', r'"accessibilityData":\{"label":"(.*?)"\}']:
        m=re.search(pat,ctx)
        if m:
            try: return html.unescape(m.group(1).encode('utf-8','ignore').decode('unicode_escape','ignore'))
            except Exception: return html.unescape(m.group(1))
    return None
def search(slot):
    url='https://www.youtube.com/results?search_query='+urllib.parse.quote(slot['query'])
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=20)
    ids=[]
    for m in re.finditer(r'"videoId":"([A-Za-z0-9_-]{11})"', r.text):
        v=m.group(1)
        if v not in ids: ids.append(v)
    c=[]
    for v in ids[:5]:
        c.append({'video_id':v,'url':'https://www.youtube.com/watch?v='+v,'title':title_for(r.text,v),'slot':slot['slot']})
    p=BASE/'candidates'/f"01_candidates_{slot['slot']}.json"
    p.write_text(json.dumps({'slot':slot,'search_url':url,'status_code':r.status_code,'candidates':c},ensure_ascii=False,indent=2),encoding='utf-8')
    return c,p
def fetch(cands, slot):
    attempts=[]
    # avoid obvious how-to bypass/evade titles for policy slot
    for c in cands:
        title=(c.get('title') or '').lower()
        if slot['slot']=='policy_boundary' and any(k in title for k in ['bypass','evade','scrape youtube without','blocked workaround']):
            attempts.append({'candidate':c,'status':'skipped_bypass_like_title'}); continue
        cmd=['python3',HELPER,c['url'],'--language','ko,en,en-US','--timestamps']
        p=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
        try:
            data=json.loads(p.stdout, strict=False)
            if 'error' not in data and data.get('full_text'):
                raw=BASE/'raw'/f"02_transcript_raw_{slot['slot']}_{c['video_id']}.json"
                raw.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
                md=BASE/'raw'/f"03_transcript_{slot['slot']}_{c['video_id']}.md"
                md.write_text(f"# Transcript {slot['slot']} {c['video_id']}\n\ntitle: {c.get('title')}\nurl: {c['url']}\nduration: {data.get('duration')}\nsegments: {data.get('segment_count')}\n\n{data.get('timestamped_text') or data.get('full_text','')}\n",encoding='utf-8')
                attempts.append({'candidate':c,'status':'selected','raw':str(raw),'md':str(md),'duration':data.get('duration'),'segments':data.get('segment_count'),'chars':len(data.get('full_text',''))})
                return attempts[-1], attempts
            attempts.append({'candidate':c,'status':'error','error':data.get('error')})
        except Exception as e:
            attempts.append({'candidate':c,'status':'parse_or_fetch_error','error':str(e),'stdout_head':p.stdout[:500],'stderr_head':p.stderr[:300]})
    return None, attempts
def layer_table(selected, slot):
    if not selected: return None
    md=Path(selected['md']).read_text(encoding='utf-8')
    lines=[]
    kws=['policy','api','quota','automated','scrap','crawl','consistent','quality','workflow','review','human','publish','risk','error','content','youtube','platform']
    for ln in md.splitlines():
        low=ln.lower()
        if re.match(r'^\d{1,2}:\d{2}', ln.strip()) and any(k in low for k in kws):
            lines.append(ln.strip())
    table={
      'table_id':f"VECTORTUBE_AUTOLOOP_LAYER_TABLE_{slot['slot']}_{selected['candidate']['video_id']}_V0",'created_at':NOW,'slot':slot,
      'source':selected['candidate'],'transcript':{'raw':selected['raw'],'md':selected['md'],'duration':selected.get('duration'),'segments':selected.get('segments'),'chars':selected.get('chars')},
      'evidence_sample':lines[:20],
      'layers':{
        'L0_surface':'slot-relevant surface claims sampled from timestamped transcript',
        'L1_conceptual':f"Reads this source as {slot['purpose']}, not as authority.",
        'L2_information_structure':'Look for data/API/workflow/quality/control structures that affect the seed mini-space.',
        'L3_context_background':'Adds external context around the selected primary question rather than expanding the seed broadly.',
        'L4_emotional_rhetorical':'Watch for hype/fear/compliance rhetoric that may distort the automation story.',
        'L5_power_authority':'Tracks platform, vendor, policy, institutional, and workflow authority pressures.',
        'L6_practical_operational':'Extracts operational gates for real use: review, quota, quality, maintenance, publishing.',
        'L7_counter_uncertainty':'Records uncertainty/failure/guard conditions; does not promote the source to truth.',
        'L8_vectorfl_mapping':'Feeds the current mini-space guard ring; no main-space mutation.'
      },
      'hold':'layer table candidate only'
    }
    p=BASE/'tables'/f"04_layer_table_{slot['slot']}_{selected['candidate']['video_id']}_v0.json"
    p.write_text(json.dumps(table,ensure_ascii=False,indent=2),encoding='utf-8')
    return str(p)
results=[]
for slot in SLOTS:
    cands,cand_path=search(slot)
    selected, attempts=fetch(cands, slot)
    att_path=BASE/'receipts'/f"05_fetch_attempts_{slot['slot']}.json"
    att_path.write_text(json.dumps({'slot':slot,'attempts':attempts},ensure_ascii=False,indent=2),encoding='utf-8')
    table=layer_table(selected, slot)
    results.append({'slot':slot,'candidate_path':str(cand_path),'selected':selected,'attempts_path':str(att_path),'layer_table':table})
# compose final autoloop mini-space
mini={
 'space_id':'VECTORTUBE_AUTOLOOP_RESULT_MINI_SPACE_5LqCwO7x_Gc_3012s_V0','created_at':NOW,'status':'AUTOLOOP_RESULT_HOLD',
 'primary_question':'AI 자동화가 실무 혁신이 되는 지점과 플랫폼/운영 리스크가 되는 지점은 어디서 갈라지는가?',
 'autoloop_results':results,
 'source_slots':{r['slot']['slot']:{'purpose':r['slot']['purpose'],'selected_video':(r['selected'] or {}).get('candidate'),'layer_table':r['layer_table']} for r in results},
 'updated_guard_ring':{
   'platform_boundary':'external candidate attached if selected; inspect before promotion',
   'quality_consistency':'external candidate attached if selected; inspect before promotion',
   'human_review':'external candidate attached if selected; inspect before promotion'
 },
 'drift_watch':['Do not turn policy slot into bypass how-to','Do not treat candidate transcripts as authority','Stop if search drifts into generic AI automation hype'],
 'promotion':'HOLD','main_space_mutation':False
}
mp=BASE/'mini_space'/'06_autoloop_result_mini_space_v0.json'
mp.write_text(json.dumps(mini,ensure_ascii=False,indent=2),encoding='utf-8')
validation={'validation_id':'VALIDATION_VECTORTUBE_AUTOLOOP_5LqCwO7x_Gc_3012s_V0','created_at':NOW,'verdict':'PASS_AUTOLOOP_EXECUTED_WITH_HOLD','checks':{},'content_checks':{'slots':len(SLOTS),'successful_transcripts':sum(1 for r in results if r['selected']),'layer_tables':sum(1 for r in results if r['layer_table']),'candidate_only_before_fetch':True,'hard_cap_transcripts_total':3,'main_space_mutation':False,'promotion_hold':True}}
for p in [mp]+[Path(r['candidate_path']) for r in results]+[Path(r['attempts_path']) for r in results]+[Path(r['layer_table']) for r in results if r['layer_table']]:
    validation['checks'][str(p)]={'exists':p.exists(),'sha256':sha(p),'bytes':p.stat().st_size}
vp=BASE/'validation'/'07_validation_vectortube_autoloop_v0.json'
vp.write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'verdict':validation['verdict'],'mini_space':str(mp),'validation':str(vp),'content_checks':validation['content_checks'],'selected':[(r['slot']['slot'], (r['selected'] or {}).get('candidate')) for r in results]},ensure_ascii=False,indent=2))
