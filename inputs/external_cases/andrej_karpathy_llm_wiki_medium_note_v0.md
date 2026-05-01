[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Andrej Karpathy LLM Wiki medium note v0

## source metadata

- source_url: `https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5`
- source_title: `Andrej Karpathy’s LLM Wiki: Create your own knowledge base`
- source_author: `Urvil Joshi`
- source_type: `external article`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo`

## why this source matters

This article explains the "LLM wiki" pattern around Andrej Karpathy's recent post and gist.

The pattern is relevant to our space because it argues for:

- keeping raw sources immutable
- compiling them into a maintained wiki layer
- using a schema file such as `CLAUDE.md` or `AGENTS.md`
- treating ingest, query, and lint as recurring operations

This overlaps with our current concerns around:

- source vs derived layers
- structured intake
- reusable answer surfaces
- reinjection and maintenance

## core idea

The article's main claim is that knowledge work with LLMs should not depend only on repeated retrieval from raw source documents.

Instead, the system should:

1. keep raw source material as ground truth
2. let an LLM build and maintain a structured wiki layer
3. use a schema/config layer to constrain how ingest and query happen

The article frames this as a compile analogy:

- raw documents are like source code
- a maintained wiki is like a compiled artifact

The key promise is expensive ingest, cheaper later query.

## three-layer structure

The article presents a three-layer structure:

### layer 1. raw sources

- PDFs
- notes
- articles
- images

These remain immutable and are treated as source truth.

### layer 2. wiki

- concept pages
- entity pages
- overview pages
- index and log

This layer is rewritten and cross-linked by the LLM.

### layer 3. schema

- `CLAUDE.md`
- `AGENTS.md`

This layer tells the agent how to ingest, maintain, and answer from the wiki.

## three operations

The article reduces the operating pattern to:

### ingest

New source arrives.
The agent reads it, summarizes it, updates linked pages, and records new connections.

### query

The user asks questions against the maintained wiki rather than reopening all raw documents each time.

### lint

The agent audits the wiki for:

- contradictions
- orphan pages
- missing concepts
- stale areas

## article's comparison with rag

The article does not say LLM wiki replaces RAG universally.

Its distinction is roughly:

- RAG is better for large, changing corpora and precise chunk traceability
- LLM wiki is better for a bounded curated corpus where synthesis across sources matters more than per-query retrieval

The article also names a risk:

- hallucinations or misunderstandings can get baked into the wiki if maintenance is careless

So lint and source spot-checking remain important.

## relevance to our current space

This source is not a direct adoption instruction.

But it is structurally relevant because it reinforces several already-active pressures in our space:

- raw source and derived layer separation
- maintained intermediate artifact layer
- schema-driven agent behavior
- answer surfaces that can become durable assets
- periodic maintenance / contradiction checking

At the same time, our current space is not the same thing as a pure LLM wiki.

Our space still has:

- lower input organ
- bridge and packet layers
- runtime manifests and receipts
- observer and reread structures

So the article should be read as a useful pattern reference, not a direct architecture replacement.

## bounded judgment

Current bounded judgment:

- useful as a conceptual and structural reference
- especially relevant for source / wiki / schema separation
- not a direct instruction to replace our current runtime with a wiki-only model
- worth keeping as an external source for later mapping against our own memory and reinjection design
