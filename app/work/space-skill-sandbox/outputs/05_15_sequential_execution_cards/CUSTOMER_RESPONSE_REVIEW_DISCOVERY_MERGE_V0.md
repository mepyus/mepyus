# Customer Response Review Discovery Merge v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  CUSTOMER_RESPONSE_REVIEW_DISCOVERY_MERGE_COMPLETED_WITH_WATCH

Purpose:
  Search customer-response review material broadly and merge it with the existing 05-15 adapter criteria.

Boundary:
  Candidate-only.
  This is not workflow, schema, registry, ontology, baseline, automation, external dispatch, customer-service policy, legal advice, AGENTS.md instruction, SKILL.md, current-position update, or output_manifest update.

## 2. Sources searched

Primary sources:

- Intercom, customer support best practices:
  https://www.intercom.com/help/en/articles/198-our-best-practice-guide-to-customer-support
- Zendesk, communication guidelines for AI assistance:
  https://support.zendesk.com/hc/en-us/articles/9182110974746-Best-practices-for-creating-communication-guidelines-to-improve-AI-assistance
- BoldDesk, ticket triage framework:
  https://www.bolddesk.com/blogs/ticket-triage
- Better Business Bureau, complaint handling process:
  https://www.bbb.org/process-of-complaints-and-reviews/complaints
- Federal Trade Commission, returns/refunds/other resolutions:
  https://consumer.ftc.gov/articles/solving-problems-business-returns-refunds-and-other-resolutions
- Federal Trade Commission, Telemarketing Sales Rule guide:
  https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule

Secondary search themes:

```text
customer support response best practices
communication guidelines
ticket triage
priority / severity / SLA
escalation matrix
refund and return handling
complaint handling
privacy / account data / payment disclosure
```

## 3. Search findings

Customer response review is not one task.
It is a bundle of at least seven checks:

```text
1. Human tone:
   personal, clear, empathetic, not robotic

2. Issue acknowledgement:
   show the customer that the specific issue was understood

3. Accuracy and source:
   answer only from known policy, order state, product facts, or support record

4. Resolution path:
   tell the customer what happens next or what they need to do

5. Priority / SLA / ownership:
   identify urgency, impact, owner, and escalation trigger

6. Authority boundary:
   do not promise refunds, credits, legal outcomes, timelines, or technical fixes without authority

7. Privacy / public risk:
   avoid exposing personal data, account data, payment details, or complaint text that may become public
```

## 4. Existing 05-15 criteria that still apply

From `ADAPTER_CARD_FORMS_V0.md` and `ADAPTER_EXTERNAL_FRAMEWORK_MERGE_V0.md`:

```text
검수 결과
핵심 판단
주의할 점
빠진 근거/첨부
지금 하지 말 것
건드리는 범위
다음 한 동작
상황 유형
승인 주체/권한
실패한다면 이유
후속 확인
```

These still fit customer response review, but the customer-response case needs more domain-specific labels.

## 5. Customer Response Safety Card v0 candidate

Use for:
  customer email, support reply, refund response, complaint response, chat response, public review reply, customer-facing status update.

```text
검수 결과:

고객 이슈 요약:

응답 초안의 핵심 주장:

고객에게 말해도 되는 내용:

금지/위험한 주장:

빠진 정책/근거/첨부:

톤 점검:
  empathy / clarity / personalization / no blame / no robotic wording

우선순위/SLA/소유자:

승인 주체/권한:
  review / reply-ok / approval-needed / escalation-needed / execution-not-allowed

개인정보/계정/결제 리스크:

실패한다면 이유:

후속 확인:

다음 한 동작:
```

Placement:
  candidate-only

Recommended label in Korean:
  고객 응답 안전 검수 카드

## 6. When to use this card

Use it when at least one is true:

```text
refund, credit, billing, cancellation, or compensation is mentioned
customer is angry, confused, repeated, or threatening escalation
there is a missed SLA or possible SLA breach
the answer depends on policy, warranty, order state, or product facts
the response mentions account, payment, personal, or private data
the reply may be public, forwarded, screenshotted, or used in a complaint
the issue may need a manager, legal, finance, engineering, or product owner
```

Do not use it when:

```text
the message is a simple low-risk acknowledgement
there is no customer-impacting decision
plain chat can answer faster and clearer
```

## 7. Priority / escalation cues

Candidate-only triage cues:

```text
P0 / Critical:
  security breach, data loss, widespread outage, payment system failure, legal threat with credible basis

P1 / High:
  customer cannot complete core workflow, refund/billing dispute with deadline, repeated unresolved complaint, enterprise/VIP customer impact

P2 / Medium:
  individual issue with workaround, unclear policy request, delayed response risk, product defect report without broad outage

P3 / Low:
  how-to question, feature request, low-urgency clarification, general feedback
```

WATCH:
  User-provided urgency is evidence, not final priority.
  Priority should be checked against impact, urgency, customer tier, and policy.

HOLD:
  Do not create an official SLA matrix from this.
  Do not automate routing from this.

## 8. Authority boundary examples

```text
reply-ok:
  acknowledge issue
  ask for missing information
  point to existing public policy
  explain next step already allowed by policy

approval-needed:
  refund, credit, discount, cancellation exception
  public apology on behalf of company
  promise of resolution date
  account change
  legal/compliance statement

escalation-needed:
  security/privacy/payment issue
  customer threatens legal action
  repeated complaint after prior response
  SLA breach or near breach
  engineering/product defect with business impact

execution-not-allowed:
  process payment
  change account
  cancel subscription
  issue refund
  disclose private information
  admit liability
```

## 9. Tone and content checks

Use these as review criteria, not rigid scripts:

```text
acknowledge:
  Does the reply reflect the customer's specific issue?

empathy:
  Does it recognize frustration or inconvenience without over-apologizing or admitting liability?

clarity:
  Is the next step obvious?

personalization:
  Does it avoid stock/robotic wording?

accuracy:
  Is every factual claim supported by policy, order state, product fact, or ticket record?

scope:
  Does it avoid promising what the agent cannot approve?

privacy:
  Does it avoid unnecessary personal, account, payment, or complaint details?

follow-up:
  Does it say what will be checked, by whom, or by when if needed?
```

## 10. Synthetic stress test

Input:

```text
Customer message:
I was charged twice and your team ignored my last two emails.
If I don't get a full refund today, I'm posting screenshots everywhere and filing a complaint.

Draft reply:
Sorry about that. We will refund you today.
This was probably a billing glitch.
Please send your card number again so we can check.
```

Card execution:

```text
검수 결과:
  DO_NOT_SEND_ESCALATE

고객 이슈 요약:
  고객은 이중 청구, 미응답, 당일 환불 요구, 공개 게시 및 민원 가능성을 제기했다.

응답 초안의 핵심 주장:
  오늘 환불하겠다고 약속하고, billing glitch라고 추정하며, 카드번호 재전송을 요청한다.

고객에게 말해도 되는 내용:
  문의를 받았고 이중 청구 여부를 확인하겠다는 점.
  확인에 필요한 안전한 정보만 요청하겠다는 점.
  담당 팀에 우선 확인 요청을 넣겠다는 점.

금지/위험한 주장:
  오늘 환불 확정
  billing glitch라고 단정
  카드번호 재전송 요청
  회사 책임 또는 법적 판단으로 읽힐 수 있는 표현

빠진 정책/근거/첨부:
  환불 정책
  결제 조회 기준
  고객 본인확인 절차
  이중 청구 확인에 필요한 안전한 정보 목록
  환불 승인 권한자

톤 점검:
  empathy:
    부족함. 고객의 불편과 반복 미응답을 구체적으로 인정해야 한다.

  clarity:
    위험함. 안전한 확인 절차와 다음 확인 시점이 없다.

  personalization:
    낮음. 상황별 대응이 아니라 짧은 사과와 성급한 약속이다.

우선순위/SLA/소유자:
  P1 / High candidate.
  billing dispute + repeated unresolved complaint + public complaint threat.
  billing/support owner 확인 필요.

승인 주체/권한:
  escalation-needed.
  refund promise requires approval.

개인정보/계정/결제 리스크:
  높음.
  카드번호 재전송 요청은 금지해야 한다.

실패한다면 이유:
  무권한 환불 약속, 결제정보 요청, 원인 단정, 고객 불만 재점화.

후속 확인:
  안전한 결제 조회 절차로 이중 청구 여부 확인.
  환불 가능 여부와 승인자 확인.
  고객에게 확인 예상 시점 전달.

다음 한 동작:
  초안을 보내지 말고 billing/support owner에게 에스컬레이션한 뒤,
  안전한 확인 절차와 승인 전 표현으로 응답문을 다시 작성한다.
```

Result:
  PASS_WITH_WATCH

## 11. Revised safe reply draft candidate

This is a candidate wording example, not an approved company policy response.

```text
안녕하세요 [Name]님.

두 번 청구된 것으로 보이고, 이전 문의에도 답을 받지 못하셨다는 점 확인했습니다.
불편을 드린 점에 대해 먼저 사과드립니다.

지금 이중 청구 여부를 확인할 수 있도록 결제 담당 팀에 우선 확인 요청을 올리겠습니다.
보안을 위해 카드번호 전체는 보내지 마시고, 필요한 경우에는 안전한 확인 절차로 요청드리겠습니다.

확인 후 환불 가능 여부와 다음 조치를 안내드리겠습니다.
제가 먼저 확인 상황을 업데이트드리겠습니다.
```

WATCH:
  This draft still needs the company's actual policy, owner, SLA, and permitted wording.

HOLD:
  no refund promise
  no liability admission
  no payment data request
  no legal/compliance conclusion

## 12. Merge back into adapter system

Customer response review is strong enough to become a candidate card.

Recommendation:

```text
Create:
  CUSTOMER_RESPONSE_SAFETY_CARD_V0.md

But only as:
  sandbox-local candidate form

Do not:
  promote
  automate
  route tickets
  create SLA policy
  create official customer support policy
```

If created, it should be placed beside:

```text
ADAPTER_CARD_FORMS_V0.md
```

and linked as candidate-only.

## 13. Hard stop confirmation

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
no official customer-service policy
no refund/SLA/legal authority
```

`STATUS: CUSTOMER_RESPONSE_REVIEW_DISCOVERY_MERGE_COMPLETED_WITH_WATCH`
