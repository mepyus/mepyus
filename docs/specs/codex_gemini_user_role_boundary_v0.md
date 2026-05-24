# Codex / Gemini / User Role Boundary v0

## Status

```yaml
status: role_boundary_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: anchor_stack_setup_roles
```

## Purpose

Fix role boundaries for the current Anchor Stack setup so the operating frame does not drift.

## Codex Role

Codex owns setup and stabilization:

- read current position
- create and edit setup files
- synthesize route/PV/gate structure
- package Gemini outputs
- downshift authority/status language
- update Movement Records
- decide current operating position within user direction

Codex must not:

- delegate operating judgment to Gemini
- create baseline/automation/runner without explicit user approval
- treat worker output as memory without packaging

## Gemini Role

Gemini is a bounded exploration and crosscheck worker.

Gemini may:

- read large or token-heavy source bundles
- produce evidence-backed route/LACL/PV observations
- test plan-mode prompts
- identify missing evidence and route overlap

Gemini must not:

- be treated as authority
- write final operating frame
- promote baseline, registry, schema, or automation
- replace Codex Movement Record packaging

## User Role

The user owns:

- goal and priority
- manual relay when runner is unavailable
- decisions that change authority, baseline, implementation, or automation state

The user should not be normalized as:

- permanent dispatcher
- copy/paste relay
- tool-output interpreter

## Relay Rule

If the user relays Gemini output:

1. Codex packages it as worker return.
2. Codex records read scope and non-inspected scope.
3. Codex accepts useful findings only as interpreted candidate values.
4. Codex downshifts authority/status language.
5. Codex updates Movement Record if reusable judgment remains.

## Current Watch

- manual relay is active but temporary
- scripted Gemini runner reliability is unresolved
- Gemini repeatedly emits authority/status language

## Do Not

- Do not let Gemini set the big frame.
- Do not ask the user to repeatedly shuttle context when a packet can be prepared.
- Do not turn this role boundary into an automation contract.
