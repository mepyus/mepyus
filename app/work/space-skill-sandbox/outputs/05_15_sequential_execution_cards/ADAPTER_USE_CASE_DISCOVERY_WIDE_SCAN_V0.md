# Adapter Use Case Discovery Wide Scan v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  ADAPTER_USE_CASE_DISCOVERY_WIDE_SCAN_COMPLETED_WITH_WATCH

Purpose:
  Search broadly for AI / GenAI / agent use cases beyond blog auto-generation and shorts automation, then translate them into possible VectorFL adapter-test surfaces.

Boundary:
  This is a discovery map, not a registry, workflow, schema, ontology, baseline, product roadmap, automation plan, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Search basis

Sources consulted:

- Google Cloud, generative AI / agent platform and enterprise use-case material:
  https://cloud.google.com/ai/generative-ai
- McKinsey, generative AI economic potential:
  https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
- Deloitte, AI Dossier / 80+ AI use cases:
  https://www.deloitte.com/global/en/issues/generative-ai/ai-use-cases.html
- IBM, AI business use cases:
  https://www.ibm.com/blog/artificial-intelligence-use-cases/
- IBM, generative AI enterprise use cases:
  https://www.ibm.com/think/topics/generative-ai-use-cases
- Britannica Money, AI for small businesses:
  https://www.britannica.com/money/ai-solutions-for-small-business
- Microsoft HR Copilot case PDF:
  https://news.microsoft.com/wp-content/uploads/prod/sites/658/2024/05/How-Microsoft-is-reinventing-HR-with-Microsoft-Copilot.pdf
- Thomson Reuters, 2025 Generative AI in Professional Services Report:
  https://legal.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2025-generative-ai-in-professional-services-report-tr5433489-rgb.pdf
- TechTarget, generative AI use cases in supply chain:
  https://www.techtarget.com/searchERP/tip/Generative-AI-use-cases-in-supply-chain
- TechTarget, generative AI use cases in manufacturing:
  https://www.techtarget.com/searcherp/tip/Use-cases-for-generative-AI-in-manufacturing

Source-level reading:
  The broad market pattern is not "content automation only."
  Repeated use-case families include customer operations, sales, marketing, HR, finance, legal/compliance, project management, software engineering, IT operations, procurement, supply chain, manufacturing, training, knowledge management, research, reporting, and small-business admin.

## 3. Adapter translation rule

Every discovered use case should be lowered into one of these candidate card types before any real test:

```text
업무 문서 검수 카드:
  review a work artifact and produce risks, missing evidence, boundaries, and next action

외부도구 사용 전 점검 카드:
  draft a bounded packet before Codex/Gemini/CLI/API/browser/tool use

글 주장/근거 점검 카드:
  check source support, claim level, and overclaim risk

쇼츠 훅/주장 점검 카드:
  check hook, allowed claim, forbidden claim, and next cut

작업 파악 읽기 카드:
  compress a project/folder/process into a temporary reading guide

new card needed:
  only if none of the above can carry the use case without distortion
```

## 4. Wide use-case inventory

### A. Customer / service / support

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Customer inquiry triage | 업무 문서 검수 카드 | classify one synthetic support ticket |
| Support reply draft review | 업무 문서 검수 카드 | check reply for missing policy/source |
| Help-center answer grounding | 글 주장/근거 점검 카드 | check answer against provided FAQ |
| Call/chat summary | 업무 문서 검수 카드 | summarize one transcript with HOLD |
| Escalation detection | 업무 문서 검수 카드 | identify if human review needed |
| Complaint pattern clustering | 작업 파악 읽기 카드 | compress 5 complaints into themes |
| Customer sentiment summary | 작업 파악 읽기 카드 | summarize comments without decision |
| Refund/return response check | 업무 문서 검수 카드 | find approval/policy boundary |
| SLA risk review | 업무 문서 검수 카드 | flag deadline/owner gaps |
| Agent handoff packet | 외부도구 사용 전 점검 카드 | draft allowed/forbidden handoff packet |

### B. Sales / CRM / business development

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Lead research summary | 작업 파악 읽기 카드 | summarize one public company page |
| Sales email draft check | 업무 문서 검수 카드 | check overclaim and missing proof |
| Follow-up recommendation | 업무 문서 검수 카드 | produce next action only |
| Proposal outline | 글 주장/근거 점검 카드 | check claim level before drafting |
| CRM note cleanup | 업무 문서 검수 카드 | normalize one note without committing |
| Meeting prep brief | 작업 파악 읽기 카드 | create temporary prep guide |
| Objection response bank | 글 주장/근거 점검 카드 | check claims against product facts |
| Cross-sell talking points | 글 주장/근거 점검 카드 | mark support strength |
| Account-risk summary | 업무 문서 검수 카드 | identify missing owner/date/source |
| Deal handoff packet | 외부도구 사용 전 점검 카드 | draft packet for tool-assisted review |

### C. Marketing / content beyond blog and shorts

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Product description claim check | 글 주장/근거 점검 카드 | mark claim_level and evidence |
| Landing page copy review | 글 주장/근거 점검 카드 | flag overclaim and missing proof |
| Ad copy risk check | 쇼츠 훅/주장 점검 카드 | identify forbidden claims |
| Email campaign draft review | 업무 문서 검수 카드 | check audience/claim/CTA |
| Brand voice consistency check | 업무 문서 검수 카드 | compare one draft to guide |
| Social post queue review | 쇼츠 훅/주장 점검 카드 | test hook/claim/risk |
| FAQ expansion | 글 주장/근거 점검 카드 | source-backed answer check |
| Case study outline | 글 주장/근거 점검 카드 | separate evidence from narrative |
| Webinar abstract | 글 주장/근거 점검 카드 | check promise vs evidence |
| Content repurposing | 작업 파악 읽기 카드 | map source to derivative formats |

### D. HR / people operations / recruiting

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Job description review | 업무 문서 검수 카드 | check missing requirements/approval |
| Candidate communication draft | 업무 문서 검수 카드 | check fairness/confidentiality boundary |
| Interview guide outline | 업무 문서 검수 카드 | flag role/source gaps |
| Resume screen rubric check | 업무 문서 검수 카드 | do not decide, check criteria only |
| HR policy Q&A grounding | 글 주장/근거 점검 카드 | answer only from provided policy |
| Onboarding reading guide | 작업 파악 읽기 카드 | temporary guide for one role |
| Training material outline | 글 주장/근거 점검 카드 | check source coverage |
| Employee support case summary | 업무 문서 검수 카드 | summarize without HR decision |
| Headcount/recruiting report narrative | 업무 문서 검수 카드 | check missing metric/source |
| HR automation intake | 외부도구 사용 전 점검 카드 | packet draft only |

### E. Finance / accounting / audit / risk

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Invoice anomaly explanation | 업무 문서 검수 카드 | flag mismatch; no payment action |
| Receipt categorization review | 업무 문서 검수 카드 | check category confidence |
| Monthly financial commentary | 글 주장/근거 점검 카드 | require metric/source |
| Budget variance summary | 업무 문서 검수 카드 | identify driver and missing evidence |
| Audit finding draft | 업무 문서 검수 카드 | check evidence and scope |
| Risk assessment report summary | 업무 문서 검수 카드 | separate finding from recommendation |
| Policy compliance check | 업무 문서 검수 카드 | flag missing policy reference |
| Financial statement filling support | 외부도구 사용 전 점검 카드 | pre-use packet; no filing |
| Fraud pattern note | 작업 파악 읽기 카드 | theme-only, no accusation |
| FinOps cloud spend summary | 업무 문서 검수 카드 | check cost driver/source |

### F. Legal / compliance / procurement contracts

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Contract clause summary | 업무 문서 검수 카드 | summarize clause with legal HOLD |
| Contract risk checklist | 업무 문서 검수 카드 | flag risk, no legal advice |
| NDA term extraction | 업무 문서 검수 카드 | extract parties/date/term only |
| Renewal deadline extraction | 업무 문서 검수 카드 | identify dates, require verification |
| Policy compliance review | 업무 문서 검수 카드 | map draft to policy source |
| Legal memo source check | 글 주장/근거 점검 카드 | evidence/source coverage only |
| Vendor agreement comparison | 업무 문서 검수 카드 | compare material differences |
| Procurement approval packet | 외부도구 사용 전 점검 카드 | draft allowed/forbidden scope |
| Regulatory update digest | 작업 파악 읽기 카드 | reading guide, no compliance decision |
| Due diligence document triage | 업무 문서 검수 카드 | classify missing docs and red flags |

### G. Project management / operations

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Meeting summary with action items | 업무 문서 검수 카드 | owner/date/source check |
| Project status report review | 업무 문서 검수 카드 | flag missing metric or blocker |
| Risk register draft | 업무 문서 검수 카드 | convert issues into risk candidates |
| Task decomposition | 업무 문서 검수 카드 | next action only, no assignment system |
| Timeline feasibility check | 업무 문서 검수 카드 | identify dependency gaps |
| Resource planning note | 업무 문서 검수 카드 | flag assumptions |
| Postmortem summary | 작업 파악 읽기 카드 | compress causes and next checks |
| SOP draft review | 업무 문서 검수 카드 | check owner, trigger, exception |
| Change announcement review | 업무 문서 검수 카드 | check audience and rollout boundary |
| Workflow tool packet | 외부도구 사용 전 점검 카드 | draft only; no tool execution |

### H. Software / IT / security

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Code review return check | 업무 문서 검수 카드 | check claim/evidence/boundary |
| AI-generated code verification plan | 외부도구 사용 전 점검 카드 | packet for tests, no execution by default |
| Bug report triage | 업무 문서 검수 카드 | clarify repro/impact/next |
| Release note draft review | 글 주장/근거 점검 카드 | check source commits/issues |
| Incident summary | 작업 파악 읽기 카드 | timeline and unresolved risk |
| Runbook review | 업무 문서 검수 카드 | check trigger/owner/hard stop |
| Security alert explanation | 업무 문서 검수 카드 | no remediation without approval |
| Dependency update plan | 외부도구 사용 전 점검 카드 | allowed/forbidden commands |
| API integration packet | 외부도구 사용 전 점검 카드 | credential/account/browser HOLD |
| Legacy code modernization brief | 작업 파악 읽기 카드 | temporary map, no refactor approval |

### I. Supply chain / procurement / manufacturing

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Supplier bid comparison | 업무 문서 검수 카드 | compare criteria and missing data |
| Supplier risk note | 업무 문서 검수 카드 | flag dependency and evidence |
| Inventory exception explanation | 업무 문서 검수 카드 | identify stock/cost tradeoff |
| Demand forecast narrative check | 글 주장/근거 점검 카드 | require forecast assumptions |
| Logistics route explanation | 업무 문서 검수 카드 | no routing action |
| Procurement negotiation prep | 작업 파악 읽기 카드 | brief only |
| Purchase request review | 업무 문서 검수 카드 | owner, budget, approval boundary |
| Quality defect report summary | 업무 문서 검수 카드 | issue/evidence/next check |
| Maintenance alert explanation | 업무 문서 검수 카드 | no equipment action |
| Training guide for shop-floor role | 작업 파악 읽기 카드 | temporary guide only |

### J. Research / analysis / knowledge management

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Literature/source scan | 글 주장/근거 점검 카드 | source coverage visible |
| Competitive research brief | 작업 파악 읽기 카드 | claim/evidence separation |
| Market trend digest | 글 주장/근거 점검 카드 | no strategic decision |
| Internal knowledge Q&A | 글 주장/근거 점검 카드 | answer from provided docs only |
| Document summarization | 업무 문서 검수 카드 | missing evidence and next action |
| Decision memo review | 업무 문서 검수 카드 | check options/risks/assumptions |
| Data narrative explanation | 글 주장/근거 점검 카드 | source/metric confidence |
| Report-to-slide compression | 작업 파악 읽기 카드 | outline only |
| Research handoff packet | 외부도구 사용 전 점검 카드 | bounded tool query |
| Synthetic scenario generation | 업무 문서 검수 카드 | label as synthetic/candidate |

### K. Education / training / coaching

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Lesson outline review | 글 주장/근거 점검 카드 | learning goal/source check |
| Training quiz draft check | 업무 문서 검수 카드 | answer key/source check |
| Role-specific job aid | 작업 파악 읽기 카드 | temporary guide |
| Personalized learning path | 업무 문서 검수 카드 | no HR decision |
| Scenario practice script | 쇼츠 훅/주장 점검 카드 | claim/risk/narrative check |
| Rubric drafting | 업무 문서 검수 카드 | criteria and bias check |
| Course content update digest | 작업 파악 읽기 카드 | source update summary |
| Coaching note rewrite | 업무 문서 검수 카드 | confidentiality/tone boundary |
| Knowledge check summary | 업무 문서 검수 카드 | no performance decision |
| Training feedback clustering | 작업 파악 읽기 카드 | themes only |

### L. Personal / solo / small-business operations

| Use case | Adapter test surface | First safe test |
| --- | --- | --- |
| Inbox reply review | 업무 문서 검수 카드 | clarify tone/risk/next |
| Calendar/meeting prep | 작업 파악 읽기 카드 | temporary prep guide |
| Personal decision memo | 업무 문서 검수 카드 | options/risks/next |
| Small-business FAQ reply | 업무 문서 검수 카드 | missing policy/source |
| Product listing review | 글 주장/근거 점검 카드 | claim and evidence |
| Invoice follow-up draft | 업무 문서 검수 카드 | no payment/account action |
| Hiring post review | 업무 문서 검수 카드 | requirements/fairness boundary |
| Local service quote comparison | 업무 문서 검수 카드 | criteria/missing info |
| Customer DM triage | 업무 문서 검수 카드 | classify and next action |
| Weekly business summary | 작업 파악 읽기 카드 | compression only |

## 5. Candidate clusters for VectorFL

The discovered use cases collapse into eight practical adapter clusters:

```text
1. Work artifact review:
   documents, emails, reports, replies, memos, policies, SOPs

2. Claim/evidence review:
   blogs, product pages, sales claims, research claims, financial commentary

3. Tool pre-use governance:
   Codex, Gemini, CLI, API, browser, CRM, HRIS, finance tools

4. Temporary reading/onboarding:
   project folders, role guides, meeting prep, incident/postmortem compression

5. Customer-facing response safety:
   support replies, refunds, complaints, FAQs, service handoffs

6. Decision-support without decision authority:
   finance variance, supplier comparison, risk summary, hiring criteria

7. Operational exception review:
   bugs, incidents, inventory exceptions, quality defects, SLA risk

8. Creative planning with claim boundaries:
   shorts, ads, social posts, webinars, scripts, training scenarios
```

## 6. New adapter cards possibly needed

Most use cases fit the five existing cards.
However, three repeated clusters may deserve future candidate cards if real tests repeat:

```text
Customer Response Safety Card:
  support/customer-facing replies with policy, tone, disclosure, escalation boundary

Decision Memo Review Card:
  options, evidence, risk, owner, decision boundary, next check

Operational Exception Triage Card:
  incident/bug/inventory/quality exception with severity, owner, evidence, next action
```

Do not create these as official cards yet.
Only create them if repeated real tests show that the existing `업무 문서 검수 카드` becomes too broad.

## 7. Highest-value next tests

Recommended test order:

```text
1. Customer-facing reply review
   reason:
     high practical value, clear risk, uses existing 업무 문서 검수 카드

2. Codex result verification
   reason:
     directly useful in this workspace, pairs with 외부도구 사용 전 점검 카드

3. Decision memo review
   reason:
     generalizes across company, personal, product, and finance decisions

4. Support ticket triage
   reason:
     common business use case, can test escalation boundaries

5. Meeting summary/action-item review
   reason:
     low-risk, common, good for owner/date/source checks
```

## 8. Readiness assessment

```text
ready for sandbox-local real-input test:
  customer-facing reply review
  Codex result verification
  meeting/action-item review
  document/memo review
  decision memo review

ready for claim-only test:
  product page copy
  blog outline
  sales email
  ad/social/shorts script

ready only as temporary guide:
  onboarding
  project/folder handoff
  incident/postmortem compression

not ready for automation:
  customer support automation
  HR screening decisions
  finance/accounting actions
  legal/compliance decisions
  procurement execution
  platform publishing
  browser/API/credential/account actions
```

## 9. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
```

`STATUS: ADAPTER_USE_CASE_DISCOVERY_WIDE_SCAN_COMPLETED_WITH_WATCH`
