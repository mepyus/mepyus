# Integrated Engine Supervisor Handoff Protocol v0

## 1. Purpose

This protocol defines the minimum notebook signals a supervisor needs to decide the next bounded action for a package.

It is not a multi-agent protocol, UI expansion plan, or automatic routing rule. It is a supervisor reading protocol over the current package notebook.

## 2. Minimum Notebook Signals

A supervisor should first read these fields:

- `package_id`
- `package_title`
- `run_count`
- latest `status`
- latest `worker_return_source`
- latest `route_label`
- latest `answer`
- latest `findings[]`
- latest `files_artifacts[]`
- latest `next_continue_hint`
- latest `risks_or_limits[]`
- latest `source_refs[]`

Raw logs are not the first read path. They are inspection artifacts used when the notebook explicitly signals weak, failed, or ambiguous material.

## 3. Source Confidence Guide

| Source | Supervisor posture |
| --- | --- |
| `worker_emitted` | Strongest notebook read path. Can usually support continue or close if findings, refs, and hint are concrete. |
| `runtime_normalized` | Usable for spine/context validation. Usually needs bounded continuation or validation before content promotion. |
| `parser_fallback` | Usable but weaker. Good for rerun or narrow reread when answer/findings are thin or generic. |
| `raw_fallback` | Inspect-first or hold. Do not continue as if successful unless raw artifacts are checked. |

## 4. Decision Rules

### Continue

Use when:

- latest status is `done`
- latest source is `worker_emitted` or otherwise readable
- `answer` and `findings[]` are specific enough
- `next_continue_hint` names a concrete next bounded step
- risks are limitations, not hard blockers

Minimum fields:

- `answer`
- `findings[]`
- `next_continue_hint`
- `source_refs[]`
- `risks_or_limits[]`

### Hold

Use when:

- latest status is failed/running/ambiguous, or
- `worker_return_source` is `raw_fallback`, or
- risks indicate execution failure, invalid boundary, or no reliable findings

Minimum fields:

- `status`
- `worker_return_source`
- `risks_or_limits[]`
- `files_artifacts[]`

### Rerun

Use when:

- package goal is still valid
- previous output is too thin, parser-derived, or failed due to environment/format rather than task invalidity
- bounded context refs are available for a cleaner worker attempt

Minimum fields:

- `worker_return_source`
- `answer`
- `findings[]`
- `next_continue_hint`
- `source_refs[]`
- `risks_or_limits[]`

### Inspect

Use when:

- notebook says material exists but quality is uncertain
- risks point to failure, parse fallback, missing block, or artifact-specific ambiguity
- supervisor needs raw stdout/stderr/operator report before continuing

Minimum fields:

- `files_artifacts[]`
- `source_refs[]`
- `risks_or_limits[]`
- `status`
- `worker_return_source`

### Close

Use when:

- latest run answers the current bounded package purpose
- concrete findings and artifact refs exist
- remaining risks are clearly recorded and do not require immediate rerun
- next step belongs to a new package or later phase rather than this package

Minimum fields:

- `answer`
- `findings[]`
- `files_artifacts[]`
- `risks_or_limits[]`
- `next_continue_hint`

Close does not mean global promotion. It means this package has produced enough bounded material for the next supervisor decision.

## 5. Notebook-Only / Deep-Inspection Boundary

Notebook-only is enough when:

- `worker_return_source` is strong or clearly labeled
- answer/findings are concrete
- next_continue_hint is specific
- risks are understandable without raw text

Deep inspection is needed when:

- source is `raw_fallback`
- status is failed or still running
- parser fallback output is too thin
- artifact quality is the actual question
- supervisor must verify stdout/stderr before rerun or close

## 6. Guardrails

This protocol does not authorize:

- automatic worker dispatch
- package promotion
- canonical ingestion
- line / axis validation
- broad UI or dashboard expansion
- treating fallback material as equal to worker-emitted return

