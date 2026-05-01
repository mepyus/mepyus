# Agentic Patterns Harness Evolution Note

## Source

```text
title: 프롬프트에서 하네스까지 - AI 에이전틱 패턴 4년의 기록
source: bits-bytes-nn
published: 2026-04-05
url: https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html
status: external reference note
baseline: false
automation: false
tool_installation: false
```

## Original Meaning

The original article is a historical reading of AI agentic patterns from 2022 to 2026. Its central claim is that engineering rigor did not disappear when AI coding became common. Rigor moved.

The article's timeline:

- Prompt Engineering, 2022-2024: the main question was "what should we say to the model?"
- Context Engineering, 2025: the main question became "what information should the model see?"
- Harness Engineering, 2026: the main question became "what system should surround the agent?"

The article frames each shift as a failure response. Prompting failed when the right information was missing. Context engineering failed when large context introduced contamination, lost-in-the-middle issues, and expensive state management. Harness engineering appears when teams accept that the agent loop, tools, feedback, verification, cost, and security are part of the real system.

The article also makes an important containment point: prompt engineering is not dead. It becomes a submodule inside context engineering, which becomes a submodule inside harness engineering. A good harness still needs good context, and good context still needs good prompts.

## Read Through Our Space

In this space, the article should not be read as "build a harness now." It should be read as a map of where hidden complexity moves when agents become more capable.

Space reading:

- Prompt quality maps to skill wording and worker guide wording.
- Context quality maps to which source refs, run notes, validations, and closeout cards are visible to the worker.
- Harness quality maps to task boundaries, permission boundaries, validation loops, and user-visible state.
- Blind prompting maps to asking workers to improve the space without evidence, source refs, or validation criteria.
- Context contamination maps to reading too much Deep Space and losing the current package boundary.
- Harness complexity maps to automation, routers, hooks, MCPs, controllers, and dashboards that may exceed user visibility.

The strongest local signal is that rigor must stay near the user's decision surface. If rigor moves into an invisible harness, the space may become more powerful but less governable.

## Different Reading For This Sandbox

The useful inversion is:

```text
Do not jump from prompt/context problems to harness construction.
First make the movement of rigor visible in small sandbox artifacts.
```

For this sandbox, the three eras become artifact questions:

- Prompt: does the candidate skill say exactly when to use it and what not to do?
- Context: does the run cite only the small internal references it needs?
- Harness: does the closeout show status, risk, next, and forbidden transitions before any automation exists?

So the article supports a sandbox practice: before building a harness, create small artifacts that reveal where rigor currently lives.

## Space Skill Sandbox Relevance

- `external-material-intake` addresses the context layer by limiting external material to comparison / borrow-later / caution.
- `preflight-guard` addresses the harness boundary before a real harness exists: delete, install, automation, baseline, and source-space changes require user judgment.
- `structured-footer` keeps rigor visible at the output surface.
- `worker_guide` is a small routing surface, not a full orchestration system.
- `failure-to-guide` can convert failures into guide candidates without immediately creating scripts, hooks, or controllers.

## Caution

This article names harness engineering as the current direction, but in this sandbox that should remain comparison material. It should not trigger harness implementation, controller creation, automatic routing, MCP/watch mode, dashboarding, whole-space indexing, or production workflow changes.

## Footer

```text
status: 완료
summary: Agentic patterns evolution 글을 원본 의미와 Space Skill Sandbox식 읽기로 나누어 저장함
risk: harness engineering을 바로 구현 대상으로 읽으면 automation/controller/router drift가 생길 수 있음
next: 필요할 때 worker guide, preflight guard, structured footer, governance posture 관련 sandbox run의 비교 재료로만 사용
```
