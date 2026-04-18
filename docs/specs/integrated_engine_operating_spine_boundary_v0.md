# Integrated Engine Operating Spine Boundary v0

## 1. Purpose

This note reframes the current integrated engine as an operating spine, not a final all-in-one app.

The spine is the minimal continuity path:

`request interpretation -> package formation -> worker handoff -> return recording -> reread/reuse continuity`

The UI is one attachable surface above this spine. It should help a selected package continue work, not try to display the whole philosophy or become a multi-agent dashboard.

## 2. What The Spine Is

The spine is the contract layer that lets a work request become a package, lets a worker receive a bounded handoff, records the run, and lets the same package continue from prior runs.

It currently projects existing runtime data from:

- CLI sessions under `runtime/cli_sessions`
- package run events under `runtime/events/integrated_engine_package_run_events.jsonl`
- package notebooks exposed through `cli_host_control.package_notebooks`

## 3. What The Spine Is Not

The spine is not:

- a full product UI
- multi-agent orchestration
- automatic worker dispatch
- automatic line / axis detection
- canonical ingestion
- final artifact viewer
- broad UI expansion

## 4. Contract Objects

### Package

Fields:

- `id`
- `title`
- `goal`
- `scope`
- `stage`
- `status`
- `route_label`
- `active_worker`
- `context_refs[]`
- `artifact_refs[]`
- `prior_run_ids[]`
- `notebook_id`

Role:

The package is the durable work vessel. It holds goal, context, prior runs, artifacts, current route, and the notebook pointer.

### HandoffPacket

Fields:

- `packet_id`
- `package_id`
- `worker_role`
- `task_brief`
- `bounded_context_refs[]`
- `explicit_inputs[]`
- `constraints[]`
- `expected_return_shape`
- `escalation_rule`
- `stop_rule`

Role:

The handoff packet is what a worker should receive instead of rereading the whole UI or chat. It is bounded and stop-rule aware.

### RunRecord

Fields:

- `run_id`
- `package_id`
- `worker`
- `input_packet_id`
- `start_time`
- `end_time`
- `result_summary`
- `return_refs[]`
- `artifact_paths[]`
- `execution_status`
- `route_mark`
- `followup_hint`

Role:

The run record is the durable result of one worker execution. It is not the whole package; it is one turn in the package notebook.

### Notebook

Fields:

- `notebook_id`
- `package_id`
- `latest_run_id`
- `previous_run_ids[]`
- `latest_stage`
- `run_count`
- `result_summary`
- `artifact_refs[]`
- `bounded_context_refs[]`
- `next_continue_hint`

Role:

The notebook is the continuity view for one package. It makes continued work possible by collecting runs, artifacts, and context refs.

### WorkerProfile

Fields:

- `worker_id`
- `type`
- `supported_task_types[]`
- `input_contract`
- `output_contract`
- `strengths`
- `limits`
- `routing_notes`

Role:

The worker profile describes how a future Codex, Gemini, manual, or other worker can attach to the spine. It does not imply orchestration.

## 5. Current Code Projection

The runtime now exposes:

- `cli_host_control.package_notebooks`
- `cli_host_control.package_run_events`
- `cli_host_control.spine_contracts`

`spine_contracts` is an adapter/projection layer over existing data. It does not replace the current session or event storage.

## 6. UI Boundary

The current UI should be a thin package workbench:

- show current package goal / stage / status
- show latest package run
- show artifact refs
- show previous runs
- support `Continue this package`

The UI should not widen into panels just to represent philosophy. Deep engine/event details remain support or inspector material.

## 7. Future Work

Future work should be bounded:

- improve result parsing into clearer run records
- add better artifact viewing
- test a real Codex/Gemini/manual worker handoff through the same HandoffPacket shape
- only later consider multi-worker orchestration
