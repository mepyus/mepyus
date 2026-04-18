# Claude Code MD Deep Reading v0

## Purpose

This note reads `references/git_search/claude-code-main` through its Markdown and manifest-adjacent surfaces first.

The goal is to understand the repo as a packaged plugin space, not as a general operating architecture.

## Files Read

### Root

- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/README.md)
- [plugins/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/README.md)
- [examples/settings/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/examples/settings/README.md)

### Plugin READMEs

- [plugins/hookify/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/README.md)
- [plugins/ralph-wiggum/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/README.md)
- [plugins/code-review/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/code-review/README.md)
- [plugins/feature-dev/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/feature-dev/README.md)
- [plugins/plugin-dev/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/plugin-dev/README.md)
- [plugins/commit-commands/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/commit-commands/README.md)

### Command and hook surfaces

- [plugins/feature-dev/commands/feature-dev.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/feature-dev/commands/feature-dev.md)
- [plugins/code-review/commands/code-review.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/code-review/commands/code-review.md)
- [plugins/hookify/commands/hookify.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/commands/hookify.md)
- [plugins/ralph-wiggum/commands/ralph-loop.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/commands/ralph-loop.md)
- [plugins/hookify/hooks/hooks.json](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/hooks.json)
- [plugins/security-guidance/hooks/hooks.json](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/security-guidance/hooks/hooks.json)

## First Structural Impression

`claude-code-main` is not organized around one canonical workflow body the way `everything-claude-code-main` is.

Its canonical unit is the **plugin**.

That means the repo is best read as:

- root product intro
- plugin catalog
- self-contained plugin packages
- a few examples/settings surfaces

## Root Layer

### `README.md`

The root [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/README.md) is primarily host-product oriented.

It explains:
- what Claude Code is
- how to install it
- where official docs live
- that plugins exist

It does **not** function as a deep architectural guide for the repo itself.

This is a key difference from `everything-claude-code-main`, whose root docs are much more system-descriptive.

### `plugins/README.md`

[plugins/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/README.md) is the actual structural center of the repo.

It does three important things:

1. defines the plugin system concept
2. enumerates each bundled plugin and its components
3. shows the standard plugin directory layout

So if the root README tells you what Claude Code is, `plugins/README.md` tells you what this repo actually contains.

## Repo-Level Structure

At the folder level, the meaningful spaces are:

- `plugins/`
- `examples/`
- `.claude/commands/`

But the weight is not evenly distributed.

### `plugins/`

This is the real center.

Each plugin acts like a small product package with:
- `README.md`
- `.claude-plugin/plugin.json`
- optional `commands/`
- optional `agents/`
- optional `hooks/`

### `examples/`

This is not a workflow layer.
It is a deployment/configuration example surface.

[examples/settings/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/examples/settings/README.md) shows that these examples are mostly organization-level configuration templates.

### `.claude/commands/`

This is a smaller embedded command surface.
It does not appear to dominate the repo the way plugin packages do.

## Plugin-First Architecture

The strongest pattern visible after reading several plugins is:

**Each plugin is a self-contained workflow bundle.**

The bundle may contain:
- one or more commands
- one or more agents
- one or more hooks
- sometimes a skill-like behavior

This is different from `everything-claude-code-main`, where:
- skills are becoming canonical
- commands often degrade into shims
- docs define a broader operating architecture

In `claude-code-main`, the plugin remains the primary packaging boundary.

## Plugin Types Observed

Reading several plugin READMEs shows at least five plugin subtypes.

### 1. Workflow plugins

Examples:
- `feature-dev`
- `code-review`
- `commit-commands`

Traits:
- one main command
- clear user task
- defined phase or step sequence
- sometimes agent orchestration inside

These feel like packaged workflows.

### 2. Hook plugins

Examples:
- `hookify`
- `security-guidance`
- `explanatory-output-style`
- `learning-output-style`

Traits:
- behavior injection around session/tool events
- hook JSON is central
- README emphasizes triggering and no-restart or lightweight configuration

These are behavioral overlays rather than full workflows.

### 3. Loop/orchestration plugins

Example:
- `ralph-wiggum`

Traits:
- long-running or repeated behavior
- hook-assisted continuation
- control behavior inside one session

### 4. Development-kit plugins

Examples:
- `plugin-dev`
- `agent-sdk-dev`

Traits:
- meta-development tooling
- help build other plugins or SDK apps
- heavier documentation and guidance

### 5. Style/policy plugins

Examples:
- `frontend-design`
- `claude-opus-4-5-migration`

Traits:
- targeted behavioral or migration guidance
- narrower scope than full workflows

## Internal Texture of Key Plugins

### `hookify`

Read:
- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/README.md)
- [commands/hookify.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/commands/hookify.md)
- [hooks/hooks.json](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/hooks.json)

What becomes clear:

- README provides the user story and rule format
- command file provides the conversational workflow for creating rules
- hook JSON installs the actual event bindings

So the connection line is:

user request -> command-driven rule authoring -> `.claude/*.local.md` rule files -> runtime hook interpreter

This plugin is structurally elegant because it separates:
- rule authoring
- rule storage
- rule execution

### `ralph-wiggum`

Read:
- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/README.md)
- [commands/ralph-loop.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/commands/ralph-loop.md)

What becomes clear:

- README explains the method and stop-hook loop philosophy
- command surface is intentionally tiny
- execution is delegated to setup script + stop hook behavior

So the plugin package uses:
- rich README for method framing
- minimal command file for activation

### `code-review`

Read:
- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/code-review/README.md)
- [commands/code-review.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/code-review/commands/code-review.md)

What becomes clear:

- README explains the public workflow in plain language
- command file contains the strict operational algorithm

The command file is much denser and more execution-specific than the README.
It specifies:
- exact agent sequencing
- tool assumptions
- validation pipeline
- filtering rules
- comment-posting behavior

This shows a common pattern in the repo:
- README = human-facing overview
- command = runtime-grade operating instruction

### `feature-dev`

Read:
- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/feature-dev/README.md)
- [commands/feature-dev.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/feature-dev/commands/feature-dev.md)

What becomes clear:

- README gives the 7-phase narrative
- command file encodes the 7-phase behavior more directly

This plugin is a good example of a packaged workflow bundle:
- one main command
- several supporting agents
- explicit multi-phase development process

### `plugin-dev`

Read:
- [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/plugin-dev/README.md)

What becomes clear:

- this is a meta-plugin for building plugins
- it groups many subskills into one toolkit
- it acts more like a documentation-rich dev kit than a narrow workflow

It is one of the few plugins that feels closer to `everything` in ambition, but still remains packaged as a plugin.

## Commands Inside Plugins

Unlike `everything-claude-code-main`, command files here are usually not shims to a broader canonical skill layer.

They are often the actual operating surface for the plugin.

Examples:
- `feature-dev/commands/feature-dev.md`
- `code-review/commands/code-review.md`
- `hookify/commands/hookify.md`
- `ralph-wiggum/commands/ralph-loop.md`

This is a major distinction:

- in `everything`, command often points beyond itself
- in `claude-code-main`, command often is the package's main executable instruction layer

## Hooks Inside Plugins

Hooks are plugin-owned, not repo-wide operating infrastructure.

Examples:
- `hookify/hooks/hooks.json`
- `security-guidance/hooks/hooks.json`

This means hook behavior is scoped by plugin package.
Each plugin can add its own reactive layer without needing one shared mega-hook system.

That makes the repo modular, but also less unified than `everything`.

## Examples and Settings

[examples/settings/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/examples/settings/README.md) shows that `examples/` is mostly deployment and governance support.

It does not try to be an architecture surface.

So `examples/` here is:
- configuration aid
- organization rollout reference
- managed settings baseline

## What This Repo Is Structurally

`claude-code-main` is best described as:

**a plugin catalog repo with packaged workflow bundles**

Not:
- a full operating architecture repo
- a runtime substrate repo
- a control-plane decomposition repo

Its strengths are:
- modular packaging
- concrete plugin examples
- small self-contained workflow bundles
- clear command/agent/hook combinations

## Main Structural Differences from `everything-claude-code-main`

### Canonical unit

- `claude-code-main`: plugin
- `everything-claude-code-main`: broader operating surface, increasingly skill-centered

### Docs role

- `claude-code-main`: plugin-level README and command docs
- `everything-claude-code-main`: repo-level operating philosophy, policy, and contracts

### Command role

- `claude-code-main`: often the real workflow surface
- `everything-claude-code-main`: often transitional or compatibility-facing

### Hook role

- `claude-code-main`: plugin-scoped behavior overlays
- `everything-claude-code-main`: part of a larger repo-wide operating layer

## Why This Repo Matters As Reference

This repo is valuable when the question is:

- how do we package one workflow tightly?
- how do command, agent, and hook live together in one small unit?
- how do we scope hook behavior to a feature bundle?
- how do we ship a focused operational bundle without building a whole meta-system?

It is less useful as a top-level architectural doctrine repo.
It is more useful as a small-package composition reference.
