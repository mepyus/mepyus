# Hermes Automation Session Pilot Prompt v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as an external automation-capable runner for VectorFL.

This pilot is based on Hermes cron automation concepts:

```text
Hermes cron jobs run in fresh sessions.
Cron prompts must be self-contained.
Hermes can run one-shot or recurring scheduled tasks.
Hermes can use scripts as pre-check / no-agent mechanical steps.
```

For this VectorFL pilot, do **not** create a real recurring cron job.
Do **not** register a Hermes cron job.

Instead, implement and run a **one-shot sandbox automation session** that simulates the safest useful part of a Hermes automation:

```text
self-contained prompt + explicit inputs + mechanical script + report + receipt
```

The goal is to test whether Hermes can use its automation strength while respecting VectorFL's IIC / SOF / MOL / RML boundaries.

## 0. Division of Labor

```text
Codex / VectorFL:
  owns space interpretation, authority, boundaries, recovery, and final judgment.

Hermes:
  may implement and run one bounded one-shot automation session in a declared sandbox output directory.
  may not create recurring automation or decide VectorFL authority.
```

## 1. Hard Boundary

Do not:

```text
create real Hermes cron jobs
edit ~/.hermes/cron/jobs.json
install gateway service
run hermes gateway install
create recurring automation
create cron jobs
update AGENTS.md
create SKILL.md
create or edit Hermes skills
edit Hermes memory
edit Hermes config
edit VectorFL baseline
create registry/schema/workflow/ontology
update current-position
update output_manifest
modify local core / derived / surface authority
move existing files
run broad repo search
inspect sibling folders
read secrets, auth files, state.db, .env, sessions, logs with credentials
install packages
use network
```

You may:

```text
create one sandbox output directory
create one automation session script inside that directory
create one self-contained automation prompt/manifest inside that directory
run the script once
write report and receipt files inside that same directory
print a concise terminal summary
```

## 2. Allowed Input Files

Read only these files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md
```

If any file is missing, record that in the receipt and continue with existing files.

## 3. Allowed Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/
```

Allowed output files:

```text
automation_session_manifest.md
run_automation_session.py
automation_session_report.md
automation_session_receipt.md
```

Do not write any other files.

## 4. Automation Session Concept

This pilot should behave like a tiny local automation session:

```text
manifest:
  self-contained instruction, input list, output list, boundaries

script:
  mechanical scan of explicit inputs
  no network
  no broad search
  no external packages
  no recurring scheduling

report:
  whether the explicit inputs satisfy a small automation-readiness check

receipt:
  what was read, written, and executed
```

The script should not ask an LLM anything.
The script should perform deterministic checks over text.

## 5. Implementation Task

Create:

```text
automation_session_manifest.md
```

It should state:

```text
purpose:
  one-shot Hermes automation session pilot for VectorFL

inputs:
  the four allowed files

outputs:
  the three allowed output files besides manifest

automation boundary:
  no real cron, no recurring job, no Hermes memory/skill/config, no VectorFL authority

success criteria:
  explicit-file only
  report and receipt written
  vessel terms detected
  automation safety terms detected
  no promotion language in final judgment
```

Create:

```text
run_automation_session.py
```

The script should:

```text
1. read the allowed input files if they exist,
2. check for vessel terms:
   IIC, SOF, MOL, RML
3. check for automation boundary terms:
   no automation
   no recurring automation
   no cron job
   no Hermes memory edit
   no Hermes skill creation
   bounded carrier
   one-shot
   1-5 explicit
   SOF current authority wins
   RML evidence
   MOL read-only
4. produce automation_session_report.md
5. produce or update automation_session_receipt.md
6. use only Python standard library
7. avoid network and subprocess cron commands
```

The script may use `pathlib`, `datetime`, and standard text operations.

## 6. Report Format

Write:

```text
automation_session_report.md
```

with exactly this shape:

```markdown
# Hermes Automation Session Pilot Report v0

## 1. Verdict

[HERMES_AUTOMATION_SESSION_PILOT_REPORT_WITH_WATCH]

## 2. Automation Session Type

one-shot sandbox automation session
not real cron
not recurring automation

## 3. Inputs

| File | Exists | Bytes | Role |
|---|---:|---:|---|

## 4. Vessel Term Detection

| Term | Found | Evidence source |
|---|---:|---|

## 5. Automation Boundary Detection

| Boundary term | Found | Evidence source |
|---|---:|---|

## 6. Automation Fit Judgment

What Hermes automation can safely do here:

What Hermes automation must not do here:

Is this ready for real Hermes cron?

## 7. Weaknesses Found

- [weakness]

## 8. WATCH

- [watch]

## 9. HOLD

- [hold]
```

## 7. Receipt Format

Write:

```text
automation_session_receipt.md
```

with exactly this shape:

```markdown
# Hermes Automation Session Pilot Receipt v0

## 1. Verdict

[HERMES_AUTOMATION_SESSION_PILOT_EXECUTED_WITH_WATCH]

## 2. Files Created

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_manifest.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/run_automation_session.py
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md

## 3. Files Read

- [list]

## 4. Files Missing

- [list or none]

## 5. Execution Summary

Command run:
Exit status:
Report path:

## 6. Cron / Automation Boundary Confirmation

no real Hermes cron job created
no ~/.hermes/cron/jobs.json edit
no gateway install
no recurring automation
no cron job
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

## 7. What Codex Should Analyze

- Did Hermes keep this as one-shot automation?
- Did Hermes avoid real cron/recurring job creation?
- Did Hermes keep the script deterministic and local?
- Did Hermes preserve SOF-over-RML and MOL-read-only?
- Is the output useful enough to justify a later real cron design review?
```

## 8. Runtime Instructions

Steps:

```text
1. Create the allowed output directory.
2. Write automation_session_manifest.md.
3. Write run_automation_session.py.
4. Run the script once using python3.
5. Verify automation_session_report.md and automation_session_receipt.md exist.
6. Print the terminal summary below.
```

## 9. Terminal Summary

After completion, print only:

```text
HERMES_AUTOMATION_SESSION_PILOT_DONE
output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/
report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md
verdict: [your verdict]
watch: [top 1-2 watch items]
```

## 10. Final Instruction

Stay bounded.
This is a one-shot automation session pilot, not real cron, not recurring automation, and not VectorFL authority.
