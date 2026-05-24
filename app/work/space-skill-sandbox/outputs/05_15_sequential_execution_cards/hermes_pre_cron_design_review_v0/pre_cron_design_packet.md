# Hermes Pre-Cron Design Packet v0

## 1. Verdict

[HERMES_PRE_CRON_DESIGN_PACKET_WITH_WATCH]

## 2. Read Scope

Files read:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md
- app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md

Files missing:
- none

Files explicitly not read:
- ~/.hermes/cron/jobs.json
- Hermes config, memory, skill, session, auth, gateway, and cron state files
- AGENTS.md, SKILL.md, current-position, output_manifest, registry, schema, workflow, ontology, baseline files
- sibling folders under the listed sandbox output paths
- secrets, auth files, state.db, .env, sessions, credential logs
- repo-wide tree, broad search results, linked files, or network resources

## 3. Cron Candidate Summary

job_name_candidate:
- vectorfl_candidate_surface_watch_manual_v0

purpose:
- Design a future Hermes automation candidate that checks a small explicit VectorFL candidate surface set for evidence or boundary changes significant enough to ask Codex/User for review, without updating VectorFL state, memory, baseline, registry, schema, workflow, ontology, or authority surfaces.

current_status:
- pre-cron design only; HOLD for real cron creation.

why_not_real_cron_yet:
- The prior pilots support bounded one-shot runner behavior with WATCH, but they do not prove recurring automation safety.
- Fresh-session cron prompts must be self-contained and still require Codex/User approval before any real schedule is registered.
- The existing evidence is candidate-level only and explicitly warns against recurring automation, promotion, standard-interface claims, memory/skill/config drift, and broad repo search.
- A deterministic no-agent script design should be reviewed before any real Hermes cron job exists.

## 4. Fresh-Session Prompt Draft

```text
You are Hermes Agent running a future candidate VectorFL pre-approved automation job.

This is a bounded candidate-surface watch task, not VectorFL authority.
Run only if this job has been explicitly approved by Codex/User after pre-cron design review.

Mission:
Read only the explicit files listed below. Do not search the repo, inspect siblings, follow links, read secrets, or use network. Produce one local markdown report in the declared sandbox output path. Do not update VectorFL state, current-position, output_manifest, baseline, registry, schema, workflow, ontology, AGENTS.md, SKILL.md, Hermes memory, Hermes skills, Hermes config, or Hermes cron state.

Explicit input files:
1. app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md
2. app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md
3. app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md
4. app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md
5. app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md

Declared output path:
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_candidate_surface_watch_v0/candidate_surface_watch_report.md

Check mechanically for:
- IIC, SOF, MOL, RML
- SOF current authority wins
- RML evidence cannot grant authority
- MOL read-only
- bounded carrier
- 1-5 explicit files
- no automation / no recurring automation / no cron job
- no Hermes memory edit / no Hermes skill creation / no Hermes config edit
- no baseline promotion / no workflow/schema/registry/ontology creation

Return a markdown report with:
1. verdict: CANDIDATE_SURFACE_WATCH_WITH_WATCH
2. files read and missing
3. detected vessel and boundary terms
4. any missing or weakened terms
5. WATCH items
6. HOLD items
7. Codex recovery handoff: what Codex should review next

STOP if:
- more than 5 inputs are required
- any input path is unclear
- broad repo search or sibling inspection seems needed
- any authority, promotion, baseline, workflow, registry, schema, ontology, memory, skill, config, gateway, or cron-state action is requested
- any network/package install/secret/session/log reading is needed

This job should only produce the declared report. It must not modify input files or create recurring automation.
```

## 5. Explicit Inputs

| File | Purpose | Sensitive? | Required? |
|---|---|---|---|
| app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_VESSEL_WORKING_STANDARD_CANDIDATE_V0.md | Vessel standard candidate and IIC/SOF/MOL/RML authority rules | no | yes |
| app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/HERMES_VECTORFL_SPACE_RECOGNITION_AND_ASSET_USE_TEST_RETURN_V0.md | Prior bounded space-recognition / asset-use evidence and drift warnings | no | yes |
| app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_external_runner_pilot_v0/vessel_runner_pilot_report.md | Prior tiny implementation runner report | no | yes |
| app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_report.md | Prior one-shot automation session report and automation boundary findings | no | yes |
| app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_automation_session_pilot_v0/automation_session_receipt.md | Prior one-shot automation receipt and boundary confirmation | no | optional but preferred |

## 6. Output Contract

declared_output_path:
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_candidate_surface_watch_v0/candidate_surface_watch_report.md

allowed_writes:
- one declared markdown report under the declared sandbox output path if the future job is explicitly approved.
- no other files.

forbidden_writes:
- ~/.hermes/cron/jobs.json, Hermes config, Hermes memory, Hermes skills, AGENTS.md, SKILL.md, VectorFL baseline, registry, schema, workflow, ontology, current-position, output_manifest, local core / derived / surface authority files, input files, sibling folders, or recurring automation artifacts.

## 7. Script / No-Agent Decision

recommended_mode:
- no-agent script preferred for the future candidate, if a real cron is ever approved.

why:
- The task is mechanical: read explicit files, detect phrases, compare missing/weak terms, and write a fixed markdown report.
- Avoiding an LLM reduces authority-language drift, hidden interpretation, memory/skill temptation, and prompt expansion.
- If the job only needs deterministic checks, Hermes cron no_agent=True with a script is safer than a full fresh LLM session.

script_outline:
- define the 5 explicit input paths and one declared output path.
- read existing inputs only; record missing files.
- check for expected vessel terms and boundary phrases via plain string matching.
- produce markdown sections: verdict, read scope, detection tables, missing/weak terms, WATCH, HOLD, Codex recovery handoff.
- exit non-zero only if the declared output path cannot be written or a hard boundary condition is triggered.
- do not import non-standard libraries, call network, call subprocess, run hermes cron commands, or modify inputs.

## 8. Schedule / Trigger Design

recommended_trigger:
- manual-trigger-first, not recurring.

why:
- The current evidence supports one-shot bounded runner behavior, not autonomous recurring authority.
- Manual trigger lets Codex/User inspect each run before any repeated scheduling is considered.
- The job concerns authority-sensitive candidate evidence and should not silently accumulate or normalize repeated automation.

why_not_recurring_yet:
- No real cron safety review has been approved.
- Failure behavior, delivery semantics, and Codex recovery loop are not yet validated under actual cron fresh-session conditions.
- Recurrence could create pressure toward workflow standardization, memory drift, or false authority through repetition.

## 9. Toolset Design

enabled_toolsets_needed:
- file only for an LLM-driven one-shot design, or no-agent script mode if using Hermes cron after approval.

disabled_toolsets:
- web, browser, terminal except script execution handled by cron itself, cronjob during the job body, memory, skills, gateway/messaging except a declared delivery mechanism, delegation, image/video/tts, and any toolset that enables network, broad search, config edits, or persistent state changes.

why:
- The task only needs explicit file reads and one declared markdown write.
- Extra tools increase the risk of broad search, network use, hidden persistence, skill/memory/config drift, or real cron mutation.

## 10. STOP Conditions

- More than 5 input files are required.
- Input file list is unclear or asks for sibling inspection.
- Broad repo search, recursive scan, or linked-file following is requested.
- Any secret, auth file, state.db, .env, session, or credential log is needed.
- Any real Hermes cron command or ~/.hermes/cron/jobs.json edit is requested.
- Gateway install, recurring automation, or cron job creation is requested.
- Hermes memory, skill, or config edit is requested.
- AGENTS.md, SKILL.md, baseline, registry, schema, workflow, ontology, current-position, or output_manifest update is requested.
- Any local core / derived / surface authority change is requested.
- The report language starts claiming proof, stable carrier, standard interface, integration-complete status, baseline readiness, or VectorFL authority.
- RML evidence is used as authority, or MOL read-only route mapping becomes automation/workflow/script execution.

## 11. Failure Behavior

If input missing:
- Continue with existing explicit files, list missing files in the report, mark WATCH, and do not infer from unprovided files.

If output path unavailable:
- STOP and report failure to the terminal if possible; do not write elsewhere or create fallback paths outside the declared sandbox.

If evidence ambiguous:
- Mark WATCH and route to Codex recovery; do not promote, decide authority, or expand scope.

If any authority pressure appears:
- STOP; record HOLD language in the report if a report can still be safely written to the declared output path; otherwise return a concise failure summary.

## 12. Codex Recovery Handoff

What Hermes returns:
- A local markdown report showing read scope, missing inputs, detected terms, missing/weak boundary terms, WATCH, HOLD, and a recommendation to ask Codex/User before any next step.

What Codex analyzes:
- Whether the job stayed explicit-file only, whether no-agent mode is sufficient, whether STOP conditions fired correctly, whether SOF-over-RML and MOL-read-only are preserved, whether output language avoids promotion, and whether real cron is still HOLD.

What User decides:
- Whether to keep using manual one-shot pilots, request another design pass, approve a no-agent one-shot cron run, or continue holding all real cron/recurring automation.

## 13. Real Cron Readiness Checklist

| Criterion | Ready? | Gap |
|---|---:|---|
| Self-contained fresh-session prompt exists | partial | Draft exists here, but Codex/User must approve exact final text. |
| Explicit input list <= 5 files | yes | Future changes must not add files without review. |
| Declared output path only | partial | Candidate path proposed; must be approved before use. |
| No-agent deterministic script decision | partial | Recommended, but actual script and cron packaging are not yet reviewed. |
| Manual-trigger-first design | yes | Recurring schedule remains HOLD. |
| Recurring schedule safety | no | Needs separate authority review after manual runs. |
| Delivery target | partial | Local markdown only recommended; actual delivery semantics not approved. |
| Toolsets minimized | partial | File/no-agent design proposed; final cron tool restrictions still need approval. |
| STOP conditions sufficient | partial | Good draft exists; Codex should stress-test before real cron. |
| Failure behavior defined | partial | Draft exists; needs validation in a one-shot no-agent trial. |
| Codex recovery handoff clear | partial | Handoff is specified but not yet exercised under real cron fresh-session execution. |
| Authority/promotion safeguards | partial | Safeguards are explicit, but recurring repetition remains a drift risk. |
| User approval for real cron | no | Not granted in this design packet. |

## 14. WATCH

- Fresh-session cron requires a fully self-contained prompt; any hidden reliance on prior conversation would fail or drift.
- No-agent script mode is safer than LLM mode, but still needs explicit approval before any real Hermes cron entry exists.
- Manual-trigger-first should not be quietly converted into recurring automation.
- Repeated reports can create false authority through familiarity even when each report says candidate/WATCH.
- Local markdown delivery avoids gateway/service risk, but Codex recovery still has to happen explicitly.

## 15. HOLD

- no real Hermes cron job created
- no ~/.hermes/cron/jobs.json edit
- no hermes cron command run
- no gateway install
- no recurring automation
- no Hermes skill creation
- no Hermes memory edit
- no Hermes config edit
- no AGENTS.md update
- no SKILL.md creation
- no baseline promotion
- no workflow/schema/registry/ontology creation
- no current-position update
- no output_manifest update
- no local core / derived / surface authority change
- no broad repo search
- real cron remains HOLD until Codex/User explicitly approve a final self-contained no-agent/manual-trigger design
