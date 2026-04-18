# OpenHarness Study Report (Reference Analysis)

Date: 2026-04-15
Actor: Gemini-CLI
Source: `references/git_search/openharness-main/`
Reason: Analyzing OpenHarness architecture for potential application to VECTORFL engine design.

## 1. Core Philosophy: The "Agent Harness" Pattern
OpenHarness defines an agent as a "Harness" wrapping an LLM:
**Harness = Tools + Knowledge + Observation + Action + Permissions**
- **Intelligence**: Provided by the model.
- **Hands & Eyes**: Provided by the tools and observation loop.
- **Safety**: Provided by the permission/governance layer.

## 2. Key Architectural Features (Applicable to VECTORFL)

### A. Skill-Based Tactical Units (`SKILL.md`)
OpenHarness uses a very clean `.md` format for defining skills. This is a direct reference for our `vectorfl/skills/` implementation.
- **Structure**: Frontmatter (Metadata) + Principles + Workflow + Checklist + Pitfalls.
- **Attribution Checklist**: Ensures provenance and original author credit (highly aligned with our "Provenance" mandate).
- **Workflow**: Provides specific, executable command sequences.

### B. Persistent Memory (`MEMORY.md`)
OpenHarness manages personal and session memory using a structured Markdown approach.
- **Index**: `MEMORY.md` acts as a central index.
- **Atomicity**: Individual `.md` files store specific knowledge units.
- **Utility**: `load_memory_prompt` injects relevant memory fragments into the agent's context, preventing context bloat while maintaining long-term recall.

### C. Governance & Permissions
- **Multi-Level Modes**: Strict path-level and command-level rules.
- **Hooks**: `PreToolUse` and `PostToolUse` hooks allow for validation and logging before/after any action.
- **Safety Boundary**: Hardcoded sensitive paths and command denial lists.

### D. Swarm & Multi-Agent Coordination
- **Subagent Spawning**: Ability to delegate complex tasks to specialized sub-agents.
- **Team Registry**: Manages multiple agents working on the same workspace.

## 3. Comparison with VECTORFL Constitution

| Feature | OpenHarness | VECTORFL | Comparison |
| :--- | :--- | :--- | :--- |
| **Central Object** | Task / Tool Call | Fragment | OpenHarness is action-oriented; VECTORFL is interpretation-oriented. |
| **Knowledge** | `SKILL.md` | `Skills/` | Both use Markdown-based tactical units. OpenHarness's format is a great UI/UX reference. |
| **Provenance** | Attribution Checklist | Source Linkage / Event Ledger | Both prioritize the "Why" and "From Where". |
| **Safety** | Permissions / Hooks | Constitution / Baseline Lock | VECTORFL uses a more philosophical/constitutional lock; OpenHarness uses tool-level hooks. |
| **Memory** | `MEMORY.md` | `runtime/memory/` | OpenHarness's index-based MD approach is more human-readable than typical JSON memories. |

## 4. Proposed Adoptions for VECTORFL

1. **Standardize `SKILL.md` Format**: Adopt the "Principles + Workflow + Checklist + Pitfalls" structure for our `vectorfl/skills/` folder to improve agent clarity.
2. **Markdown-Based Memory Index**: Consider implementing a `MEMORY.md` index in `runtime/memory/` to allow human-readable audits of what the engine "remembers".
3. **Lifecycle Hooks**: Explore adding explicit `pre_action` and `post_action` hooks to our RPC calls (like `process_tank_job` in WashTank) to automate constitutional checks.

---
*Note: This report is stored in `gemini/` as per the current session protocol. No files outside `gemini/` were modified.*
