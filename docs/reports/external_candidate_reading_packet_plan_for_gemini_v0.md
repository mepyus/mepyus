# External Candidate Reading Packet Plan for Gemini v0

## 1. Purpose

Prepare bounded Gemini readings for four external candidates:

```text
1. https://github.com/mksglu/context-mode
2. https://github.com/Q00/ouroboros
3. https://github.com/ENTERPILOT/GoModel
4. https://aifrontier.kr/ko/episodes/ep94/
```

This plan does not decide adoption.

It prepares the User to manually pass one source at a time to Gemini so Gemini can return worker evidence.

This plan is:

```text
candidate reading packet plan
not implementation
not adoption
not automation
not tool attachment
not workflow
not registry/index/ledger
not current-position update
```

Authority:

```text
Gemini returns worker evidence only.
Codex structures packets and later packages returned evidence.
ChatGPT/User review direction and decide.
User gate remains final.
```

Source access note:

```text
Codex performed a lightweight source identity check on the four User-provided URLs.
Detailed source reading is delegated to Gemini through the packets below.
```

## 2. Current Project State

```text
Formation Prework Round 1 is closed.
MCP and AWS sample-deep-insight are preserved as operation references.
Current state is WAIT_FOR_NEXT_EXTERNAL_CANDIDATE.
New external candidates have now appeared.
The next safe move is to read them one by one through bounded Gemini worklists.
```

Relevant current references:

```text
docs/reports/function_process_formation_prework_candidate_v1.md
docs/reports/reusable_settings_and_formation_prework_bridge_v0.md
docs/reports/function_process_formation_prework_real_test_round1_closeout_v0.md
docs/reports/next_chat_reentry_summary_after_formation_prework_round1_v0.md
docs/reports/whole_space_second_pass_structural_synthesis_note_v0.md
```

Current reusable lenses:

```text
Formation Prework v1
Resource / Tool
Plan before Execution
Mistake-Memory
Worker Evidence Packaging
Bounded Deep Reread
Continue-Until-Blocked
User-as-Judge
```

## 3. Candidate Overview Map

| Candidate | Source | Initial type | Likely lens | Possible project role | Main risk | Suggested read order |
|---|---|---|---|---|---|---|
| `context-mode` | `https://github.com/mksglu/context-mode` | tool / MCP / context-management candidate | Resource / Tool, Worker Evidence Packaging, Bounded Deep Reread | context handling, session continuity, tool-output containment, worker packet affordance | MCP/tool attachment pressure; automatic routing/hook adoption pressure | 1 |
| `ouroboros` | `https://github.com/Q00/ouroboros` | agent workflow / spec-first operation candidate | Plan before Execution, Formation Prework, User-as-Judge | specification-first planning, replayability, evaluation loop comparison | Agent OS / hidden architecture drift; plan packet becoming mandatory workflow | 2 |
| `GoModel` | `https://github.com/ENTERPILOT/GoModel` | API gateway / provider abstraction candidate | Resource / Tool, Tool-side execution, Observability / Guardrail | provider gateway comparison, observability / guardrail reference | implementation pressure; gateway adoption; multi-provider routing becoming architecture | 3 |
| `AI Frontier EP94` | `https://aifrontier.kr/ko/episodes/ep94/` | strategic context / market trend reference | Formation Prework, User-as-Judge, Tool unbundling context | background for managed agents, wrapper fragility, model/tool unbundling | trend becoming law; overgeneralized strategy claim | 4 |

## 4. Reading Order Decision

Recommended order:

```text
1. context-mode
2. ouroboros
3. GoModel
4. AI Frontier EP94
```

### 4.1 context-mode

why read now:

```text
It appears most directly connected to context management, session continuity, tool output handling, and worker evidence packaging.
It also directly pressures Resource / Tool boundaries because it is an MCP/tooling candidate.
```

why read before others:

```text
It can clarify how "context as resource" and "tool output as contained evidence" should be read before reading broader agent workflow or gateway candidates.
```

what Gemini should focus on:

```text
context saving
session continuity
tool output containment
raw output vs indexed/retrieved evidence
worker packet / evidence packaging relevance
MCP/tool attachment pressure
```

what Gemini should avoid:

```text
install instructions as adoption recommendation
MCP server adoption
automatic hook/routing adoption
turning context-mode architecture into our architecture
```

### 4.2 ouroboros

why read now:

```text
It appears relevant to specification-first operation and replayable AI coding workflows.
```

why read after context-mode:

```text
After context/resource boundaries are clearer, ouroboros can test whether plan/spec-first workflow signals fit without becoming a mandatory workflow.
```

what Gemini should focus on:

```text
specification-first structure
plan before execution
replayability
evaluation loop
policy-bound agent operation
```

what Gemini should avoid:

```text
agent OS adoption
hidden architecture import
workflow/baseline promotion
```

### 4.3 GoModel

why read now:

```text
It appears relevant to API gateway / provider abstraction / observability / guardrails.
```

why read after context-mode and ouroboros:

```text
It is closer to implementation and Tool-side execution pressure, so it should come after Resource/Tool and Plan/Execution reading is grounded.
```

what Gemini should focus on:

```text
provider abstraction
API gateway role
observability and guardrails
Tool-side execution layer
implementation pressure
```

what Gemini should avoid:

```text
gateway adoption recommendation
SDK/API implementation planning
multi-provider routing architecture import
```

### 4.4 AI Frontier EP94

why read now:

```text
It appears to be strategic context rather than a direct tool/function candidate.
```

why read last:

```text
It can contextualize the first three technical candidates, but reading it first may overgeneralize trends into laws.
```

what Gemini should focus on:

```text
managed agents
wrapper fragility
model/tool unbundling
Claude Code / Codex app discussion
why tools should be formed before adoption
```

what Gemini should avoid:

```text
market trend as project law
strategic commentary as implementation direction
overgeneralized doctrine
```

## 5. Gemini Packet Design Principles

Gemini should:

```text
read one source at a time
return worker evidence only
distinguish source claims from project interpretation
identify useful comparison lenses
identify candidate signals
identify watch items
identify what should not be inferred
avoid adoption / implementation recommendations
avoid broad unrelated research
avoid turning source architecture into project architecture
stop after final STATUS
```

Gemini should not:

```text
install, clone, run, or execute anything
recommend adoption
create architecture
create workflow
create schema
create automation
grant itself authority
update current-position
```

## 6. Per-Source Gemini Worklists

### 6.1 Gemini Packet - context-mode

```markdown
# Gemini Packet — context-mode External Candidate Reading

## Role

You are Gemini acting as a bounded reader and evidence collector.

You are not an implementer, adopter, installer, architect, router, or authority.

## Source

https://github.com/mksglu/context-mode

## Mode

External candidate reading.
Worker evidence only.
No implementation.
No adoption recommendation.

## Purpose

Read `context-mode` as an external candidate related to context handling, session continuity, tool-output containment, and worker evidence packaging.

The goal is to understand what it claims and how it may compare to our Formation Prework / Resource-Tool / worker-evidence boundaries.

## Reading Questions

1. What problem does context-mode claim to solve?
2. What are its main mechanisms?
3. How does it treat raw tool output, indexed evidence, session continuity, context compression, and routing/hook behavior?
4. Which parts look Resource-side, Tool-side, or both?
5. Which parts are relevant to worker evidence packaging or bounded deep reread?
6. Which parts create MCP/tool adoption pressure?

## Formation Prework Focus

Answer:

- what arrived
- why it may matter
- possible space role
- prior project lenses it touches
- candidate signals
- watch items
- what still requires User decision

## Resource / Tool Check

Classify major elements as:

- Resource-side context/material
- Tool-side action/operation
- both
- unclear

Do not turn Resource / Tool into rigid ontology.

## Plan / Execution Check

Does context-mode require a Plan Packet before Execution, or is it mainly context/evidence infrastructure?

## Process Asset Signal Check

Does this source suggest reusable process assets for:

- bounded evidence retrieval
- output containment
- session continuity
- worker packet design
- mistake-memory or context recovery

## Pipeline Candidate Check

Could this source inspire a pipeline candidate?

If yes, mark it as `CANDIDATE_ONLY`.

Do not recommend implementation.

## Watch Items

Check:

- context-mode becoming MCP attachment pressure
- hook/routing behavior becoming hidden router
- context-saving becoming automation pressure
- indexed session memory becoming registry/ledger
- tool output containment becoming verified truth
- installation instructions being mistaken for recommendation

## Do Not Infer

- no MCP adoption
- no plugin installation
- no hook adoption
- no routing adoption
- no context-mode architecture import
- no official workflow
- no automation
- no current-position update

## Expected Output Structure

Return:

1. Status
2. Source Summary
3. Source Claim Evidence
4. Resource / Tool Map
5. Formation Prework Candidate Signals
6. Worker Evidence Packaging Relevance
7. Process Asset Signals
8. Watch Items
9. Do-Not-Infer List
10. Recommendation for handling: CANDIDATE_ONLY / WATCH_ONLY / HOLD / DISCARD
11. Uncertainty
12. Final Status

## Final Status

Use one:

STATUS: SOURCE_READ_COMPLETE
STATUS: SOURCE_READ_BLOCKED

After the final STATUS line, output nothing else.
```

### 6.2 Gemini Packet - ouroboros

```markdown
# Gemini Packet — ouroboros External Candidate Reading

## Role

You are Gemini acting as a bounded reader and evidence collector.

You are not an implementer, adopter, installer, architect, router, or authority.

## Source

https://github.com/Q00/ouroboros

## Mode

External candidate reading.
Worker evidence only.
No implementation.
No adoption recommendation.

## Purpose

Read `ouroboros` as an external candidate related to specification-first operation, replayability, planning before execution, agent workflow, and evaluation loops.

The goal is to understand whether it offers comparison evidence for our Plan before Execution / Formation Prework / User-as-Judge boundaries.

## Reading Questions

1. What does ouroboros mean by "Stop prompting. Start specifying"?
2. What is its proposed workflow or operating model?
3. How does it separate specification, planning, execution, replayability, and evaluation?
4. What does it imply about agent OS or agent workflow structure?
5. Which ideas are useful as comparison only?
6. Which ideas risk becoming hidden architecture or mandatory workflow?

## Formation Prework Focus

Answer:

- what arrived
- why it may matter
- possible space role
- prior project lenses it touches
- candidate signals
- watch items
- what still requires User decision

## Resource / Tool Check

Classify whether ouroboros is mainly:

- Resource-side specification/material
- Tool-side execution system
- Plan/Execution framework
- agent workflow candidate
- unclear

Do not turn this classification into ontology.

## Plan / Execution Check

Focus on:

- specification before execution
- plan artifact before execution artifact
- replayability
- evaluation loop
- policy-bound operation

Compare lightly with our existing `Plan Packet before Execution` signal.

## Process Asset Signal Check

Does this source suggest reusable process assets for:

- plan packet design
- execution packet design
- replayable task records
- evaluation loops
- worker handoff

## Pipeline Candidate Check

Could this source inspire a pipeline candidate?

If yes, mark it as `CANDIDATE_ONLY`.

Do not recommend implementation.

## Watch Items

Check:

- ouroboros becoming agent OS adoption pressure
- specification-first becoming mandatory workflow
- replayability becoming ledger
- evaluation loop becoming hidden controller
- plan packet becoming ceremony
- source architecture becoming project architecture

## Do Not Infer

- no ouroboros adoption
- no agent OS adoption
- no workflow creation
- no policy/schema import
- no implementation
- no current-position update
- no autonomous agent authority

## Expected Output Structure

Return:

1. Status
2. Source Summary
3. Source Claim Evidence
4. Plan / Execution Map
5. Resource / Tool Map
6. Formation Prework Candidate Signals
7. Process Asset Signals
8. Watch Items
9. Do-Not-Infer List
10. Recommendation for handling: CANDIDATE_ONLY / WATCH_ONLY / HOLD / DISCARD
11. Uncertainty
12. Final Status

## Final Status

Use one:

STATUS: SOURCE_READ_COMPLETE
STATUS: SOURCE_READ_BLOCKED

After the final STATUS line, output nothing else.
```

### 6.3 Gemini Packet - GoModel

```markdown
# Gemini Packet — GoModel External Candidate Reading

## Role

You are Gemini acting as a bounded reader and evidence collector.

You are not an implementer, adopter, installer, architect, router, gateway designer, or authority.

## Source

https://github.com/ENTERPILOT/GoModel

## Mode

External candidate reading.
Worker evidence only.
No implementation.
No adoption recommendation.

## Purpose

Read `GoModel` as an external candidate related to API gateway, provider abstraction, observability, guardrails, streaming, cost/usage tracking, and multi-provider routing.

The goal is to understand whether it is useful as a Tool-side comparison reference and whether it should remain watch-only due to implementation pressure.

## Reading Questions

1. What problem does GoModel claim to solve?
2. What provider abstraction or OpenAI-compatible API surface does it expose?
3. What observability, guardrail, cost, usage, streaming, or routing mechanisms does it describe?
4. Is it Resource-side, Tool-side, or gateway infrastructure?
5. What risks would appear if this were read as an implementation target?
6. Should it be Formation Prework-ready, watch-only, or hold?

## Formation Prework Focus

Answer:

- what arrived
- why it may matter
- possible space role
- prior project lenses it touches
- candidate signals
- watch items
- what still requires User decision

## Resource / Tool Check

Classify:

- Resource-side material
- Tool-side execution layer
- API/provider gateway
- observability/guardrail reference
- unclear

Do not turn this into architecture.

## Plan / Execution Check

Does GoModel suggest anything about planning before execution?

Or is it mainly execution/gateway infrastructure?

## Process Asset Signal Check

Does this source suggest reusable process assets for:

- provider selection review
- gateway boundary review
- observability checklist
- guardrail packet design
- usage/cost evidence capture

## Pipeline Candidate Check

Could this source inspire a future pipeline candidate?

If yes, mark it as `CANDIDATE_ONLY` or `WATCH_ONLY`.

Do not recommend implementation.

## Watch Items

Check:

- GoModel becoming gateway adoption pressure
- API abstraction becoming project architecture
- multi-provider routing becoming hidden router
- observability becoming ledger
- guardrails becoming formal permission system
- source docs becoming implementation plan

## Do Not Infer

- no GoModel adoption
- no gateway implementation
- no SDK/API work
- no provider routing architecture
- no observability stack creation
- no formal guardrail system
- no current-position update

## Expected Output Structure

Return:

1. Status
2. Source Summary
3. Source Claim Evidence
4. Resource / Tool / Gateway Map
5. Formation Prework Candidate Signals
6. Process Asset Signals
7. Watch Items
8. Do-Not-Infer List
9. Recommendation for handling: CANDIDATE_ONLY / WATCH_ONLY / HOLD / DISCARD
10. Uncertainty
11. Final Status

## Final Status

Use one:

STATUS: SOURCE_READ_COMPLETE
STATUS: SOURCE_READ_BLOCKED

After the final STATUS line, output nothing else.
```

### 6.4 Gemini Packet - AI Frontier EP94

```markdown
# Gemini Packet — AI Frontier EP94 External Candidate Reading

## Role

You are Gemini acting as a bounded reader and evidence collector.

You are not a strategist with final authority, market forecaster, implementer, adopter, or workflow creator.

## Source

https://aifrontier.kr/ko/episodes/ep94/

## Mode

External context/reference reading.
Worker evidence only.
No implementation.
No adoption recommendation.

## Purpose

Read AI Frontier EP94 as strategic background related to managed agents, wrapper fragility, model/tool unbundling, Claude Code / Codex apps, and why tools should be formed before adoption.

The goal is to decide whether this source is a context reference, comparison lens, watch item, or Formation Prework candidate.

## Reading Questions

1. What are the main claims or topics in the episode relevant to agents, tools, wrappers, and model/tool unbundling?
2. What does it suggest about managed agents or tool ecosystems?
3. Does it provide a concrete function/tool candidate, or mainly strategic background?
4. What does it imply about why our space should form tools before adopting them?
5. Which parts should remain context-only?
6. Which parts risk becoming overgeneralized trend law?

## Formation Prework Focus

Answer:

- what arrived
- why it may matter
- possible space role
- prior project lenses it touches
- candidate signals
- watch items
- what still requires User decision

## Resource / Tool Check

Classify:

- Resource-side context/reference
- Tool-side candidate
- strategic background
- comparison lens
- unclear

## Plan / Execution Check

Does this source support Plan before Execution?

Or does it mainly explain why premature tool adoption is risky?

## Process Asset Signal Check

Does this source suggest reusable process assets for:

- tool adoption caution
- managed-agent comparison
- wrapper fragility check
- model/tool unbundling interpretation
- strategic watch item extraction

## Pipeline Candidate Check

Could this source inspire a pipeline candidate?

If weak, mark `HOLD` or `WATCH_ONLY`.

Do not force a tool/function candidate if it is only context.

## Watch Items

Check:

- AI Frontier becoming overgeneralized trend law
- market commentary becoming project strategy
- managed agent discussion becoming adoption pressure
- wrapper fragility becoming hard prohibition
- model/tool unbundling becoming architecture claim

## Do Not Infer

- no strategic doctrine adoption
- no managed-agent adoption
- no wrapper/tool rejection by default
- no implementation plan
- no architecture change
- no baseline promotion
- no current-position update

## Expected Output Structure

Return:

1. Status
2. Source Summary
3. Source Claim Evidence
4. Context Reference vs Function Candidate Judgment
5. Formation Prework Candidate Signals
6. Watch Items
7. Do-Not-Infer List
8. Recommendation for handling: CONTEXT_REFERENCE / CANDIDATE_ONLY / WATCH_ONLY / HOLD / DISCARD
9. Uncertainty
10. Final Status

## Final Status

Use one:

STATUS: SOURCE_READ_COMPLETE
STATUS: SOURCE_READ_BLOCKED

After the final STATUS line, output nothing else.
```

## 7. Cross-Source Synthesis Plan

Do not synthesize before all four one-source readings are complete.

After all four readings, run a bounded synthesis asking:

```text
Which sources are one-time context references?
Which are Formation Prework candidates?
Which are comparison lenses only?
Which are watch/hold?
Which signals relate to Resource / Tool?
Which signals relate to Plan before Execution?
Which signals relate to pipeline-ready candidates?
Which should not move?
Which source, if any, deserves a Formation Prework v1 application?
```

Synthesis must still return:

```text
worker evidence
uncertainty
watch items
User decision needs
```

It must not return adoption, implementation, or architecture decisions.

## 8. User Decision Gate

User must decide:

```text
whether to send the packets to Gemini
whether to read all four or start with one
whether to approve a later synthesis
whether any source should move into Formation Prework v1
whether any source should be held or discarded
```

Codex may prepare packets.

Gemini may return evidence.

Only User can approve movement beyond candidate/reference handling.

## 9. Watch Items

```text
external source becoming adoption pressure
repo architecture becoming hidden architecture
Resource / Tool becoming rigid ontology
Plan Packet becoming mandatory workflow
GoModel becoming implementation pressure
context-mode becoming MCP attachment pressure
ouroboros becoming agent OS pressure
AI Frontier becoming overgeneralized trend law
Gemini evidence becoming truth
Codex packet becoming final authority
cross-source synthesis becoming ranking/selection authority
```

## 10. Do Not Do Yet

```text
no implementation
no automation
no runtime script
no repo cloning/running
no SDK work
no registry/index/ledger
no formal schema
no official workflow
no current-position update
no baseline promotion
no tool/API/function attachment
no MCP attachment
no AWS architecture adoption
no GoModel gateway adoption
no agent OS adoption
no Plan Packet workflow creation
no Gemini autonomous authority
no Codex final authority
```

## 11. Final Recommendation

Recommended first Gemini run:

```text
context-mode
```

Reason:

```text
It appears most directly connected to context management, session continuity, Resource / Tool boundary, tool output handling, and worker evidence packaging.
It also tests the strongest immediate risk: useful context tooling becoming MCP/tool attachment pressure.
```

Recommended sequence:

```text
1. context-mode
2. ouroboros
3. GoModel
4. AI Frontier EP94
```

After all four readings:

```text
run bounded cross-source synthesis
```

Do not run synthesis before all four readings are complete unless the User explicitly changes the plan.

## 12. Final Status

```text
STATUS: EXTERNAL_CANDIDATE_READING_PACKET_PLAN_FOR_GEMINI_PREPARED
```
