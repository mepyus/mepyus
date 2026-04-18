# Integrated Engine Candidate Handling Process Camera v0

## 1. Status

Status: process asset draft, sample-grounded.

This process camera is derived from the completed camera review structuring cycle.
It is not a promoted camera.
It is not a global ontology.
It is not a multi-agent orchestration implementation.

## 2. What This Process Camera Is

The candidate handling process camera is a bounded engine-operating frame for handling a target object as a candidate.

It separates:

- target object: what is being handled
- process camera: how the engine handles it
- execution packet: what a worker receives
- return record: what comes back into the engine

## 3. Problem It Solves

Without this process camera, each new target risks restarting the full validation cycle from scratch.

This process camera preserves the method:

- start from purpose
- lock scope
- discover and compare candidates
- bundle evidence
- validate before action
- decide usable / hold / supplement / insufficient
- form a bounded execution packet
- return a structured record

## 4. Inputs

Minimum inputs:

- current purpose
- target type
- target object or source zone
- candidate source zone
- selected lens set
- known status lock
- allowed actions
- forbidden actions
- expected return shape

Optional inputs:

- prior validation records
- shadow-fit results
- failure/rollback history
- supervisor decision note

## 5. Process Stages

### 1. Request / Purpose Intake

Capture what is being asked and why.

Output:

- current purpose
- target type
- expected decision layer

### 2. Scope And Boundary Lock

Define what is included, excluded, and forbidden.

Output:

- scope boundary
- authority boundary
- current status lock

### 3. Candidate Discovery

Find candidate targets or candidate structures within the bounded source zone.

Output:

- candidate list
- candidate source zone
- candidate selection reason

### 4. Candidate Comparison

Compare candidates by fit, role, and risk.

Output:

- selected candidate
- rejected candidates
- rejection reasons

### 5. Evidence Bundling

Bundle the evidence needed for the selected candidate.

Output:

- evidence bundle
- evidence strength
- thin / missing evidence notes

### 6. Validation Gate

Run process-level and target-level gates before action.

Output:

- gate results
- directly / weakly / not yet ratings
- authority drift warnings

### 7. Insufficiency / Supplement / Hold / Usable Decision

Decide whether the candidate is usable, needs supplement, should stay hold, or is insufficient.

Output:

- final candidate decision
- reason
- next safe action

### 8. Action Packet Formation

Create a compact execution packet if bounded work can proceed.

Output:

- execution packet
- worker-consumable context
- allowed and forbidden actions

### 9. Return Record / Redeposit

Receive and redeposit result into engine/space.

Output:

- return record
- redeposit payload
- next valid use
- what remains hold

## 6. Outputs

Possible outputs:

- candidate decision note
- evidence map
- validation gate result
- execution packet
- return record
- hold / supplement / insufficient note
- redeposit candidate

## 7. What Stays Bounded

Bounded:

- one target object or candidate zone at a time
- explicit lens set
- explicit evidence bundle
- explicit authority boundary
- no automatic promotion
- no rollout without separate validation

## 8. What It Does Not Do

This process camera does not:

- promote a camera
- validate all target types equally
- replace target-specific evidence
- create a global ontology
- create a multi-agent system
- authorize automatic reuse
- bypass supervisor judgment

## 9. Sample-Grounded Origin

This process camera is grounded in the completed camera review cycle where:

- original note was operational
- review guideline reread was `directly`
- rollback rule reread was `directly`
- three adjacent shadow-fits remained `weakly`
- final closeout preserved original-note-centered inspection tooling

## 10. Phase 2 Validation

Separation check:

- process camera is separate from original camera target

Inspectable gate check:

- stages have input/output roles
- gates remain bounded

Overclaim check:

- no fake universality is claimed

