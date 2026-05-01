[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Token efficiency Claude Codex stdy note v0

## source metadata

- source_url: `https://www.stdy.blog/increasing-token-efficiency-by-setting-adjustment-in-claude-and-codex/`
- source_title: `Claude Code 및 Codex 설정 변경으로 토큰을 절약하는 방법`
- source_author: `Steady Study`
- source_type: `external article`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo`

## why this source matters

This source matters because it is not a generic AI essay.

It is a concrete operational article about where coding-agent token waste actually comes from and which configuration levers can reduce unnecessary context load in Claude Code and Codex.

That overlaps with active concerns in our space around:

- token efficiency
- bounded tool surfaces
- controlling automatic context injection
- limiting oversized outputs
- worker-style non-interactive execution
- avoiding unnecessary connector or web-tool expansion

## core claim

The article's core claim is that token waste in coding agents comes less from one abstract cause and more from repeated operational surfaces such as:

1. automatically injected extra context
2. oversized tool output left in history
3. external connectors and IDE/tool integrations that add extra calls and context

The practical message is:

- token efficiency improves when the operator narrows what gets injected by default
- but every reduction has tradeoffs, and the wrong reduction can cause more retries or missing context

## Claude Code section

The article lists several Claude Code levers:

- turning off git instruction injection if it is not needed
- keeping IDE auto-connect off unless IDE context is truly useful
- respecting `.gitignore` during globbing so large ignored trees do not flood search results
- lowering output caps carefully
- disabling MCP, memory, `CLAUDE.md`, or built-in agents for very small or worker-style runs
- restricting tools in simple or non-interactive modes

The key pattern is not “disable everything.”

The real pattern is:

- reduce automatic context that is not helping the current task
- preserve only the surfaces that are actually needed for the current mode

## Codex section

The Codex part says there are fewer obvious token levers, but a few still matter:

- disable ChatGPT-connected apps/connectors if they are not needed
- disable web search when local codebase work does not require it
- cap tool output size
- use non-interactive execution flags and profiles for worker-like runs
- use cleaner machine-readable output surfaces such as JSON and output-last-message files
- use read-only sandbox for read-only automation so failed write attempts do not create retry loops
- use ephemeral mode to avoid unnecessary session persistence

Again, the central pattern is boundedness:

- keep the tool and context surface no larger than the job requires

## strongest structural signals

This source reinforces several signals that already appear in our space.

### 1. structure before free-form agenting

The article repeatedly argues for:

- setting the mode first
- deciding which connectors/tools are allowed
- deciding whether the run is interactive or worker-style
- narrowing default context before the agent starts

This aligns strongly with precondition-first operation.

### 2. bounded surface over universal agent freedom

The article does not celebrate maximum tool freedom.

It prefers:

- only the tools needed
- only the connectors needed
- only the context surface needed
- explicit profiles or aliases for different run modes

This is a clear bounded-surface signal.

### 3. maintenance and validation discipline

The article also warns that aggressive caps or stripped settings can backfire:

- the model may need to re-run commands
- important tail information may be lost
- certain workflows may break if too much context is removed

So the source is not only about cutting tokens.
It is about making careful, reversible, workload-sensitive adjustments.

## bounded relevance to our current space

This source is especially relevant to our space because we already care about:

- script-first vs Codex-first division
- external tool boundary
- bounded connector usage
- read-only or worker-style runs
- output size and context budget

It should still be read as:

- a concrete operating reference
- not a direct mandate to disable every feature
- not a direct architecture replacement

## current bounded judgment

- useful as a strong external operating note
- more concrete than a broad philosophy article because it names real settings and tradeoffs
- especially useful for bounded mode selection, connector discipline, and output-budget thinking
- still not enough by itself for promotion
- keep as external ingest material with no promotion
