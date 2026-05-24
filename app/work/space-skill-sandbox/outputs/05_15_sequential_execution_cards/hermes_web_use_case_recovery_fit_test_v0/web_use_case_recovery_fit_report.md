# Hermes Web Use-Case Recovery Fit Report v0

## 1. Verdict

[HERMES_WEB_USE_CASE_RECOVERY_FIT_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_execution_to_space_recovery_gate_buildup_v0/execution_to_space_recovery_gate_buildup.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/real_artifact_recovery_classification_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_recovery_adversarial_wording_test_v0/recovery_adversarial_wording_test_report.md

Files missing:
- none

Files explicitly not read:
- public web pages and Reddit threads named by Codex; Codex already summarized them in the prompt
- sibling folders under app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards
- linked files named inside input files
- repo-wide tree, broad search output, runtime logs, sessions, secrets, auth files, state.db, .env, credential logs
- AGENTS.md, SKILL.md, Hermes memory, Hermes skills, Hermes config, Hermes cron state, ~/.hermes/cron/jobs.json
- VectorFL baseline, registry, schema, workflow, ontology, current-position, output_manifest, local core / derived / surface authority files

## 3. External Use-Case Families Considered

- A Morning brief cron
- B Email / customer reply drafting
- C Database assistance
- D Deeper web exploration with documented data points
- E Skill / toolset audit
- F Obsidian / notes output sink

## 4. Scenario Fit Table

| Scenario | Safe Hermes task shape | Required Codex packet | Future allowed tools | Forbidden actions | Hermes return contract | Likely recovery classes | Gemini maturation? | STOP triggers |
|---|---|---|---|---|---|---|---|---|
| A Morning brief cron | Start as one-shot/manual-trigger brief over explicit source list or previously captured local inputs; no real cron until separate approval. If later automated, prefer no-agent script and fresh-session self-contained prompt. | Explicit sources, allowed date range, summary length, delivery target candidate, output path, non-goals, no-persistence rule, STOP conditions, report/receipt shape. | Future only after approval: web/search or feed fetcher, terminal/file for deterministic script, cronjob only after pre-cron review, local delivery. | No real cron now; no recurring automation; no live delivery setup; no memory/skill/config edit; no broad web crawl; no auto-ingest into Space. | Brief, source list/citations, what was checked/not checked, receipt, errors, WATCH/HOLD, recovery recommendation. | task output = discard or residue; run evidence = receipt; recurring source/brief pattern = candidate; no-agent brief packet = component only after review; real cron pressure = STOP. | Yes, only reduced recurring information needs or source-cluster patterns; not raw daily briefs. | create cron now, run daily automatically, deliver to live platform without approval, save as memory/default, use prior brief success as authority. |
| B Email/customer draft | One-shot review/drafting over explicit sanitized email/customer context; draft for human review only; separate risk classification from reply text. | Sanitized message(s), customer context, contract/refund/SLA/account status if available, allowed tone, prohibited claims, review depth, send/no-send boundary, output path. | Future only after approval: email read-only/exported local files, file, terminal for local transforms; no send tool unless separately approved. | No live email connection now; no automatic sending; no mailbox monitoring; no customer data memory; no CRM/database mutation; no legal/policy finalization. | Draft(s), risk flags, missing context, read/write scope, receipt, WATCH/HOLD, suggested recovery class. | one-off draft = discard; receipt = receipt; repeated missing context = residue; risk thresholds = candidate; intake card = component; automatic sending/policy/memory = STOP. | Yes, for batches of sanitized residue/candidate risk patterns; not raw customer emails. | auto-send, default response policy, save customer facts to memory, monitor inbox continuously, use legal/refund/SLA/account suspension without review. |
| C Database assistance | Query drafting or analysis over explicit schema/sample snippets; read-only by default; live DB access requires separate bounded packet and credentials never exposed. | Database purpose, schema excerpt, sample rows if safe, question, read-only/mutation boundary, allowed SQL dialect, credential exclusion, output path, rollback/STOP rules if ever live. | Future only after approval: file/code execution for local samples, database client in read-only sandbox, terminal for static query linting. | No live DB now; no credentials/secrets; no writes/migrations/deletes; no broad data dump; no production connection; no hidden persistence. | Proposed query, assumptions, safety notes, schema/context used, result interpretation if local sample given, receipt, non-actions, WATCH/HOLD. | query draft = candidate; run evidence = receipt; repeated schema/context gaps = residue; reusable query template/checklist = component; live mutation/credential use = STOP. | Yes, for abstracted query patterns or schema-context packet requirements; not raw private data. | connect to production, update/delete/migrate, read secrets, store credentials, make query default automation, exfiltrate broad tables. |
| D Web exploration | Bounded research packet over explicit allowed source list, search query list, max source count, and citation requirements; reduce findings before recovery. | Research question, approved sources/search terms, source cap, date scope, citation format, output path, exclusion list, confidence labels, recovery target. | Future only after approval: web/search/browser with tight source cap, file for report, maybe terminal for citation formatting. | No web/browser now; no open-ended browsing; no broad repo search; no unbounded scraping; no raw output bulk ingestion; no memory write. | Findings table, citations/URLs, data point provenance, uncertainties, excluded sources, receipt, WATCH/HOLD, reduced candidate/residue packet. | raw findings = residue; source/citation receipt = receipt; repeated pattern/threshold = candidate; research packet template = component; official update claim = STOP. | Yes, reduced cited data points and pattern candidates are suitable for Gemini comparison. | browse whole web, treat findings as authority, update current surface/baseline, save as memory, automate recurring crawl. |
| E Skill/toolset audit | Design-only audit over an explicit exported skill/tool inventory supplied by Codex/User; proposals only, no direct ~/.hermes reads or edits. | Explicit inventory file(s), audit goal, keep/remove criteria, no-edit boundary, output path, proposal-only wording, review owner. | Future only after approval: file reads of exported inventory, terminal for local counts, maybe Hermes CLI only if specifically allowed and non-mutating. | No ~/.hermes read now; no skill edit/create/delete; no config/toolset changes; no memory edit; no broad search; no curator/cron mutation. | Audit findings, proposed keep/merge/archive list, evidence, risk notes, receipt, explicit no-edits, Codex review recommendation. | audit report = candidate; tool inventory receipt = receipt; reusable audit checklist = component; config/skill changes = STOP or space_update_proposal if proposal only. | Maybe, for reduced audit heuristics across multiple audits; not full private skill contents. | edit skills/config, create SKILL.md, save procedure to memory, enable/disable toolsets, treat audit as authorization. |
| F Notes output sink | Local sandbox note-output simulation only; distinguish external note sink from VectorFL memory and from recovery-approved Space content. | Declared local output path, note naming, retention policy candidate, recovery boundary, what counts as receipt/residue/candidate, no external note connection. | Future only after approval: file write to approved local notes folder or Obsidian vault, no network; cron only after separate approval. | No Obsidian/external notes now; no real cron; no memory edit; no output_manifest/current-position update; no note accumulation as authority. | Note/report, receipt, source list, recovery class suggestions, explicit statement that note sink is not Space memory, WATCH/HOLD. | notes = task output/receipt/residue; repeated note pattern = candidate; note template = component; Space memory/update claim = STOP. | Yes, only filtered residue/candidates from notes batches, not the whole notes folder. | write to Obsidian now, treat notes as memory/authority, auto-sync daily, update Space/current-position/output_manifest, bulk-ingest notes. |

## 5. What Hermes Is Good For

- Producing bounded reports, receipts, drafts, query candidates, research packets, and local notes from explicit context packets.
- Running one-shot or manual-trigger tasks with declared inputs, outputs, tools, and STOP rules.
- Separating task output from receipt, residue, candidate, component, space_update_proposal, and STOP language.
- Drafting reusable but non-authoritative candidates and component candidates for Codex/User review.
- Preparing reduced packets that Gemini can compare without granting authority.

## 6. What Hermes Must Not Own

- VectorFL authority, baseline, policy, workflow, schema, registry, ontology, current-position, output_manifest, or current surface updates.
- Hermes memory, skills, config, gateway, real cron, recurring automation, or delivery-target setup for VectorFL without separate approval.
- Email sending, database mutation, production credentials, customer-facing final decisions, or legal/refund/SLA policy.
- Broad search, unbounded web exploration, raw output ingestion, or whole-space recognition.
- The final recovery decision; Codex decides final recovery.

## 7. Execution-to-Space Recovery Rules

- Use the lowest sufficient class.
- One-off task outputs usually stay discard or task-local output.
- Evidence that Hermes ran belongs in receipt.
- Meaningful but unstable traces become residue.
- Reusable judgments, thresholds, prompts, or task-shape ideas become candidate.
- Named bounded reusable parts become component only when boundaries are clear.
- Future updates to current surfaces or official docs are space_update_proposal only if no edit/action occurs.
- Unauthorized action verbs, persistence, memory, skill, cron, automation, policy, default, official workflow, current-position, output_manifest, or authority mutation pressure are STOP.

## 8. Output Flood Control

- Require one report and one receipt per bounded task.
- Cap source count, input files, time range, and output length before execution.
- Keep raw outputs task-local; recover only reduced receipts/residues/candidates/components.
- Batch selected residues/candidates/components for Gemini only after Codex filtering.
- Do not bulk-ingest daily briefs, raw email drafts, web findings, DB outputs, audit logs, or note folders into VectorFL Space.
- Prefer summary receipts and explicit non-actions to large transcript dumps.

## 9. B2B / Company-Work Implications

- Hermes can help with customer drafts, research, database/query assistance, notes, and operational briefs if each task is explicit, bounded, and reviewed.
- Customer-facing and company-risk work needs extra STOP triggers around legal, refund, SLA, account suspension, contract status, automatic sending, production database access, and policy/default language.
- Live integrations should be introduced in stages: local/sanitized packet -> manual-trigger pilot -> receipt/recovery review -> proposal packet -> separate approval for any live connector or recurrence.
- Notes, briefs, and receipts are not memory by default; VectorFL remembers selectively after recovery.

## 10. WATCH

- real-world Hermes use cases must be adapted into bounded task packets before execution
- cron/fresh-session power can become recurring automation drift
- memory and skills are useful but are HOLD for VectorFL authority-sensitive tests unless separately approved
- toolset breadth can hide scope expansion
- delivery targets can become external side effects
- note accumulation can masquerade as memory or authority
- database and email tasks carry credential, privacy, and mutation risk
- web exploration can flood Space unless reduced by Codex
- Codex decides final recovery; Hermes only suggests classification

## 11. HOLD

- no real cron
- no recurring automation
- no Hermes memory edit
- no Hermes skill creation or edit
- no Hermes config edit
- no gateway install
- no browser/web/network in this test
- no email/calendar/database/Obsidian/Slack/Telegram connection
- no AGENTS.md update
- no SKILL.md creation
- no baseline promotion
- no workflow/schema/registry/ontology creation
- no current-position update
- no output_manifest update
- no current surface update
- no local core / derived / surface authority mutation
- no broad repo search
- no raw output bulk ingestion into VectorFL Space

## 12. Next Smallest Action

Run one bounded simulated-context packet test for Scenario B or D only: provide 2-3 sanitized synthetic customer messages or 3 pre-captured source excerpts, ask Hermes to produce one report and one receipt, classify task output versus receipt/residue/candidate, and enforce no live email, no browser/web, no memory/skill/config edit, no cron, and no authority update.

## 13. Hard Stop Confirmation

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
