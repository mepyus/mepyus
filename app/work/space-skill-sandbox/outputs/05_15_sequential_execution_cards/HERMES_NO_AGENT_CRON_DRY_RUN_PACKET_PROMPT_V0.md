# Hermes No-Agent Cron Dry-Run Packet Prompt v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as an external automation design-and-dry-run assistant for VectorFL.

This is a **no-agent/manual-trigger cron dry-run packet** stage.

Do not create a real Hermes cron job.
Do not edit Hermes cron state.
Do not run any `hermes cron` lifecycle command.

Your job is to build a sandbox-only candidate packet for a future no-agent cron:

```text
candidate no-agent script
final self-contained cron prompt candidate
local dry-run report
local dry-run receipt
Codex real-cron readiness review checklist
```

## 0. Current Decision State

Current stable decision:

```text
Pre-cron design review: passed
Real cron: HOLD
Next step: no-agent/manual-trigger cron dry-run packet
```

Important path correction:

```text
actual prior receipt path:
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md
```

Do not use the typo path:

```text
hermes_pre_crON_design_review_v0
```

## 1. Hard Boundary

Absolutely do not:

```text
run hermes cron create/add/update/run/remove
run hermes cron list as part of this task
edit ~/.hermes/cron/jobs.json
create a real cron job
create recurring automation
install gateway service
run hermes gateway install
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
write candidate no-agent script
write final self-contained cron prompt candidate
run the candidate script once locally as a dry-run
write dry-run report
write dry-run receipt
write Codex real-cron readiness review checklist
print a concise terminal summary
```

## 2. Input Files

Read only these explicit files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_design_packet.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md
```

If any file is missing, report it and continue with existing files.

Do not read anything else.

## 3. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/
```

Allowed output files:

```text
candidate_no_agent_surface_watch.py
final_self_contained_cron_prompt_candidate.md
no_agent_cron_dry_run_report.md
no_agent_cron_dry_run_receipt.md
codex_real_cron_readiness_review_checklist.md
```

Do not write any other files.

## 4. Candidate No-Agent Script Requirements

Create:

```text
candidate_no_agent_surface_watch.py
```

This script is a candidate for a future no-agent Hermes cron script.

It must:

```text
1. use only Python standard library
2. read only the explicit input files listed in this prompt
3. not use network
4. not call subprocess
5. not call hermes
6. not create cron jobs
7. not modify input files
8. write only no_agent_cron_dry_run_report.md in the declared output directory
9. be runnable manually with python3
```

The script should check for:

```text
IIC
SOF
MOL
RML
STOP
SOF current authority wins
RML evidence
MOL read-only
no automation
no recurring automation
no cron job
no Hermes memory edit
no Hermes skill creation
bounded carrier
one-shot
1-5 explicit
Real cron
HOLD
```

The script should produce:

```text
no_agent_cron_dry_run_report.md
```

## 5. Self-Contained Cron Prompt Candidate

Create:

```text
final_self_contained_cron_prompt_candidate.md
```

This is a future prompt candidate only.
It must be self-contained because Hermes cron sessions are fresh sessions.

It must include:

```text
purpose
explicit input list
declared output path
no-agent script path candidate
STOP conditions
failure behavior
Codex recovery handoff
HOLD statement that real cron remains uncreated
```

It must explicitly state:

```text
Real cron remains HOLD until Codex/User approve the final no-agent script,
self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.
```

## 6. Dry-Run Report Format

The candidate script must write:

```text
no_agent_cron_dry_run_report.md
```

with this shape:

```markdown
# Hermes No-Agent Cron Dry-Run Report v0

## 1. Verdict

[HERMES_NO_AGENT_CRON_DRY_RUN_PACKET_RETURNED_WITH_WATCH]

## 2. Dry-Run Type

manual local dry-run
no real cron
no recurring automation
no Hermes cron command

## 3. Inputs

| File | Exists | Bytes | Role |
|---|---:|---:|---|

## 4. Detection Results

| Term | Found | Evidence source |
|---|---:|---|

## 5. Missing / Weak Terms

- [term or none]

## 6. No-Agent Cron Candidate Fit

What this script can safely do:

What it must not do:

Ready for real cron?

## 7. WATCH

- [watch]

## 8. HOLD

- [hold]
```

## 7. Dry-Run Receipt Format

After running the script once manually, write:

```text
no_agent_cron_dry_run_receipt.md
```

with this shape:

```markdown
# Hermes No-Agent Cron Dry-Run Receipt v0

## 1. Verdict

[HERMES_NO_AGENT_CRON_DRY_RUN_EXECUTED_WITH_WATCH]

## 2. Files Created

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/candidate_no_agent_surface_watch.py
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/final_self_contained_cron_prompt_candidate.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_receipt.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/codex_real_cron_readiness_review_checklist.md

## 3. Files Read

- [list]

## 4. Files Missing

- [list or none]

## 5. Execution Summary

Command run:
Exit status:
Report path:

## 6. Boundary Confirmation

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

## 7. Next Decision

Real cron remains HOLD until Codex/User approve the final no-agent script, self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.
```

## 8. Codex Review Checklist

Create:

```text
codex_real_cron_readiness_review_checklist.md
```

with this shape:

```markdown
# Codex Real Cron Readiness Review Checklist v0

## 1. Verdict

[CODEX_REAL_CRON_READINESS_REVIEW_REQUIRED]

## 2. Must Pass Before Real Cron

| Criterion | Pass? | Evidence | Gap |
|---|---:|---|---|
| no-agent script uses only standard library |  |  |  |
| no-agent script reads only explicit files |  |  |  |
| no-agent script writes only declared output |  |  |  |
| self-contained prompt includes full boundaries |  |  |  |
| schedule is manual-trigger-first |  |  |  |
| delivery is local markdown only |  |  |  |
| STOP conditions cover authority drift |  |  |  |
| failure behavior is explicit |  |  |  |
| Codex recovery handoff is explicit |  |  |  |
| User approval is still required |  |  |  |

## 3. Automatic Fail Conditions

- any real cron command already ran
- ~/.hermes/cron/jobs.json changed
- gateway installed
- recurring automation created
- memory/skill/config edited
- broad search performed
- VectorFL authority changed

## 4. Recommended Decision

Real cron:
  HOLD

Next safe step:
  Codex reviews this packet and either requests a patch or approves another manual dry-run.
```

## 9. Runtime Steps

```text
1. Create output directory.
2. Write candidate_no_agent_surface_watch.py.
3. Write final_self_contained_cron_prompt_candidate.md.
4. Run candidate_no_agent_surface_watch.py once with python3.
5. Write no_agent_cron_dry_run_receipt.md.
6. Write codex_real_cron_readiness_review_checklist.md.
7. Print terminal summary.
```

## 10. Terminal Summary

After completion, print only:

```text
HERMES_NO_AGENT_CRON_DRY_RUN_PACKET_DONE
output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/
script: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/candidate_no_agent_surface_watch.py
prompt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/final_self_contained_cron_prompt_candidate.md
report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_report.md
receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_receipt.md
checklist: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/codex_real_cron_readiness_review_checklist.md
verdict: [your verdict]
watch: [top 1-2 watch items]
```

## 11. Final Instruction

Stay bounded.
This is a no-agent cron dry-run packet, not real cron and not recurring automation.
