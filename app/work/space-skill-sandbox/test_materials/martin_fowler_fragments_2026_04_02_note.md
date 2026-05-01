# Martin Fowler Fragment 2026-04-02 Note

## Source

```text
title: Fragments: April 2
author: Martin Fowler
date: 2026-04-02
url: https://martinfowler.com/fragments/2026-04-02.html
status: external reference note
baseline: false
automation: false
tool_installation: false
```

## Original Meaning

Fowler is collecting several signals about LLM-assisted software work. The original article is not a single method proposal. It is a fragment bundle around system health, AI-assisted cognition, verification, and the continuing role of source code as a human-readable language.

The main original reading:

- Technical debt is about code changeability.
- Cognitive debt is about people losing shared understanding.
- Intent debt is about goals and constraints not being captured in artifacts.
- AI can be used as cognitive offloading when humans still deliberate, but it becomes cognitive surrender when humans stop evaluating.
- If agents make code generation cheap, verification becomes the scarce and expensive work.
- The future of code still depends on useful abstractions, names, and shared language.

## Read Through Our Space

In this space, the article is less about "AI coding will change engineering" and more about where the user's sovereignty should sit.

Space reading:

- Cognitive debt maps to worker output that is too long, too confident, or too hard for the user to judge.
- Intent debt maps to candidate artifacts that do not say what they are, what they are not, and what boundary they must not cross.
- Verification becoming expensive maps directly to closeout cards, validation rounds, structured footers, and evidence-bearing run notes.
- "Cognitive surrender" is the failure mode where the user accepts an agent's summary because it sounds complete.
- Ubiquitous language maps to this space's need for small stable terms: candidate, validation, user judgment, source-space, automation boundary.

## Different Reading For This Sandbox

The useful inversion is:

```text
Do not ask first: "Can the agent generate more?"
Ask first: "Can the human still see what changed, why it matters, and what is not allowed next?"
```

So this article supports a sandbox practice:

- Every generated artifact should carry its current status.
- A summary is not evidence.
- A PASS or OK is not a lock.
- If verification is the expensive part, the interface should make verification smaller.
- The closer something gets to source-space, automation, install, baseline, or routing, the more explicit user judgment becomes.

## Space Skill Sandbox Relevance

- `external-material-intake` prevents an external article from becoming internal authority too quickly.
- `preflight-guard` protects the point where intent debt could become real behavior change.
- `structured-footer` reduces cognitive surrender by making risk and next action visible.
- Closeout cards reduce intent debt by recording what was validated and what remains only a candidate.

## Boundary

This note is not adoption, promotion, baseline, automation, or tool installation. It is a lightweight external material note for later comparison.

## Footer

```text
status: 완료
summary: Martin Fowler의 2026-04-02 fragment를 원본 의미와 Space Skill Sandbox식 읽기로 나누어 저장함
risk: verification/intent debt 관점을 내부 기준처럼 바로 고정하면 external authority drift가 생길 수 있음
next: 필요할 때 external-material-intake나 verification 관련 sandbox run의 비교 재료로만 사용
```
