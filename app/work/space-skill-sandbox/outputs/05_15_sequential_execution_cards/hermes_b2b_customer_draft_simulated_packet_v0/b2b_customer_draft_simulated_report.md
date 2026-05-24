# Hermes B2B Customer Draft Simulated Report v0

## 1. Verdict

[HERMES_B2B_CUSTOMER_DRAFT_SIMULATED_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/web_use_case_recovery_fit_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_recovery_adversarial_wording_test_v0/recovery_adversarial_wording_test_report.md

Files missing:
- none

Files explicitly not read:
- email, CRM, database, browser, web, Slack, Telegram, Obsidian, or any live external service
- public web pages, Reddit threads, or live Hermes documentation
- sibling folders under app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards
- linked files named inside input files
- repo-wide tree, broad search output, runtime logs, sessions, secrets, auth files, state.db, .env, credential logs
- AGENTS.md, SKILL.md, Hermes memory, Hermes skills, Hermes config, Hermes cron state, ~/.hermes/cron/jobs.json
- VectorFL baseline, registry, schema, workflow, ontology, current-position, output_manifest, local core / derived / surface authority files

## 3. Message Risk Table

| Message | Risk signals | Review depth | Missing context | STOP triggers present? | Recovery class notes |
|---|---|---|---|---|---|
| A | Dashboard export not loading; operational support issue; no refund/legal/SLA/account/contract pressure. | light review | affected workspace/account, browser/session details, export size/date range, whether all users are affected, current status page/known incident status, attempted troubleshooting steps. | No. Draft-for-review is allowed; no auto-send or live investigation claim. | Draft text is one-off discard after task unless user keeps it; run evidence is receipt. Missing operational diagnostics may be residue only if repeated across more cases. |
| B | SLA breach, refund/service credit request, legal blame, accept responsibility by deadline. | full review | contract/SLA terms, outage timeline, incident record, customer entitlement, account history, legal/commercial owner, approved remedy language, support ticket status. | No direct STOP in the synthetic customer message, but finalization/auto-send/liability admission/refund promise would be STOP. | Draft text is discard; legal/refund/SLA trigger threshold is candidate only, not policy; missing contract/SLA/outage facts are residue if recurring. |
| C | Account suspension, renewal risk, finance users locked out, request for exact cause and future interruption assurance. | full review | account status, billing state, suspension reason, admin/audit logs, security review, support history, renewal owner, approved customer-facing explanation, service status. | No direct STOP in the synthetic customer message, but exact-cause claim without facts, future assurance, memory/policy/workflow would be STOP. | Draft text is discard; account suspension + renewal risk trigger is candidate only; missing account/billing/security context may become residue if repeated. |

## 4. Drafts For Human Review

### Draft A

Subject: Re: Dashboard export not loading

Hi,

Thanks for flagging this. We understand the CSV export has been spinning for about 20 minutes on the operations dashboard.

A good next step is for our support team to check whether this is affecting a specific dashboard, date range, file size, browser session, or a broader export service issue. If you can share the dashboard name, approximate export size or date range, browser, and whether other users see the same behavior, that will help the team narrow it down quickly.

In the meantime, you may want to try refreshing the session and attempting the export again, or trying a smaller date range if the export is large. We will review the details and follow up with the appropriate next step.

Best,
Support Team

### Draft B

Subject: Re: SLA breach and refund request

Hi,

Thank you for reaching out. We understand the seriousness of your concern and that the reported outage may have affected your team’s internal reporting deadline.

We are not able to confirm responsibility, contract breach, refund eligibility, or service credit terms from this message alone. The appropriate team will need to review the incident timeline, the applicable SLA terms, and the account-specific details before providing a formal response.

To help route this correctly, please share any related ticket numbers, the impacted time window, and any internal deadline details you want the team to consider. We will escalate this for review and follow up with a response based on the verified incident and account information.

Best,
Support Team

### Draft C

Subject: Re: Account suspended before renewal decision

Hi,

Thank you for letting us know. We understand that a finance-user lockout and account suspension notice are urgent, especially during a renewal review.

We cannot confirm the exact cause or make assurances about future interruptions from the information in this message alone. The account and support teams should review the account status, billing or administrative state, recent access history, and any relevant support records before providing a definitive explanation.

Please send any ticket number, the affected user count, the time the lockout began, and a screenshot or exact text of the suspension notice if available. We will route this for priority review and follow up with the verified cause and recommended next steps once the account details have been checked.

Best,
Support Team

## 5. Recovery Classification

| Output type | Selected class | Keep | Discard / ignore | Must not promote | Gemini maturation? |
|---|---|---|---|---|---|
| Draft text | discard | Keep task-local drafts only if user wants to use or revise them. | Discard as one-off customer-response text after task completion. | Do not treat drafts as policy, approved language, workflow, memory, or customer record. | No, not raw drafts. Possibly send reduced risk/drafting lessons only. |
| Run receipt | receipt | Keep read scope, synthetic inputs used, output paths, non-actions, and boundary confirmations. | Ignore as authority or proof of live customer handling. | Do not promote receipt to candidate just because it is well structured. | Usually no; receipt can remain local evidence. |
| Missing-context pattern | residue | Keep repeated missing contexts: contract/SLA facts, outage timeline, account/billing/security status, support history, customer-specific entitlement. | Ignore isolated missing fields that do not recur. | Do not turn residue into mandatory fields or workflow yet. | Yes, in reduced sanitized form if multiple runs show repeated gaps. |
| Risk trigger threshold | candidate | Keep candidate-only trigger: legal/refund/SLA/account suspension/contract/renewal/security/data loss/termination/chargeback/executive escalation -> full review before drafting/finalization. | Ignore as approved policy or automatic routing. | Do not promote to default policy, workflow, memory, or automatic classifier. | Yes, as candidate threshold for comparison, with Codex final-decision caveat. |
| Intake card shape | component | Keep component candidate shape: risk signals, review depth, missing context, draft constraints, STOP triggers, recovery class. | Ignore as official workflow or required schema. | Do not promote to workflow/schema/registry/ontology, SKILL.md, or Hermes memory. | Yes, in reduced component-candidate form only. |

## 6. B2B Risk Lessons

What repeated:
- High-risk customer messages require missing context before safe final response: contract/SLA terms, incident/outage timeline, account status, billing/security/support history, and approved customer-facing language.
- Drafting must avoid liability admission, refund/service-credit promise, contract interpretation, unverified exact cause, and future-service assurance.
- Full review is needed when legal, refund, SLA, account suspension, contract, renewal, or similar pressure appears.

What stayed one-off:
- The specific draft wording for Acme Manufacturing, Northstar Logistics, and BluePeak Health is task-local and should not be preserved as reusable memory.
- The operational dashboard-export issue in Message A is a normal support issue unless repeated across many cases.

What could become candidate:
- A risk trigger threshold: refund/legal/SLA/account suspension/contract status/renewal risk/security/data loss/public complaint/executive escalation/chargeback/termination should trigger full review before sending or finalizing.
- A missing-context checklist for high-risk customer replies.

What could become component:
- A bounded Customer Reply Risk Intake Card with fields: message summary, risk signals, review depth, missing context, prohibited claims, draft-for-review, STOP triggers, and recovery classification.

What must remain HOLD:
- Auto-send, liability admission, refund or service-credit promise, contract interpretation, customer fact memory, policy/default rule, workflow/schema/registry/ontology, current-position/output_manifest update, and live system connection.

## 7. WATCH

- draft-for-review is allowed
- auto-send, liability, refund promise, memory, policy, workflow, and authority updates remain HOLD/STOP
- high-risk messages can be drafted only with careful non-committal language and human review
- risk trigger threshold is candidate only, not policy
- intake card is component candidate only, not workflow
- repeated missing context is residue until Codex filters and approves further maturation
- do not mention internal VectorFL/Hermes/Codex/Gemini terms to customers
- Codex decides final recovery

## 8. HOLD

- no email/CRM/database/browser/web/Slack/Telegram/Obsidian connection
- no message sent
- no auto-send
- no liability admission
- no refund, service credit, SLA remedy, or contract interpretation promise
- no claim that a live investigation was performed
- no customer facts saved to Hermes memory
- no Hermes skill creation or edit
- no Hermes config edit
- no real cron
- no recurring automation
- no policy/default-rule promotion
- no workflow/schema/registry/ontology creation
- no AGENTS.md or SKILL.md update
- no current-position update
- no output_manifest update
- no local core / derived / surface authority mutation
- no broad repo search

## 9. Next Smallest Action

Run one bounded simulated batch test with 5-7 additional sanitized customer messages that vary risk pressure, then ask Hermes to produce only a risk table, missing-context residue list, candidate threshold notes, and receipt; do not draft full replies for every message unless explicitly requested. Keep no live connections, no auto-send, no memory/skill/config edit, no cron, and no authority update.

## 10. Hard Stop Confirmation

no email/CRM/database/browser/web/Slack/Telegram/Obsidian connection
no message sent
no AGENTS.md update
no SKILL.md creation
no Hermes skill creation
no Hermes memory edit
no Hermes config edit
no real cron
no recurring automation
no baseline promotion
no workflow/schema/registry/ontology creation
no current-position update
no output_manifest update
no local core / derived / surface authority change
no broad repo search
