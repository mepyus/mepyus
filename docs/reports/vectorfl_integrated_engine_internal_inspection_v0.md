# VectorFL Integrated Engine Internal Inspection v0

Date: 2026-04-11

## verdict

- The integrated engine is usable as a first operating skeleton.
- The next priority is hardening the shared operating structure for Codex, Gemini CLI, Claude Code, or any future CLI worker.
- The current state is not ready for broad automation.
- The correct next shape is `shared operating contract + worker-visible state + explicit return artifacts`, not more manual form fields.

## inspected scope

Files inspected:

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/runtime/vectorfl_integrated_engine_shell.py`
- `app/core/runtime/viewer_server.py`
- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`
- `scripts/run_line_thickening_sample.py`
- `scripts/run_external_case_flowline_sweep.py`

Also checked:

- integrated-engine latest manifest chain
- current worker-session state
- candidate line-related scripts
- current generated/latest smoke-test state

## current engine shape

The engine currently has three layers:

1. State/API layer:
   - `app/runtime/vectorfl_integrated_engine_api.py`
   - builds state
   - defines latest manifest paths
   - writes work packet / assignment / route / gate / brief / launch gate / worker session
   - runs read-only worker bridges for Codex/internal-read/synthesis

2. Surface layer:
   - `app/runtime/vectorfl_integrated_engine_shell.py`
   - renders `/vectorfl-engine`, `/team`, `/internal`, `/synthesis`
   - shows operator guide, worker session setup, work packet, assignment, reports, gates, glossary

3. Server route layer:
   - `app/core/runtime/viewer_server.py`
   - exposes GET pages and POST actions

This is acceptable for first skeleton, but not yet program-grade separation.

## shared worker reference requirement

Any future tool must be able to enter from the same structure:

- Codex
- Gemini CLI
- Claude Code
- any later CLI worker

They should not depend on hidden chat context.

They should read:

- current work packet
- current assignment
- worker-session latest
- relevant contracts/source packs
- latest report/gate chain
- forbidden scope

They should write only to an explicit return artifact that the supervisor surface can read.

## current latest manifest map

Core chain:

- `runtime/manifests/vectorfl_integrated_engine_work_packet_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_assignment_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_codex_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_supervisor_route_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_internal_read_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_synthesis_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_supervisor_gate_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_implementation_brief_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_implementation_launch_gate_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`

Imported/substrate chain:

- `runtime/manifests/vectorfl_paper_codex_handoff_latest_v0.json`
- `runtime/manifests/vectorfl_paper_codex_return_latest_v0.json`
- `runtime/manifests/vectorfl_paper_gemini_review_latest_v0.json`
- `runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json`
- `runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json`

Important:

- the imported/substrate chain is not the new integrated-engine canonical state
- it is still useful reading material and guard context

## current write surfaces

Writes latest state:

- `create_vectorfl_integrated_engine_work_packet`
- `create_vectorfl_integrated_engine_assignment`
- `emit_codex_handoff_from_assignment`
- `run_codex_assignment_bridge`
- `create_vectorfl_integrated_engine_supervisor_route`
- `run_internal_read_from_supervisor_route`
- `run_synthesis_from_internal_read`
- `create_supervisor_gate_from_synthesis`
- `create_implementation_brief_from_supervisor_gate`
- `create_implementation_launch_gate`
- `create_vectorfl_integrated_engine_worker_session`
- `create_worker_session_from_current_context`

Read/build state:

- `build_vectorfl_integrated_engine_state`
- `_cell_registry`
- `_team_registry`
- `_engine_loop`

Risk:

- many actions write latest manifests directly
- this is fine for first skeleton, but later program form should separate:
  - draft
  - preview
  - supervisor-approved latest
  - worker return

## worker-session state

Current worker session artifact:

- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`

Current role:

- primary worker: `codex`
- secondary worker: `gemini`
- Gemini model/session memo: `gemini-cli default`
- status: `configured_not_running`

Current meaning:

- this config is visible to the supervisor
- it does not execute Gemini
- it does not modify the repo
- it is a shared setup record for terminal/page synchronization

This is good direction, but the next return slot is still missing.

Missing:

- no `vectorfl_integrated_engine_gemini_line_return_latest_v0.json`
- no Gemini line-thickening report shape
- no translation material return shape
- no explicit "Gemini inspected these scripts and recommends these next actions" artifact

## script candidate inspection

Confirmed existing runnable candidates:

- `scripts/run_line_thickening_sample.py`
- `scripts/run_external_case_flowline_sweep.py`

Removed from auto-config candidates because not present in this workspace:

- `app/work/stage0_reboot/scripts/observe/run_material_diversity_space_expansion.sh`
- `app/work/stage0_reboot/scripts/observe/run_adjacent_topic_cluster_expansion.sh`

Why this matters:

- a shared operating engine cannot hand other CLI tools dead paths as current instructions
- missing paths can be archived as historical references only after confirmed
- worker-session auto-config should only show runnable or inspectable candidate scripts by default

Current candidate roles:

- `scripts/run_line_thickening_sample.py`
  - sample line-thickening observation writer
  - writes to a runtime root provided by `--runtime-root`, defaulting to `runtime/line_thickening_demo`
  - useful as a sample, not necessarily as the next production line-thickening engine

- `scripts/run_external_case_flowline_sweep.py`
  - reads `inputs/external_cases`
  - writes generated sweep output under `app/work/archive_review/external_case_support/external_case_flowline_sweep/generated`
  - useful for flowline contact detection
  - not read-only because it writes a timestamped generated file

## current smoke-test caveat

Current latest work packet/assignment is still smoke-test state:

- `button validation duplicate guard smoke test`

This should not drive the next real Gemini/Codex run.

Before a real internal line/translation run:

- create a fresh work packet for the actual task
- then auto-config worker session from that current context
- then decide whether Gemini should inspect scripts or run one bounded script

## CLI tool contract

Any future CLI worker should receive this contract:

Input:

- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_work_packet_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_assignment_latest_v0.json`
- relevant contracts/source packs listed in state

Allowed:

- read files
- inspect script purpose
- propose which scripts are safe to run
- produce line-thickening and translation-material report
- summarize blockers

Forbidden by default:

- modify repo
- replace current slot
- declare gate close
- treat generated script output as product completion
- promote candidates
- run broad orchestration

Required return:

- summary
- files/scripts inspected
- line candidates or thickening opportunities
- translation material candidates
- recommended next action
- blockers
- whether supervisor decision is required

## recommended next hardening

Next implementation should be small:

1. Define a Gemini line/translation return artifact shape.
2. Add one latest return path, for example:
   - `runtime/manifests/vectorfl_integrated_engine_gemini_line_return_latest_v0.json`
3. Add a read-only or report-only bridge path that consumes worker-session latest.
4. Show the latest Gemini line/translation return in the team page.

Do not yet:

- build a scheduler
- run multiple workers
- create history
- change current slot
- close actual_export_only gate
- expand page architecture broadly

## supervisor judgment

The integrated engine is now good enough to support internal inspection and shared CLI coordination.

It is not yet ready to delegate operational authority.

The next durable step is to make Gemini's expected return explicit, so that "Gemini is helping" becomes a visible return artifact instead of another terminal-side memory burden.

## worker/tool registry hardening update

The first registry hardening pass has been applied.

Changed:

- `WORKER_REGISTRY` now centralizes currently supported worker identities:
  - `codex`
  - `gemini`
  - `claude_code`
- `LINE_SCRIPT_CANDIDATE_REGISTRY` now centralizes runnable/inspectable line-script candidates:
  - `scripts/run_line_thickening_sample.py`
  - `scripts/run_external_case_flowline_sweep.py`
- `TRANSLATION_MATERIAL_BASELINE` now centralizes default translation-material targets.
- integrated engine state now exposes:
  - `worker_registry`
  - `line_script_candidate_registry`
  - `translation_material_baseline`
- the worker-session surface reads worker select options from `worker_registry` instead of hardcoding them in the HTML shell.

Why:

- future tools should be added by changing a registry/config shape, not by chasing scattered UI strings
- the integrated engine should support Codex/Gemini/Claude Code or later CLI workers as interchangeable workers with different authority levels
- the supervisor should still see the selected worker/model/session on the page

Guard:

- this is not a scheduler
- this does not run any CLI
- this does not grant Gemini or Claude Code operating authority
- this does not alter current slot, gate, or candidate promotion state

Remaining gap:

- worker profiles are still code-level constants, not external operator-editable config files
- this is acceptable for the first hardening pass
- if tool switching becomes frequent, move the registry into a dedicated contract/manifest after the return artifact shape is locked

## operating dialogue baseline update

Added a bounded operating dialogue surface and API:

- page: `/vectorfl-engine/operate`
- action: `/api/vectorfl-engine/actions/operating-dialogue`
- artifact: `runtime/manifests/vectorfl_integrated_engine_operating_dialogue_latest_v0.json`

Interpretation:

- Codex remains the default operating worker.
- Gemini CLI, Claude Code, and later tools are selectable through the same registry path.
- The dialogue action records configuration and can update worker-session latest.
- It does not run any CLI, schedule workers, replace slots, promote candidates, or declare gate close.

Why this matters:

- the supervisor should not need to manually edit every setup field
- the integrated engine needs a conversation-to-configuration seam before real in-page worker execution
- other CLI tools can inspect the latest dialogue + worker-session artifacts to understand the current operating intent

## worker launch draft boundary update

Added a non-executing worker launch draft path:

- action: `/api/vectorfl-engine/actions/worker-launch-draft`
- artifact: `runtime/manifests/vectorfl_integrated_engine_worker_launch_draft_latest_v0.json`
- source: latest operating dialogue + latest worker-session

Interpretation:

- this records the command family, command preview, input mode, selected worker/model, prompt material, and guard scope
- it is the next seam before real CLI invocation, not the invocation itself
- it keeps Codex/Gemini/Claude Code swappable through registry metadata

Guard:

- no CLI execution
- no repo modification
- no scheduler
- no current slot replacement
- no candidate promotion
- no gate close

## worker launch execution update

Added the first actual CLI execution path from latest launch draft:

- action: `/api/vectorfl-engine/actions/run-worker-launch-draft`
- artifact: `runtime/manifests/vectorfl_integrated_engine_worker_execution_latest_v0.json`

Execution posture:

- Codex runs through `codex exec --skip-git-repo-check --sandbox read-only --cd <repo> -`
- Gemini can run through the same launch-draft boundary when selected and available
- Claude Code is still disabled until configured and tested

Guard:

- latest execution result is evidence only
- no current slot replacement
- no candidate promotion
- no gate close
- no scheduler or queue

Validation note:

- read-only Codex CLI execution succeeded through the integrated engine HTTP route after restarting the viewer server with network access
- the execution report confirmed that current latest work packet / assignment are still smoke-test artifacts
- next safe step is not broader execution; it is a bounded Gemini line/translation return slot/schema before asking Gemini to produce line-thickening or translation material
