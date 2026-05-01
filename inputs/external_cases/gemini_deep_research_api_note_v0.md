[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Gemini deep research API note v0

## source metadata

- source_title: `How to use Deep Research with the Gemini API`
- source_type: `external API/product documentation excerpt`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo from user-provided raw text`
- raw_source_file: `inputs/external_cases/gemini_deep_research_api.txt`

## why this source matters

This source matters because it describes a concrete long-horizon research agent surface with:

- asynchronous background execution
- plan-first collaborative planning
- explicit approval to move from plan to execution
- multimodal grounding
- external tool access through MCP
- generated visuals
- streaming progress and thought summaries

This is relevant to our space because it overlaps with active pressures around:

- bounded research orchestration
- plan before execution
- external tool boundary
- long-running work surfaces
- report-first output
- human review before stronger execution

## core claim

The source presents Gemini Deep Research not as a normal single-response model call, but as a background research agent running through the `interactions` surface.

The operating shape is:

1. start a long-running research task
2. poll or stream progress
3. optionally run collaborative planning first
4. explicitly flip from planning mode to execution mode
5. receive a detailed researched output with optional visuals and tool use

## operating structure

### 1. background interaction, not one-shot content generation

The source is explicit that deep research uses the `interactions` API and runs in the background.

This means the work unit is not:

- immediate short answer
- single blocking call

It is closer to:

- agent task
- running research job
- status-polled or streamed process

### 2. collaborative planning before execution

The most important operating rule in the source is the planning gate:

- `collaborative_planning=True` returns a plan
- refinement can continue across previous interaction state
- execution does not start until `collaborative_planning=False` is explicitly sent

This is a strong boundary signal:

- planning is not execution
- "go ahead" language alone is not enough
- mode switching must be explicit

### 3. tool surface is configurable and broad

The source says the research agent can use:

- Google Search
- URL Context
- Code Execution
- MCP server
- File Search

This matters because the agent is not presented as pure model reasoning.
It is a bounded research surface with tool permissions and source configuration.

### 4. multimodal and visualization support

The source also frames the agent as able to:

- ground on PDFs and documents
- use images and other material as research context
- return charts and infographics
- stream progress with thought summaries

So the output surface is not only text.
It is a richer report-oriented research surface.

## bounded relevance to our current space

This is not a direct adoption order.

But it is strongly relevant as a reference for:

- plan-first research workflow
- explicit transition from planning to execution
- long-running task surfaces instead of one-shot chat
- tool-bounded agent design
- report-first research output

It also reinforces several already-active pressures in our space:

- structure before free-form agenting
- bounded surface over universal agent freedom
- maintenance / review discipline before stronger execution

## important boundary

This source should not be overread as:

- “just turn our current space into Gemini Deep Research”
- “tool access means unrestricted execution”
- “planning and execution are the same phase”

The strongest reusable part is the boundary logic:

- planning first
- explicit execution approval
- configurable tool surface
- background task status handling

## current bounded judgment

- useful as a strong external operating reference
- especially relevant to planning/execution separation and bounded research orchestration
- stronger than a broad philosophy article because the API surface and execution boundary are concrete
- still not a direct architecture replacement by itself
- keep as external ingest material with no promotion
