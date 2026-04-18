# Everything Claude Code MD Surface Map v0

## Purpose

This note reads `references/git_search/everything-claude-code-main` through its Markdown surfaces first.

The point is not to explain every file.
It is to make each folder's role and usage legible by following the repo's own documentation surfaces.

## Top-Level Read

The repo presents itself in [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/README.md) as a complete agent harness performance system, not just a config pack.

The most important top-level signals are:

- `README.md`: product framing, install story, supported surfaces
- `COMMANDS-QUICK-REF.md`: command catalog and user-facing entry map
- `WORKING-CONTEXT.md`: current operating status and active governance
- `RULES.md`, `AGENTS.md`, `CLAUDE.md`: canonical posture files
- `the-shortform-guide.md`, `the-longform-guide.md`, `the-security-guide.md`: human onboarding and philosophy layer

So the repo is not “docs beside code”.
The docs are the operating interface.

## Folder Roles

### `commands/`

Main read:
- [commands/verify.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/verify.md)
- [COMMANDS-QUICK-REF.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/COMMANDS-QUICK-REF.md)

Role:
- Slash-entry compatibility surface
- User-facing invocation names
- Short dispatch docs

Usage pattern:
- User invokes `/something`
- command file accepts arguments
- command delegates to a skill or workflow body

Important structural point:
- Commands are increasingly treated as legacy shims.
- The maintained logic is moving out of `commands/` and into `skills/`.

This is stated explicitly in [commands/verify.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/verify.md): the command is a legacy shim and the canonical workflow lives in the skill.

Practical reading:
- `commands/` tells you what the public entry names are.
- It does not tell you where the real maintained body lives.

### `skills/`

Main read:
- [skills/verification-loop/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/verification-loop/SKILL.md)
- [docs/SKILL-PLACEMENT-POLICY.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/SKILL-PLACEMENT-POLICY.md)

Role:
- Canonical workflow surface
- Task-specific maintained bodies
- Reusable operational knowledge

Usage pattern:
- A command may delegate into a skill
- A user or harness may invoke a skill directly
- Skills hold the real steps, checks, and workflow phases

Important structural point:
- Curated skills in `skills/` are ship-ready.
- Learned/imported/evolved skills are explicitly separated into home-directory roots and are not shipped.

This means `skills/` is both:
- the canonical maintained execution surface
- the curated boundary of what the repo considers productized knowledge

Practical reading:
- If you want the real workflow, read `skills/` before `commands/`.

### `agents/`

Main read:
- [agents/code-reviewer.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/agents/code-reviewer.md)

Role:
- Persona/task contracts
- Tool access declaration
- Behavioral specialization layer

Usage pattern:
- An orchestration surface or command selects an agent
- The agent defines model, tool access, review/process expectations, and output shape

Important structural point:
- Agents are not generic descriptions.
- They are operational role contracts with constraints.

In [agents/code-reviewer.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/agents/code-reviewer.md), the file declares:
- purpose
- required use conditions
- tools
- model
- review process
- confidence filter
- approval/block criteria

Practical reading:
- `agents/` shows how the repo decomposes labor into specialized roles.
- It is closer to an execution-role catalog than to reusable procedure text.

### `contexts/`

Main read:
- [contexts/review.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/contexts/review.md)

Role:
- Lightweight mode presets
- Focus and output-shaping hints

Usage pattern:
- A task enters a mode such as review/research/dev
- Context file supplies focus, checklist, and output bias

Important structural point:
- Contexts are much thinner than agents or skills.
- They do not fully own a workflow.
- They tune the reading/response mode.

Practical reading:
- `contexts/` tells you how the repo marks “what kind of work is happening right now”.

### `hooks/`

Main read:
- [hooks/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/hooks/README.md)
- `hooks/hooks.json`

Role:
- Event-driven automation layer
- Guardrails and lifecycle reactions

Usage pattern:
- Tool event or lifecycle event occurs
- Hook runs before/after or at stop/session boundaries
- Hook warns, blocks, persists, or audits

Important structural point:
- `hooks/README.md` reads like an operator manual.
- It explains event semantics, exit codes, lifecycle timing, and customization.
- This folder is not “extra scripts”.
- It is the reactive operating layer around sessions.

Practical reading:
- `hooks/` is where immediate guard, persistence, audit, and reminder behavior lives.
- It complements, but does not replace, skills.

### `rules/`

Main read:
- [rules/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/rules/README.md)

Role:
- Broad standards and checklists
- Layered defaults + language/domain overrides

Usage pattern:
- `common/` provides universal rules
- language/domain folders extend and override

Important structural point:
- Rules are not deep workflows.
- They define standards, conventions, and broad checklists.
- The repo explicitly says: rules tell you what to do, skills tell you how to do it.

Practical reading:
- Read `rules/` when you need standards and override structure.
- Read `skills/` when you need an actual operating procedure.

### `plugins/`

Main read:
- [plugins/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/plugins/README.md)

Role:
- External ecosystem bridge
- Installation guide for third-party plugin surfaces

Usage pattern:
- add marketplace
- browse or install plugin
- extend Claude Code with external capabilities

Important structural point:
- `plugins/` is not the repo's own core skill/agent layer.
- It is the outward-facing extension bridge.

Practical reading:
- `plugins/` tells you what outside surfaces this system expects to coexist with.

### `docs/`

Main read:
- [docs/ECC-2.0-REFERENCE-ARCHITECTURE.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/ECC-2.0-REFERENCE-ARCHITECTURE.md)
- [docs/SKILL-PLACEMENT-POLICY.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/SKILL-PLACEMENT-POLICY.md)

Role:
- Architecture explanation
- policy/governance
- design records and migration contracts

Usage pattern:
- use `docs/` to understand why the repo is shaped the way it is
- use it to distinguish curated surfaces from generated/local ones

Important structural point:
- `docs/` is where the repo explains its own internal reorganization, policy boundaries, and future architecture.
- It is not just user help; it is also self-description.

Practical reading:
- If `commands/` and `skills/` tell you how to use the system, `docs/` tells you how the system thinks about itself.

### Harness-Specific Hidden Surfaces

Visible top-level folders and files:
- `.claude/`
- `.codex/`
- `.opencode/`
- `.kiro/`
- `.cursor/`

Role:
- harness-specific packaging and compatibility surfaces

Practical reading:
- These folders mean the repo is not bound to one host.
- The same conceptual system is re-emitted into several harness ecosystems.

## How To Read This Repo Quickly

If the goal is “what is this folder for?”, this order works well:

1. `README.md`
2. `WORKING-CONTEXT.md`
3. one representative file from `commands/`
4. the corresponding `skills/.../SKILL.md`
5. `hooks/README.md`
6. `rules/README.md`
7. one representative file from `agents/`
8. one representative file from `contexts/`
9. `docs/` policy/architecture docs

This gives the role split without dropping into scripts too early.

## Simple Translation Of Folder Meaning

- `commands/`: public entry names
- `skills/`: real workflow bodies
- `agents/`: specialized worker roles
- `contexts/`: mode presets
- `hooks/`: reactive automation layer
- `rules/`: standards and defaults
- `plugins/`: outside extension bridge
- `docs/`: architecture and policy memory

## Why This Repo Is Useful As A Reference

The repo makes a crucial distinction very visible in Markdown:

- entry surface is not the same as maintained body
- standards are not the same as workflows
- role contracts are not the same as contexts
- hooks are not the same as skills
- curated shipped knowledge is not the same as learned local knowledge

That separation is one of the main reasons the repo is structurally valuable.
