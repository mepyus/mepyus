# External Material Synthesis Round 001

## Scope

```text
mode: sandbox synthesis
source_space_modified: false
baseline: false
automation: false
tool_installation: false
```

This synthesis rereads the recent external materials as pressure on the current goal: make the space usable by Gemini/Codex without hiding the user's decision surface.

Materials:

- `test_materials/martin_fowler_fragments_2026_04_02_note.md`
- `test_materials/skillify_geeknews_note.md`
- `test_materials/gstack_geeknews_note.md`
- `test_materials/google_cloud_agent_governance_stack_note.md`
- `test_materials/agentic_patterns_harness_evolution_note.md`

## 1. What These Materials Are Really Pressuring

The common pressure is not "add more agent machinery."

The common pressure is:

```text
As AI workers become more capable, the user needs a smaller and clearer surface for:
identity, context, permission, validation, routing, risk, and next action.
```

Fowler says the scarce work moves to understanding, intent, and verification. Skillify says failures should become durable structures, not repeated reminders. GStack says a coding agent becomes useful when the workflow has visible roles and review stages. Google Cloud says agent fleets need identity, access control, monitoring, and audit. The harness evolution article says rigor moves from prompt wording to context and then to the surrounding system.

Read together, they do not say "install a harness." They say the current space needs a user-legible operating surface before any harness can be trusted.

## 2. Original Pressure By Material

### Fowler fragment

Original pressure:

- code generation is getting cheaper
- verification and intent capture become more important
- cognitive surrender is a real risk

Space pressure:

- Gemini/Codex output must not end as confident prose
- every output needs visible status, risk, next, and evidence boundary
- "summary" must not become "truth"

### Skillify

Original pressure:

- repeated failures should become skills, scripts, tests, routing checks, and audits
- latent judgment and deterministic execution should be separated
- dark/unreachable skills are a real failure mode

Space pressure:

- a failure should first become a guide candidate, not a hook
- deterministic scripts require user judgment before creation
- routing should be tested as cases before automatic routing exists

### GStack

Original pressure:

- AI coding can be wrapped in a sprint-like team simulation
- roles, adversarial reviews, cross-model checks, browser QA, and worktrees can increase throughput
- "thin shell, thick skills" can be enough to coordinate work

Space pressure:

- borrow the visible workflow shape, not the command suite
- role labels must not over-promote AI authority
- browser QA, cross-model review, team setup, and auto-update are preflight boundaries

### Google Cloud Agent Governance Stack

Original pressure:

- production agent fleets need identity, registry, policy enforcement, anomaly detection, and security posture
- misconfigured agents act actively, not just passively leak data

Space pressure:

- even sandbox workers need a lightweight answer to "who did what under what boundary?"
- tool/skill availability must be visible before use
- user needs a posture card before production governance tools

### Agentic patterns / harness evolution

Original pressure:

- rigor moved from prompts to context to harnesses
- each shift happened because the previous layer failed
- harness engineering includes tools, loops, cost, security, and feedback

Space pressure:

- do not jump from "we need rigor" to "build a harness"
- first show where rigor currently lives: skill text, selected context, validation, closeout
- context overload is a danger; reading the whole Deep Space can erase the current boundary

## 3. The Deeper Common Pattern

The external materials share one transition:

```text
AI worker value increases when the process around the worker becomes explicit.
AI worker risk increases when that process becomes invisible automation.
```

For this space, that means the next useful layer is not a controller. It is a compact operating surface that lets the user see:

- which worker/agent acted
- what material it read
- what boundary it was under
- what it changed or did not change
- what claim still needs validation
- what action would cross into user judgment
- what the next sandbox move is

This is the missing middle between "external notes" and "source-space promotion."

## 4. What This Means For Gemini/Codex Actual Use

If Gemini/Codex are now helping operate the space, each run needs a small receipt-like surface.

Minimum useful run receipt:

```text
worker:
task:
mode:
source_refs:
allowed_actions:
forbidden_actions:
created_or_modified:
validation_status:
risk:
next:
```

This is not a schema proposal for the source space. It is a sandbox candidate surface for making real use observable.

Why it matters:

- Fowler: prevents cognitive surrender and intent debt
- Skillify: gives failures a place to become guide candidates
- GStack: makes workflow stages visible without importing commands
- Google Cloud: gives lightweight identity, registry, and posture before governance tools
- Harness evolution: shows where rigor lives before harness implementation

## 5. Candidate Skills Or Lenses Suggested By The Synthesis

### run-receipt-lens

Purpose:

```text
Lower any Gemini/Codex sandbox run into a small receipt showing worker, task, source refs, allowed/forbidden actions, output, risk, and next.
```

Why now:

- actual use needs traceability
- current structured footer is useful but too compressed for multi-worker or external-material runs

Boundary:

- no automation
- no log aggregation
- no dashboard
- no source-space schema

### governance-posture-card

Purpose:

```text
Show whether current sandbox activity has identity, tool/skill visibility, policy boundary, anomaly note, and posture summary.
```

Why now:

- Google Cloud material points to governance layers
- the sandbox needs the user-visible version, not cloud governance infrastructure

Boundary:

- no Google Cloud setup
- no MCP registry
- no policy gateway
- no monitoring service

### verification-surface

Purpose:

```text
Separate generated output, evidence, validation needed, user judgment needed, and forbidden next actions.
```

Why now:

- Fowler and harness evolution both say verification becomes central
- current closeout cards do this, but not yet as a reusable lens

Boundary:

- no test framework adoption
- no daily evals
- no automatic scoring

### failure-to-guide-plus

Purpose:

```text
Convert a concrete failure into a guide candidate, plus a check case, before any deterministic script or route is created.
```

Why now:

- Skillify pressure is useful, but "make it permanent" is too strong for this space

Boundary:

- no script creation unless separately approved
- no automatic routing
- no baseline

## 6. Dangerous Misreads

Do not read Fowler as:

```text
AI output is okay if it sounds thoughtful.
```

Read it as:

```text
the user needs verification and intent surfaces.
```

Do not read Skillify as:

```text
every failure should immediately become a permanent skill with tests and automation.
```

Read it as:

```text
recurring failure should first become a visible guide candidate and check case.
```

Do not read GStack as:

```text
install the virtual software team.
```

Read it as:

```text
visible workflow stages reduce ambiguity, but commands and setup are separate user-judgment boundaries.
```

Do not read Google Cloud governance as:

```text
install governance products.
```

Read it as:

```text
the user needs lightweight answers to identity, permission, tool visibility, anomaly, and posture questions.
```

Do not read harness evolution as:

```text
build a harness now.
```

Read it as:

```text
make the current location of rigor visible before constructing machinery.
```

## 7. Recommended Next Sandbox Run

Recommended:

```text
Run 014: run-receipt-lens sandbox check
```

Goal:

```text
Test whether a Gemini/Codex run can be lowered into a receipt that shows identity, task, source refs, allowed/forbidden actions, output, validation, risk, and next.
```

Why this is the right next step:

- It directly addresses the user's concern that the space must become actually usable.
- It is smaller than automation, harness, governance stack, or tool installation.
- It lets future external materials and worker runs become traceable.
- It extends structured-footer without replacing it.

Do not execute yet:

- no new skill creation unless requested
- no source-space promotion
- no automation
- no MCP/hook/watch mode
- no tool installation
- no controller/router

## 8. 4-Line Footer

```text
status: 완료
summary: 최근 외부 자료 5개를 실제 Gemini/Codex 공간 사용 단계에 필요한 run receipt, governance posture, verification surface 후보로 두껍게 재해석함
risk: 외부 자료의 harness/governance/skillify 압력을 곧바로 자동화나 설치로 읽으면 사용자 판단면이 사라질 수 있음
next: 사용자 검토 후 Run 014 run-receipt-lens sandbox check 여부 선택
```
