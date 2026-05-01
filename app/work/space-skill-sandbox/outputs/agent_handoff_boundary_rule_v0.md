# Agent Handoff Boundary Rule v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- relay_v1: false
- automation: false
- agent_implementation: false

## 1. Purpose

이 문서는 Codex / Gemini / Runner / User 사이의 수동 전달 경계를 정의한다.

핵심 문장:

Codex creates the packet.
Gemini executes the packet.
Runner transports the packet to Gemini.
User approves, triggers, and judges the flow.

## 2. Role Separation

### Codex

Codex may:

- read current sandbox state
- inspect outputs / runs / review
- create next Gemini task packet
- create validation records
- prepare next step after validation

Codex must not:

- promote to source-space
- create baseline
- declare Relay v1.0
- create automation
- create hook / MCP / watch mode
- merge existing program
- run Gemini automatically without user trigger

### Gemini

Gemini may:

- execute a packet created by Codex or supervisor
- create requested sandbox output files
- create run record
- create validation record
- report closeout

Gemini must not:

- create its own task packet and execute it
- create the next packet for itself
- modify source-space
- create baseline
- declare Relay v1.0
- modify worker guide
- create automation
- create hook / MCP / watch mode
- promote candidate documents

### Runner

Runner may:

- read a packet file
- call Gemini manually when user runs the command
- save raw output
- save outbox output
- record timestamp and run id

Runner must not:

- watch folders
- auto-trigger on file changes
- apply Gemini output automatically
- modify source-space
- create next packet
- validate results
- promote results

### User

User may:

- approve execution
- run the manual command
- decide whether to continue
- provide Gemini result to Codex / reviewer
- make final judgment

User is the final judge.

## 3. Correct Handoff Flow

Correct flow:

Codex creates packet
→ User manually triggers runner
→ Runner invokes Gemini
→ Gemini executes packet
→ Runner saves outbox/raw result
→ Codex validates result
→ Codex creates next packet only after validation

## 4. Forbidden Flow

Forbidden flow:

Gemini creates packet
→ Gemini executes its own packet
→ Gemini validates itself
→ Gemini creates next packet

This is not allowed because packet creator and packet executor collapse into one role.

## 5. Temporary Supervisor Exception

If Codex is unavailable due to token limits,
ChatGPT/supervisor may draft a packet for later Codex storage.

But:

- Gemini must not self-author its own packet.
- The packet must be stored as a file before execution.
- The packet must clearly record its creator.
- Execution must be user-triggered.
- Validation must be separate from execution.

## 6. Non-Automation Note

This document defines a manual handoff boundary only.
It does not create automation.
It does not declare Relay v1.0.
It does not create agent implementation.
It does not promote any sandbox document.
