# Hermes Pre-Cron Design Review Prompt v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as an external automation design assistant for VectorFL.

This is a pre-cron design review.

Do **not** create a real cron job.
Do **not** edit Hermes cron state.
Do **not** install or trigger gateway services.

Your task is to design a future-safe Hermes cron candidate, not execute it.

## 0. Why This Exists

Hermes is strong at automation, but VectorFL authority is not automated.

Current division:

```text
Codex / VectorFL:
  owns space interpretation, SOF authority, recovery, and final judgment.

Hermes:
  may run bounded one-shot automation sessions and may later run cron only after design review and explicit approval.
```

This prompt asks Hermes to prepare a cron design packet that Codex can analyze later.

## 1. Hard Boundary

Do not:

```text
create real Hermes cron jobs
edit ~/.hermes/cron/jobs.json
run hermes cron add/create/update/run/remove
install gateway service
run hermes gateway install
create recurring automation
create cron jobs
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
read secrets, auth files, state.db, .env, sessions, credential logs
install packages
use network
```

You may:

```text
create one sandbox output directory
write one pre-cron design packet
write one pre-cron review receipt
read only the explicit files listed below
print a concise terminal summary
```

## 2. Explicit Input Files

Read only:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md
app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md
```

If a file is missing, report it and continue with existing files.

Do not read anything else.

## 3. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/
```

Allowed output files:

```text
pre_cron_design_packet.md
pre_cron_review_receipt.md
```

Do not write any other file.

## 4. Design Target

Design one future Hermes cron candidate for VectorFL.

The cron candidate should be safe, small, and useful.

Target scenario:

```text
Daily or manual-triggered check of a small explicit VectorFL candidate surface set.
The job should detect whether candidate evidence changed enough to ask Codex/User for review.
It should not update VectorFL state.
It should not write memory.
It should not promote anything.
It should not scan the repo.
```

Important:

```text
This is only a design.
Do not create the cron job.
```

## 5. Design Requirements

The pre-cron design must specify:

```text
1. Job name candidate
2. Purpose
3. Fresh-session self-contained prompt
4. Explicit file list
5. Script/no-agent decision
6. Schedule candidate
7. Delivery target candidate
8. Enabled toolsets needed
9. What the job may read
10. What the job may write
11. STOP conditions
12. Failure behavior
13. Codex recovery handoff
14. Why this should not be recurring yet
15. Criteria required before real cron creation
```

## 6. Safe Design Defaults

Use these defaults unless evidence says otherwise:

```text
schedule:
  manual-trigger-first, not recurring

delivery:
  local declared markdown file only

enabled_toolsets:
  file only, or no-agent script if possible

input files:
  1-5 explicit paths

write path:
  sandbox output only

agent mode:
  avoid LLM if deterministic script is enough

real cron:
  HOLD
```

## 7. Required Design Packet Format

Write:

```text
pre_cron_design_packet.md
```

with exactly this shape:

```markdown
# Hermes Pre-Cron Design Packet v0

## 1. Verdict

[HERMES_PRE_CRON_DESIGN_PACKET_WITH_WATCH]

## 2. Read Scope

Files read:
Files missing:
Files explicitly not read:

## 3. Cron Candidate Summary

job_name_candidate:
purpose:
current_status:
why_not_real_cron_yet:

## 4. Fresh-Session Prompt Draft

```text
[self-contained prompt for a future Hermes cron job]
```

## 5. Explicit Inputs

| File | Purpose | Sensitive? | Required? |
|---|---|---|---|

## 6. Output Contract

declared_output_path:
allowed_writes:
forbidden_writes:

## 7. Script / No-Agent Decision

recommended_mode:
why:
script_outline:

## 8. Schedule / Trigger Design

recommended_trigger:
why:
why_not_recurring_yet:

## 9. Toolset Design

enabled_toolsets_needed:
disabled_toolsets:
why:

## 10. STOP Conditions

- [condition]

## 11. Failure Behavior

If input missing:
If output path unavailable:
If evidence ambiguous:
If any authority pressure appears:

## 12. Codex Recovery Handoff

What Hermes returns:
What Codex analyzes:
What User decides:

## 13. Real Cron Readiness Checklist

| Criterion | Ready? | Gap |
|---|---:|---|

## 14. WATCH

- [watch]

## 15. HOLD

- [hold]
```

## 8. Required Receipt Format

Write:

```text
pre_cron_review_receipt.md
```

with exactly this shape:

```markdown
# Hermes Pre-Cron Design Review Receipt v0

## 1. Verdict

[HERMES_PRE_CRON_DESIGN_REVIEW_EXECUTED_WITH_WATCH]

## 2. Files Created

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_design_packet.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md

## 3. Files Read

- [list]

## 4. Files Missing

- [list or none]

## 5. Boundary Confirmation

no real Hermes cron job created
no ~/.hermes/cron/jobs.json edit
no hermes cron command run
no gateway install
no recurring automation
no Hermes skill creation
no Hermes memory edit
no Hermes config edit
no AGENTS.md update
no SKILL.md creation
no baseline promotion
no workflow/schema/registry/ontology creation
no current-position update
no output_manifest update
no local core / derived / surface authority change
no broad repo search
only declared output directory written

## 6. What Codex Should Analyze

- Is the prompt truly self-contained?
- Does it avoid real cron too early?
- Is no-agent script mode preferable?
- Are STOP conditions sufficient?
- Is Codex recovery handoff clear?
```

## 9. Terminal Summary

After completion, print only:

```text
HERMES_PRE_CRON_DESIGN_REVIEW_DONE
output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/
design_packet: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_design_packet.md
receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md
verdict: [your verdict]
watch: [top 1-2 watch items]
```

## 10. Final Instruction

Stay bounded.
Design only.
No real cron.
No recurring automation.
No VectorFL authority action.
