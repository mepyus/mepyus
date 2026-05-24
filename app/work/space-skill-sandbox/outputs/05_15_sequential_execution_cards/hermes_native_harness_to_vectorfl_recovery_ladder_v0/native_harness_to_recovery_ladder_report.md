# Hermes Native Harness to VectorFL Recovery Ladder Report v0

## 1. Verdict

[HERMES_NATIVE_HARNESS_TO_VECTORFL_RECOVERY_LADDER_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_execution_to_space_recovery_gate_buildup_v0/execution_to_space_recovery_gate_buildup.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/web_use_case_recovery_fit_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_b2b_customer_draft_simulated_packet_v0/b2b_customer_draft_simulated_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/real_artifact_recovery_classification_report.md

Files missing:
- none

Files explicitly not read:
- live connectors: email, CRM, database, browser, web, Slack, Telegram, Obsidian, or any external service
- sibling folders under app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards
- linked files named inside input files
- repo-wide tree, broad search output, runtime logs, sessions, secrets, auth files, state.db, .env, credential logs
- AGENTS.md, SKILL.md, Hermes memory, Hermes skills, Hermes config, Hermes cron state, ~/.hermes/cron/jobs.json
- VectorFL baseline, registry, schema, workflow, ontology, current-position, output_manifest, local core / derived / surface authority files

## 3. Core Principle

- Let Hermes act natively.
- Let VectorFL recover selectively.

This means Hermes should not be reduced to a crippled file-only assistant forever. Hermes may eventually use its native harness: browser/web, terminal, file, external-app connectors, delivery targets, manual-trigger jobs, approved recurring automation, memory, and skills.

This does not mean Hermes outputs become VectorFL authority. Hermes execution permission and VectorFL recovery permission are separate. Hermes may be allowed to perform a native task, while VectorFL recovers only a receipt, residue, candidate, component, or proposal after Codex filtering.

The separation is:
- Hermes execution permission: can Hermes use a tool or connector for this task?
- external action approval: can Hermes create a side effect such as sending, writing, mutating, scheduling, or persisting?
- VectorFL recovery permission: can the resulting output enter VectorFL as receipt/residue/candidate/component/proposal, and does any part remain HOLD/STOP?

Therefore:
- Hermes memory != VectorFL memory
- Hermes skill != VectorFL SKILL.md
- Hermes cron != VectorFL workflow
- Hermes note/output sink != VectorFL authority
- Hermes report != VectorFL baseline
- Hermes successful run != VectorFL approval
- Hermes execution permission != VectorFL recovery permission
- Hermes side effect approval != VectorFL promotion approval

## 4. Role Separation

| Layer | Owns | Does not own | WATCH |
|---|---|---|---|
| Hermes native harness | Execution, tools, connectors, drafts, reports, receipts, local scripts, approved automation, and Hermes-native continuity when separately allowed. | VectorFL authority, baseline, recovery decision, official workflow, VectorFL memory, or promotion. | Tool fluency can look like authority; side effects need approval; successful execution can be over-recovered. |
| VectorFL Space | Meaning, criteria, authority layers, selective memory, placement/promotion boundaries, and what counts as recovered. | Hermes internal harness, Hermes tool availability, or every raw Hermes output. | Over-controlling Hermes can destroy useful execution; under-filtering can pollute Space. |
| Codex recovery gate | Translation between Hermes outputs and VectorFL recovery classes; downshift/filter; STOP/HOLD enforcement. | Silent promotion, live connector approval by implication, or automatic VectorFL authority movement. | Codex can bottleneck; must distinguish side-effect approval from VectorFL promotion approval. |
| Gemini maturation lens | Broad comparison over reduced residues/candidates/components; naming and pattern maturation proposals. | Authority, approval, baseline, workflow, ontology, memory, cron, or Space updates. | Gemini can over-name patterns into ontology if not bounded to proposals. |
| User approval | Direction, external side-effect approval, promotion decisions, and final authority escalation. | Automatic recovery of all Hermes outputs. | User approval must be specific: execution side effect, Hermes-native persistence, and VectorFL promotion are different approvals. |

## 5. Permission Ladder

| Stage | Hermes-native capability | Example use | Required Codex packet | Required Hermes receipt | VectorFL recovery allowed | Approval needed | STOP / approval triggers | WATCH |
|---|---|---|---|---|---|---|---|---|
| 0 Simulated | No live connectors; synthetic or sanitized context only. | Simulated B2B customer draft test; synthetic recovery classification. | Synthetic inputs, task goal, forbidden actions, output directory, report/receipt format, recovery target. | Synthetic inputs used, files read/written, no live connector, no message sent, no memory/skill/cron/config edits. | Drafts discard; run evidence receipt; repeated missing context residue; thresholds candidate; intake cards component candidate. | Usually no external approval; only ordinary task approval. | Any attempt to send, save memory, create policy/workflow, or update VectorFL authority is STOP. | Good for risk shaping but not proof of live readiness. |
| 1 Local file + terminal | Local file reads/writes in sandbox and terminal/code execution under explicit scope. | One-shot script, deterministic checks, local report/receipt. | Explicit input files, allowed command/script, declared output path, no broad search, no secrets, expected exit behavior. | Commands/tools used, exit status, files read/written, errors, non-actions, output paths. | Receipt; residue from failures; candidate script idea; component if named bounded runner part. | Approval for command execution if side-effectful; no VectorFL promotion approval implied. | File moves, broad search, input mutation, baseline/output_manifest/current-position updates are STOP. | Local runner success is evidence, not semantic proof or authority. |
| 2 Browser/web read-only | Bounded web/browser/search read-only collection. | Cited research packet, source comparison, deeper web exploration with source cap. | Research question, allowed sources/search terms, source cap, date scope, citation requirements, excluded sites, output path. | URLs/sources visited, citations, query terms, time/date scope, non-actions, no forms submitted, no accounts mutated. | Source/citation receipt; raw findings residue; repeated patterns candidate; research packet template component. | Approval to use network/browser; no external write approval if read-only. | Login, scraping beyond scope, posting, updating Space, treating web findings as authority are STOP or external_action_approval_required. | Web output flood must be reduced before recovery. |
| 3 External app read-only | Read/export from approved external app without mutation. | Email export, DB read-only sample, notes folder read, CRM export. | Connector/app, account/source, read-only boundary, data minimization, privacy limits, exact query/export scope, output path. | Connector touched, records/messages/schemas read, filters used, credentials excluded, no writes/sends/mutations. | Receipt; sanitized residue; candidate missing-context patterns; component packet shape. | Explicit external read approval; credential boundary approval; no write approval. | Reading secrets, broad export, production table dump, hidden persistence, customer data memory are STOP/external approval failures. | Read-only does not mean safe to recover raw data into VectorFL. |
| 4 External app write-draft only | Create drafts or local notes without sending/publishing/finalizing. | Save email draft, create local note draft, prepare message but do not send. | Target app/location, draft-only boundary, no-send rule, content constraints, reviewer, rollback/delete plan, output path. | Draft location/ID if allowed, no send/publish confirmation, content summary, reviewer needed, non-actions. | Draft text discard/task-local; receipt; residue/candidate from reduced patterns; component draft template if bounded. | external_action_approval_required for app write; separate approval still needed for sending/publishing. | Send/post/publish, liability admission, refund promise, memory save, policy/workflow/default wording are STOP or external-action blocked. | Draft location can be mistaken for memory or authority. |
| 5 Manual-trigger automation | One-shot script, no-agent runner, manually triggered job. | Manual surface watch dry-run, local batch processor, one-shot report generator. | Script/manifest, explicit inputs, one execution, output path, failure behavior, no recurrence, STOP rules, receipt shape. | Script path/content summary, command run, exit status, input/output files, no cron, no recurring automation, failures. | Receipt; residue from failures; candidate automation idea; component runner packet if reusable and bounded. | Approval for one-shot execution; not approval for recurrence. | Scheduling, daily run, cron creation, automatic retention/delivery, current-position/output_manifest edits are STOP/external_action_approval_required. | Manual-trigger-first can drift into cron normalization. |
| 6 Recurring automation | Approved Hermes cron/scheduled check or recurring brief. | Scheduled morning brief, recurring no-agent check, approved delivery. | Self-contained cron prompt/script, schedule, delivery target, toolsets, fresh-session context, failure/STOP behavior, retention, recovery handoff. | Job identity, schedule, prompt/script version, run outputs, delivery target, failures, side effects, non-actions, recovery summary. | Each run yields receipt; selected residues/candidates/components only after Codex filtering; cron itself is not VectorFL workflow. | explicit recurring automation approval; external delivery approval; still separate VectorFL recovery/promotion approval. | Creating/enabling cron without approval, editing jobs.json, treating schedule as workflow/baseline/memory is STOP or external_action_approval_required. | Cron output flood and fresh-session drift require strict receipts and summarization. |
| 7 Hermes memory/skill use | Hermes-native memory for Hermes continuity; Hermes skill for Hermes procedure. | Remember user preference for Hermes use, load/create Hermes procedure for non-VectorFL task if approved. | What may be remembered/skillified, scope, retention, non-VectorFL status, exclusion of VectorFL authority, review requirement. | Memory/skill action taken or explicitly not taken, content summary, scope, where stored, why approved. | Usually receipt/candidate only for VectorFL; Hermes memory/skill is not VectorFL memory/SKILL.md. | explicit Hermes persistence approval; separate VectorFL promotion approval if any recovery is proposed. | Saving VectorFL standards into Hermes memory, creating SKILL.md, treating Hermes skill as VectorFL workflow is STOP. | Useful continuity can become hidden authority if not labeled Hermes-native only. |

## 6. Recovery Contract

For every Hermes-native run, define:
- report: human-readable task result, limits, and recommendations.
- receipt: evidence of the run, exact scope, tools, connector use, side effects, output paths, and non-actions.
- tools/connectors used: web/browser/file/terminal/email/database/notes/messaging/cron/memory/skills/etc.
- external side effects: sends, writes, posts, drafts, database reads/writes, scheduled jobs, memory/skill/config changes.
- files read/written: exact paths, missing files, and explicitly not-read areas.
- live systems touched: account/app/source, read/write mode, record scope, and credentials excluded.
- customer/user impact: whether anything was sent, published, changed, or merely drafted.
- failures: errors, partial results, fallback attempts, and safe stops.
- non-actions: no-send, no-memory, no-skill, no-cron, no-authority-update, no-broad-search, no-promotion.
- recommended recovery class: discard, receipt, residue, candidate, component, space_update_proposal, STOP, or external_action_approval_required.
- Codex decision required: final recovery class and any VectorFL placement/promotion decision remain Codex/User controlled.

## 7. Boundary Examples

- Hermes browser research vs VectorFL source recovery:
  - Hermes may browse a bounded source list after approval.
  - VectorFL recovers only citation receipt, reduced findings residue, and candidate patterns.
  - Raw browsing transcript does not become Space memory.

- Hermes email draft vs VectorFL customer-risk residue:
  - Hermes may draft for human review from explicit or approved email context.
  - Sending is external_action_approval_required.
  - VectorFL may recover repeated risk/missing-context residue or candidate thresholds, not raw customer drafts as authority.

- Hermes DB query draft vs VectorFL query-pattern candidate:
  - Hermes may draft SQL or analyze sanitized schema/sample data.
  - Live DB execution needs explicit external action approval; writes/migrations are higher-risk.
  - VectorFL may recover query-pattern candidates or a bounded query checklist, not credentials or raw private data.

- Hermes cron job vs VectorFL receipt/candidate only:
  - Hermes may run approved cron in its own harness.
  - Hermes cron is not VectorFL workflow.
  - Each run returns receipts; only selected reduced residue/candidates/components enter VectorFL review.

- Hermes memory/skill vs VectorFL memory/SKILL.md separation:
  - Hermes memory/skills may support Hermes-native continuity only after explicit approval.
  - They do not write VectorFL memory, baseline, or SKILL.md.
  - Saving VectorFL authority into Hermes persistence without approval is STOP.

- Hermes note output vs VectorFL selective memory:
  - Hermes may write an approved note/output sink.
  - Notes are external outputs, not VectorFL authority.
  - VectorFL recovers selectively through Codex, not by bulk-ingesting notes.

## 8. External Action Approval Lane

A task is not automatically VectorFL STOP when Hermes can natively perform an external side effect. It becomes external_action_approval_required when execution is plausible but must pause for explicit approval before side effects.

Use external_action_approval_required for:
- sending email
- writing to external app
- saving an external draft or note
- running live DB query
- posting message
- enabling cron
- changing delivery target
- modifying Hermes memory/skill/config

VectorFL STOP is different. Use VectorFL STOP for:
- unauthorized VectorFL authority mutation
- baseline/workflow/schema/registry/ontology creation
- current-position/output_manifest update
- VectorFL memory update without approval
- treating Hermes output as VectorFL policy/default/approval
- creating local core / derived / surface authority changes

If both appear, stop and label both dimensions:
- external side effect needs approval
- VectorFL recovery/promotion remains HOLD or STOP

## 9. What Must Stay VectorFL HOLD

- VectorFL baseline promotion
- VectorFL workflow/schema/registry/ontology creation
- current-position update
- output_manifest update
- local core / derived / surface authority changes
- AGENTS.md update
- VectorFL SKILL.md creation
- VectorFL memory or official Space memory movement
- treating Hermes report as baseline
- treating Hermes successful run as approval
- treating Hermes cron as VectorFL workflow
- treating Hermes note/output sink as VectorFL authority
- bulk ingestion of raw Hermes outputs

## 10. What Must Stay Hermes-Native

- Hermes tool choice and harness mechanics when separately approved for execution.
- Hermes memory for Hermes continuity, if explicitly approved and scoped.
- Hermes skills as Hermes procedural aids, if explicitly approved and not confused with VectorFL SKILL.md.
- Hermes cron as Hermes scheduler, if explicitly approved and not confused with VectorFL workflow.
- Hermes notes/reports/receipts as task outputs, not Space authority.
- Hermes connector operation logs and side-effect receipts as execution evidence.

VectorFL should recover meaning from these artifacts, not absorb the internal machinery as authority.

## 11. Gemini Maturation Inputs

What can be sent to Gemini:
- Reduced residues: recurring missing context, failure modes, output flood risks.
- Candidate thresholds: risk triggers, wording STOP triggers, source selection patterns.
- Component candidates: intake card shape, dry-run packet shape, receipt contract shape.
- Cross-run summaries prepared by Codex, not raw connector dumps.

What must not be sent:
- Secrets, credentials, auth files, session logs, state.db, private raw customer data, raw email bodies, raw DB dumps, raw notes folders, or unbounded web transcripts.
- Anything framed as already-authoritative baseline/workflow/ontology/memory.
- Material requiring Gemini to approve promotion or side effects.

How to reduce packets:
- Strip raw content to abstracted signals, counts, source/citation receipts, and short examples.
- Preserve provenance and uncertainty.
- Label every item as residue/candidate/component/proposal only.
- Include HOLD/STOP boundaries and Codex final-decision statement.

## 12. Failure Modes

- over-constraining Hermes:
  - Treating every native tool as forbidden prevents Hermes from becoming useful as an execution workbench.
  - Fix: separate execution permission from recovery permission.

- over-recovering Hermes outputs:
  - Treating reports, notes, cron outputs, or successful runs as Space authority pollutes VectorFL.
  - Fix: receipts/residue/candidates/components stay proposals unless approved.

- confusing Hermes memory with VectorFL memory:
  - Hermes continuity can become hidden VectorFL standard.
  - Fix: label Hermes memory as Hermes-native only; VectorFL memory requires separate recovery approval.

- confusing cron with workflow:
  - A recurring Hermes job can feel like an official process.
  - Fix: Hermes cron is scheduler evidence; VectorFL workflow remains HOLD unless separately approved.

- confusing notes with authority:
  - Notes/output sinks can accumulate and look like memory.
  - Fix: notes are task outputs until Codex recovers selected content.

- confusing side-effect approval with promotion approval:
  - Permission to send/write/run does not mean permission to promote into VectorFL.
  - Fix: track external_action_approval_required separately from VectorFL recovery class.

- Codex bottleneck:
  - Too many Hermes outputs can overload the recovery gate.
  - Fix: summary receipts, output caps, reduced packets, and Gemini maturation batches.

- output flood:
  - Cron, web, email, and notes can generate too much raw material.
  - Fix: source caps, run receipts, deduplication, discard/receipt/residue triage.

## 13. WATCH

- do not cripple Hermes-native execution
- do not let Hermes outputs become VectorFL authority by accident
- Hermes execution permission is not VectorFL recovery permission
- Hermes side effect approval is not VectorFL promotion approval
- external_action_approval_required should not be confused with VectorFL STOP
- Hermes memory is not VectorFL memory
- Hermes skill is not VectorFL SKILL.md
- Hermes cron is not VectorFL workflow
- Hermes note/output sink is not VectorFL authority
- Hermes report is not VectorFL baseline
- Hermes successful run is not VectorFL approval
- Codex decides final recovery

## 14. HOLD

- no live connector used in this design task
- no message sent
- no real cron
- no recurring automation
- no Hermes memory edit
- no Hermes skill creation or edit
- no Hermes config edit
- no AGENTS.md update
- no SKILL.md creation
- no baseline promotion
- no workflow/schema/registry/ontology creation
- no current-position update
- no output_manifest update
- no local core / derived / surface authority change
- no broad repo search
- no raw Hermes output bulk ingestion into VectorFL Space

## 15. Next Smallest Action

Run one bounded Stage 1 or Stage 2 side-effect-lane test: give Hermes a local file or read-only web-style source packet and ask it to classify separately (1) Hermes execution permission, (2) external_action_approval_required if any, and (3) VectorFL recovery class. Produce one report and one receipt only; do not use live connectors, no memory/skill/config edit, no cron, no VectorFL authority update.

## 16. Hard Stop Confirmation

no live connector used
no message sent
no real cron
no recurring automation
no Hermes memory edit
no Hermes skill creation or edit
no Hermes config edit
no AGENTS.md update
no SKILL.md creation
no baseline promotion
no workflow/schema/registry/ontology creation
no current-position update
no output_manifest update
no local core / derived / surface authority change
no broad repo search
