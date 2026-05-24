# Gemini Space-Aware External Loop Test 001 - Anchor Request

## Status

```yaml
status: live_test_packet_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
packet_role: external_tool_interpretation_anchor_request
```

## External Tool Role

You are acting as an autonomous external execution carrier for one bounded VectorFL operating test.

Do not execute the full task yet.
Do not draft the final plan yet.
Do not claim authority, readiness, baseline, registry, schema, or automation.

## Current User Purpose

```text
Hermes / OmX / OpenClaw 같은 외부 실행 도구를 VectorFL 공간과 연결해서,
실제 작업 하나를 공간 참조 기반으로 실행하고,
그 결과를 다시 Movement Record로 회수하는 최소 운용 흐름을 설계해봐.
```

## Test Question

Before planning, decide whether this task needs VectorFL Space anchors.

The test is not whether you produce a good answer.
The test is whether you recognize that the execution must start from space memory and return recoverable material.

## Required Output Shape

Return only the following sections:

```text
EXTERNAL_TOOL_INTERPRETATION
ANCHOR_REQUEST
STOP_BEFORE_EXECUTION
```

## EXTERNAL_TOOL_INTERPRETATION must include

- how you understand the user purpose
- whether this is a design expansion or an actual operating-loop entry
- what you must not do before receiving anchors

## ANCHOR_REQUEST must include

- needed material families
- needed route / PV / LACL signals if known
- what active surfaces you expect Codex to provide
- what evidence / return shape you need
- what would be unsafe to infer without anchors

If you think no anchors are needed, state `NO_ANCHOR_NEEDED` and explain why.

## STOP_BEFORE_EXECUTION must include

- confirmation that you are stopping before the execution plan
- what you expect Codex to provide next as an Anchor Packet

## Boundary

Your result is raw trace / candidate material only.
Codex will review and downshift it before any Return-to-Space recovery.
