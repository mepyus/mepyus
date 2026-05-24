# Final Self-Contained Cron Prompt Candidate v0

## Purpose

This is a future Hermes no-agent/manual-trigger cron prompt candidate for VectorFL candidate-surface watch.

It is only a candidate. It does not create a real cron job. It does not approve recurring automation. It does not grant VectorFL authority.

Real cron remains HOLD until Codex/User approve the final no-agent script, self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.

## Future Cron Mode Candidate

```text
mode: no_agent script preferred
trigger: manual-trigger-first
recurrence: none unless separately approved later
schedule candidate: manual run only / one-shot explicit trigger
agent reasoning: disabled if no-agent script is used
```

## Explicit Input List

Read only these five explicit files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_design_packet.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_pre_cron_design_review_v0/pre_cron_review_receipt.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md
```

Do not read anything else.

## Declared Output Path

The future no-agent script candidate writes only:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_report.md
```

For a real future cron, Codex/User must approve whether this path stays fixed or is changed to a timestamped sandbox output path.

## No-Agent Script Path Candidate

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/candidate_no_agent_surface_watch.py
```

The script must:

```text
use only Python standard library
read only the explicit input files
write only the declared output file
avoid network
avoid subprocess
avoid Hermes CLI calls
avoid cron commands
avoid input mutation
avoid broad search
avoid sibling inspection
```

## Mechanical Checks

The script checks for:

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

## STOP Conditions

STOP if any of these are needed or requested:

```text
real Hermes cron job creation
hermes cron create/add/update/run/remove/list command
~/.hermes/cron/jobs.json edit
recurring automation
gateway install
Hermes skill creation or edit
Hermes memory edit
Hermes config edit
AGENTS.md update
SKILL.md creation
baseline promotion
workflow/schema/registry/ontology creation
current-position update
output_manifest update
local core / derived / surface authority change
broad repo search
sibling folder inspection
secret/auth/state.db/.env/session/credential-log read
network access
package install
subprocess calls
input file mutation
more than 5 input files
unclear input path
fallback writes outside declared output path
RML evidence treated as authority
MOL read-only treated as automation/workflow/script execution
```

## Failure Behavior

If an input file is missing:
- Continue with existing explicit files.
- Mark the missing file in the report.
- Do not infer from missing files.
- Do not search for replacement files.

If the output path is unavailable:
- Fail closed.
- Do not write elsewhere.
- Return a concise failure summary if possible.

If evidence is ambiguous:
- Mark WATCH.
- Do not promote.
- Do not update state.
- Route to Codex/User recovery.

If authority pressure appears:
- STOP.
- Preserve HOLD language.
- Do not create real cron, recurring automation, memory, skills, config, baseline, workflow, schema, registry, ontology, current-position, or output_manifest changes.

## Codex Recovery Handoff

Hermes/no-agent script returns:
- one local markdown report with read scope, detection results, missing/weak terms, WATCH, and HOLD.

Codex analyzes:
- whether the script read only explicit files;
- whether it wrote only the declared output;
- whether it avoided Hermes cron state and all real cron commands;
- whether STOP/failure behavior is adequate;
- whether SOF-over-RML and MOL-read-only boundaries remain visible;
- whether real cron should remain HOLD, be patched, or proceed to an explicitly approved one-shot/manual-trigger cron creation step.

User decides:
- whether to approve another dry-run;
- whether to patch the candidate script/prompt;
- whether to approve any real Hermes cron creation later.

## HOLD Statement

Real cron remains HOLD until Codex/User approve the final no-agent script, self-contained prompt, schedule, delivery behavior, and STOP/failure behavior.
