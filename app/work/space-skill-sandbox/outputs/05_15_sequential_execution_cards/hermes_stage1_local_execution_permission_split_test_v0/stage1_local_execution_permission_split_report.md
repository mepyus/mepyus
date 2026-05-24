# Hermes Stage 1 Local Execution Permission Split Report v0

## 1. Verdict

[HERMES_STAGE1_LOCAL_EXECUTION_PERMISSION_SPLIT_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_native_harness_to_vectorfl_recovery_ladder_v0/native_harness_to_recovery_ladder_report.md

Files missing:
- none

Files explicitly not read:
- live connectors: email, CRM, database, browser, web, Slack, Telegram, Obsidian, or any external service
- sibling folders under app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards
- linked files inside the input file
- repo-wide tree, broad search output, runtime logs, sessions, secrets, auth files, state.db, .env, credential logs
- AGENTS.md, SKILL.md, Hermes memory, Hermes skills, Hermes config, Hermes cron state, ~/.hermes/cron/jobs.json
- VectorFL baseline, registry, schema, workflow, ontology, current-position, output_manifest, local core / derived / surface authority files

## 3. Stage 1 Decision Table

| Task | Hermes execution permission | External action approval | VectorFL recovery class | Why | Required receipt | WATCH | HOLD |
|---|---|---|---|---|---|---|---|
| A Local read-only summarizer | allowed with constraints | none | receipt + possible residue/candidate | Reading explicit local markdown files and writing one sandbox report/receipt is Stage 1 native local execution. No live connector, no shell command, and no VectorFL authority mutation are requested. The run evidence is receipt; reduced repeated findings may become residue; bounded reusable conclusions may be candidate only. | exact files read, files written, no shell command, no live connector, no input mutation, no authority update, recommended recovery class | Do not treat a clean summary as baseline or current-surface truth. Lowest sufficient recovery class wins. | no broad search, no sibling inspection, no output_manifest/current-position/baseline update |
| B Local deterministic script runner | allowed with constraints | none for external systems; local command approval required before run | receipt + possible component candidate | A one-shot stdlib Python script over explicit files can be Stage 1 local terminal execution if the user approves the command, inputs are fixed, outputs are declared, and inputs are not mutated. External action approval is not the lane because no external system is touched. The command result is receipt; the bounded script shape may be component candidate, not workflow. | script path/content summary, command run, exit status, explicit input files, declared outputs, input mutation confirmation, non-actions, recovery recommendation | Script success proves execution only, not semantic compliance or VectorFL approval. Component candidate is not workflow. | no arbitrary shell expansion, no package install, no recurrence, no input mutation, no authority update |
| C Local script updates current surface | technically possible but not allowed under this test as requested | not applicable / not the main issue | STOP | The problem is not external side effect approval; it is VectorFL authority mutation. Updating runtime/views/current_asset_map_v1.md and output_manifest automatically crosses current surface/output manifest boundaries. Local file write is not the same as sandbox output write. | receipt may record the blocked request and STOP rationale only; do not execute the mutation | Do not soften authority mutation into ordinary local execution just because it is local. | STOP: no current-position/current surface update, no output_manifest update, no local core/derived/surface authority change |

## 4. Permission Split Findings

What Hermes can do natively:
- Read explicit local files under a bounded prompt.
- Write a declared sandbox report and receipt.
- Prepare a deterministic local script-run packet.
- Run a one-shot local command only when explicitly approved, scoped, and recorded.
- Produce execution evidence as a receipt and propose reduced recovery classes.

What still needs local execution approval:
- Running a local command or script, even if it is standard-library only.
- Any command that creates files, changes permissions, moves files, mutates inputs, or could inspect beyond the explicit scope.
- Any shift from design/classification to actual one-shot execution.

What is external_action_approval_required:
- None for Task A.
- None for external systems in Task B; the needed approval is local command approval, not external action approval.
- Not the main issue for Task C because no external system is touched.
- In general, this lane applies to live side effects such as sending, posting, external-app writes, live DB actions, external drafts/notes, delivery target changes, or recurring scheduler enablement.

What is VectorFL STOP:
- Any automatic current surface/current_asset_map/current-position update.
- Any output_manifest update.
- Any baseline, workflow, schema, registry, ontology, local core, derived, or surface authority mutation.
- Treating Hermes execution success, report output, or receipt as VectorFL approval.
- Turning a component candidate into an official workflow without separate Codex/User promotion approval.

What can be recovered:
- Task A: execution evidence as receipt; stable reduced observations as residue or candidate only.
- Task B: command/run evidence as receipt; reusable bounded script shape as component candidate only.
- Task C: blocked request and STOP rationale as receipt of refusal/block only; no authority mutation recovered as accepted output.

## 5. Local Stage 1 Receipt Contract

For Stage 1 local runs, require:
- explicit input files
- declared output path
- commands/scripts used
- exit status if executed
- files read/written
- input mutation confirmation
- non-actions
- recovery recommendation

Additional Stage 1 receipt requirements:
- state whether shell/terminal was used
- state whether the command was user-approved before execution
- state whether only declared outputs were written
- state whether package install, network, broad search, sibling inspection, and secrets reads were avoided
- state whether any VectorFL authority file was requested or touched
- state that receipt is evidence only, not authority

## 6. Misclassification Risks

- Mistaking local execution permission for VectorFL authority update permission.
- Treating sandbox output writes as equivalent to current surface writes.
- Treating a successful local script as semantic validation.
- Treating a reusable script as an approved workflow.
- Treating a receipt as baseline, memory, or policy.
- Over-blocking Task A and Task B merely because they use files or terminal; Stage 1 is meant to allow bounded local execution.
- Under-blocking Task C because it uses only local files; VectorFL authority mutation is still STOP even without external connectors.
- Confusing local command approval with external_action_approval_required.

## 7. WATCH

- local execution permission must not be confused with VectorFL authority update permission
- Hermes execution permission != VectorFL recovery permission
- Hermes side effect approval != VectorFL promotion approval
- local file write != VectorFL authority write
- sandbox output write != current surface update
- local command run != recurring automation
- script success != semantic compliance
- receipt != authority
- component candidate != workflow
- lowest sufficient recovery class wins
- Codex/User decide final VectorFL recovery and promotion

## 8. HOLD

- no live connector use
- no message sending
- no real Hermes cron
- no recurring automation
- no Hermes memory/skill/config edit
- no AGENTS.md update
- no SKILL.md creation
- no baseline promotion
- no workflow/schema/registry/ontology creation
- no current-position or current surface update
- no output_manifest update
- no local core / derived / surface authority mutation
- no broad repo search
- no sibling inspection
- no secret/auth/session/state/credential file reads
- no arbitrary shell command execution for this test

## 9. Next Smallest Action

Run a bounded Stage 1 one-shot local deterministic script packet with an explicitly provided Python standard-library script, two explicit sanitized input files, one declared sandbox output directory, user-approved command text, one execution, one report, and one receipt. Keep real cron, external connectors, memory/skill/config edits, and all VectorFL authority updates on HOLD.

## 10. Hard Stop Confirmation

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
