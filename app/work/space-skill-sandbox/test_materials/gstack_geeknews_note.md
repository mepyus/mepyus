# GStack GeekNews Note

## Source

```text
title: Garry Tan / GStack external material
source: GeekNews summary and user-pasted Korean summary
url: https://news.hada.io/topic?id=27756
github: https://github.com/garrytan/gstack
date_seen: 2026-04-28
status: external reference note
baseline: false
automation: false
tool_installation: false
```

## Original Meaning

The original material presents GStack as Garry Tan's open-source AI coding workflow for turning Claude Code and related agents into a virtual software team. The frame is not "one prompt generates code." The frame is a skill pack that simulates roles and stages across a sprint.

The main original reading:

- GStack follows a "thin shell, thick skills" philosophy: structured markdown prompts and slash commands do much of the orchestration without a heavy custom runtime.
- It covers a full sprint-like lifecycle: think, plan, build, review, test, ship, and reflect.
- It uses role-oriented skills such as CEO/product thinking, design review, engineering review, QA, security, and release.
- Office Hours-style prompts push product judgment by asking evidence-seeking questions about whether users really want the idea.
- Adversarial review attempts to find missing failure handling, privacy gaps, handoff issues, and design weaknesses.
- Cross-model review, Playwright browser QA, worktree-based parallel sessions, and team setup are presented as practical scaling tools.
- The material claims strong public interest and large productivity gains, but those claims should be treated as external claims rather than local evidence.

## Read Through Our Space

In this space, GStack is less important as a tool to install and more important as a pressure test for our sandbox boundaries.

Space reading:

- "Thin shell, thick skills" maps well to the current Space Skill Sandbox direction: small markdown skills before heavy runtime.
- The sprint lifecycle shows a possible worker-guide routing map, but it is too broad to import directly.
- Office Hours maps to product-intent pressure: before implementation, ask what evidence shows real demand.
- Adversarial review maps to validation rounds and failure-to-guide candidates.
- Playwright QA maps to verification pressure, but also crosses into automation/tool execution.
- Worktree-based parallel agent sessions map to fleet/process governance, not just coding speed.
- Team setup and auto-update map to install/config boundaries that require user judgment.

The strongest local signal is that AI coding gets more useful when the process is visible. But visibility is not the same as adoption. A visible external workflow can be lowered into candidates without becoming the local operating model.

## Different Reading For This Sandbox

The useful inversion is:

```text
Do not import the virtual software team.
Extract the smallest visible decision surface that reduces user burden without increasing hidden authority.
```

For this sandbox, GStack becomes a set of questions:

- Which part is only a prompt pattern?
- Which part changes tools, config, browser automation, or team behavior?
- Which role labels help the user think, and which ones overstate AI authority?
- Which reviews can stay as read-only validation cases?
- Which failures should become guide candidates rather than commands?
- Which outputs need a structured footer before the next step?

So the article supports a sandbox practice: borrow structure, not control. Use GStack to test whether this space can lower a big external workflow into small candidate skills, review cases, and closeout cards.

## Space Skill Sandbox Relevance

- `external-material-intake` should read GStack as comparison / borrow-later / caution, not as a setup instruction.
- `preflight-guard` should catch `/qa`, `/codex`, team setup, browser automation, install, config, and auto-update boundaries.
- `structured-footer` should compress each run into status, summary, risk, and next so the user can see where the sprint-like chain stops.
- `failure-to-guide` can extract small guide candidates from recurring GStack-style risks, such as "role label over-promotes authority" or "review output becomes implementation pressure."
- `worker_guide` can borrow routing clarity, but should avoid becoming a slash-command controller.

## Caution

This material describes an opinionated AI coding workflow with commands, browser QA, cross-agent review, team setup, and parallel sessions. In this sandbox, it should remain comparison material. It should not trigger GStack installation, Claude Code config changes, slash-command adoption, Playwright automation, worktree orchestration, auto-update behavior, or source-space changes.

## Footer

```text
status: 완료
summary: GStack 자료를 원본 의미와 Space Skill Sandbox식 읽기로 나누어 저장함
risk: 가상 소프트웨어 팀 구조를 그대로 받아들이면 command/controller, install/config, automation, role-authority drift가 생길 수 있음
next: 필요할 때 external-material-intake, preflight-guard, worker-guide routing 관련 sandbox run의 비교 재료로만 사용
```
