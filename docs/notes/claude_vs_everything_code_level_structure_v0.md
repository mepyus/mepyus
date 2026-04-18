# Claude Code Main vs Everything Claude Code Main
# Code-Level Structure Comparison v0

## Purpose

This note compares the two repos at the code-structure level.

The comparison axis is:

- `claude-code-main` as **plugin-local small engines**
- `everything-claude-code-main` as **repo-wide operating layer**

This is not a feature comparison.
It is a comparison of where runtime logic lives and how connection lines are formed.

## Files Read For Comparison

### `claude-code-main`

- [plugins/hookify/core/config_loader.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/core/config_loader.py)
- [plugins/hookify/core/rule_engine.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/core/rule_engine.py)
- [plugins/hookify/hooks/pretooluse.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/pretooluse.py)
- [plugins/hookify/hooks/stop.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/stop.py)
- [plugins/ralph-wiggum/scripts/setup-ralph-loop.sh](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/scripts/setup-ralph-loop.sh)
- [plugins/ralph-wiggum/hooks/stop-hook.sh](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/hooks/stop-hook.sh)
- [plugins/security-guidance/hooks/security_reminder_hook.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/security-guidance/hooks/security_reminder_hook.py)

### `everything-claude-code-main`

- [scripts/session-inspect.js](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/scripts/session-inspect.js)
- [scripts/lib/session-adapters/registry.js](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/scripts/lib/session-adapters/registry.js)
- [scripts/lib/orchestration-session.js](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/scripts/lib/orchestration-session.js)
- [scripts/lib/state-store/queries.js](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/scripts/lib/state-store/queries.js)
- [scripts/lib/inspection.js](/Users/sungsookim/universe/vectorfl_replica/references/git_search/everything-claude-code-main/scripts/lib/inspection.js)

## The Shortest Difference

`claude-code-main` usually solves a problem **inside one plugin package**.

`everything-claude-code-main` usually solves a problem **by lifting it into a repo-level shared operating layer**.

## Where The Core Lives

### `claude-code-main`

The core usually lives inside the plugin itself.

Examples:

- `hookify` owns:
  - config parsing
  - rule model
  - evaluation engine
  - per-event executors

- `ralph-wiggum` owns:
  - loop setup
  - local state file
  - stop-hook loop continuation

- `security-guidance` owns:
  - its own single-purpose checker

There is no strong evidence of one repo-wide shared runtime that all plugins depend on heavily.

### `everything-claude-code-main`

The core is spread across repo-level libraries and scripts.

Examples:

- `session-inspect.js` delegates to a shared adapter registry
- `session-adapters/registry.js` selects adapters across different source types
- `orchestration-session.js` builds unified snapshots from multiple files and tmux state
- `state-store/queries.js` defines repo-wide storage/query behavior
- `inspection.js` reads store outputs and derives recurring-failure reports

So the “core” is not a single plugin-local engine.
It is a shared operating layer used by many surfaces.

## Connection Line Shape

### `claude-code-main`

The connection line is usually short:

user action
-> plugin command or hook
-> plugin-local core
-> immediate output or state update

#### Example: Hookify

`.claude/hookify.*.local.md`
-> `config_loader.py`
-> `rule_engine.py`
-> `pretooluse.py` / `stop.py`
-> JSON response to Claude hook runtime

This is a tight loop inside one plugin.

#### Example: Ralph

`/ralph-loop`
-> `setup-ralph-loop.sh`
-> `.claude/ralph-loop.local.md`
-> `stop-hook.sh`
-> transcript read + iteration update
-> block exit and feed same prompt back

Again, short and local.

### `everything-claude-code-main`

The connection line is longer:

CLI or hook or observer surface
-> shared lib
-> adapter/snapshot/store layer
-> normalized structure
-> reporting / persistence / follow-on tooling

#### Example: Session inspection

`session-inspect.js`
-> `session-adapters/registry.js`
-> selected adapter
-> canonical snapshot
-> optional persistence or downstream inspection

#### Example: orchestration snapshot

plan/session target
-> `orchestration-session.js`
-> worker markdown files + tmux panes
-> unified worker snapshot

#### Example: failure inspection

state store
-> `state-store/queries.js`
-> recent skill runs
-> `inspection.js`
-> grouped normalized failure patterns
-> report

This is not one plugin's private logic.
It is a repo-wide dataflow.

## State Philosophy

### `claude-code-main`

State is often:
- local
- human-readable
- plugin-scoped
- minimal

Examples:
- `.claude/ralph-loop.local.md`
- `.claude/hookify.*.local.md`
- security warning state files in `~/.claude`

The plugin keeps only what it needs.

### `everything-claude-code-main`

State is more often:
- normalized
- queryable
- aggregate-friendly
- cross-surface

Examples:
- canonical session snapshots
- SQLite state store rows
- skill run records
- orchestration snapshots
- inspection reports

This is a stronger control-plane posture.

## Reuse Philosophy

### `claude-code-main`

Reuse is mostly package-level.

Example:
- `hookify` has a reusable engine, but it is still primarily for the hookify plugin.

Most plugins do not seem to route through one shared reusable abstraction layer.

### `everything-claude-code-main`

Reuse is repo-level and intentional.

Examples:
- adapters are used to normalize multiple session sources
- state store APIs are used across session/status tooling
- inspection/report logic assumes normalized stored data

The repo wants shared infrastructure.

## Script Thickness

### `claude-code-main`

The dominant script style is:
- thin executor
- compact plugin-local core
- direct file/state interaction

This makes plugins easy to understand in isolation.

### `everything-claude-code-main`

The dominant script style is:
- CLI router or façade
- layered library calls
- snapshot/store/report composition

This makes the repo feel more like an operating platform.

## Best Reading Of Each Repo

### `claude-code-main`

Best read as:

**small packaged workflow engines**

Use it when asking:
- how should one focused plugin own its runtime logic?
- how can a hook, command, and small state file form one complete feature?
- how do we keep execution local and understandable?

### `everything-claude-code-main`

Best read as:

**shared operating system for multiple surfaces**

Use it when asking:
- how should multiple surfaces share adapters, snapshots, and state?
- how do we normalize heterogeneous sources into one contract?
- how do we support inspection, persistence, and future operator surfaces?

## Translation Value

If we want a small, bounded capability:
- `claude-code-main` is usually the better reference

If we want a reusable, cross-surface operating layer:
- `everything-claude-code-main` is usually the better reference

## Strongest Contrast

The strongest contrast is this:

- `claude-code-main` keeps meaning close to the plugin
- `everything-claude-code-main` lifts meaning into shared infrastructure

That is the code-level form of the earlier structural difference between:

- **plugin-first packaging**
- **repo-wide operating architecture**
