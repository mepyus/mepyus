# Everything Claude Code MD Deep Reading v1

## Scope

This note goes one step deeper than the surface map.

It is based on actually reading representative Markdown files inside:

- `commands/`
- `skills/`
- `agents/`
- `contexts/`
- `docs/`

The goal is to understand the internal texture of each folder, not just its label.

## Files Read

### Root and policy

- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/README.md)
- [COMMANDS-QUICK-REF.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/COMMANDS-QUICK-REF.md)
- [WORKING-CONTEXT.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/WORKING-CONTEXT.md)
- [docs/SKILL-PLACEMENT-POLICY.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/SKILL-PLACEMENT-POLICY.md)

### Commands

- [commands/plan.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/plan.md)
- [commands/verify.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/verify.md)
- [commands/loop-start.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/loop-start.md)
- [commands/harness-audit.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/harness-audit.md)
- [commands/learn.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/learn.md)
- [commands/orchestrate.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/commands/orchestrate.md)

### Skills

- [skills/verification-loop/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/verification-loop/SKILL.md)
- [skills/continuous-agent-loop/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/continuous-agent-loop/SKILL.md)
- [skills/strategic-compact/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/strategic-compact/SKILL.md)
- [skills/workspace-surface-audit/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/workspace-surface-audit/SKILL.md)
- [skills/continuous-learning-v2/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/continuous-learning-v2/SKILL.md)
- [skills/project-flow-ops/SKILL.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/skills/project-flow-ops/SKILL.md)

### Agents and contexts

- [agents/code-reviewer.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/agents/code-reviewer.md)
- [agents/planner.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/agents/planner.md)
- [agents/loop-operator.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/agents/loop-operator.md)
- [contexts/dev.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/contexts/dev.md)
- [contexts/research.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/contexts/research.md)
- [contexts/review.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/contexts/review.md)

### Docs

- [docs/ECC-2.0-REFERENCE-ARCHITECTURE.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/ECC-2.0-REFERENCE-ARCHITECTURE.md)
- [docs/COMMAND-AGENT-MAP.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/COMMAND-AGENT-MAP.md)
- [docs/SESSION-ADAPTER-CONTRACT.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/docs/SESSION-ADAPTER-CONTRACT.md)

## Commands: Internal Texture

`commands/` is not one uniform folder.
It contains at least three distinct subtypes.

### 1. Entry-contract commands

Examples:
- `plan.md`
- `loop-start.md`
- `harness-audit.md`
- `learn.md`

These still define meaningful behavior at the command layer.

Typical traits:
- clear invocation syntax
- explicit steps
- safety or output contracts
- deterministic or bounded execution expectations

Examples:
- `plan.md` is a user-facing contract for planning before code.
- `loop-start.md` is a managed-loop entry contract with pattern and mode selection.
- `harness-audit.md` explicitly binds the command to one deterministic script and says not to invent new scoring dimensions.
- `learn.md` is still command-shaped and file-output-oriented.

### 2. Legacy shims

Examples:
- `verify.md`
- `orchestrate.md`

These do not want to own workflow logic anymore.
They exist as compatibility doors.

Typical traits:
- explicit statement that the maintained body lives in `skills/`
- delegation language instead of procedure body
- reduced local logic

This is a major structural signal:
the repo is actively migrating from command-owned workflow to skill-owned workflow.

### 3. Catalog/entry layer

Seen through:
- `COMMANDS-QUICK-REF.md`
- `docs/COMMAND-AGENT-MAP.md`

This gives the public surface map:
which commands exist, what they roughly do, and whether they call agents or skills.

### Command folder conclusion

`commands/` is not the source of truth for workflows.
It is a mixed entry layer:
- some still carry real contract logic
- some are compatibility shims
- some exist mainly for discoverability

## Skills: Internal Texture

`skills/` also has internal subtypes.
It is not just “procedures”.

### 1. Workflow skills

Examples:
- `verification-loop`
- `project-flow-ops`

Traits:
- ordered phases
- explicit output shape
- operational use cases
- strong task orientation

These read like maintained runbooks.

### 2. Operator-pattern skills

Examples:
- `strategic-compact`
- `workspace-surface-audit`

Traits:
- centered on one operational concern
- combines heuristics, timing, and decision guidance
- often complements hooks or scripts

These are not full pipelines, but they are more than a checklist.

### 3. Loop/governance skills

Examples:
- `continuous-agent-loop`

Traits:
- pattern selection
- failure mode framing
- recovery guidance
- relation to quality gates/evals/persistence

These read as control guidance for long-running execution.

### 4. Subsystem-spec skills

Examples:
- `continuous-learning-v2`

Traits:
- architecture explanation
- storage model
- hook wiring
- file structure
- command inventory

This kind of skill is almost a mini product spec embedded as a skill.

### Skill folder conclusion

`skills/` is the canonical maintained body, but inside it there are multiple densities:
- runbook workflows
- operator patterns
- loop governance
- subsystem documentation

This means “skill” in ECC is broader than “task recipe”.

## Agents: Internal Texture

Representative reads:
- `code-reviewer.md`
- `planner.md`
- `loop-operator.md`

These files are clearly role contracts, but their internal density differs.

### Heavy procedural agents

Examples:
- `code-reviewer`
- `planner`

Traits:
- detailed process
- output format
- quality filters
- red flags / approval criteria
- examples

These are closer to executable role manuals.

### Thin operator agents

Example:
- `loop-operator`

Traits:
- concise mission
- checkpoint logic
- escalation conditions

This is a more compact supervisory role.

### Agent folder conclusion

`agents/` is not just personas.
It is a role-contract layer where some roles are fully proceduralized and others are minimal supervisory shells.

## Contexts: Internal Texture

Representative reads:
- `dev.md`
- `research.md`
- `review.md`

These are consistently thin.

Traits:
- mode
- focus
- behavior bullets
- preferred tools
- lightweight output bias

Contexts do not own workflows.
They shape stance.

This is important because it distinguishes them from agents:
- agent = role contract
- context = mode preset

## Docs: Internal Texture

The docs sampled here reveal that `docs/` carries at least three functions.

### 1. Architecture explanation

Example:
- `ECC-2.0-REFERENCE-ARCHITECTURE.md`

This is outward-facing architectural framing.
It explains intended layers and reference inspirations.

### 2. Cross-surface map

Example:
- `COMMAND-AGENT-MAP.md`

This is a routing document.
It ties commands to agents and skills and helps keep refactors consistent.

### 3. Normative contract

Example:
- `SESSION-ADAPTER-CONTRACT.md`

This is not casual documentation.
It is a normative spec that defines canonical shape, versioning rules, adapter obligations, and consumer expectations.

### Docs folder conclusion

`docs/` is not just explanation.
It contains:
- concept docs
- routing/index docs
- real normative contracts

## Cross-Folder Reading

The strongest pattern visible across the Markdown layer is this:

### Entry surface vs maintained body

- `commands/` often provides the invocation name
- `skills/` increasingly provides the maintained body

### Role vs mode

- `agents/` define who does the work and with what rigor
- `contexts/` define in what mode the work is framed

### Reactive layer vs workflow layer

- `hooks/` react to events and guard behavior
- `skills/` define longer procedural bodies

### Standards vs procedures

- `rules/` define what should hold
- `skills/` define how to actually do the work

### Explanation vs contract

- some `docs/` files explain architecture
- some `docs/` files are effectively specifications

## What Became Clear Only After Reading Inside

1. `commands/` is more transitional than it first appears.
   A meaningful portion of the folder is already being hollowed into shims.

2. `skills/` is broader than “task recipes”.
   Some skills are really operator subsystems or mini design specs.

3. `agents/` is stronger than simple personas.
   The heavier agent files define confidence thresholds, verdict structures, and review/process contracts.

4. `contexts/` is intentionally light.
   It stays out of ownership and only biases behavior.

5. `docs/` contains genuine normative documents.
   It is not safe to treat the docs folder as commentary only.

## Structural Value As Reference

This repo is useful because the Markdown surfaces make these boundaries explicit:

- entry vs body
- role vs mode
- guard vs workflow
- standard vs procedure
- explanation vs contract

That separation is visible before reading much code, which is exactly why this repo is a strong structure-first reference.
