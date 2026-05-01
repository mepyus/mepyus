# Skillify GeekNews Note

## Source

```text
title: Garry Tan의 "Skillify" - AI 에이전트의 실패를 영구적 구조 수정으로 바꾸는 방법론
source: GeekNews
date_seen: 2026-04-28
url: https://news.hada.io/topic?id=28777
status: external reference note
baseline: false
automation: false
tool_installation: false
```

## Original Meaning

The original post presents Skillify as an opinionated agent quality workflow. Its claim is that important agent failures should not be handled by reminders alone. They should be converted into a durable structure: skill instructions, deterministic scripts, tests, resolver triggers, routing checks, audits, smoke tests, and filing rules.

The main original reading:

- Agent failures should become reusable skills when the same mistake must not recur.
- Work should be split between latent judgment and deterministic execution.
- If a script can answer exactly, the agent should not reason loosely in latent space.
- A skill without tests and routing checks can decay or become unreachable.
- Discoverability matters because many skills can exist but fail to trigger.
- The workflow is intentionally stronger than "write a helpful instruction file."

## Read Through Our Space

In this space, the post is useful but dangerous if copied directly. The valuable part is not "make everything permanent." The valuable part is the failure-to-structure loop.

Space reading:

- A failure can become a guide candidate, but not automatically a baseline.
- Deterministic work should be separated from judgment work, but script creation is still an implementation boundary.
- Skill routing is useful only while it remains visible, reviewable, and small enough for the user to understand.
- Tests and resolver checks are verification material, not permission to install tools or create automation.
- "Make it permanent" should be translated into "prepare a candidate and ask where the boundary is."

## Different Reading For This Sandbox

The useful inversion is:

```text
Do not skillify every failure into machinery.
First lower the failure into a visible guide candidate and decide whether machinery is justified.
```

So this article supports a sandbox practice:

- Repeated failure should be captured as a small failure-to-guide candidate.
- The first output should be a human-readable rule, not a hook, daemon, resolver, or install.
- Deterministic scripts are allowed only after the user accepts that the task is deterministic and worth mechanizing.
- Routing checks should be represented as reviewable cases before they become automatic routing.
- Discoverability can be tested with run notes before introducing controller behavior.

## Space Skill Sandbox Relevance

- `failure-to-guide` can use this as supporting material: failure should be lowered into a guide candidate only when the boundary is clear.
- `preflight-guard` remains important because "make it permanent" can cross into baseline, automation, tool setup, or routing changes.
- `structured-footer` should keep the status visible: a useful skill candidate is still not adoption.
- `worker_guide` routing should avoid dark skills by keeping trigger rules visible and reviewable.

## Caution

The GeekNews post describes an opinionated method around skills, scripts, tests, and resolver checks. In this sandbox, that should be treated as comparison material only. It should not create automatic skill routing, tool installation, daily evals, hooks, or source-space changes by itself.

## Footer

```text
status: 완료
summary: Skillify GeekNews 글을 원본 의미와 Space Skill Sandbox식 읽기로 나누어 저장함
risk: 실패를 바로 영구 구조나 자동 라우팅으로 바꾸면 baseline/automation drift가 생길 수 있음
next: 필요할 때 failure-to-guide 또는 verification 관련 sandbox run의 비교 재료로만 사용
```
