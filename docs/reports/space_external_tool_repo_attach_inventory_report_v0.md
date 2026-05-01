# Space External Tool Repo Attach Inventory Report v0

## 1. Purpose

This report answers the first half of the user request:

- what the imported external tools are for
- what functional surfaces they expose
- which of them are worth carrying into our space at repo-attach or feature-attach level

## 2. Bounded Repo Set Read

Primary repos read for this pass:

- `oh-my-codex-main`
- `OpenHarness-main`
- `qmd-main`
- `ralph-main`
- `claude-code-main`
- `everything-claude-code-main`
- `autoresearch-master`

## 3. Repo Family Classification

| repo | primary purpose | current reading |
| --- | --- | --- |
| `oh-my-codex-main` | workflow layer around Codex | workflow/runtime overlay |
| `OpenHarness-main` | agent harness infrastructure | infrastructure/runtime architecture |
| `qmd-main` | local retrieval and search engine | retrieval/index layer |
| `ralph-main` | repeated completion loop over PRD items | bounded execution loop pattern |
| `claude-code-main` | base agent product + plugin examples | product/reference surface |
| `everything-claude-code-main` | install profile / rules / hook distribution | packaging/reference surface |
| `autoresearch-master` | autonomous ML research loop | specialized experiment harness |

## 4. Purpose / Function Readout

### 4.1 OMX (`oh-my-codex-main`)

Main purpose:

- strengthen Codex sessions with reusable workflow, skills, team runtime, and durable local state

Main surfaces:

- role keywords / workflows
- `.omx/` state
- team runtime
- HUD/operator support

Useful read:

- it is a workflow layer, not a replacement model runtime
- it distinguishes clarification, planning, team execution, and persistent completion loops

### 4.2 OpenHarness

Main purpose:

- open agent harness infrastructure with tools, skills, memory, permissions, MCP, background tasks, and coordination

Main surfaces:

- query engine / tool loop
- tool registry
- permission checker
- skills/plugins
- session state and multi-agent coordination

Useful read:

- this is the broadest infrastructure repo in the set
- it exposes the strongest "runtime replacement" pressure if taken wholesale

### 4.3 QMD

Main purpose:

- on-device document search across markdown and notes using BM25, vector search, reranking, CLI, and MCP

Main surfaces:

- local collections and indexing
- search / query / get surfaces
- `--json` / `--files` output for agents
- MCP server

Useful read:

- this repo is already shaped for agentic retrieval use
- its smallest attachable unit is clearer than the other repos

### 4.4 Ralph

Main purpose:

- autonomous repeated completion loop over PRD items with fresh-context iterations

Main surfaces:

- `prd.json`
- `progress.txt`
- loop script
- PRD and Ralph skills

Useful read:

- this is a completion-loop pattern, not a generic harness
- its main reusable idea is bounded repeated execution with append-only progress

### 4.5 Claude Code Main

Main purpose:

- base product entry, plugin examples, and setup guidance

Main surfaces:

- core product usage
- plugin directory
- hooks/examples

Useful read:

- useful as product/reference grounding
- not a good repo-level attach target for our space

### 4.6 Everything-Claude-Code

Main purpose:

- modular install profiles, rules, agents, commands, and hooks for Claude Code setups

Main surfaces:

- install profiles
- packaged rules
- hooks/runtime add-ons

Useful read:

- strongest value is install/profile packaging ideas
- this is not a core engine candidate for us

### 4.7 Autoresearch

Main purpose:

- autonomous experimental loop for model training iteration

Main surfaces:

- one-file model modification loop
- experiment cycle under fixed time budget
- `program.md` as human-written research-org surface

Useful read:

- very specialized
- meaningful only as a narrow "experiment loop" pattern, not as near-term space attachment

## 5. First Attachability Split

### Strong attach candidates

- `qmd-main`

Reason:

- clearest bounded function
- retrieval/index layer is separable from the rest of our runtime
- its CLI/MCP/file output shapes map well to agent-facing retrieval support

### Bounded pattern candidates

- `OpenHarness-main`
- `oh-my-codex-main`
- `ralph-main`

Reason:

- they contain useful function or runtime patterns
- but repo-level import would overreplace too much of our current structure

### Reference-only for now

- `claude-code-main`
- `everything-claude-code-main`
- `autoresearch-master`

Reason:

- useful for grounding, packaging ideas, or narrow inspiration
- not strong near-term repo attach targets under the current space boundary

## 6. Report-First Conclusion

The imported tool set does not behave like one adoption pool.

It splits into three kinds:

1. one strong bounded retrieval candidate (`qmd-main`)
2. several useful runtime/workflow patterns that should be borrowed selectively (`OpenHarness`, `OMX`, `Ralph`)
3. several repos that should remain reference-only for now

That is the correct first report before any structuring decision.
