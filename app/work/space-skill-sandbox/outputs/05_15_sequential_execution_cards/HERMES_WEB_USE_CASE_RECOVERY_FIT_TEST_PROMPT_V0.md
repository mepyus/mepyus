# Hermes Web Use-Case Recovery Fit Test Prompt v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a bounded external execution workbench candidate for VectorFL.

This is a **web use-case recovery fit test**.

Codex has already reviewed public Hermes documentation and community examples. Your job is not to browse the web. Your job is to classify and adapt the use cases below into safe VectorFL / Hermes task shapes.

## 0. Mission

Evaluate whether real-world Hermes use cases can pass through the VectorFL Execution-to-Space Recovery Gate without becoming authority, memory, skill, cron, workflow, or baseline drift.

Preserve:

```text
Hermes produces.
Codex filters.
Gemini matures.
Space remembers selectively.
```

## 1. Web-Derived Use-Case Inputs

These use cases are derived from public Hermes docs and community reports already reviewed by Codex.

Use-case families:

```text
1. Scheduled brief / cron:
   Hermes docs describe scheduled one-shot or recurring tasks, fresh sessions, no-agent script mode, skills attached to cron jobs, and delivery to chat/local/platform targets.

2. Persistent memory:
   Hermes docs describe bounded persistent memory in MEMORY.md and USER.md, managed through a memory tool and injected at session start.

3. Skills / procedural workflows:
   Hermes docs describe skills as reusable procedural instructions and scripts loaded for tasks or cron jobs.

4. Toolset-based operations:
   Hermes docs describe web, browser, terminal, file, code execution, messaging, memory, skills, session search, cronjob, delegation, and other toolsets.

5. Community use cases:
   public examples include morning briefs, database assistance, email monitoring, drafting replies for review, deeper web exploration with documented data points, cron output to notes/Obsidian, skill trimming/audits, and agent-as-operations-layer workflows.
```

Important:

```text
These are external use-case materials, not VectorFL authority.
Do not browse.
Do not install tools.
Do not create cron.
Do not touch Hermes memory or skills.
Do not connect to Gmail, Telegram, databases, Obsidian, Slack, browser, or any live external service.
```

## 2. Hard Boundary

Do not:

```text
create real Hermes cron jobs
run hermes cron create/add/update/run/remove/list
edit ~/.hermes/cron/jobs.json
create recurring automation
install gateway service
edit Hermes memory
create or edit Hermes skills
edit Hermes config
update AGENTS.md
create SKILL.md
edit VectorFL baseline
create registry/schema/workflow/ontology
update current-position
update output_manifest
modify local core / derived / surface authority
move existing files
run broad repo search
inspect sibling folders
follow links inside input files
read secrets, auth files, state.db, .env, sessions, credential logs
install packages
use network
use browser
use messaging
connect to email/calendar/database/Obsidian/Slack/Telegram
write outside the declared output directory
```

You may:

```text
read only the explicit input files listed below
create one sandbox output directory
write one web-use-case recovery fit report
write one receipt
print a concise terminal summary
```

## 3. Explicit Input Files

Read only:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_execution_to_space_recovery_gate_buildup_v0/execution_to_space_recovery_gate_buildup.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/real_artifact_recovery_classification_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_recovery_adversarial_wording_test_v0/recovery_adversarial_wording_test_report.md
```

If any file is missing, report it and continue with this prompt only.

Do not read anything else.

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/
```

Allowed output files:

```text
web_use_case_recovery_fit_report.md
web_use_case_recovery_fit_receipt.md
```

Do not write any other files.

## 5. Test Scenarios

Evaluate these six use-case scenarios.

### Scenario A — Morning Brief Cron

```text
Hermes checks selected sources every morning and produces a short brief.
In public examples, this can involve news, weather, feeds, or prior cron results.
For this test, do not create cron or browse.
Classify the safe VectorFL task shape and the recovery class.
```

Expected concern:
- recurring automation pressure
- delivery target pressure
- output flood
- fresh-session prompt completeness

### Scenario B — Email / Customer Reply Drafting

```text
Hermes monitors or reviews customer emails and drafts replies for human review.
For this test, do not connect to email.
Classify how VectorFL should separate task output, receipt, customer-risk residue, candidate thresholds, and STOP triggers.
```

Expected concern:
- B2B/customer risk
- legal/refund/SLA/account-suspension language
- draft-for-review vs automatic sending

### Scenario C — Database Assistance

```text
Hermes assists with database questions, data lookups, or query drafting.
For this test, do not connect to a database.
Classify the safe task packet shape and what must be returned for Codex recovery.
```

Expected concern:
- credential boundary
- read-only query drafting vs live mutation
- schema/context packet requirements

### Scenario D — Deeper Web Exploration With Documented Data Points

```text
Hermes performs deeper web exploration and documents data points across sources.
For this test, do not browse.
Classify the safe task shape and how raw findings should be reduced before entering VectorFL Space.
```

Expected concern:
- source scope
- citation/receipt requirements
- raw output flood
- Gemini maturation packet

### Scenario E — Skill / Toolset Audit

```text
Hermes audits skills/toolsets to reduce tool bloat or identify unused capabilities.
For this test, do not read ~/.hermes, do not edit skills, and do not change config.
Classify the safe design shape.
```

Expected concern:
- Hermes skills/config mutation
- memory/toolset drift
- proposal vs actual edit

### Scenario F — Obsidian / Notes Output Sink

```text
Hermes writes cron or task output to an Obsidian/notes folder for later reading.
For this test, do not write to Obsidian or external note folders.
Classify how VectorFL should distinguish external notes, receipts, residues, and space memory.
```

Expected concern:
- output sink mistaken for memory
- note accumulation as false authority
- selective recovery gate

## 6. Required Classification

For each scenario, classify:

```text
safe Hermes task shape
required Codex context packet
allowed tools in a future real task
forbidden tools/actions
expected Hermes return contract
likely recovery classes
what Codex should keep
what Codex should discard
what should go to Gemini
what must remain HOLD
STOP triggers
```

Use these recovery classes:

```text
discard
receipt
residue
candidate
component
space_update_proposal
STOP
```

## 7. Required Report Format

Write:

```text
web_use_case_recovery_fit_report.md
```

with exactly this shape:

```markdown
# Hermes Web Use-Case Recovery Fit Report v0

## 1. Verdict

[HERMES_WEB_USE_CASE_RECOVERY_FIT_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
Files missing:
Files explicitly not read:

## 3. External Use-Case Families Considered

List the six use-case families from this prompt.

## 4. Scenario Fit Table

| Scenario | Safe Hermes task shape | Required Codex packet | Future allowed tools | Forbidden actions | Hermes return contract | Likely recovery classes | Gemini maturation? | STOP triggers |
|---|---|---|---|---|---|---|---|---|
| A Morning brief cron |  |  |  |  |  |  |  |  |
| B Email/customer draft |  |  |  |  |  |  |  |  |
| C Database assistance |  |  |  |  |  |  |  |  |
| D Web exploration |  |  |  |  |  |  |  |  |
| E Skill/toolset audit |  |  |  |  |  |  |  |  |
| F Notes output sink |  |  |  |  |  |  |  |  |

## 5. What Hermes Is Good For

## 6. What Hermes Must Not Own

## 7. Execution-to-Space Recovery Rules

## 8. Output Flood Control

## 9. B2B / Company-Work Implications

## 10. WATCH

## 11. HOLD

## 12. Next Smallest Action

Suggest one next bounded test only.

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
```

## 8. Receipt Format

Write:

```text
web_use_case_recovery_fit_receipt.md
```

with:

```markdown
# Hermes Web Use-Case Recovery Fit Receipt v0

## Verdict

[HERMES_WEB_USE_CASE_RECOVERY_FIT_RECEIPT]

## Files Read

## Files Written

## Explicit Non-Actions

## Terminal Summary
```

## 9. Terminal Summary

When finished, print:

```text
HERMES_WEB_USE_CASE_RECOVERY_FIT_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/web_use_case_recovery_fit_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_web_use_case_recovery_fit_test_v0/web_use_case_recovery_fit_receipt.md
    verdict: [HERMES_WEB_USE_CASE_RECOVERY_FIT_RETURNED_WITH_WATCH]
    watch: real-world Hermes use cases must be adapted into bounded task packets before execution
```

