# Runtime API Response Key Inspection — 2026-05-09

## 0. Status

- source-evidence inspection only
- observation-map support only
- not schema
- not API contract authority
- not automation
- not dashboard redesign
- requires Supervisor/Gemini review

## 1. Source / Provenance Note

Files inspected:

- `scripts/run_viewer_server.py`
- `app/core/runtime/viewer_server.py`
- `app/runtime/vectorfl_integrated_engine_api.py`

Search terms used:

```text
build_vectorfl_integrated_engine_state
vectorfl-engine/state
cli_host_control
latest_readable_return
package_run_events
recent_readable_returns
```

Directly observed:

- `scripts/run_viewer_server.py` imports `run_viewer_server` and defaults to runtime root `runtime`, host `127.0.0.1`, and port `8421`.
- `app/core/runtime/viewer_server.py` maps `GET /api/vectorfl-engine/state` to `build_vectorfl_integrated_engine_state(runtime_root)`.
- `build_vectorfl_integrated_engine_state` returns a large dict with operating posture, guard, worker policy, manifests, registries, engine loop, operating board, bridge substrate, implementation boundary, and `cli_host_control`.
- `build_cli_host_control_state` builds the CLI/control nested shape with latest return, recent returns, deposit-ready returns, package run events, package notebooks, spine contracts, and guard flags.

Inference:

- A future Runtime State Observation Map should read a small set of top-level status keys plus selected `cli_host_control` nested keys before reading larger manifests, registries, or raw previews.
- Long preview fields and arrays should be summarized by keys/counts/status first.

Missing evidence:

- Backend was not executed in this inspection task.
- No live sample JSON was called in this inspection task.
- Nested shapes for every manifest and registry were not exhaustively mapped.

Needs Supervisor review:

- Which keys Gemini should include in a 20-line observation map.
- Whether any runtime key should be considered stale, historical, or too broad for first-read use.

## 2. Endpoint / Builder Link

```text
endpoint:
GET /api/vectorfl-engine/state

handler_file:
app/core/runtime/viewer_server.py

response_builder_function:
build_vectorfl_integrated_engine_state(runtime_root)

runtime_root_source:
scripts/run_viewer_server.py accepts argv[1] or defaults to Path("runtime"); viewer_server passes runtime_root into the response builder.

provenance:
OBSERVED_FILE_EVIDENCE
```

## 3. Top-Level Response Key Table

| Key | Observed Shape / Type | Purpose | Read First? | Watch | Provenance |
| --- | --------------------- | ------- | ----------- | ----- | ---------- |
| `schema_version` | string | identify state shape/version | yes | not schema authority | OBSERVED_FILE_EVIDENCE |
| `surface_role` | string | names engine-level operating surface | yes | role label may be conceptual | OBSERVED_FILE_EVIDENCE |
| `route` | string | route label for engine surface | yes | not HTTP route list | OBSERVED_FILE_EVIDENCE |
| `current_posture` | string from supervisor decision | status/posture signal | yes | depends on latest manifest freshness | OBSERVED_FILE_EVIDENCE |
| `core_sentence` | string | operating summary sentence | yes | not proof of state | OBSERVED_FILE_EVIDENCE |
| `guard` | dict of booleans | safety / non-promotion guardrails | yes | guard presence is not enforcement proof | OBSERVED_FILE_EVIDENCE |
| `session_worker_policy` | nested dict | worker/model role policy | maybe | can be long; summarize | OBSERVED_FILE_EVIDENCE |
| `contracts` | dict of path state objects | contract file availability | maybe | path existence, not semantic validity | OBSERVED_FILE_EVIDENCE |
| `source_packs` | dict of path state objects | source pack availability | no by default | can distract from runtime state | OBSERVED_FILE_EVIDENCE |
| `worker_registry` | dict/list constant | available worker definitions | maybe | not live worker health | OBSERVED_FILE_EVIDENCE |
| `cli_host_control` | nested dict | CLI/session/control state | yes | contains arrays and previews; avoid full dump | OBSERVED_FILE_EVIDENCE |
| `language_loop_control` | nested state from helper | language loop state | no by default | not inspected in this task | OBSERVED_FILE_EVIDENCE + MISSING_EVIDENCE |
| `line_script_candidate_registry` | list with `exists` flags | candidate script availability | maybe | not safety proof | OBSERVED_FILE_EVIDENCE |
| `translation_material_baseline` | list with `exists` flags | translation material availability | no by default | historical/baseline wording risk | OBSERVED_FILE_EVIDENCE |
| `latest_manifests` | dict of path states | manifest availability | maybe | path state only | OBSERVED_FILE_EVIDENCE |
| `latest_work_packet` | manifest dict | latest work packet | maybe | may be large/stale | OBSERVED_FILE_EVIDENCE |
| `latest_assignment` | manifest dict | latest assignment | maybe | may be stale | OBSERVED_FILE_EVIDENCE |
| `latest_codex_run` | manifest dict | latest Codex run | maybe | do not dump raw run | OBSERVED_FILE_EVIDENCE |
| `latest_supervisor_route` | manifest dict | latest route | maybe | supervisor decision may need context | OBSERVED_FILE_EVIDENCE |
| `latest_internal_read_report` | manifest dict | latest internal report | no by default | likely larger semantic material | OBSERVED_FILE_EVIDENCE |
| `latest_internal_read_run` | manifest dict | latest internal read run | no by default | raw/process detail risk | OBSERVED_FILE_EVIDENCE |
| `latest_synthesis_report` | manifest dict | latest synthesis report | no by default | likely semantic summary, not runtime status | OBSERVED_FILE_EVIDENCE |
| `latest_synthesis_run` | manifest dict | latest synthesis run | no by default | raw/process detail risk | OBSERVED_FILE_EVIDENCE |
| `latest_supervisor_gate` | manifest dict | gate state | maybe | gate label is not final user decision | OBSERVED_FILE_EVIDENCE |
| `latest_implementation_brief` | manifest dict | implementation brief | maybe | not current build proof | OBSERVED_FILE_EVIDENCE |
| `latest_implementation_launch_gate` | manifest dict | launch gate | maybe | gate can be stale | OBSERVED_FILE_EVIDENCE |
| `latest_worker_session` | manifest dict | worker session config | maybe | config is not execution result | OBSERVED_FILE_EVIDENCE |
| `latest_operating_dialogue` | manifest dict | latest operating dialogue | no by default | likely verbose | OBSERVED_FILE_EVIDENCE |
| `latest_worker_launch_draft` | manifest dict | worker launch draft | maybe | draft is not executed work | OBSERVED_FILE_EVIDENCE |
| `latest_worker_execution` | manifest dict | worker execution state | maybe | inspect shape before trusting status | OBSERVED_FILE_EVIDENCE |
| `cell_registry` | list from helper | operating cells | no by default | registry may be large | OBSERVED_FILE_EVIDENCE |
| `team_registry` | list from helper | team/worker registry | no by default | registry may be large | OBSERVED_FILE_EVIDENCE |
| `engine_loop` | list from manifests | loop projection | maybe | derived from manifests | OBSERVED_FILE_EVIDENCE |
| `operating_board` | nested dict | decision queue / active cases / remaining gates | yes for posture | can become dashboard narrative | OBSERVED_FILE_EVIDENCE |
| `bridge_substrate` | nested dict | bridge/gate/comparison status | maybe | older substrate layer can over-anchor | OBSERVED_FILE_EVIDENCE |
| `next_implementation_boundary` | nested dict | first real object/actions/do-not-build list | yes for next setup | candidate boundary, not roadmap authority | OBSERVED_FILE_EVIDENCE |

## 4. Nested Key Notes

### cli_host_control

```text
observed_fields:
schema_version
position
not_a_surface
primary_observation_surface
session_root
adapter_contract
available_backends
available_task_types
available_marks
index
latest_session
latest_structured_return
latest_deposit_candidate_preview
latest_operator_report_preview
latest_readable_return
recent_readable_returns
deposit_ready_returns
package_run_events
package_notebooks
spine_contracts
guard

useful_for:
CLI/control readiness, latest return status, recent activity, package run event visibility, bounded worker/session continuity.

default_read:
schema_version, position, not_a_surface, primary_observation_surface, available_backends, available_task_types, available_marks, latest_readable_return summary, counts for recent_readable_returns/package_run_events/package_notebooks.

avoid_full_dump:
index, latest_session, latest_structured_return, previews, recent arrays, package_run_events, package_notebooks, spine_contracts.

watch:
This is an observation/control state, not proof that run/mark actions are safe.

provenance:
OBSERVED_FILE_EVIDENCE
```

### latest_readable_return

```text
observed_fields:
session_id
backend_kind
task_type
status
purpose_text
suggested_next_use
route_label
marks
mark_history
structured_return_preview
deposit_candidate_preview
operator_report_preview
session_path
structured_return_path
deposit_candidate_path
operator_report_path

useful_for:
Latest result/judgment signal, route/watch/deposit candidate reading, artifact path discovery.

default_read:
session_id, backend_kind, task_type, status, suggested_next_use, route_label, marks, session_path, structured_return_path.

avoid_full_dump:
structured_return_preview, deposit_candidate_preview, operator_report_preview, mark_history unless needed.

watch:
Preview text is truncated and should not replace reading the artifact when semantic judgment is needed.

provenance:
OBSERVED_FILE_EVIDENCE
```

### recent_readable_returns

```text
observed_fields:
List of up to 8 session-shaped summaries with session_id, backend_kind, task_type, status, purpose_text, suggested_next_use, route_label, marks, mark_history, previews, artifact paths, started_at, ended_at.

useful_for:
Recent activity and continuity scan.

default_read:
count plus session_id/status/route_label/suggested_next_use for the first few entries.

avoid_full_dump:
all previews and full mark_history across the list.

watch:
Recent list is an activity surface, not causal proof; use bounded RUNLOG/raw trace if causality is the question.

provenance:
OBSERVED_FILE_EVIDENCE
```

### package_run_events

```text
observed_fields:
Read by `_read_package_run_events(repo_root, 80)` and returned as `package_run_events[:24]` inside cli_host_control.

useful_for:
Package/run event sequence, UI activity rail, package-specific current/history events.

default_read:
count, latest few event ids/types/status/session/package labels if available.

avoid_full_dump:
all 24 events by default; underlying ledger/raw event file unless event-level causality is required.

watch:
Event sequence supports process observation but not full root-cause proof by itself.

provenance:
OBSERVED_FILE_EVIDENCE + CODEX_INFERENCE
```

### status / refresh / error / staleness fields

```text
observed_fields:
current_posture
guard
bridge_substrate.*_status
latest_* manifest dicts
latest_readable_return.status
recent_readable_returns[].status
package_run_events[].status if present
next_implementation_boundary

useful_for:
Top-level status, readiness posture, latest result state, missing/stale layer detection.

default_read:
current_posture, guard, latest_readable_return.status, latest_readable_return.route_label, latest_readable_return.suggested_next_use, next_implementation_boundary.first_real_object/actions/do_not_build_yet.

avoid_full_dump:
latest_* manifests, bridge_substrate narratives, operating_board active cases unless specifically needed.

watch:
There is no explicitly observed `stale` or `error` top-level key in the builder; staleness must be inferred from timestamps/paths/statuses or checked by live sample.

provenance:
OBSERVED_FILE_EVIDENCE + CODEX_INFERENCE
```

## 5. Candidate Runtime Observation Map Inputs

```text
Status:
schema_version, surface_role, current_posture, guard, latest_readable_return.status

Latest result / judgment:
cli_host_control.latest_readable_return: session_id, backend_kind, task_type, suggested_next_use, route_label, marks, artifact paths

Recent activity:
cli_host_control.recent_readable_returns count + first few session_id/status/route_label

Control readiness:
cli_host_control.position, not_a_surface, primary_observation_surface, available_backends, available_task_types, available_marks, adapter_contract

Package/run events:
cli_host_control.package_run_events count + latest few event status/session/package labels

Staleness / error:
current_posture, latest_readable_return.status, started_at/ended_at in recent returns, latest_manifests path states, missing session_id/path fields

Do not dump by default:
latest_structured_return, latest_session, previews, full recent arrays, full package_run_events, package_notebooks, spine_contracts, latest_* manifests, cell/team registries, operating_board narratives
```

## 6. Gaps / Missing Evidence

```text
gap:
live sample freshness
why it matters:
source code shows shape, but current runtime data can be stale or missing
current evidence:
builder function and nested dict keys inspected
recommended next check:
Gemini or Supervisor can use recent live sync summary as runtime sample, or request one bounded sample if needed
```

```text
gap:
full nested manifest shapes
why it matters:
latest_* manifest values may contain important state or large payloads
current evidence:
top-level keys observed in builder only
recommended next check:
read only selected manifest shape when a missing layer requires it
```

```text
gap:
explicit staleness/error contract
why it matters:
observation map needs to know how to detect stale runtime data
current evidence:
no explicit top-level staleness key observed; statuses/timestamps/paths exist in nested areas
recommended next check:
mark staleness as inferred unless a sample or helper function proves it
```

```text
gap:
package_run_events field shape
why it matters:
events support process observation, but their exact fields are read from another helper/ledger
current evidence:
`_read_package_run_events(repo_root, 80)` and `package_run_events[:24]` observed
recommended next check:
inspect `_read_package_run_events` only if the observation map needs event field names
```

## 7. Recommended Next Step

```text
ROUTE_TO_GEMINI_RUNTIME_OBSERVATION_MAP
```

Gemini should use these source-observed keys to draft a compact Runtime State Observation Map. It should treat the map as a reading lens candidate, not schema or API authority.

## 8. Final Verdict

```text
RUNTIME_API_KEYS_INSPECTED_WITH_WATCH
```

Confidence level:

Medium-high for top-level and `cli_host_control` source-observed keys; medium for event/staleness details because no live sample or full event helper inspection was performed in this task.

Strongest observed evidence:

`/api/vectorfl-engine/state` is directly wired to `build_vectorfl_integrated_engine_state`, which explicitly returns `cli_host_control` and the main runtime/state keys.

Weakest missing evidence:

No explicit staleness/error contract is observed, and package event field shape is only partially inspected.

One next recommended action:

Give this key inspection to Gemini for a 20-line Runtime State Observation Map with strong downshift: map/lens only, not schema.
