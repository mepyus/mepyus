# Hermes Real Artifact Recovery Classification Prompt v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a bounded external execution workbench candidate for VectorFL.

This is a **real artifact recovery classification test**.

You are not performing new external work. You are reading a small set of actual prior Hermes artifacts and classifying how Codex should recover them into the Execution-to-Space Recovery Gate.

## 0. Mission

Read the explicit Hermes artifact files below and classify each artifact as one of:

```text
discard
receipt
residue
candidate
component
space_update_proposal
STOP
```

The goal is to test whether the recovery gate works on real Hermes outputs, not only synthetic snippets.

Preserve:

```text
Hermes produces.
Codex filters.
Gemini matures.
Space remembers selectively.
```

Important:

```text
Hermes must not overvalue its own prior outputs.
Prior Hermes success is evidence only.
Reports and receipts are not authority.
Candidate/component/proposal classifications are proposals only.
Codex decides final recovery.
```

## 1. Hard Boundary

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
write outside the declared output directory
```

You may:

```text
read only the explicit input files listed below
create one sandbox output directory
write one real-artifact classification report
write one receipt
print a concise terminal summary
```

## 2. Explicit Input Files

Read only these files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VESSEL_STANDARD_EXTERNAL_TOOL_FIT_RETURN_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_no_agent_cron_dry_run_packet_v0/no_agent_cron_dry_run_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_recovery_adversarial_wording_test_v0/recovery_adversarial_wording_test_report.md
```

If any file is missing, report it and continue with existing files.

Do not read anything else.

## 3. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/
```

Allowed output files:

```text
real_artifact_recovery_classification_report.md
real_artifact_recovery_classification_receipt.md
```

Do not write any other files.

## 4. Recovery Classes

Use these definitions:

```text
discard:
  one-off byproduct; no need to preserve beyond task result.

receipt:
  evidence that a task ran, with scope, files, tools, and result path.

residue:
  meaningful trace that may matter later but is not reusable yet.

candidate:
  reusable judgment, threshold, pattern, prompt, script idea, or operating behavior.

component:
  named function/part that can be reused inside a bounded lane.

space_update_proposal:
  possible future update to current surface, baseline, guide, spec, registry, workflow, ontology, or memory, but not approved.

STOP:
  authority, memory, automation, cron, skill, config, baseline, policy, registry, workflow, ontology, current-position, output_manifest, or local authority mutation pressure.
```

## 5. Classification Rules

Use the lowest sufficient class.

```text
If the artifact mainly proves a run happened -> receipt.
If it contains meaningful trace but no reusable rule -> residue.
If it contains a reusable judgment/threshold/pattern -> candidate.
If it defines a named reusable part with boundaries -> component.
If it recommends future space/current/baseline update without editing -> space_update_proposal.
If it requests or performs unauthorized authority/persistence/action -> STOP.
```

Do not:

```text
promote Hermes success into authority.
promote receipt into candidate because it is well formatted.
promote a candidate into component because it is useful.
promote component into workflow.
promote proposal into update.
soften STOP into review when action verbs appear.
```

## 6. Artifact-Specific Questions

For each artifact, answer:

```text
1. What is the artifact primarily?
2. What recovery class should Codex assign?
3. What should be kept?
4. What should be discarded or ignored?
5. What must not be promoted?
6. Is there any STOP pressure?
7. Should this be sent to Gemini for maturation? If yes, why and in what reduced form?
```

## 7. Required Report Format

Write:

```text
real_artifact_recovery_classification_report.md
```

with exactly this shape:

```markdown
# Hermes Real Artifact Recovery Classification Report v0

## 1. Verdict

[HERMES_REAL_ARTIFACT_RECOVERY_CLASSIFICATION_RETURNED_WITH_WATCH]

## 2. Read Scope

Files read:
Files missing:
Files explicitly not read:

## 3. Artifact Classification Summary

| Artifact | Primary nature | Selected class | Keep | Discard / ignore | Must not promote | STOP pressure | Gemini maturation? |
|---|---|---|---|---|---|---|---|
| HERMES_VESSEL_STANDARD_EXTERNAL_TOOL_FIT_RETURN_V0.md |  |  |  |  |  |  |  |
| HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md |  |  |  |  |  |  |  |
| vessel_runner_pilot_report.md |  |  |  |  |  |  |  |
| no_agent_cron_dry_run_report.md |  |  |  |  |  |  |  |
| recovery_adversarial_wording_test_report.md |  |  |  |  |  |  |  |

## 4. Cross-Artifact Pattern

What repeats across artifacts:
What remains only receipt:
What becomes candidate:
What becomes component:
What should be sent to Gemini:
What must stay HOLD:

## 5. Over-Recovery Risks

## 6. Under-Recovery Risks

## 7. Codex Recovery Recommendation

## 8. WATCH

## 9. HOLD

## 10. Next Smallest Action

Suggest one next bounded test only.

## 11. Hard Stop Confirmation

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
real_artifact_recovery_classification_receipt.md
```

with:

```markdown
# Hermes Real Artifact Recovery Classification Receipt v0

## Verdict

[HERMES_REAL_ARTIFACT_RECOVERY_CLASSIFICATION_RECEIPT]

## Files Read

## Files Written

## Explicit Non-Actions

## Terminal Summary
```

## 9. Terminal Summary

When finished, print:

```text
HERMES_REAL_ARTIFACT_RECOVERY_CLASSIFICATION_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/real_artifact_recovery_classification_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_real_artifact_recovery_classification_v0/real_artifact_recovery_classification_receipt.md
    verdict: [HERMES_REAL_ARTIFACT_RECOVERY_CLASSIFICATION_RETURNED_WITH_WATCH]
    watch: real artifacts must not be over-recovered into authority; Codex decides final recovery
```

