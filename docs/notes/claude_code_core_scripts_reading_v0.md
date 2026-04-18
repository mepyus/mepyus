# Claude Code Core Scripts Reading v0

## Scope

This note focuses on the main executable scripts inside `references/git_search/claude-code-main`.

It is not a full repo review.
It follows the code paths that actually power the most important plugin behaviors.

## Files Read

### Hookify

- [plugins/hookify/core/config_loader.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/core/config_loader.py)
- [plugins/hookify/core/rule_engine.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/core/rule_engine.py)
- [plugins/hookify/hooks/pretooluse.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/pretooluse.py)
- [plugins/hookify/hooks/stop.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/hookify/hooks/stop.py)

### Ralph Wiggum

- [plugins/ralph-wiggum/scripts/setup-ralph-loop.sh](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/scripts/setup-ralph-loop.sh)
- [plugins/ralph-wiggum/hooks/stop-hook.sh](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/ralph-wiggum/hooks/stop-hook.sh)

### Security and examples

- [plugins/security-guidance/hooks/security_reminder_hook.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/plugins/security-guidance/hooks/security_reminder_hook.py)
- [examples/hooks/bash_command_validator_example.py](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/examples/hooks/bash_command_validator_example.py)

## Main Script Styles

The repo's main executable code is small, direct, and plugin-scoped.

There are three dominant styles:

1. thin event executors
2. compact core evaluators
3. stateful shell hooks

## Hookify: The Cleanest Core

`hookify` is the clearest example of a small but complete internal engine.

### Structure

- `config_loader.py`: reads `.claude/hookify.*.local.md`
- `rule_engine.py`: evaluates normalized rules
- `hooks/pretooluse.py`: loads rules for bash/file events and runs engine
- `hooks/stop.py`: loads stop rules and runs engine

### Connection line

project `.claude/hookify.*.local.md`
-> frontmatter/message parse
-> normalized `Rule` + `Condition`
-> `RuleEngine`
-> event-specific JSON response to Claude hook runtime

### What matters

#### `config_loader.py`

This file does the structural work.

It:
- defines `Condition` and `Rule`
- converts simple `pattern` rules into condition lists
- parses YAML-like frontmatter from markdown
- loads only enabled rules
- filters rules by event

Important detail:
- the config surface is markdown, but the runtime surface is typed rule objects

That means the plugin separates:
- authoring format
- parsed model
- execution logic

#### `rule_engine.py`

This is the real core.

It:
- caches regex compilation
- checks all rules
- separates blocking matches from warning matches
- emits different response shapes depending on hook event

Important detail:
- `Stop` returns `decision=block`
- `PreToolUse` / `PostToolUse` return `permissionDecision=deny`

So the engine is not just matching patterns.
It knows the output contract for different hook phases.

#### `pretooluse.py` and `stop.py`

These are deliberately thin.

They:
- load stdin JSON
- infer event type
- load matching rules
- call the engine
- always emit JSON
- fail open on import/runtime errors

Important detail:
- these executors never try to own matching logic themselves
- they only bridge Claude hook input to the engine

### Hookify conclusion

`hookify` is a miniature architecture:

- user-defined local markdown rules
- parser/normalizer layer
- rule evaluation core
- tiny per-event executors

This is probably the strongest “small internal engine” pattern in `claude-code-main`.

## Ralph Wiggum: Stateful Loop Hook

`ralph-wiggum` is structurally different.
It is less like an engine and more like a small state machine implemented through one state file and one stop hook.

### Structure

- `setup-ralph-loop.sh`: initialize state
- `stop-hook.sh`: intercept exit and continue loop

### Connection line

command activation
-> `.claude/ralph-loop.local.md`
-> stop event
-> transcript read
-> completion/max-iteration check
-> either stop loop or block exit and feed same prompt back

### What matters

#### `setup-ralph-loop.sh`

This script is not trivial glue.
It:
- parses prompt and options
- validates max iteration and completion promise arguments
- creates `.claude/ralph-loop.local.md`
- writes loop state as markdown frontmatter + prompt body
- prints strong operator warnings and promise discipline

Important detail:
- the state file is intentionally human-readable and session-local
- the prompt body itself is the payload for future loop iterations

#### `stop-hook.sh`

This is the actual loop operator.

It:
- reads hook input JSON
- checks for active state file
- parses frontmatter
- validates state integrity
- enforces max iteration stop
- opens transcript JSONL
- extracts last assistant text
- checks completion promise in `<promise>` tags
- increments iteration
- outputs blocking JSON with the original prompt as `reason`

Important detail:
- the loop is implemented by blocking stop and reusing the same prompt
- transcript parsing is used only to detect completion, not to generate the next prompt

This keeps the loop method simple:
- prompt stays constant
- files and git history carry progress

### Ralph conclusion

`ralph-wiggum` is not a general orchestration engine.
It is a focused in-session loop state machine built from:
- one setup script
- one markdown state file
- one stop hook

## Security Guidance: Focused Single-Purpose Hook

`security_reminder_hook.py` shows a third pattern:
one self-contained policy checker.

### Structure

It:
- receives hook JSON
- only handles file-edit tools
- extracts content and file path
- checks against hardcoded security patterns
- persists per-session warning state in `~/.claude`

### What matters

- It is intentionally standalone.
- It does not share a generic rule engine with other plugins.
- It chooses focused practicality over abstraction.

This is different from `hookify`.
`hookify` builds a reusable engine.
`security-guidance` builds one dedicated checker.

## Example Hook: Minimal Reference Pattern

`examples/hooks/bash_command_validator_example.py` is useful because it shows the smallest viable hook shape:

- parse stdin JSON
- inspect tool name and input
- collect violations
- print warnings to stderr
- exit `2` to block

This example helps explain the rest of the repo:
many plugin hooks are just more specialized versions of this basic contract.

## Cross-Script Pattern

Across these files, the repo repeatedly uses the same structural move:

1. keep hook executors thin
2. keep state external in markdown/json files when needed
3. use one compact core per plugin instead of one shared mega-runtime

That is the main code-level trait of `claude-code-main`.

## What This Means Structurally

`claude-code-main` does not hide a large shared runtime behind the plugins.

Instead, each important plugin tends to choose one of these shapes:

- tiny engine + thin hooks (`hookify`)
- state file + lifecycle hook (`ralph-wiggum`)
- single-purpose checker (`security-guidance`)

So the repo's internal code philosophy is:

- keep packages small
- keep runtime logic close to the plugin
- prefer explicit data files and simple scripts over heavy shared infrastructure

## Best Reference Value

This repo is strongest when you want examples of:

- small hook runtimes
- event executor separation
- local markdown/json state as plugin memory
- focused plugin-specific engines instead of one giant shared core
