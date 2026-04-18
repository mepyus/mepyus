# Integrated Engine Input Contract Note v0

## 1. Verdict

PASS_WITH_NOTE

This note defines the current bounded contract of the integrated-engine input side. It is descriptive, not final schema. It is meant to help later packetization work without pretending all input material is already packetized or canonical.

## 2. Input Object Types

### 2.1 Raw Request Trace

- What it is: The user's original instruction, goal, concern, or scope as entered into the current operating flow.
- Likely formed in: User Surface, command/header area, conversation, or supervisor instruction text.
- What it is not: It is not yet an evidence bundle, work packet, engine-ingest-ready material, or final decision.
- Downstream consumer: VectorFL interpretation / mediation layer.
- Confusion risk: Treating raw user words as already normalized engine task can skip lens, guard, and evidence formation.

### 2.2 Interpreted Request / Intermediate Formation

- What it is: VectorFL's reading of the request into purpose, object scope, lens, guard, expected return, route, and surface projection.
- Likely formed in: `CliHostControlPanel.tsx`, current work packet formation layer, user instruction interpretation protocol, evidence bundle gate.
- What it is not: It is not execution result, not canonical ingestion, not automatic approval.
- Downstream consumer: Engine request candidates, CLI execution packet, validation/reread queues.
- Confusion risk: Treating interpretation as completion or treating route labels as canonical state.

### 2.3 Candidate Source Material

- What it is: Source refs, context refs, docs, generated outputs, reports, notes, or runtime artifacts that may support the current packet.
- Likely formed in: User-provided refs, `observer_ingest_min/generated`, docs/reports, docs/specs, runtime manifests, runtime reports.
- What it is not: It is not automatically selected evidence or engine-ingest-ready material.
- Downstream consumer: VectorFL evidence bundle gate, process camera evidence lens, execution packet.
- Confusion risk: A file list can look like evidence even when the support reason is missing.

### 2.4 Engine-Ingest-Ready Material

- What it is: Material shaped enough to be handled by the engine as a request, candidate, validation target, deposit candidate, execution packet, or return record.
- Likely formed in: VectorFL packet formation, `runtime/contracts`, `app/runtime/vectorfl_integrated_engine_api.py`, process-camera packet/return flow.
- What it is not: It is not raw source text and not automatically canonical memory.
- Downstream consumer: Engine Surface, runtime API, process/validation/deposit candidate handling.
- Confusion risk: `deposit_candidate` or return record can be misread as already ingested/canonical.

### 2.5 Reference / Preprocessed Feed Material

- What it is: Source material after basic profiling, split, manifesting, trace, and readable board generation.
- Likely formed in: `app/work/observer_ingest_min/run_observer_ingest_min.py`, `app/work/observer_ingest_min/generated`, `app/input_layer` modules.
- What it is not: It is not final line/axis, not governance decision, and not complete engine ingestion.
- Downstream consumer: VectorFL reread/evidence bundle, input-side audits, future packetization, runtime/source views.
- Confusion risk: Preprocessed outputs can be over-promoted because they look structured.

### 2.6 Trace / Return-Adjacent Material

- What it is: Processing traces, operator summaries, return records, reports, validation notes, and redeposit payloads.
- Likely formed in: observer ingest outputs, runtime reports, process camera return records, docs/reports closeouts.
- What it is not: It is not always source input; sometimes it is post-processing memory or supervision record.
- Downstream consumer: Engine memory/redeposit candidates, supervisor, VectorFL reread, future execution packets.
- Confusion risk: Trace material can be mistaken for raw evidence or final authority unless its stage is explicit.

## 3. Maturity / Authority Boundary

| object type | maturity | authority boundary |
| --- | --- | --- |
| Raw request trace | earliest | user intent, not engine task completion |
| Interpreted request | intermediate | VectorFL mediation candidate, not final decision |
| Candidate source material | unbundled or partially bundled | support material until evidence reason is attached |
| Engine-ingest-ready material | bounded handoff-ready | candidate / validation / deposit / packet, not canonical by default |
| Reference/preprocessed feed | source prepared for reading | readable feed, not final line/axis/case |
| Trace/return-adjacent material | post-action or supervision record | redeposit candidate unless explicitly promoted elsewhere |

## 4. Contract Rule

The input side hands forward different object types. It should not flatten them into one "input":

```text
raw request trace
-> interpreted request / intermediate formation
-> candidate source material
-> evidence bundle or preprocessed feed
-> engine-ingest-ready material
-> return / trace / redeposit candidate
```

This is a reading contract. It is not a final API schema.

## 5. Phase 4 Validation

- Object distinction check: passed. Raw request, interpreted request, candidate source, ingest-ready material, preprocessed feed, and trace/return material are separated.
- Fake-finality check: passed. The note does not claim that all input objects are already packetized or canonical.
- Packetization support check: passed with note. The distinctions should help future packet work, but this note does not implement packetization.

